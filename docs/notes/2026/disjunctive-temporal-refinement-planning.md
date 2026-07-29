---
title: "Disjunctive Temporal Refinement Planning with Variable Action Duration and Execution Makespan Bounds"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/ZRWF2944"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZRWF2944.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03j"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "variable-duration-assumption", "modified-pddl", "benchmark-only", "satisficing-solver"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Disjunctive Temporal Refinement Planning with Variable Action Duration and Execution Makespan Bounds

## 一句话总结

本文处理行动时长可变、且执行 makespan 须落在下/上界的 temporally-uncertain execution：plan 必须在 minimum 与 maximum temporal networks 都无潜在 violation。扩展 PDDL 以 `:tuep` 和 `:makespan-constraint` 表达约束，并以 Titan 的 time-last/over-time-critical refinement 在四个修改 IPC 2002 domains 比较。结果是 benchmark 中的 satisficing planning 表现，非真实执行可控性或必然无重规划保证。

## 方法与证据

- 常规 STP 只对应 minimum makespan；该问题要求任意动作时长范围下不破坏条件/time windows，摘要称潜在 EXPSPACE-complete（§2）。
- makespan-constraint 可写比较或双边界；TIL/PDDL3 preferences 可模拟但需 dummy predicates（§3）。
- Table 1：OTC 总体 solve 更多，已知 optimal makespan 时 TL 常更快；Titan 使用 satisficing resolver，因此 OTC 的 no-solution 不代表完整 search space 已证明不可解（§4）。

## 适用边界与复现

- 复现须公开 action duration intervals、bounds、PDDL extensions、Titan version/heuristic、OTC/TL params和 timeout；部署需接合 STNU/dispatch、传感器延迟、资源冲突与安全 fallback。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZRWF2944.pdf) 人工核对问题、语法和 Table 1；未把 plan validity 写成现实执行保证。
