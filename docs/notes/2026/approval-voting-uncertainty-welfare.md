---
title: "Social Welfare Maximization in Approval-Based Committee Voting under Uncertainty"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RABQ9914.pdf"
code_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["complexity_by_uncertainty_model"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Social Welfare Maximization in Approval-Based Committee Voting under Uncertainty

## 一句话总结

论文研究不确定批准偏好下委员会的社会福利分布、成为社会福利最大化委员会的概率以及存在鲁棒委员会的计算复杂度。

## 方法与证据

- 将经典 Approval Voting 扩展到 Lottery、Candidate Probability 等不确定偏好模型，定义 `SW-Dist`、`SWM-Prob` 和 `ExistsSWM-Prob`。
- Theorems 3.1–3.2 表明在 Lottery 和 Candidate Probability 模型下，给定委员会的社会福利分布可多项式时间计算。
- 对 `SWM-Prob`，Theorem 4.1 给出 Lottery 模型的 NP-hardness，Corollary 4.2 给出精确概率计算的 #P-completeness；Theorems 4.4–4.5 给出 Lottery 模型阈值 1 与 Candidate Probability 模型的多项式结果。
- Theorem 5.1 显示 Lottery 模型的 `ExistsSWM-Prob(p)` 仍难，Theorems 5.3–5.4 刻画阈值 1 的可解情形。Theorem 6.2 仅在 3VA 模型下给出期望社会福利最大委员会的 `(1/2,1/2)` 鲁棒性；Theorem 6.3 指出该结论不延伸到一般 Candidate Probability 模型。

## 局限与复现

- 每项复杂性或鲁棒性结论依赖特定不确定模型、阈值和福利定义，不能相互替换或视为一般投票结论。
- 分析聚焦委员会与批准集合交集大小定义的社会福利，未覆盖任意偏好或满意度函数。
- 复现需依据 §§2–6、Table 1 和各定理中的模型表示、阈值及委员会大小条件。

## 与 AAMAS 的关系与核验说明

工作结合计算社会选择与不确定推理。笔记按不确定模型逐项记录正负复杂性结果，尤其保留 3VA 鲁棒性结论的适用范围。
