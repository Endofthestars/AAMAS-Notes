---
title: "Heterogeneous RBCs via Deep Multi-Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "applications", "agent_engineering"]
doi: "10.65109/VZHC1838"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VZHC1838.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["macroeconomic_simulation_only", "calibration_and_reward_dependence", "no_empirical_economic_validation", "not_financial_or_policy_advice"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Heterogeneous RBCs via Deep Multi-Agent Reinforcement Learning

## 一句话总结

MARL-BC 将多 household deep RL 接入 Cobb-Douglas RBC 环境，以异质资本/劳动 productivity 生成内生行为；单 agent 可复现 textbook RBC、同质多 agent 近似 Krusell–Smith，异质模拟展示 wealth/consumption 分布，但它是校准的经济模型实验，不是宏观预测或政策工具。

## 方法与证据

- household 观察自身 capital/labour、aggregate capital 和 technology，选择消费比例与劳动；aggregate inputs 驱动 production，productivity 决定个体 wage/interest（§2--3）。
- `n=1`/AR(1) shock 是 RBC limit；大量 ex-ante identical agents 是 KS mean-field limit；用 DDPG/SAC/TD3/PPO 学习并与经典解对照（§3--4）。
- 异质 productivity 产生 wealth、MPC、Gini 分布；从 9 扩到 529 agents 时 SAC 最稳定，最大模型约 50M updates、两小时单 CPU（§4）。

## 局限与复现

- 结果依赖 utility、生产函数、shock、校准、reward 与 RL 超参数；复现 textbook/KS limit 不证明宏观预测、危机或政策反事实有效。
- 有限训练、nonstationarity、seed 与 algorithm choice 可改变结果；异质 productivity 是设定，未覆盖制度、信贷、企业和价格刚性。
- 应公开环境/校准/seed/updates 与同经典解的误差。本文不构成经济、金融或政策建议。

## 与 AAMAS 的关系与核验说明

该文连接 MARL、agent-based macroeconomics 与 heterogeneous-agent GE。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VZHC1838.pdf) 核对 limit cases、算法、异质模拟和计算限制；未将仿真输出视为经济预测。
