---
title: "PROTECDOME: PROTECtion DOME for Public Spaces against Rogue Drones"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["safety_verification", "robotics_embodied", "agent_engineering", "marl_coordination", "human_agent_interaction", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/RXLH8860"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RXLH8860.pdf"
demo_url: "https://www.youtube.com/watch?v=uSw1n0784d8"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06f"
spark_draft_verdict: "multimodal_counter_uas_design_requires_quantitative_active_radar_and_detection_only_boundaries"
spark_qa_verdict: "needs_revision_reconcile_unquantified_outdoor_evaluation_active_radar_future_status_and_security_layer_description"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_page_demo_without_quantitative_results", "extensive_outdoor_evaluation_claim_without_reported_metrics", "false_positive_reduction_and_robustness_design_claims", "active_radar_incorporation_described_as_current_work", "current_demo_limited_to_rf_acoustic_vision_detection_tracking_localization", "no_jamming_capture_neutralization_or_autonomous_force", "legal_and_innocent_drone_false_positive_governance_unreported", "lea_human_confirmation_authority_and_rules_of_engagement_unreported", "public_space_camera_acoustic_rf_privacy_unreported", "data_retention_access_and_purpose_limitation_unreported", "security_layer_architecture_not_validated_controls", "key_management_audit_and_security_testing_unreported", "spoofing_jamming_evasion_poisoning_unreported", "environment_failure_and_multi_target_uncertainty_unreported", "spectrum_interference_and_compliance_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_public_surveillance_false_positive_lea_authority_detection_only_active_radar_security_privacy_spectrum_adversarial_and_multi_target_uncertainty_boundary_check"
escalation_verdict: "insufficient_quantitative_security_governance_and_active_radar_integration_evidence"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted public-surveillance, LEA, detection-only, active-radar, and security-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# PROTECDOME: PROTECtion DOME for Public Spaces against Rogue Drones

## 一句话总结

PROTECDOME 将 camera、acoustic array 与 RF sensing 的单模态输出融合，在 Web platform 中展示 rogue-drone detection、tracking、localization、alerting 与 situational awareness；摘要称系统经过 extensive real-world outdoor evaluation，但三页论文没有提供任何 detection rate、false-alarm rate、range、error 或 latency。公开证据支持的是指定区域内 RF/acoustic/vision 演示，不支持有源雷达已完成集成，也不包含 jamming、capture、neutralization 或 autonomous use of force。

## 目标与多模态流程

论文列出四项目标：

1. 早期、实时 detection、tracking 与 classification；
2. 通过 evidence-based toolkit 做 public-space risk quantification 与 vulnerability analysis；
3. 建立集 detection、tracking、alerting、situational awareness 于一体的 CUAS，以 multimodal sensor fusion 支持 single/multiple-target tracking；
4. 提升 law-enforcement agencies（LEAs）的长期 CUAS capacity。

核心模态为 camera、acoustic array 和 RF sensors，RF 描述同时提及 active/passive radars；论文也列出 DVB-T、UMTS、4G/5G 等 signals of opportunity。每个 modality 先做 unimodal detection，并在可行时给出 localization；输出进入 multimodal system，单模态与融合结果再由专用 Web platform 可视化。

## 七层架构

1. **Physical topology**：硬件与网络结构；
2. **Information collection and transfer**：采集各 detection subsystem 数据，并按作者描述 “securely” 传往 ground control；
3. **Unimodal functionality**：分别定义各 modality 的能力与输出；
4. **Multimodal system**：融合不同 modality，目标是提高 detection accuracy/robustness 并减少 false positives；
5. **Platform/UI**：管理、可视化与解释 CUAS data；
6. **Storage/data management**：存储、索引、检索及敏感信息保护；
7. **Security**：secure channels、encryption、authentication 与 access control。

七层是 architecture description。论文没有给出协议、密码算法、key lifecycle、access policy、audit trail、penetration test 或 adversarial evaluation，因而不能把 “securely”、Layer 6/7 或 “resilient end-to-end defense”写成已实现且有效的控制。

## Demo 与 active-radar 边界

结论称系统在 designated area 中利用 RF、acoustic 与 vision data 演示 rogue-drone detection、tracking 与 localization，并提供 [演示视频](https://www.youtube.com/watch?v=uSw1n0784d8)。虽然 architecture 段把 RF sensors 写成 active and passive radars，结论却明确把 incorporation of the active radar component 作为 current work。基于这三页来源，最稳妥结论是：有源雷达属于正在纳入/后续扩展项，不能写成当前 demo 已集成或已验证的能力。

论文描述的操作边界是 detection、tracking、localization、classification、alerting 与 situational awareness；没有描述 jamming、spoofing takeover、capture、interception、neutralization 或 autonomous use of force。`counter-UAS` 名称不能用来补出这些未报告能力。

## “户外评估”与证据缺口

摘要称 software/hardware implementation “extensively evaluated in real-world outdoor experiments”，但正文没有结果表或数字，也没有报告：

- precision、recall、ROC/AUC、F1、false-positive/false-alarm rate；
- detection range、coverage、localization/tracking error 或 latency；
- weather、light、terrain、RF/noise、occlusion 或 crowd conditions；
- target drone types、size、speed、altitude、合法/恶意构成或 single/multi-target counts；
- unimodal-versus-fusion baseline、ablation 或 modality-failure test；
- runs、variance、confidence interval、failure cases 或 independent replication；
- sensor/hardware specification、compute、bandwidth、packet loss 或 communication performance；
- spoofing、jamming、evasion、sensor poisoning 或 cyber testing；
- deployment/maintenance cost、LEA operator study 或 decision outcome。

因此 “improving robustness/reliability”“reduce false positives”与 “resilient end-to-end defense”是目标/设计主张，不是本文提供的量化结论；“real-time”也没有 latency measurement 支撑。

## 公共空间、LEA 与安全治理

三页稿未报告：

- 对 innocent/legal drones 的 false-positive handling、人工复核和纠错；
- classification criteria、legal authority、rules of engagement、LEA human confirmation 和责任链；
- camera、acoustic 与 RF sensing 对旁观者/合法使用者的 privacy 与 civil-liberties impact；
- data purpose limitation、minimization、retention、deletion、access 和 secondary use；
- spectrum authorization、signals-of-opportunity 合规与 interference impact；
- authentication implementation、encryption suite、key management、secret rotation 和 security audit；
- 对 spoofing、jamming、evasion、poisoning、sensor compromise 的检测与恢复；
- noise、occlusion、crowds、weather 和 modality outage 下的 fail-safe；
- multi-target association、identity handoff、uncertainty/calibration 和 conflicting-sensor resolution。

这些是论文未披露的治理与验证项，不是已经发生误捕、非法监控、干扰或安全事件的证据。系统输出在高影响 LEA 场景中应保留不确定性、来源和人工确认，不能把 classifier label 自动当作合法处置依据。

## 页码核验

- p. 4185：题名、作者、摘要、引言、四项目标与 sensor motivation；
- p. 4186：系统 proposal、figures、七层架构、结论、demo 与 active-radar current work；
- p. 4187：致谢与参考文献，没有新增评测结果。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RXLH8860.pdf) 核验；`reviewed` 不表示户外性能、误报控制、有源雷达集成、安全层有效性、LEA 合规、隐私治理或任何 mitigation capability 已得到验证。
