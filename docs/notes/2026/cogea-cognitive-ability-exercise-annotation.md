---
title: "CogEA: A Multi-Agent System for Cognitive Ability Annotation of Exercises by Simulating Human Behaviors"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/EDGL6988"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EDGL6988.pdf"
demo_url: "https://youtu.be/y3XLdWIuxNE"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05r"
spark_draft_verdict: "needs_revision_for_accuracy_granularity_page_map_claim_evidence_and_education_risk_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_preliminary_ninety_six_percent_protocol_page_map_generalization_and_downstream_education_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["llm_agents_simulate_not_measure_student_behavior", "ninety_six_percent_extraction_granularity_ambiguous", "expert_protocol_agreement_and_confidence_interval_missing", "knowledge_and_cognitive_type_breakdown_missing", "baselines_seeds_runs_and_error_analysis_missing", "single_middle_school_generalization_unvalidated", "feedback_memory_and_rag_ablation_missing", "automatic_answer_and_explanation_generation", "teacher_oversight_and_escalation_unreported", "bias_and_cultural_validity_unreported", "middle_school_data_governance_unreported", "external_llm_api_data_exposure", "assessment_and_recommendation_effectiveness_unvalidated", "downstream_student_misclassification_harm"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_accuracy_granularity_expert_protocol_simulated_student_claim_auto_generated_content_middle_school_governance_external_api_and_downstream_education_impact_check"
escalation_verdict: "needs_revision_corrected_for_preliminary_accuracy_protocol_generalization_human_oversight_data_governance_and_downstream_education_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted educational-validity and downstream-impact check; Codex source and physical-page reconciliation"
reviewed_at: "2026-07-30"
---

# CogEA: A Multi-Agent System for Cognitive Ability Annotation of Exercises by Simulating Human Behaviors

## 一句话总结

CogEA 让 virtual administrator、至少五个 virtual students 和 virtual teacher 协作维护中学题库，并为每题选择 knowledge concept 与 cognitive type；论文只用 100 道题、4 位专家得到含义未完全定义的 “96% extraction is accurate” 初步结果，没有验证真实学生认知、跨学校泛化、学习评估或推荐效果。

## 系统与教育边界

CogEA 是 LLM-based exercise annotation and maintenance demo，不是真实 student cognitive model，也没有根据 student traces 校准其 “virtual student” behaviors（pp. 4098–4099）。

论文提出这些 annotation 可支持 learning-state assessment 与 exercise recommendation，但没有报告：

- 真实学生或教师 user study；
- learning outcome；
- assessment validity；
- recommendation accuracy 或 educational benefit。

因此 “simulating human behaviors” 表示 agent role-play design，不是对真实学生 problem-solving process 的测量。

## Exercise data schema

CogEA 的 exercise data 有五个 indexes（p. 4099）：

1. `question`
2. `answer`
3. `explanation`
4. `knowledge`
5. `cognitive type`

前三项是 basic indexes；`knowledge` 与 `cognitive type` 是 evaluation indexes。

作者把 cognitive ability 分成：

- **knowledge selection**：题目需要选择哪个 knowledge concept；
- **knowledge application**：该 concept 以什么 cognitive type 被使用。

cognitive type 基于 Marzano’s Taxonomy of Educational Objectives，分为 retrieval、comprehension、analysis、utilization 四类。这个 schema 是作者的 annotation representation，不等于已经证明它完整覆盖学生认知能力。

## Virtual Administrator

virtual administrator 包含 completion agent 与 filtering agent（p. 4099）。

completion agent 检查 `question`、`answer`、`explanation` 是否完整：

- question 不完整时，要求用户补全；未补全的 exercise 不被接受；
- answer 或 explanation 不完整时，agent 自动生成相应内容。

filtering agent 从 knowledge base 为每题选择一个不超过 30 个 knowledge concepts 的 candidate set，供后续 annotation。

自动补 answer/explanation 会改变原始教学内容。三页稿没有说明生成内容的 factuality check、teacher approval、版本记录或错误撤销流程。

## Virtual Students

每个 virtual student 模拟 problem-solving behavior，并为每题选择（p. 4099）：

- candidate set 中一个 knowledge concept；
- 四类中的一个 cognitive type。

为缓解错误，每道题由 five or more virtual student agents 标注。agents 使用不同 LLM APIs 与 contexts 来模拟学生差异。

不同 API/context 只能制造模型输出差异；论文没有用真实 student ability、response pattern、misconception 或 demographic data 验证这些差异是否代表实际学生群体。

## Virtual Teacher

virtual teacher 包含 evaluation agent 与 feedback agent（p. 4099）：

- evaluation agent 评估并整合各 virtual students 的 annotations，决定 final annotation；
- feedback agent 为被认为标错的 virtual students 生成 feedback；
- feedback 写入该 virtual student 的 interaction memory；
- 后续 prompt 通过 RAG module 加入 previous feedback。

作者说这样可避免 previously made mistakes，但没有报告去掉 feedback、memory 或 RAG 的 ablation，也没有说明 teacher 如何确定某个 student annotation 错误。

## Dataset 与模型设置

demonstration 部署在一所 middle school 的 5,100 exercises dataset 上（p. 4099）。agents 调用 GPT、Gemini 与 DeepSeek APIs。

三页稿没有报告：

- subject、grade breakdown 或 language；
- dataset license、collection process 与 quality control；
- GPT/Gemini/DeepSeek 的 exact model/version；
- prompts、contexts 或 temperature/sampling settings；
- API failure/retry policy；
- latency、token use、cost 或 compute。

这些缺失使外部复现和 cross-model attribution 都受到限制。

## 唯一 accuracy evidence

Section 3 的完整结果表述是（p. 4099）：

- 从 dataset 中 randomly selected the annotation of 100 exercises；
- 邀请 four experts evaluate the annotation；
- expert evaluations indicated that **96% of the extraction is accurate**；
- 作者称其为 preliminary validation。

“extraction”的 denominator 与 unit 没有定义清楚。论文没有说明 96% 是：

- exercise-level final-label accuracy；
- knowledge concept accuracy；
- cognitive-type accuracy；
- field-level extraction accuracy；
- 四位专家 individually 或 aggregated 的比例。

因此本笔记保留原始措辞，不把它改写为全库准确率、最终标签准确率或专家一致率。

## Evaluation 缺口

论文没有给出：

- expert qualifications、annotation protocol 与 independence；
- majority rule、adjudication 或 disagreement handling；
- inter-rater agreement；
- confidence interval；
- knowledge 与 cognitive-type 的分项结果；
- error types 或 confusion matrix；
- manual、single-LLM、single-agent 或其他 baselines；
- seeds、runs 或 repeated sampling；
- held-out setup；
- 按 subject、grade、language、school 或 question type 的泛化；
- five-or-more agents 数量变化与 feedback/RAG ablations；
- manual time/cost 与 system time/cost。

100 题抽检只能提供有限的 preliminary evidence，不能支撑全量或跨域可靠性结论。

## 教育风险与治理边界

用于真实平台前需要处理短稿未说明的风险：

- auto-generated answer/explanation 的 hallucination 与教学错误；
- teacher-in-the-loop review、override 与 escalation；
- knowledge/cognitive labels 的 bias 与 cultural validity；
- 使用单校数据造成的 distribution shift；
- middle-school exercise data 的 authorization、privacy、retention 与 audit；
- 发送题目或相关内容到 external LLM APIs 的 disclosure 与 data controls；
- 错误 annotation 进入 student assessment 或 recommendation 后的错分、不公平路径和资源分配。

题库不一定包含学生个人数据，但论文没有交代数据内容与治理范围；不能据此假设不存在未成年人或学校数据风险。

## 资源、结论与页码核验

论文提供 [demonstration video](https://youtu.be/y3XLdWIuxNE)，但没有给出 code repository。

官方 PDF 物理页逐页核对：p. 4098 为 identity、Abstract、Introduction 起始与 Figure 1；p. 4099 为 Introduction continuation、Figure 2、Sections 2.1–2.6、Accuracy of Annotation 与 Conclusion；p. 4100 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EDGL6988.pdf) 核验；`reviewed` 不表示真实学生认知、学习效果、跨校泛化或 downstream assessment/recommendation safety 已经验证。
