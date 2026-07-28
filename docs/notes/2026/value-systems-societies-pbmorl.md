---
title: "Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "human_agent_interaction", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NLVD8864.pdf"
preprint_url: "https://arxiv.org/abs/2602.08835"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["value_operationalization", "synthetic_evaluation_scope", "cluster_interpretation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_value_learning_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning

## 一句话总结

论文以 clustering 与 preference-based multi-objective RL，从轨迹偏好中联合学习社会共享的 value grounding、多个群体 value systems，以及各群体对应的近 Pareto-optimal policy。

## 方法与证据

- 模型在 MDP 中将不同 values 表为多目标 reward 向量，将 value system 表为对这些目标的线性 scalarization；社会不被压成单一偏好，而由多个用户 cluster 表示（§1、§3–4）。
- 方法向样本 agent 查询两类 trajectory pairwise preferences：对 value-system 的偏好和对 value alignment 的偏好，以学习 social grounding、cluster weights 与 per-cluster policy（§1、§4）。
- 每个 cluster 的输出是该群体的 value system 加一项近 Pareto-optimal policy；这是一种由观察偏好驱动的表示/聚类，不是对真实社会价值的客观发现或规范性裁决（§1）。
- 评估将方法与 PbMORL 和 baselines 在两个带 human values 的 synthetic MDPs 上比较；结果只支撑这些合成环境的 approximation/behaviour 学习能力（§1、§5）。

## 局限与复现

- value grounding 的可识别性依赖给定 value vocabulary、偏好查询质量和 MDP 表示；misspecification、策略性回答、群体变化和少数群体覆盖并未由算法自动解决。
- “社会 value systems”是样本内 cluster abstraction，不应被当作社会共识、人口学因果分组或可部署的道德授权。
- 复现应报告 query budget、preference noise、cluster 数/初始化、reward/objective normalization、Pareto quality及跨 seed 稳定性；仅报告总 reward 不足以验证价值对齐解释。

## 与 AAMAS 的关系与核验说明

该工作连接 pluralistic value-aware agents 与多目标偏好学习。笔记基于作者公开的 [arXiv PDF](https://arxiv.org/pdf/2602.08835) 核对其联合学习对象和两项合成 MDP 评估范围。
