---
title: "Bayesian Network Structure Learning through Large Language Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "generative_agents"]
dblp_key: ""
doi: "10.65109/SGHT1267"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SGHT1267.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03e"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "llm_causal_claims", "data_free_structure_learning", "benchmark_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Bayesian Network Structure Learning through Large Language Models

## 一句话总结

DCA 以 Decider--Critic--Arbiter 对变量 triplets 作因果判断，再按跨 triplet 出现频率计算 edge confidence，删冗余 edge 和 cycle 中最低置信 edge 来输出 DAG。Cancer/Alarm/Hailfinder 表中 DCA 无 cycles，且在 Cancer/Alarm 有较优 SHD/F1；但 LLM 的语义判断与删环只保证图结构合法，不证明因果方向真实或可用于医学/风险决策。

## 方法与证据

- Decider 提出 hypothesis，Critic 检查/反驳，争议由 Arbiter 决定；triplet 取代 pair context（§2）。
- refinement 先让 LLM 移除可由间接路径解释的 edges，再以 occurrence-ratio confidence 打破 cycles（§2）。
- Hailfinder 上 Zero-shot/CoT 的 SHD 较低却有约 21 isolated nodes，DCA 为 0 cycles/0 isolated nodes；ROT 有 252.67 cycles（Tables 1--2）。这未验证 ground-truth causality、prompt sensitivity或外部数据泛化。

## 适用边界与复现

- 仅适合文本先验生成候选图；应由领域专家和数据/干预证据独立验证。复现须固定 LLM、prompt、triplets、votes/edge confidence、删环规则和 seed，并检查 DAG、SHD、F1及 node coverage。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SGHT1267.pdf) 人工核对 DCA、refinement 与 Tables 1--2；未把 DAG 合法性写成因果真值。
