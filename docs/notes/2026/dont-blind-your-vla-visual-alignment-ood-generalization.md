---
title: "Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/PPER9186"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PPER9186.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["simpler_simulation_scope", "ood_benchmark_scope", "teacher_alignment_bias", "representation_proxy", "no_real_robot_validation", "action_safety_not_guaranteed"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization

## 一句话总结

论文研究 VLA 在动作监督微调后遗忘视觉—语言表征的问题，并在 standard SFT 上加入以冻结通用视觉教师为参照的中层 patch 级余弦对齐损失。它在 Simpler/RL4VLA 式 OOD 仿真、LIBERO 和自建 VL-Think 诊断上报告相对 naive SFT 的改善；但证据仍是仿真/离线表示代理，没有真机、真实安全或完整预训练阶段验证。

## 方法与证据

- 起点是已预训练的 VLA 在有限机器人数据上做 task-specific SFT。作者以 OpenVLA-7B 与其 PrismaticVLM base 对照，t-SNE、attention map 及 VL-Think 都显示 naive action fine-tuning 后的表征分离度/视觉 grounding 下降（§4–5）。t-SNE、线性 probe 和 attention 可作为诊断，不能单独证明控制因果机制或安全性。
- Visual Representation Alignment 取 VLA transformer 中一个语义中层的视觉 token，借 projector 映射到教师维度，并最小化与冻结教师 patch feature 的平均负相似度：\(L_{total}=L_{VLA}+\lambda L_{align}\)（§6）。梯度更新 VLA visual/text encoder 与 backbone，教师保持冻结；作者的最佳消融选择为 C-RADIOv3 教师、backbone-to-encoder 对齐、中层、cosine loss，且报告 \(\lambda=0.2\) 最稳定（§6, §8）。
- 主要 OOD 实验为 Simpler-based RL4VLA：至少 hold out 每个 axis 的一个 factor，列出 9 novel objects、16 unseen receptacles、5 textures、16 distractor backgrounds；128 seeds 报告 mean±SD，并称使用 paired one-sided Wilcoxon test（§7.1）。训练使用 1,400 MPLib expert trajectories、16 tables/16 objects、所有 linear layers LoRA；因此结论针对该数据量、随机化和 adapter 设置，不等于任意 VLA/机器人。
- Table 1 的 OpenVLA-Align 比 OpenVLA SFT 在所列 semantic、vision、execution shifts 多数更高，例如 Carrot 0.61 vs 0.49、Instruct 0.83 vs 0.74、VisionImg 0.79 vs 0.71、Tex03 0.58 vs 0.43；但也有 Whole03 0.20 vs 0.23 的回落。摘要称“最多 10% relative gain”，因此应读作特定仿真指标的相对改进，不能概括为普适 OOD 保证。
- LIBERO 中 OpenVLA 的 Spatial/Object/Goal/Long 为 85.2/89.0/90.4/76.8，Align 为 93.2/96.4/95.6/89.4；\(\pi_{0.5}\) 和 SmolVLA 也有对应提升（Table 2）。ImageNet-100 linear probe 为 OpenVLA SFT 77.48%、pretrained 79.88%、Align 82.13%，教师 C-RADIOv3 87.31%（Table 3）；这是视觉语义可分性代理，并非机器人任务成功或风险指标。
- VL-Think 固定 WidowX-250S/Simpler pick-and-place 的低控制复杂度，让机械臂把 carrot 放到有符号的 board；八类任务涵盖形状、颜色、交通/洗涤/天气/公共信息符号、箭头和奇偶（§4）。它隔离视觉—语言知识而非操控难度；OpenVLA-Align 对颜色、public-info、shape 有改善，但 Table 7 中 Arrow/Laundry/Parity/Traffic/Weather 未普遍改善，故对齐不是对所有遗忘概念的恢复。
- Freeze baseline 在 Table 1 几乎为零，说明仅冻结视觉 encoder 会与演化的 action components 失配；这支持“需要联合适配”，不表示 visual alignment 已优于所有保留知识路线（§7.3–7.4）。论文还说明因算力约束只研究 fine-tuning，没有 full-scale robotic pretraining（§9）。

## 适用边界与复现

- 可作为 VLA 微调中降低 visual-representation drift 的研究基线，适合在已有动作数据和通用视觉教师时比较 SFT、freeze 与 alignment；部署前须在目标 embodiment、sensor、latency、lighting、occlusion、failure mode 和真实长时序任务上独立验证。
- Simpler 评测的是“real-world policy in simulation”，VL-Think 又刻意固定 grasp/动作复杂度；没有真实机械臂、接触失败、控制延迟、相机标定误差、移动人/物、紧急停止或 human safety 评测。成功率、attention 和 probe 不构成 collision/contact safety、OOD fail-safe 或 production robustness 认证。
- 对齐效果依赖教师语义与 student-token correspondence；C-RADIOv3、DINOv2、SigLIP、Theia 的消融有差异（Table 4）。需要检查教师许可/输入预处理、patch 对齐、projector freeze、\(\lambda\)、层选择和数据域偏差，避免把教师偏好迁移为无条件的“通用视觉”。
- 官方 PDF 多处将实现/附录结果留为 `??`，只给出补充材料站点而未在正文提供完整附录；复现应额外取得代码、精确 layers/projector、LoRA/optimizer/schedule、每个 OOD split、evaluation episodes、Wilcoxon pairing/p-values、LIBERO 配置与随机种子。应报告每个 shift 的最差情形和失败类型，而非只报平均成功率。

## 与 AAMAS 的关系与核验说明

这是 embodied-agent/VLA 的表征保持与 OOD 泛化工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PPER9186.pdf) 核对诊断任务、冻结教师的 patch-level alignment、RL4VLA/Simpler OOD 设置、LIBERO/linear-probe 结果、teacher/layer/loss 消融及作者明确的 fine-tuning-only 算力限制；没有把仿真 success、视觉代理或注意力图误写为真机泛化、实际操控可靠性或安全保证。
