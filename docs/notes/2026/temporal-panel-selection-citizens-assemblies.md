---
title: "Temporal Panel Selection in Ongoing Citizens’ Assemblies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "norms_trust_governance", "game_theory_mechanism"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XBME2274.pdf"
preprint_url: "https://arxiv.org/abs/2602.16194"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["metric_representation_assumptions", "equal_panel_size_scope", "pfc_vs_prf_scope", "approximation_growth"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Temporal Panel Selection in Ongoing Citizens’ Assemblies

## 一句话总结

本文把持续性公民大会建模为一串互不重叠的随机 panel，要求每轮、累积前缀或全局群体在度量空间中获得比例代表，同时让每个人的总入选概率相等；证明了这些目标之间存在严格的条件与近似因子权衡。

## 方法与证据

- 对人口 $V$ 的代表性度量，α-PFC 要求每个大小至少 $n/k$ 的群体在 panel 中有一名距离足够近的代表；β-PRF 更强，对大小至少 $q n/k$、直径 $r$ 的群体要求至少 $q$ 名代表落在其 β 倍距离邻域（§2）。已有关系给出 β-PRF 蕴含 $(1+\sqrt2)\beta$-PFC。
- 时间选择算法输出 $ℓ$ 个不相交 panel。individual fairness 指每个人进入总并集的概率为 $\sum_i k_i/n$；panel、global、prefix representation 分别约束单轮、所有轮并集、以及每一个初始前缀（§2）。这是假定人口间存在给定 representation metric 的抽象公平模型。
- Theorem 3.1：先从 $V$ 选大小 $k_1$ 的 α-PRF panel，再从其中选大小 $k_2$ 的 β-PRF panel；仅当 $k_1$ 可被 $k_2$ 整除时，后者对原人口为 $(2\alpha\beta+\beta)$-PRF。若不可整除，存在实例使其对原人口不满足任何有限 PRF/PFC 近似（§3）。
- 对所有 panel 大小均为 $k$ 的 global（非每一前缀）情形，Corollary 3.2 给出多项式算法：global panel 为 6-PRF、每个 panel 为 26-PRF、每人进入任一特定 panel 的概率为 $k/n$（§3）。不同 panel size 的常数 PRF 推广仍是 open question。
- Theorem 4.1（相同 panel size $k$）：NestedBasedRepresentation 用嵌套群体层级，能同时使每个单独 panel 和每个 prefix 达到 $O(4^\ell)$-PFC，并保持每人进入总并集的概率 $\ell k/n$（§4）。因此这是随 panel 数指数增长的 PFC 近似，不是常数 PRF 保证。
- Theorem 5.1 放弃单独 panel 表示性后，ChainBasedRepresentation 对可变 $k_t$ 给出每个 prefix 的 $O(1)$-PFC 和总入选概率 $\sum_t k_t/n$；证明细化为 19-PFC（§5）。是否能让每个 prefix 达到常数 PRF 仍是 open question。

## 局限与复现

- 所有保证依赖静态人口、可计算且满足三角不等式的 representation metric、panel 互不重叠及给定容量；现实中人口属性、参与意愿、拒绝率、资格限制和 metric 的定义都可能变化。
- PFC 只要求合格群体附近存在一名代表，PRF 要求数量随群体规模增长。不能把 Theorems 4/5 的 PFC 结论表述为完整比例席位或真实政策偏好的 PRF 保证。
- 同时要求每轮和每个前缀的结果只有 $O(4^\ell)$ 因子；本文未证明常数因子是否可得。Theorem 3.1 的不可整除反例同样限制了直接“先选大 panel 再分割”的实践推断。
- 复现应明确 metric、群体半径、容量序列、是否所有 panel 等大、抽样/rounding 方案与随机种子；逐前缀验证 PFC/PRF，而非只检查最终全局 panel，且报告 individual selection probabilities。

## 与 AAMAS 的关系与核验说明

该文为长期轮换式公民参与设计提供比例代表与个体公平的算法化框架，属于公平资源分配、治理与机制/社会选择。笔记依据作者公开 [PDF](https://yhkalayci.github.io/temporal_sortition.pdf) 手工核对 PFC/PRF 定义、定理条件、因子和开放问题。
