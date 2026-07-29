---
title: "Selective Amnesia: Observation Unlearning in Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/SOOJ3168"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SOOJ3168.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "machine_unlearning_claims", "q_learning_scope", "policy_action_agreement_metric", "not_compliance_deletion_proof"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Selective Amnesia: Observation Unlearning in Reinforcement Learning

## 一句话总结

本文提出针对 Q-learning 的 observation-level reinforcement unlearning（RUL）：Q-Cover 将含目标 observation 的 action value 覆盖为默认 observation 的值，Twin Q-Backward 沿原 policy trajectories 反向替换受影响 Q-values，再由 Bellman optimization 得 policy。它以“与从未见过该 observation 的 scratch-trained policy 的动作一致率”评估，在 LINKT/3×3 gridworld 达 1.0、CliffWalking 为 \(85.76\%\pm4.56\%\)；这不是深度 RL、记忆参数、训练数据或隐私泄露已被可验证删除的通用证明。

## 方法与证据

- target 是 observation component \(o_i\)，剩余观测为 \(o_{-i}\)。RUL 要求 unlearned Q-policy 满足对应 Bellman equation，且 \(\pi^{UL}(o_{-i})=\pi^{RT}(o_{-i})\)，后者是删去 observation 后从头训练的 policy（Definition 1, Eqs. 1–2）。该定义是 functional/policy equivalence，不是证明模型权重、replay buffer、logs、gradients 或输出对被删信息无任何可恢复痕迹。
- Q-Cover 取目标 \(o_i\) 发生变化的 trajectory state-action pair，用该 state 下默认初始 \(o_i^{def}\) 的 Q-value 覆盖当前 Q-value（Eq. 3）。方法假设默认值有意义、目标影响可在记录 trajectories 中定位，并且用于覆盖的 counterfactual Q-value 本身不含残余目标信息。
- 仅覆盖当前 pair 会影响其所有前驱 trajectories，故 Twin Q-Backward 依 Bellman relation 向 episode 起点反向更新 Q-values，随后 Q-Backward Optimization 取 max action（Eq. 4, §2）。完整性取决于 trajectory set \(L\) 覆盖所有依赖路径、环境/transition/reward定义不变、Q-table 可准确编辑；摘要没有给 offline/deep neural Q 的稳定性、近似误差或部分可观测情形。
- UAcc 是在 \(O_{eval}\) 上 unlearned 与 retrained policy action agreement。LINKT Chain 移除 position observation 得 UAcc 1.0；CliffWalking 添加/删除 waypoint indicator 后十个 independently trained policies均值 85.76%、SD 4.56；3×3 grid 两个 task报告 Q-tables match、UAcc 100%（§3）。UAcc 忽略 action-value distance、trajectory distribution、return/safety、membership inference、information extraction和未测 observations。

## 适用边界与复现

- 适合研究小型/tabular Q-learning 的功能性 observation ablation；不应将其作为 GDPR/隐私删除、保密图像/传感器遗忘、模型安全修复或深度 RL unlearning 的合规证明。高风险部署仍需要数据删除、访问控制、重训练或经审计的可认证 unlearning 流程。
- 复现需给 MDP、observation decomposition/default value、target-change/trajectory detection、\(L\) 覆盖、Q-Cover/backward/optimization 实现、\(\gamma\)、scratch retraining、LINKT/CliffWalking/gridworld modifications、seeds和 \(O_{eval}\)。同时报告 UAcc、Q-value/return差、state coverage和各 trajectory 影响范围。
- 应扩展至 function approximation/deep Q、replay/off-policy data、continuous/partial observations、stochastic/nonstationary environments、多目标/敏感 features和多次 unlearning；评估 privacy attacks、parameter/activation probing、OOD policy、forgetting–utility tradeoff与计算成本。对真实敏感传感器问题，应证明数据、缓存、checkpoint和下游导出物都受处理。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 RL/machine unlearning 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SOOJ3168.pdf) 核验 RUL 定义、Q-Cover/Twin Q-Backward、UAcc和三个 tabular testbeds；没有把 policy-level agreement写成通用、隐私或法律意义的完整遗忘。
