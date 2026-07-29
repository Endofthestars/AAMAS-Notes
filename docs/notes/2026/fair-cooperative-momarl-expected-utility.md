---
title: "Fairness in Cooperative Multi-objective Multi-agent Reinforcement Learning using Expected Utility"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "resource_allocation", "agent_engineering"]
dblp_key: ""
doi: "10.65109/YPUN4596"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YPUN4596.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["nash_social_welfare_value_choice", "common_vector_reward_scope", "esr_trajectory_fairness", "global_return_conditioning", "communication_dependency", "benchmark_environment_scope", "decentralized_critic_failure", "no_formal_fairness_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fairness in Cooperative Multi-objective Multi-agent Reinforcement Learning using Expected Utility

## 一句话总结

论文研究共享向量奖励的 cooperative MO-DEC-POMDP，以 Nash Social Welfare（NSW，目标回报乘积）作为 objective-wise fairness scalarization，并主张在非线性 utility 下应优化 Expected Scalarized Return（ESR：逐轨迹先 scalarize）而不是 Scalarized Expected Return（SER：先取期望）。它将 EUPG/MOCAC 扩展为独立的 Dec-EUPG/Dec-MOCAC；由于 ESR policy 必须按全局累计回报条件化，进一步提出 Local-Return-Dec-EUPG，让 agent 通信交换局部累计回报来近似该量。资源分配和 Multi-Walker 实验支持 Dec-EUPG 的公平效率，但 Dec-MOCAC 未能解决任务，且“公平”来自 NSW 与共享目标的建模选择；通信、局部奖励可加性和单次轨迹均衡不等于对 agent、群体或现实受益人的公平保证。

## 方法与证据

- 模型是多目标 Dec-POMDP：每步所有 cooperative agents 收到同一 \(d\)-维 reward vector，维度代表 objectives 而非 agent-specific payoffs（§2）。因此结果不直接处理个体 agent、不同人群或利益相关方之间的分配公平。
- scalarization 取 NSW \(u(r)=\prod_i r_i\)，用于在 objectives 间兼顾效率和均衡（§2.2）。NSW 的零/负回报敏感性、目标尺度和可比较性会决定“公平”排序；论文没有从数据或利益相关方偏好学习该 utility。
- SER 为 \(u(\mathbb E[G])\)，ESR 为 \(\mathbb E[u(G)]\)。对线性 \(u\) 二者等价，非线性时不同（§2.3）。toy MDP 和共同奖励 matrix game 展示 SER 可偏好在不同轨迹中将一目标置零的高方差策略，而 ESR 偏好每次执行回报较均衡的确定策略（§4.1–4.2）。这是对 NSW/给定例子的规范性解释，不是所有风险偏好或所有公平定义下的支配关系。
- Dec-EUPG 的每个 agent 以 local history 和全局 past accumulated return \(G_t^-\) 为条件，并用总轨迹回报的 utility 更新 policy；Dec-MOCAC 以 distributional critic 估计多目标 return distribution（§5.1）。即便 policy 参数分散，执行时需要全局累计量，不能自动满足纯本地信息的 decentralised execution。
- Local-Return-Dec-EUPG 用每个 agent 自己的 accumulated return 和邻居共享的累计回报构建 global-return proxy（Algorithm 1、§5.2）。作者允许训练与执行通信，且只在可通信时更新；没有学习通信策略。性能依赖于 reward 能局部分解、通信覆盖/时序和近似误差，断连/延迟/对抗消息不在结论范围内。
- 评测包含部分可观测 resource distribution/resource gathering（最多 4 agents、4 objectives）与 MOMALand 的 MO-Multi-Walker Stability；比较 centralized single-agent、single-objective decentralized、FEN-Agents、FEN-Objectives 等，并以 NSW 输出衡量（§6.1–6.2）。这些是合成的共同团队奖励任务，不能替代真实 ride-sharing、电网或多方服务公平评测。
- 论文报告 centralized MOCAC 学得快但早收敛；decentralized MOCAC（无论 global/local conditioning）在所测任务中表现最差，归因于 agent-specific critic 看不到决定 value 的 joint action；Dec-EUPG 达到公平有效政策，Local-Return 与 global-return 版本接近（§6.3–7）。因此“第一解法”是对 Dec-EUPG 的经验结果，不是对所有 ESR MOMARL 或 actor–critic 的普遍成功。
- 结论明确把 CTDE ESR、多 policy outer-loop 和更好通信策略留作未来工作（§7），没有给出公平/收敛/样本复杂度的形式保证。

## 适用边界与复现

- 适用于团队共享多维回报、决策者明确接受 NSW 且要求每次 episode/trajectory 不牺牲某些目标的 cooperative MOMARL 研究；尤其适合作为 ESR 与 SER 差异的实验 baseline。
- 不应把 NSW 目标公平直接映射为人群公平、法律合规或 agent 个体公平。部署前需明确 objectives、尺度与下界，处理零/负回报，做跨群体/最坏轨迹审计，并建立通信失败和安全 override。
- 复现应固定 MO-DEC-POMDP、reward decomposition、NSW 预处理、ESR/SER 计算、policy/critic architecture、训练 budgets/seeds、通信 graph/range/频率/丢包、global/local return proxy，逐轨迹而非仅均值报告各 objective、NSW、方差和失败率。
- 后续需评估目标 scale sensitivity、不同 fairness utility（如 Lorenz/Gini/max-min）、agent-specific utility、非可加局部奖励、通信成本与恶意/陈旧信息、CTDE 方法和真实约束下的 out-of-distribution episode fairness。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 cooperative MOMARL、公平多目标决策与 ESR 工作。笔记依据 [AAMAS 官方 PDF（主站）](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YPUN4596.pdf) 核验 NSW、ESR/SER 例子、Dec-EUPG/Dec-MOCAC、全局累计回报限制、Local-Return 通信、评测任务和 Dec-MOCAC 的失败结论；没有把实验性 objective-wise 结果表述为对人群、agent 或现实部署的通用公平保证。
