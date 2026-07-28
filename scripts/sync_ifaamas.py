#!/usr/bin/env python3
"""Synchronize AAMAS metadata from the official IFAAMAS proceedings page."""

from __future__ import annotations

from datetime import datetime, timezone
from html.parser import HTMLParser
from http.client import RemoteDisconnected
import json
from pathlib import Path
import re
import sys
import tempfile
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SOURCES_PATH = ROOT / "data" / "sources.json"
PAPERS_DIR = ROOT / "data" / "papers"
PROVENANCE_DIR = ROOT / "data" / "provenance"
USER_AGENT = "AAMAS-Notes metadata sync (https://github.com/Endofthestars/AAMAS-Notes)"
MAX_ATTEMPTS = 5

TRACKS = {
    "K": "keynote",
    "R": "research",
    "A": "aaai",
    "B": "blue_sky",
    "C": "doctoral_consortium",
    "D": "demo",
    "J": "jaamas",
}
PAPER_ID_RE = re.compile(r"^[A-Z]{4}\d{4}\.pdf$", re.IGNORECASE)
PAGE_RE = re.compile(r"\(Page\s+(\d+)\)", re.IGNORECASE)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    temporary.replace(path)


def fetch_html(url: str) -> str:
    for attempt in range(MAX_ATTEMPTS):
        request = Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urlopen(request, timeout=60) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(charset, errors="replace")
        except HTTPError as exc:
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt == MAX_ATTEMPTS - 1:
                raise
            retry_after = exc.headers.get("Retry-After", "")
            delay = float(retry_after) if retry_after.isdigit() else 5.0 * (2**attempt)
            print(f"IFAAMAS HTTP {exc.code}; retrying in {delay:g}s", file=sys.stderr)
            time.sleep(delay)
        except (RemoteDisconnected, TimeoutError, URLError) as exc:
            if attempt == MAX_ATTEMPTS - 1:
                raise
            delay = 2.0 * (2**attempt)
            print(
                f"Transient IFAAMAS connection error ({type(exc).__name__}); "
                f"retrying in {delay:g}s",
                file=sys.stderr,
            )
            time.sleep(delay)
    raise RuntimeError("unreachable")


class ProceedingsParser(HTMLParser):
    """Extract paper-like entries while retaining the official track boundary."""

    def __init__(self, source_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.source_url = source_url
        self.current_track: str | None = None
        self.in_paragraph = False
        self.in_strong = False
        self.paragraph_text: list[str] = []
        self.title_text: list[str] = []
        self.pdf_href = ""
        self.records: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "a":
            anchor = attributes.get("name") or attributes.get("id")
            if anchor in TRACKS:
                self.current_track = TRACKS[anchor]
            href = attributes.get("href") or ""
            if self.in_paragraph and "../pdfs/" in href:
                filename = Path(urlparse(href).path).name
                if PAPER_ID_RE.match(filename):
                    self.pdf_href = href
        if tag == "p":
            self.in_paragraph = True
            self.paragraph_text = []
            self.title_text = []
            self.pdf_href = ""
        elif self.in_paragraph and tag == "br":
            self.paragraph_text.append("\n")
            if self.in_strong:
                self.title_text.append(" ")
        elif self.in_paragraph and tag == "strong":
            self.in_strong = True

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "strong":
            self.in_strong = False
        elif tag == "p" and self.in_paragraph:
            self._finish_paragraph()
            self.in_paragraph = False

    def handle_data(self, data: str) -> None:
        if not self.in_paragraph:
            return
        self.paragraph_text.append(data)
        if self.in_strong:
            self.title_text.append(data)

    def _finish_paragraph(self) -> None:
        if self.current_track is None:
            return
        text = "".join(self.paragraph_text)
        page_match = PAGE_RE.search(text)
        retracted = "retracted" in text.lower()
        if page_match is None or (not self.pdf_href and not retracted):
            return

        title = " ".join("".join(self.title_text).split())
        if not title:
            return
        page = page_match.group(1)
        author_text = text[page_match.end() :]
        authors: list[str] = []
        for line in author_text.splitlines():
            line = " ".join(line.replace("\xa0", " ").split())
            if not line:
                continue
            name = re.sub(r"\s*\(.*\)\s*$", "", line).strip()
            if name:
                authors.append(name)
        if not authors:
            return

        if self.pdf_href:
            filename = Path(urlparse(self.pdf_href).path).name
            official_id = Path(filename).stem.upper()
            editions = [urljoin(self.source_url, self.pdf_href)]
        else:
            official_id = f"RETRACTED-P{page}"
            editions = []

        self.records.append(
            {
                "id": f"ifaamas:2026:{official_id.lower()}",
                "conference": "AAMAS",
                "year": 2026,
                "title": title,
                "authors": authors,
                "track": self.current_track,
                "topics": ["unclassified"],
                "pages": page,
                "doi": "",
                "dblp_key": "",
                "dblp_url": "",
                "electronic_editions": editions,
                "official_id": official_id,
                "official_source": self.source_url,
                "publication_status": "retracted" if retracted else "active",
                "note_status": "metadata_only",
                "note_path": "",
            }
        )


def parse_proceedings(html: str, source_url: str) -> list[dict[str, Any]]:
    parser = ProceedingsParser(source_url)
    parser.feed(html)
    parser.close()
    records = parser.records
    seen: set[str] = set()
    for record in records:
        identifier = record["id"]
        if identifier in seen:
            raise RuntimeError(f"duplicate official paper identifier: {identifier}")
        seen.add(identifier)
    return sorted(records, key=lambda record: (int(record["pages"]), record["official_id"]))


def sync() -> tuple[Path, int]:
    sources = read_json(SOURCES_PATH)["sources"]
    source = next(
        (
            item
            for item in sources
            if item.get("provider") == "IFAAMAS" and int(item.get("year", 0)) == 2026
        ),
        None,
    )
    if source is None:
        raise RuntimeError("No IFAAMAS source configured for AAMAS 2026")

    source_url = str(source["url"])
    records = parse_proceedings(fetch_html(source_url), source_url)
    if not records:
        raise RuntimeError("IFAAMAS returned no AAMAS 2026 paper records")

    output = PAPERS_DIR / "AAMAS2026.jsonl"
    text = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records)
    atomic_write(output, text)

    track_counts: dict[str, int] = {}
    status_counts: dict[str, int] = {}
    for record in records:
        track_counts[record["track"]] = track_counts.get(record["track"], 0) + 1
        status = record["publication_status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    provenance = {
        "conference": "AAMAS",
        "year": 2026,
        "provider": source["provider"],
        "source_url": source_url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "record_count": len(records),
        "track_counts": dict(sorted(track_counts.items())),
        "publication_status_counts": dict(sorted(status_counts.items())),
    }
    atomic_write(
        PROVENANCE_DIR / "AAMAS2026.json",
        json.dumps(provenance, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    return output, len(records)


def main() -> int:
    output, count = sync()
    print(f"{output.relative_to(ROOT)}: {count} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
