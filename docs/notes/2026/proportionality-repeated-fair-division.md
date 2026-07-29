---
title: "Proportionality Variations in Repeated Fair Division of Indivisible Goods"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/CYZH1121"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CYZH1121.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02d"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["additive_utilities", "temporal_fairness_scope", "existence_complexity", "ef1_not_proportionality"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Proportionality Variations in Repeated Fair Division of Indivisible Goods

## 一句话总结

论文为重复分配同一批不可分物品定义按指定时间段平均满足比例性的 `S`-proportionality，并比较全局、固定长度连续窗口等变体的可满足性、计算复杂度和若干受限偏好下的正面结果。

## 方法与证据

- 实例含 n 位 agents、m 个物品、T 轮及每轮可加非负效用。Definition 1 要求：对 family `S` 中的每个轮次子集和每个 agent，其在这些轮得到的总效用至少为该时期全部物品总效用的 `1/n`（§2）。
- Global proportionality 只取 `S={[T]}`；k-consecutive proportionality 则对每个长度 k 的连续窗口都施加上述要求（Definitions 2--3）。二者不可互推：Example 2.1 分别给出只满足一种的序列。
- 对 constant valuations，Proposition 1 表明当 `T=ℓ·n` 时总存在可多项式计算、每轮 EF1 的 globally proportional 序列；相同轮次条件下亦满足 `(ℓ·n)`-consecutive proportionality。EF1 是逐轮无嫉妒至多一个物品，不能与比例性混同。
- Theorem 3.1：对任意 `T>1`，即使 constant ternary valuations，ExistGlobalProp 仍为 NP-complete。对 binary valuations，Proposition 2 在不重叠 `S`，或 constant valuations 下同长度连续窗口的 `S`，给出多项式判定/构造。
- Proposition 3 对同一 valuation scale 的 mirrored valuations，列出三个 m、n、T 整除/奇偶条件，在这些条件下可多项式构造 global proportional 且每轮 EF1 的序列；并报告实验显示变体在实践中可能比一次性比例性更常可达，但摘要没有完整实验设计和数值。

## 适用边界与复现

- 结论建立在固定 agents/物品、每轮完整分配、可加效用和预先定义的时间 family 上；不直接适用于物品到达、成员变化、预算/容量、策略行为或非可加偏好。
- 跨期平均公平可以掩盖短期严重不利，因此 global proportionality 不意味着每轮或任意短窗口公平；窗口长度和 `S` 的治理选择本身是规范性决策。
- 一般存在性困难，正面结果仅覆盖明确的轮次、binary/mirrored/constant valuation 条件；不能据此保证实际课程、轮班或设备分配一定可行。
- 复现应提供 n,m,T、每轮效用与是否恒定、S 的完整集合、分配/EF1 校验、求解器和复杂度归约或构造规则；实践实验还须公开实例生成、baselines、可满足率与短期伤害分布。

## 与 AAMAS 的关系与核验说明

这是时间维度上的计算社会选择与资源分配工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CYZH1121.pdf) 核对 Definitions 1--3、Example 2.1、Propositions 1--3 和 Theorem 3.1，并保留各正面结论的精确偏好与轮次条件。
