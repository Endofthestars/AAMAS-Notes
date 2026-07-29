---
title: "Network-based Active Learning for Identifying Illicit Actors in Financial Transaction Networks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/GOCK1684"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GOCK1684.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03i"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "financial-crime-labels", "imbalanced-data", "synthetic-and-bitcoin-datasets", "not-investigative-proof"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Network-based Active Learning for Identifying Illicit Actors in Financial Transaction Networks

## 一句话总结

C2 AL 同时训练 content-only 与 collective classifier，在二者预测不一致 nodes 上按两模型 entropy 聚合查询，并以 clustering 做 diversity 而非多数类判断。六个 Bitcoin/AMLworld networks 中，达到 fully supervised XGBoost+CC 的 75% F1 所需标签最多少 48%；它仅提高人工调查的优先级，不构成违法认定、账户处置或合规结论。

## 方法与证据

- CC 将 1-hop in/out neighbors 的预测标签比例加入 features；CO/CC 使用 XGBoost（§2）。
- Table 1 中 C2 AL 在 Ell++W 需 3,840 labels（AL 6,820），LI-Small 是唯一预算内达到 target 的方法（16,400）；六数据 illicit rate .7--2.2%、90/10 split、5 seeds（§3）。
- label noise、时间漂移、执行者对抗、跨链转移和 false positives 未被摘要的受控实验充分覆盖。

## 适用边界与复现

- 必须保留 analyst review、溯源、误报申诉与隐私/公平审计；复现应公开 split、budget、features、query batches、threshold、seeds与 precision/recall。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GOCK1684.pdf) 人工核对算法、数据和 Table 1；未把分类输出写成执法证据。
