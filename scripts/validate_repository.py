#!/usr/bin/env python3
"""Validate AAMAS Notes metadata, taxonomy, and review-state invariants."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VALID_STATUSES = {"metadata_only", "classified_draft", "note_draft", "reviewed"}
VALID_PUBLICATION_STATUSES = {"active", "retracted"}
REQUIRED_REVIEW_FRONTMATTER = {
    "note_status",
    "review_route",
    "risk_level",
    "escalation_model",
    "escalation_reason",
    "generated_by",
    "reviewed_by",
    "reviewed_at",
}
REQUIRED_FIELDS = {
    "id",
    "conference",
    "year",
    "title",
    "authors",
    "track",
    "topics",
    "dblp_key",
    "note_status",
    "note_path",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


def validate() -> list[str]:
    errors: list[str] = []
    taxonomy = load_json(ROOT / "data" / "taxonomy.json")
    topics = set(taxonomy["topics"])
    tracks = set(taxonomy["tracks"])
    seen_ids: dict[str, str] = {}
    seen_keys: dict[str, str] = {}
    seen_dois: dict[str, str] = {}
    seen_note_paths: dict[str, str] = {}

    for path in sorted((ROOT / "data" / "papers").glob("AAMAS*.jsonl")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            label = f"{path.relative_to(ROOT)}:{line_number}"
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{label}: invalid JSON: {exc}")
                continue
            missing = sorted(REQUIRED_FIELDS - set(record))
            if missing:
                errors.append(f"{label}: missing fields {missing}")
                continue
            if record["conference"] != "AAMAS":
                errors.append(f"{label}: conference must be AAMAS")
            if record["track"] not in tracks:
                errors.append(f"{label}: unknown track {record['track']!r}")
            unknown_topics = sorted(set(record["topics"]) - topics)
            if unknown_topics:
                errors.append(f"{label}: unknown topics {unknown_topics}")
            if record["note_status"] not in VALID_STATUSES:
                errors.append(f"{label}: invalid note_status {record['note_status']!r}")
            if record.get("publication_status", "active") not in VALID_PUBLICATION_STATUSES:
                errors.append(
                    f"{label}: invalid publication_status "
                    f"{record.get('publication_status')!r}"
                )
            if not isinstance(record["authors"], list) or not record["authors"]:
                errors.append(f"{label}: authors must be a non-empty list")
            if record["note_status"] == "reviewed":
                note_path = ROOT / record["note_path"]
                if not record["note_path"] or not note_path.is_file():
                    errors.append(f"{label}: reviewed record must reference an existing note")
                elif note_path.is_file():
                    frontmatter = load_frontmatter(note_path)
                    missing_review_fields = sorted(
                        field
                        for field in REQUIRED_REVIEW_FRONTMATTER
                        if not frontmatter.get(field, "").strip()
                    )
                    if missing_review_fields:
                        errors.append(
                            f"{label}: reviewed note missing front matter "
                            f"{missing_review_fields}"
                        )
                    if frontmatter.get("note_status") != "reviewed":
                        errors.append(
                            f"{label}: reviewed record references a note whose "
                            "note_status is not reviewed"
                        )
                    escalation_model = frontmatter.get("escalation_model", "")
                    if (
                        escalation_model
                        and escalation_model != "none"
                        and not frontmatter.get("escalation_verdict", "").strip()
                    ):
                        errors.append(
                            f"{label}: escalated review must include "
                            "escalation_verdict"
                        )
                if not str(record.get("reviewed_by", "")).strip():
                    errors.append(f"{label}: reviewed record must name its reviewer")
                if not str(record.get("reviewed_at", "")).strip():
                    errors.append(f"{label}: reviewed record must include its review date")
            note_path_value = str(record["note_path"]).strip()
            if note_path_value:
                if note_path_value in seen_note_paths:
                    errors.append(
                        f"{label}: duplicate note_path; "
                        f"first seen at {seen_note_paths[note_path_value]}"
                    )
                else:
                    seen_note_paths[note_path_value] = label

            for field, seen in (
                ("id", seen_ids),
                ("dblp_key", seen_keys),
                ("doi", seen_dois),
            ):
                value = str(record.get(field, "")).strip().lower()
                if not value:
                    continue
                if value in seen:
                    errors.append(f"{label}: duplicate {field}; first seen at {seen[value]}")
                else:
                    seen[value] = label
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    paper_files = list((ROOT / "data" / "papers").glob("AAMAS*.jsonl"))
    print(f"Repository validation passed ({len(paper_files)} metadata files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
