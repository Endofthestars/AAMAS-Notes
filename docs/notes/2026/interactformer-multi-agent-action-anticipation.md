---
title: "InteractFormer: Inter-Agent Spatiotemporal Attention for Multi-Agent Action Anticipation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "human_agent_interaction", "marl_coordination"]
dblp_key: ""
doi: "10.65109/ZFVD4206"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZFVD4206.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "multi_agent_video_anticipation", "attention_visualization", "lemma_benchmark", "sportshhi_pseudo_anticipation", "not_intent_or_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# InteractFormer: Inter-Agent Spatiotemporal Attention for Multi-Agent Action Anticipation

## 一句话总结

InteractFormer 用 token-level cross-agent visual attention、bounding-box cross-attention 与 temporal cross-attention 预测多 agent 的 future verb–noun actions 或 pairwise interaction labels。它在 LEMMA household collaboration 与 SportsHHI team-sports 上优于所列 baselines，尤其 LEMMA 复杂 multi-agent settings；SportsHHI 只取每 clip 前 25% 构造 pseudo-anticipation。模型预测数据集标注的未来动作/交互类别，不等于理解人的意图、可靠预测真实世界协作，或可安全触发机器人主动协助。

## 方法与证据

- 输入 \(N\) agents、\(T\) frames 的 agent-specific visual views；输出每 agent future \((verb,noun)\) 与 pair \((i,j)\) interaction class（§2）。预测依赖 video crop/track 与 bounding boxes，检测、遮挡、身份 switch、视角缺失和新角色会影响下游结果；摘要未测这些误差。
- visual cross-attention 让 agent attend 到其他 agent patch tokens，BBox attention 以 trajectories/relative configuration grounding；temporal cross-attention 建模 coordination/role switching。attention weights 是模型内部相关性，不构成因果、意图或解释忠实度证明，无法单独验证“为何”预测正确。
- LEMMA 使用 egocentric streams 加 third-person BBox enrichment，按 official setup joint predict next actions；Table 1 的 2×1/2×2 cases gains较显著，但 1×2 verb/noun并非全胜。SportsHHI 用 full frame ViT+BBox centers，并只观察 clip 前 25%来预测 label，属于作者定义的 pseudo anticipation，不等于原数据集真实 future-action protocol。
- SportsHHI Table 2：SlowFast-R50/R101/ViT-B 上 mAP/Recall@20 分别 7.55/30.91、8.01/30.24、9.82/37.64，高于 Wu et al. rows。摘要未给 splits、seeds/CI、latency、tracking quality、class imbalance、longer horizons或 per-interaction errors。
- Figure 1 的 qualitative attention 称模型在合作时关注伙伴/共享 object、独立时偏自 FPV。这说明可视化案例一致性，但不验证 attention explanation 的充分性、反事实稳定性或对 human–robot safety 的作用。

## 适用边界与复现

- 适合受控视频 benchmark 的 multi-person activity anticipation；不能仅据预测自动执行机器人动作、判断人类意图/责任或在体育、家庭、工作场所进行安全关键干预。部署需独立的 perception uncertainty、action-risk、consent/privacy与 human confirmation layers。
- 复现需固定 LEMMA/SportsHHI versions/splits、view/crop/BBox extraction、observation horizon、encoders/feature resolution、cross-attention architecture、loss/optimizer、baselines、seeds/raw predictions及 mAP/Top-1/Recall@20/CI。明确 SportsHHI pseudo-anticipation construction。
- 应测 BBox/tracker noise、occlusion、camera/lighting/domain shift、more agents、unknown roles、long horizon、counterfactual interactions及 calibration/abstention。报告 errors in action vs interaction、false proactive-assistance triggers、runtime与 privacy impact。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 embodied multi-agent action anticipation 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZFVD4206.pdf) 核验 architecture、LEMMA/SportsHHI protocols、Tables 1–2及 attention-visualization scope；没有将 benchmark label prediction 写成人类意图或安全保证。
