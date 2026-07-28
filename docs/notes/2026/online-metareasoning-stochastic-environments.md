---
title: "Think Fast! Learning to Control Online Reasoning in Stochastic Environments"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/MXNX1909"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MXNX1909.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["distribution_shift_in_metacontroller", "perfect_environment_model_assumption", "state_abstraction_error", "planning_acting_misalignment", "no_hard_real_time_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Think Fast! Learning to Control Online Reasoning in Stochastic Environments

## 一句话总结

OnLearn 将“现在继续计划、用何种 planner hyperparameter，还是依当前解执行”建模为 online metalevel SSP MDP，并以 deep RL 在一类问题分布上学习控制器；它可把更多推理放在信息更充分或计划代价更低的 state。在两个合成随机 gridworld 分布中，它优于固定 planning ratio、myopic Bounds 与只在初始 state 计划的 OffLearn；但训练分布代表性、准确环境模型与 state-abstraction 质量是决定性前提，不能把实验中的成本改善当作实时安全或任意机器人场景的保证。

## 方法与证据

- object-level 问题是 finite stochastic shortest-path (SSP) MDP，目标是到 absorbing zero-cost goal 的最小期望累计成本；planner 是任意可参数化的 black box，其完整 internal configuration \(\chi\) 诱导当前 best policy。论文假定存在 proper policy，improper policy 有无限期望 cost（§3--4）。
- metalevel state 为 object state 与 planner configuration \((s,\chi)\)。动作要么以超参数 \(\delta\) 运行 planner 一个固定元时间步（object level 执行 `nop`，环境仍可能演化），要么执行当前 \(\pi_\chi\) 选出的 object action；两个动作都产生 object-level cost（Definition 1、Eq. 1--2）。因此方法控制何时、何地及如何思考，而非改写 planner 的正确性。
- 由于原始 metalevel MDP 过大，作者以 problem context features \(\Psi\) 和 algorithm/configuration features \(\Omega\) 做抽象，使用 DQN 学习 OnLearn。抽象可能使 transition non-Markovian；其理论表述以 bounded costs、有限 effective horizon、最大 planning budget 后 proper policy 等条件与 \(\epsilon\)-approximate Q-abstraction 为前提（§5）。
- baseline 是固定 decision-time planning (DTP，多组 ratio)、Lin et al. 的 meta-myopic Bounds、以及只允许在 initial state 计划的 learned OffLearn。RL controllers 按 5 个 DQN random seeds 评估（§6.1--6.3）。
- ObstacleRacetrack 是带未知障碍的 2D racetrack：撞到/穿过才知障碍状态。相对 OnLearn，Bounds 的 mean excess cost 高 37%、OffLearn 高 30%，最佳 DTP 高 51%；禁用 hyperparameter control 的 OnLearn 高 18%（Figure 2、§6.5）。
- RadWorld 是随机障碍/辐射分布 gridworld，移动与 planning 都累积辐射 cost，行动 failure probability 随辐射从 0 到 0.75。相对 OnLearn，Bounds 有 2.4 倍 excess cost、OffLearn 2.9 倍；示例轨迹先在起点计划 4 个元步，抵达低辐射区再长时间计划（Figure 3、§6.4--6.5）。
- 方法在每个 domain 的程序化 \(p(M)\) 上训练 10K object-level MDP、在同分布 held-out 1K MDP 测试；成本以该 instance optimal-policy expected cost 归一化。因推理自身有 cost，1 是 lower bound；统计以 one-sided Mann--Whitney U、\(p=0.01\)（§6.4--6.5）。

## 安全边界与复现

- 论文明确假定有代表性的 problem distribution 可供训练，并在结尾说明 agent 有完美环境模型；Obstacle 的未知性是已建模、可观测的简单 epistemic factor，不是开放世界模型误差。传感器失败、地图/动力学漂移、网络/算力抖动、极端罕见事件或任务分布变化均会使 learned metacontroller 在错误时刻少想/多想。
- planner 与 metacontroller 分离可能导致 plan/act 不对齐：作者给出一种反例方向——低计划成本的 state 未必对解决 object-level problem 有帮助，而 metacontroller 无法要求 planner 为到达该 state 而规划（§7）。该架构不是对硬 deadline、碰撞风险或实时控制可行性的证明。
- 规划期间 `nop` 也会有状态转移和成本。在辐射、移动机器人、医疗或车辆等场景，不能让 learned policy 自主决定“暂停动作去思考”，除非外层 runtime monitor 保证安全停止/保持、通信/能源预算、最大思考时限、急停与保守 fallback；高危区域应由硬约束而非学习到的 cost trade-off 管理。
- 评测只有两个 synthetic 2D gridworld 分布及 5 个 DQN seeds；没有实体机器人、复杂连续感知、OOD、adversarial observation、planner failure、wall-clock latency、GPU contention、网络断连或安全事故指标。reported excess-cost 是该基准的相对量，不能转译为真实风险降低比例。
- 复现应锁定 procedural generators、10K/1K split、随机 seeds、feature/abstraction functions、planner increment \(\tau\)、hyperparameter action space、DQN settings、cost/failure definitions 和所有 DTP ratios；并加入 model-mismatch、abstraction aliasing、budget exhaustion、deadline 与 fail-safe 触发压力测试。

## 与 AAMAS 的关系与核验说明

这是 online metareasoning、probabilistic planning 与 learned metalevel control 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MXNX1909.pdf) 核对 SSP/metalevel formulation、抽象前提、baseline、两个 domain、10K/1K protocol、Figure 2--3 数值与 §7 limitations；没有把同分布 synthetic 成本结果误称为通用实时安全或 autonomous deployment 认证。
