---
title: "Minimax and Preferential Almost-Stable Matchings"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/PCDE6577"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PCDE6577.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["strict_ordinal_preferences", "static_matching_scope", "np_hardness", "bounded_list_tractability_only", "preference_elicitation_burden", "fairness_metric_tradeoff", "extended_results_external"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Minimax and Preferential Almost-Stable Matchings

## 一句话总结

论文在 strict preferences、可不完整列表的 Stable Roommates/Marriage 中提出两种 almost-stable 目标：minimax 将任一 agent 参与的 blocking pairs 最大数最小化，避免把偏离诱因集中到少数人；preferential 只最小化指定 agent 子集的 blocking pairs。两者在极小阈值下已很难：SRI 中判断是否每人至多一个 blocking pair 在列表长度至多 10 或完整列表时仍 NP-complete；最大基数 SMI 版本在列表长度至多 3 时也 NP-complete；指定集合零 blocking pair 也 NP-hard。正面结果主要限于很短列表（长度 ≤2）或 preferential set 与最大列表长度都小的 FPT/XP 参数化情形，不能把它当作一般市场的可扩展公平匹配算法。

## 方法与证据

- SRI 是一般图中的 stable roommates，SMI 是二分 acceptability graph；blocking pair 指双方都严格偏好彼此于当前 partner（或 unmatched）。论文讨论的 matching 均假定静态、对称可接受性、严格序偏好（§1）。并未覆盖 ties、合约/容量、多对一、动态到达或策略性申报。
- Minimax-AlmostStable-SRI 目标为 \(\min_M\max_a |bp_a(M)|\)，不同于最小化全局 blocking pairs：它控制最坏个体的偏离机会；Max-SMI 版本还限制在最大 cardinality matchings（§2）。该公平准则会与总阻塞数、匹配规模和群体公平产生不同 trade-off。
- Theorem 2.1：\(k\)-Max-AlmostStable-SRI 在 \(k=1\) 时 NP-complete，即使 preference list 长度最多 10 或全部 complete；并导出该最优化问题相对其最优 minimax 值 para-NP-hard，且除非 P=NP 不存在保证优于 2 的多项式近似（§2.1）。这表明“小的每人阻塞负担”不意味着容易求解。
- 对 list length ≤2 的 SRI，acceptability graph 仅是 paths/cycles：用 Irving 先查稳定匹配，否则取 maximum-cardinality matching 并 rematch，保证每 agent 最多一个 blocking pair；Theorem 2.3 给出 \(O(n)\) exact algorithm（§2.1）。这是非常窄的选择集假设。
- Theorem 2.4：\(k\)-Max-AlmostStable-Perfect-SMI 在 \(k=1\)、每列表长度 ≤3 时 NP-complete；相应最大基数 SMI minimax 也有强困难性。list length ≤2 时 Theorem 2.6 给线性 exact algorithm（§2.2）。因此从两个到三个可选 partner 的小扩张已改变复杂性边界。
- preferential 目标对给定 \(A'\) 最小化涉及其成员的 blocking pairs，而非优待其余 agent；动机是有些 agent 受法规/合同限制不能发起偏离（§3）。这是一种规范性建模选择，实际政策必须说明为何某群体的稳定性被优先。
- 在最大基数 SMI，0-Preferential-AlmostStable-Perfect-SMI-Dec 对 list length ≤3 即 NP-complete（Theorem 3.1）。但 \(k\)-Preferential-AlmostStable-Max-SMI 在组合参数 \((|A'|,d_{max})\) 下 FPT、只按 \(|A'|\) 为 XP（Theorem 3.3/Corollary 3.4）；一般 SRI 也在 \((|A'|,d_{max})\) 下 FPT（Theorem 3.8/Corollary 3.9）。参数小才是可行性来源，而不是目标本身。
- 正式会议稿将更完整 ILP、实验、近似/不可近似细节置于引用的扩展 arXiv 文本；本笔记只依据 AAMAS 论文可见定理陈述，不宣称有会议稿未报告的实证性能。

## 适用边界与复现

- 适用于需要明确分析局部偏离诱因的静态小型匹配机制：例如先限定各 agent 只报少量 acceptable choices，或 preferential population 很小且列表长度有界。
- 不应在住宿、医疗、就业或通信资源分配中把 minimax blocking count 当成唯一公平/稳定准则。需与总福利、规模、群体公平、法律、可解释性、可申诉性和策略性误报风险一并评估。
- 复现应实现 strict-list parsing、acceptability symmetry、blocking-pair audit、matching cardinality 与两个目标；用 ILP/枚举核对小实例的 optimum，并在长度 ≤2 时验证线性算法。对复杂性结论应使用论文 reduction 的完整版本，不以随机实验替代理论证明。
- 实务中可先做 preference-elicitation 与缩短列表的敏感性分析，报告 \(|A'|\)、\(d_{max}\)、总/个体 blocking pairs 与未匹配人数；若参数不小，应使用精确 MIP/启发式并明确无全局最优/近似保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 matching theory、机制设计与多智能体资源分配工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PCDE6577.pdf) 核验 minimax/preferential 定义、Theorems 2.1/2.3/2.4/2.6/3.1/3.3/3.8 与结论中的复杂性边界；没有将局部可解情形或扩展版实验误表述为一般高规模市场的可部署算法。
