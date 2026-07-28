# AAMAS 论文语料

本目录保存经过人工整理或审核的阅读笔记。规范化书目元数据位于
`data/papers/`。

## 建设顺序

1. AAMAS 2022–2026 全量元数据（已建立首次快照）
2. 多智能体规划、调度与资源分配
3. 安全、验证、运行时保障与智能体工程
4. 其余 AAMAS 专属方向

当前已有 3 篇笔记完成正文级证据核验；其余记录仍保持 `metadata_only`。

## 首批 reviewed 笔记

| 论文 | 方向 | 核验范围 |
|---|---|---|
| [The Multi-Agent Off-Switch Game](notes/2026/multi-agent-off-switch-game.md) | 安全、博弈机制 | 定义、定理、构造、局限 |
| [Contrastive Explanations of BDI Agents](notes/2026/contrastive-explanations-bdi-agents.md) | 可解释性、智能体工程 | 方法、人因实验、局限 |
| [Scaling Multi-Agent Epistemic Planning through GNN-Derived Heuristics](notes/2026/gnn-epistemic-planning-heuristics.md) | 认知规划、学习启发式 | 方法、Tables 1–5、局限 |

这些笔记由 `GPT-5.3-Codex-Spark` 生成初稿，再由 Codex GPT-5.6 Sol 对官方 PDF
中的方法、主要结果、比较与局限逐项复核。它们不是人类领域专家签字，也不代表完成
独立实验复现。
