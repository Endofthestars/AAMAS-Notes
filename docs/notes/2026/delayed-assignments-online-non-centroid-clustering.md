---
title: "Delayed Assignments in Online Non-Centroid Clustering with Stochastic Arrivals"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "marl_coordination", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/AVAR7513"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AVAR7513.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["asymptotic_iid_model_only", "finite_metric_space_assumption", "fixed_cluster_size_assumption", "no_empirical_evaluation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Delayed Assignments in Online Non-Centroid Clustering with Stochastic Arrivals

## 一句话总结

论文提出允许付出等待代价的 online 非中心聚类：在有限度量空间、未知固定 i.i.d. 到达分布、簇容量为固定常数且簇数随输入增长的条件下，贪心 DGreedy 有常数 ratio-of-expectations（等容量时上界为 `8/(1-e^-2)`）；这不是 adversarial arrival、有限样本或真实 matchmaking 系统的竞争比保证。

## 方法与证据

- 每个到达点可延后不可撤销地加入已有簇或开启簇；目标同时计入簇内两两距离与等待成本。为避免 singleton 的平凡零代价，簇被要求最终为预设固定大小（§3）。
- DGreedy 在等待点与可容纳簇的距离不超过双方等待量之和时插入；也比较两个等待点创建空簇的方案，并以增量成本和等待量打破选择（算法 1，§4）。
- 分析把点分为 early/late：用 arrival distribution 定义位置半径，界定早到点的预期等待；每个位置最多一个 late point，并以有限空间直径控制其余项（Lemmas 1--5）。
- Theorem 3 在 UIID、有限 metric、每种 cluster size 为常数且 `k` 随 `n` 增长时给出常数 RoE；等大小簇的渐近上界为 `8/(1-e^-2)`。论文也说明可经变换扩展某些 non-metric/hedonic setting，并讨论 lower/upper capacity bounds（§4--5）。

## 局限与复现

- 保证比较的是期望总成本之比在 `n → ∞` 的极限；并不涵盖 adversarial 或分布漂移的到达、未知/无限位置空间、短队列，亦非每条序列的常数 competitive ratio。
- 证明依赖固定簇大小、有限 metric 与独立同分布位置；实际游戏组队、拼车或联邦学习常有取消、异质偏好、动态容量、再分配和多目标公平性，不能直接套用。
- 文中无仿真、真实数据或系统实验，因此没有 latency、匹配质量、吞吐、公平性或计算开销的经验结论。复现应实现算法与理论定义，分别在 i.i.d./shift/adversarial trace 下报告有限样本成本、等待分位数与运行时间。
- 作者列出 general delay cost、已知或随时间变化的 arrival distribution、以及允许付费修改既有聚类为后续方向（§6）。

## 与 AAMAS 的关系与核验说明

该文将 coalition/matching 的延迟决策抽象为 online 聚类，是多智能体资源协调的理论基础工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AVAR7513.pdf) 人工核对问题定义、算法、Theorems 1--3、适用前提和未来工作；没有将其渐近随机模型结论外推为产品级配对性能。
