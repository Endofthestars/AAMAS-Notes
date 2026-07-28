---
title: "Cross-Domain Alignment with Fine Geometric Perception for Detail-Preserving Point Cloud Completion"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/MQXV5147"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQXV5147.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["synthetic_shape_benchmark", "cross_category_not_real_sensor_domain", "completion_hallucination_risk", "no_downstream_safety_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Cross-Domain Alignment with Fine Geometric Perception for Detail-Preserving Point Cloud Completion

## 一句话总结

CAM-FGP 将局部细节提取（FGDE）、hierarchical optimal transport 跨域 feature alignment（HOTN）与多阶段 hidden-state fusion 结合，完成稀疏点云；在 ShapeNet-55/34 与 PCN 的合成/对象 benchmark 上降低 Chamfer Distance、提高 F-score，但并非真实传感器或下游机器人安全验证。

## 方法与证据

- FGDE 从 partial cloud 获取高分辨率局部几何，并以低分辨率全局 context（DCPM/self-attention）补足缺失区的结构线索；目标是曲率、边界、连续性等细节与全局形状语义兼顾（§3.1）。
- HOTN 对 sample/domain/patch 层级的多源 feature distributions 做 optimal transport 对齐，feature OT 用 sliced Wasserstein distance 近似以降低大规模计算成本（§2.1、§3.2）。
- Multi-Stage Hidden-State Fusion 对各 completion stage 的全局表示施加可学习权重，以融合 coarse 与 fine predictions（Eq. 12--14、§3.3）。
- ShapeNet-55 训练样本由 8,192-point object 合成：2,048 点 partial input、6,144 点 target；评测用固定 viewpoint，并按 25%/50%/75% missing 分 easy/medium/hard。ShapeNet-34 为 unseen-category protocol；PCN 为 object-shape benchmark（§4.1）。
- 论文表中 CAM-FGP 在 ShapeNet-55 报 CD-Avg 0.89、F-score 0.491（Table 1）；ShapeNet-34 unseen categories 报 CD-Avg 1.32、F1 0.540（Table 2）；PCN 报 L1 CD-Avg 6.70（Table 3）。PCN ablation 去 FGDE/DCPM/HOTN/multi-stage fusion 后平均 CD 分别为 7.82/7.58/7.45/7.60（Table 4）。

## 适用边界与复现

- ShapeNet/PCN 的 partials 是由完整物体点云与模拟 viewpoint/遮挡生成；“cross-domain”在本文主要指 source/target feature 与类别泛化，不证明对真实 LiDAR、深度相机、天气、反射、标定误差或动态场景的 domain transfer。
- Completion 会推断不可见几何；低 Chamfer/F-score 不能保证生成部分真实存在，故不能直接作为碰撞规避、抓取、导航或自动驾驶的感知事实。
- 应使用同一 point count、viewpoint/occlusion protocol、Chamfer/F-score 定义、normalization、seed 与 hardware，复现所有 three difficulty levels 和 category split；另外报告 runtime/memory、真实采集 cross-sensor 数据及 downstream task impact。
- 文中视觉示例与 ablation 支持各模块在该基准上的贡献，但不提供不确定性估计、拒绝输出机制或针对安全关键长尾失效的评估。

## 与 AAMAS 的关系与核验说明

这是可服务于 embodied agents 的 3D perception/representation 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQXV5147.pdf) 核对模块、数据生成协议、Tables 1--4 与 ablation；没有将合成对象完成表现表述为真实机器人或车辆可部署能力。
