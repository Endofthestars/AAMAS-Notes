---
title: "Multi-Agent Cooperative Transportation: Optimal and Efficient Task Allocation and Path Finding"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "resource_allocation", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/WZSB2882"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WZSB2882.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["discrete_grid_assumption", "sum_of_costs_objective", "centralized_planning", "known_static_tasks", "small_synthetic_benchmarks", "suboptimal_selector_dependence", "no_physical_transport_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Agent Cooperative Transportation: Optimal and Efficient Task Allocation and Path Finding

## 一句话总结

论文定义 CT-TAPF：多机器人需组队占据 cooperative task 的多个 slots、集合后共同搬运，并在二维图上完成无冲突路径；CT-TCBS 以 A*、增量 team-assignment expansion 和 MC-CBS 求 SoC 最优解，另以 Best/ Worst Task 选择器换取运行时间。最优性仅针对静态、离散、集中式且模型完全已知的定义，实证规模为合成网格，尚未证明真实仓库协作运输的可行性或安全性。

## 方法与证据

- CT-TAPF 在无向二维图上给出 \(n\) agents 和 \(m\) tasks；每个 task 需要 \(k_i\) agents 到达相连的 start-slot 配置后，作为大实体共同移至 goal，目标最小化全部 agent 的 sum of costs（§3）。agent 每次至多占一个 task slot，且假设 \(n\ge\max_i k_i\)；没有处理动态订单、故障、载荷不确定性、连续动力学或人机共域。
- CT-TCBS 是两层 A* 搜索：高层处理 task assignment 与冲突约束，低层为独立/大 agent 规划路径；Incremental expansion 逐步扩张协作 team，避免对所有 agent-slot 组合的直接枚举（§4）。这仍是 NP-hard 问题的集中式求解，不给大规模实时上界。
- §4.7 的最优性论证要求 composite heuristic 可采纳、每一步成本非负、以及 MC-CBS 约束只删去碰撞计划而不删最优无冲突计划。因此“provably optimal”指论文定义下的 SoC optimum，不包含执行延迟、能耗、吞吐、公平、鲁棒性或连续世界碰撞安全。
- 次优 CT-TCBS-BT/WT 每轮只扩张一个全局挑选的任务：BT 选预计最易完成、WT 选最难完成，任务难度由 Hungarian assignment 的无约束到达/执行成本估计（§4.8）。选择器是启发式，放弃最优保证；场景结构会改变 BT/WT 的成功率和质量。
- optimal 分析在 25 个 8×8、至多 8 tasks/6 agents、全为二人任务的 collision-rich 合成实例上进行；跨方法分析为 50 个 16×16、10% 障碍、最多 15 tasks/5 agents 的 random/spatially-biased 实例，最大例为 9 个单人、3 个双人、2 个三人和 1 个四人任务。每例受 500 s 和 4 GB 限制（§5）。
- Incremental 的成功率显著高于 Incremental-LR/Combinatorial，且成功实例的 task-expansion 对 conflict-expansion 中位比为 9.54；MAX-d conflict resolvers 在该集成问题中扩张更多节点（§5.1）。这些是特制冲突网格的搜索行为，不是所有 CBS 方法的一般排序。
- Table 3 的 372 个共同解实例中，Optimal 为 \(203.30\pm201.75\) s、0% gap，WT 为 \(107.33\pm165.36\) s、\(3.47\pm5.81\)% gap，Greedy-PP 为 \(0.03\pm0.01\) s、\(24.06\pm22.20\)% gap；WT 在 random layouts 的成功率倾向更高、BT 在 spatially-biased layouts 更好（§5.2）。结果未覆盖真实布局、机器人通信、同步搬运误差或实际装卸时间。

## 适用边界与复现

- 适用于静态、全局可观测的离散仓储/物流抽象中，研究 task team formation、slot assignment 与 collision-free MAPF 的耦合；若任务需要持续感知、非刚性载荷、复杂抓取、异构机器人或分布式自治，应重新建模与验证。
- SoC 最优可令个别机器人等待较久，并不等同于 makespan、吞吐、能耗、服务等级或劳动/安全公平最优。任务 start slots 未保留的建模选择、团队视为大实体、图连通与完美通信假设都可能改变真实系统结论。
- 复现需固定地图、任务 type/slot/start/goal、agent 初始点、冲突模型、SoC 定义、A*/heuristic、Incremental/LR/Combinatorial 和 MC-CBS resolver、BT/WT/Hungarian 成本、timeout/memory 及随机生成器。报告 success、SoC、optimality gap、节点扩张、墙钟、内存和不可解/超时实例。
- 部署前应在高保真连续仿真及现场做载荷、控制误差、定位噪声、通信丢失、人类障碍物和紧急停止测试；中央图搜索得到的路径不构成碰撞安全或协作搬运成功的保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多机器人规划、任务分配和 cooperative MAPF 论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WZSB2882.pdf) 核验 CT-TAPF 定义、CT-TCBS 的 A* 最优性条件、BT/WT、实验规模、Table 3 和场景依赖结果；没有把离散 SoC 最优或有限合成成功率误写为真实物流效率、可靠性或物理安全保证。
