---
title: "Cleaner Adversarial CAPTCHAs: Intelligent Targets and Precise Noise for Usable Security"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/AFAW3962"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AFAW3962.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["no_human_usability_study", "imagenet_proxy_not_deployed_captcha", "adaptive_attacker_scope", "architecture_dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Cleaner Adversarial CAPTCHAs: Intelligent Targets and Precise Noise for Usable Security

## 一句话总结

论文提出保留梯度幅度的 Precise Gradient Method（PGM），并以类别混淆或模型置信度选择目标类别，令 ImageNet 分类器更快被定向误导、且 L2 扰动更小；但“人类可用”的结论仅由视觉扰动代理指标支撑，文中没有真人 CAPTCHA 可解性或真实攻击成功率试验。

## 方法与证据

- PGM 以归一化的原始输入梯度替换 FGSM 的 sign 更新，并结合噪声扩散；Class Relations Network（CRN）从 ILSVRC2012 验证集构造每类的常见 top-5 混淆类别，Distance-Based Target（DBT）则按单图预测概率排名选目标（§5）。
- 实验在 ImageNet validation set 的 MobileNetV2/V3、ResNet50、EfficientNet-B4/B7、ViT-B/16 上，使用相同的逐步扰动 schedule；指标为达到误分类的平均迭代次数和 L2 distortion（§6）。例如 EfficientNet-B7 的 CRN-10 + PGM 平均 2.29 次迭代，对随机目标 + PGM 为 3.92；多数组合的 PGM L2 小于 FGSM（表 2–4）。
- 对 MobileNetV2 做五阶段 adversarial retraining（每阶段加入 10,000 个新扰动样本）时，随机目标攻击变难得多，而 CRN/DBT 的迭代数更稳定；同时干净图像 AUC 从 0.971 降至约 0.945–0.950（§7、表 5）。

## 局限与复现

- ImageNet 物体分类、平均迭代数与 L2 噪声不是 CAPTCHA 的端到端安全或可用性测量；文中未进行真人阅读正确率、耗时、无障碍性、误拒率，亦未在真实 CAPTCHA 服务或独立 bot solver 上测试。
- 结果依赖于白盒/已知分类器、指定的目标选择、扰动 schedule 与六个架构。作者也指出 DBT 的排名规律在 ViT 上不稳定；压缩、去噪、adversarial retraining 和自适应攻击仍会构成攻防循环（§6、§8）。
- “更低 L2”不等同于人眼不可觉或不同设备/压缩链路下稳定。实际部署还需对迁移攻击、查询预算、过滤、重放、隐私与对合法用户的公平影响进行独立评估。
- 复现应开放 ImageNet 样本划分、所有预训练权重/版本、CRN 构造、目标 rank、epsilon schedule、随机种子和逐样本结果；部署评估须预注册真人研究与多类 bot/后处理攻击。

## 与 AAMAS 的关系与核验说明

这是以对抗样本生成改善自动化验证挑战安全性的工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AFAW3962.pdf) 核对算法、ImageNet 实验、重训练设定及作者自述的自适应攻击限制，未把分类代理结果表述为已证明的可用 CAPTCHA 系统。
