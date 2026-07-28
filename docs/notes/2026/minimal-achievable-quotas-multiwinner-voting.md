---
title: "On Minimal Achievable Quotas in Multiwinner Voting"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ZUBO6825.pdf"
preprint_url: "https://arxiv.org/abs/2510.19620"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["alpha_quota_direction", "jr_ejr_scope", "complexity_scope", "interval_domain_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# On Minimal Achievable Quotas in Multiwinner Voting

## 一句话总结

本文将 approval-based 多胜者投票中固定的比例 quota 替换为实例依赖的缩放因子 $\alpha$：$\alpha$ 越小，能主张代表权的团体越小、标准越强；作者研究满足 α-JR/EJR/EJR+ 的最小可实现 $\alpha$、其复杂度和若干结构化偏好域的算法。

## 方法与证据

- $(\alpha,\ell)$-cohesive group 需有至少 $\alpha\ell n/k$ 名选民并共同认可至少 $\ell$ 名候选人；由此定义 α-JR、α-EJR、α-EJR+。$\alpha=1$ 回到经典定义，而 $\alpha$ 变小会扩大需受保护群体，因而更难满足（§4）。
- Proposition 4.7 仅在 $\alpha_1\le\alpha_2\le\alpha_3$ 时给出 $\alpha_1$-EJR+ ⇒ $\alpha_2$-EJR ⇒ $\alpha_3$-JR；若三个 α 反向严格递减，这些版本不可比较（Proposition 4.8）。不能忽略 α 的不同而沿用经典 EJR⇒JR 的表述。
- 每个实例都有可在多项式时间构造的 α-EJR+ committee，只要 $\alpha>k/(k+1)$（引用的 Theorem 4.6）；作者定义 $\alpha^*_\Phi(I)$ 为能满足公理的 committee 中最小 α。$α=0$ 的边界需排除空群体的技术问题（§4）。
- Proposition 4.9 构造实例使 $\alpha^*_{JR}$ 与 $\alpha^*_{EJR}$ 相差 $k/(k+1)$。Theorem 4.13 进一步表明 CC、seq-CC、seq-Phragmén、PAV、α-MES、α-GJCR 等规则相对最优 α-JR 的加性差可达 $k^2/(k+1)^2$（§4）；这是最坏情形，不是这些规则在每个实例上的差距。
- Theorem 5.2：对固定有理 $\alpha\in(0,1)$，判定是否存在满足 α-JR/EJR/EJR+ 的 committee 是 NP-hard；α-JR 与 α-EJR+ 的相关判定达到 NP-complete。给定 committee 时，α-JR 值可在 $O(nm)$ 求、α-EJR+ 值可在 $O(mnk)$ 求；给定 α 的 α-JR committee 可用可行性 ILP 求解（§5、Propositions 5.1/5.5、Theorem 5.3）。
- 对 party-list，$\alpha^*_{EJR+}$ 可在 $O(k\log|P|+|P|)$ 计算、$\alpha^*_{JR}$ 在 $O(|P|)$ 计算（Theorem 6.2）。在 voter-interval / candidate-interval 域，可验证给定 committee 的 α-EJR（分别 $O(n^3k)$、$O(m^2kn)$），并在 $O(n^2m\log n)$ / $O(m^2n\log n)$ 求 $\alpha^*_{JR}$；这些不是一般 profile 的 tractability 结论（§6）。

## 局限与复现

- α 是 quota 的缩放因子而非“公平分数”：较小 α 更严格，数值下降未必能在不同 $n,k$ 或不同模型间直接比较。
- α-JR 仅要求某个群体成员获得一席认可，α-EJR 要求成员获得 $\ell$ 个认可席位，α-EJR+ 又有不同的未选候选人见证形式；不得把单一 α-JR ILP 的可解性外推到 α-EJR 优化。
- 通用 profile 中 α-EJR 验证本身 coNP-hard（Theorem 5.4），而区间域只为 α-JR optimal value 提供了明确多项式算法；α-EJR/EJR+ 在 VI/CI 域的 optimal α 仍是开放问题。
- 实验是 IC 与 Euclidean Threshold 生成的、小到中等规模合成 profile（最多 60 voters、15 candidates），每个表项平均 400 instance；其平均差距不能取代理论最坏界或真实选举行为。
- 复现需保存 approval profile、$n,m,k$、所用 $\alpha$ 候选值、tie-breaking、ILP solver/状态、VI/CI 排序证明和抽样模型参数；报告 α-JR、α-EJR、α-EJR+ 时应分别给出。

## 与 AAMAS 的关系与核验说明

该文把比例代表的阈值从统一 quota 推进到实例依赖的公平强度，连接多胜者社会选择、公平分配和机制设计。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2510.19620) 手工核对定义、定理、复杂度和受限域范围。
