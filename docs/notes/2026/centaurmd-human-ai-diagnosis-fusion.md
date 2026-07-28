---
title: "CentaurMD: Confidence-Aware Human-AI Decision Fusion for Multi-Label Disease Diagnosis via Label-Specific MoE"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/DWYB7830"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DWYB7830.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["medical_high_stakes", "simulated_expert_annotations", "retrospective_dataset_only", "no_prospective_or_external_clinical_validation", "not_for_diagnosis"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# CentaurMD: Confidence-Aware Human-AI Decision Fusion for Multi-Label Disease Diagnosis via Label-Specific MoE

## 一句话总结

CentaurMD 以最大熵多标签混淆矩阵估计缺失的 human confidence，再用 label-specific MoE 为 human/AI 分配每标签权重；在三个回顾性数据集上优于多种 fusion baseline，但部分“专家”预测是按固定 accuracy 模拟，且没有前瞻性临床验证，因此不能用于诊断或替代医生。

## 方法与证据

- 先从 ground truth、human label 与 label-transition probability 构造 MLCM，编码错诊/漏诊相关性；Transformer 提取其特征，label-specific gates 产生 human/AI 权重与每标签 threshold（§3）。
- 在 ChestX-ray、S12L-ECG、LID-FFA 比 human-only、ResNet18/VGG19/AlexNet 和 CHM、HAIT、JSF、L2D-CL 等；指标为 Hamming loss、AUC、MAP、MMR（§4）。
- ChestX-ray 有 4,375 X-rays、13,080 annotations、22 radiologists，reference 为 3 radiologist consensus；S12L-ECG 有 827 records。LID-FFA 的 human annotations 则按 90% accuracy 模拟生成（§4.1）。
- 作者报告相对既有 fusion baseline 平均 Hamming loss 降 39.14%、MMR 升 17.38%；数值是数据集/模拟专家/阈值设定下的 retrospective metric，非临床 outcome（§4--5）。

## 临床边界与复现

- simulated expert labels 不能代表真实临床不确定性、reader disagreement、疲劳、workflow、患者群体偏差或罕见病；融合器从验证资料学习 human reliability 也可能在新站点失配。
- 无 prospective study、external multi-site validation、calibration/decision-curve、subgroup fairness、harm analysis 或监管/人机责任流程，不能把 Hamming/MMR 改善解释为安全、有效诊疗。
- 多标签漏诊/误诊的临床代价不等，固定 threshold 与 aggregate metrics 不足。任何医疗使用须由合格临床团队、独立验证、监测和合规审批决定。
- 复现应公开 split、preprocessing、human/模拟标注生成、模型和 gates、threshold selection、seed、per-label sensitivity/specificity/calibration 与跨机构测试；本笔记不构成医学建议。

## 与 AAMAS 的关系与核验说明

该文研究 human-AI multi-label decision fusion。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DWYB7830.pdf) 核对方法、三数据集、真实/模拟标注差异、基线和指标；明确不将其视为临床诊断验证或部署建议。
