#!/usr/bin/env python3
"""Synchronize normalized AAMAS bibliographic metadata from DBLP."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from http.client import RemoteDisconnected
import json
from pathlib import Path
import sys
import tempfile
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SOURCES_PATH = ROOT / "data" / "sources.json"
PAPERS_DIR = ROOT / "data" / "papers"
PROVENANCE_DIR = ROOT / "data" / "provenance"
USER_AGENT = "AAMAS-Notes metadata sync (https://github.com/Endofthestars/AAMAS-Notes)"
PAGE_SIZE = 100
REQUEST_DELAY_SECONDS = 1.5
MAX_ATTEMPTS = 5
CURATED_FIELDS = (
    "track",
    "topics",
    "note_status",
    "note_path",
    "reviewed_by",
    "reviewed_at",
)


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


def fetch_json(url: str) -> dict[str, Any]:
    for attempt in range(MAX_ATTEMPTS):
        request = Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urlopen(request, timeout=60) as response:
                return json.load(response)
        except HTTPError as exc:
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt == MAX_ATTEMPTS - 1:
                raise
            retry_after = exc.headers.get("Retry-After", "")
            delay = float(retry_after) if retry_after.isdigit() else 5.0 * (2**attempt)
            print(f"DBLP HTTP {exc.code}; retrying in {delay:g}s", file=sys.stderr)
            time.sleep(delay)
        except (RemoteDisconnected, TimeoutError, URLError) as exc:
            if attempt == MAX_ATTEMPTS - 1:
                raise
            delay = 2.0 * (2**attempt)
            print(
                f"Transient DBLP connection error ({type(exc).__name__}); "
                f"retrying in {delay:g}s",
                file=sys.stderr,
            )
            time.sleep(delay)
    raise RuntimeError("unreachable")


def page_url(url: str, first: int) -> str:
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query["h"] = str(PAGE_SIZE)
    query["f"] = str(first)
    query["format"] = "json"
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def fetch_all_hits(url: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    first = 0
    total: int | None = None
    while total is None or first < total:
        payload = fetch_json(page_url(url, first))
        result = payload.get("result", {}).get("hits", {})
        page = [hit for hit in as_list(result.get("hit")) if isinstance(hit, dict)]
        total = int(result.get("@total", len(page)))
        if not page:
            break
        hits.extend(page)
        first += len(page)
        if first < total:
            time.sleep(REQUEST_DELAY_SECONDS)
    if total is not None and len(hits) != total:
        raise RuntimeError(f"DBLP pagination incomplete: expected {total}, received {len(hits)}")
    return hits


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def text_value(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("text", "")).strip()
    return str(value or "").strip()


def normalize_hit(hit: dict[str, Any], expected_year: int) -> dict[str, Any] | None:
    info = hit.get("info", {})
    key = text_value(info.get("key"))
    title = text_value(info.get("title")).rstrip(".")
    year_text = text_value(info.get("year"))
    if not key or not title or not year_text.isdigit():
        return None
    year = int(year_text)
    if year != expected_year:
        return None

    author_items = as_list(info.get("authors", {}).get("author"))
    authors = [text_value(author) for author in author_items]
    authors = [author for author in authors if author]

    ee = [text_value(item) for item in as_list(info.get("ee"))]
    ee = sorted({item for item in ee if item})
    doi = next((item.removeprefix("https://doi.org/") for item in ee if "doi.org/" in item), "")
    dblp_url = text_value(info.get("url"))
    if dblp_url and dblp_url.startswith("db/"):
        dblp_url = f"https://dblp.org/{dblp_url}"

    return {
        "id": f"dblp:{key}",
        "conference": "AAMAS",
        "year": year,
        "title": title,
        "authors": authors,
        "track": "unclassified",
        "topics": ["unclassified"],
        "pages": text_value(info.get("pages")),
        "doi": doi,
        "dblp_key": key,
        "dblp_url": dblp_url,
        "electronic_editions": ee,
        "note_status": "metadata_only",
        "note_path": ""
    }


def preserve_curation(
    records: list[dict[str, Any]],
    output: Path,
) -> list[dict[str, Any]]:
    if not output.is_file():
        return records
    previous = {
        record["id"]: record
        for line in output.read_text(encoding="utf-8").splitlines()
        for record in [json.loads(line)]
        if record.get("id")
    }
    for record in records:
        old = previous.get(record["id"], {})
        for field in CURATED_FIELDS:
            if field in old:
                record[field] = old[field]
    return records


def sync_source(source: dict[str, Any]) -> tuple[Path, int]:
    year = int(source["year"])
    hits = fetch_all_hits(source["url"])
    records = [
        record
        for hit in hits
        if isinstance(hit, dict)
        for record in [normalize_hit(hit, year)]
        if record is not None
    ]
    records.sort(key=lambda record: record["dblp_key"])
    if not records:
        raise RuntimeError(f"DBLP returned no AAMAS {year} records")

    output = PAPERS_DIR / f"AAMAS{year}.jsonl"
    records = preserve_curation(records, output)
    text = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records)
    atomic_write(output, text)

    provenance = {
        "conference": "AAMAS",
        "year": year,
        "provider": source["provider"],
        "source_url": source["url"],
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "record_count": len(records)
    }
    atomic_write(
        PROVENANCE_DIR / f"AAMAS{year}.json",
        json.dumps(provenance, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    return output, len(records)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year", type=int, action="append", help="year to sync; repeatable")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = read_json(SOURCES_PATH)
    requested = set(args.year or [])
    sources = [
        source
        for source in config["sources"]
        if source.get("provider") == "DBLP"
        and (not requested or int(source["year"]) in requested)
    ]
    if requested and requested != {int(source["year"]) for source in sources}:
        missing = sorted(requested - {int(source["year"]) for source in sources})
        print(f"No DBLP source configured for years: {missing}", file=sys.stderr)
        return 2
    failures: list[str] = []
    for source in sources:
        try:
            output, count = sync_source(source)
        except Exception as exc:
            year = int(source["year"])
            failures.append(f"AAMAS {year}: {type(exc).__name__}: {exc}")
            continue
        print(f"{output.relative_to(ROOT)}: {count} records", flush=True)
    if failures:
        print("One or more yearly sources failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
