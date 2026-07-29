---
title: "A Hierarchical Approach with Crisis Mitigation for Multi-Robot Spatio-Temporal Restoration"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "planning_scheduling", "marl_coordination"]
dblp_key: ""
doi: "10.65109/UYQK9511"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYQK9511.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["known_environment_assumption", "decay_model_assumption", "simulator_only_evaluation", "tuned_crisis_parameters", "central_planner_dependency", "battery_and_motion_model_scope", "no_hardware_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Hierarchical Approach with Crisis Mitigation for Multi-Robot Spatio-Temporal Restoration

## 一句话总结

论文提出 MR-STAR：多机器人在已知环境中反复访问、恢复会随时间衰减的区域属性，并最小化属性低于阈值的累计损失。H-BFVG-CM 先以空间位置和衰减率聚类为辖区、分配 home robot，再在需求 surge 时按折现损失将外部机器人临时编为 surge team；在自定义仿真与 Stage 2D 中优于所比基线，但尚未在实体机器人或未知环境验证。

## 方法与证据

- MR-STAR 假设 \(m<n\) 个机器人、单一可同时充电的站点、已知障碍和各区域单调衰减函数；机器人可移动、恢复区域或回站充电。目标是将每个区域低于 critical threshold 的时间/机会损失降至最小。单机器人无时间衰减/电池约束时已退化为 TSP，因此原问题 NP-hard（§1、§3）。
- H-BFVG 的中央层用 K-means 按空间坐标和 decay rates 建立 jurisdiction，并以 Hungarian assignment 将每簇分给 home robot；本地层使用已有 single-robot greedy heuristic 规划持续恢复。这是“cluster-first, route-second”的集中规划架构，不是完全分散通信控制（§4）。
- surge detection 估计辖区内机器人能否在区域到达阈值前完成恢复；对紧急 cluster，用预期折现损失衡量从其他辖区抽调机器人是否净有益，并检查路程/服务/返程电量。被抽调者完成后解除绑定返回 home jurisdiction；实验取 \(\tilde k=3,k=1,\gamma=0.75\)，来自 preliminary trials（§4、§6.1.2）。
- 定量模拟在 500×500 开阔地图，区域初值 \([0,100]\)、阈值 50，比较相关/不相关 decay；对 4/8/10 robots × 24/64/100 areas 的每个配置重复 1,000 次。比较 mixed portfolio、solo distributed、global greedy、deadline job scheduling、approximate MDP；论文报告 H-BFVG 的累积损失与低于阈值时长均最好，统计显著性为 1%（§6.1、Table 1、Fig. 3--4）。
- crisis ablation 令 Q1/Q2 decay 加倍，H-BFVG-CM 相对无危机重规划有改进。该结果表明在此人为定义的局部 surge 下临时重分配有效，不说明可处理未知灾害、通信失败或区域属性估计错误（§6.1.2、Fig. 5）。
- Stage 2D 使用带 motion/sensor noise 的 `sdr-b` 室内图与 cluttered `grass` 图，6 robots × 36 areas、两次 surge、各 5 trials；仅对比适配的多机器人 time-varying-reward orienteering solver。H-BFVG-CM 保持属性高于阈值的表现更好（§6.2、Fig. 6--7），但这仍是 2D 模拟而非硬件实验。
- 复杂度分解包括辖区聚类 \(O(qnm|A|)\)、Hungarian 分配 \(O(m^3)\)、crisis detection \(O(mn+m^2)\)、mitigation \(O(mn)\)。作者报告大规模机器人/区域下各组件总运行在数秒量级；该时间来自 Intel i7-10750H/16GB 上的实现，依赖已知距离/衰减与阈值（§4、§6.3、Fig. 8）。

## 适用边界与复现

- 适合需要持续维护可测区域属性、能获得可靠衰减模型、并允许中央协调器分配辖区的研究型室内监测、消毒或农业恢复场景。
- 不应将模拟的“危机缓解”直接作为安全关键救援部署依据：真实传感会延迟/漂移，衰减与空间相关可突变，电池/充电拥塞、地图变化、碰撞和通信丢失会破坏调度前提。
- 复现应固定地图、区域位置/初值/阈值、衰减及相关性生成、机器人运动与电池/充电模型、K-means attributes/iterations、Hungarian 或 greedy assignment、\(\tilde k,k,\gamma\)、surge 时间、1,000 trial 与 5-trial seed、所有基线的实现和统计检验；同时报告低阈值时间、累计损失、碰撞/充电失败和 wall-clock。
- 实体部署前应在高保真仿真和受控硬件中进行地图/感知/通信/电池失效压力测试，加入碰撞与人类安全约束、任务优先级和人工接管；对持续未知衰减需在线估计及置信度门控，而非只依赖预先调查的函数。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多机器人任务分配、持续规划与危机重规划论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYQK9511.pdf) 核验 MR-STAR 假设、H-BFVG-CM、参数、各类基线、1,000 次定量试验、Stage 2D 的 5 次试验和复杂度；没有把仿真恢复指标表述为现场环境治理或机器人安全已获证明。
