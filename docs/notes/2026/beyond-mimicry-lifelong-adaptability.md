---
title: "Beyond Mimicry: Toward Lifelong Adaptability in Imitation Learning"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["agent_engineering", "generative_agents", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/LDHN8550"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LDHN8550.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04l"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["imitation-learning", "compositional-generalization", "lifelong-learning", "goal-conditioned-mdp", "blue-sky"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Beyond Mimicry: Toward Lifelong Adaptability in Imitation Learning

## 一句话总结

本文提出 Compositional Repertoire Learning（CRL）议程：模仿学习不应只复放 demonstrations，而应提取可重组行为原语与组合规则，从而在新目标与 context 下获得终身适应性。

## 方法与证据

- 文章区分 mimicry 与 adaptive behaviour，批评 average episodic reward 难以分辨轨迹记忆和真正的 compositional generalisation（§1–§2）。
- 提出 Goal-conditioned Contextual MDP：显式区分 goals、可控 contexts、observation projection 与 context distance，以便系统地改变组合条件而非只做 IID hold-out（§3）。
- 建议以 systematicity、productivity、substitutivity 等维度衡量组合泛化，并讨论 hybrid architectures、认知科学与文化演化方向（§2–§5）。

## 适用边界与复现

- 这是一篇 5 页 Blue Sky 研究议程，并未给出 CRL 训练算法、完整 benchmark 或实证胜率；其“mimicry”诊断不构成对所有 IL 方法的经验定论。
- 后续工作需实例化 primitives/composition rules、GCMDP context interventions、训练/测试组合拆分、success metrics 与 BC/goal-conditioned/hierarchical IL 基线。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LDHN8550.pdf) 人工核对 CRL、GCMDP 和评估主张；明确保留其尚待算法化和实验验证的研究议程性质。
