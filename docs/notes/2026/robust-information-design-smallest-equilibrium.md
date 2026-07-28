---
title: "Robust Information Design for Multi-Agent Systems with Complementarities: Smallest-Equilibrium Threshold Policies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "norms_trust_governance", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/HWRI8919"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HWRI8919.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["smallest_equilibrium_selection_assumption", "global_complementarities_only", "convex_potential_and_welfare_scope", "illustrative_case_studies_not_deployment"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Robust Information Design for Multi-Agent Systems with Complementarities

## 一句话总结

在 binary-action strategic-complementarity MAS 中，论文假定 agent 选择诱导 Bayesian game 的 smallest equilibrium，而非设计者偏好的均衡；对全局互补、精确凸势函数和凸 welfare，最优稳健信息政策是按一维 state score 的全体行动/全体不行动阈值（至多一个状态随机混合）。

## 方法与证据

- 用 feasibility 与 sequential-obedience constraints 构造 policy-level LP，刻画 smallest-equilibrium play 下可实现的 sequential recommendation policy（Theorem 4.3）。
- Theorem 5.2 在 binary-action supermodular game、convex potential 与 convex designer welfare 下推出 perfect coordination 最优；排序 state score 后，阈值规则以 `O(|Θ| log |Θ|)` 找到阈值，边界状态至多混合一次（§5）。
- vaccination-style 两状态案例中，H 推荐全体 vaccination，L 以 `p*=0.684` 混合；technology-adoption 的 `N=10` 近连续离散化例取阈值约 `0.56`、混合 `0.24`（§6）。
- 两例中的 constructive policy 匹配 LP optimum；paper 将 classical obedience-only/partial implementation 的更高 welfare 解释为依赖有利均衡选择、在 smallest equilibrium 下不可置信（§1、§6）。

## 局限与复现

- 阈值闭式结论不是一般 information design 结论：它依赖全连接的 global complementarities、有限 state、精确势博弈及凸性。network/local complementarity 会改变临界值与混合。
- smallest equilibrium 是保守的 equilibrium-selection 建模选择，best-equilibrium 与实际行为都可能不同；案例是模型化 vaccination/technology adoption，而非临床、公共卫生或市场实证。
- 信息披露涉及公平、可解释性、隐私与操纵风险；不能由 welfare LP 推出真实政策的正当性或效果。复现应公布 payoff、prior、state discretization、LP solver、score/tie rule 与完整代码。
- 作者将 local network effects、真实 vaccination data、以及改变 designer objective 作为后续方向（§7）。

## 与 AAMAS 的关系与核验说明

这是 MAS 的稳健信息设计与均衡选择理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HWRI8919.pdf) 核对 LP、Theorems 4.3/5.2、案例和适用前提；未把阈值模型外推为现实公共卫生或技术采纳政策建议。
