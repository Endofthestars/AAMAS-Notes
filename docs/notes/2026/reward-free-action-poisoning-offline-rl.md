---
title: "Reward-Free Action Poisoning in Offline RL via Conditional Shapley Value Estimation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "marl_coordination"]
dblp_key: ""
doi: "10.65109/WJRF3793"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WJRF3793.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02e"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["offensive_security_research", "offline_rl_data_integrity", "reward_free_attack_scope", "defense_not_evaluated"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Reward-Free Action Poisoning in Offline RL via Conditional Shapley Value Estimation

## 一句话总结

SAPA 是一种离线 RL 数据完整性攻击评估方法：不用数据集中的显式 reward，而以 conditional Shapley value 找出轨迹中高贡献 state--action pairs，再用条件 VAE 生成替换动作，使受污染数据训练出的策略回报下降。

## 方法与证据

- 作者以 conditional value function 处理 state--action pairs 的时序依赖，并对每个 pair 计算 conditional Shapley value；其 subset value 是轨迹中基于近似收益/评分的条件期望累和（Eq. 1--2）。
- 无 reward 时，利用一个小型 expert dataset 训练 scoring function `F(s,a)` 区分专家动作和离线数据中的次优动作，再以 F 的分数替代 value function 中的 reward 项（Eq. 3--4）。这仍依赖专家数据和该评分器对“好动作”的可辨识性。
- 将高 Shapley-value 动作视为关键动作；CVAE 以 state 和 Shapley value 为条件生成替换动作，训练损失为重构项加 KL 项（Eq. 5）。论文的攻击目标是降低所训练 offline RL policy 的 cumulative return，而非提出防御。
- 在 D4RL 的 HalfCheetah、Hopper、Walker2d 上攻击 BC/BCQ/CQL/IQL/DT，并比较 random、advantage、reward-free advantage、traditional Shapley 等选择法。Table 1 显示 SAPA 在表中多数设定有较低的攻击后分数，例如 medium-expert HalfCheetah/BCQ 从原始 86.7 降至 23.2；摘要未给出污染比例、攻击预算或防御评估细节。

## 适用边界与复现

- 此研究用于揭示数据投毒风险和检验防御，不能用于破坏生产系统、车辆、机器人、推荐或其他真实训练数据；部署环境应把它作为受控红队/基准方法，并获得系统所有者授权。
- “reward-free”指不从被攻击数据直接取得 reward，不代表无需先验：算法使用 expert dataset、评分模型、环境/轨迹结构和 CVAE，且 Shapley 估计的计算与近似误差会影响攻击选择。
- D4RL 连续控制基准中的回报下降不等于对现实系统可行或隐蔽；现实日志还涉及访问控制、审计、行为约束、异构数据和安全监控。论文未报告检测/净化/鲁棒训练防御。
- 复现和防御评测应隔离在沙箱中，明确数据/模型许可证、污染预算和动作约束、expert split、F/CVAE 架构与训练、Shapley 近似、seeds、offline algorithm 参数、回报方差及数据完整性检测指标。

## 与 AAMAS 的关系与核验说明

这是离线强化学习安全的攻击面分析。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WJRF3793.pdf) 核对 §2--4、Eqs. 1--5 与 Table 1；保留技术机制以支持防御研究，同时不提供对真实系统实施投毒的操作指南。
