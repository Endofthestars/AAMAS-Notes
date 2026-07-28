---
title: "Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "marl_coordination", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/MQIK8423"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["assignment_path_planning_separation", "flow_not_collision_safe", "traffic_estimation_error", "real_time_deadline_scope", "warehouse_simulation_to_deployment_gap"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery

## 一句话总结

论文把在线 MAPD 的 agent-to-task assignment 表为直接嵌入 grid map 的 minimum-cost flow，而非先算所有 agent-task shortest paths 再做二部匹配；正流同时给出 assignment 与 spatial guide path。与 Guided PIBT 的 traffic-aware planner 结合后，在模拟 warehouse/sortation maps 中对 20,000 agents、30,000 tasks 的 assignment 可低于 1 秒，严格 1 秒窗口下拥堵场景吞吐最多高出 Greedy 约 15.9%。但 flow 不含时间维度，也不保证 collision-free，真实安全/实时性依赖下游 path planner、交通估计、硬件、地图与运行时监控。

## 方法与证据

- MAPD 是已知 2D grid 上不断出现 pickup→delivery tasks 的在线问题；每个离散步必须在固定 planning window 内更新 assignment 与 committed movement。目标为 throughput，且 cell/edge-swap collision 必须避免（§2）。
- 传统 linear assignment 要构建 agent-task complete bipartite graph，需 all-pairs shortest-path costs；例子中 10,000 agents × 15,000 tasks 产生 1.5 亿 edges。本文 flow model 直接以每个 free grid cell 为 node、相邻 cell 为 directed edge；dummy source 接 free agents、pickup locations 接 dummy sink，发送 \(\min(n,m)\) units flow（§5.1--5.2）。
- 从每位 agent 位置沿 positive flow 追踪至 task node，得到 task 与 guide path（Algorithm 1）。该 objective 对所给 spatial edge costs 是 global min-cost assignment，但流网络允许多单位 flow 经过同一 edge，**不**显式建时间和 collision-preventing capacity；论文将 avoidance 留给 Guided PIBT/PIBT（§5.2.1--5.2.2）。
- edge cost 可用 unit distance、Guided PIBT 给出的 future vertex/contraflow traffic estimate，或执行历史的 exponentially discounted average waiting time（\(\gamma=0.9\)）。planner 再用 flow guide paths 与 congestion costs 产生 collision-free movement decisions（§4.1、§5.2.3、§6）。
- 实验为 C++/LEMON、32GB/16 AMD EPYC-Rome CPU，Random 64×64、Warehouse Small 33×57、Sortation Large 140×500 等 LoRR-style simulated maps；task pool 为 agent 数 1.5 倍，1000 simulation steps。Sortation Large 的 16k/20k agents 下 linear assignment（含 Dijkstra costs）10 分钟内无法完成，而 flow assignment 小于 1 秒（§7--7.1）。
- Table 1：在 1s real-time window，20k Sortation Large 时 Flow-Traffic throughput 31,658，对 Greedy 27,323（+15.91%）；但 Flow-Unit Cost 为 24,501（-10.33%），说明 speed/assignment alone 不保证吞吐。20k 时 unit-cost guide paths 在 1000 步中 997 次未能在 1 秒内由 path planner 初始化完成（§7.2）。
- 对 RMCA 的 published instances（500 tasks、25 cases/setting），flow 平均 makespan 更低且从不 timeout，RMCA 在高 task frequency 有大量 >1s steps（Table 2）。在超大 Iron Harvest map（约 6.5m free cells），flow 给 20k agents 的平均 assignment time 约 18.2s，作者改为每 30 steps 重调度；这不是每动作 1 秒级 planning（§7.3--7.4、Table 3）。

## 安全边界与复现

- minimum-cost flow 是 assignment/guidance 层，不是 MAPF safety proof。任何将其直接用于叉车、移动机器人、飞机牵引或人员共域环境的系统必须由独立时空 reservation/MAPF、速度/制动约束、传感器避障、急停、deadlock recovery 和 runtime monitor 保障；guide path 不可直接下发为物理轨迹。
- 交通 costs 是未来 planner estimate 或过去平均等待，可能对突发障碍、人类、通信延迟、机器人故障、地图变化和非平稳 demand 失准。错误估计可把大量 agents 同时导入狭窄区域；应限流、监测 occupancy/queue、设置 replan threshold、保守 capacity 与手动/本地 fallback。
- “实时”须逐项报告：flow solve、guide-path generation/refinement、collision-free action commitment、通信和执行延迟。论文自身显示 unit-cost flow 在 20k Sortation Large 的 guide-path 初始化经常超时，并在 ultra-large maps 以每 10/30 steps 才调度一次来控制成本；不可泛称整个系统始终 1 秒。
- 评测采用 gridworld、合成 task generator 与固定地图/分布，指标是 throughput/makespan/runtime；没有真实仓库 robot、连续运动、定位噪声、人机共域、充电/能源、payload、deadline、故障、任务优先级或安全事故指标。作者将 deadline-aware、energy-constrained、dynamic environments 列为未来工作（§8）。
- 复现应固定 map/task generator、seed、task pool ratio、timeout/commit horizon、flow solver/version、edge-cost formula与 warm-start、Guided PIBT/PIBT configuration、hardware与是否计入 assignment/guide/path costs；同时报告 collision/near-miss、missed deadlines、energy、fairness per task/robot及 OOD congestion/failure tests。

## 与 AAMAS 的关系与核验说明

这是 online MAPD、task assignment 与 multi-agent path planning 集成工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf) 核对 flow construction/retrieval、时间/碰撞分离、traffic costs、实验 maps/protocol、Table 1--3、RMCA 对比与 ultra-large scheduling；没有把 map-level min-cost flow 或模拟吞吐改进误表述为实体系统 collision safety 或端到端实时部署保证。
