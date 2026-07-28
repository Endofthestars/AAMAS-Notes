---
title: "TEACH: Temporal Variance-Driven Curriculum for Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ADKV2733.pdf"
preprint_url: "https://arxiv.org/abs/2512.22824"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["soft_policy_approximation_scope", "goal_sampling_scope", "benchmark_generalization"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# TEACH: Temporal Variance-Driven Curriculum for Reinforcement Learning

## 一句话总结

TEACH 是用于连续目标空间 goal-conditioned RL 的 teacher：它按近期 policy-confidence 的时间方差重采样目标，把训练重点放在价值估计变化较活跃的 skill frontier。

## 方法与证据

- 在 multi-goal MDP 中，student 是以 state 与 goal 为条件的策略，teacher 在 episode 开始时选择目标；训练使用 DDPG actor-critic 与 replay buffer（§3–4）。
- 对每个目标，policy-confidence 定义为 replay-state 分布下 $Q^{\pi}(s,g,\pi(s,g))$ 的期望。TEACH 在时间窗口内计算该标量的方差，再按方差归一化的概率采样有限个预先均匀抽取的候选目标（Eq. 7–11、Algorithm 2）。
- 其理论联系是：在 soft policy update、温度 $\alpha>0$、小 $\Delta Q$ 与小策略更新的一阶/二阶近似下，相邻策略 KL 近似正比于动作分布下 $\Delta Q$ 的方差（Eq. 5、Appendix A）。这为“高时间方差对应较显著策略演化”提供启发式依据。
- 实验覆盖 11 个 robotic manipulation 与 maze-navigation 的目标条件任务；论文将 TEACH 与既有 curriculum/goal-selection 方法比较，并报告更快或更稳定的学习曲线（§5）。

## 局限与复现

- KL–Q-variance 关系不是一般 DDPG 的无条件收敛定理：推导采用 softmax policy，而实际训练为带探索噪声的 deterministic DDPG，并依赖小更新 Taylor 近似。
- 课程分布仅在固定的 $N$ 个初始均匀候选目标上近似，不能声称对整个连续目标空间精确归一化或覆盖。
- 高方差也可能来自 critic 噪声；时间窗口旨在缓解该问题，但不构成鲁棒性保证。11 个指定环境上的结果不能推及稀疏奖励、离散动作或安全关键部署。
- 复现应固定候选目标集、窗口 $n$、更新频率 $\Delta$、DDPG/hyperparameters 与随机种子；同时记录 success、样本量与 confidence-variance 分布，避免只比较最终回报。

## 与 AAMAS 的关系与核验说明

该文将自动课程学习用于 goal-conditioned agent 的训练调度。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2512.22824) 核对了 Eq. 5、Eq. 7–11、Algorithm 2、附录近似前提及实验任务范围。
