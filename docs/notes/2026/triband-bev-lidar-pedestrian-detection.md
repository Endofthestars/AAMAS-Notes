---
title: "TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/INST9866"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/INST9866.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["autonomous_driving_safety_scope", "kitti_validation_only", "single_gpu_latency_measurement", "no_system_level_or_field_validation", "not_for_deployment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion

## 一句话总结

TriBand-BEV 将完整 LiDAR cloud 压缩成三 height-band 的 2D BEV tensor，用轻量 backbone/高分辨率 neck 预测 oriented 2D footprint，再回投 3D box；在 KITTI validation 取得 pedestrian BEV AP 58.7/52.6/47.2 (easy/moderate/hard) 与 49 FPS，但这不是自动驾驶安全或真实道路部署验证。

## 方法与证据

- 三 channel 编码 height/intensity/density，检测 head 预测 BEV oriented boxes，IQR filter 剔除 reconstruction outliers；单 network 处理 car/pedestrian/cyclist（§3--5）。
- 训练含 vertical re-bin 与 reflectance jitter；使用 high-resolution bidirectional fusion、area attention、rotated IoU 与 distribution focal side offsets（§4--5）。
- KITTI official-style 评估含 easy/moderate/hard（由 occlusion/truncation 等定义）；RTX 4090 Laptop、PyTorch 2.5.1/CUDA 测单次 inference 20.4 ms≈49 FPS（§3、§6）。
- 相对 Complex-YOLO 报 pedestrian BEV AP 增益；论文也指出主要限制为 height estimation，multi-offset inference 约三倍成本（§6--7）。

## 安全边界与复现

- KITTI AP/latency 不覆盖真实道路 weather、sensor dirty/failure、time sync、motion prediction、braking/control、redundancy、long-tail VRU、bias、系统延迟或安全 case。
- LiDAR-only 选择可能在稀疏远距、遮挡或反射异常时失效；“stable under occlusion”的 qualitative scene 不是 failure-rate 或 assurance 证据。
- 49 FPS 与 RTX 4090 Laptop 条件不可直接迁移到 embedded hardware；应测 end-to-end latency、memory、功耗、drops、adversarial/weather 和 closed-loop safety。
- 复现应发布 split、calibration、BEV range/bin、augmentation、IQR/NMS、GPU/precision、per-class/per-distance AP；任何车辆/机器人使用须独立安全验证与人类责任机制。

## 与 AAMAS 的关系与核验说明

该文是移动机器人 LiDAR 3D perception 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/INST9866.pdf) 核对 encoding、KITTI、AP、FPS 和 height limitation；未将 benchmark 结果表述为道路安全或可直接部署。
