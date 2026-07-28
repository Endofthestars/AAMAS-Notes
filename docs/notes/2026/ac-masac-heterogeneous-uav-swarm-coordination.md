---
title: "AC-MASAC: An Attentive Curriculum Learning Framework for Heterogeneous UAV Swarm Coordination"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "robotics_embodied", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/VJGN3439"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VJGN3439.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["custom_2d_simulation", "leader_state_observation_assumption", "reward_shaping_dependency", "simulated_communication_drop", "no_sim_to_real_validation", "collision_safety_not_guaranteed"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# AC-MASAC: An Attentive Curriculum Learning Framework for Heterogeneous UAV Swarm Coordination

## 一句话总结

AC-MASAC 是面向二维 Leader–Follower 异构 UAV path planning 的 CTDE MASAC：leader/follower actor 与 centralized critic 使用不同的 attention context，课程从简单到复杂，并以 hierarchical policy transfer 加 stage-proportional replay 对抗 sparse reward/forgetting。custom Gym/Pygame simulation 中它在 Success Rate、Formation Keeping Rate、Success-weighted Mission Time 上优于 MASAC/MADDPG/RRT*；但 followers 直接得到 leader position/speed、动力学与通信丢失均为模拟，论文明确将 sim-to-real physical hardware 留作未来工作。

## 方法与证据

- 环境是 2D POMDP，leader 要到目标并避障，followers 保持相对 leader 的 formation；连续 action 是 acceleration 与 angular velocity，各自有预设 kinematic bounds，\(\Delta t=0.1s\) 的 deterministic discretized dynamics（§2）。不是 3D flight dynamics、wind/GPS/actuator/battery/airspace模型。
- leader observation 为 own pose/speed/heading、goal coordinates、nearest-obstacle-within-40m flag；follower observation 为 own state 加 leader position/speed。虽然标注 decentralized execution，follower 仍假定可获得 leader state，不是受带宽/延迟/定位误差约束的真实通信估计（§2）。
- reward 为角色特定的目标、避障、formation distance、velocity matching等 shaped terms；SR 是 leader 无碰撞到目标比例，FKR 是满足 formation constraints 的比例，SMT 是 average episode length×SR（§2）。高 SR/FKR 是该 reward/threshold/场景下的 proxy，不等于碰撞风险、最小间距、能耗或任务安全保证。
- leader actor 对 follower observations 做 selective cross-entity attention；follower actor 以自身为 query，以 leader+other followers observations 为 context；critic 同样用 structured attention，embedding dimension 128、多头结构和 mask 忽略 absent/out-of-range agents（§3）。attention weight 不等于可解释/可信通信策略，也没有形式化安全或因果贡献证明。
- curriculum 依复杂度分 stages；stage transition 以 SR、reward CV、FKR thresholds 判定，policy transfer 针对角色 transfer actor/critic部分，replay 按随 stage 衰减的 historical/current ratio 采样（§3、Alg. 1）。这些 thresholds/transfer/replay schedule 是设计选择；训练分布覆盖不足仍可能导致复杂/OOD场景失败。
- 实验为 custom OpenAI Gym + Pygame simulation，比较 MASAC、MADDPG，以及以 centralized reference path 的 RRT*；baseline hyperparameters用默认值（§4）。不同算法是否经过等量调参、计算预算和 reward engineering 未由“默认”保证公平。
- 在代表性 worlds 和 ablations 中，AC-MASAC SR/FKR/SMT 最好；attention-only A-MASAC 直接训练最复杂环境，其 final average reward 比 curriculum AC-MASAC 低约 82%，C-MASAC（curriculum-only）用于 attention ablation（§4、Fig. 6）。这些是作者的 simulation learning curves/metrics，非跨平台统计认证。
- communication-imperfection test 在 simulated packet drop 下称能避免 catastrophic collisions/formation breakup、precision 随 \(p_{drop}\) 增大 graceful degradation；其余主实验先假定 ideal channels（§4）。未覆盖 correlated burst loss、delay/jitter、spoofing、out-of-order messages、GPS drift或 network contention。
- 结论明确未来将研究 sim-to-real transfer 和 physical hardware deployment（§5）。没有真实 UAV、风洞、室内/户外 flight、human proximity、监管/失效恢复或能耗测试。

## 适用边界与复现

- 可作为 leader–follower formation 的 simulation research baseline；部署前需将观测改为真实 sensing/communication estimator，加入 3D dynamics、wind、latency、actuator saturation、battery、GNSS/vision uncertainty、moving obstacles和 agent failure。
- 不应将 reward-shaped success、simulated packet-drop robustness或 attention mask 标为 collision avoidance certification。真实 swarm 必须有 independent geofence/separation monitor、control barrier/shield、emergency hover/land、human override、flight-rule compliance和 hardware-in-the-loop/field validation。
- followers 直接可见 leader state 是强信息结构；若实际仅有 broadcast/relative sensing，应报告 message rate/latency/loss、state-estimation error与 performance degradation，并对 partial observations 重训/验证。
- curriculum result依 task order和 transfer/replay schedule；应做 curricula order、thresholds、reward coefficients、agent count/heterogeneity/formation geometry、obstacle density/dynamics、seeds、training budget与 baseline tuning 的 ablation，报告 worst-case collision/FKR/SR而不只平均 reward。
- 复现应固定 Gym/Pygame world、2D kinematics/time step、roles/observations/actions/noise、reward/metric thresholds、stage maps/transition criteria、transfer/replay ratios、network/attention/hyperparameters、MASAC/MADDPG/RRT* budgets、packet-loss process、seeds与 evaluation episodes。

## 与 AAMAS 的关系与核验说明

这是 heterogeneous MARL UAV coordination 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VJGN3439.pdf) 核对 2D POMDP、leader/follower observations、attention actor/critic、curriculum transfer/replay、simulation baselines/metrics/ablations、packet-drop test与明确的 sim-to-real future work；没有把二维 reward-driven simulation 或 attention 输出误写成真实飞行、通信鲁棒性或碰撞安全保证。
