---
title: "An ML-BDI Reasoner to Support Crime Investigation in Digital Forensics"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "norms_trust_governance", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/ZGRS2204"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZGRS2204.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "forensic_decision_support_only", "synthetic_sensor_degradation", "occupancy_inference_scope", "legal_admissibility_not_established"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# An ML-BDI Reasoner to Support Crime Investigation in Digital Forensics

## 一句话总结

本文提出 ML‑BDI reasoner，用 Random Forest 从 smart-building IoT traces 推断 room occupancy，并在 sensor 退化/低 confidence 时由 Jason BDI agent 选择显式 symbolic fallback plan 或 abstain，同时记录 plan id、timestamp、RF confidence 与 sensor state 以便审查。模拟退化实验中 BDI 常修正 RF 错误，但该系统仅支持特定占用推断，不确定人身份、犯罪行为、意图或证据真实性，审计日志也不自动满足证据链、可采性或正当程序要求。

## 方法与证据

- 目标场景是 IoT smart environments 中由 sensor traces 重建“是否/多少人曾在房间”，承认设备故障、噪声、网络/firmware changes 和 anti-forensic disruption 使数据不完整或矛盾（§1）。论文并不解决 acquisition integrity、设备身份认证、clock synchronization、chain of custody、raw-data preservation、tamper detection、warrant/privacy、嫌疑人身份或行为归责。
- hybrid design 以 RF 做 occupancy perception，Jason/AgentSpeak(L) BDI 的 beliefs 含 sensor state 和 model confidence，plans 编码低可靠性时 sensor-only fallback/abstention等 conservative policies（§1）。可检查 plan 和日志增强可解释性，但 symbolic rules 的正确性、覆盖率、版本/维护、threshold和规则冲突都未在 extended abstract 中正式验证。
- data 80% train/20% test；test 逐步用 per-cell MCAR random erasure 与 time-windowed sensor outages 模拟 unavailable sensors（§3）。每 timestamp RF 输出 prediction/confidence，连同 degraded readings 输入 BDI；高 confidence accept RF，低 confidence symbolic inference（图 1）。MCAR/规则化 outage 并不代表真实攻击、选择性篡改、correlated failure、传感器 drift、房间布局变化或 adversarial spoofing。
- Table 1 给 10 个 seeds：BDI interactions 143–240，BDI correct 108–199、error 28–74，RF error 50–133，\(BDI\ Correct-RF\ Error\) +35 至 +101；作者总结平均约 210 interventions/run、约 75% resolved（§3）。这里的“correct”是相对该数据集 ground truth/退化条件，并非对独立案件的 truth；表未给总体 accuracy/precision/recall/FPR、abstention rate、confidence calibration、阈值、原始 dataset规模/来源、degradation levels、CI/显著性或与其他 imputation/robust ML/human investigator baselines 比较。
- 审计 trace 包含 plan id、timestamp、RF confidence、sensor state（abstract），有利于复核决策路径；但没有 cryptographic provenance、immutable logging、reproducible container/model hash、rule/model version、data transformations、access controls或 disclosure protocol。作者将来计划更多 datasets/sensing configs及 neuro-symbolic extension（§4），说明其取证适用性仍属初步。

## 适用边界与复现

- 适用于研究/内部 triage 中对明确授权的 IoT occupancy signal 做低风险线索排序，且将输出视作需要进一步调查的假设；不可单独用于搜查、拘留、起诉、定罪、保险/雇佣制裁或将室内 presence 推断为某个人/犯罪事实。
- 复现需公开合法可共享的 sensor dataset、room/sensor topology、occupancy labels与数据切分、RF features/hyperparameters/seed、confidence definition/threshold、MCAR/outage generator、所有 Jason beliefs/plans/tie-breaking/abstention、log schema及 per-seed raw predictions。需在不退化/每种退化强度下报告 overall/conditional performance、error severity、abstention与coverage，而不仅是 BDI Correct–RF Error。
- 应在真实设备故障、clock drift、packet loss、different buildings/sensors/occupancy patterns、unseen layout、data contamination和有控制的 spoofing/anti-forensics下独立测试；比较传统 forensic review、robust/imputation models、其他 symbolic policies，做 calibration/threshold/sensitivity与disparate impact analyses。第三方 red-team 与 blinded expert review 应评估错误解释是否会误导调查。
- 实际取证必须保留原始数据/hash、完整 collection chain、可复现 environment/model/rule/log versions、访问授权、专家方法说明和被影响方的 challenge/独立复核机制。任何 BDI fallback 或“高 confidence”都只是一项可质询的分析步骤，不能补足缺失证据或将概率结果变成法律事实。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 ML–symbolic BDI 与 IoT digital forensics extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZGRS2204.pdf) 核验 RF+Jason architecture、80/20 split、MCAR/outage degradation、confidence policies、日志字段和表 1 的 per-seed counts；没有将模拟 occupancy improvements 写成犯罪调查结论、身份识别、抗篡改、法庭可采性或自动执法保证。
