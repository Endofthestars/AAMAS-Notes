---
title: "An Open-Source Framework for Closed-Loop Multi-UAV Planning and Execution"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["planning_scheduling", "agent_engineering", "robotics_embodied", "human_agent_interaction", "safety_verification", "generative_agents", "marl_coordination", "applications"]
dblp_key: ""
doi: "10.65109/QTXJ5819"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QTXJ5819.pdf"
demo_url: "https://youtu.be/Ml4c3v8C8X4"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06e"
spark_draft_verdict: "hil_system_demonstration_without_quantitative_or_certification_evidence"
spark_qa_verdict: "needs_revision_preserve_real_hardware_evidence_open_source_url_gap_and_unreported_sar_safety_metrics"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["open_source_claim_without_repository_url_in_paper", "three_uav_hil_demonstration_without_quantitative_results", "no_runs_success_failure_or_mission_duration", "no_baseline_ablation_or_statistics", "natural_language_mission_goal_input", "llm_modulo_planner_without_model_prompt_or_safety_evaluation", "sensor_detection_accuracy_and_knowledge_freshness_unreported", "replanning_latency_concurrency_and_failure_unreported", "ros2_4g_vpn_rtsp_security_and_reliability_unreported", "geofence_collision_airspace_fail_safe_and_override_unreported", "video_location_and_missing_person_privacy_unreported", "hil_demo_not_certified_autonomous_sar"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_real_hardware_hil_scope_natural_language_and_llm_planning_sensor_replanning_network_flight_safety_override_privacy_and_certification_boundary_check"
escalation_verdict: "insufficient_certification_evidence"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted HIL, flight-safety, and SAR deployment-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# An Open-Source Framework for Closed-Loop Multi-UAV Planning and Execution

## 一句话总结

AUSPEX 用 PLAN、EXEC、KNOW、SENS、AERO 与 AUGUR 在 ROS 2 上形成 heterogeneous multi-UAV planning–execution–feedback–replanning loop，并以三架真实 UAV hardware、4G/VPN/RTSP 链路演示 missing-person search、replanning 和 first-aid delivery；三页稿没有任何成功率、时延、感知、通信或飞行安全指标，所以这是有真实 hardware-in-the-loop 证据的 system demonstration，不是认证级自主 SAR deployment。

## 资源与开源边界

论文提供 [HIL 演示视频](https://youtu.be/Ml4c3v8C8X4)，并把 AUSPEX 称为 open-source framework，但三页 PDF 没有给出 source repository URL、release、commit 或安装说明。笔记不从相关文献或网络自行补仓库，也不把 “open-source” 改写成当前论文已提供完整 reproduction package。

## Closed-loop architecture

- **AUSPEX-PLAN**：根据 mission goals、current knowledge 与 constraints 为每架 UAV 生成 action sequence。公开实现列出 Unified Planning、Adaptive Large Neighborhood Search（ALNS）和 Say’n’Fly LLM-modulo planner，但每种 planner 都需要 adaptation。
- **AUSPEX-EXEC**：实时向 UAV 下发 planned actions，接收 feedback，并把需要 replanning 的状态送回系统。
- **AUSPEX-KNOW**：维护按需更新的 static mission parameters，以及持续流入的 telemetry/dynamic knowledge；PLAN 查询它来构建 current planning problem。
- **AUSPEX-AERO**：把 EXEC task 翻译为 flight-controller commands。通常部署在 airborne companion computer；若 off-board，则要求稳定 connection。
- **AUSPEX-SENS**：处理 continuous sensor streams，例如 object detection，并把 inferred information 写入 KNOW；可 onboard 或 off-board。
- **AUGUR**：human–machine interface，用于 mission control、supervision 和 mission definition，也支持 natural-language mission goals。

模块通过 ROS 2 backbone 通信。闭环可以概括为：

\[
\text{KNOW}\rightarrow\text{PLAN}\rightarrow\text{EXEC}\rightarrow
\text{AERO/UAV \& SENS}\rightarrow\text{feedback/KNOW}\rightarrow\text{replan}.
\]

架构提供集成点，但论文没有报告 planner arbitration、feedback consistency、stale knowledge detection、concurrent replanning 或 safe plan handover。

## HIL hardware 与任务

Real-World HIL-Validation 使用三架 heterogeneous UAV：

- 2 × Holybro X500v2：Pixhawk 6C、PX4 Autopilot、Raspberry Pi 5 offboard controller；
- 1 × Multikopter MK-U20：Cube Orange+、ArduPilot、Nvidia Jetson Xavier NX companion computer。

每架 UAV 通过 4G USB surf stick 接入 cellular network，经 VPN 连接 Ground Control Station（GCS）和 AUSPEX ROS 2 backbone；video stream 用 RTSP 传到 GCS。PLAN、EXEC、KNOW、SENS 部署在 GCS。

SAR demonstration 中，camera UAVs 先搜索 missing-person target；识别后触发 replanning；携带 first-aid kit 的 UAV 起飞并投送到目标附近；mission goals 完成后全部 return home。AUGUR 用于下达和监控任务。

论文还称 AUSPEX 可连接 third-party environments 做 SIL，例如基于 Unreal Engine 的 photorealistic Dynamic REAP。

## HIL 证据能说明什么

正文支持以下有限陈述：

- system integration 覆盖三种真实 flight-controller/companion-computer combinations；
- closed-loop command、telemetry、video 和 replanning path 在 HIL demonstration 中被走通；
- heterogeneous payload 分工和 target-triggered replanning 有具体场景。

正文没有报告：

- site、weather、obstacles、airspace 或 flight duration；
- runs、mission success/failure、abort 或 manual intervention；
- planner/replanning latency、plan validity 与 task completion time；
- object-detection precision/recall、false alarm/missed target；
- delivery position error、minimum separation、collision/near miss；
- 4G/ROS 2 packet loss、latency、disconnect/reconnect；
- energy use、vehicle failure 或 worst-case recovery；
- baseline、planner comparison、ablation、variance 或 statistics。

因此 “validated”与 “applicable to SAR”应限定为论文所述 HIL/SIL demonstration context。真实 hardware 参与不等于 fielded autonomous operation、regulatory approval、reliability qualification 或 safety certification。

## Planning、flight 与 cyber governance

高风险闭环未报告的控制包括：

- natural-language goal parsing、prompt/command injection、ambiguity rejection；
- Say’n’Fly model/version/prompt、LLM output validation 与 planner fallback；
- telemetry/sensor freshness、conflict resolution、false-detection handling；
- replanning trigger、race/oscillation prevention、in-flight plan transition；
- independent geofence、collision/separation、airspace/altitude constraints；
- lost-link return-to-home、safe landing、emergency stop、human override；
- ROS 2 identity/access、VPN keys、4G threat model、RTSP confidentiality；
- command authorization、secret rotation、tamper-evident logs 与 provenance；
- video/location/missing-person consent、access、retention 与 deletion。

这些是未报告的 safeguards，不是已发生事故、攻击或隐私泄露的证据。高风险来自真实 flying hardware 与 SAR 场景中错误 command/knowledge 的潜在后果。

## 页码核验

- p. 4176：题名、作者、摘要、引言、architecture 与 PLAN/EXEC/KNOW；
- p. 4177：architecture 图、AERO/SENS/AUGUR、HIL hardware/network/mission、SIL 和结论；
- p. 4178：致谢与参考文献，没有新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QTXJ5819.pdf) 核验；`reviewed` 不表示 source release、quantitative reliability、flight safety、cyber/privacy governance 或 autonomous SAR certification 已得到验证。
