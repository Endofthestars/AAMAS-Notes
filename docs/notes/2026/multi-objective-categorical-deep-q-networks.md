---
title: "Multi-Objective Categorical Deep Q-Networks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/ARIZ7102"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ARIZ7102.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["scalarization_misspecification", "theorem_condition_gamma_K", "exponential_multiobjective_scaling", "continuous_action_discretization", "benchmark_only_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Multi-Objective Categorical Deep Q-Networks

## 一句话总结

MO-CDQN 以多维 categorical return distribution 扩展 C51-DQN，在给定、可非线性的 scalarization 下按 Expected Scalarized Return (ESR) 学习单一 policy；Distributed MO-CDQN 让多个已知 scalarizations 的 learners 共享 off-policy experience。论文在 MO-Gymnasium 基准上显示相对 EUPG/MOCAC 更高样本效率，并在 10 个多策略标量化中胜出 9 个；但它优化的是设计者写入的 utility，不会自行解决目标选择或安全约束，理论与实践都受 \(\gamma K<1\)、离散动作和目标数指数复杂度限制。

## 方法与证据

- MO-MDP 的 reward 是 \(d\)-维向量。论文区分 SER（先取期望 return vector 再 scalarize）与 ESR（每次 trajectory return 先 scalarize 再取期望）；ESR 更适合单次执行或不可逆决策，但这只是目标定义，并不自动指定何种 trade-off 合理（§2.1--2.2）。
- MO-CDQN 对每个 \((s,a)\) 预测 joint multivariate categorical return distribution：每个 objective 有固定 support，联合 support 是其 Cartesian product。动作选择显式使用当前 accumulated return，将 future-support 平移后以 scalarization 的期望比较；TD target 以 distributional Bellman update、projection 与 cross-entropy 训练（§4.1）。
- Theorem 4.3：若 \(u\) 对 \(\ell_1\) 范数为 \(K\)-Lipschitz 且 \(\gamma K<1\)，\(E_uT\) 是 contraction；继而固定点的 expected scalarized return 对该条件下的 scalarization 最优（Corollary 4.4）。这不是对任意非线性/不连续 utility、任意近似网络训练或任意现实 MDP 的无条件收敛定理。
- Distributed MO-CDQN 为每个预先指定 scalarization 配一 learner/replay buffer，轮流提出 action、随机选择一个 action 与环境交互，再共享 transition；目的是以 off-policy data 并行优化 policy portfolio，而不是从用户中学习偏好（§5）。
- single-policy 评测在 MO-Gymnasium 的 Fruit-Tree-Navigation、Deep-Sea-Treasure、Fishwood、Four-Room、Minecart、MountainCar；MO-CDQN 通常给 50% 的 environment-step budget，baselines EUPG/MOCAC 给双倍预算，短任务 11 seeds、长任务 5 seeds，周期性跑 100 episodes取 expected scalarized return（§6.1--6.2）。
- 论文报告 MO-CDQN 在这些图表中更快达到更高 returns：如高度 stochastic task 小于 100k steps 达到更好 policy，而 MOCAC 需超过 200k 才达到相近；Minecart 约 150k 得到 satisfying policy，而 EUPG/MOCAC 在其双倍预算也未解决。multi-policy 在 FTN/Four-Room/Minecart 的 10 个 hand-picked scalarizations 上胜出 9 个（§6.3、Figure 1、Table 1--2）。

## 安全边界与复现

- scalarization 是价值判断接口：奖励维度、归一化、ideal point、权重/乘积/min 函数会决定谁的风险、资源或损失被牺牲。算法的“optimal”只相对于这些输入；不等于公平、Pareto complete、符合人类偏好、满足法规或对每个 objective 有 safety floor。
- ESR 会偏好单次 trajectory 的 balanced utility，但并不取代硬约束、chance constraints、shielding、risk measure、uncertainty calibration或人类批准。医疗、车辆、电网、气候等文中动机例子没有被实验；不得从 benchmark scalarized return 推断可安全部署。
- categorical support 依赖每个 objective 的 \(V_{MIN},V_{MAX},N\)，out-of-range return 与投影误差会改变 policy；联合 atom 数随 objectives 相乘，论文明确指出 objective 数增加时计算成本指数增长。须报告 support/range 来源、normalization、clipping、projection residual与 memory/latency。
- 方法只适合 discrete action set；continuous control 需要 discretization，作者明确警告会失去 fine-grained control 并可能次优。连续或安全关键控制不应仅把动作粗分桶后沿用性能宣称。
- multi-policy variant 假定用户显式给定一组 scalarization functions，不能处理未知、冲突、随时间变化或由多利益方协商的偏好。应采用 preference elicitation、stakeholder review、sensitivity/robust optimization、objective-wise metrics和拒绝不安全 utility specification 的治理流程。

## 与 AAMAS 的关系与核验说明

这是 distributional multi-objective RL 与 ESR optimization 的论文。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ARIZ7102.pdf) 核对 ESR/SER 区分、joint categorical representation、Theorem 4.3/Corollary 4.4 条件、Distributed algorithm、MO-Gymnasium protocol、Figure 1/Table 1--2 与 §7--8 限制；没有把给定 utility 下的基准最优表述为现实偏好、Pareto 公平或安全认证。
