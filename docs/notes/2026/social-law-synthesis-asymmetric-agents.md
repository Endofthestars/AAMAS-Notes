---
title: "You Can Go First — Planning for Social Law Synthesis in Asymmetric Multi-agent Settings"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "planning_scheduling", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/FAZU7063"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FAZU7063.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03i"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "asymmetric-roles", "regimentation-only", "optimal-primary-plan-assumption", "ipc-benchmark-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# You Can Go First — Planning for Social Law Synthesis in Asymmetric Multi-agent Settings

## 一句话总结

论文为 privileged primary P 与 secondary S 的非对称 dyadic team 综合 social norms：额外 P goals \(G_N\) 与精确 S plan \(\pi_S\)，要求存在 P-acceptable plan 且所有满足 norms 的 optimal P plan 不与 joint plan 冲突。给 Stackelberg 与 FOND strong-policy compilations；IPC variants 中 FOND 在 Blocksworld 较好、Stackelberg 在部分 Gripper/Logistics 较好。这是 STRIPS/planning 模型内的 sound/complete 综合，不等同于人机优先权、同意或现实社会规范合法性。

## 方法与证据

- Stackelberg leader 选 norms，follower 试图证明 C1/C2 失效；FOND 将 P choices 设为 non-determinism，S 找强策略（§2--3）。
- S plan length 有 \(k\) bound；评估采用 symbolic Stackelberg 与 PR2，在 IPC variants 表现互补（§3）。

## 适用边界与复现

- 复现应公开 agent goals/actions/costs、privilege assumptions、\(k\)、C1/C2、planner configs和 instances。真实 HRI 需参与者偏好、权限、碰撞安全和人工覆盖；regimentation 不能替代治理程序。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FAZU7063.pdf) 人工核对 norms、两 compilation 与 benchmarks；未夸大为现实社会律认证。
