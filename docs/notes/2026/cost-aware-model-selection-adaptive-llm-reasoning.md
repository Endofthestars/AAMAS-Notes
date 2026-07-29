---
title: "Cost-Aware Model Selection and Adaptive Reasoning in Large Language Models via Online Learning"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["generative_agents", "agent_engineering", "resource_allocation", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/WSXD8440"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WSXD8440.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04x"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_mdp_state_and_preference_boundary_revision"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "cost_aware_dueling_bandit", "condorcet_winner_assumption", "fixed_confidence_identification", "asymptotic_cost_guarantee", "budgeted_fine_tuning_preliminary", "test_time_scaling_mdp_ongoing", "human_preference_scope", "limited_quantitative_reporting"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_online_learning_guarantee_mdp_status_and_preference_scope_check"
escalation_verdict: "pass_after_delta_asymptotic_and_ongoing_work_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted online-learning boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Cost-Aware Model Selection and Adaptive Reasoning in Large Language Models via Online Learning

## 一句话总结

本文用预算受限的 sequential decision 统一 LLM 评估、微调和推理：已完成部分在异构比较成本下用 dueling bandit 高置信识别 Condorcet winner，并给出期望成本下界、渐近最优算法与实验；低成本推理辅助微调和串行/并行混合 test-time scaling 仍是初步或进行中方向，尚无完成的性能结果。

## 统一问题：评估、适应与推理预算

静态 benchmark 可能受到数据污染、泄漏和指标错配影响；开放生成任务又很难获得校准的标量质量分数，因此论文考虑由人类或 human-aligned judgment 产生的相对偏好反馈。成对反馈本身昂贵，不同模型查询还可能具有不同计算或金钱成本（§1，p. 3981）。

作者把三阶段都写成在线决策：

1. 用有限评估预算从候选模型中识别偏好反馈下的最佳模型；
2. 用有限训练预算决定训练哪个模型，以及何时用较便宜的推理样本降低不确定性；
3. 用有限推理预算在延长单条 reasoning trace 与并行探索多条 traces 之间分配计算。

这里只在给定观测协议下讨论相对偏好和资源分配，不证明选出的模型符合普遍、跨人群或跨文化的人类价值。

## 已完成研究：[6] 成本感知 dueling bandit

### 问题设定

给定有限候选模型，学习者观察模型输出之间带噪的 pairwise preferences，并面对 heterogeneous comparison costs。问题被形式化为 fixed-confidence cost-aware dueling bandit：

- 假设存在 Condorcet winner，即一个候选在两两比较中击败每个其他候选；
- 目标是在错误概率至多 \(\delta\) 的意义下识别该 winner；
- 优化对象是停止前累计的预期比较成本，而非模型回答质量本身（§2，p. 3982）。

### 下界、算法与保证

作者首先给出任意 \(\delta\)-probably-correct algorithm 的 expected-cost information-theoretic lower bound。利用 Condorcet 结构，该下界得到 closed-form characterization，并据此揭示最优 sampling strategy 如何权衡统计难度与比较成本，而不是只依赖隐式或数值求解的优化问题。

随后提出 cost-aware Track-and-Stop-style algorithm：

1. 根据统计难度和比较成本，自适应匹配最优成本比例；
2. 因最优 allocation 可能不唯一，sampling rule 跟踪的是**一组**最优 allocations；
3. 以面向 dueling-feedback best-arm identification 的 generalized likelihood ratio stopping rule 决定何时停止。

论文声称该算法是 \(\delta\)-probably correct，并在 \(\delta\to0\) 时渐近达到成本下界。这表示在论文的 Condorcet、噪声偏好和成本模型内，以至少 \(1-\delta\) 的概率正确识别，并在小错误概率极限中达到成本比率；它不保证任意有限 \(\delta\) 时精确成本最优，也不覆盖模型假设外的部署环境（§2，p. 3982）。

### 评估证据

作者在 synthetic instances 以及从 head-to-head comparisons 派生的 real-world LLM evaluation datasets 上评估，并报告相对于 cost-unaware 和 heuristic baselines，在所有所测设置中持续降低 evaluation cost（§2，p. 3982）。

概述没有列出具体数据子集、模型、比较成本、样本量、预算、增益数值、方差或显著性。因而不能据此声称已经在生产部署中节省算力/金钱，也不能说被选模型回答质量更高。

仓库内已有该完整研究论文的独立笔记：[Cost-Aware Best Arm Identification via Dueling Feedback with Applications to Large Language Models](./cost-aware-best-arm-dueling-feedback.md)；本节只保留博士概述明确转述的结论。

## 进行中方向一：预算化模型适应

考虑 \(K\) 个候选模型，其性能随 costly fine-tuning actions 变化，而训练后最佳模型事前未知。在任一中间训练水平，学习者还可获取相对便宜的 inference-time samples 来更新性能估计，再决定：

- 继续训练某个模型；或
- 暂不训练，先收集更多推理反馈。

作者把它建模为具有异构 action costs 的 online-learning / decreasing-bandit 问题，以 pseudo-regret minimization 为目标。三页稿只称 preliminary analysis suggests：在中间训练水平策略性配置推理样本，甚至在不继续训练时，也可能显著降低 pseudo-regret（§3.1，p. 3982）。

这不是完整定理或实验结论；文中没有学习曲线、噪声模型、成本函数、算法、下界、对照或统计结果，不能写成已验证的最优微调策略。

## 进行中方向二：混合 test-time scaling MDP

Sequential test-time scaling 延长一条 reasoning trace，但可能收益递减或因错误累积而退化；parallel scaling 独立运行多条 traces 再聚合，计算成本更高且 traces 之间不共享信息。作者据此研究结合两者的 adaptive strategy（§3.2，p. 3982）。

明确给出的 MDP 语义只有：

- **State**：每一条 intermediate reasoning trace 对应一个 state；
- **Action**：延长当前 trace，或以不同成本分支为多条 parallel traces；
- **目标定位**：依据演化中的 reasoning trajectory 与剩余预算，自适应权衡 parallel exploration 和 sequential refinement。

本稿没有给 reward、transition kernel、终止条件、预算是否显式编码于 state、分支数量、聚合规则、求解算法、训练结果或性能定理。该部分是 ongoing formulation，不能宣称已经提升推理准确率、减少成本或学得最优计算策略。

## 偏好与理论保证的边界

- Noisy pairwise preference 是特定任务、提示、比较者或 Arena-derived 数据中的观测信号，不是普遍人类偏好、价值对齐或安全性的证明。
- Condorcet winner 的存在是结构假设；循环偏好或随任务、人群、时间变化的比较关系不在当前保证中。
- \(\delta\)-correctness 是识别概率保证；\(\delta\to0\) 的 cost optimality 是渐近结论，二者都不构成有限预算下的普遍部署最优性。
- 已完成证据只属于模型选择 [6]；预算化微调与 test-time MDP 不能借用 [6] 的定理和实验作为自身验证。

## 复现信息

三页稿没有代码或数据仓库、算法伪代码、lower-bound/GLR 公式、具体 head-to-head 集合、成本口径、模型列表、超参数、随机种子、结果表或置信区间。复现 [6] 需回到完整论文；后两个方向目前还缺少可执行实现和评估协议。

## 与 AAMAS 的关系与核验说明

本文把 online learning、dueling bandits、best-arm identification、budgeted adaptation 和 sequential decision-making 用于 LLM agents 的资源分配。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WSXD8440.pdf) 核对 §2 的 lower bound、allocation-set tracking、GLR 与渐近保证，以及 §3.1/§3.2 的 preliminary/ongoing 状态；未把 pairwise preferences、渐近成本理论或 MDP 设想外推为普遍人类对齐或部署收益。
