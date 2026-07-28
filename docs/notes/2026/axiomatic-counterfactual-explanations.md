---
title: "Axiomatic Foundations of Counterfactual Explanations"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "safety_verification", "human_agent_interaction"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CKPK5561.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["axiom_compatibility_scope", "counterfactual_semantics", "complexity_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Axiomatic Foundations of Counterfactual Explanations

## 一句话总结

论文为分类器的 counterfactual explainer 提出九条公理，刻画公理兼容性与五类 counterfactual family，区分 local/global、necessary/sufficient 以及 sceptical/credulous 的语义。

## 方法与证据

- 模型是有限特征域上的 surjective classifier；query 包含 theory、classifier 和待解释 instance，explainer 产生能改变/刻画分类的部分赋值（§2–3）。
- 论文定义九条 explainer axioms，并以 Theorem 1 给出若干不可兼容组合、Theorem 2 说明除已排除者外的公理组合皆有某个 explainer 满足；因此不是所有“合理性质”能同时要求（§3）。
- 表征结果得到五种不同 family：necessary reasons 与 sufficient reasons；其中各有 global 与 local 形式，而 local sufficient reasons 再分 sceptical 与 credulous（§4–6）。
- 现有多数 counterfactual explainers 被形式化为 local credulous sufficient reasons；先前的 global 方法对应 global necessary reasons。该 taxonomy 识别出若干此前未被单独区分的类型（§1、§6–7）。
- 复杂度依赖 family、classifier 表示和 domain：Theorems 13–14 对 DecideExp/FindExp 给出多项式、coNP-complete 或 NP-hard 的分类案例；不能将某一 family 的易解性外推至所有 counterfactual 定义（§8）。

## 局限与复现

- 这是解释语义与公理的表征，不是对现实因果干预、数据分布合理性、行动可行性或用户接受度的保证。
- “global”描述 classifier 整体行为，“local”围绕给定 instance；必要/充分、sceptical/credulous 也不可互换。
- 复现应先固定 feature theory、classifier encoding、query 和每条公理，再验证 family membership 与 DecideExp/FindExp 的复杂度；只生成一个接近输入的反事实不足以验证表征结论。

## 与 AAMAS 的关系与核验说明

该工作为 agent 决策解释提供形式化 vocabulary，适用于分析 explanation guarantees 的边界。笔记基于官方公开 [AAMAS PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CKPK5561.pdf) 核对了九公理、五类 taxonomy 与复杂度结论的条件性。
