---
title: "Multimodal Emotion Recognition in Conversation via Large Language Models and Global-Local Cross-Domain Graphs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/HIXY4457"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HIXY4457.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "multimodal_emotion_recognition", "pseudo_labels", "conversation_benchmarks", "sensitive_inference", "not_mental_health_or_truth_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multimodal Emotion Recognition in Conversation via Large Language Models and Global-Local Cross-Domain Graphs

## 一句话总结

LLM-EmoGraph 为 multimodal emotion recognition in conversation 组合 multimodal masking、cross-domain multi-graph pretraining、dual-channel graph filtering 的 global/local feature fusion，以及 LLM-enhanced weakly supervised hierarchical classification。作者称其在两个 benchmarks 优于既有方法；扩展摘要未给完整数值表或训练细节。它预测的是数据集定义的 utterance emotion labels，不可被表述为读取人的真实内心、心理/医疗诊断、可信意图判断或对个体的自动决策依据。

## 方法与证据

- 输入为 text、speech、visual cues 和 conversation context，目标是 target utterance 的 label（Figure 1）。MELD 示例覆盖 Happy/Sad/Surprised/Fear/Angry；数据标签是任务构造与标注约定，受语境、文化、讽刺、缺失模态和 annotator disagreement 影响。
- architecture 的 multimodal masking 和 cross-domain multi-graph pretraining 用于让 representation 在不同 graph domains/modalities 间具有 uniformity/transferability；abstract 未定义 pretraining corpus、domain split、mask rates、graph topology、leakage controls或 transfer metric，故不能据此断言跨域泛化。
- adaptive dual-scale fusion 及 dual-channel graph filtering 分别捕捉 global emotional structure 与 local details；LLM-enhanced hierarchical classifier 以 weak supervision 改善 pseudo-label quality、缓解 fine-grained class scarcity（Figure 2, §1）。pseudo labels 的偏差会被层级/LLM 放大，且“LLM enhanced”未说明 model/version/prompt、calibration、abstention或 human validation。
- 作者只称在 two benchmark datasets 显著优于 existing methods，摘要未呈现数据集名之外的第二集、F1/accuracy、class-wise effects、CI/seeds、ablations、compute、privacy consent或错误案例。因此不能将“significant”扩展为统一 SOTA、实际对话稳健性或跨人群公平性。
- 论文动机包括 conversational AI、recommendation 与 medical diagnostics 的应用举例，但没有 clinical data/diagnosis validation、informed-consent/biometric governance、harm assessment或 deployment protocol。音视频情感推断本身可能涉及敏感个人数据与不当监控风险。

## 适用边界与复现

- 适合受控数据集上的 multimodal conversational label prediction 研究；不应用于雇佣、教育惩罚、保险、执法、医疗分诊、危机判断或隐蔽情绪监控。人机界面若展示结果，应明确不确定性、允许纠正/拒绝并避免将 label 归因成事实。
- 复现需公开两数据集及 splits、modal feature extractors/alignments、masking、cross-domain graphs/pretraining data、fusion/filter/hierarchy、LLM/version/prompt/pseudo-label pipeline、baselines/tuning budget、seeds/CI与 per-class metrics。还应报告 modality-missing、speaker/domain split、calibration、confusion and subgroup errors。
- 应测 language/culture/accent/appearance shift、sarcasm/ambiguous context、noise/missing video/audio、adversarial manipulation、consent withdrawal与 label disagreements。部署须最小化音视频收集、保护 biometric data、限制 retention/access，并有人类复核和申诉机制。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 multimodal conversational emotion-recognition 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HIXY4457.pdf) 核验 Figure 1 task、Figure 2 模块、weak supervision与“两基准优于”范围；没有把标签预测写成真实情绪、心理健康或敏感决策保证。
