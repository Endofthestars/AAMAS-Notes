---
title: "When LLM Agent Teams Fail at Topological Spatial Reasoning Under Partial Observability"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/RTFT9958"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RTFT9958.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03j"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "text-only-simulator", "full-map-prompt", "small-episode-sample", "model-version-dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# When LLM Agent Teams Fail at Topological Spatial Reasoning Under Partial Observability

## 一句话总结

论文以 text-only bomb-defusal graph task 隔离 LLM team 的拓扑空间推理：agents 在局部观察下用公共 chat 同步，full-map encoding 与 belief template 形成记忆接口。3 agents/5 bombs 下，o4-mini 从 5 nodes 的 90 分降至 100 nodes 的 20±8.17，Llama-3.1-70B 53 nodes 仅 6.67±4.71（Table 1）。这说明特定接口/模型/任务的 scaling failure，不是现实多机器人或所有 LLM 协作能力的定论。

## 方法与证据

- 环境为无权连通 graph，agent move/inspect/cut 并在 chat log 协调 hidden bomb phases；invalid outputs 由 rule feedback 回报（§2）。
- experiment 使用 full-map encoding、no dropout、3 agents、5 bombs，仅改变 map size；score 最大 90，失败 horizon 为 100（§3）。
- 作者将 communication dropouts、不同 encoding 和 memory 设计留为 future work，故未证明具体修复方案或 partial-observability 下的鲁棒 coordination（§3.2）。

## 适用边界与复现

- 复现须固定 graph generation、map serialization、prompt/model versions、chat budget/template、bomb phases、sampling和 episode seeds；分报告 invalid actions、completion/rounds/score。真实任务还需感知、通信丢失、执行安全与人类监督测试。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RTFT9958.pdf) 人工核对 task 和 Table 1；未将 benchmark failure 写成普适推理能力测量。
