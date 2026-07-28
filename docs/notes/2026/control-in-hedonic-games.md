---
title: "Control in Hedonic Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WVYI7850.pdf"
preprint_url: "https://arxiv.org/abs/2602.18506"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["hedonic_preference_model_scope", "stability_existence_barrier", "parameterized_complexity_scope", "external_control_interpretation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Control in Hedonic Games

## 一句话总结

论文首次系统研究外部控制者通过添加或删除 agent 改变 hedonic coalition formation，以“指定 agent 不单独”“指定 pair 同联盟”“grand coalition 稳定”为目标，对 friend-oriented 与 additive 表示下 IR/IS/NS/CS 给出完整复杂度分类。

## 方法与证据

- 控制目标为 NA（$x$ 不 singleton）、PA（$x,y$ 同 coalition）、GR（全部剩余 agent 构成且稳定的 grand coalition）；AddAg 从预给可添加集选至多 $k$ 人，DelAg 从原 agent 集删至多 $k$ 人。稳定性是 individual rationality (IR)、individual stability (IS)、Nash stability (NS)、core stability (CS)，而非机制激励相容或现实组织治理（§2）。
- 两个偏好表示：FriHG 将他人分为 friends/enemies，以 friend 数优先、enemy 数次级比较；AddHG 为 agent 对同 coalition 成员 utility 之和。FriHG 是 AddHG 的特例。Table 1 还区分 directed acyclic preference graph（DAG）和 symmetric graph，结论不可跨表示直接互用（§2、Table 1）。
- 对 FriHG 的 NA/PA，IR、IS、CS 的 DelAg 是 immune：若删后能达目标稳定 partition，则原实例也能达（Proposition 1）；对 symmetric preferences 的 NS 也 immune。反之 AddAg 下 IR/IS 的 NA/PA 有多项式算法，依赖 friendship graph 的最小权路径/非平凡环；CS 的 AddAg 有多项式算法，经 two-pair Steiner-network 子图（Theorems 1–2）。
- FriHG 的 NS（一般图）对 NA/PA、两种动作均 NP-complete，即使 $k=0$；对 GR，AddAg 是按 $k$ W[2]-hard 但 in XP，DelAg 对所有四种稳定概念是 P（Theorems 3–4、Table 1）。$k=0$ 的硬度说明基础 stable-partition/goal 判定已难，不能解读为“允许控制动作本身造成了全部难度”。
- AddHG 下，IR 的 NA（两种动作）NP-complete 且即使 $k=0$、仅一个 feedback arc；IR-NA-DelAg immune，但某些 DAG/symmetric AddAg 情形可解（Theorem 4、Proposition 2、Proposition 5）。IS/NS 的 NA 与 PA 都 NP-complete，并保留在 $k=0$ 的 DAG 或 symmetric 限制（Theorems 5–6）。
- AddHG 的 PA 对 IR/CS 两种动作 NP-complete，即使 $k=0$ 且 DAG 最大度 9；对 IR/IS/NS 还在 $k=0$ 的 symmetric 图上 NP-hard（Theorems 7–8）。这显示“pair 同盟”比 NA 在该表示上更顽固。
- 对 AddHG-GR，IR/IS/NS/CS 两种动作均 in XP 且按 $k$ W[2]-hard（DAG）；IR/IS/NS 在 symmetric 情形也 W[2]-hard。CS-GR 两种动作整体 coNP-complete，即使 $k=0$、symmetric（Theorems 9–11）。Table 1 的 W[2]-hard + XP 是参数化状态，不是普通多项式时间结论；CS-GR 使用不同的 coNP 验证结构。

## 局限与复现

- “控制”是假定一个外部 actor 可无摩擦添加/删除 agent，agent 的偏好固定且已知；不建模 consent、隐私、退出权、策略性谎报、招募成本、法律伦理或删除现实成员的可行性。
- 结果只覆盖 FriHG/AddHG 与 IR/IS/NS/CS；fractional、anonymous、B/W preferences、strict-core/Pareto 与破坏性控制均未被分类。不能将一个 P/immune 单元推广到未研究的偏好或稳定概念。
- 多数 hardness 在 $k=0$ 已成立，源于判断存在稳定且满足目标的 partition 的难度。报告控制算法时应分别测量基问题、预算 $k$、候选添加集和实际选人/删人构造，不能只报“NP-hard”。
- 复现应实现两种 preference encoding、每个 stability definition、目标/动作的精确定义，逐项检查 Table 1。对正结果记录 graph weights、最短路径/环或 Steiner subgraph；对硬度验证 reductions 的 $k=0$、DAG、symmetric 和最大度限制。

## 与 AAMAS 的关系与核验说明

该文将计算社会选择中的控制问题推广到 coalition formation，适合资源分配和外部治理研究。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2602.18506) 核对定义、Table 1 与 Theorems 1–11；复杂度结论均保留 preference representation、稳定概念、动作、目标及参数化前提。
