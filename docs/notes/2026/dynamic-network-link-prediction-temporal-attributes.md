---
title: "Dynamic Network Link Prediction Based on Characterization of Temporal Attributes"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering"]
dblp_key: ""
doi: "10.65109/WGQF3050"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WGQF3050.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03k"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "dynamic-graph-benchmark", "unclear-complexity", "reference-quality-concern", "limited-reproducibility-detail"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Dynamic Network Link Prediction Based on Characterization of Temporal Attributes

## 一句话总结

GDTEformer 将节点和属性的时间演化表示为带方差的不确定性高斯嵌入，融合空间相对位置偏置与结构损失来做动态网络链路预测。扩展摘要在 Cora、DBLP、MOOC、Brain 上报告较 Transformer、TGAT、DNformer、MTSN 更高 AUC/Precision；模型复杂度、实现和全部实验细节尚不足以据此复现或判断泛化。

## 方法与证据

- GDTE 把节点/属性 embedding 设为随时间变化的函数，以常微分方程描述动态，并将条件 embedding 建模成均值由积分演化、协方差为 $\delta_t I$ 的 Gaussian；新节点以标准 Gaussian 初始化。论文将方差解释为不确定性（§2.2）。
- 编码器—解码器接收 GDTE 生成的节点矩阵和属性矩阵，以多层 multi-head self-attention 与特征融合将 link prediction 重写为矩阵生成问题（§2.1）。
- Spatial Position Encoding 以节点最短路径倒数构造相对位置权重，并作为可学习 bias 加入 attention score；Structural Loss 将交叉熵与归一化 Laplacian 矩阵范数约束加权，以兼顾局部预测与全局结构（§2.2）。
- 按时间顺序 70%/15%/15% 划分训练/验证/测试，并用 AUC、Precision 评估。Table 1 的 AUC 结果中，70% 训练时 GDTEformer 在四数据集为 0.9859/0.9764/0.9657/0.9546；30% 时为 0.7469/0.7356/0.7213/0.6856。正文称 3 个组件均不可少，且在 MOOC 上 GDTE 比 DeepWalk 高 0.0758 AUC（§3）。

## 适用边界与复现

- 摘要未完整说明各数据集的时间粒度、负采样、节点/属性特征预处理、超参数、计算成本和统计显著性；跨数据泄漏与时间切分实现都可能显著影响结果。
- References 中含有占位式作者条目，文献链不能作为方法来源证据。复现应以公开代码或完整版本为准，固定 chronological split、负边构造、embedding/ODE/attention 宽度、SPE 截断与 structural-loss $\alpha$，并同时报告 AUC、Precision、训练时间和方差。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WGQF3050.pdf) 人工核对 GDTE、SPE、结构损失、数据集和 Table 1；表中数字是作者在摘要中报告的 benchmark 结果，未被外部复现验证。
