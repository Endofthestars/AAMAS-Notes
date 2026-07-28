---
title: "IntRec: Intent-based Retrieval with Contrastive Refinement"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: "10.65109/AGOG8131"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AGOG8131.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["oracle_feedback_evaluation", "candidate_proposal_recall_limit", "user_feedback_misinterpretation", "open_vocabulary_mislocalization", "human_robot_overclaim"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# IntRec: Intent-based Retrieval with Contrastive Refinement

## 一句话总结

IntRec 在冻结的 CLIP 与 CenterNet2 proposals 之上维护 Intent State：positive anchors 与 rejected-region negative constraints，并以 `max positive similarity − λ × max negative similarity` 重新排序候选框。它在 LVIS/Objects365/COCO 上报告 AP 提升，在作者构造的 LVIS-Ambiguous 上一次 corrective feedback 从 14.8 提升至 22.7 AP；但该 feedback 在评测中由 ground truth 自动判定 top-1 错误并注入，且模型只能重排已有 proposals，因此不能证明真实用户、机器人或 AR 系统会可靠消歧或识别候选集以外目标。

## 方法与证据

- 初始 query 可含 text、reference image 或两者；冻结 CLIP ViT-B/16 text/image encoders 产生 512-d embeddings。Intent State \(IS_t=(Z_{pos}^{(t)},Z_{neg}^{(t)})\) 记忆 confirmed cue 与 rejected candidate，候选区由冻结 CenterNet2/ResNet-50 class-agnostic detector 生成（§3.1、§4.1）。
- 候选 \(r_j\) 的 score 是对 positive exemplars 的最大 cosine similarity 减去 \(\lambda\) 倍对 negative exemplars 的最大 similarity（Eq. 1）。negative feedback 将被拒区域 embedding 加入 \(Z_{neg}\)；positive confirmation/refinement 将区域或新文本 embedding 加入 \(Z_{pos}\)（Eq. 2--3、Algorithm 1）。
- 文中的 ambiguity-resolution 推导只说明：若 target 与 rejected distractor 为不同 embeddings，且选择足够的 \(\lambda\)，可使这**一对**候选的重排得分反转。它不保证 user 的反馈正确、target 在 candidate set、所有多个 distractors 都被消除、box localization 正确或开放域语义被理解（§3.4）。
- 评测在 LVIS v1（866 common/frequent base、337 rare novel）、Objects365 与 COCO。每张图固定生成 \(M=100\) proposals，最多 \(K=2\) turns，\(\alpha=0.6,\lambda=1\)（§4.1--4.2）。LVIS-Ambiguous 是用 frozen Grounding DINO 与 ground-truth category/IoU 规则筛出的“同类 distractor 排在 true target 前”的子集，而非自然用户对话数据。
- Turn-1 的 protocol 是 oracle-style：若 Turn-0 top-1 错误，就把该 prediction 直接提供为 negative feedback，然后计算重排 AP。Table 4 从 14.8 到 22.7（+7.9）是在这种模拟 corrective signal 下取得；实际用户要识别/选择错误框、表达新的正约束，并可能误操作，论文未评估。
- Table 2：ResNet-50 下 text-only IntRec 35.0 AP、multimodal 35.4 AP；后者 rare AP 25.6，相对 CAKE 25.0、CoDet 24.5。Table 3 的 zero-shot transfer 在 Objects365/COCO 使用同一种 top-1 negative 重排，Turn-1 比 Turn-0 高；单次交互约 29 ms（RTX 3090）。

## 安全边界与复现

- 系统不会产生新框或修正 proposal：作者明确承认若真实目标太小、严重遮挡或 detector 未给出 bounding box，interactive refinement 无法恢复。任何抓取、导航、AR 指引或盘点场景必须先评测 proposal recall、检测置信度、遮挡/OOD 与 false-localization，不应因后续 re-ranking 而跳过感知安全门槛。
- 实验把 “not this object” 当成准确、无歧义的 region-level negative label；真实界面中的歧义语言、错误点击、延迟、多用户冲突、恶意反馈、不同视觉能力与反馈疲劳都可能把正确 target 记为负例，造成持续误导。须提供显示候选、undo/reset、confirmation threshold、feedback provenance、误点击容错与人工 fallback。
- 论文提及 human-robot collaboration、AR/VR 作为动机，但没有用户研究、交互时长/认知负担、任务成功/安全、隐私或实体机器人试验。AP 与 29 ms GPU re-ranking 不等于 end-to-end latency、可用性、动作授权或风险降低。
- CLIP/CenterNet2 冻结模型的 dataset bias、文本/图像编码歧义和开词表误检仍存在；negative penalty 只抑制相似区域，也可能排除真正相似目标。高风险场景须结合物体 identity verification、multi-view/temporal consistency、距离/碰撞约束、uncertainty display与 explicit human approval，禁止单框定位直接触发物理动作。
- 复现应锁定 CLIP/CenterNet2/ImageNet-21k weights、proposal count/score、LVIS split、LVIS-Ambiguous construction rule、IoU threshold、\(K,\alpha,\lambda\)、oracle feedback simulator与 GPU timing；并补充真实/噪声反馈、target-not-proposed、复杂语言、对抗遮挡与 end-to-end user-study 测试。

## 与 AAMAS 的关系与核验说明

这是 interactive open-vocabulary object retrieval 与 stateful contrastive refinement 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AGOG8131.pdf) 核对 Intent State、Eq. 1--3、candidate architecture、LVIS-Ambiguous 构造、Turn-1 oracle feedback protocol、Tables 2--5 和作者给出的 proposal-recall 限制；没有把模拟纠错 AP 提升表述为真实人机交互、可靠感知或安全执行保证。
