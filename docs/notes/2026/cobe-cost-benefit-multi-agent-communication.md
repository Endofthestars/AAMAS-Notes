---
title: "Why and Whom to Communicate? A Dual-Objective, Cost-Benefit Framework for Multi-Agent Communication"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/TAYO7266"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TAYO7266.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["empirical_pareto_front_dependence", "communication_cost_model_dependence", "simulation_benchmarks_only", "knee_point_selection_sensitivity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Why and Whom to Communicate? A Dual-Objective, Cost-Benefit Framework for Multi-Agent Communication

## 一句话总结

COBE 将 MADRL 通信建模为 reward 最大化与 communication cost 最小化的双目标问题：从同一 on-policy minibatch 估计/平滑经验 Pareto front，以 curvature knee point 作为动态 target，指导 agent 只在预期收益值得时发送 intended action；实验证明其在所用模拟任务的 reward-cost 平衡较好，但 cost 定义和 knee rule 本身就是偏好选择。

## 方法与证据

- 在 cooperative Dec-POMDP 中，outcome profile 是 forward-looking critic value 与归一化 communication usage；先滤除噪声/短暂 profile，再取 Pareto non-dominated set（§3）。
- 对平滑的 discrete front 以曲率选 marginal value-per-cost 最大的 knee `p*`，重算 target 并以 Pareto-guided alignment loss 训练 communication policy，决定 why/when/whom，message 为 intended action（§3.4--3.5）。
- 与 IC3Net、TarMAC、MAGIC、I2C 等 MAC baseline 比较，并有 Pareto endpoint/heuristic 与 constrained/scalarized single-objective ablation；报告 mean±std、reward、communication rate/cost 与 collision 等（§4）。
- 论文的主张是 COBE 在 Cooperative Navigation 等 benchmark 提供更好 empirical trade-off；其例子中 knee 约 38% communication cost，但不是跨任务恒定预算或物理网络指标（§4）。

## 局限与复现

- Pareto front 是由 critic、normalization、smoothing、minibatch 和当前策略估计；非平稳 RL、不同 reward scale、不同 cost unit 或 noisy critic 会移动 knee point，仍需设计这些选择。
- “communication cost”不是实际 bytes、bitrate、latency、packet loss、privacy、energy 或 topology failure；真实网络可能与模拟 action-sharing 成本完全不同。
- 任务/agent count、baseline tuning、random seed 和 constrained/scalarized budget 网格决定排名。复现应公开环境、模型、front filtering/curvature、normalization、所有 hyperparameters、seed、learning curve 与 token/bytes/latency。
- 论文将 heterogeneous costs 与 uncertainty-aware value estimates 视为更现实方向；在安全关键多机器人/分布式系统仍需真实通信验证。

## 与 AAMAS 的关系与核验说明

本文研究多智能体通信的 cost-benefit 调度。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TAYO7266.pdf) 核对双目标 formulation、经验 Pareto/knee、baseline 与 ablation；未把 benchmark communication rate 外推为生产网络效率保证。
