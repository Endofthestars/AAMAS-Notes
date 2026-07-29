---
title: "Diagnosing Faults in Deep Reinforcement Learning based Systems: Settings and Benchmarks"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["safety_verification", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/NSTI8981"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NSTI8981.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04m"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["reinforcement-learning", "fault-diagnosis", "benchmark", "simulator", "blue-sky"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Diagnosing Faults in Deep Reinforcement Learning based Systems

## 一句话总结

本文定义 RL Diagnosis（RLDX）：给定 policy、环境 simulator 与异常 observations，在一致性低于阈值时辨识导致 DRL 执行异常的根因，并提供 AI Gym faulty-execution benchmark 方向。

## 方法与证据

- 用 MDP policy 与 stochastic simulator 形式化正常执行，以 `consistent(Obs, policy, simulator)` 判断观测能否由正常过程生成（§3）。
- 讨论 weak/strong fault model、按 action/state 等不同粒度定义 component、全/部分观测及不同 fault persistence 等诊断设定（§3）。
- 贡献是 RLDX 问题谱系和 benchmarks；诊断可辅助 repair/replanning，但论文不提供已证实的通用诊断或修复算法（摘要、§1–§5）。

## 适用边界与复现

- 需要可信 simulator、policy access 和合理 observation model；simulator mismatch、分布漂移与多重故障可使根因不可辨识。
- 复现须公开 Gym version、policy/training seeds、fault injection、trace/observation visibility、threshold、diagnostic ground truth 和 precision/recall/repair utility。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NSTI8981.pdf) 人工核对 RLDX、fault settings 与 benchmark 贡献；未将 diagnosis benchmark 等同于运行时安全保证。
