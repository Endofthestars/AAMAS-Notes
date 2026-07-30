---
title: "MedCoScientist: A Multi-Agent LLM Framework for Clinical Decision Support"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "human_agent_interaction", "safety_verification", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/GDIW9780"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GDIW9780.pdf"
demo_url: "https://youtu.be/ezTswtNTbNA"
code_url: "https://github.com/ITMO-NSS-team/CoScientist/tree/main/MedCoScientist"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05x"
spark_draft_verdict: "source_grounded_with_required_case_scope_pilot_evidence_model_role_clinical_validation_and_governance_corrections"
spark_qa_verdict: "needs_revision_corrected_for_single_case_wording_four_subsystem_inconsistency_and_outperformance_evidence_boundary"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["rare_case_demonstration_not_clinical_validation", "small_qualitative_pilot", "sample_size_and_case_count_unreported", "ground_truth_and_expert_adjudication_unreported", "diagnostic_accuracy_sensitivity_specificity_unreported", "outperforming_and_more_reliable_author_claims", "patient_provenance_consent_and_deidentification_unreported", "mri_data_governance_and_access_control", "pubmed_retrieval_and_pico_accuracy_unvalidated", "citation_validity_and_guideline_freshness", "model_calibration_and_uncertainty_unreported", "automation_bias_and_clinician_overreliance", "multi_agent_error_propagation", "privacy_security_audit_and_liability_unreported", "clinical_outcome_and_external_validation_absent", "four_subsystems_enumeration_incomplete"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_clinical_evidence_ground_truth_patient_data_retrieval_citation_guideline_automation_bias_human_responsibility_security_audit_and_liability_check"
escalation_verdict: "escalate_for_evidence_and_governance_remediation_before_deployment_or_strong_performance_claims"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted clinical-safety and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# MedCoScientist: A Multi-Agent LLM Framework for Clinical Decision Support

## 一句话总结

MedCoScientist 把 MRI 解读、鉴别诊断、PubMed 检索和 PICO 抽取组织成 clinician-in-the-loop 多智能体流程，并以 pituitary apoplexy 作示范；论文只报告一个未注明样本规模和评分协议的定性 pilot，因此 “outperforming single LLMs” 与 “more reliable” 是作者主张，不构成临床诊断有效性或安全性证据。

## 资源与定位

论文提供 [演示视频](https://youtu.be/ezTswtNTbNA)、[MedCoScientist 代码目录](https://github.com/ITMO-NSS-team/CoScientist/tree/main/MedCoScientist) 和 [CoScientist 父项目](https://github.com/ITMO-NSS-team/CoScientist)。

系统定位为 clinical decision support，而非 autonomous diagnosis。作者明确表示它不输出应直接执行的“final answer”，最终诊断责任留给 physician。保留医生最终决定是必要边界，但论文没有研究医生是否会正确发现错误、产生 automation bias，或在时间压力下过度依赖系统。

## 演示任务

案例围绕罕见内分泌急症 pituitary apoplexy。输入包括 T1-weighted pituitary MRI 和简短病史；系统分类 DICOM modality、提取和解释影像 findings、形成并验证 differential diagnosis，再用关键词检索 PubMed。

论文称这是 demonstrative case study / representative scenario，但没有明确给出：

- 病例总数或是否严格为 \(n=1\)；
- 影像和病史来源；
- patient consent、ethics approval 或 de-identification；
- reference diagnosis、radiologist/endocrinologist annotation 或 adjudication；
- train/validation/test separation。

因此笔记记录“以一个疾病案例为示范”，不把它改写成患者队列、独立临床试验或外部验证。

## 控制与执行 agents

Control and orchestration agents 使用 `qwen3-235b-a22b`：

- **Chat Agent**：判断直接回答还是多步推理；
- **Planner Agent**：把 query 转成 ordered atomic steps；
- **Supervisor Agent**：顺序调用 domain agents、收集中间结果并处理 execution failures；
- **Re-planner Agent**：判断中间结果是否需要改计划；
- **Summary Agent**：聚合完成步骤，生成用户可见输出。

Domain-specific agents 包括：

- **Hypothesis PICO Agent**：同样由 `qwen3-235b-a22b` 驱动，把科学或临床 hypothesis 分解为 PICO；
- **Image Analyzer Agent**：使用 fine-tuned VLM Gemma 27B 与面向 endocrinology/cardiology 的 DICOM prompt；
- **PubMed Literature Agent**：使用 GPT-4o，检索、分类文献并抽取 PICO。

论文称系统有 “four tightly coupled subsystems”，但紧接着只枚举 data/state、control agents 和 domain-specific execution agents 三项。三页稿没有明确给出第四项；不能替作者补写。

## MRI 四阶段流程

Image Analyzer 的 chain-of-thought pipeline 分为：

1. **Classification**：识别 modality 与 acquisition/sequence；
2. **Finding Extraction**：总结 anatomical/pathological features、severity、confidence 与 artifacts；
3. **Interpretation**：映射 ICD codes，生成 differential、简短 report 和 prognosis；
4. **Validation**：对照 guidelines（例如 ACR），修订 differential，并生成 PubMed keywords。

“validation”在这里是系统流程节点。论文没有报告 guideline version、更新机制、规则覆盖、影像 ground truth、model calibration 或专家复核，因此不能把节点名称理解为临床验证已经完成。

## PubMed、study taxonomy 与 PICO

PubMed Agent 根据关键词或 hypotheses 获取 publications，把 metadata 存入 system state，并按 study type 分类：

- observational：prospective/retrospective 与 cross-sectional/cohort/case-control；
- experimental：clinical/in vivo/in vitro/in silico 及 randomized/non-randomized/propensity-score-matched；
- review：narrative/systematic/meta-analytic。

随后抽取 Population/Problem、Intervention、Comparison、Outcome。

论文没有测量 retrieval recall/precision、文章相关性 rubric、study-type classification accuracy、PICO extraction accuracy、重复/撤稿处理、citation-to-claim entailment 或 PubMed 更新时效。检索到文献不等于诊断已被 evidence grounding 验证。

## Small pilot

作者称运行了 small pilot，比较：

- **GPT-5.2**：给出正确 primary diagnosis，但 differential 有限；
- **Gemini-3-Flash**：也找到正确诊断，但 justification 很少；
- **DeepSeek-V3.2**：漏掉该诊断；
- 三者都抽取 PICO；GPT-5.2 返回最相关文献，Gemini 返回更多但较不相关，DeepSeek 返回较少且相关性有限。

正文没有给病例数、重复次数、prompt parity、model configuration、scoring rubric、blinding、clinician adjudication 或统计量。“correct”“most relevant”“limited”均是未给操作定义的定性判断。

MedCoScientist 本身没有在表格中报告同样的定量 score。结论称它在 accuracy 和 justification 上 outperform single LLMs，并因 Re-planner 更可靠；这些只能归属作者，不能从该 pilot 推出普遍或临床显著优势。

## 缺失的临床证据

本文未报告：

- sensitivity、specificity、accuracy、AUROC、calibration 或 confidence interval；
- radiologist/endocrinologist ground truth 与 inter-rater agreement；
- diagnostic delay、treatment choice、adverse event 或 patient outcome；
- multi-center、prospective、external 或 demographic subgroup validation；
- hallucination、wrong-citation、missed-guideline 或 tool-failure rate；
- agent ablation、single-LLM matched-budget baseline 或 failure propagation；
- clinician user study、trust calibration、override rate 或 time-to-decision；
- reproducible model snapshots、prompts、temperature、seed 与 inference cost。

Future Work 计划扩大实验、加入更多 comparable systems 和 expert clinician evaluation，反向说明这些证据尚未在本稿中完成。

## 临床治理与安全

MRI、病史与检索状态可能含敏感健康数据。论文没有说明数据最小化、encryption、access control、retention、audit log、cross-agent isolation 或 incident response。

其他高风险点包括：

- MRI artifact、domain shift 或 rare-case prior 造成错误 diagnosis；
- 上游 Image Agent 错误被 Planner、PubMed keywords 和 Summary 逐级放大；
- incorrect ICD mapping 或 outdated guideline 形成虚假验证感；
- retrieved paper 与患者不匹配，或 citation 不支持生成 claim；
- physician 因多 agent、trace 或“validated”标签产生 automation bias；
- 最终责任留给医生，却未定义 vendor、developer、institution 与 clinician 的 liability；
- external model/API update 改变输出而无版本审计。

高风险等级来自临床影响与评估、隐私和责任证据缺口，不表示当前演示已用于真实患者决策或已造成伤害。

## 页码核验

- p. 4134：身份、临床动机、pituitary-apoplexy case、资源和 pipeline 起点；
- p. 4135：study taxonomy/PICO、agents、模型归属、四阶段影像流程、small pilot、结论与 Future Work；
- p. 4136：致谢和参考文献，没有新增临床评估。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GDIW9780.pdf) 核验；`reviewed` 不表示诊断 accuracy、clinical reliability、patient safety、guideline validity、citation correctness 或部署合规已经验证。
