---
title: "Learning to Control Reconfigurable Multiagent Systems"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["robotics_embodied", "marl_coordination", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/UPSM9650"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UPSM9650.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05d"
spark_draft_verdict: "source_grounded_draft_needs_revision"
spark_qa_verdict: "pass_with_controller_count_ratio_and_simulation_boundary_reinforced"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_program", "reconfigurable_multiagent_system", "salp_chain_locomotion", "two_dimensional_simulation", "gnn_ppo_controller", "zero_shot_length_and_disabled_units", "controller_count_ambiguity", "figure_values_not_tabulated", "no_dynamic_docking_or_undocking", "no_underwater_hardware_validation", "future_skill_chaining_and_marl"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_controller_count_zero_shot_ratio_failure_robustness_simulation_and_dynamic_reconfiguration_boundary_check"
escalation_verdict: "pass_after_internal_count_ambiguity_and_simulation_only_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted controller-evidence check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Learning to Control Reconfigurable Multiagent Systems

## 一句话总结

本文把 salp chain 的结构映射进图神经网络控制器，并在 SCLD 的二维 locomotion simulation 中测试未见链长和 disabled units；这些 zero-shot 结果不构成动态 docking/undocking、真实水下硬件或任意链长控制的验证。

## 可重构 salp chain 的控制问题

Reconfigurable Multiagent Systems（RMSs）由能够 docking 和 undocking 的个体 agents 组成，可形成具有新能力的 composite agent。本文以 salp-inspired agents 为例：每个 salp unit 使用喷射推进，多个 units 可连成链（§1，p. 4017）。

作者指出三个问题：

1. 单个 unit 的推进只有一个自由度，整条链的平移和旋转需要协调多个喷口；
2. 增加或移除 units 会改变自由度，固定结构控制器通常需要为新配置重新设计；
3. 链中 units 可能失效，控制器需要在失效下保留性能。

本稿当前只测试固定策略对不同测试链长和 disabled units 的泛化，没有展示一次 episode 中真实执行 docking、undocking 或拓扑变化。

## SCLD 与控制任务

Salp Chain Locomotion Domain（SCLD）模拟二维 linked salp-unit chain（§3，p. 4018）：

- 每个 episode 的目标 pose 在形状和位置上变化；
- 每个 salp unit 只有沿一个自由度施加向前或向后力的能力；
- units 通过 revolute joints 连成链；
- 每个 unit 获得属于整体目标 pose 的可达目标位置；
- 控制目标是协调局部力，让整条链同时完成平移与旋转并匹配目标 pose。

论文把该问题写成 MDP，包含状态 \(S\)、动作 \(A\)、奖励 \(R(s)\)、转移 \(P(s'|s,a)\) 与策略 \(\pi(a|s)\)，并使用折扣回报定义 value（§2，p. 4018）。

Figure 1 把 normalized mean distance reward 的 1.0 定义为整条链完全匹配目标 pose。论文没有给完整奖励函数、episode horizon 或所有曲线点的表格值。

## 图控制器与源内计数歧义

salp units 被表示为图节点，连接关系构成边。论文比较：

- GCN；
- GATv2；
- GT；
- mixed graph structure；
- fully connected graph structure；
- 以 PPO 训练的 MLP baseline。

正文同时写道：每个 `model-topology pair` 训练两个 controllers，分别使用 8-unit 与 16-unit chain；紧接着又称最终有 6 个 graph-based controllers 和 1 个 baseline MLP controller（§3，p. 4018）。

结合三种 GNN、两种 topology 和两种训练长度，这个对应关系无法由三页稿安全消歧。最稳妥的记录是：**原文报告 6 个 graph-based controllers 和 1 个 MLP baseline，但 model-topology pair、两种 topology 与 8/16-unit 训练之间的精确映射不清楚。** 本笔记不自行把它重算为 6 或 12。

## Zero-shot 评测范围

策略在 8-unit 或 16-unit chain 上训练，再执行两类 zero-shot 测试（§3 与 Figure 1，p. 4018）：

- 未在训练中出现的 chain lengths；
- 逐渐增加的 disabled salp units。

最大评测链长为 40 units；disabled units 的最大数量是训练链长的 50%。这里的 zero-shot 只表示 SCLD 中未见链长与 disabled-unit 条件，不表示未见真实水域、动态结构重构或硬件故障类型。

## 90% 性能与长度—鲁棒性权衡

摘要称 graph-based controllers 在 zero-shot 设置下最多保留 90% performance，并称 SCLD 结果在最长为训练长度两倍的链上保持 90% performance。正文进一步指出：

- 使用更长链训练，会使控制器在更长测试链上维持 90% threshold，体现更强 scalability；
- robustness 呈相反趋势；
- 随 train-length / zero-shot-length ratio 增加，16-unit GT controller 能处理的 disabled units 数量下降 6.25%；
- 8-unit GT controller 在 2:3 ratio 时的 robustness，与它在 1:1 ratio 下测试时相同。

这些是来源文字对 Figure 1 的解释。论文没有印出完整曲线数据、6.25% 的分母或所有阈值交点，因此不能把比例换算成未披露的绝对 unit 数，也不能据图虚构模型排名或统计显著性。

`up to twice the training length` 也不是任意长度保证；评测上限仍为 40 units。

## 尚未完成的动态重构研究

§4（p. 4018）明确把更复杂任务放在 proposed research：

- 把低层 locomotion 抽象为 macro-actions；
- 使用 skill chaining；
- 学习 spread out、converge、break into subchains 等技能；
- 用 multiagent RL 决定何时 docking/undocking，以及选择何种 chain configuration；
- 通过拆分绕过障碍，再重组为包围不规则目标的形状。

本稿没有上述高层策略的实现、训练或结果，也没有 obstacle avoidance、target enclosure、动态 topology change 或 regrouping 实验。

## 复现与现实部署边界

三页稿没有给 PPO 超参数、训练步数、随机种子、重复次数、网络层数、消息传递次数、完整 reward、failure sampling protocol、方差、置信区间、代码或运行成本。

所有当前结果来自二维仿真。引用文献中的真实 salp-inspired hardware 不能倒灌为本文实验；本稿没有水池/海洋测试、流体动力学迁移、传感器噪声、执行器故障、安全性或现实能耗数据。

## 与 AAMAS 的关系与核验说明

该工作把可变规模机器人结构、GNN policy、强化学习和 failure-condition generalization 放入多智能体控制问题。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UPSM9650.pdf) 核对引言（p. 4017）以及 SCLD、§§3–4 和 Figure 1（p. 4018），并保留 controller count 的源内歧义和 simulation-to-hardware 边界。
