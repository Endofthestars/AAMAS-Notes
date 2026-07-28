---
title: "Zero-Shot Coordination in Ad Hoc Teams with Generalized Policy Improvement and Difference Rewards"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: "10.65109/TNEX7143"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TNEX7143.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["gpi_guarantee_not_applicable", "simulation_scope", "library_coverage_dependency", "full_observability_assumption", "no_communication_assumption", "controlled_robot_demo"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Zero-Shot Coordination in Ad Hoc Teams with Generalized Policy Improvement and Difference Rewards

## 一句话总结

GPAT 用预训练 learner-policy library 的 difference-reward Q functions 做 generalized policy improvement：测试时每一步从 library 取最大值对应的动作，不做 teammate-type inference 或 online learning。它在三类模拟 AHT 中常胜于给定基线，并在两台 TurtleBot 的受控 foraging 演示中运行；但新 teammate 改变 transition dynamics，经典 GPI “优于库中 policy”的保证不成立，且当库中没有相关 skill 时其线性版本可劣于基线。因此它是对有限预训练 skill coverage 的 zero-update execution 方法，不是无条件的未知队友协调保证。

## 方法与证据

- 问题为 fully cooperative MMDP、fixed team、single learner、共享 state/reward，且论文明确假设 agents 无 communication；不处理部分可观测、队员进出、多个 learner 或 human AHT（§2--3）。
- 经典 GPI 对固定 dynamics、变 reward 的 source tasks 可保证至少不差于 library policy；AHT 中 reward 固定而 unseen teammate policy 改变 dynamics。论文明确说明这一 guarantee 不适用，pretrained Q 仍假设 source-team dynamics，difference rewards 只是降低 shift 影响，**仍不保证** policy improvement（§1、§5.1）。
- GPAT 第一步对 source teams 预训练 learner policies；第二步针对 learner difference reward \(\Delta r^a\) 做 policy evaluation/Q learning；第三步以各 \(Q_i^{\Delta r}\) 最大值的 GPI action 动态切换。对 deterministic teammates，difference-reward counterfactual 用 uniform learner policy 计算（§5）。
- 线性-reward 版用 successor features，general-reward 版直接学习 Q；两者都依赖 source policies/环境 features/credit-assignment counterfactual 的质量。它不观察新队友后再估计 type，故是 zero-shot update，但并非对任意行为空间的 zero-information robustness（§5）。
- 评测为 2-agent 8×8 foraging、3-predator 13×13 predator-prey 与 2-agent Overcooked；训练 foraging/predator learner 使用 SFQL，Overcooked 使用 Stable-Baselines3 DQN，主结果以 1,000 episodes、10 replicates、95% CI 的 IQM 对比（§6.1、Table 2）。
- foraging Experiments 1/2 中 GPAT linear outperform baselines（除 oracle），对应 library 含一个/多个可用 skills；Experiment 3 中 library 没有匹配 new teammate（其偏好 yellow），GPAT linear 反而低于 Robust 与 PLASTIC。作者将此归因于 library mismatch 与 new-teammate distribution shift（§6.2、Table 2）。
- ablation 显示去 difference rewards 会造成 Q overestimate、不能适时切换 policy；文中平均 value error 为 GPAT w/o DR 32.0%、GPAT 18.1%。这支持所选模拟中的 credit assignment作用，不证明在不同 reward/counterfactual 或真实传感噪声下稳定（§6.2、Fig. 6--7、Table 3）。
- general-reward GPAT 在 Exp. 3 与 Robust/PLASTIC 相近，线性版本则较差；所以线性 SF 表达的效率/性能也受 reward representation与是否存在相关库技能影响（§6.2、Table 3）。
- 现实演示仅使用两台 Robotis TurtleBot3 Burger，在 foraging environment 中，各自 ROS instance、motion capture marker 定位，GPAT command 经 ROS 下发；报告的是两种实验的路线/collect behavior，而没有多队友类型、户外/拥挤、通信丢失、长期统计成功率或安全事故指标（§6.3、Fig. 8）。

## 适用边界与复现

- 适用于可获得少数 representative source teammate/team、共享/足够准确的 state 与 reward、环境 action/state semantics 对齐且可离线训练 library 的合作任务。上线前应明确 library coverage；无法表示的新 capability、目标、观测、动作延迟或策略将破坏 Q transfer。
- 不要声称 “GPI guarantee” 或 “zero-shot” 等于对新队友必然更好。这里 zero-shot 指测试期间没有 learner update/type inference；不是对 changed dynamics 的理论 performance lower bound。需与 best-library、robust policy、oracle和 no-DR baseline 一起报告 OOD regret、worst seed、failure rate与 calibration。
- Difference reward 需要合理 counterfactual/team-reward access；真实机器人中队友行为、共同奖励、传感/定位和动作执行均有噪声/延迟时，该反事实可不可信。应测试 partial observability、reward delay/misspecification、nonstationary teammate、agent dropout、heterogeneous action spaces、communication限制与 adversarial/malfunctioning team members。
- TurtleBot demo 不能代替多组织 search-and-rescue/工业协作验证。此类部署还需 collision/velocity/geofence safety controller、human override、network/security、time synchronization、task-level constraints、offline-to-online identification和 staged field trials。
- 复现应固定 environment/version/layout、source/target teammate policies和 skill coverage、reward/feature weights、SFQL/DQN/PPO hyperparameters、library size、difference-reward reference action、10 evaluation episodes used for \(w_{\Delta r}\)、GPI rule、1,000 episode/10 replicate/IQM CI protocol、random seeds，以及 TurtleBot/ROS/mocap/controller latency/command limits。

## 与 AAMAS 的关系与核验说明

这是 ad hoc teaming 的 zero-shot coordination 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TNEX7143.pdf) 核对 GPAT 三步骤、经典 GPI 保证不适用于 teammate-dynamics shift、difference reward 实现、三项模拟及其 library-mismatch反例、ablation和 TurtleBot 受控演示；没有把 zero-update 执行或 demo 误写为任意未知队友的理论保证、开放世界鲁棒性或现场安全验证。
