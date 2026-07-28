---
title: "Existence and Computation of Fair Allocations under Constraints"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/BTPV8020"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BTPV8020.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["fairness_definition_value_judgment", "divisible_additive_scope", "budget_constraint_specification", "charity_unassigned_goods", "ppad_not_polynomial_time", "truthfulness_impossibility"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Existence and Computation of Fair Allocations under Constraints

## 一句话总结

本文在可分物品、加法估值与 agent-specific generalized-assignment budget 下研究 feasible envy-freeness（FEF）：只比较他人或 charity bundle 中本 agent 放得进预算的子 bundle。作者证明 FEF 且 Pareto-optimal（PO）分配总存在、搜索问题在 PPAD，并证明 FEF+PO+truthfulness 不可兼得；这为特定数学公平提供存在性/复杂性结论，不能决定现实中预算、资格、未分配物品或真实偏好是否正当，也不等于多项式可部署机制。

## 方法与证据

- 每种可分物品对 agent \(i\) 有非负 value \(v_{i,g}\) 与 size \(s_i(g)\)，其 bundle 的 size 总和不得超过 budget \(B_i\)；未被分配的部分进入 charity（§2）。FEF 要求 agent 只在其预算可容纳的他人/charity 子 bundle 中不 envy（§1–2）。它承认容量不等时不应比较完整 bundle，但 budget、size、可分性和 charity 的设定均是设计选择，而非一般平等、需求、权利或合法性的定义。
- 作者先在 closed agent-specific constraints 与 Lipschitz-continuous valuations 的更一般框架下给出 FEF 存在性（Theorem 1）。证明由任意 \(\epsilon\) 的 FEF-\(\epsilon\) 构造、紧致/闭性极限得到，明确是 non-constructive，不能直接给出求解算法（§3）。
- 约束下 FEF allocation space 可非凸（Theorem 2, §4），与无约束 envy-free 的线性不等式描述不同。这解释了不能把常规凸优化直觉直接迁移到有 budget/feasibility 的情形，也意味着局部/线性插值操作未必保留 FEF。
- 对广义 assignment constraints，作者用 fixed-point/pseudo-circuit 与 weighted-social-welfare linear optimization 证明 FEF+PO allocation 存在，且找它的问题属于 PPAD（Theorem 3, §5）。论文同时说明该问题已有特例为 PPAD-hard；“in PPAD”是总搜索复杂度归类，不是已知多项式时间算法或可伸缩的在线 allocation procedure。
- PO 是相对所有可行 allocations 的 Pareto efficiency。证明选取正权重 welfare maximizer，并借 envy graph/权重关系排除 feasible envy（§5）。它不优化最低保障、群体差距、长期机会、过程公平或支付/战略成本；PO 也允许有人很差，只要无法不伤害他人地提高其效用。
- 论文给出不可能性：不存在总是输出 envy-free 且 PO allocation 的 truthful mechanism（Theorem 4, §6），结论在无约束可分 goods 的两 agent 两 goods 实例也成立。因 FEF 在无约束时退化为 envy-freeness，这排除三者 FEF、PO、truthfulness 的同时保证；它不是“所有公平机制皆不可 truthful”，而是这个联合目标的边界。
- 正面地，文中为 two-agent generalized assignment constraints 构造 truthful 的 FEF mechanism（Theorem 5），并给出始终输出 PO allocation 的 truthful mechanism（Theorem 6），分别牺牲另一个目标（§6.1）。不要把这两个单独 compatibility result 拼接为同一机制同时满足三者。
- 论证限定 goods 的非负加法 valuation 与可分 fraction；作者将 approximate FEF/PO 与 truthfulness 的兼容性列为未来工作（§6）。它没有进行市场、用户或公共资源的实证评估。

## 适用边界与复现

- 适用于资源确实可分、价值可线性相加、每人容量可被可信量化且可由机制执行的研究型 allocation。现实土地、算力、医疗、住房、课程或信贷常含不可分性、互补/替代、资格、等待时间、地域与法律约束，应先重建模型而非直接套用 FEF。
- charity 是未分配物的会计构造，不是中性的现实处理：应明确谁持有、何时再分配、是否浪费、是否被弱势群体需要，以及是否诱发策略性少报预算/价值。高影响分配还需最低服务、资格/反歧视审查、申诉、人工复核、隐私与审计。
- 复现需实现 fractional allocation、agent-specific sizes/budgets、charity、FEF 的所有预算可行 subset 检查、PO feasibility，以及论文的 \(\epsilon\)-切分和 fixed-point/linear-OPT pseudo-circuit。应分别验证 Theorem 1 的极限性质、Theorem 2 非凸反例、Theorem 3 的 FEF+PO 条件和 Theorem 4 的操纵反例，并报告数值精度与求解时间。
- 应扩展到不可分/混合物品、非加法偏好、private budgets、dynamic arrivals、团体公平、近似激励相容、计算可行算法与真实制度约束；所有 fairness 结论应与受影响者参与定义的 entitlement 和 harm 指标并列评估。

## 与 AAMAS 的关系与核验说明

这是 AAMAS fair-division 中把约束、效率与激励兼容性放在同一模型的理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BTPV8020.pdf) 核对 generalized assignment/charity/FEF 定义、Theorem 1 非构造存在性、Theorem 2 非凸性、Theorem 3 FEF+PO 与 PPAD-membership、既有 PPAD-hard 特例、Theorem 4 不可能性及 Theorem 5–6 分别的正面机制；没有将 PPAD-membership 写成高效求解、将 FEF 写成一般社会公平，或将单独 truthfulness 结果误写成三性质兼容。
