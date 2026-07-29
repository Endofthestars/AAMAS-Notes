#!/usr/bin/env python3
"""Generate MkDocs indexes from the canonical AAMAS JSONL records."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def load_records() -> list[dict]:
    records: list[dict] = []
    for path in sorted((ROOT / "data" / "papers").glob("AAMAS*.jsonl")):
        records.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines())
    return records


def load_topic_labels() -> dict[str, str]:
    taxonomy = json.loads((ROOT / "data" / "taxonomy.json").read_text(encoding="utf-8"))
    return taxonomy["topics"]


def frontmatter(title: str, description: str, *, hide_navigation: bool = False) -> str:
    hidden = "\nhide:\n  - toc\n  - navigation" if hide_navigation else ""
    return (
        "---\n"
        f'title: "{title}"\n'
        f'description: "{description}"\n'
        "tags:\n"
        '  - "AAMAS"\n'
        '  - "多智能体系统"\n'
        '  - "论文笔记"\n'
        f"{hidden}\n"
        "---\n"
    )


def write_home(records: list[dict], reviewed: list[dict], labels: dict[str, str]) -> None:
    years = sorted({record["year"] for record in records}, reverse=True)
    topic_count = Counter(
        topic for record in reviewed for topic in record["topics"] if topic != "unclassified"
    )
    cards: list[str] = []
    emoji = {2026: "🤖", 2025: "🧭", 2024: "🧠", 2023: "🕸️", 2022: "📚"}

    for year in years:
        year_records = [record for record in records if record["year"] == year]
        year_reviewed = [record for record in reviewed if record["year"] == year]
        topics = Counter(
            topic
            for record in year_reviewed
            for topic in record["topics"]
            if topic != "unclassified"
        )
        href = f"notes/{year}/" if (DOCS / "notes" / str(year) / "index.md").exists() else "notes/"
        tags = "".join(
            f'<a class="area-tag" href="{href}">{labels.get(topic, topic)} {count}</a>\n'
            for topic, count in topics.most_common(8)
        )
        if not tags:
            tags = '<span class="area-tag">元数据已收录 · reviewed 待建设</span>\n'
        cards.append(
            '<div class="conf-card" markdown>\n\n'
            f"### {emoji.get(year, '📄')} [AAMAS {year}]({href})\n\n"
            f'<div class="conf-count">{len(year_records)} 条元数据 · '
            f"{len(year_reviewed)} 篇 reviewed</div>\n\n"
            '<div class="area-groups"><div class="area-group">\n'
            '<div class="area-group-label">已审核主题</div>\n'
            f'<div class="area-tags">\n{tags}</div>\n'
            "</div></div>\n\n</div>"
        )

    body = (
        frontmatter(
            "AAMAS Paper Notes · 可审计多智能体论文解读",
            "AAMAS 2022–2026 官方元数据与正文级 reviewed 阅读笔记。",
            hide_navigation=True,
        )
        + "\n<!-- 由 scripts/generate_site_indexes.py 自动生成 -->\n\n"
        '<div class="hero" markdown>\n\n'
        "# 📚 AAMAS 论文解读\n\n"
        '<p class="hero-subtitle">Autonomous Agents · Multiagent Systems · '
        "每篇 reviewed 笔记均公开核验路径与证据边界。<br>"
        "覆盖 AAMAS 2022–2026，持续按批次更新。</p>\n\n"
        '<div class="hero-stats">\n'
        f'<div class="stat"><span class="stat-number">{len(records)}</span>'
        '<span class="stat-label">条论文元数据</span></div>\n'
        f'<div class="stat"><span class="stat-number">{len(reviewed)}</span>'
        '<span class="stat-label">篇 reviewed 笔记</span></div>\n'
        f'<div class="stat"><span class="stat-number">{len(topic_count)}</span>'
        '<span class="stat-label">个已审核主题</span></div>\n'
        "</div>\n\n"
        '<a class="github-link" href="notes/">开始阅读 reviewed 笔记</a>\n\n'
        "</div>\n\n---\n\n"
        '<div class="conf-grid" markdown>\n\n'
        + "\n\n".join(cards)
        + "\n\n</div>\n"
    )
    (DOCS / "index.md").write_text(body, encoding="utf-8")


def write_notes_indexes(reviewed: list[dict], labels: dict[str, str]) -> None:
    notes_root = DOCS / "notes"
    notes_root.mkdir(exist_ok=True)
    by_year = Counter(record["year"] for record in reviewed)
    overview = [
        frontmatter("Reviewed 笔记", "完成正文级证据核验的 AAMAS 论文笔记。"),
        "\n# Reviewed 笔记\n\n",
        "只有核对原论文、关键方法、实验或定理边界后，记录才进入本目录。\n\n",
    ]
    for year, count in sorted(by_year.items(), reverse=True):
        overview.append(f"- [AAMAS {year}](./{year}/)：{count} 篇\n")
    (notes_root / "index.md").write_text("".join(overview), encoding="utf-8")

    for year in sorted(by_year, reverse=True):
        year_records = sorted(
            (record for record in reviewed if record["year"] == year),
            key=lambda record: record["title"].casefold(),
        )
        topic_count = Counter(
            topic
            for record in year_records
            for topic in record["topics"]
            if topic != "unclassified"
        )
        pills = "".join(
            f'<span class="pill">{labels.get(topic, topic)} <b>{count}</b></span>\n'
            for topic, count in topic_count.most_common()
        )
        lines = [
            frontmatter(
                f"AAMAS {year} reviewed 论文笔记",
                f"AAMAS {year} 已完成正文级核验的论文笔记。",
            ),
            f"\n# AAMAS {year} reviewed 论文笔记\n\n",
            '<div class="conf-index" markdown>\n\n',
            '<div class="conf-stats-bar">\n',
            f'<div class="cs-item"><span class="cs-num">{len(year_records)}</span>'
            '<span class="cs-lab">reviewed 笔记</span></div>\n',
            f'<div class="cs-item"><span class="cs-num">{len(topic_count)}</span>'
            '<span class="cs-lab">研究主题</span></div>\n',
            '<div class="cs-item"><span class="cs-num">正文级</span>'
            '<span class="cs-lab">证据核验</span></div>\n',
            "</div>\n\n",
            "## 研究主题\n\n",
            f'<div class="conf-pills">\n{pills}</div>\n\n',
            "## 全部笔记\n\n",
        ]
        for record in year_records:
            slug = Path(record["note_path"]).stem
            authors = ", ".join(record["authors"])
            topics = " · ".join(labels.get(topic, topic) for topic in record["topics"])
            lines.append(
                f"**[{record['title']}](./{slug}.md)**\n"
                f": {authors} · {record['track']} · {topics}\n\n"
            )
        lines.append("</div>\n")
        year_dir = notes_root / str(year)
        year_dir.mkdir(exist_ok=True)
        (year_dir / "index.md").write_text("".join(lines), encoding="utf-8")


def main() -> None:
    records = load_records()
    reviewed = [record for record in records if record["note_status"] == "reviewed"]
    labels = load_topic_labels()
    write_notes_indexes(reviewed, labels)
    write_home(records, reviewed, labels)
    print(f"Generated Paper Notes indexes for {len(records)} records / {len(reviewed)} reviewed")


if __name__ == "__main__":
    main()
