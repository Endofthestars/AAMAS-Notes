# AAMAS 论文语料

本目录保存经过人工整理或审核的阅读笔记。规范化书目元数据位于
`data/papers/`。

## 建设顺序

1. AAMAS 2022–2026 全量元数据（已建立首次快照）
2. 多智能体规划、调度与资源分配
3. 安全、验证、运行时保障与智能体工程
4. 其余 AAMAS 专属方向

当前已有 8 篇笔记完成正文级证据核验；其余记录仍保持 `metadata_only`。

## 首批 reviewed 笔记

| 论文 | 方向 | 核验范围 |
|---|---|---|
| [The Multi-Agent Off-Switch Game](notes/2026/multi-agent-off-switch-game.md) | 安全、博弈机制 | 定义、定理、构造、局限 |
| [Contrastive Explanations of BDI Agents](notes/2026/contrastive-explanations-bdi-agents.md) | 可解释性、智能体工程 | 方法、人因实验、局限 |
| [Scaling Multi-Agent Epistemic Planning through GNN-Derived Heuristics](notes/2026/gnn-epistemic-planning-heuristics.md) | 认知规划、学习启发式 | 方法、Tables 1–5、局限 |
| [µACP](notes/2026/muacp-resource-constrained-agent-communication.md) | 通信、形式化推理 | 定理、验证、理论条件 |
| [Multi UAVs Preflight Planning](notes/2026/multi-uav-preflight-planning.md) | 规划调度、应用 | 建模、Table 2–3、局限 |
| [ReAcTree](notes/2026/reactree-llm-agent-planning.md) | 生成式智能体、规划 | 方法、Tables 1–4、失败分析 |
| [Multi-Robot BDI Architecture](notes/2026/multi-robot-bdi-continuous-planning.md) | 具身机器人、智能体工程 | 架构、四配置仿真、局限 |
| [Three-Layer RL Task Allocation](notes/2026/three-layer-rl-task-allocation.md) | 协调、规划调度 | 方法、Table 2、可比性边界 |

首批三篇采用 Spark 初稿和 Sol 复核。2026-pilot-01 的五篇采用 Spark 双轮独立审校；
其中 µACP 的高风险定理条件额外由 Terra 定点复核。它们不是人类领域专家签字，也不代表
完成独立实验复现。
