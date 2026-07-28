# AAMAS Notes

面向 AAMAS（International Conference on Autonomous Agents and Multiagent
Systems）的可审计论文语料库。仓库将“官方元数据”“自动分类草稿”和“人工核验
笔记”分开维护，供 PaperCompass 的趋势分析、选题查新和研究方向评估使用。

## 配置范围

- DBLP 元数据源：AAMAS 2022–2025
- IFAAMAS 官方 proceedings：AAMAS 2026（等待 DBLP 编目后并入自动同步）
- 深度笔记优先级：多智能体规划/调度/资源分配，以及可信、安全、验证和工程
- 不在仓库中镜像论文 PDF

`data/papers/` 中出现相应年份文件才表示该届已完成首次全量同步；仅在
`data/sources.json` 中配置来源不代表数据已经抓取成功。

## 目录

```text
data/
  sources.json                 # 每届会议的权威元数据入口
  taxonomy.json                # AAMAS 专属主题分类
  papers/AAMAS2025.jsonl       # 一行一篇的规范化元数据
  provenance/AAMAS2025.json    # 本次抓取时间、来源和记录数
docs/
  index.md                     # 语料入口
templates/
  paper-note.md                # 单篇笔记模板
scripts/
  sync_dblp.py                 # DBLP 增量同步
  validate_repository.py       # 唯一 ID、字段、分类和状态校验
```

## 维护流程

1. `scripts/sync_dblp.py` 只更新书目元数据，不生成研究结论。
2. 新记录初始状态固定为 `metadata_only`、主题为 `unclassified`。
3. 自动分类后改为 `classified_draft`，必须保留分类依据。
4. 阅读原论文并核对实验数据后，才可改为 `reviewed`。
5. 所有自动同步和笔记修改通过 Pull Request 合并。

运行全部同步：

```bash
python3 scripts/sync_dblp.py
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests
```

只同步某一年：

```bash
python3 scripts/sync_dblp.py --year 2025
```

GitHub Actions 的手动入口也支持选择单个年份。每个年份使用独立的
`automation/dblp-sync-<year>` PR 分支，避免一次上游故障阻塞其他年份。

## 状态含义

| 状态 | 含义 |
|---|---|
| `metadata_only` | 仅确认题目、作者和书目标识符 |
| `classified_draft` | 已自动或人工分类，但尚未完成论文核验 |
| `note_draft` | 已有解读草稿，尚未完成复核 |
| `reviewed` | 已核对原论文、关键实验和局限 |

## 数据与版权

- DBLP 书目元数据以 CC0 提供；每个快照保留其导出 URL。
- IFAAMAS/ACM 论文版权仍归相应权利人。本仓库默认只保存元数据、链接和原创
  解读，不重新发布 PDF。
- 当前仓库尚未授予内容再利用许可；转为公开仓库前将单独确定原创笔记许可。

## 与 PaperCompass 集成

PaperCompass 应把 `data/papers/*.jsonl` 作为独立的 AAMAS 语料源，不能与
Paper-Notes 的会议计数静默合并。分析报告必须同时记录本仓库 commit 和同步时间。
