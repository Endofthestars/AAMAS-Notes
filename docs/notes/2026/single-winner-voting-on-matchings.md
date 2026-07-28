---
title: "Single-Winner Voting on Matchings"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "argumentation_reasoning"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RKNE1743.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["utility_model_scope", "complexity_landscape", "matching_candidate_space"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Single-Winner Voting on Matchings

## 一句话总结

论文把每个可行 matching 当作候选人、让外部 voters 对整个 matching 表达偏好，并在指数级候选空间下刻画 welfare、Pareto optimality 与 Condorcet winner 的计算复杂度。

## 方法与证据

- 与传统 matching-under-preferences 不同，voters 不属于底层图，也不只关心自身匹配边；他们评价完整 matching。底层图可非二部，且多数结果对二部图也成立（§1）。
- 每个 voter 指定一个 preferred matching；论文采用 affine overlap utility、one-edge approval 和 $\kappa$-missing approval 三类 utility。后两类为 0/1 approval，$\kappa$-missing 表示偏好 matching 最多缺失 $\kappa$ 条边（§1–2）。
- Utilitarian welfare 在 affine 下可多项式求解，但在 approval 类下为 NP-complete；egalitarian welfare 在 affine 与 one-edge approval 下 NP-complete。对 $\kappa$-missing，1-missing 可多项式、2-missing 起 NP-hard，体现类似 2-SAT/3-SAT 的复杂度跳变（§3）。
- Pareto construction 通常比 verification 容易：affine 下可利用 utilitarian optimization 构造 strong Pareto-optimal matching，但 verification 为 coNP-complete；approval 情形的 verification 与 egalitarian welfare 的难度关联（§4）。
- Condorcet winner 的存在性在所有 utility 模型中一般 NP-hard，唯一例外是 approval utility 下 weak Condorcet winner 的平凡存在；weak/strong Condorcet winner verification 在所考虑 utility 下均为 coNP-complete（§5）。
- 因此 matching 的组合结构本身没有普遍消除指数候选空间带来的困难；utility 模型参数和 strong/weak solution concept 的微小变化即可改变复杂度（§1、Table 1）。

## 局限与复现

- 结论针对 voter 对完整 matching 的偏好，不可直接转用到稳定婚姻、house allocation 等“图中 agent 只评自身 partner”的标准模型。
- $\kappa$-missing 的相变不能简化为所有 approval 规则都 NP-hard：文中明确区分了 $\kappa\le1$ 与 $\kappa>1$。
- Condorcet 的“存在”“verification”“weak/strong”是不同问题；实验或实现必须分开报告。
- 复现应显式生成 matching 空间或采用结构化优化 oracle，并针对三种 utility、两种 welfare、Pareto 版本及 Condorcet 版本逐项比对；不能只测试一个小图实例。

## 与 AAMAS 的关系与核验说明

该工作把社会选择的单胜者标准应用到组合资源分配。笔记基于官方公开 [AAMAS PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RKNE1743.pdf) 核对了 utility 类型、强弱概念和复杂度边界。
