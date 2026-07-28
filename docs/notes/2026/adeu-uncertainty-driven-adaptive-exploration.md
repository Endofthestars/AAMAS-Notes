---
title: "A Novel Framework for Uncertainty-Driven Adaptive Exploration"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/HQII4250"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HQII4250.pdf"
preprint_url: "https://arxiv.org/abs/2509.03219"
code_url: "https://github.com/leoBakop/adaptive_exploration"
note_status: "reviewed"
review_route: "manual_safety_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_safety_scope_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["safety_claim_scope", "uncertainty_model_dependency", "simulation_evaluation_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_safety_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source safety check)"
reviewed_at: "2026-07-29"
---

# A Novel Framework for Uncertainty-Driven Adaptive Exploration

## 一句话总结

ADEU（Adaptive Exploration via Uncertainty）把当前策略作为动作分布中心、把不确定性作为分布扩散程度，从而在单个 episode 内随状态在利用与探索之间切换。

## 方法与证据

- ADEU 接受一个状态不确定性机制与 normalizer；离散实验使用 Multinomial，连续动作实验使用 Gaussian。低不确定性使采样动作靠近当前策略，高不确定性则增大偏离并促成探索（§2.1，Equation 1）。
- 该框架可将访问频率/内在动机（如 RND）或 Q 值 ensemble 的 epistemic uncertainty 作为不确定性输入，并把若干既有自适应探索方法表为特例；这说明的是框架兼容性，而非所有机制效果相同（§2.2，Tables 1–2）。
- Theorem 4 针对作者定义的 Increasing-Reward Single-Agent Games，并要求有效的不确定性机制和有限动作空间；其结论是已找到某状态最佳动作后减少在该状态的探索、转向后继探索（§2.1、Appendix D）。
- §3 实现 TD3+ADEU（RND 或 UCB 型不确定性），并同 TD3+RND、TD3+UCB、Noisy Nets 等比较；报告 MuJoCo、DeepSea 和构造的 Frozen Lake 结果，同时提供[代码](https://github.com/leoBakop/adaptive_exploration)。
- 文中提出安全感知变体：令高预期成本状态的采样方差变小，从而贴近已知策略；或将成本与不确定性项结合（§2.3，Equations 5–6）。构造的 Safety Frozen Lake 结果分别报告奖励和平均约束违反（Table 4）。

## 安全范围、局限与复现

- ADEU 的一般理论不是任意 MDP 或真实机器人上的最优/安全保证。Theorem 4 的适用对象有唯一增益动作/邻接结构等明确的 Increasing-Reward 假设，且取决于“不确定性机制有效”。
- “可接入任意不确定性机制”是 API/构造层面的包容性；论文实验自己显示常量或不合适机制会较差，性能依赖所选机制（§2.2、§3）。
- 安全变体的低风险行为依赖导师提供的安全状态/政策、已知或学习到的成本，以及安全初始策略等条件。Table 4 是构造网格仿真，不能证明未知动力学、成本估计误差或真实机器人中的零违规安全。
- 论文结论明确把“计算相邻安全状态允许探索的上界以保证安全”列为 ongoing work（§5）；因此应把本文的 safety-aware 版本理解为启发式/经验探索控制，而非完成的安全认证。
- 复现应固定 TD3 基础实现、RND/UCB 定义和 normalizer、rollout/随机种子、early-termination 环境、成本估计与预训练安全策略，分别报告平均/最大回报和约束违反；不能只复现单一最高分。

## 与 AAMAS 的关系与核验说明

该工作将探索时机作为自主决策问题，并连接不确定性、机器人控制和安全探索。笔记使用作者公开的 [arXiv HTML 原文](https://arxiv.org/html/2509.03219v6) 作为主文本，已将特定游戏的定理、仿真结果和安全扩展前提分开记录。
