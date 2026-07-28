---
title: "Multi-Agent Pickup and Delivery with Heterogeneous Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "marl_coordination"]
dblp_key: ""
doi: "10.65109/GKGU6726"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GKGU6726.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["grid_and_discrete_time_assumption", "static_operable_zones_and_capabilities", "shared_token_coordination", "fixed_handover_frontiers", "task_assignment_exponential_worst_case", "simulation_only", "small_task_count"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Agent Pickup and Delivery with Heterogeneous Agents

## 一句话总结

论文将 online MAPD 扩展到按 class 划分、各自只能在 operable zone 内移动并有 item-category/capacity 约束的异构机器人；一个 request 可由多类 agent 经 zone frontier handover 接力完成。框架先在 zone 图上为 item batch 规划最少 zone/exchange 的高层路径，再把每段转成子任务，在各 zone 内用 Token Passing（TP）分配并以时空 Dijkstra 生成无碰撞路径。医院、超市和工地三张模拟地图上的 20 个动态任务显示其 makespan/service time 优于一个顺序子任务 TP 基线；这不是对任意实际物流、连续运动、网络延迟或大任务流的最优性与实时性保证。

## 方法与证据

- 环境是四连通 grid/无向图、离散时间；同一 class 的 agent 共享静态 operable zone、可搬运 item categories 和容量。任务是有限 online stream，每个 request 含多个 item categories、一个目的地，允许不同 item 在不同时间送达（§4）。zone 不连通、能力/地图动态变化、连续动力学和同步 handover 失败不在该建模内。
- 高层先为每个 item category/batch 选 pickup location；按可达 capacity 分批后，在由可承运 zones 组成的图上选最短路径以减少 zone 数/交接次数。再以 frontier nodes、pickup/delivery 与占用 penalty 构成 item planning graph，Dijkstra 选择 exchange locations（§5.2）。pickup location 是随机选择，exchange 位置固定而非全局联合优化，故该启发式不保证最小 makespan 或最优资源利用。
- 每条跨 zone item path 被改写成有 precedence 的 pickup–delivery subtasks；下一段只在前一 handover 后生成。相同 delivery 的多个 subtask 可组合给同一 agent，区内用 TP shared token 和时空 Dijkstra 避免 vertex/edge collisions（§5.3）。这要求共享 token/任务管理器状态正确、同步且可访问；区间通信和边界 handover 的可靠协议并未展开验证。
- 复杂度：高层 zone 路径为 \(O(E+N\log N)\)，frontier planning graph 为 \(O(F^2+F\log F)\)，每 batch 重复；选择一组同 destination subtasks 的最坏情况是 \(O(2^T)\)，每 agent 时空规划为 \(O(LT_{max}\log(LT_{max}))\)（§5.4）。因此 agent 数、批量、frontier、horizon 或同目的地 subtask 数上升时，不能由小地图结果外推为可扩展实时保证。
- 实验为 hospital (40×60, 2 classes, 每 class 9 agents)、grocery (60×40, 6 classes, 每 class 6)、construction (60×40, 8 classes, 每 class 3)，每场景 20 tasks、Poisson/exponential arrival（\(\mu=0.4\)），item/task 配置随机；基线是将每 item 单独、一次执行一个 pickup-delivery subtask 的 TP 变体（§6.1）。没有现成异构 MAPD baseline，比较并不能建立相对其他异构规划器的优势。
- 作者报告所提方法在三图中 makespan、service time 和 serviced subtasks 均优于该基线，约将 subtasks、makespan 和 service time 减半；运行时间在 grocery/construction 与基线近似（约 120/500s），但 hospital 更慢（约 500s vs 200s），归因于高容量 supplier 带来的组合计算（§6.2）。更多 classes 时 service time 下降也同时增加总 agents，不能单独归因于 heterogeneity。

## 适用边界与复现

- 适用于仓储/医院等可离散化、能力和可操作区域相对稳定、跨区交接点明确的多机器人配送原型；适合将异构性显式变为跨 zone 的依赖与交接约束。
- 部署前应验证真实机器人的连续路径、载荷/操作时间、交接容错、通信延迟/丢包、token manager 一致性、任务取消/优先级、动态障碍/故障与交通拥堵。不可将“collision-free grid path”直接当成物理执行安全或按时送达证明。
- 复现应固定三张地图、zones/classes、item-capacity 与 pickup 集、任务 arrivals/seed、batch/exchange penalties、TP token 顺序、时空 Dijkstra horizon 和基线定义；报告分位数 latency、makespan、service time、计算/通信开销、handover 等待和未完成任务。
- 后续应加入更大/障碍更多地图、更多任务与长期流、基于学习的 pickup/exchange heuristic、异步/部分通信、动态速度与能耗，并与强的异构 MRTA/MAPD 规划和全局优化基线比较。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的异构多机器人规划、MAPD 与协作交接工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GKGU6726.pdf) 核验 problem formulation、two-level/TP pipeline、复杂度、三张地图参数和报告的运行/质量差异；未把启发式路径、共享 token 的仿真结果说成全局最优、真实物流实时性或通信鲁棒性保证。
