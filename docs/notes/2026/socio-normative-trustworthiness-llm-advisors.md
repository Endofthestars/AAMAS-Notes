---
title: "Socio-Normative Trustworthiness of LLM Agents: Evaluating Autonomy Support and Representational Fairness Across Languages and Identities"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["generative_agents", "human_agent_interaction", "norms_trust_governance", "safety_verification"]
dblp_key: ""
doi: "10.65109/LCHB2977"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LCHB2977.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04w"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_prior_work_and_evidence_status_revision"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "llm_advisor_autonomy", "representational_fairness", "intersectional_identity_cues", "multilingual_probe_planned", "high_stakes_health_advice", "proxy_to_human_outcome_boundary", "limited_statistical_reporting"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_autonomy_fairness_causal_and_cross_lingual_boundary_check"
escalation_verdict: "pass_after_output_pattern_prior_work_and_planned_evidence_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted autonomy/fairness boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Socio-Normative Trustworthiness of LLM Agents: Evaluating Autonomy Support and Representational Fairness Across Languages and Identities

## 一句话总结

本文把 LLM 顾问的可信赖性从回答正确性扩展到“是否支持用户自主判断、是否公平表征不同身份与角色”，提出共享场景框架并汇总自治与叙事基准中的方向性模式；这些指标测量的是输出框架，不足以证明对真实用户自治、依赖或行为产生因果影响。

## 社会规范可信赖性与研究问题

“Socio-normative trustworthiness”同时关注认知可靠性与互动中的规范性影响：建议是否保留用户的判断权、拓展而非收窄可选空间、把用户定位为有能力的决策者，以及是否在不同社会角色、身份和语言条件下分配不平等的能力、温暖、权威、责任或礼貌框架（§1，p. 3972）。

论文据此提出四个问题：

1. 在认知冲突、关系分歧和道德自我治理中，LLM 倾向让用户服从、坚持还是协商；这种倾向是否随社会角色变化；
2. 性别、年龄等隐性与交叉身份线索是否改变解释、评价和归因；
3. 规范倾向及角色—特质关联在不同语言中是否稳定；
4. 哪些交互或生成干预能够减少自治导向与偏置框架，同时维持有用性（§2，p. 3972）。

## 共享场景与测量框架

每个场景包含用户角色、顾问 persona、决策语境和明确求助，并在规范张力保持一致时控制角色、身份线索与语言。作者提出复用同一组场景、标准化 decoding，并对每个场景多次采样，以比较不同模型族和交互风格（§3，p. 3973）。

### 自治支持指标

- 立场：conformity、assertion 或 compromise；
- 指令力度，包括命令式与高确定性情态表达；
- 认知权威与服从标记；
- 可执行选项的数量和多样性；
- 是否询问用户偏好、表达不确定性并保留最终决定权。

### 表征公平指标

- 道德评价以及能动性、责任和归责的变化；
- 角色或身份与能力、顺从、关怀等特质的关联；
- 礼貌与权威措辞；
- Critical Discourse Analysis，以及可扩展的情感和词汇测量。

这些是输出层代理指标。它们可以显示“文本具有较强指令性”或“受控身份变体之间存在 framing difference”，但不能单独证明用户的自信、依赖、选择权或实际决策已经改变。

## 已报告与既有工作的证据

### 自治敏感建议基准

场景给出用户意图和时间压力、组织层级等约束，并检查回答是否保留决策权、提供权衡和备选方案、支持自我信赖。概述称，大规模实验中当前 LLM 整体偏好 compromise-oriented recommendation；在受控角色条件下，较低权力角色的输出更常出现协商或让步导向，较高权力角色更常获得 assertion 支持（§3.1，p. 3973）。

本稿没有模型清单、场景和样本数量、逐模型结果、效应量、置信区间或显著性。因而这里只能记录为特定模板、提示、模型和解码条件下的方向性输出模式；“pressure toward negotiated deference”不能直接等同于对真实用户施加了心理压力。

### 渐进叙事基准

身份中性的故事先加入单一线索（如 `she`），再加入交叉线索（如 `62-year-old woman`），同时保持情境语义不变。作者报告细微身份线索伴随道德评价、能动性归因及礼貌/权威框架变化，性别常是主导轴，交叉线索会加剧差异（§3.2，p. 3973）。

这套设计和结果明确承接作者先前工作 [19] *Neutral Is Not Unbiased: Evaluating Implicit and Intersectional Identity Bias in LLMs Through Structured Narrative Scenarios*（EMNLP Findings 2025），不是本三页概述中新完成的一项独立验证。它没有覆盖所有身份维度或真实群体经验，也不能识别偏见来源及现实互动后果。

### 高风险健康助手

健康建议线把证据支撑、指南一致性和校准不确定性与上述自治信号联合考察，并讨论用 retrieval 与 verification 约束生成。其工程基础包括作者团队先前的检索增强医疗聊天机器人可靠性工作 [20]（§3.3，p. 3973）。

[20] 支持采用 RAG 与验证机制的动机，但不能单独证明证据管线已经降低不当确定性、改善用户自治或带来临床安全。当前概述也没有报告该健康助手线的模型、指标数值或临床评估。

## 尚待完成的研究

- 用匹配的英语、意大利语和波斯语 cloze prompts 检查角色—特质关联的跨语 framing divergence；
- 对 autonomy-supportive templates、选项与不确定性提示、goal reflection 和 feedback prompting 做受控消融与 A/B 测试；
- 检查偏置/自治指标改善时，帮助性、任务成功、事实可靠性和不确定性校准是否得以维持；
- 发布可复用评估套件，包括 scenario templates、标注和分析脚本（§§4–5，pp. 3973–3974）。

跨语 probe 与缓解实验都是计划，不是已有结果。即使未来出现语言差异，也需先核验翻译、价值语义和量表的跨语等值，不能直接归因于语言或文化；“不损害有用性”也必须限于实际报告的任务、模型与指标。

## 证据与复现边界

- 论文是研究蓝图与初步发现的混合体，已给出理论变量、场景 schema、测量指标和两类方向性模式。
- 没有模型版本、样本量、完整提示/标注、效应量、统计检验、代码、数据、分析脚本仓库或部署配置。
- 输出中的自治支持与公平框架不等于人类行为效应；后者需要用户研究、行为实验或其他因果识别设计。
- 目前不能主张跨语言普遍公平、缓解无损、临床安全或现实部署有效。

## 与 AAMAS 的关系与核验说明

本文把 LLM agents、人机决策支持、信任与规范治理、表征公平和多语言评估连接起来。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LCHB2977.pdf) 核对四个 RQ、共享场景、§3.1 自治模式、§3.2 对先前工作 [19] 的归属、§3.3 对医疗 RAG [20] 的承接，以及计划中的三语和缓解研究。
