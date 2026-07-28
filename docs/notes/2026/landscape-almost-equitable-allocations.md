---
title: "The Landscape of Almost Equitable Allocations"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/PORK6413"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PORK6413.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["valuation_oracle_assumption", "eq1_not_full_equity", "existence_conditions", "computational_hardness", "no_welfare_guarantee", "theoretical_model_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check; author preprint fallback)"
reviewed_at: "2026-07-29"
---

# The Landscape of Almost Equitable Allocations

## 一句话总结

本文刻画一般、可非单调估值下的 EQ1（equitable up to one item）：所有人不必完全等值，但每两人之间的价值差可通过移除至多一个物品缓解。它给出若干精确存在性/计算边界：两人且 grand bundle 同号时可高效求解，更多人必须附加估值结构才有保证；一般多 agent 情况即使 grand-bundle 同号也可能无解且判定困难。EQ1 是特定报告估值下的形式性质，不是现实公平感、效率或策略无关保证。

## 方法与证据

- 研究对象是不可分物品与 set valuations，可含 goods/chores、非单调甚至负边际值；假定可多项式时间 oracle 查询估值（§2）。这与从人类收集、存在噪声/策略性陈述或难以计算的真实效用不同。
- EQ1 放松完全 equitability：允许从相关 bundle 移除至多一件物品以消除价值不等（§2）。它不要求 envy-freeness、Pareto optimality、最大 social welfare、比例性、个体合理性或稳定性；即使满足 EQ1，也可能有人绝对效用很低。
- 两个 agent、两人对 grand bundle 都非负（对称地都非正）时，Theorem 3.1 给出总存在且多项式算法；关键是“同意 grand bundle 的符号”，不是逐物品同号。若一人把所有物品视为正、另一人视为负，EQ1 可连两人/加性估值也不存在（§1, §3）。
- 多于两个 agent 的一般估值中，grand bundle 都非负仍可能没有 EQ1；其 existence decision 为 NP-complete（Theorem 3.2）。因此不得从“两人可解”或“所有人总值同号”推断一般群体可行。
- 当每人估值有 marginal-witness 结构且 grand bundle 非负，EQ1 可多项式计算（Theorem 4.2）；submodular 与 doubly monotone 是其推论（Theorems 4.4–4.5）。相应非正/supermodular结论通过补集变换给出，条件不可混用。
- 对所有子集均 nonnegative（或 nonpositive）的估值，Theorem 5.1 证明 EQ1 总存在，解决先前开放问题；其通用构造可为指数时间。nonnegative submodular 且 \(|M|\ge|N|\) 时另有多项式 non-empty allocation 算法（Theorem 5.4）。存在性与可实践求解复杂度必须分开表述。
- 论文还把非单调 nonnegative cut function 作为图划分应用例（§6），但没有真实用户、市场、资源分配数据或行为实验；定理不能验证效用可测、估值诚实或实施后的社会效果。

## 适用边界与复现

- 适合作为 mixed-manna/非单调公平分配的理论基线：先明确估值类、oracle 表示、agent 数、grand-bundle 符号以及是否要求 non-empty bundles，再选对应定理/算法。
- 实际公共资源、任务、福利或负担分配还需审查估值 elicitation、弱势群体影响、可解释性、参与/申诉、效率、激励兼容性、预算/法律约束和动态变化。EQ1 不能替代这些制度与伦理保证。
- 复现应固定物品/agent 编码、估值 oracle、符号/类别判定、EQ1 witness 的方向和单件移除规则、算法/停止条件及所有复杂度度量；应独立验证输出 allocation 对每对 agent 的完整 EQ1 不等式。
- 应研究 noisy/partial/strategic valuations、近似 oracle、多人异质 mixed-manna、EQ1 与 EF1/效率的联合可行性及算法实践尺度，并报告无解、运行时间与分配福利分布。

## 与 AAMAS 的关系与核验说明

这是计算社会选择中的不可分 mixed-manna 公平分配理论工作。AAMAS 官方 PDF 镜像本次连接超时，笔记依据同题、同作者、同 AAMAS DOI 的 [作者 arXiv 全文](https://arxiv.org/abs/2511.07395) 核对，并保留 [AAMAS 官方记录](https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm)。没有把 EQ1、两人结果、nonnegative 子类或图割应用误写成一般多 agent 存在性、真实公平、效率或政策实施保证。
