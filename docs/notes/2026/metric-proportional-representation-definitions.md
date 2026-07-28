---
title: "Relationships and Connections between Definitions of Metric Proportional Representation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/VKHN5660"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VKHN5660.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["definition_and_approximation_scope", "metric_pseudometric_assumptions", "no_empirical_evaluation", "algorithmic_construction_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Relationships and Connections between Definitions of Metric Proportional Representation

## 一句话总结

论文绘制 metric committee selection 中比例代表定义的蕴含图：多代表的 PRF 与 Uniform Core 在常数近似下等价，ordinal RankPJR/OPRF 蕴含 metric PRF 而反向不成立；单代表的 PFC、IF、近似 core 也在特定资源增广参数下相连。它是概念/近似保证映射，而非一个新的通用求解算法或实证比较。

## 形式结果与证据

- 问题在有限 pseudo-metric `(V∪C,d)` 上选 size-`k` committee，Hare quota 为 `n/k`；论文区分 single representation（PFC、IF、Approximate Core）和 multi representation（PRF/mPJR、q-core、PRC），并区分个体型与总距离型效用（§1–2）。
- Uniform Core 要求所有 `q` 同时满足 q-core。Theorem 4.2：`β`-PRF 蕴含 `(3β+2)`-UC；Theorem 4.3：`β`-UC 蕴含 `β`-PRF，因此是常数近似关系、不是同一参数下字面相等。文中还将这一类与 PRC 连接（§4.1）。
- 对 ordinal 定义，OPRF（RankPJR）要求共同 top-`ρ` 候选得到比例覆盖。Theorem 4.7：OPRF 蕴含 3-PRF；存在 PRF 但不满足 OPRF 的例子。ordinal EAR 满足 OPRF/RankPJR+，故经蕴含链得到多项 metric 近似保证；metric EAR 则可满足 PRF 而违反 OPRF（§4.2、表 1）。
- 单代表方面，Theorem 4.10 给 `(1,β)`-Approximate Core 蕴含 `β`-PFC；但有资源增广时，聚合距离定义可让少数人被平均掩盖，AC/PRC 可与 PFC/PRF 分离。论文明确留下 AC 的 `α∈(1,2)` 中间范围和常数紧性等开放问题（§4.3、结论）。

## 局限与复现

- 所有关系受定义细节、`β` 近似、resource augmentation `α`、coalition 阈值和 pseudo-metric（允许零距离不同点）制约；不能把“equivalent up to a constant”理解为相同 committee、相同 fairness 强度或有限常数上的可互换实现。
- ordinal 结论假定 rankings 与某个 metric 一致；从排名可得的 OPRF 并不在任意非 metric 偏好配置下自动对应距离公平。PRC/AC 的总距离指标还能补偿个体伤害，因此不替代个体覆盖保证。
- 论文主要给定理、构造性分离和对 EAR 既有算法的保证传播，不报告新算法的运行时、实例规模、近似常数紧性或真实选举/聚类数据的实证表现。
- 复现应逐项实现论文定义、包含参数 (`α,β,q,ℓ,ρ`) 的量词顺序，核验分离实例与 EAR 两变体的 tie-breaking；实际采用前还应针对应用的 metric 估计误差、候选可行性、群体权重及隐私/公平目标选择恰当定义。

## 与 AAMAS 的关系与核验说明

该文服务于计算社会选择、设施选址和公平聚类中的比例代表概念选择。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VKHN5660.pdf) 核对 Theorem 4.2、4.3、4.7、4.10 及 EAR 的范围，保留其近似参数与未解决区间。
