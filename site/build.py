#!/usr/bin/env python3
"""Build the small, dependency-free AAMAS Notes reading site."""

from __future__ import annotations

import html
import json
import re
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "_site"

def frontmatter_and_body(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    _, raw, body = text.split("---", 2)
    fields = {}
    for line in raw.splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields, body.strip()

def inline(value: str) -> str:
    value = html.escape(value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    return re.sub(r"\[([^]]+)\]\(([^ )]+)\)", r'<a href="\2">\1</a>', value)

def markdown(body: str) -> str:
    out: list[str] = []
    in_list = in_table = False
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            if in_list: out.append("</ul>"); in_list = False
            if in_table: out.append("</tbody></table>"); in_table = False
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(set(cell) <= {"-", ":"} for cell in cells): continue
            if not in_table: out.append("<table><tbody>"); in_table = True
            out.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells) + "</tr>")
        elif stripped.startswith("### "): out.append(f"<h3>{inline(stripped[4:])}</h3>")
        elif stripped.startswith("## "): out.append(f"<h2>{inline(stripped[3:])}</h2>")
        elif stripped.startswith("# "): out.append(f"<h1>{inline(stripped[2:])}</h1>")
        elif re.match(r"(?:[-*]|\d+\.)\s+", stripped):
            if not in_list: out.append("<ul>"); in_list = True
            out.append(f"<li>{inline(re.sub(r'^(?:[-*]|\d+\.)\s+', '', stripped))}</li>")
        elif stripped.startswith("> "): out.append(f"<blockquote>{inline(stripped[2:])}</blockquote>")
        else: out.append(f"<p>{inline(stripped)}</p>")
    if in_list: out.append("</ul>")
    if in_table: out.append("</tbody></table>")
    return "\n".join(out)

def layout(title: str, content: str, description: str = "") -> str:
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · AAMAS Notes</title><meta name="description" content="{html.escape(description)}"><link rel="stylesheet" href="/AAMAS-Notes/assets/site.css"></head><body><header><a class="brand" href="/AAMAS-Notes/">AAMAS <span>Notes</span></a><nav><a href="/AAMAS-Notes/#notes">已审核笔记</a><a href="https://github.com/Endofthestars/AAMAS-Notes">GitHub</a></nav></header><main>{content}</main><footer>基于官方 AAMAS 元数据与原创核验笔记构建 · 不镜像论文 PDF</footer></body></html>"""

def load_records() -> list[dict]:
    records: list[dict] = []
    for path in sorted((ROOT / "data" / "papers").glob("AAMAS*.jsonl")):
        records.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines())
    return records

def main() -> None:
    if OUTPUT.exists(): shutil.rmtree(OUTPUT)
    (OUTPUT / "assets").mkdir(parents=True)
    records = load_records()
    reviewed = sorted((r for r in records if r["note_status"] == "reviewed"), key=lambda r: r["title"].lower())
    topics = Counter(t for r in records for t in r["topics"] if t != "unclassified")
    cards = []
    for record in reviewed:
        slug = Path(record["note_path"]).with_suffix(".html").relative_to("docs")
        tags = "".join(f'<span class="tag">{html.escape(t.replace("_", " "))}</span>' for t in record["topics"])
        cards.append(f'<article class="card" data-search="{html.escape((record["title"] + " " + " ".join(record["topics"])).lower())}"><div class="card-meta">AAMAS {record["year"]} · {html.escape(record["track"])}</div><h2><a href="/AAMAS-Notes/{slug.as_posix()}">{html.escape(record["title"])}</a></h2><p>{html.escape(", ".join(record["authors"]))}</p><div>{tags}</div><small>审核：{html.escape(record.get("reviewed_at", ""))}</small></article>')
    topic_summary = "".join(f'<span class="tag">{html.escape(t.replace("_", " "))} · {n}</span>' for t, n in topics.most_common(8))
    home = f'''<section class="hero"><p class="eyebrow">AUDITABLE AAMAS CORPUS</p><h1>把论文目录，变成可核验的阅读路径。</h1><p>参考 PaperNote 的“主题索引 → 论文 → 笔记”结构，AAMAS Notes 只公开元数据、官方链接与原创审核笔记。</p><div class="stats"><div><b>{len(records):,}</b><span>论文元数据</span></div><div><b>{len(reviewed)}</b><span>已审核笔记</span></div><div><b>2022–2026</b><span>覆盖年份</span></div></div></section><section class="topics"><h2>研究主题</h2><div>{topic_summary}</div></section><section id="notes"><div class="section-title"><div><p class="eyebrow">REVIEWED READING</p><h2>已审核笔记</h2></div><input id="search" type="search" placeholder="搜索题目或主题"></div><div class="grid" id="cards">{"".join(cards)}</div></section><script>document.querySelector('#search').addEventListener('input',e=>document.querySelectorAll('.card').forEach(c=>c.hidden=!c.dataset.search.includes(e.target.value.toLowerCase())));</script>'''
    (OUTPUT / "index.html").write_text(layout("AAMAS Notes", home, "AAMAS 可审计论文笔记库"), encoding="utf-8")
    for record in reviewed:
        meta, body = frontmatter_and_body(ROOT / record["note_path"])
        destination = OUTPUT / Path(record["note_path"]).with_suffix(".html").relative_to("docs")
        destination.parent.mkdir(parents=True, exist_ok=True)
        links = f'<p class="links"><a href="{html.escape(meta.get("pdf_url", "#"))}">官方 PDF</a> <a href="{html.escape(meta.get("official_url", "#"))}">会议目录</a></p>'
        audit = f'<aside><b>审核信息</b><br>路线：{html.escape(meta.get("review_route", ""))}<br>风险：{html.escape(meta.get("risk_level", ""))}<br>审核人：{html.escape(meta.get("reviewed_by", ""))}<br>日期：{html.escape(meta.get("reviewed_at", ""))}</aside>'
        page = f'<a class="back" href="/AAMAS-Notes/">← 全部笔记</a>{links}<article class="note">{markdown(body)}</article>{audit}'
        destination.write_text(layout(record["title"], page, record["title"]), encoding="utf-8")
    shutil.copy2(ROOT / "site" / "site.css", OUTPUT / "assets" / "site.css")

if __name__ == "__main__": main()
