---
title: "Scaling Multi-Agent Epistemic Planning through GNN-Derived Heuristics"
conference: "AAMAS"
year: 2026
track: "research"
topics:
  - "planning_scheduling"
  - "argumentation_reasoning"
dblp_key: ""
doi: "10.65109/QMRY9661"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QMRY9661.pdf"
code_url: "https://github.com/FrancescoFabiano/deep"
note_status: "reviewed"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.6 Sol)"
reviewed_at: "2026-07-28"
---

# Scaling Multi-Agent Epistemic Planning through GNN-Derived Heuristics

## 一句话总结

论文把多智能体认知状态的 Kripke 图编码交给 GNN 学习“距最近目标的距离”，以此引导
epistemic planner 搜索；它显著减少多数基准上的展开节点，但求解数和运行时间尚未稳定
超过 BFS，当前更接近可行性验证。

## 研究问题与设定

Multi-Agent Epistemic Planning（MEP）同时表示真实世界和嵌套信念，状态是 pointed
Kripke structure，搜索空间与公式检查成本很高。作者希望学习一个近似完美启发式：
给定 e-state 及目标，预测到最近目标状态的距离，并在 `deep`/EFP 求解器中用于
Heuristics-First Search（HFS）。

## 方法

1. 把 Kripke 状态转换成带节点和智能体关系边的图，并比较 mapping、hash、bitmask
   三种节点编码；另加目标节点，使估计依赖当前目标。
2. 对训练问题执行有深度上限的随机化 DFS，加入概率剪枝、节点上限和重复状态检查；
   从目标状态回溯，为可达状态标注最近目标距离。
3. 丢弃不可达状态、限制各距离桶样本数并归一化距离。
4. 使用两层 GINEConv、mean pooling 和残差回归头，以 MSE/AdamW 训练。
5. 推理时以 GNN 预测值引导 HFS；HFS* 再加入当前深度。由于学习启发式不保证
   admissible，作者明确不把 HFS* 称为 A*。

## 实验与证据

聚合的 Nodes、Time 和 Length 只在各比较方法都解出的实例上计算，解读时不能忽略
Solved Inst. 的差异。

| 结论 | 证据位置 | 核验状态 |
|---|---|---|
| hash 在三种编码中取得 75/79 solved、45 个聚合节点和 871 ms，整体优于 map/mask | Table 1，p.101 | 已核对数值 |
| HFS* 解出 75/79，HFS 解出 49/79；聚合节点分别为 17 与 18 | Table 2，p.101 | 已核对；未把差值误写成相对提升率 |
| 全 Test set 上 GNN 解出 59/66、BFS 61/66，但聚合节点为 64 对 242 | Table 3，p.103 | 已核对收益与代价 |
| CC-GR 跨域模型与 BFS 均解出 55/59；节点 288 对 389，但时间 4,116 ms 对 1,384 ms | Table 4，p.103 | 已核对 |
| 按 solved 指标，GNN 为 64/75，高于列出的四个 H-EFP 单启发式 | Table 5，p.103 | 已核对；正文称其为互补而非替代 |
| GR 域中 GNN 解题数低于 BFS，且当前无 batch inference，运行时间不具竞争力 | §4.3、§5，pp.102–103 | 已核对负结果 |

## 主要贡献

1. 给出从 Kripke e-state 到 GNN 输入的三种编码与目标条件化方案。
2. 建立自动生成“状态—目标距离”训练对的流水线。
3. 把学习距离集成进可运行的 MEP 求解器，并公开 `deep` 代码。
4. 用节点、时间、计划长度和求解实例数呈现学习启发式的收益与限制。

## 局限与威胁

论文明确说明：

- 当前 GNN 推理没有 CUDA/batch 搜索集成，运行时间不具竞争力；
- AL 的学习信号弱，GR 的有效计划稀疏，GNN 在这些域中收益有限；
- 数据生成和 HFS/GNN 仍是 proof of concept，MCTS、portfolio 与在线学习留作未来工作；
- 完整域参数、超参数及实验表主要位于扩展版附录。

我们的额外判断：

- 正文主要报告聚合趋势，没有给出跨随机种子显著性检验；
- GNN 在 Table 3 少解出两个实例，不能只凭节点指标声称全面优于 BFS；
- 代码公开不等同于本文精确 commit、模型权重和训练集快照已固定。

## 与 AAMAS 研究方向的关系

该工作直接属于 `planning_scheduling`，同时涉及多智能体信念表示和自动推理。对
PaperCompass 的启示是：学习型启发式最有希望作为传统启发式 portfolio 的补充，而非
仅以平均节点减少就替换完备的搜索基线。

## 复现信息

- 官方 PDF SHA-256：`fca7fa4b48892383692c8c3667a0f07186ae6bfd1cbc090e8445fbc0b59d38aa`
- DOI：<https://doi.org/10.65109/QMRY9661>
- 代码：<https://github.com/FrancescoFabiano/deep>
- 环境：Intel i9-13900H、64 GB RAM、NVIDIA RTX 4070 8 GB；超时 600 秒
- 框架：PyTorch、PyTorch Geometric、GINEConv、AdamW
- 未核验项：代码 commit、扩展版附录、训练数据快照及端到端重跑
- 当前核验级别：`SOURCE_METHOD_RESULTS_LIMITATIONS_VERIFIED`

## 核验说明

Spark 负责首次结构化阅读；复核阶段重新读取了 Tables 1–5、指标口径和 Limitations，
并纠正了草稿中容易把“节点更少”写成“整体性能更好”的倾向。尚未复现实验运行，因此
这里的 `reviewed` 是论文证据核验，不是结果复现认证。
