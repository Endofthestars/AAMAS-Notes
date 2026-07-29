---
title: "A Multimodal AI Approach for Predicting Personal Privacy Preferences in Photo Sharing"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "human_agent_interaction", "generative_agents"]
dblp_key: ""
doi: "10.65109/QNBC3731"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/QNBC3731.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03e"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "privacy_sensitive_data", "small_personal_history", "survey_dataset", "not_consent_mechanism"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Multimodal AI Approach for Predicting Personal Privacy Preferences in Photo Sharing

## 一句话总结

PPF-H 以 privacy statements、少量历史 decisions与共识 rule base 构建个人 profile，规则匹配失败时由 Qwen-2.5-VL 32B 推理新照片/情境的 comfort。486 位参与者、每人 16 个情境的 leave-one-out 中 PPF-H-D accuracy 为 0.8445、F1 .6663；预测不能替代照片中人的明确同意、撤回权或平台隐私义务。

## 方法与证据

- 第一阶段抽 factor/偏好、采样历史案例形成经 \(\tau\) 一致性验证的 rules，结合 consensus rules；第二阶段按情境 factors 触发 rule，否则 MLLM 预测（§3）。
- 评估有 scene-only、statement/history personalization 与 hybrid；\(k=6,\tau=2,n=6\)，Table 1 给出各项 metrics及 per-user correct counts（§4）。
- 自述与实际选择不一致、个人差异和视觉内容重要是分析结论；数据集/任务为二元 comfort 分类，未测试真实分享、跨文化/时间漂移、攻击或 consent outcomes（§2--5）。

## 适用边界与复现

- 用作可解释的 privacy-support suggestion，而非自动发布准许。应最小化照片/脸部数据、取得当事人同意、默认保护、允许纠错/拒绝与人工复核。
- 复现须保护原始数据，公开匿名化 split、factor schema、prompts/model、rule validation与 threshold；分报告 false-positive（错误暴露）风险、群体差异和校准。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/QNBC3731.pdf) 人工核对框架、486×16 leave-one-out 与 Table 1；未把预测准确率写成同意或合规证明。
