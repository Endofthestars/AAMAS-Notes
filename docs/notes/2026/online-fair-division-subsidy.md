---
title: "Online Fair Division With Subsidy: When Do Envy-Free Allocations Exist, and at What Cost?"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DXUE6939.pdf"
preprint_url: "https://arxiv.org/abs/2510.13633"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["online_irrevocability", "valuation_class_scope", "subsidy_bound_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Online Fair Division With Subsidy: When Do Envy-Free Allocations Exist, and at What Cost?

## 一句话总结

论文研究物品在线到达且必须不可撤销分配时的公平分配：允许事后非负补贴以消除 envy，刻画哪些估值类能始终维持 envy-freeability，以及为此需要多少补贴。

## 方法与证据

- $m$ 个不可分 goods 依次到达，$n$ 个 agent 固定；每一步都必须立即分配，算法不知道总物品数。终止后可选择补贴向量，但每个可能终止时刻都须保持保证（§2）。
- allocation 可借助补贴达到 EF 当且仅当它是 locally efficient（LE）：对已固定的 bundles，不存在重排 bundles 能提高社会福利（Theorem 2.3）。
- 对 additive、SPLC 与任意 $k$-demand valuations，论文给出逐步维持 LE（因而 envy-freeability）的在线算法；但 budget-additive、二值边际的 submodular、二值边际的 supermodular 估值中，无法始终保持 LE（§3、Table 1）。
- “始终可 envy-freeable”不代表补贴不随 $m$ 增长：即便 additive，最小总补贴也可达 $\Omega(mn)$；SPLC 与允许 $k$ 随 $m$ 增长的 $k$-demand 也继承该类下界（§4）。
- 小补贴的正面类别包括固定 $k$ 的 $k$-demand/$k$-valued（界可依赖 $k$ 但不依赖 $m$）、rank-one、restricted additive 与 identical monotone valuations；论文对多数界限给出紧或近紧说明（§4、Table 1）。
- 论文追踪的是任意时刻若过程停止时使当前 allocation EF 所需的最小补贴，而不是维护一个不可撤销的在线 payment vector（§1）。

## 局限与复现

- 结果为 goods 的 normalized、monotone 估值与 online items/offline agents 设置；chore 扩展只在文中高层讨论，不能直接等同所有结论。
- “小补贴”指不随物品数 $m$ 增长，并不必然与 agent 数 $n$ 或参数 $k$ 无关。
- 只最大化当前 welfare 并非所有估值类的完整解法；论文强调 LE 能在线维持的类别严格更广于在线 welfare maximization 可行的类别。
- 复现应在每次到达后检查 LE（所有 bundle permutation），并用差分约束/最短路形式求当前最小非负 subsidy；需对 adversarial arrival order 报告最大补贴，而非只评最终一次 allocation。

## 与 AAMAS 的关系与核验说明

该文将公平分配、在线决策与可解释的 monetary compensation 结合。笔记基于作者公开的 [arXiv PDF](https://arxiv.org/pdf/2510.13633) 核对了 LE 等价关系、估值类边界与补贴量级。
