---
title: "Active Evaluation of General Agents: Problem Definition and Comparison of Baseline Algorithms"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "game_theory_mechanism"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PUBN4692.pdf"
preprint_url: "https://arxiv.org/abs/2601.07651"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["ranking_ground_truth_assumption", "simulated_online_evaluation", "cross_task_score_aggregation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Active Evaluation of General Agents: Problem Definition and Comparison of Baseline Algorithms

## 一句话总结

本文将多任务 agent 评估改写为在线主动采样：每轮选择一个任务和一对 agent 取样分数、更新总排名，并用覆盖不同 top-$k$ 偏好的累计排名误差来比较评估算法的样本效率。

## 方法与证据

- 问题包含 $n$ 个任务、$m$ 个 agent 以及随机得分机制；每轮算法选择任务和两名 agent、取得一对分数后输出新排名（§2–3、Algorithm 1）。这评估的是“如何采样并排序”，不是训练被评估的 agent。
- Generalized Top-$k$ Ranking Error（GRE）把 top-$k$ 成员识别误差和这些成员的归一化 Kendall-tau 排名误差加权；Average GRE（AGRE）再对采样轮次取平均，因此会同时惩罚早期和后期的错误（§3.1）。指标需要一个 ground-truth ranking；真实数据中作者用最小化任务排名平均 Kendall-tau 距离的 Kemeny ranking 作为估计目标。
- 比较对象包括 UniformAveraging、BasicUCB、Batch/Online Elo、Soft Condorcet Optimization（SCO）、Copeland、Ranked Pairs、Maximal Lotteries、Nash Averaging 和 Proportional Representation 等；其中部分方法仅均匀选任务/agent，部分把 social-choice 或零和元博弈算法改成在线形式（§4、Table 1）。
- 合成实验使用 $m=8,n=50$ 的 Mallows/Plackett–Luce 型任务排名和正态分数。低任务变异时，UniformAveraging、BasicUCB、BatchElo 等早期误差下降快；任务变异更高时，Proportional Representation 在该设定中更突出。Nash averaging 的任务对手可偏向离全局排名很远的任务，导致过拟合（§5.1、Table 2、Figure 3）。
- Atari 实验把 Agent57 表的 8 个 agent、57 个游戏的历史均值/标准差视为正态得分生成器，并按游戏线性归一化后模拟在线查询，不是重新运行 Atari 训练或真实交互（§5.2.1）。在这一模拟中 BatchSCO 的 AGRE 最低，OnlineSCO 次之；BatchElo 仍是稳健基线但被 SCO 明显超过（§5.2.1、Table 3）。

## 局限与复现

- AGRE 的“正确”参考排名在合成数据中由生成过程给出，在 Atari 中则由 Kemeny 式估计构造；不同的全局效用、任务权重或归一化会改变结论，不能把它当作唯一客观真值。
- Atari 部分只从已有 Agent57 统计量采样正态分数，未覆盖非正态回报、agent/任务相关性、动态成本、失败重试或真实评测基础设施的噪声。
- Elo/SCO 的优劣在低/高任务变异和合成/Atari 间发生变化。论文没有给出跨所有一般 agent benchmark 的最优算法保证，作者也把自适应 task selection 视为后续工作（§7）。
- 复现须固定任务排名/得分生成器、随机种子、$k$、轮次数、score normalization、Kemeny ground-truth 推断和各方法的 batch/online 更新细节；报告整条 GRE 曲线，而非仅报告终点或单一 top-$k$。

## 与 AAMAS 的关系与核验说明

该文研究如何以有限评测预算比较多任务 agent，连接 agent evaluation、主动学习与社会选择式聚合。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2601.07651) 核对了在线循环、AGRE 定义、算法范围和 Atari 模拟的证据边界。
