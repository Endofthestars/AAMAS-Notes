---
title: "Grounded Communication Policies in Heterogeneous Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["marl_coordination", "agent_engineering", "human_agent_interaction", "safety_verification"]
dblp_key: ""
doi: "10.65109/OAYF2008"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OAYF2008.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05f"
spark_draft_verdict: "source_grounded_proposal_draft"
spark_qa_verdict: "pass_with_proposed_and_planned_boundary"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_proposal", "heterogeneous_agent_reinforcement_learning", "communication_action_policy_decoupling", "latent_common_ground_approximation", "assumed_shared_beliefs_not_ground_truth", "multi_turn_communication_overhead", "auxiliary_objectives_not_implemented", "planned_experiments_only", "no_semantic_alignment_validation", "no_real_robot_or_human_ai_evaluation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_common_ground_semantics_implementation_status_and_evaluation_boundary_check"
escalation_verdict: "pass_after_assumed_shared_belief_and_proposal_only_boundary_reinforcement"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted common-ground check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Grounded Communication Policies in Heterogeneous Agent Reinforcement Learning

## 一句话总结

这篇 Doctoral Consortium 文稿提出把 heterogeneous-agent reinforcement learning 中的 communication policy 与 action policy 解耦，以多轮消息和 recurrent latent memory 近似维护 task-relevant common ground；框架、LSTM/GRU、辅助目标和三阶段评测都仍是拟实施方案，本稿没有证明 agents 已形成共享语义，也没有当前的稳定性、样本效率、泛化或真实部署结果。

## 问题：信息交换不等于 common ground

作者认为，现有 communication-based MARL 常把 message 当作 policy-network input 或 action-space 的一部分，由选择环境动作的同一 policy 隐式决定传什么信息。这可以扩大局部观察，却没有显式表示信息是否被其他 agents 理解、对齐或共同持有。

该问题在 heterogeneous-agent reinforcement learning（HARL）中更突出，因为 agents 可能具有不同 observation modalities、perceptual resolution 或 action capabilities。例如，一个 agent 看到颜色、另一个看到形状时，仅广播 observation 并不能自动保证二者对同一 target object 具有一致解释（§1，pp. 4026–4027）。

文稿回顾 Traffic Junction、SMAC、Google Research Football、mixed predator–prey 等 benchmark 及多种 communication methods 的表现。这些均是引用文献中的 prior-work 结果，不是本文新实验。

## 本文所说的 common ground

作者借鉴 human dialogue 中 clarification、confirmation 和 repair 的迭代观念，但为本研究给出的 common ground 是：

- dynamic 且 potentially incomplete；
- 仅包含 task-relevant beliefs；
- agents **assume to be mutually held**；
- 可能需要通过 interaction 持续 maintenance、revision 或 repair。

它不等于更完整的 environment state，也不等于单个 agent 的 observation space。更重要的是，“assume mutually held”不代表这些 beliefs 已成为共享真值、完整共享语义或具有 formal mutual-belief guarantee；本文只拟通过 message exchanges 近似一个 latent context。

## 拟议的解耦框架

作者提出为每个 agent 设置两个 distinct learned components（§2，p. 4027）：

1. **Communication policy**：决定何时通信、发送什么、如何回应收到的消息；目标是更新代表 common ground 的 shared belief 或 latent context。作者计划用 LSTM 或 GRU 跨 communication turns 维护 internal dialogue state。
2. **Action policy**：依据 local observation 和 communication process 提供的 grounded information 选择 environment action。

在该设计中，communication 可与 action selection 并行，每个 environment step 可以有多轮交流，让 agents 反复澄清和对齐 beliefs。communication policy 不拟发送所有可得信息，而是依据对其他 agents capabilities 与 likely actions 的推断，选择预计与其决策相关的 messages。

这些是作者提出的架构行为，不是已实现系统的运行事实。

## Latent memory 与候选训练目标

文稿拟把 common ground 表示为 recurrent latent memory，通过 gated recurrent mechanisms 和 communication actions 更新。该表示不被假定为 globally observable，只由消息交换近似。

除 task reward 外，communication policy **可能**使用以下 auxiliary objectives：

- agents 所推断 beliefs 的 agreement 或 consistency；
- messages 与 relevant latent variables 的 mutual information；
- 对 redundant 或 unnecessary communication 的 penalty。

作者称这些目标旨在塑造 communication behaviour 而不直接干扰 action learning。三页稿没有给出损失公式、权重、训练算法、收敛性质或消融结果；latent consistency 也不能当作真实语义理解的验证。

## 三阶段 Planned Research

§3（p. 4027）把后续研究明确分成三阶段：

1. 在 controlled heterogeneous-agent environments 中实现框架，先从 grid-world 与 predator–prey 开始；
2. 与 communication embedded in action policies 的 MARL baselines 比较 coordination、learning stability 和 sample efficiency，并消融 recurrent communication memory 与 multi-turn communication；
3. 把 learned communication policies 迁移到 novel tasks、unseen agent combinations 或 altered observation modalities，评估 distribution shift 下的 generalisation。

这些都是计划，不是已完成结果。本稿没有实现、dataset、baseline 数值、学习曲线、sample-efficiency 数字、随机种子、统计检验、runtime、ablation 或 generalisation evidence。

## 开销、语义与现实边界

作者预期显式 common-ground modelling 可能增加 computational 和 communication overhead，并把信息持久化、relevance determination、misalignment detection/correction 列为 open challenges；文稿没有测量这些开销。

mixed robot teams 与 human–AI teaming 只作为 potential implications。三页稿没有真实机器人、人类参与者、安全性、鲁棒性、对抗通信、scalability 或 deployment evaluation，因此不能声称该框架已：

- 建立 human-like common understanding；
- 提高 coordination、stability、sample efficiency 或 generalisation；
- 降低通信成本或抵抗噪声/欺骗；
- 支持安全的 real-world 或 human–AI teaming。

## 页码与核验说明

PDF 页脚确认：p. 4026 为摘要、引言和异构通信问题；p. 4027 为 proposed approach、latent representation、learning objectives、planned research 与 significance；p. 4028 为致谢和 References，没有结果章节。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OAYF2008.pdf) 核对问题定义、common-ground 边界、拟议组件与三阶段计划；`reviewed` 表示这些来源主张已核验，不表示计划中的实现或效果已经完成。
