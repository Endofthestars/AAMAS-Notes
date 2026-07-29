---
title: "Towards AI-Sympathy Using Agents"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["human_agent_interaction", "agent_engineering", "safety_verification", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/TJGL1277"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TJGL1277.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-04p"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_schema_and_stage_revision"
spark_consistency: "pass_after_pdf_layout_reconciliation"
risk_level: "medium"
risk_tags: ["blue_sky_vision", "human_agent_teaming", "agent_self_modeling", "trust_calibration", "deception_open_problem", "no_system_or_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; Codex PDF-layout and source reconciliation"
reviewed_at: "2026-07-29"
---

# Towards AI-Sympathy Using Agents

## 一句话总结

本文提出 cognitive sympathy 框架，用 AI-sympathy、Human-sympathy 和 Self-sympathy 描述人理解 AI、AI 理解人及 AI 表征自身局限的互补需求，再给出 Foundations、Integration、Co-Agency、Co-Evolution 四阶段研究路线；这是 Blue Sky 概念议程，没有实现系统、用户研究或安全性评测。

## 三种 sympathy 与团队基础

- **AI-sympathy** 是人对 AI 如何处理信息、学习、推理和失败的、具有技术依据的敏感理解；它要求人了解模型约束和失效模式，而非把 AI 拟人化（§1、§2.1，pp. 3905–3906）。
- **Human-sympathy** 是 AI 建模、适应并尊重人的认知、情绪、情境和操作约束的能力，包括降低认知摩擦、预判误解与 automation bias、尊重价值和情绪边界，以及支持而非取代人的判断（§2.2）。
- **Self-sympathy** 是 AI 表征自身内部状态、能力与局限，评估输出是否适合当前任务，并在不可靠时请求澄清、提高透明度、切换策略、降低自治或让渡决策的能力。作者把它与预先写死的 guardrail 区分：目标是由智能体自己的模型识别情境性局限（§2.3）。
- 路线图把三种 sympathy 映射到高效团队的四个基础：**Shared Understanding、Decision-Making Model、Communication & Collaboration、Trust**。这些是组织与团队研究中的既有概念，本文的贡献是把它们组织进 cognitive sympathy 议程，而非重新实证这些基础。

## 四阶段路线图

1. **Stage 1 — Foundations**：建立人的心智/认知负荷、AI 能力边界与共享世界的显式表示，以及早期联合决策、双向可解释沟通、信任指标和安全委托规则；多数能力仍在设计时静态定义。救灾例中，无人机发现粉尘超出传感器可靠范围并报告检测退化，人类提供“先找幸存者”的任务优先级，协同仍主要依靠人工（§4.1，p. 3907）。
2. **Stage 2 — Integration**：人在合作中学习 AI 的推理与约束，AI 持续适应人的经验、压力和变化中的认知状态；需要同步人、AI 和团队目标，进行 mixed-initiative 角色协商、多模态解释与不确定性沟通，并动态校准过度/不足信任。例中无人机依据团队压力和命令调整搜索，同时用实时反馈帮助人解释不确定性（§4.2，p. 3908）。
3. **Stage 3 — Co-Agency**：设想双方成为可流动地 lead、follow、teach 的共同代理，维护风险、策略、情境和人类状态的联合模型，并协商角色、意图与自治边界。例中 AI 提出撤离方案，但在两条高风险路线的伦理取舍处让渡给人，并解释其推理和局限（§4.3）。
4. **Stage 4 — Co-Evolution**：在跨任务和多次部署中互相塑造能力，形成单方都未预先具备的策略、沟通协议和协作惯例。原文的 drone–human “triage funnel” 是这一阶段的设想：它被描述为经共同试验逐步涌现，而不是本文已设计或部署的方法（§4.4）。

## 证据边界与后续验证

- §3 回顾的 ontology、BDI、Theory of Mind、goal recognition、cognitive-load estimation、agent introspection、形式验证与 explainability 都是已有研究线索；论文没有把这些组件集成为可运行 cognitive-sympathy 系统。
- 四阶段救灾过程是同一个说明性场景，不是实验记录。文中没有参与者、任务、对照组、实现细节、性能指标或统计结果，不能据此断言 sympathy 机制已经提高团队效率、韧性、信任或安全。
- 作者列出的后续工作包括：Self-sympathy 的反思模型；以通信效率和 human mental models 等为例的指标与基准；人机团队的目标表示、协议模型、标准与参考架构；共享且可解释的决策模型；防止 deception 或 AI-sympathy 被不道德使用；以及模型的 resilience 与 fault tolerance（§5，p. 3908）。
- 实证时还需区分“系统声称了解自身”与可校准的能力估计，测量人是否形成更准确的 AI 心智模型，并在压力、误导、能力漂移和价值冲突下检验让渡、信任与安全机制。

## 与 AAMAS 的关系与核验说明

本文把 human-agent interaction、认知与信任建模、智能体通信、自治分配和安全治理串成面向 AAMAS 社区的研究议程。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TJGL1277.pdf) 核对 §2 的定义、§4.1–4.4 的阶段和 §5 的开放问题；特别按 PDF 第 3908 页阅读顺序确认 triage-funnel 示例属于 Co-Evolution，未把双栏文本错配为 Integration 的已实现能力。
