---
title: "AIDERS: An Integrated Multi-UAV Platform for Disaster Management"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["agent_engineering", "robotics_embodied", "marl_coordination", "planning_scheduling", "human_agent_interaction", "safety_verification", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/PBBJ5387"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PBBJ5387.pdf"
code_url: "https://github.com/KIOS-Research/AIDERS"
demo_url: "https://www.youtube.com/watch?v=u2TRXvnYEiA"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06f"
spark_draft_verdict: "platform_description_requires_quantitative_operational_safety_and_privacy_boundaries"
spark_qa_verdict: "needs_revision_downgrade_performance_claims_separate_pdf_annotation_resources_and_preserve_unreported_controls"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_page_system_demo_without_quantitative_results", "real_time_and_high_precision_author_claims_without_metrics", "no_dataset_baseline_ablation_runs_variance_or_seeds", "no_real_disaster_deployment_or_first_responder_study", "people_localization_and_live_video_privacy_unreported", "unique_uav_identifier_not_authentication_evidence", "dji_mavlink_websocket_rtmp_nginx_security_unreported", "telemetry_freshness_network_reliability_and_reconnect_unreported", "false_positive_false_negative_and_model_uncertainty_unreported", "camera_footprint_and_fire_prediction_accuracy_unreported", "mission_conflict_collision_geofence_airspace_lost_link_unreported", "fail_safe_human_override_logs_provenance_and_rollback_unreported", "simulation_and_containerization_not_operational_certification"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_emergency_uav_operational_safety_people_localization_video_privacy_communications_security_telemetry_uncertainty_fail_safe_override_and_certification_boundary_check"
escalation_verdict: "insufficient_quantitative_operational_safety_security_and_privacy_evidence"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted UAV-safety, communications-security, privacy, and deployment-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# AIDERS: An Integrated Multi-UAV Platform for Disaster Management

## 一句话总结

AIDERS 把 DJI/MAVLink UAV 接入、地图化任务规划、遥测与直播、多机网格任务，以及人员、灾害、火势和建图算法组合成 Web-based 灾害管理平台；三页展示稿没有报告任何数据集、精度、时延、网络可靠性、扩展性或真实灾害部署结果。因此它提供的是系统组成与功能演示，不是 “real-time”“high-precision”、运行安全或救援成效的定量验证。

## 资源与链接核验

PDF annotations 给出 [AIDERS 代码仓库](https://github.com/KIOS-Research/AIDERS) 与 [演示视频](https://www.youtube.com/watch?v=u2TRXvnYEiA)。正文文本抽取只显示 `https://code` 和 `https://aiders` 两个占位形式；本笔记没有把它们当成真实 URL，也没有根据仓库或视频补写论文正文未报告的评测结果。

## 平台与通信架构

AIDERS 面向 real-world and simulated UAV operations。平台通过 AIDERS Android mobile app 接入 DJI UAV，也声称支持 MAVLink-compatible UAV。NGINX 处理用户请求和 WebSocket connections；MySQL 用于持久化；offline map server 支持无互联网地图；Docker 提供模块化 container deployment；centralized system launcher 用于启动和停止服务。

Table 1 的技术栈为：

| 层 | 论文列出的技术 |
|---|---|
| Front-end | HTML、CSS、JavaScript |
| Back-end | Python-based Django、Go |
| Database | MySQL |
| Mobile Application | Android、DJI Mobile SDK |
| Computer Vision | Python-based models |

Android app 先通过 DJI Mobile SDK 完成论文所称的 authorization，随后使用 unique UAV identifier 建立 WebSocket connection，并以 RTMP 传输 live stream。这里的 identifier 只是连接标识；论文没有给出证据表明它构成强身份认证，也没有披露 DJI/MAVLink/WebSocket/RTMP/NGINX 的端到端鉴权、加密、密钥或权限配置。

## Dashboard、任务与算法

- Dashboard 用地图集中展示 UAV telemetry、mission planning 和 live-video capture；camera footprint 按 position、altitude、heading 与 gimbal angle 计算和可视化。
- Flight planning 支持 point-to-point missions 与 multi-agent grid missions，并允许配置参数和算法；mobile/IoT telemetry 与 images 也可进入可视化界面。
- HRNet segmentation 用于作者所述的 crowd localization/object detection，EfficientNetB0 用于 disaster classification，WALDO 用于作者称为 high-precision 的 object identification；平台还描述 simultaneous crowd localization and disaster classification。
- 其他集成功能包括 predictive fire-spread modeling、real-time mosaic mapping，以及 offline orthophoto 与 3D-model generation。

这些项目证明论文描述了相应接口和功能，不证明 camera footprint 是真实覆盖保证，也不证明人员识别、火势预测或地图产品达到可用于自动应急决策的精度。

## 评测证据边界

论文没有实验/结果表，也没有报告：

- task dataset、采集规模、标注、训练/测试划分或 model version；
- detection/classification precision、recall、F1、false alarm 或 missed detection；
- crowd/target localization error、fire-spread accuracy、mosaic/orthophoto/3D quality；
- latency、throughput、live-stream delay 或 end-to-end response time；
- UAV 数量扩展曲线、network bandwidth、packet loss、reconnect 或 reliability；
- real disaster deployment、mission success/failure、first-responder study 或 user study；
- baseline、ablation、runs、variance、confidence interval 或 random seeds。

因此 “real-time”“high-precision”“seamless”“scalability”“reliable performance”是作者/设计表述；“robust simulation”指作者称可在 virtual environments 中测试，并不构成已公开的可复现实验、安全认证或 operational disaster-response validation。“save lives”是应用愿景，不是本文测得的 outcome。

## 应急、飞行与数据治理

三页稿未报告以下 safeguards：

- stale telemetry detection、clock/time consistency、network degradation 和 reconnect handling；
- false-positive/false-negative threshold、uncertainty reporting、human confirmation 与 escalation；
- camera-footprint error 和 fire-model uncertainty；
- multi-UAV mission conflict、collision/minimum separation、geofence、airspace/altitude constraints；
- lost-link behavior、return/land policy、fail-safe、emergency stop 与 human override；
- command authorization、transport encryption、secret/key rotation、access audit；
- tamper-evident logs、data/model provenance、version pinning 和 rollback；
- live video、faces/locations/people detection 的 consent、purpose limitation、access、retention 和 deletion；
- Docker/network isolation、tenant/resource controls 和 incident response。

这些是当前三页论文没有披露的控制，不是已经发生碰撞、攻击、误判或隐私事件的证据。人员定位和直播属于高影响信息源，不能仅凭平台可视化直接触发救援或执法行动；真实部署仍需独立飞行约束、数据治理与人工确认。

## 页码核验

- p. 4182：题名、作者、摘要、引言与 platform design 开始；
- p. 4183：Table 1、mobile app、dashboard、flight planning、integrated algorithms 与结论；
- p. 4184：致谢与参考文献，没有新增定量实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PBBJ5387.pdf) 核验；`reviewed` 不表示算法性能、通信安全、隐私合规、飞行安全、真实救援效果或运行认证已经得到验证。
