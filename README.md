# AAMAS Notes

面向 AAMAS（International Conference on Autonomous Agents and Multiagent
Systems）的可审计论文语料库。仓库将“官方元数据”“自动分类草稿”和“人工核验
笔记”分开维护，供 PaperCompass 的趋势分析、选题查新和研究方向评估使用。

## 配置范围

- DBLP 元数据源：AAMAS 2022–2025
- IFAAMAS 官方 proceedings：AAMAS 2026（DBLP 编目前使用官方目录）
- 首次快照：2022–2026 共 2,419 条会议内容记录
- 首批正文级核验：3 篇 `reviewed` 笔记
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
  review-routing.md            # Spark 主导、Sol 风险升级策略
templates/
  paper-note.md                # 单篇笔记模板
scripts/
  sync_dblp.py                 # DBLP 增量同步
  sync_ifaamas.py              # IFAAMAS 官方 proceedings 同步
  validate_repository.py       # 唯一 ID、字段、分类和状态校验
```

## 维护流程

1. 同步脚本只更新官方书目元数据，不生成研究结论。
2. 新记录初始状态固定为 `metadata_only`、主题为 `unclassified`。
3. 自动分类后改为 `classified_draft`，必须保留分类依据。
4. 阅读原论文并核对实验数据后，才可改为 `reviewed`。
5. 所有自动同步和笔记修改通过 Pull Request 合并。

同步器只刷新官方字段，并保留 `topics`、`note_status`、`note_path`、审核人和审核
日期等策展字段，避免定期同步覆盖人工或模型辅助整理结果。

运行全部同步：

```bash
python3 scripts/sync_dblp.py
python3 scripts/sync_ifaamas.py
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests
```

只同步某一年（2022–2025）：

```bash
python3 scripts/sync_dblp.py --year 2025
```

2026 使用 IFAAMAS 官方目录，并明确保留官方撤稿标记：

```bash
python3 scripts/sync_ifaamas.py
```

GitHub Actions 的手动入口支持选择单个年份。每个年份使用独立的
`automation/metadata-sync-<year>` 分支，避免一次上游故障阻塞其他年份。出于
最小权限原则，Actions 只推送同步分支，不创建或批准 PR；维护者检查后运行：

```bash
gh pr create \
  --base main \
  --head automation/metadata-sync-2026 \
  --title "chore(data): sync AAMAS metadata (2026)"
```

## 状态含义

| 状态 | 含义 |
|---|---|
| `metadata_only` | 仅确认题目、作者和书目标识符 |
| `classified_draft` | 已自动或人工分类，但尚未完成论文核验 |
| `note_draft` | 已有解读草稿，尚未完成复核 |
| `reviewed` | 已核对原论文、关键实验和局限 |

`publication_status` 独立记录官方发布状态；撤稿记录保留在快照中并标记为
`retracted`，不会静默删除或进入普通论文分析。

`reviewed` 表示笔记中声明的核验范围已经完成，不自动等同于人类领域专家签字或
独立复现实验。每篇笔记必须公开 `generated_by`、`reviewed_by`、`reviewed_at`
以及尚未核验的边界。

模型审核默认遵循 [Spark 双通道路由](docs/review-routing.md)：Spark 分别完成草稿
和独立反向 QA；Sol 只处理冲突、高风险主张和滚动 10% 抽样。长期目标是让
80%–90% 的模型工作量由 Spark 完成。

## 数据与版权

- DBLP 书目元数据以 CC0 提供；每个快照保留其导出 URL。
- IFAAMAS/ACM 论文版权仍归相应权利人。本仓库默认只保存元数据、链接和原创
  解读，不重新发布 PDF。
- 当前仓库尚未授予内容再利用许可；转为公开仓库前将单独确定原创笔记许可。

## 与 PaperCompass 集成

PaperCompass 应把 `data/papers/*.jsonl` 作为独立的 AAMAS 语料源，不能与
Paper-Notes 的会议计数静默合并。分析报告必须同时记录本仓库 commit 和同步时间。
