---
title: "Peer-Aware Cost Estimation in Nonlinear General-Sum Dynamic Games for Mutual Learning and Intent Inference"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: "10.65109/MGNP2868"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MGNP2868.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["two_player_full_observability", "peer_learning_model_known", "local_ilq_equilibrium", "approximate_gradient", "simulation_safety_only", "intent_signaling_tradeoff"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Peer-Aware Cost Estimation in Nonlinear General-Sum Dynamic Games for Mutual Learning and Intent Inference

## 一句话总结

N-PACE 面向两方非线性、不完全信息一般和动态博弈：每个 agent 在 ILQ 局部 Nash 近似中不仅从对方动作估计其 cost/intent parameter，也显式模拟对方如何估计自己，从而避免把对方错误设为“已知真实 intent 的 expert”。在 lunar-lander、lane merging、intersection driving 仿真中，估计和碰撞率优于 expert-peer/minmax baselines；但前提是共享状态与动作完全可观测、对方学习动态和初始信念已知/近似已知，且安全结果只来自简化运动学 Monte Carlo，不能用作真实车辆或 HRI 的安全证明。

## 方法与证据

- 设置为两 agent、shared state 的连续时间离散化系统 \(s_{t+1}=f_t(s_t,a_t^i,a_t^j)\)，\(f\) 可微；各自 running cost 对 state/actions 二阶可微、对 intent \(\theta_k\) 可微。论文**假定双方在每步都可观察所有 states 与 control signals**（§3）。
- 每个 agent 在 receding horizon 内以 ILQGame 线性化 dynamics、二次化 costs、解 coupled Riccati equations，得到依赖本方真实 \(\theta_k\) 与对方估计 \(\hat\theta_{-k}\) 的 feedback policy。这是局部 Nash trajectory，不是全局 equilibrium（§3.1）。
- 普通在线估计以对预测 peer action 与观测 action 的误差做 gradient update；其预测 policy 中代入本方真实 \(\theta_k\)，等于假设 peer 知道自己的真实 intent。论文将这称为 expert-peer assumption，会产生结构性偏差（§3.2、Remark 2）。
- N-PACE 改为同时跟踪对方对双方参数的估计：\(\hat\theta^i_{t+1}=h_l^i(\hat\theta^i_t,\hat\theta^j_t,a_t^i,s_t)\)，\(\hat\theta^j_{t+1}=h_l^j(\hat\theta^j_t,\hat\theta^i_t,a_t^j,s_t)\)。可用不同 gradient/Bayesian/neural learner，但关键是彼此知道 learning dynamics（§3.3、Algorithm 1）。
- 若双方从相同 initial estimates 出发并持续互相跟踪，该推断动态实际等效集中式；若 initial beliefs/learning dynamics 失配，作者说偏差通常衰减但也观察到更大误差下出现 divergence，不能宣称普遍无偏/收敛（§3.3、§4.2）。
- 为实时计算，论文忽略 ILQ converged trajectory 对 \(\hat\theta\) 的依赖，以最终 LQ policy gradient 近似真实梯度；更精确 AD 仍可用但可能不满足实时性。该近似本身没有覆盖所有 nonlinear game 的误差界（§3.2）。
- Proposition 1 的收敛比较仅限 Hessian 对 intent 不变、intent 在线性一阶项出现、policy 对自身 intent 线性且 operating set compact，并要求 sufficiently small learning rate。它说明此类下 N-PACE 可收敛而 expert assumption 可对所有 rate 失败，不是所有非凸 ILQ game 的保证（§3.3）。
- intent signaling 通过在本方 cost 加 \(\eta\|\hat\theta^k_{t+1}-\theta_k\|^2\) 来选择更易被 peer 学到的行动；Lemma 1 说明固定状态/信念/peer action 下增大 \(\eta\) 不增加该一步 estimation error，却可能增加 control effort（§3.4）。
- intersection 的 300 Monte Carlo kinematic simulations：expert-peer 4.33% failure（13 collisions），N-PACE 1.33%（4），minmax 0.66%（2）；N-PACE+signaling \(\eta=1,10\) 均 0%，但平均 control effort 从 N-PACE 4.86 升至 5.44/5.45。它是定义的 gray-box collision area 与 5s、50 samples 下的指标（§4.3、Table 1、Figure 6）。

## 安全边界与复现

- 不可将“0/300 simulated collisions”解释为道路安全认证：模型没有感知误差、遮挡、通信延迟/丢失、路权/交通法规、车辆 actuator/制动极限、轮胎/天气、行人、第三方车辆、对抗者或责任机制。任何实车应用须有独立 verified safety controller、RSS/MPC barrier/monitor、急停和人类监督。
- 本方法要求对方 cost parameter 有合适可辨识参数化，且知道或足够准确地建模其 learning rule、learning rate、prior/variance；现实人类/商业自动系统往往不满足，也可能策略性伪装其学习行为。不能把动作观察直接归因为“意图”。
- ILQ 的局部线性/二次近似及 trajectory-gradient omission 都可能在急剧非线性、接触、离散 maneuver 或多峰策略下失效；多 agent 超过两个、部分可观测、异步更新时需重新推导与验证。
- signaling 以让 peer 更快学到本方 intent 为目标，可能改变行为和提高控制努力；在人机交互中还涉及告知、可解释性、操纵风险、隐私及是否允许系统以行动影响人的 belief，应有明确 consent 与审计。
- 复现应固定 dynamics/costs、horizon/dt、ILQ initialization/tolerance、gradient approximation/AD、\(\alpha\)、priors/variance/mismatch distribution、intent range、collision geometry、300 seeds、all baseline definitions 与 \(\eta\)；报告 convergence failures、near-misses、control effort、runtime、parameter sensitivity和 OOD learner/dynamics tests。

## 与 AAMAS 的关系与核验说明

这是 general-sum dynamic games、intent inference 与人机/车辆交互的工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MGNP2868.pdf) 核对问题假设、ILQ/gradient approximation、N-PACE coupled updates、Proposition 1 的限制、signaling objective、三项 case studies 与 Table 1；没有将局部仿真中较低碰撞率误写为全局 equilibrium、真实 intent 识别或部署级车辆安全保证。
