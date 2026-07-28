---
title: "Practical approach to 2-Euclidean Preferences"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TNYC5178.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["recognition_complexity_scope", "heuristic_certificate_scope", "benchmark_generalization"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Practical approach to 2-Euclidean Preferences

## 一句话总结

论文提出实用型 2-Euclidean election 识别/反驳流程，组合 forbidden patterns、reduction rules、ILP 与改进 QCP，在 PrefLib 基准上显著减少 Unknown，但不改变一般识别的 $\exists\mathbb R$-complete 性。

## 方法与证据

- 2-Euclidean 意味 voters 和 candidates 可嵌入 $\mathbb R^2$，且排序由到 voter 的距离严格决定；对 $d\ge2$ 的识别问题为 $\exists\mathbb R$-complete（§1）。
- 方法首先用 3-8 pattern 与基于 voter convex hull 的 forbidden substructures 找 no-certificate；这种不完整 characterization 能反驳部分实例，找不到模式并不证明 yes（§1、§3）。
- reduction rules 去除可简化部分；ILP 用 embedding graph 的必要性质反驳，QCP 扩展既有方案以尝试构造 embedding（§1、§4–6）。
- 实验把 PrefLib unresolved instances 从既有方法的 343 降至 60，并报告 98.7% PrefLib instances 在 1 秒内解决；这些是指定实现、硬件与基准下的经验结果（§1、§7）。

## 局限与复现

- Unknown 是该实用流程的合法输出，不能被当作 2-Euclidean 证明或反例。
- 禁止子结构、ILP refutation 与 QCP embedding 的证据强度不同；应保存 yes/no certificate、求解器状态、时间限额与 reduction log。
- PrefLib 结果不等于任意合成、对抗或更大选举上的同等覆盖率。

## 与 AAMAS 的关系与核验说明

该工作为受限偏好选举提供实践识别工具。笔记依据官方公开 [AAMAS PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TNYC5178.pdf) 核对了复杂度、pipeline 和基准范围。
