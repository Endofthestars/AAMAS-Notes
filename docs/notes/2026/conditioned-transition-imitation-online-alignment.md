---
title: "Towards Generalisable Imitation Learning Through Conditioned Transition Estimation and Online Behaviour Alignment"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/VJZU8032"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VJZU8032.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["teacher_action_labels_only_unsupervised", "online_environment_access_required", "mujoco_benchmark_scope", "conditional_local_convergence"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Towards Generalisable Imitation Learning Through Conditioned Transition Estimation and Online Behaviour Alignment

## 一句话总结

UfO 先用 agent 自己在线交互得到的动作—状态转移训练条件生成器，再令策略产生能重构教师状态转移的动作，最后短时对抗微调；它在五个 MuJoCo v4 基准的作者设定中回报和方差均表现最好，但“无监督”仅指没有教师动作标签，且其收敛陈述是条件性的局部结论。

## 方法与证据

- reconstruction 阶段交替冻结策略与生成器：策略用教师 `(s,s')` 最小化 `|s'−G(s,π(s))|`；生成器则由 agent 在线执行 `π(s)` 所得到的环境真实 next state 最小化同类损失（算法 1、式 4–5）。因此不需教师 action，但需要可交互环境、agent action 和 action-conditioned 转移样本。
- adversarial 阶段冻结生成器，用教师与 agent 的相邻状态差分训练 discriminator 并微调策略；论文将该阶段限制为至多约 10 epochs、小学习率与梯度裁剪，以降低遗忘/盲目模仿风险（§3.2、§6.2）。
- 主比较包括 BCO、GAIfO、CILO、MAHALO 和 OPOLO，在 InvertedPendulum、Hopper、Ant、Swimmer、HalfCheetah v4 上以 AER 和相对 random/teacher 的 Performance `P` 衡量。表 1 报告 UfO 在五个任务均 `P≥1`，HalfCheetah AER `9959.6±589.3`，教师为 `9512.3±538.6`；该表称平均自 10,000 seeds。测试 seed 以其首状态未出现在训练/online-play 中筛选（§4）。
- 形式部分：Lemma 5.1 在可微、Lipschitz 梯度、受限学习率/紧集更新下给交替优化到局部 stationary point；Lemma 5.4 还要求生成器近似真实动力学、两时间尺度等前提。对抗阶段的 Lemma 5.6 假设生成器固定、discriminator 近最优、梯度小且裁剪，结论是保留既有行为并改善泛化（§5）。

## 局限与复现

- “unsupervised”不应理解为无需动作或无需环境监督：没有教师动作标注，但 generator 明确以 agent 已知动作与真实环境转移训练，且后段还需 online play；不适用于只能离线拿到视频、不能安全试错的场景，除非另有环境模型来源。
- 同一 `(s,s')` 可由多动作产生时，状态重构本身未必识别教师的唯一 action/intention；算法学到的是可实现相似转移且高回报的 policy，这也解释为何能优于 teacher，而非严格动作模仿。
- 泛化证据限于作者的 MuJoCo、教师权重/Imitation Datasets、所选起始状态筛选和 10,000 seeds；低标准差不自动等价于对动力学、观测噪声、动作约束或真实机器人分布移位的泛化。
- 理论结论没有给全局神经网络收敛、有限样本率或未见状态保证；需逐项验证其可微/有界/近最优 discriminator 假设。复现应发布教师轨迹与权重、所有 seeds/筛选脚本、网络/优化器、online interaction budget、消融和跨动力学评估。

## 与 AAMAS 的关系与核验说明

该文将 ILfO 与在线模型学习/对抗对齐结合，用于从状态轨迹构建 agent policy。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VJZU8032.pdf) 核对两阶段训练、对照、数值与 lemma 假设，未将“教师动作标签无监督”扩展为无环境交互的学习能力。
