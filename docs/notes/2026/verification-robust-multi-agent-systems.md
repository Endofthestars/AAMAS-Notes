---
title: "Verification of Robust Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["safety_verification", "argumentation_reasoning", "marl_coordination"]
dblp_key: ""
doi: "10.65109/DHRR7601"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DHRR7601.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04f"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["formal-verification", "patl", "robustness", "parametric-transitions", "bounded-memory"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Verification of Robust Multi-Agent Systems

## 一句话总结

本文研究 stochastic MAS 的 robust PATL model checking：transition probabilities 可在 $\epsilon$ 范围内或由参数共同扰动，coalition 使用 observation-based、automata 表示的 bounded-memory strategies，并给出不同参数模型下的复杂度上界。

## 方法与证据

- robustness 要求 PATL specification 对所有 well-defined transition valuations 成立；automata bounded-memory 策略严格强于仅记忆最近状态的经典 recall，同时避免 unbounded recall 的不可行性（§1、§3、§5–6）。
- 对 universal reachability，表 1/Thm. 7.1–7.3 给出：$\epsilon$-perturbation 在 P；固定数量参数的 parametric MDP 在 NP∩co-NP；无界参数在 $\forall\mathbb R$。复杂度提升来自对实数参数的量化（§6–7）。
- 对 observation-based bounded-memory PATL，论文给出 $\epsilon$-perturbation 为 $\Sigma_2^P$、固定参数为 $\Sigma_2^P$、无界参数为 $\Sigma_3^{\mathbb R}$ 的 membership 结果；主要贡献是复杂度理论而非工具性能实验（§1、§7）。

## 适用边界与复现

- 结果主要是 membership，并未普遍给出 matching hardness 或可扩展实现；概率不确定性模型和固定/unbounded 参数数的选择直接决定复杂度，不能将“robust verification”理解为所有扰动下的工程可判定性。
- 复现需给出 stochastic MAS、observation relations、PATL formula、automaton memory bound、parameter constraints和量化语义；实践中还应说明参数区间来自何种统计置信或模型误差，而非任意设定。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DHRR7601.pdf) 人工核对 perturbation 模型、Theorem 7.1–7.3 与表 1；未把理论 membership 表述为已验证的工业 MAS 工具链。
