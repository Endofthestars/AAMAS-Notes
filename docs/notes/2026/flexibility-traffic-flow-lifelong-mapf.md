---
title: "Flexibility-Based Traffic Flow Optimisation in Lifelong Multi-Agent Path Finding"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "marl_coordination"]
dblp_key: ""
doi: "10.65109/IRBO1733"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IRBO1733.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["simulation_benchmark_only", "grid_map_and_pibt_dependence", "task_arrival_model_scope", "hardware_specific_runtime"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Flexibility-Based Traffic Flow Optimisation in Lifelong Multi-Agent Path Finding

## 一句话总结

PTFO 为 LMAPF 中每个 agent 的所有等长最短路径构建 OCPG，并按这些路径的概率分布估计期望拥堵，以指导 PIBT 的下一步；在四个 grid benchmark、最多 16,000 agents 的模拟中提高完成任务数，但收益依赖路径等价、PIBT、任务分配和特定地图/机器配置。

## 方法与证据

- 现有 TFO 只按一条预先计算的 guide path 估计流量，忽略运行时 low-level planner 会选择其他等成本路径。PTFO 用 optimal-cost path graph 表示所有 cost-equivalent path，再聚合其 edge traversal probability 为 traffic flow（§3--4）。
- 流量被转成 guidance heuristic，和 PIBT 的局部冲突处理结合；提供全量 PTFO、采样版 PTFO_S、带 refinement 的变体。大图用 30% agents 的 flow 近似以压低 OCPG 计算（§5）。
- 对 PIBT 与 TFO/TFO_Re，在 sortation_small、room-64-64-8、ost003d、warehouse_large 测试；前三张地图使用 32 核 AMD EPYC-Rome，最大 warehouse 为 16,000 agents，报告任务完成数和每 timestep response time（§6）。
- 作者称多数规模下 PTFO 系列吞吐更高；sortation_small 接近 PIBT 的两倍；在 14,000 agents 的大图，PTFO_Sa30 约为 PIBT 吞吐两倍。数字来自模拟图表，不是实体仓储部署（§6）。

## 局限与复现

- 方法假定离散 grid、等成本 shortest paths 和 PIBT 风格的实时偏离；连续运动、转向/动力学、异构机器人、通信延迟、失效和安全距离没有验证。
- throughput 受外部 goal/task 产生器、地图、密度、time limit 与 CPU 实现影响；论文也注明实验 time-limit 控制并不完美，不能只凭完成数比较 runtime。
- 16k 场景依赖 30% sampling；应公开 OCPG 构建、sampling seeds、任务序列、所有实例和 response-time 原始值，并将内存/GC、预处理与在线开销分开报告。
- 作者提出优化 OCPG search-tree、进一步降低计算与研究更高效 flow approximation；真实系统需在机器人/仓储 trace 上重测延迟、碰撞率与任务公平性（§7）。

## 与 AAMAS 的关系与核验说明

本文是大规模持续多机器人路径协调与拥堵引导工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IRBO1733.pdf) 核对模型、PTFO、benchmark 规模、指标和作者对实现性能的讨论；未把 grid-simulation 吞吐提升外推为生产仓库保证。
