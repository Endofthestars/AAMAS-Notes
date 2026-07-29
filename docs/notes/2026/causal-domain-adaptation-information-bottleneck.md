---
title: "Causal Domain Adaptation: An Information Bottleneck Approach"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/UYYQ1151"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYYQ1151.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03p"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "markov-blanket-invariance", "causal-graph-specification", "zero-shot-domain-adaptation", "synthetic-shift-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Causal Domain Adaptation: An Information Bottleneck Approach

## 一句话总结

该工作将 domain adaptation 写为学习对目标变量充分、但压缩掉不稳定变化的表示；已知 DAG 时只用 target 的 Markov blanket。线性 Gaussian 情况的 MB--GIB 为 CCA 风格闭式投影，非线性/非 Gaussian 情况的 MB--VIB 使用变分编码器；在作者构造的 MAGIC--IRRI 大幅分布变化中，MB--GIB 表现最佳。

## 方法与证据

- 理论声称：Gaussian 情况下最优 bottleneck directions 可由 Markov blanket 表达且信息谱与所有非 target 变量一致；若 target conditional on blanket 不变，source 学到的 population predictor 在 target 保持风险；有限样本下对 blanket 外 shift 鲁棒（§2）。
- MB--GIB 先标准化，再以 CCA 排序 blanket 输入中对 target 最有信息的线性方向，并按 bottleneck 参数丢弃弱方向；restricted-to-blanket 在该 Gaussian 设定下无信息损失（§2.1）。
- MB--VIB 用 encoder 输出 latent distribution、probabilistic decoder 预测 target，并以压缩罚项抑制无关输入，支持高维非线性/非 Gaussian 数据（§2.2）。
- 评估含 7-node SEM、64-node MAGIC--IRRI Gaussian BN、Sachs single-cell 数据；摘要只详细给出 MAGIC--IRRI：同时改变 3 个协变量后隐去 HT，MB--GIB MAE/RMSE/$R^2$ 为 5.5706/7.0083/0.5670，MB--VIB 为 7.0837/10.0190/0.1211，BN 为 9.3827/11.1872/-0.0957，DNN 为 14.4523/17.7908/-1.7711（Table 1）。

## 适用边界与复现

- 保证依赖 Markov blanket invariance、足够正确的 causal graph 与对 blanket 内的可支持数据；若 target-to-blanket mechanism 变了、blanket 错设、latent confounding 或 blanket 内严重 support shift，zero-shot transfer 会失败。
- 复现应固定 DAG/blanket、intervention 机制、source/target 划分、标准化、CCA/IB 参数、VIB architecture 与 $\beta$、随机种子、所有三类数据结果及 runtime。论文建议以 target residual/likelihood 监控，并可改 parents-only、提高压缩或加小量 target labels。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYYQ1151.pdf) 人工核对 MB--GIB/MB--VIB、假设和 Table 1；未把作者模拟的 mechanism-stability 结果泛化为未知真实因果结构下的保证。
