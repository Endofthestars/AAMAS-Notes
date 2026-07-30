---
title: "Logical Robots: Declarative Multi-Agent Programming in Logica"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["argumentation_reasoning", "agent_engineering", "marl_coordination", "robotics_embodied", "planning_scheduling", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/UKVJ1021"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UKVJ1021.pdf"
demo_url: "https://logica.dev/robots"
video_url: "https://tinyurl.com/logicalrobots"
code_url: "https://github.com/EvgSkv/logica/tree/main/docs/robots"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05x"
spark_draft_verdict: "source_grounded_with_required_page_map_performance_evaluation_synchrony_shared_memory_and_simulation_scope_corrections"
spark_qa_verdict: "needs_revision_corrected_for_page_boundary_sql_performance_and_unvalidated_resilience_claims"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["two_dimensional_simulation_only", "database_speed_and_large_scale_unbenchmarked", "asp_prolog_grounding_comparison_unvalidated", "planning_control_unification_author_claim", "discrete_synchronous_round_assumption", "leader_single_point_of_failure", "cross_robot_memory_consistency_and_access", "sensor_noise_and_communication_failure_unmodeled", "collision_and_safety_metrics_unreported", "no_success_rate_baseline_or_scaling", "no_random_trials_or_formal_verification", "no_real_robot_or_sim_to_real_validation", "no_user_or_education_study", "security_and_control_integrity_unreported", "distributed_mapping_robustness_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_sql_performance_synchrony_leader_shared_memory_consistency_sensor_failure_control_integrity_formal_verification_and_sim_to_real_check"
escalation_verdict: "escalate_for_evidence_and_governance_remediation_before_deployment_or_strong_performance_claims"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted multi-robot safety and simulation-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Logical Robots: Declarative Multi-Agent Programming in Logica

## 一句话总结

Logical Robots 用会编译为 SQL 的 Logica predicates 在同一声明式环境中表达 2D 多机器人 sensing、reactive control、shared memory 与 path planning，并提供十个递进关卡；论文没有 SQL/ASP/Prolog benchmark、成功率、碰撞、扩展性、形式验证、真实机器人或教学研究，因此只证明了平台演示能力，不证明 database-speed 性能、部署安全或教育效果。

## 公开资源

论文提供：

- [在线 demo](https://logica.dev/robots)；
- [源代码](https://github.com/EvgSkv/logica/tree/main/docs/robots)；
- [演示视频](https://tinyurl.com/logicalrobots)。

本文核验论文中的平台与例子描述，不把站外服务当前可用性或代码正确性视为已独立验证。

## Logica 与平台定位

Robot behavior 由 logical predicates 定义，把 simulated radar arrays 与 memory 映射为 desired motor outputs。作者称 Logica 编译到 SQL，将 sensor streams 视作 relational tables，并依赖数据库聚合处理：

- high-level reasoning，例如对 beacon distance 做 `ArgMin`；
- low-level control，例如对 radar data 做 `WeightedAverage`。

作者将其与 ASP/Prolog 的 grounding bottleneck 对比，并称可在 database speeds 上处理 large-scale sensor data。论文没有给 system size、SQL engine、query plan、latency、throughput、ASP/Prolog baseline 或硬件，因此这是设计定位，不是性能结论。

## 2D simulation ontology

迷宫包含四类 entities：

- **Robots**：独立执行相同 Logica movement-control program；
- **Beacons**：静态 waypoints 与 area triggers；
- **Areas**：可在 accessible/restricted 状态间切换；
- **Win Conditions**：例如要求 robots 同时到达 Mining zones。

这是离散二维 simulation。论文没有 robot dynamics、actuator saturation、friction、sensor calibration、3D geometry 或 physical safety layer。

## Sensor 与 Memory

`Sensor(robot_name:, sensor:)` 提供即时观测。`sensor.radar` 是 rays array，每条包含：

- angle；
- distance；
- object type：beacon / wall / robot / none；
- label：beacon ID 或 robot name。

`Memory(robot_name:, memory:)` 读取 user-defined strings、lists 或 JSON。默认 robot 只能读自己的 memory，也可配置读取其他 robots 的 memory。每个 robot 的 store 跨 timesteps 保留，直至被覆盖。

论文没有定义 concurrent write semantics、snapshot isolation、stale reads、access authorization、malicious robot、memory corruption 或 conflicting updates。共享读取在 demo 中方便协调，但不自动构成真实分布式 memory protocol。

## 离散同步执行

Simulation 在 discrete synchronous rounds 中运行。每个 timestep，每台 robot：

1. 读取 Sensor 与 Memory；
2. 独立执行 Logica program；
3. 输出 `desire` 与 updated memory。

同步模型让所有 robots 共享清晰的 step boundary。真实系统中的不同控制周期、network latency、message loss 与 clock drift 未被建模，因此不能直接把同步 simulation behavior 外推到 physical multi-robot coordination。

## WeightedAverage reactive control

示例定义 `FreedomMotion(radar)`：每条 radar ray 以 distance 为权重给其 angle 投票；远处物体或无障碍方向权重更强，近障碍方向更弱。

Robot 使用固定 `speed=0.5`，生成：

- `left_engine = speed - freedom + 0.1`；
- `right_engine = speed + freedom`。

正的 freedom 让 robot 向一侧转，负值反向；`0.1` asymmetry 用于打破 symmetric configuration 的 deadlock。

该代码展示从 relational aggregation 到 differential-drive command 的表达方式。论文没有报告 collision rate、minimum clearance、stability、deadlock frequency、sensor noise 或 adversarial layout。

## Distributed mapping 与 planning state

更复杂的场景让 robots 观察 beacons，并在 local memory 保存 pairwise distances。Leader 聚合其他 robots 的 memories，构建 beacon network；一旦某 robot 到达 Home，leader 计算 shortest paths。

`PosteriorHomeDistance` 使用 `Min=` 聚合 Bellman–Ford 风格的三类候选：

- 保留旧 `HomeDistance(beacon)`；
- Home beacon 距离为 0；
- 通过 neighbor 更新 `HomeDistance(neighbor)+D(neighbor,beacon)`。

信息在多个 timesteps 中传播。这个例子说明递归 aggregation 与 shared state 的声明式表达，但没有证明在 leader failure、partial map、incorrect distance、disconnection 或 delayed memory 下收敛和恢复。

## 十个 examples 与 demo plan

平台包含 ten progressively challenging coordination scenarios。论文计划详细展示：

- **Level 7 — Station Management**：部分 robots 保持与 station beacons 接触以关闭 hazards，其他 robots 前往 Mining area；
- **Level 8 — Formation Navigation**：robots 读取遇到的 robots 的 memory，形成跟随并共同到达 Home；
- **Level 10 — Distributed Mapping**：robots 发现 beacons，leader 聚合 shared memory 并运行 distributed Bellman–Ford。

这些是功能场景，不是随机 trial、benchmark suite 或成功率评估。

## 缺失证据

本文没有报告：

- SQL execution latency、throughput、memory 或 query scaling；
- 与 ASP、Prolog、imperative controller 或其他 MAS language 的 baseline；
- success/collision/deadlock/path-length/energy metrics；
- robots、radar rays、beacons、map size 增长时的 scaling；
- random seeds、multiple layouts 或 repeated trials；
- safety invariants、formal verification 或 counterexample analysis；
- leader crash、robot failure、message delay/loss 或 Byzantine memory；
- real robot、hardware-in-the-loop 或 sim-to-real transfer；
- participant user study、classroom deployment 或 learning outcome。

因此 “unifies symbolic planning and low-level control”表示同一 Logica programming environment 覆盖两类表达，不证明控制正确性或所有规划/控制问题的统一语义。“novel educational tool”是作者定位，尚无教育效果证据。

## 多机器人与部署风险

潜在风险包括：

- leader 是 mapping/path computation 的单点；
- configurable cross-robot memory 缺少一致性与权限模型；
- synchronous rounds 掩盖异步时序故障；
- radar object classification、distance 或 label error 传播进 motor output 和 map；
- `0.1` heuristic 不能保证所有布局中避免 deadlock；
- SQL/query 或 user-authored predicate error 可影响所有 robots；
- simulation 的 simple differential drive 不覆盖真实 actuator、collision 与 emergency stop；
- 在线 editor 或 shared program 若无访问控制，可能改变 fleet behavior。

高风险等级来自控制与协作结论向真实机器人外推时缺少 safety、fault tolerance 与 sim-to-real 证据；不表示当前 2D educational demo 已造成现实危害。

## 页码核验

- p. 4137：身份、Introduction、Logica/SQL 定位、资源、ontology 与 Sensor 起点；
- p. 4138：Memory、synchronous control、WeightedAverage、planning state、Bellman–Ford 与 demo levels；
- p. 4139：参考文献，没有新增实验结果。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UKVJ1021.pdf) 核验；`reviewed` 不表示 database-speed performance、control safety、distributed robustness、formal correctness、sim-to-real 或教育效果已经验证。
