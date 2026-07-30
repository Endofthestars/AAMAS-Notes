---
title: "Learning Preferences and Resolving Conflicts in Multi-User Personalisation in Human-Robot Interaction"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["human_agent_interaction", "argumentation_reasoning", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: "10.65109/TBUZ5275"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TBUZ5275.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05i"
spark_draft_verdict: "source_grounded_draft"
spark_qa_verdict: "pass_with_current_future_full_paper_and_assistive_safety_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_program", "multi_user_preference_conflict", "base_score_not_complete_human_value", "rq1_author_reported_validation_summary_only", "bsef_full_paper_boundary", "llm_elicitation_future", "contestability_explanations_future", "linear_argument_strength_not_system_realtime", "user_studies_planned", "assistive_and_older_adult_context", "no_clinical_safety_or_deployment_validation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_contestability_representation_full_paper_human_study_and_assistive_safety_check"
escalation_verdict: "pass_after_current_future_base_score_user_study_and_clinical_boundary_reinforcement"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted contestability and assistive-HRI check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Learning Preferences and Resolving Conflicts in Multi-User Personalisation in Human-Robot Interaction

## 一句话总结

这篇 Doctoral Consortium 文稿当前概述了两项工作：以 Gradual Argumentation Framework 整合多个用户的 arguments、reasons 与 robot observations 来处理 preference conflicts，以及用 Base Score Extraction Functions 把单个用户的 ordinal preferences 映射为 argument base scores；主动 LLM elicitation、feedback-driven updates、自然语言解释、contestability、主动确认和用户研究仍是 future work，尚无临床、照护安全或长期部署证据。

## 四个问题缺口与研究问题

作者把 multi-user HRI personalisation 的缺口归纳为（pp. 4047–4048）：

1. **single-user limitation**：照护场景中 patient、caregiver、therapist 等多方偏好可能冲突；
2. **changing preferences**：偏好与 context 会随时间变化，传统 data-driven model 可能需新增数据并 retrain；
3. **qualitative–quantitative mismatch**：复杂、带理由的 human preferences 被压成单一 scalar utility 时会丢失语义；
4. **opacity**：无法解释为何作出决定，就难以让用户 challenge、correct 或 influence system。

相应 RQ1–RQ4 询问：如何解决多用户冲突、如何表示 preferences/reasons/context、如何主动获取和更新 user knowledge，以及什么解释能让用户有效影响 robot decisions。

## GAF 表示及其边界

Gradual Argumentation Framework（GAF）给每个 argument 一个 numerical **base score**，再结合 argument relations 计算 **final strength**，据此选择决定。

在本文语境中：

- base score 表示某用户赋予某个 argument 的重要性；
- final strength 是 argumentation computation 的结果；
- users’ reasons 与 robot environmental observations 都可成为 arguments；
- 插入或修改 arguments 可改变模型，而无需重新训练 data-driven policy。

base score 不是完整 human value、全局 utility function、偏好不确定性或全面 user model；final strength 也不证明最终行动正确、公平或安全。

## RQ1：当前 multi-user conflict framework

文稿把 RQ1 列为 contribution to date（p. 4048）。框架：

- 汇集 multiple users’ arguments 与 reasons；
- 把 robot observations of the environment 也表示为 arguments；
- 生成相应 GAF；
- 允许新 arguments 插入或已有 arguments 修改；
- 依据 final strengths 作出决定。

作者称该 framework 已“validated theoretically and through a use case”，use case 是 assistive robot 为 older adults 做 frailty assessment。三页稿没有 theorem、proof、formal conditions、use-case protocol、participants、metrics、results 或 user-study evidence，所以只能保留为作者的概述性验证声明。

“resolve conflicts fairly”是目标描述；稿内没有 fairness definition、aggregation rights、priority rule、power imbalance analysis 或 formal guarantee。

## RQ2：当前 BSEF contribution 与 full-paper 边界

Standard GAF 通常以 heuristic 或 aggregate data 设置 base scores，难以形成 individual user model。作者提出 Base Score Extraction Functions（BSEFs），把单个用户对 arguments 的 stated ordinal preferences 转为 GAF 所需的 quantitative base scores（p. 4048）。

该 current contribution 对应仓库中的 AAMAS full research paper `LIEI2830`，已有[正文级 reviewed 笔记](./user-preferences-base-score-gradual-argumentation.md)。本笔记不把 full paper 的函数、性质、synthetic experiments、数值或 feeding graph 倒灌到三页 DC 文稿。

DC 稿只支持 BSEF 的输入–输出目的；它没有说明 ordinal elicitation 是否准确、argument set 是否完备、不同 semantics 是否一致，或 mapped scores 是否代表真实偏好强度。

## RQ3：Future LLM-assisted active learning

RQ3 位于 **Future Directions**。作者拟开发 agentic system：

- 以自然语言主动询问 users’ preferences 与 reasons；
- 解释用户 challenge robot decision 时提供的新 argument、contradiction 或 model correction；
- 在用户纠正某个 argument importance 后更新 base scores；
- 不依赖重新训练 data-driven model。

LLM 在这里是拟议的 elicitation 与 feedback-interpretation component。文稿没有实现、模型、prompt、accuracy、hallucination/error handling、privacy、security 或 update-correctness results；不能声称系统已理解用户或可靠修正 user model。

## RQ4：Future explanations 与 contestability

RQ4 同样是 future work。作者希望：

- 把 argument attribution 或 counterfactual explanation 转成 natural language；
- 让用户据此 influence robot decisions or beliefs；
- 根据可能的 framework changes 预测 future decisions；
- 主动 warning user 并等待 confirmation。

文稿说 argument **final-strength computation** 是 linearly complex，因此可能快速评估 changes。该复杂度不涵盖 LLM、speech、perception、user modelling、robot control 或 end-to-end latency，也不是 real-time 或 safety guarantee。

contestability 仍是设计目标；稿内没有测量用户是否理解解释、是否能成功纠错、是否感到被赋权，或不同 stakeholders 的 contest 权如何冲突。

## Planned user studies 与 assistive 场景

作者计划与 Barcelona healthcare partners 在 assistive scenarios 做 user studies：

- frailty-assessment robots（引用的系统 already implemented）；
- robotic feeding；
- home robots。

“already implemented”修饰引用的 frailty robot 场景，不等于本 DC 的完整 argumentation framework 已完成 user study、clinical validation 或 deployment。feeding/home 也是引用的候选研究场景。

三页稿没有 participant counts、demographics、recruitment、protocol、control group、metrics、longitudinal outcomes、ethics approval、consent、privacy、failure handling、安全事件或 code。

## 高影响 HRI 与安全边界

older-adult assessment、feeding 和 home assistance 涉及健康、身体与照护权力关系。本稿不能支持：

- robot 已公平解决 patient/caregiver conflicts；
- base score 已忠实表示完整 human values；
- natural-language explanations 已提高 understanding、trust 或 influence；
- 系统已长期适应 changing preferences；
- robot 可替代 clinicians、caregivers 或 user consent；
- framework 已在 frailty、feeding 或 home 场景安全部署。

任何后续实物研究仍需 independent safety layer、human override、role/consent governance、privacy protection、uncertainty and failure reporting、ethics review，以及对弱势用户理解负担和 stakeholder power imbalance 的评估；这些不是本文当前结果。

## 页码与核验说明

PDF 逐页核对：p. 4047 为摘要、四个 gaps、GAF 引介与 Figure 1；p. 4048 为 RQ1–RQ4、Methodology、当前 RQ1/RQ2、Future RQ3/RQ4 和 planned user studies；p. 4049 为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TBUZ5275.pdf) 核对 current/future 状态、base-score 表示、full-paper 关系和 assistive-HRI 边界；`reviewed` 不表示拟议的 LLM、contestability 或用户研究已经完成，也不表示临床或照护安全有效。
