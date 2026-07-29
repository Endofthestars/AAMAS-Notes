---
title: "TCRL: Temporal-Coupled Adversarial Training for Robust Constrained Reinforcement Learning in Worst-Case Scenarios"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/GPHO5000"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GPHO5000.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02w"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "simulated_robotics_only", "worst_tc_attack_model", "reward_constraint_design", "no_real_world_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# TCRL: Temporal-Coupled Adversarial Training for Robust Constrained Reinforcement Learning in Worst-Case Scenarios

## 一句话总结

TCRL 针对随时间累积、耦合的状态扰动训练 constrained RL：以 worst-case cost network 近似攻击下可达动作的最大安全成本，再在奖励上加入自相关和熵变化两项约束，试图削弱攻击者的时间预测能力。将其接入 PID-PPO-Lagrange 后，在 Ball-Circle/Ball-Run 的 Worst-TC 模拟攻击下，表 1 报告成本 \(3.84\pm6.45\)、回报 \(709.40\pm253.81\)，优于三个基线；这依赖作者构造的攻击、约束与仿真动力学，不能构成物理系统安全保证。

## 方法与证据

- worst-case cost Bellman operator 在扰动状态球内可能诱导的动作集合上取最大后继成本；训练 \(Q^\pi_\varphi\) 以估计每状态 worst-case safety cost，而不显式学习一个攻击者策略（§2）。
- 防御优化在攻击轨迹下最大化 reward，同时约束估计成本 \(\tilde V_c^\pi\le\eta\)、reward 自相关 \(C_{corr}\le\epsilon_{corr}\) 与滑窗离散 reward 熵变化 \(C_{ent}\le\epsilon_{ent}\)。后两项被解释为打破 temporal coupling、保持奖励不可预测（§2，式 1）。
- 评估用 robotic motion control 的 Bullet Safety Gym 模拟任务，构造训练充分的 Worst-TC attacker，并将 TCRL 融入 PID-PPO-Lagrange。表 1 是 10 个 seeds、各 50 episode 的均值±标准差：PPOL-vanilla 630.73/75.44，random 600.31/72.80，ADV-PPOL(MC) 521.57/25.32，TCRL-PPOL 709.40/3.84（reward/cost）（§3、表 1）。
- 摘要称 TCRL 同时抵御 temporal-independent attacks，但没有在此版本给出完整攻击预算、所有任务分数、消融或理论分析，指向代码仓库获得详细版（摘要、§4）。

## 适用边界与复现

- 适合研究 adversarial observation 下的 safe-RL 训练；worst-case 是由 \(\Omega(s,\pi)\)、扰动半径和作者的 Worst-TC 模型定义的，不覆盖所有传感器、执行器、动力学、通信或物理攻击。
- reward autocorrelation/entropy 约束可能改变任务目标、学习稳定性和可解释性；其“不可预测”不等于保密或对自适应攻击者有效。成本估计误差还会造成虚假安全。
- Ball-Circle/Ball-Run、Bullet 模拟、PID-PPO-Lagrange 和 10 seeds 不能推出真实车辆、机器人或电网的约束满足。高标准差也要求报告失败率和尾部风险，而不只看均值。
- 复现应公开任务、cost/reward、\(\Omega\)、攻击训练/预算、所有约束阈值/窗口/离散 bin、网络和优化超参；分别报告无攻击、独立/耦合/未见攻击下的 return、cost violation、CVaR、每 seed 曲线及 reward-constraint 消融，并在硬件前进行正式安全分析。

## 与 AAMAS 的关系与核验说明

该文为安全约束下自主体强化学习的鲁棒训练方案。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GPHO5000.pdf) 人工核对 worst-cost operator、双奖励约束、Worst-TC、任务/seed 协议和表 1；未将模拟低成本误写为现实安全认证。
