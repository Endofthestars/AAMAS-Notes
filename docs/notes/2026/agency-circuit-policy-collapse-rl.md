---
title: "The Agency Circuit: A Neuro-Symbolic Solution for Mitigating Policy Collapse in Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "safety_verification", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/TRFJ2704"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/TRFJ2704.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["predefined_micro_actions", "hand_tuned_helplessness_threshold", "gridworld_only_evaluation", "ten_seed_scope", "curiosity_baseline_scope", "neuroscience_analogy", "no_high_dimensional_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# The Agency Circuit: A Neuro-Symbolic Solution for Mitigating Policy Collapse in Reinforcement Learning

## 一句话总结

Agency Circuit 在 DQN 之外学习一个连续 helplessness signal；其超过阈值时，symbolic predicate 触发 Control Exertion Module（CEM）执行预定义 micro-action，以打断 trap 内的被动循环。它在特制 2D gridworld 中优于 DQN 与 DQN+ICM 并能迁移到两种未见 trap，但成功高度依赖人工给定的触发阈值、micro-action 集和环境结构，不能证明一般深度 RL 或现实自主系统免于 policy collapse。

## 方法与证据

- 论文把 predictable negative feedback 后的 value corruption、重复/不作为描述为“policy collapse”，并借用 learned helplessness 与 mPFC--DRN 的神经科学类比（§1--3）。这是功能性设计隐喻，而非对生物神经回路或心理状态的实证建模。
- 神经子系统从历史 state/reward 学习 raw helplessness \(h_t\)，control value 衰减后形成 effective helplessness；当 \(h_{eff,t}>\theta_h\) 且不在 cooldown 时，Boolean IsHelpless 触发 CEM 的离散微动作，随后回到 base DQN（§4）。解释性来自可见阈值和触发记录，但错报/漏报仍可不必要地覆盖学习策略。
- Table 1 使用 \(\theta_h=0.8\)、history length 50、control decay 0.995、cooldown 10、prediction horizon 20，以及预定义 \(A_{micro}=\{up,down,left,right\}\)（§5）。这把关键 escape affordance 与阈值选择提供给系统；作者将自动发现微动作/元策略列为未来工作。
- trap environment 中，DQN 和 DQN+ICM 的成功率近 0%，AC-DQN 高成功且更低 escape latency；图表均为 10 independent runs 的均值±1 std（§6.1）。基线只覆盖普通 DQN 和该 curiosity mechanism，未与更广的 risk-sensitive、hierarchical、reset/replay 或 model-based RL 系统比较。
- internal-dynamics 图显示阈值触发后 control value spike、effective helplessness 降近零（§6.2）。这验证设计链路在代表性轨迹中按预期发生，不等于 estimator 真实识别了通用“无助”或因果地解释全部性能差异。
- sensitivity 显示低 \(\theta_h\) 过度干预、高 \(\theta_h\) 失于干预（§6.3）；zero-shot 仅在 Sticky Trap 与 Teleporter Trap 两个未见 gridworld 变化中评测，AC-DQN 高成功而两基线 0%（§6.4）。这不足以证明跨动力学、视觉输入、连续动作或长任务的泛化。
- 作者明确限制为低维 gridworld；扩到 Atari/pixel observation 需要 CNN/GRU、面对 gradient interference、长程 recurrence、阈值/损失超参、large action space micro-action design 与 compute cost 等挑战（§8）。

## 适用边界与复现

- 适用于研究可审计的 trap-recovery 与 exploration failure diagnosis，特别是已知存在小型 corrective action 的离散 MDP；它不应被用作心理健康推断、人格/韧性评价或安全关键控制的单独保护层。
- 需要验证“负 return 预测”确实区分可恢复 trap 与合法的暂时低奖励状态。随机奖励、部分可观测、稀疏长延迟回报、非平稳环境、危险动作或高维 continuous action 都可能使阈值触发造成伤害。
- 复现需发布所有 grid layouts/rewards/trap dynamics、DQN/ICM/AC network和训练参数、helplessness target/estimator、\(\theta_h,k,\delta,N,N_{cooldown}\)、micro-action semantics、10 seeds、训练曲线、trigger frequency/precision、成功率/latency及两种未见 trap 的完整轨迹。应增加多种 RL baseline、跨任务/OOD/噪声/误触发消融和统计检验。
- 在机器人或高风险场景中，CEM action 必须先经过安全 shielding/约束验证、人工定义的 emergency policy 和可撤销审计；“恢复 agency”的抽象不能授权跳过物理安全、用户同意或任务约束。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的神经符号强化学习、可解释恢复机制与探索失败论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/TRFJ2704.pdf) 核验 CEM、Table 1、DQN/ICM 比较、10-run 范围、阈值敏感性、两项 gridworld zero-shot 和作者的可扩展性限制；没有把 learned-helplessness 类比或有限 trap 成功误写为一般 RL 稳定性、生物真实性或现实系统安全保证。
