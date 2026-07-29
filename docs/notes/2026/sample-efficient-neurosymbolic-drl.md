---
title: "Sample-Efficient Neurosymbolic Deep Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/RPUM9981"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RPUM9981.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02r"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "partial_policy_quality", "officeworld_only", "epsilon_greedy_scope", "baseline_tuning_asymmetry"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Sample-Efficient Neurosymbolic Deep Reinforcement Learning

## 一句话总结

SR-DQN 将在较简单环境学到的 ASP 部分逻辑策略迁移到更长时程任务：推理出的建议动作在 \(\epsilon\)-greedy 探索中获得更高抽样权重，并在利用阶段按随 \(\epsilon\) 衰减的因子重标 Q 值。OfficeWorld 的 DeliverCoffeeAndMail 与 PatrolABC 上，摘要称其末期回报更高、方差更低于 DQN 和调优后的 reward-machine DQN；结果取决于逻辑映射、部分策略质量、手定置信度 \(\rho=0.8\) 和同域任务扩展，不能保证不良规则在其它领域不会误导学习。

## 方法与证据

- 将 MDP 的状态特征与动作映射至 ASP Herbrand bases，以形如 `a :- f1, ..., fn` 的 normal rules 表示部分策略 \(\pi_{ASP}\)；给定当前状态求 answer set 得到建议动作集合 \(A_{\pi_{ASP}}\)（§2）。
- 探索时，建议动作权重为 \(\rho\)，其余为 \(1-\rho\)，归一化后抽样；若没有建议则退化为均匀随机。利用时将每个动作 Q 值乘以 \(k_a=1+\epsilon w_a\)，从而在训练初期放大符号建议、随 epsilon decay 逐步让神经估计占主导（§2.1）。
- 作者明确允许不完美知识；\(\rho\in[0,1)\) 表示对规则的信任度。论文将方法写在 DQN 中，但主张可扩展至其他 epsilon-greedy DRL；这不是对任意 actor-critic、连续动作或离策略算法已验证的结果（§2--4）。
- 实验使用 OfficeWorld：从较简单 DeliverCoffee/PatrolAB 学得的规则迁移到 DeliverCoffeeAndMail/PatrolABC，比较 DQN 和 reward-machine DQN。基线 DQN 先在易任务调参，随后同一超参数用于难任务；RM-DQN 尝试不同 transition rewards 并保留调优情景中最优设置，\(\rho=0.8\)。图 1 显示 SR-DQN 末期平均回报最高、相对 DQN 方差更低，而 RM-DQN 更慢且平均回报较低（§3--4）。

## 适用边界与复现

- 适合稀疏奖励、离散动作、可把状态/动作可靠映射到逻辑符号、且存在可迁移的浅层顺序知识的任务；规则并非安全约束，错误建议仍会影响探索和 Q 选择。
- 置信度 \(\rho\)、epsilon schedule、规则覆盖率/冲突、ASP 推理延迟及 feature/action grounding 决定效果；固定 \(\rho=0.8\) 不是校准结果。训练分布外、规则互斥或无建议状态可能使优势消失。
- OfficeWorld 两类任务的图示没有给出全部随机种子、置信区间、样本量或跨领域数据；RM-DQN 的 reward tuning 与 DQN 的易任务调参也需完整公布，才能判断比较公平性。
- 复现应开源 OfficeWorld 版本、逻辑规则来源/学习过程、grounding、\(\rho\)/epsilon、DQN 与 RM 全部超参和每 seed 曲线；做规则噪声、置信度、无规则、错误规则、不同 horizon/域外任务及 wall-clock ASP 开销消融。

## 与 AAMAS 的关系与核验说明

该文将符号推理作为自主体 DRL 的可解释探索/利用先验。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RPUM9981.pdf) 人工核对 ASP 部分策略、双阶段权重/重标、\(\rho=0.8\)、OfficeWorld 任务迁移和图 1 比较；未将该同域实验夸大为普适样本效率或安全结论。
