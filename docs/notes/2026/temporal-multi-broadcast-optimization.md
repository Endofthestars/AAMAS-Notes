---
title: "Temporal Multi-Broadcast Optimization"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/ITHO9185"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ITHO9185.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02m"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["temporal_graph_assumptions", "distance_measure_scope", "offline_schedule_assumption", "complexity_not_deployment_performance"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Temporal Multi-Broadcast Optimization

## 一句话总结

论文定义 D-Temporal Multi-Broadcast：给定静态图、边的 traversal/multiplicity 约束和多个 sources，离线安排边的可用时间，以最小化 sources 到所有节点的最坏 temporal distance；比较六种时间距离下的复杂度与近似界。

## 方法与证据

- temporal distance 包括 Earliest-Arrival (EA)、Latest-Departure (LD)、Fastest-Time (FT)、Shortest-Traveling (ST)、Minimum-Hop (MH)、Minimum-Waiting (MW)，它们通常不满足 triangle inequality（§1）。
- D-TMB 的 scheduler 为 edge--time pairs 分配 labels，受 multiplicity 限制；固定基础设施下优化 source 到所有 vertices 的 worst-case D。作者也说明其与 D-ReachFast 在每种 D 下的等价（§1.2）。
- Single-source：EA 与 LD 可解；对 FT/ST/MH/MW，判定给定值可行 NP-complete。ST/MH 不可近似优于 2；FT/MW 的不可近似因子与节点数指数或输入权重/距离函数有关，且文中给 matching 简单近似（§1.2）。
- Multi-source：任意 D 下即使只判定可行性也 NP-complete，且固定多于一个 source 仍成立；EA/LD 在 multiplicity 至少为 sources 数，或底层图为 tree 且每边 multiplicity 至少 2 时有多项式算法（§1.2）。

## 适用边界与复现

- 结论针对离线、已知 static graph/traversal/multiplicity 的 temporal graph；不直接解决在线故障、随机延迟、排队、容量竞争、安全策略、信息/货物异质性或分布式协议开销。
- 选择 D 会改变“好”的含义：最早到达、总在途时间、跳数和等待时间不能互换；复杂度/近似因子不等于物流、无线网络或信息传播的实际 SLA。
- 多 source 的一般不可行/NP-complete 结果强调需先明确 feasibility 条件，不能假定任意 schedule 可广播成功。
- 复现需提供图、sources、edge traversal function、multiplicity、time-label domain、选定 D、reductions/algorithms与最坏实例；应用评估还应加入动态不确定性和实际调度成本。

## 与 AAMAS 的关系与核验说明

这是 temporal graphs 上的多智能体/多源调度理论。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ITHO9185.pdf) 核对 §1--1.2 的问题定义与复杂度分类，未把离线理论结果转写为现实网络性能声明。
