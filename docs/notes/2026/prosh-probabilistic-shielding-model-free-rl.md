---
title: "ProSh: Probabilistic Shielding for Model-free Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "marl_coordination"]
dblp_key: ""
doi: "10.65109/KCVZ6904"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KCVZ6904.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02k"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["safe_rl_bound_depends_on_critic", "expected_cost_not_per_trajectory_safety", "deterministic_optimality_scope", "simulation_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# ProSh: Probabilistic Shielding for Model-free Reinforcement Learning

## 一句话总结

ProSh 在 constrained MDP 中给 state 增加 risk budget，并以 learned backup cost critic 在采样前将 actor 的动作分布与 backup action 混合；它给出随 critic 误差变化的期望成本界，并在确定性环境、误差趋零时证明渐近最优性。

## 方法与证据

- Risk-augmented CMDP 将 state 写为 `(s,x)`，x 是从该点起允许的 expected cost budget；`Q_b(s,a)` 估计从 state--action 可达到的最小期望成本。增广 transition 把执行后的预算按 critic 值重新分配（Definition 1）。
- `Q_b`-shielded policy 仅在动作的风险预算不低于 `Q_b(s,a)` 时赋予概率；若当前预算低于 `Q_b(s)`，采用最小估计成本的 backup action（Definition 2）。Theorem 1 给出将任意候选分布以系数 λ 与 backup policy 混合的 shield。
- Algorithm 1 在每一步先 shield、再从安全分布抽样并更新 actor/critic。该方法限制的是分布/期望成本，并非每条轨迹绝不越界。
- Theorem 2(i) 给训练任意步骤的成本界 `C ≤ x0 + 2Δ_b/(1−γ_c)`，其中 `Δ_b=||Q_b−Q_b*||∞`；(ii) 的渐近最优性需要 deterministic environment 且 `Δ_b→0`。摘要指出 tabular、过参数化网络或 batch Q-evaluation 等附加假设下可期望误差收敛。
- 与 PPO-Saute、TD3-Lagrangian、PID-TD3、FOCOPS、CPO 比较，图示覆盖 HalfCheetah 与 PointCircle；作者称 ProSh 训练期成本控制与回报权衡较好，但扩展摘要没有完整 benchmark、seeds 或置信区间。

## 适用边界与复现

- 安全保证是 discounted expected cost、并且取决于真实但通常未知的 backup-critic sup-norm error；不等于碰撞/伤害的零概率约束，也不能替代真实系统安全论证。
- 近最优结论限于确定性环境和 critic error 消失；随机环境只保留含可控/消失系数的安全界。模型自由不代表无需风险/成本定义、初始化 budget 或可靠 critic 学习。
- 连续控制仿真不足以支持机器人、车辆、医疗或工业部署。应加入传感器故障、不可建模风险、distribution shift、硬约束和独立安全监控。
- 复现应披露 CMDP cost/reward/budget/discount、backup critic 训练/误差评估、shield 参数/λ、actor update、环境版本、全部 seeds 与 safety-return curves；真实测试须先在隔离场景和运行时保护下进行。

## 与 AAMAS 的关系与核验说明

该工作将 probabilistic shielding 扩展到 model-free safe RL。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KCVZ6904.pdf) 核对 Definitions 1--2、Theorems 1--2、Algorithm 1 与 §3，明确将其 guarantee 限定为 critic-error-dependent expected-cost bound。
