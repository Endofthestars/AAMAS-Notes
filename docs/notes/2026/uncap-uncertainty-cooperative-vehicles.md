---
title: "UNCAP: Uncertainty-Guided Neurosymbolic Planning Using Natural Language Communication for Cooperative Autonomous Vehicles"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "safety_verification", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/WHRE3513"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WHRE3513.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["simulation_only", "closed_world_cav_scope", "vlm_planning_latency", "uncertainty_calibration_assumption", "communication_integrity_not_tested", "packet_loss_future_work", "no_formal_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# UNCAP: Uncertainty-Guided Neurosymbolic Planning Using Natural Language Communication for Cooperative Autonomous Vehicles

## 一句话总结

UNCAP 面向 cooperative connected autonomous vehicles（CAVs）：先以 BARE 广播低带宽状态，再以 SPARE 选择有安全相关性的邻车，传递带 quantifiable perception uncertainty 的文本消息；ego 只融合能降低不确定性、对 VLM plan 有正 pointwise mutual information（PMI）的对象。在 CARLA/OPV2V 仿真中，全文系统报告 80.3% driving score、33 KB/episode，较“广播所有文本、无选择/融合”方案 89 KB 降约 63%，并提高规划 confidence；但它没有处理真实网络、欺骗通信、混合人类交通或实体车，不能作为安全上路证明。

## 方法与证据

- 每辆车将 sensor observation 转为语义文本。BARE 先交换位置、速度等最小包；SPARE 以安全距离阈值（实验为 50 m）筛潜在协作者，再请求更详细 reasoning message。目标是在 bandwidth cost 与 \(I_p(o_j;\pi_i\mid o_i)\) 的安全阈值之间选择通信边（§3）。
- 低层 perception 用 YOLOv9；每 object 的 confidence 经 conformal calibration 转为 uncertainty \(u_p\)。两个视角融合采用最小 uncertainty，即选较不确定度低的 calibrated detection；只保留能降低 ego uncertainty 且 PMI 为正的对象（§3.4）。这是假设 calibrated confidence 与跨车 detection correspondence 在部署域仍成立。
- 高层 VLM plan uncertainty 定义为 \(u_d(o,\pi)=-\log p_{VLM}(\pi\mid o)\)，以邻车 observation 前后的 next-token likelihood ratio 计算 plan PMI；PMI \(\le0\) 的消息不参与最终融合（§3.5）。token likelihood 只是模型 confidence proxy，并非碰撞概率或形式化风险界。
- 评测使用 CARLA 上的 OPV2V：4 类布局（merge、intersection、urban occlusion 等），并在 appendix 扩至 9 个 OPV2V/custom scenarios，每场景 2--4 CAV；GPT-4o 为默认 VLM，perception/communication 10 Hz，所有方法共用 detection output 与 route（§4.1）。
- 主要指标：Driving Score（progress/rule compliance/comfort composite）、Route Completion、Infraction Penalty、total bandwidth、信息增益与 near-miss distance margin。它们是仿真 quality/safety proxy，不是 ISO/SOTIF 或道路认证测试（§4.2）。
- Table 1：No-Comm 的 DS/RC/IP 为 48.9/39.7/62；类似 LangCoop 的“不做 SPARE 与 fusion、全广播”是 52.4/79.6/65、89 KB；full UNCAP 是 80.3/89.2/90、33 KB。仅无 SPARE 的 fusion 为 78.8/87.2/90、89 KB；“UNCAP w/ Images”反降到 DS 69.5/IP 78、带宽 33,600 KB，说明多视角图像会干扰 VLM 且极耗带宽（§4.3--§4.5）。
- Table 2 中 full UNCAP 的 perception confidence IG 1.04 与全融合相同，decision confidence 0.78、IG 0.60；无 SPARE 的 decision IG 0.02，图像通信 IG 0.11。论文据此主张选择性文本而非单纯更多输入能改善 plan confidence（§4.5）。
- VLM replacement：GPT-4o-mini/GPT-4o/GPT-4.1/GPT-5 的 DS 为 64.7/80.3/80.3/74.5，RC 均约 88--89.2，GPT-5 因 API 无 token probabilities 未给 IG（Table 3）。系统 VLM 只在 critical decision points 查询，作者估算约 1.33 s planning、约 1.5 s/decision overall；这仍须与控制频率、最坏时延和失效降级策略一起评估（§4.5）。
- 未来工作明列 mixed traffic、人类自然语言指令、packet loss 与实体 CAV fleet 下的 sensor noise/dynamics（§5）。论文未给通信认证、对抗文本/伪造不确定度、隐私泄漏、网络攻击或 formal collision-avoidance guarantee。

## 适用边界与复现

- 适用于封闭/低风险测试场中、具备可信 V2V 身份与已校准共享感知的 cooperative fleet；语言消息应是结构化 schema，而非自由文本直接驱动 control。
- 不可直接用于公共道路。需独立 safety monitor、可验证 trajectory planner、最小安全距离/紧急制动 shield、V2X authentication/anti-replay、消息完整性与 plausibility checks、fail-silent/no-comm fallback，并把 VLM 仅限高层建议。
- 复现应固定 CARLA/OPV2V 版本、四类与扩展九类场景、车辆数、YOLOv9 权重、conformal calibration split、GPT/VLM 版本/prompt、50 m 阈值、route 与 timeout；重建 Table 1--3、KB/episode、PMI、near-miss distance、端到端和尾部 latency。
- 扩展评估应包含 dense fleets、异构 sensors、network loss/jitter/partition、误校准、遮挡、恶意/错误协作者、隐私约束、human drivers 与物理车；报告 collision/near-collision、规则违反和不确定度校准的置信区间，而非仅平均 driving score。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 cooperative autonomy、语言通信与不确定性规划工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WHRE3513.pdf) 核验 §3 的 BARE/SPARE、conformal uncertainty/PMI、§4 的 CARLA/OPV2V 设置及 Table 1--3、§5 的未来工作；没有将模拟中“安全分数/距离裕度”提升误表述为经过真实车辆或形式化验证的安全性。
