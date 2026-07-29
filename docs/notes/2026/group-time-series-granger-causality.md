---
title: "From Knowledge to Causality: Self-Supervised Representation Learning for Granger Causal Discovery in Groups of Time Series"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "applications"]
dblp_key: ""
doi: "10.65109/CZZR3069"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CZZR3069.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02u"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "granger_not_interventional_causality", "representation_learning_dependence", "synthetic_and_fmri_scope", "no_clinical_inference"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# From Knowledge to Causality: Self-Supervised Representation Learning for Granger Causal Discovery in Groups of Time Series

## 一句话总结

CausalKGR 先以 Transformer VAE 和 Knowledge-Conditional Attention（KCA）为每组多变量时间序列学习表征，再以 global fusion 融合跨组信息，并用带 group-lasso 的非线性自回归模型识别表征级 Granger 边。在线性 VAR、非线性 Lorenz-96 与静息态 fMRI 上摘要报告优于四个基线；这些边表示给定模型、观测和时间窗口下的预测增益，不能被解释为干预因果、脑区机制或临床诊断结论。

## 方法与证据

- 输入为 \(m\) 组多变量时间序列，目标同时学习每组高层表示并推断 directed group-level Granger graph；若组 \(j\) 的过去在控制其它组后改进组 \(i\) 表示的预测，则称其 Granger-cause \(i\)（§2）。
- local dynamics encoder 用 Transformer VAE 得到潜变量；KCA 以输入 embedding 为 query、以潜变量派生 key/value，迫使重构依赖压缩后的“knowledge condition”。global interactions fusion 再对所有组潜变量建全局 context，以重构、\(L_1\)、FFT 与 KL 等损失联合训练（§3.1--3.2）。
- 表征阶段后，每个目标组使用 attention autoregressive predictor；输入权重列施加 group lasso，proximal step 将某列缩至零时，将该源组判为 Granger non-causal。框架也可把每个单变量当作一组应用于一般多变量发现（§3.3）。
- 与 GC、2GVCI、gCDMI、HGCRM 比较时，摘要称 CausalKGR 在 VAR/Lorenz-96 的 AUROC/AUPRC 最优；Lorenz-96 随组数增加仍称 AUROC>0.90，而 HGCRM 约 0.78。fMRI 7 ROI 案例指出 PCC 对 AG/MTG 的边，且基线漏检 MTG→AG；删除 GIF 有明显下降（§4）。

## 适用边界与复现

- Granger causality 是时间预测意义的方向性，受未观测共同原因、采样频率、滞后窗口、非平稳、测量噪声和表征学习影响；它不是结构因果模型的 intervention effect。
- 组划分、VAE latent size、KCA、FFT/正则权重、稀疏阈值和优化器都可能改变边。高 AUROC 的合成机制恢复，不等价于真实高维系统的边可靠性。
- fMRI 结果为单个 resting-state 数据集的网络解释，不能推出脑区直接影响、精神疾病机制或临床标志物；多重比较、个体异质、HRF 延迟和预处理应独立处理。
- 复现应公开数据切分、组定义、窗口/预处理、网络/latent/损失/稀疏参数、seed 与 baseline 调参；报告边稳定性、bootstrap、precision-recall、calibration、消融及对隐混杂/非平稳/错分组的敏感性，必要时以干预或外部证据验证候选边。

## 与 AAMAS 的关系与核验说明

该文为群体时间序列的表征学习与预测型因果图发现提供组件。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CZZR3069.pdf) 人工核对 KCA、GIF、group-lasso、四基线、VAR/Lorenz-96 与 fMRI 结果；未把 Granger 图夸大为可干预或临床因果图。
