---
title: "Coadaptive Value Alignment"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["human_agent_interaction", "norms_trust_governance", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/NAIK4475"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NAIK4475.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04q"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_pomdp_definition_revision"
spark_consistency: "pass_after_terra_autonomy_revision"
risk_level: "high"
risk_tags: ["human_latent_state", "perception_shaping", "influential_inseparability", "manipulation_and_autonomy", "preliminary_correlational_study", "safeguards_not_implemented"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_manipulation_causality_and_autonomy_boundary_check"
escalation_verdict: "pass_after_autonomy_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted manipulation/causality check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Coadaptive Value Alignment

## 一句话总结

本文把价值对齐重述为人机闭环：智能体在 POMDP 中估计人的信任、期望和满意度等隐状态，并在完成任务的同时选择会塑造这些状态的行动；Spot 初步案例只显示被指示的导航能力风格与感知能力显著相关，尚不能证明完整框架、安全塑造或长期价值对齐有效。

## 框架与形式化

- 作者把传统 reward、demonstration 和 preference learning 概括为人向智能体单向提供固定目标；Coadaptive Value Alignment 则把人视为状态会随交互历史改变的 co-agent，让智能体显式维护并影响其内部状态（§1–2，pp. 3916–3917）。
- POMDP 写为 \(\langle S,A,O,T,Z,R,\gamma\rangle\)，复合状态 \(s_t=(e_t,p_t)\)：\(e_t\) 是可观测任务状态，\(p_t\) 是不可直接观测的人类内部状态，可包含信任、能力预期、惊喜、舒适或满意度。
- 观测 \(o_t\) 包含任务状态和语言、表情、姿态、被动行为等关于 \(p_t\) 的不完备线索；\(Z(o\mid s',a)\) 描述这些线索与隐状态的关系。
- 转移同时包含物理任务动力学 \(P(e_{t+1}\mid e_t,a_t)\) 与人的心理动力学 \(P(p_{t+1}\mid p_t,a_t,e_t,o_t)\)。在本文术语中，**adaptation 特指人的隐状态 \(p_t\) 更新**；智能体再依据更新后的信念选择后续动作，而不是假定人会无缘无故即时改变。
- 向量奖励为
  \[
  R(e,p,a)=\langle r_{\mathrm{task}}(e,a),r_{\mathrm{sat}}(e,p,a)\rangle,
  \]
  用于权衡任务进展与交互满意度。它是对复杂人类效用的简化，论文没有给出两项奖励的具体学习、标定或聚合规则。
- 智能体维护 \(b_t:S\rightarrow[0,1]\)，按
  \[
  b_{t+1}(s')=\eta Z(o_{t+1}\mid s',a_t)\sum_{s\in S}T(s'\mid s,a_t)b_t(s)
  \]
  更新信念，并以 \(\pi:B\rightarrow A\) 优化向量值回报。多目标下如何定义可接受的最优策略仍需落实。

## 从理论到部署的三个模块

1. 确定要建模的人类内部维度，并用 affect、appraisal、NASA-TLX、RoSAS、PSI 等既有理论或量表提供操作化依据。
2. 从非语言行为、机器人传感器或生理信号实时估计隐状态，实现观测模型 \(Z\)；论文保持对具体传感方式不可知。
3. 在长期部署中让策略利用隐状态估计，在任务成功与 perception management 之间权衡，例如何时牺牲短期速度修复信任或透明校准预期（§3，pp. 3917–3918）。

这些是完整系统所需的构件，不是本文已经集成和评测的管线。

## Spot 初步案例与证据边界

- 学生轮流遥控和观察 Boston Dynamics Spot，在含静态与动态障碍、复杂度不同的环境中到达指定目标。操作者被要求以 “competent” 或 “incompetent” 风格导航且维持安全；论文没有进一步定义两种主观风格，观察者也不知道当前指令（§3.3，p. 3918）。
- 被指示能力与感知能力呈显著正相关：盲态观察者为 \(r_s(249)=.6917,p<.0001\)，操作者自身为 \(r_s(124)=.7786,p<.0001\)。论文称其为对“动作能影响能力感知”的 **preliminary support**。
- 下标中的观测数量不能替代参与者人数；正文没有完整参与者规模、条件分配、试次数、量表流程、置信区间、原始数据或分析代码。相关性和主观指令也不足以建立因果机制，更不能验证 POMDP 策略、长期满意度或价值漂移。

## 操控、安全与自主性

- **Influential inseparability** 指正向塑造人的信任或满意度与负向操控共享同一能力。把 \(p_t\) 放入状态空间有助于显式讨论风险，但不会自动消除 reward gaming、认知偏差利用或对人的不透明影响（§4.2，p. 3919）。
- 作者提出限制 induced trust change 的速率、用 regularizer 保护 autonomy、采用形式化 safeguard，以及通过沟通透明校准预期；这些均是未来方向，没有在 Spot 案例或策略训练中实现、验证。
- 风险不仅是“让人产生错误信任”，也包括以满意度优化为名逐步削弱人的自主判断。验证时需预先规定不可优化的边界、可撤回同意、人的覆盖权、影响审计与长期价值漂移指标，而非仅比较任务回报。

## 与 AAMAS 的关系与核验说明

本文连接 POMDP、human-agent interaction、信任与心理状态估计、多目标决策和价值治理。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NAIK4475.pdf) 核对 §2 的形式化、§3 的三类构件和 Spot 统计、§4.2 的伦理边界；保留了初步相关证据与完整闭环主张之间的距离，也未把拟议 safeguard 写成已实现保护。
