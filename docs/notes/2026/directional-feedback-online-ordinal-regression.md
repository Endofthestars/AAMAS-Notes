---
title: "DFORD: Directional Feedback based Online Ordinal Regression Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "unclassified"]
dblp_key: ""
doi: "10.65109/QKDH8961"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QKDH8961.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02n"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["directional_feedback_reliability", "online_convex_model_assumptions", "ordinal_label_binning", "small_tabular_evaluation", "no_human_feedback_study"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DFORD: Directional Feedback based Online Ordinal Regression Learning

## 一句话总结

DFORD 在在线序数回归中不观察真实标签，只获得“本轮采样预测位于真值左侧还是右侧”的方向反馈；它以探索分布把这一个比特转成损失与阈值梯度的无偏估计，并在线性/核化凸模型下给出对数级期望正则化 hinge regret。该结果依赖反馈正确、标签阈值模型和受控特征范数；两项离散化表格实验不能证明在嘈杂人类反馈、漂移数据或复杂排序任务中同样有效。

## 方法与证据

- 序数标签为有序类别，预测由评分函数与一组有序阈值决定；论文以 MAE 和其凸 surrogate（hinge 型损失）评价，并对权重和阈值正则化（§2--3）。
- 每轮以混合分布 \(P^t=(1-\gamma)P_1^t+\gamma P_2^t\) 抽样标签：\(P_1\) 集中于当前模型标签，\(P_2\) 在其左右按距离衰减地探索。系统仅返回采样标签相对真标签的左/右方向；据此构造 \(\tilde z^t\) 与 \(\tilde\tau^t\)，作为损失导数的无偏估计，再进行在线更新（§3）。
- 线性 DFORD 维护特征权重与阈值；核化版本以支持向量表示评分函数。为避免在线 kernel 表示随轮数无限增长，论文加入截断策略，以额外近似代价换取受限存储/计算（§3--4）。
- Lemma 4.1 在论文给定条件下保证估计阈值维持有序；Theorem 4.2 在特征范数、正则系数和探索率等条件下给出期望正则化 hinge regret 上界 \(16K^2(R^2+1)\ln K\ln T/(\lambda\gamma)\)，即随轮数为 \(O(\log T)\)（§4）。这是相对于文中比较器和 surrogate 的理论保证，不能直接等同于真实 MAE 的普遍优势。
- 实验将 Abalone 分为 4 个标签（degree-3 kernel）并将 California Housing 按等频方式分为 10 个标签（linear）；以 10 次运行的 MAE 比较全信息 PRank 与区间反馈 PRIL。报告中 DFORD 优于 PRIL、并可与 PRank 接近，证据范围仅限这两套处理后的表格数据（§5、表 1）。

## 适用边界与复现

- 适合只能询问“偏高还是偏低”而无法披露精确等级的在线标注或交互式排序场景；反馈方向应被记录为带噪声且可能有系统偏差的信号，不能默认正确。
- 理论条件包括有界特征、特定正则化/探索设置、固定有序标签与阈值可行性；类别不均衡、概念漂移、延迟反馈、对抗或依赖性反馈不在证明范围。
- 两个数据集都经过标签分箱；不同 bin 数、切分、核、\(\gamma\)、\(\lambda\) 与截断预算都可能改变 MAE 和计算量。论文未给出人类反馈实验、噪声消融或跨领域评估。
- 复现应固定数据预处理和轮次顺序，实现混合采样、importance-weighted 无偏估计、阈值投影/有序性检查及 kernel 截断；同时报告真实 MAE、surrogate regret、查询率、方向错误率、运行时间和支持向量数，并和随机/延迟/噪声反馈及不同分箱方案比较。

## 与 AAMAS 的关系与核验说明

该文把受限反馈下的在线学习建模为可用于智能体交互的序数决策组件。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QKDH8961.pdf) 人工核对方向反馈定义、混合探索、Lemma 4.1、Theorem 4.2 以及 Abalone/California Housing 实验；未把 surrogate regret 或处理后的两组数据结果表述为通用部署性能。
