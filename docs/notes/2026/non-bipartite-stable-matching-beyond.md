---
title: "Non-Bipartite Stable Matching and Beyond"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/SLTP2592"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SLTP2592.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04x"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_popularity_complexity_and_experiment_scope_revision"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "non_bipartite_stable_matching", "minimax_almost_stability", "designated_deviators", "capacity_near_feasibility", "justified_envy_freeness", "popular_matching", "complexity_scope", "random_simulation_scope"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_matching_complexity_fairness_and_empirical_scope_check"
escalation_verdict: "pass_after_exact_jef_popularity_and_capacity_modification_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted matching-theory boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Non-Bipartite Stable Matching and Beyond

## 一句话总结

本文把博士研究组织为三条相连路线：用 stable partitions 描述非二分匹配的不稳定结构，以 minimax 和指定偏离者目标控制 almost-stability，再通过容量修改研究多对多 near-feasibility；复杂性和算法结论均依赖具体模型，而“移除 1%”“随机偏好下 likely”“平均只需少量修改”只是概述转述的实验观察，不是任意市场保证。

## 基础问题：稳定匹配可能不存在

在二分市场中，两类参与者相互匹配；非二分市场则让同一类型的 agents 或资源彼此配对，如伙伴匹配、donor–recipient pairs 之间的交换或其他 peer-to-peer 市场。稳定性要求不存在一对 agents，使双方都愿意相互匹配而放弃当前 partner，或在有空余容量时形成有利偏离（§1，p. 3978）。

非二分一对一问题即使具有严格、完整偏好列表，也可能没有稳定匹配。Irving 的高效算法是在稳定匹配**存在时**找到一个，并不保证所有实例都存在稳定解（§2，p. 3978）。

## 一对一：结构、almost-stability 与指定偏离者

### Stable partitions

Tan 的 stable partition 描述导致稳定匹配不存在的偏好结构。作者与 Manlove 的工作 [17,24] 进一步刻画 stable/unstable structures，并联系 fair stable half-integral matchings；[18] 研究不稳定结构出现的可能性和规模（§2，p. 3978）。

[18] 的综合模拟报告，例如从实例中移除 \(1\%\) agents 通常会使稳定匹配存在。三页稿没有给实例分布、规模、重复次数、置信区间或删除规则，因此这里只能视为该模拟设置中的趋势，不能推成最坏情形或真实市场保证。

### Minimax almost-stability

传统 aggregate 指标最小化总 blocking pairs 或至少参与一个 blocking pair 的 agents 数量，但可能把大量不稳定集中在少数人身上。[21] 改为最小化任一 agent 所参与 blocking pairs 的最大数，以控制最坏个体负担（§2，pp. 3978–3979）。

- 判定是否存在一个 matching，使每位 agent 至多参与一个 blocking pair，是 `NP-complete`；
- 当偏好列表非常短时，作者给出高效算法；
- 后续 [22] 给出高效近似算法和基于 ILP 的算法；
- [22] 的实验报告，在 **uniformly random preferences** 下，minimax 意义上较均衡的 almost-stable matching 很可能存在。

最后一项是指定随机偏好模型下的实验观察；本概述没有算法近似比、ILP 设置、实例规模、重复次数或统计不确定性。

### 指定偏离者集合 \(D\)

[21] 及后续 [23] 还假设只有指定集合 \(D\) 中的 agents 能够发起 blocking-pair deviation，并问是否存在一个 matching，使 \(D\) 中无人有发起偏离的动机。概述称即使在强限制下，该问题一般仍不能高效求解（除非 \(P=NP\)），但提供参数化算法以及偏好列表很短时的多项式算法（§2，p. 3979）。

这不是关于现实中谁“会”偏离的因果模型，而是一项把可行动偏离者作为输入的规范性和算法性假设。

## 多对多：stable partitions 与 near-feasibility

多对多模型为每位 agent 设置整数容量。Irving–Scott 把“存在时寻找稳定匹配”的算法扩展到此设置，Fleiner 给出到一对一问题的归约。作者与 Manlove 的 [19,20]：

- 在多对多非二分设置中定义 stable partitions；
- 紧密刻画 stable 与 unstable preference structures；
- 通过修改少数 agents 的容量，把原实例转为可接受稳定匹配的实例（§3，p. 3979）。

Glitzner 的 [15,16] 把 almost-stability 与容量修改的 near-feasibility 放入统一框架。概述声称，在**允许容量修改**的模型内，同时最小化 capacity extensions 与 agents 的偏离激励，并兼顾个体和 aggregate 层面，可以多项式时间求解。该结果不意味着禁止容量修改的普通 almost-stable matching 一般也可多项式求解。

作者另报告平均只需“very few”容量修改即可获得有稳定匹配的实例。三页稿未说明实验分布、样本量、“few”的数值或不确定性，因此这是平均实验现象，而非任意实例的容量上界。

## 持续方向一：justified envy-freeness

在二分一对一匹配中，稳定性与 justified envy-freeness 加 non-wastefulness 等价。多对多时不再有同样等价关系；当允许 ties 且采用某些偏好规则时，**精确** justified-envy-free matching 甚至可能不存在，但 [28] 表明近似版本仍存在（§4，p. 3979）。

作者在非二分多对多模型中的 preliminary result 仅是：

- 严格偏好下，stable matching 必然 justified envy-free；
- 逆命题不成立，所以某些没有稳定匹配的实例仍可能有 justified-envy-free matching。

是否能多项式时间判断 justified-envy-free matching 的存在，以及保证何种近似，是尚未解决的问题，不能写成已完成算法或普遍存在定理。

## 持续方向二：popular matchings

Popular matching 在与任何其他 matching 的 head-to-head election 中都不落败，因此是 weak Condorcet winner。严格偏好下 stable matching 必然 popular，但逆命题一般不成立，所以 popular matching 可能在稳定匹配不存在时仍存在（§4，p. 3979）。

- 在 Stable Roommates 中，判断 popular matching 是否存在是 `NP-complete`；
- [8] 只在**二分设置**中报告 popular matching 相对 stable matching 可显著增加规模而不引入太多不稳定性；
- 把这一研究扩展到非二分设置的快速指数时间或参数化算法，是未来工作。

## 证据、归属与复现边界

- 当前三页稿综合作者及合作者的 [15]–[24]，没有逐项重给完整证明；复杂性和算法结论应回到相应完整论文复核。
- `typically`、`likely`、`on average` 分别对应模拟、uniformly random preferences 和未详述的平均实验，不能互相替换或外推到现实偏好。
- 概述没有代码、实例、生成器、随机种子、运行时间、完整 ILP、统计表或置信区间。
- 稳定性、blocking-pair count、JEF 与 popularity 是匹配模型内的性质，不自动等同于现实公平、福利、法律合规、可接受性或策略真实性。

仓库内已有相关完整 AAMAS 工作的独立笔记：[Minimax and Preferential Almost-Stable Matchings](./minimax-preferential-almost-stable-matchings.md) 与 [Near-Feasible Stable Matchings: Incentives and Optimality](./near-feasible-stable-matchings.md)；本笔记只总结博士研究概述如何连接这些路线。

## 与 AAMAS 的关系与核验说明

本文连接 matching theory、multi-agent resource allocation、algorithmic fairness、parameterized complexity 与 computational social choice。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SLTP2592.pdf) 核对一对一/多对多结构、minimax 与指定偏离者复杂性、允许容量修改时的多项式结果、JEF 初步结论以及 popularity 的二分/非二分边界。
