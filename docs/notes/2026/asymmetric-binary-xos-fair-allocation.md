---
title: "On the Fair Allocation to Asymmetric Agents with Binary XOS Valuations"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BSDW5494.pdf"
preprint_url: "https://arxiv.org/abs/2601.09299"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["binary_xos_scope", "asymmetric_entitlement_scope", "aps_wmms_non_equivalence", "existence_vs_computation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# On the Fair Allocation to Asymmetric Agents with Binary XOS Valuations

## 一句话总结

针对拥有不同 entitlement 的 agent 和 binary XOS valuation，本文给出紧的 $1/2$-APS allocation 及多项式算法；同时证明一般 XOS 下始终存在 $1/n$-WMMS allocation，且即使 binary XOS 也不能统一改进该比例。

## 方法与证据

- binary XOS 指 valuation 能表示为 additive clauses 的最大值，且边际价值为 0/1；它严格强于 binary additive 的假设。APS 与 WMMS 是两种不同公平基准，后者按 entitlement 加权的 partition 来定义（§2）。
- Theorem 1：已知所有 agent 的 APS 值时，作者的顺序式 Algorithm 1 构造每名 agent 至少 $1/2$ APS 的 allocation；证明使用 binary-XOS 中 non-wasteful bundle 与按 entitlement/APS 排序的归纳（§3.1）。
- Theorem 2：Algorithm 2 从 $\lfloor b_i m\rfloor$ 开始迭代下调 APS guess；Algorithm 1 返回的 unsatisfied agent 表示当前 guess 过高。它在 $O(mn(m+\log n))$ 时间输出 $1/2$-APS allocation（§3.2）。结合先前的不可行实例，该 $1/2$ 因子对 binary XOS APS 是 tight。
- entitlement 相同时，APS 不小于 MMS，因此 Corollary 1 给出可多项式计算的 $1/2$-MMS allocation；这不是非对称 WMMS 的结论（§3）。
- Proposition 1：非对称 entitlement 下，即使 valuation additive，某 agent 的 APS/WMMS 可以任意小，故 APS 算法不自动给 WMMS 近似（§4）。
- Theorem 3：任意 XOS valuation 下存在 $1/n$-WMMS allocation；作者的 existence construction 以各 agent 的 WMMS partition 为基础。Theorem 4 构造 binary XOS instance，说明没有 allocation 能保证优于 $1/n$-WMMS。Theorem 5 仅对 binary additive valuation 给出 exact WMMS 且 $O(m\log n)$ 的算法（§4）。

## 局限与复现

- $1/2$-APS 的存在/算法严格依赖 binary XOS；对一般 XOS，论文不声称同一半因子。$1/n$-WMMS 的 theorem 是 existence 结论，并未为一般 XOS 提供相应的多项式计算算法。
- APS 与 WMMS 在不对称 entitlement 下没有固定上/下界关系；以 APS 高近似率宣称 WMMS 公平会违反 Proposition 1。
- binary XOS 与 binary additive 的差异实质性：后者可 exact WMMS，前者的 worst-case 上界仍为 $1/n$。不能因所有 marginal values 为 0/1 就套用 additive 算法。
- 复现应给出 XOS clauses/oracle、entitlements 是否归一、APS guess 更新轨迹、non-wasteful bundle procedure、WMMS partition 定义和 tie-breaking；分别验证 APS、MMS 和 WMMS，且在不同 $n$ 下报告近似比例。

## 与 AAMAS 的关系与核验说明

该文研究带不平等 entitlement 的不可分物品公平分配，连接资源分配、公平性和算法机制设计。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2601.09299) 手工核对 APS/WMMS 定义、各定理条件、因子与运行时间。
