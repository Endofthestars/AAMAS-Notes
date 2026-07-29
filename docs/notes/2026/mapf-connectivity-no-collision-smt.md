---
title: "Modelling Multi-Agent Pathfinding Problems by Integrating Connectivity and No-Collision Constraints"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["planning_scheduling", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/BHIZ5140"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BHIZ5140.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["multi-agent-pathfinding", "smt", "monosat", "connectivity", "sat-encoding"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Modelling Multi-Agent Pathfinding Problems by Integrating Connectivity and No-Collision Constraints

## 一句话总结

本文以 SMT 分离 MAPF 的两类约束：将每 agent 的起终点连通性交由 MonoSAT 的单调图理论 propagator，碰撞避免保留为 Boolean/2-SAT，从而压缩 Pass/Shift 时间展开编码并提高部分设定的求解效率。

## 方法与证据

- MAPF 在离散时间图上要求每 agent 从 start 到 goal、无 vertex/edge conflict，优化 makespan 或 sum of costs；标准 SAT 中 transitive connectivity 造成大量 clauses（§1–3）。
- 作者把 Pass（顶点/边移动）和 Shift（相邻时刻相对移动）两套 encoding 改写为 Graph variants，利用 MonoSAT s--t connectivity，collision constraints 由 SAT 层处理；另有禁止 phantom agents 的 Pass+Graph+(3) 版本（§3）。
- 在 20×20 至 100×100 的 empty/random/warehouse grids 和三张大型游戏地图上，单 CPU、5 分钟/instance、64GB 条件评估。Pass+Graph 在 makespan 解出的 instances 超过纯 Pass 两倍、sum-of-costs 多约四分之一；Shift+Graph 对 sum-of-costs 则变差（§4–5）。

## 适用边界与复现

- 比较固定 MonoSAT/SAT 求解器下的 encoding，不与 CBS 等不同范式最优 MAPF solver 横比；结果随图密度、cost objective 和 propagator 强度变化，不能概括为所有 MAPF 更快。
- 复现需公开实例生成、horizon/cost bound 搜索、Pass/Shift/Graph clauses、MonoSAT/PBlib 版本及参数、硬件/5 分钟限制、随机 scenario 与 solved-instance 原始表。应扩展到更多拥堵、动态障碍和持续占据目标模型。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BHIZ5140.pdf) 人工核对 encoding 分工、实验协议和作者的相对性能结论；未把 encoding 规模减少混同为所有实际机器人调度的端到端优势。
