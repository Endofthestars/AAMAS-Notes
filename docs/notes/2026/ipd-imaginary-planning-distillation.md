---
title: "IPD: Boosting Sequential Policy with Imaginary Planning Distillation in Offline Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BELB5985.pdf"
preprint_url: "https://arxiv.org/abs/2603.04289"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["learned_model_rollout_scope", "uncertainty_filter_scope", "d4rl_generalization"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# IPD: Boosting Sequential Policy with Imaginary Planning Distillation in Offline Reinforcement Learning

## 一句话总结

IPD 将 learned world model 内的 MPC imagined rollouts、quasi-optimal value function 与 Transformer sequence policy 联合：先增广低质量离线轨迹，再用 value-guided loss 和动态 return-to-go 蒸馏规划结果。

## 方法与证据

- 从原始 offline dataset 学习 expectile/Huber 风格的 quasi-optimal $V,Q$ 与加权行为策略；该 value function 同时识别待修复的低价值 state，并作为后续 prompt 与 action-gradient regularizer（§3.1）。
- world model 用 ensemble Gaussian dynamics 表示 aleatoric 与模型分歧型 epistemic uncertainty；通过 pairwise Gaussian JS divergence 形成 $U(s,a)$，只允许不超过阈值的不确定性集合内 imagined rollout（§3.2）。
- 对选定的 suboptimal trajectory segment，MPC 在 world model 内采样候选序列、以预测奖励和 terminal value 打分并选取首动作；通过 uncertainty check 的 imagined transitions 加进 $D_{aug}$（§3.3、Algorithm 1）。
- Transformer policy 在 $D_{aug}$ 上进行 action sequence regression，同时减去 $\alpha Q(s,\pi_\eta(\cdot))$ 作为 value-guided 项；训练/推断以 $V(s)$ 而非手工设定 return-to-go 作为动态条件（§3.4）。
- 实验在 D4RL 的 locomotion、AntMaze 和 Adroit 类任务比较 value-based 与 Transformer offline RL 基线；消融把 MPC augmentation 与 greedy Q rollout、不同 return-to-go 方案及增广量分开评估，论文报告 IPD 在所测集上取得较高归一化分数与更低测试方差（§4、Table 1、Figures 2–3）。

## 局限与复现

- “可靠”imagined rollout 由已训练 ensemble/JS uncertainty 阈值定义，不是对真实 dynamics error、distribution shift 或安全约束的可证明上界。
- $V,Q$ 被作者称为 quasi-optimal；其 action gradient、state ranking 和 terminal value 都会受离线 value overestimation 与模型误差影响。
- 结论来自 D4RL 指定数据、模型、MPC horizon/rollout 数和超参数；不能外推为所有静态日志、稀疏奖励或真实机器人上的稳定改进。
- 复现应保存原始/增强数据比例、uncertainty threshold、被拒绝 rollout、MPC horizon、ensemble seeds 与 value-estimation diagnostics；还需比较真实环境评估和纯 imagined return，避免将后者当性能证据。

## 与 AAMAS 的关系与核验说明

该文连接 offline world-model planning 与 sequential agent policy。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2603.04289) 核对了 uncertainty 过滤、MPC data augmentation、IPD loss 和 D4RL 实验范围。
