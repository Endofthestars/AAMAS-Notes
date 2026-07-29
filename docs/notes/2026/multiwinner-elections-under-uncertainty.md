---
title: "Strategic Behavior, Fairness, and Social Optimality in Multi-Winner Elections under Uncertainty"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "norms_trust_governance", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/GEVH7247"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GEVH7247.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03t"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "drl-equilibrium-approximation", "ordinal-to-cardinal-mapping", "impartial-culture-model", "regulatory-threshold"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Strategic Behavior, Fairness, and Social Optimality in Multi-Winner Elections under Uncertainty

## 一句话总结

本文以独立 DRL voters 近似 multi-winner approval voting 的均衡：完整信息下会学习到操纵；不完整信息下会收敛为 approve top-$k$ 的 cutoff strategies。这些策略在作者实验里通常满足比例公平指标但不最大化功利福利；最低批准数 $\lfloor0.4K\rfloor$ 在约半数试验提升福利、仅 3% 降低。

## 方法与证据

- 研究 seq-CC、seq-PAV、MES，voters 有私有 ordinal rankings 和从 ranking 以 linear/convex/concave 映射得到的可分 cardinal utilities；preference profile 取 impartial culture、Euclidean、Mallows（§3）。
- 单阶段同时博弈中，agent action 是 approval ballot、reward 是当选 committee utility。DRL 不设计规则，而是数值近似 BNE；最多 40 voters、20 candidates，评估 $\epsilon$-BNE、welfare、truthful prefix 和 JR/PJR/EJR/Priceability/core 等（§4）。
- 完整信息实例中有利操纵会被学到；Bayesian settings 中策略为 top-$k$ cutoff，$\epsilon\le0.05$、胜过随机投票。seq-PAV/MES 的批准数多于 seq-CC（§5）。
- 576 个 reduced cutoff-game experiments：要求最少 $\lfloor0.4K\rfloor$ approvals 约半数严格提高 welfare、仅 3% 降低；实验中的 committee 都满足所测公平性指标，但这不是一般理论保证（§5）。

## 适用边界与复现

- DRL 收敛不等同于严格 BNE 证明，结果依赖 utility mapping、偏好分布、architecture/training seeds 和限定的 rules。观察到公平不排除未测 profile 或策略下的公平反例。
- 复现应公开 profile generators、candidate/voter/committee sizes、utility normalization、rule implementations、RL algorithm/rewards/training budget、out-of-sample evaluation、reduced-game solver 与最低批准阈值。实际制度变化需考虑信息披露、选民认知与权利影响。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GEVH7247.pdf) 人工核对模型、实验规模和 regulatory 结论；未把模拟均衡表述为现实投票行为预测。
