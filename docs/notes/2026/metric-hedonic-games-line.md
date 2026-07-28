---
title: "Metric Hedonic Games on the Line"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination"]
dblp_key: ""
doi: "10.65109/CJCT2898"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CJCT2898.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["one_dimensional_type_assumption", "distance_preference_proxy", "stability_efficiency_gap", "improvement_cycle_risk", "unbounded_price_of_anarchy", "coalition_constraint_sensitivity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Metric Hedonic Games on the Line

## 一句话总结

本文提出一维 metric hedonic games：每个 agent 有固定实数 type，联盟内成本由 type 差的 average、maximum 或 cutoff（超过阈值 \(\lambda\) 的“enemy”比例）给出，并可限制联盟数。作者证明所有所研究变体都有 jump 或 swap stable coalition structure，但不同模型的收敛性和福利质量差别很大：Avg-/Cutoff-Jump 可有 improving-response cycle，大多数设置的 Price of Anarchy 无界，而部分 PoS 为 1。它是对高度简化偏好几何的联盟形成分析，不能保证现实群体会收敛、接受或形成高福利分组。

## 方法与证据

- agents 的固定 values 排在一条实线上，距离为 \(|v_i-v_j|\)；最多允许 \(k\) 个 coalitions。Average/Maximum 分别聚合联盟内对其他成员的平均/最大距离；Cutoff 以距离大于 \(\lambda\) 的成员比例为 cost（§1.1）。因此 type 的一维顺序、绝对距离和同质性偏好是建模假设，未覆盖多维身份、互补技能、权力关系、沟通摩擦或联盟外部性。
- singleton cost 分为 happy-in-isolation（HIS，0）与 unhappy-in-isolation（UIS，\(\infty\)）；jump stability 排除单个 agent 的严格降成本跳转，swap stability 排除双方都严格改善的交换（§1.1）。稳定性不是同意、程序公平、抗胁迫、群体 welfare 或动态可达性的同义词。
- 论文定义 social cost 为全体个体成本和，并以 PoA/PoS 比较 worst/best equilibrium 和 optimum（§1.1）。若 optimum cost 为零，任何正成本 equilibrium 可使比率无界，因此无界 PoA 是该度量下的最坏情况陈述，不给出典型实例的绝对伤害或实际规模预测。
- 所有 Max-/Avg-/Cutoff-Swap games 都有 equilibrium 且具 finite improvement property（FIP）；任何 sorted coalition 在三类 swap model 中都 stable（Cor. 2.2, Thm. 2.3）。这里 sorted 指 type 在某一 coalition 的两个成员之间的 agents 也都在其中，属于一维秩序的结构性质。
- 对 Jump-UIS，grand coalition 对三种 cost 都 stable；Max-Jump 在 HIS/UIS 也有 FIP，但 Avg-Jump 与 Cutoff-Jump 存在 improving-response cycle（Obs. 3.1, Thm. 3.3）。后两者仍可用文中算法构造 jump-stable structure（Thm. 3.6）；存在 equilibrium 不表示任意 myopic best/improving-move simulation 会终止。
- Theorem 4.1：当 \(k\ge2\) 时，所有研究设置的 PoA 均无界；Cutoff 的 zero-cost optimum 构造及 Avg/Max 的实例支撑该结论（§4.1）。这否定了将局部稳定直接作为高社会质量代理的做法。
- PoS 更细：所有 Swap games 和“nice” Cutoff-Jump 的 PoS 为 1；Max-/Avg-Jump 的 PoS 大于 1，其他 Cutoff-Jump 也可大于 1（Thm. 4.6, Lem. 4.8–4.10）。PoS=1 只说明存在一个最优 stable structure，不说明非协调分散行动会选择它。
- 作者指出 Avg-Jump optimal structure 是否总可排序仍未解决，并建议考察 coalition size constraints 和更有信息量的效率界（Conclusion）。所以不能据此宣称已给出所有变体的高效算法或完整复杂度分类。

## 适用边界与复现

- 适用于分析“相似 type 的分组”这一机制，例如训练配速或一维政治位置的玩具模型；必须先验证一维 numeric embedding、distance-based cost 与联盟数限制是否是合理近似。
- 若用于人员/社群分组，不应以 agent type 距离自动决定归属。需要自愿与知情、敏感属性保护、反歧视审查、可解释的约束、退出/申诉机制及对 group-level impact 的审计；stable partition 不能替代这些治理条件。
- 复现应生成排序 values、实现三种 cost 及 HIS/UIS singleton rule，枚举或求解 stable/optimal partitions，验证 sorted structures、FIP 或论文给出的 IRC，并分别计算 social cost、PoA/PoS。应测试 ties、\(\lambda\)、\(k\)、固定 coalition sizes 与不同 improving-move scheduler。
- 后续可扩展到多维/不确定 type、network interaction、容量与技能约束、联盟外部性、机制设计和动态学习；还应评估如何选择 stable equilibrium，因 worst equilibrium 可非常低效。

## 与 AAMAS 的关系与核验说明

这是 AAMAS coalition formation/hedonic games 的理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CJCT2898.pdf) 核验了三类距离成本、HIS/UIS、jump/swap stability、FIP 与 cycle、stable-structure existence、PoA 无界及 PoS 分类；没有把一维形式稳定性写成现实社群的收敛、公平或福利保证。
