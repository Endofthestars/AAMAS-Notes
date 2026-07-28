---
title: "Feasible Constraint Policy Optimization for Safe Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "marl_coordination", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VKKT4028.pdf"
code_url: ""
note_status: "reviewed"
review_route: "manual_safety_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "not_used"
spark_qa_verdict: "manual_safety_scope_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["safety_claim_scope", "optimization_assumptions", "approximate_implementation"]
escalation_model: "none"
escalation_reason: "terra_service_unavailable"
escalation_verdict: "manual_scoped_review_after_terra_connection_failures"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source safety check; Terra service unavailable)"
reviewed_at: "2026-07-29"
---

# Feasible Constraint Policy Optimization for Safe Reinforcement Learning

## 一句话总结

FCPO 将精确惩罚、信赖域与 ADMM 分解结合，以处理初始策略可能不可行的 CMDP；论文在 Safety-Gymnasium 任务中比较奖励与成本约束表现。

## 方法与证据

- §2 定义 CMDP 的折扣奖励 `J(π)`、成本 `J_k(π)` 和可行策略集。FCPO 以精确惩罚扩展优化问题，再引入信赖域和 ADMM 分解，并用一阶/PPO 风格参数化更新实现（Algorithms 1–2、§3）。
- Propositions 1–2 的“相同最优解”只在最优拉格朗日乘子存在且惩罚系数 `σ ≥ ||ν||∞` 等条件下成立，针对原始问题与精确惩罚问题的关系。
- Theorem 3 说明存在足够大的 `σ` 时，文中 Algorithm 1 的策略序列具有惩罚目标非下降、在当前策略满足约束时的单调性能改进且不违反约束、以及约束违反度非增等性质。
- §3 同时明确实际实现以采样近似状态分布、以参数化策略替代一般策略，并以 PPO clipping/ADMM 求解近似优化；这些实现近似不应自动继承所有精确问题的保证。
- §4 的 Figures 2–3 在 Safety-Gymnasium 的任务中比较 FCPO 与 CPO、FOCOPS、P3O 等，报告多数任务的奖励与成本约束结果；这是仿真实验比较而非部署安全认证。

## 安全范围、局限与复现

- 论文的可行性/单调性语言须连同 Proposition 1–2、Theorem 3 的惩罚系数、最优乘子、精确优化和当前可行策略等条件理解；它不是每个参数化 PPO 训练步的无条件安全保证。
- Safety-Gymnasium 结果不证明真实机器人、人类环境或任意 CMDP 的安全，也不涵盖模型误差、传感噪声或分布漂移下的部署风险。
- 复现需固定 CMDP 成本定义、`σ`、信赖域、ADMM/PPO 超参数、采样方案与 §4 基准；应分别报告理论 surrogate、近似训练过程和经验成本结果。

## 与 AAMAS 的关系与核验说明

论文属于安全强化学习与约束决策。两次 Terra 审计因服务端连接失败未能完成；为避免扩大安全主张，本笔记按原文命题条件和近似实现做了人工范围审阅，并在前端元数据中明确该限制。
