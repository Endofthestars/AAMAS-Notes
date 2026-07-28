---
title: "Fair Allocation of Improvements: When Old Endowments Shape New Assignments"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FRTB6682.pdf"
preprint_url: "https://arxiv.org/abs/2504.16852"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["quasilinear_payment_scope", "envy_graph_characterization", "risk_averse_truthfulness_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Fair Allocation of Improvements: When Old Endowments Shape New Assignments

## 一句话总结

论文面向旧房拆除、以新房补偿原住户的分配问题：把对他人新房的比较与其旧房禀赋同时纳入 envy，在允许收支平衡转移支付时刻画 EF/比例公平可达性，并优化不可避免的 envy 或不比例度。

## 方法与证据

- 模型有 $n$ 名 agent、其既有旧房分配 $O$ 和 $n$ 套新房；agent 对所有新旧房给出非负估值，效用为 $v_i(A_i)+p_i$，并以改善量 $v_i(A_i)-v_i(o_i)+p_i$ 比较。payment 可正可负但总和为零（§2）。
- 对给定新房分配 $A$，Theorem 3.1 给出 EF-able 的等价刻画：存在平衡 payment 使其 EF，当且仅当每个 agent 置换下总改善不超过原分配，亦即差分 envy 图 $G_{A,O}$ 没有正权环（§3.1）。因此福利最大的新房分配并不自动 EF-able；若旧房 envy 图没有负环，或全体对旧房估值相同，才有该充分条件（Proposition 3.2）。
- 若无法 EF，固定 $A$ 时可将最小可能的最大 envy 精确写为 $G_{A,O}$ 的最大平均环权；用最大平均环与最长路构造 payment，可在强多项式时间计算（Lemmas 3.6–3.7）。但连同分配一起最小化该量是否能多项式求解，论文明确留为 Open Question 3.8。
- 对比例公平，论文证明固定 $A$ 下最小最大 disproportionality 是总 disproportionality 的 $1/n$，相应平衡 payment 有闭式表达；任一 utilitarian-welfare-maximizing assignment 使该目标全局最小。因此可在多项式时间找比例分配及 payment，或判定不存在（Lemma 4.2、Lemma 4.3、Corollary 4.4）。
- 直接征询旧房主观估值会导致安全且有利的虚报。论文改为征询公用房屋特征的加性或乘性估值；在 $n\ge2$、所有新房特征都未知、并将“安全”量化到所有可能新房特征组合时，Minimum Disproportionality mechanism 是 risk-avoiding truthful（Proposition 5.1）。

## 局限与复现

- 所有结论针对一人一套房、准线性效用、可为负且总和为零的 transfer payment；不能直接移植到预算受限、不可收款或多单位住房分配。
- EF-able 的图论条件和最大平均环算法是对**给定**新房 assignment 的结论；联合最小化最大 envy 的计算复杂度并未解决。
- RAT 不是 dominant-strategy truthfulness。其正面结果依赖加性/乘性特征表示、至少两名 agent、所有新房特征未知，以及扩展后的最坏情形“安全”定义；已知新房特征或旧房独有特征可重新产生安全操纵（§5、Appendix C）。
- 复现应分别实现 maximum-weight matching、差分 envy 图的最大平均环/最长路 payment、以及比例目标的闭式 payment；对特征诱导下的虚报，需枚举或构造对抗的新房特征组合，而非只在固定房源上测策略性。

## 与 AAMAS 的关系与核验说明

该文将公平分配、机制设计与城市更新中的旧禀赋纳入同一 formal model。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2504.16852) 核对了 Theorem 3.1、Lemmas 3.6–3.7、Lemmas 4.2–4.3、Corollary 4.4 与 Proposition 5.1 的前提和结论。
