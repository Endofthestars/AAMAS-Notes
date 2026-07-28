---
title: "Exploring Relations among Fairness Notions in Discrete Fair Division"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/DRAH3963"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DRAH3963.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["fairness_definition_value_judgment", "indivisible_item_model_scope", "implication_not_existence", "valuation_entitlement_assumption", "counterexample_scope", "inference_engine_input_dependency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Exploring Relations among Fairness Notions in Discrete Fair Division

## 一句话总结

本文把 22 个离散 fair-division notions（EF/EF1/EFX、PROP 系列、MMS/APS、epistemic/minimum/groupwise/pairwise variants 等）按“任一 \(F_1\)-fair allocation 是否也必为 \(F_2\)-fair”组织为条件性的 implication hierarchy，并为多数未蕴含 pair 给出反例；还以 inference engine 对已编码结果做传递推理。它帮助选择和比较形式公理，却不保证这些 allocation 存在、能高效计算、与 Pareto efficiency/激励兼容，或在现实公共资源制度中等同于社会公平。

## 方法与证据

- fair division instance 由有限 agents、不可分 items、valuation functions 和 positive entitlement weights 组成，allocation 是 items 的完整不相交分配（§2）。论文区分 goods、chores、mixed manna；equal/unequal entitlements；additive、submodular、subadditive、general valuations及不同 marginal assumptions。每一结论都带这些前提，跨设置直接搬用会失效。
- 对 notions \(F_1,F_2\)，\(F_1\Rightarrow F_2\) 的含义是该 setting 内所有 \(F_1\)-fair allocations 也满足 \(F_2\)；一个 \(F_1\) 但非 \(F_2\) allocation 即证非蕴含（§1, §4）。这说明公理的逻辑强弱，不说明 \(F_1\) allocation 是否存在、是否可计算、是否产生更高 welfare 或更被人接受。
- 覆盖包括 envy family（EF、EF1、EFX、epistemic EEF/EEFX/EEF1）、proportionality family（PROP、PROP1、PROPx、PROPm、PROPavg、GPROP/PPROP）、MMS/APS 与 minimum/groupwise/pairwise variants（§3）。各指标比较 bundle、去一件、可担保 share、认知或群体参照的方式不同；名称相近不意味着价值含义、对弱势群体影响或可实施性相同。
- 对 additive equal-entitlement goods/chores/mixed 及多种更广 setting，作者给 near-complete implication figures。Table 1 指出：additive goods、submodular goods、subadditive goods 仍各有 1 unresolved implication；unequal additive goods/chores 各有 3；general goods、additive chores/mixed 和若干 binary-marginal cases可达 0 open problems。故“near-complete”并非全 settings、全 22-pair 的闭合理论。
- 示例条件性结果包括 EFX \(\Rightarrow\) EF1、MEFS \(\Rightarrow\) PROP（subadditive）、EF \(\Rightarrow\) GPROP（subadditive）、PROP \(\Rightarrow\) EF（superadditive）、MMS \(\Rightarrow\) MXS（additive equal）等（Table 2）。这些箭头的 valuation sign、entitlement、agent number 和 item type 条件不可省略；论文也列出大量 additive counterexamples（Table 3）。
- inference engine 接收 conditional implications 和 conditional counterexamples，在给定 setting 上先取 implication transitive closure，再把 counterexample 沿蕴含关系传播（§5）。例如它可推出 EEFX 不蕴含 PROPavg 的链式结果；engine 的正确范围受输入 facts、条件 lattice 与编码准确性约束，不能发现未编码的新数学证明或判定现实案例是否公平。
- 作者将 feasibility 与 implication 分开处理：Fig. 1 中 green nodes 为已知 feasible notions、gray nodes 的 feasibility 可为 open；§6 还指出加入 Pareto optimality、equitability、Nash welfare、约束/混合物品等会产生新问题。因而蕴含层级不是可部署 algorithm menu。
- 论文给 web application/JavaScript engine 和 GitHub source（§1, §5），但用于概念查询的工具不取代对 valuation elicitation、个案约束、数值实现、战略报告或分配后果的审计。

## 适用边界与复现

- 适用于理论研究者或机制设计者在明确的不可分 item/valuation/entitlement 模型中筛选 compatible fairness targets、解释为何两个公理不可互换。使用时必须先写明正负边际、item 可分性、agent 数、权重和是否允许未分配/补偿。
- 住房、医疗、教育、工作、救灾或公共物资不能仅选择一个“更强” notion 就称公平。需额外处理资格/需求/历史不平等、不可比较效用、最低保障、法律权利、程序参与、隐私、策略性报告、长期后果、申诉与人工复核；形式 EF/PROP/MMS 不能替代这些要求。
- 复现应使用论文/完整版本的 definitions、Table 2/3 与附录 proof instances，按条件检查每条 implication/反例，并复现 inference engine 的 input tuple、transitive closure 和 query output。应明确某一结果是手工证明、引文结果还是 engine 推导，避免将推导链误当独立新定理。
- 后续应整合可行性与算法复杂度、Pareto/效率/激励约束、restricted allocation、mixed divisible-indivisible resources、uncertain/strategic valuations、agent welfare/rights与实证参与者对不同公理的理解；文中的开放 pair 和非加法 chores 也是直接研究缺口。

## 与 AAMAS 的关系与核验说明

这是 AAMAS discrete fair division 的综述式理论/推理工具工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DRAH3963.pdf) 核对 22 notions、条件性 implication 定义、Table 1 的 unresolved 范围、Table 2/3 的代表结论/反例、inference engine 两步推导及作者列出的 feasibility/PO/约束扩展缺口；没有将逻辑蕴含地图误写成 allocation existence、效率、truthfulness、现实公平或决策授权保证。
