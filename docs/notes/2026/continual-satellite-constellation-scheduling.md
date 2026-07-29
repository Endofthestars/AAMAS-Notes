---
title: "Large-Scale Continual Scheduling and Execution for Dynamic Distributed Satellite Constellation Observation Allocation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "resource_allocation", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/JCYH5778"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JCYH5778.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "simulation_evidence_only", "omniscient_offline_upper_bound", "incomplete_local_search", "future_in_space_demonstration"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Large-Scale Continual Scheduling and Execution for Dynamic Distributed Satellite Constellation Observation Allocation

## 一句话总结

本文把大规模卫星星座的持续观测分配建模为 Dynamic COSP（DCOSP）：优化随环境变化后真正执行的请求数，而不只是静态时刻排入计划的任务数；提出动态增量邻域随机搜索 D‑NSS，以图分区、变更修复和局部优化在 108/200 卫星、至多 1000 requests 的仿真中接近全知上界并显著少于 DSA 的消息量，但它是不完备 local search，尚不能代替飞行级安全、通信或任务保证。

## 方法与证据

- COSP 中每个 satellite agent 管理本地候选 observation tasks 和 Boolean variables；任务不可重叠，受 memory capacity 与 downlink 约束，constraint graph 密集（度数 \(\Omega(|A|\cdot|R|)\)）且其他 agent 的变量/约束仅局部可知（§2）。DCOSP 将问题视为连续 COSP instances 序列，适用的是该离散任务、明确资源与本地知识模型，而非任意卫星自主飞行。
- 与将每个静态 instance utility 求和不同，DCOSP 的 \(F(X_\delta)\) 计数真正 completed 的 requests：任务需被选中且执行期间与问题保持静态的时间区间相交。该 optimality condition 强调 schedule/execution overlap；它未量化科学价值质量、成像质量、碰撞/姿态风险、燃料、地面授权、优先级公平或失败恢复。
- 作者以未来信息把动态 DCOSP collapse 为静态 DCOP，并只保留 horizon 内持续任务，得到全知 offline upper benchmark（§3.1）。这是 evaluation oracle，现实 distributed agents 不具备 dynamics 的先验，不能把“near-optimal gap”解释为在线最优或上线 SLA。
- D‑NSS 为不完备 DDCOP local search：先做 decomposition heuristic 分区，动态时移除过时任务/插入新任务修复 schedules，再在 partition 内迭代 refinement（§3.2）；每 iteration 的计算与通信为 \(O(|A_N|\cdot|R_N|)\)，其中量取最大 partition。复杂度不包含 partition quality、动态频率、全局协调失败、网络丢包/延迟、onboard runtime/能耗或 worst-case convergence。
- 仿真比较 0‑NSS（from scratch）、D‑DSA/0‑DSA、非通信 greedy/random；Planet 200 satellites、Walker 108 satellites、24h horizon（§4）。表 1 在 up to 1000 requests 的 Walker 中 D‑NSS gap 0.14%、5.2 ms、240.2 KB，而 D‑DSA 为 1.17%、58.2 ms、10,459.5 KB；Planet 中 D‑NSS gap 1.87%、消息 7.3 KB。大规模“thousands”情形作者描述 satisfaction/time/message 优势但本文未列完整数据、分布、seeds/CI或通信故障结果。
- 文中称 D‑NSS 将服务于 2026 开始、60 多 spacecraft 的 NASA FAME 演示（§1/5）。这是未来计划；官方摘要没有提供在轨试验、端到端安全案例、真实地面链路/云层/姿态扰动、故障注入或飞行认证证据。

## 适用边界与复现

- 适用于大量有明确时间窗、resource/downlink constraint 的观测请求，且能容忍分区 local-search 的近似和延迟；不应直接控制姿态/推进、紧急避碰、关键基础设施或任何要求全局最优/可证明安全的卫星任务。
- 复现需公开 constellation orbital/access windows、request arrivals/value/期限、task duration、memory/downlink/energy limits、动态事件及静态区间、partition heuristic、repair policy、NSS parameters/iteration budget/message encoding、seed 与 hardware。用 centralized branch-and-bound 仅在小实例计算 omniscient upper bound，并严格区分它与 online algorithm 的信息集。
- 应压力测试更高 dynamicity、cloud/weather/target uncertainty、通信延迟/丢包/分区、satellite/ground-station loss、资源估计偏差、异构有效载荷、优先级冲突、恶意/错误任务、超大 request rate 与长 horizon；报告 actual completed science value、deadline misses、onboard CPU/RAM/energy、message peak、tail latency、公平与 failure recovery，而非只看 gap。
- 飞行部署需在 scheduler 外保留安全约束、姿态/能量保护、collision/keep-out、command authentication、地面 override、可审计决策日志和 fallback rule-based planning。调度仿真的 near-optimal request count 不能证明观测正确、轨道安全或灾害响应可靠。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的动态 DCOP、分布式多智能体调度与空间系统 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JCYH5778.pdf) 核验 DCOSP 的 executed-requests objective、全知 offline benchmark、D‑NSS 三阶段与分区复杂度、108/200 satellite/24h setup、表 1 数值和未来 FAME 描述；没有把 simulation 比较或计划中的 mission 写成已验证的在轨自主能力。
