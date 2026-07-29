---
title: "Cost-Aware Best Arm Identification via Dueling Feedback with Applications to Large Language Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "agent_engineering", "resource_allocation"]
dblp_key: ""
doi: "10.65109/GEKA7634"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GEKA7634.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03o"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "condorcet-winner-assumption", "known-costs", "asymptotic-guarantee", "human-preference-noise"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Cost-Aware Best Arm Identification via Dueling Feedback with Applications to Large Language Models

## 一句话总结

该工作在 dueling bandit best-arm identification 中显式计入比较成本：每个 arm 已知成本，比较 $(i,j)$ 花费 $c_i+c_j$。在唯一 Condorcet winner 假设下，作者推导可解释的实例相关 cost lower bound，并提出 DCTAS；其保证 $\delta$-probably correct，且当 $\delta\to0$ 时总成本渐近最优。

## 方法与证据

- 学习者顺序选择 pairwise preference comparison，观察 Bernoulli 结果 $p_{i,j}$；目标以误差最多 $\delta$ 找出击败所有其他 arm 的 Condorcet winner，并最小化截至停止的累计比较成本（§2）。
- 作者利用 Condorcet 结构将通常难解释的 min--max information lower bound 化为对各候选非最优 arm 与比较对象的显式式子，给出最优 cost allocation 的 closed-form characterization（Theorem 3.1）。
- DCTAS 依经验偏好与已知成本计算目标 sampling fractions：初期保证每个 pair 被抽样，其后跟踪落后最多的目标分配；以 Chernoff-style statistic 停止并推荐最大化最弱证据的 arm。Theorem 4.1 声称算法 $\delta$-PC 且成本与 lower bound 渐近匹配（§4）。
- 实验包括三臂合成实例（$\delta=0.01$、500 trials）及 Chatbot Arena 的 text-to-image/text-to-text/vision/search 偏好数据（100 trials、$\delta=10^{-10}$）。摘要称 DCTAS 一致低于 TAS 等基线；使用另一停止规则的 DCTAC 实测成本最低，但该经验结果不替代 DCTAS 的渐近保证（§5）。

## 适用边界与复现

- 保证要求 costs 事先已知、偏好独立 Bernoulli、唯一 Condorcet winner；循环偏好、随时间变动的 API 定价/延迟、依赖性人类标注与不可比较输出可能破坏模型。
- 复现应给出所有 pairwise outcomes、成本口径（模型生成、人审、重试和缓存）、$\delta$、tie/缺失处理、DCTAS tracking 与 stopping 参数、随机种子及实际累计成本的置信区间。模型选择部署还应评估质量、延迟、隐私和公平，而非仅最低查询费用。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GEKA7634.pdf) 人工核对问题设定、定理陈述和实验协议；未把 Condorcet/渐近理论外推为任意 LLM 比较流程的成本保证。
