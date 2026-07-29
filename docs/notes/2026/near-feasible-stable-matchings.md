---
title: "Near-Feasible Stable Matchings: Incentives and Optimality"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/RZEM3915"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RZEM3915.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03h"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "nonbipartite-many-to-many-model", "capacity-modification-scope", "complexity-result-scope", "random-instance-experiments"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Near-Feasible Stable Matchings: Incentives and Optimality

## 一句话总结

论文在 non-bipartite many-to-many Stable Fixtures 中用 capacity modifications 使实例可解，并以 blocking entries 量化近可行 matching 的个体/总偏离激励。MIM/MAM 同时最优的 capacity function 可二次时间求，单 agent capacity change 至多 1；MIDI/MADI 的复杂度取决于 capacity restrictions。这是匹配模型内的稳定性/激励度量，不自动产生现实市场公平、可接受性或真实偏好结论。

## 方法与证据

- MIM/MAM 分别最小化最大/总 capacity modifications；允许 ± 或仅 + 时存在同时最优 \(c'\)（§2）。
- blocking entry 推广 blocking pair；MIDI/MADI 分别最小化最大/总阻塞项。无 capacity violation 时 MIDI para-NP-hard、MADI NP-hard且 XP；无 restrictions 时二者在 P（§2）。
- 作者还称可同时最小化 blocking 指标且不差于最优 capacity modification；实验为 uniformly random preferences，完整结果在 arXiv full version（§2--3）。

## 适用边界与复现

- 复现须公开 preference model、capacities、permitted modification set、matching definition和 blocking-entry counts；对真实市场应补充偏好 elicitation、策略申报、法定容量和分配公平约束。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RZEM3915.pdf) 人工核对概念、复杂度与结论；未将 near-feasible stability 夸大为实务公平保证。
