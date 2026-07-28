---
title: "The Reachability Objective in Multi-Agent Path Finding"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: "10.65109/OOLP5568"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OOLP5568.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["grid_simulation_only", "reachability_objective_scope", "sixty_second_time_limit", "solver_and_dummy_target_dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# The Reachability Objective in Multi-Agent Path Finding

## 一句话总结

MAPF-RO 只要求每个 agent 曾到达 target、之后可继续移动，不要求同时停在 target configuration；论文据此改造 LaCAM 为 complete 的 LaCAMRO，提出 PIE_RO anytime 版本，并把 MAPF with Unassigned Agents 规约为 RO，在 grid simulation 中对高密度实例提升 coverage/runtime，但不保证经典 MAPF 目标或现实机器人约束下同样获益。

## 方法与证据

- MAPF-RO 的输入与 classic MAPF 相同，但解只需每条 collision-free path 包含其 target；目标到达可异步，已到达 agent 能移开，从而避免密集图中“最终全占 target”的滑块难题（§1--3）。
- LaCAMRO 对已完成任务的 agent 使用 dummy targets，并给出多种选择策略；Theorem 1 说明其对 MAPF-RO complete。PIE_RO 交错规划/执行以得到 anytime 解，但不声称最优（§4）。
- 在 standard grid maps 与高密度 empty grids 上比较现有 RO、classic MAPF 与 LaCAMRO variants；Java 18 在 Linux VM、每 solver 60s。报告 coverage 与 cost/SST，部分情形相对基线多解约 1,000 agents（§5）。
- 进一步将 MAPF-UA 中无任务 agent 通过 target/RO reduction 处理；规约保留 RO 侧的 soundness/optimality/completeness 性质，并在 1,600 instances 上比较（§6）。

## 局限与复现

- RO 是不同任务目标：允许 agent 离开 target 对 search/rescue 或 lifelong task 合理，却不适用于必须占位、充电、交付后停靠或经典 MAPF final configuration 的任务。
- 结果来自 grid、60-second cutoff、Java/VM 与特定 dummy heuristic；coverage 不等于实时安全、路径平滑、动力学可执行性、通信延迟或多机器人物理碰撞率。
- CBSRO 有 optimal/sound/complete 性质但难扩展；LaCAMRO 的 complete 性也不等于最优或在受限动作模型下可行。应公开 instances、seed、CPU/内存、timeout、所有参数与每实例 runtime。
- 作者指出可改进 LaCAMRO 的 solution quality、扩展 MAPF-UA solver；应在连续/异构机器人及真实仓储任务分配下重测（§7）。

## 与 AAMAS 的关系与核验说明

本文属于多智能体路径规划和任务目标建模。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OOLP5568.pdf) 核对 RO 定义、LaCAMRO completeness、PIE_RO、实验 cutoff 和 MAPF-UA 规约；未将模拟 coverage 表述为实体系统性能或通用 MAPF 优越性。
