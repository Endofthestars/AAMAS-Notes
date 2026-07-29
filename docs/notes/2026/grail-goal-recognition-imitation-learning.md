---
title: "GRAIL: Goal Recognition Alignment through Imitation Learning"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["human_agent_interaction", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/ZCPS6180"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZCPS6180.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04g"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["goal-recognition", "imitation-learning", "inverse-rl", "suboptimal-behavior", "closed-set-goals"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# GRAIL: Goal Recognition Alignment through Imitation Learning

## 一句话总结

GRAIL 对每个候选目标用 imitation learning 或 AIRL 从示范学习目标条件行为策略，再以各策略对观测到的部分轨迹的 likelihood 进行一次前向评分，从而把系统性偏好或次优行为作为可学习信号而非 optimality noise。

## 方法与证据

- 标准 GR 常假设 actor 近似奖励最优；GRAIL 将 closed-set candidate goals 拆为逐目标 IL problems。IL 学 policy，AIRL 只用于取得 goal-directed policy head，测试阶段不做 reward recovery 或 planner invocation（§1–2）。
- 输入为 state/action 的部分 observation sequence 与候选 goals，输出最大 likelihood 的 goal；这保留单次前向式识别，同时使 learned policy 可表征诸如偏好公园路线的系统偏差（§1–2）。
- MiniGrid 和 PandaReach 评估称：有系统偏差的 MiniGrid 上 GRAIL variants 接近完美、Q-learning GR 接近随机；PandaReach 的 noisy optimal 条件优于 actor-critic，而 clean optimal 时与 RL-GR 持平或稍弱（摘要、§1）。

## 适用边界与复现

- 结论限于受控的 closed-set goals、提供逐目标 demonstrations 的环境；真实开放目标空间、goal drift、对抗性伪装与示范偏差可能令高 likelihood 不等于真实意图。
- 复现需公布 candidate goal sets、demo collection/noise/bias 注入、IL/AIRL variants、policy architecture、轨迹评分/normalization、splits/seeds 和每种 partial-observation 长度。交互应用不得把预测 goal 自动当作用户授权。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZCPS6180.pdf) 人工核对逐目标策略学习、测试期 scoring 与 MiniGrid/PandaReach 结论；未将受控识别准确率外推为对人类意图的可靠判断。
