---
title: "SpeakerAICoach: A Multi-Agent Mobile Presenter Training"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["human_agent_interaction", "agent_engineering", "safety_verification", "generative_agents", "applications"]
dblp_key: ""
doi: "10.65109/QBWH4657"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QBWH4657.pdf"
code_url: "https://github.com/av-savchenko/Speaker-Trainer"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05o"
spark_draft_verdict: "source_grounded_with_whisper_ethnicity_category_on_device_and_claim_overreach"
spark_qa_verdict: "needs_revision_corrected_for_asr_demographic_category_onnx_coaching_evidence_privacy_fairness_and_identifier_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["recorded_video_and_audio", "server_side_biometric_processing", "age_gender_and_ethnicity_inference", "clothing_gaze_and_emotion_inference", "sensitive_attributes_in_personalized_llm_prompt", "consent_notice_retention_access_and_deletion_unreported", "category_schema_and_subgroup_metrics_missing", "demographic_bias_and_stereotype_amplification", "multi_agent_error_propagation", "coaching_effectiveness_not_evaluated", "cultural_validity_not_evaluated", "mobile_latency_energy_and_reliability_missing", "onnx_not_on_device_proof", "printed_doi_url_malformed"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_multimodal_pipeline_demographic_benchmark_sensitive_attribute_personalization_privacy_fairness_coaching_and_identifier_check"
escalation_verdict: "needs_revision_corrected_for_asr_ethnicity_category_demographic_prompt_privacy_fairness_coaching_mobile_and_doi_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted sensitive-attribute, fairness, and coaching-evidence check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# SpeakerAICoach: A Multi-Agent Mobile Presenter Training

## 一句话总结

SpeakerAICoach 把 recorded presentation 切成 1–2 秒 fragments，由 server-side speech/vision agents 并行标注，再由 aggregation 与 LLM agent 生成 Android timeline coaching；论文只评估了 age/gender/ethnicity models，没有证明 coaching 能提升技能、跨文化有效或敏感属性个性化公平安全。

## 系统边界

用户通过 Android client 录制 presentation；analytical agents 在 server side 立即并行处理，结果再回到 mobile interface（pp. 4083–4084）。摘要所说 “on-device clients with server-side inference” 指移动客户端体验，不代表 models 在手机本地运行。

系统把 media 切成 1–2 second fragments。各 agent 把 timestamped annotations 写入 shared fragment timeline，间接协作；modality isolation 使 individual model 可以替换。

论文提供 [source code](https://github.com/av-savchenko/Speaker-Trainer) 和 [demo video](https://youtu.be/zKpVFS8b7d8)。

## Audio 与 speech agents

audio/speech pipeline 包括（p. 4084）：

- **Noisereduce**：减少 environmental noise；
- **STOI**：计算 speech-intelligibility quality indicator；
- **ASR agent**：生成 word-level timing，用于 filler-word count 和 speaking rate；
- **Aniemore**：做 speech-emotion recognition，输出 soft confidence，再与 facial affect 融合。

论文引用“ASR models such as Whisper”已显示跨 accents/noise 的 generalization，这是背景文献说明；正文没有明确说 SpeakerAICoach 实际部署 Whisper。

## Vision agents

视觉侧包括：

- pose/gesture agent：跟踪 body keypoints，计算 amplitude、speed、repetitiveness；
- appearance agent：使用 ResNet-34 与 DeepFashion 分析 clothing/style；
- facial-affect agent：使用 EmotiEffLib models；
- demographic agents：估计 age、gender 和 ethnicity。

摘要还把 gaze 列为分析 cue。三页稿没有给每个 cue 的 exact training/evaluation、failure threshold 或 cross-modal fusion calibration。

## Demographic model training

作者训练 EfficientNet-B0 与 MobileFaceNet（p. 4084）：

1. 以 VGGFace2-pretrained models 为起点；
2. 在 LAGENDA 上 fine-tune simultaneous age/gender prediction；
3. multi-task loss 为 weighted cross-entropy age term 与 gender cross-entropy 之和；
4. 在 UTKFace official test set 报告 Table 1。

论文比较 argmax/direct age prediction 与 age-class posterior 的 expected value（EV）。

## Table 1：age/gender 结果

| Model | Gender accuracy | Age MAE Argmax/direct | Age MAE EV |
|---|---:|---:|---:|
| DEX | 91.05% | 6.48 | — |
| ResNet-50（InsightFace） | 87.52% | 8.57 | — |
| MobileNet-v1 | 90.09% | 7.07 | — |
| MiVOLO | 92.04% | 5.55 | — |
| ResNet50, CLAP2016 | — | 5.44 | — |
| MobileFaceNet（Ours） | 94.25% | 5.39 | 5.24 |
| EfficientNet-B0（Ours） | 94.65% | 5.53 | 4.96 |

这些是 demographic prediction metrics，不是 presentation quality、recommendation usefulness 或 learning outcome。

正文称模型 state-of-the-art/lightweight，但没有统一 training protocol、runtime、model size、confidence interval 或 subgroup analysis；Table 1 不能单独证明所有 comparators 上的公平 head-to-head superiority。

## Ethnicity classifier

作者在 age/gender models 的 facial embeddings 上训练 linear SVM，使用 UTKFace ethnicity data，并报告（p. 4084）：

- test accuracy：85.43%；
- recall：77.7%。

论文使用术语 **ethnicity**，没有把它定义为 race 或 skin color。正文未披露：

- category definitions；
- train/test split；
- recall averaging；
- per-category precision/recall；
- intersectional results；
- uncertainty 或 calibration。

因此不能把总体数字解释为各群体上同等可靠，也不能擅自补写 binary category schema。

## Aggregation、LLM 与 mobile interaction

aggregation agent：

- 沿 timeline 对齐 fragment annotations；
- normalize scores；
- 计算 average engagement、behavior consistency 等 high-level metrics。

feedback LLM 读取 structured summaries 而不是 raw signals，生成 coaching suggestions。作者称这 “preserves interpretability”，但没有 explanation-quality 或 user-comprehension study。

Android interface 显示 processing progress、color-coded multimodal timeline；用户可 scrub timeline、回放 fragment，并查看 aligned speech/gesture scores 与 contextual evidence（p. 4084）。

demographic models 转为 ONNX 以改善 CPU inference speed。论文没有 latency、energy、memory、model-size 或 phone benchmark，所以不能由 ONNX 推出完整 on-device inference 或 mobile efficiency。

## Sensitive-attribute personalization

系统把 estimated age、gender、ethnicity 与 visual/acoustic patterns 用于 personalized LLM prompt。作者还说用户可选择适合 cultural context 的 LLM，并宣称 framework 适用于所有年龄、职业和 skill levels（p. 4084）。

三页稿没有验证：

- demographic attributes 对 coaching 是否必要；
- 去掉这些 attributes 的 non-sensitive alternative；
- 属性误判怎样改变 recommendation；
- subgroup recommendation quality 或 disparate harm；
- stereotypes 是否进入 feedback；
- model/LLM change 是否真的带来 cultural validity。

这些只能视为设计与适用性主张。

## Privacy、公平与治理缺口

系统处理 recorded video/audio、face、voice、gaze、gesture、clothing、emotion 与 demographic attributes，并把客户端内容交给 server-side agents。论文没有说明：

- informed consent 与明确用途告知；
- data minimization；
- encryption in transit/at rest；
- storage location、retention period、access control；
- withdrawal、deletion、export 或 audit；
- de-identification 或 biometric template protection；
- age/minor policy；
- fairness testing、human appeal 或 override。

错误可以沿 perception agent → aggregation → demographic-personalized prompt → LLM recommendation 传播。将 noisy ethnicity/gender/age inference 用于 presentation coaching 可能产生 stereotyping、misgendering、文化刻板印象或不相关建议；论文没有 error-propagation 或 harm evaluation。

## Full coaching evidence 缺口

论文没有评估：

- presentation skill improvement 或 learning gain；
- recommendation factual/ pedagogical correctness；
- coach/expert agreement；
- user trust、usability、acceptance 或 adverse feedback；
- cultural/linguistic validity；
- end-to-end latency、energy、reliability、failure recovery；
- ASR/emotion/gesture/clothing/facial errors 在真实用户上的组合影响。

因此 Android demo 证明的是 pipeline 与 interface showcase，不是 coaching effectiveness。

## DOI identifier 说明

PDF 的 ACM reference/footer 把 DOI URL 错印成：

`https://doi.org/10.65109/http://doi.org/10.65109/QBWH4657`

其中重复嵌套了 DOI resolver。本文记录使用与 official paper ID suffix 对应的 intended canonical DOI：`10.65109/QBWH4657`，并保留这一印刷异常说明，避免把 malformed URL 当成不同 identifier。

## 页码与核验说明

PDF 逐页核对：p. 4083 为 identity、Abstract、Introduction、architecture、system start 与 code/video；p. 4084 为 complete agents、model training、Table 1、ethnicity results、aggregation/LLM、mobile demo 与 Conclusion；p. 4085 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QBWH4657.pdf) 核对 pipeline、Table 1、ethnicity metrics 与 DOI anomaly；`reviewed` 不表示 coaching effectiveness、cross-cultural validity、demographic fairness、privacy governance 或 mobile performance 已经验证。
