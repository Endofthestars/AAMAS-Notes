---
title: "Complexity and Behaviour in Strategic Models of Elections"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["game_theory_mechanism", "argumentation_reasoning", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/ELCK5589"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ELCK5589.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05a"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_with_complexity_representation_and_empirical_boundary_check"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "worst_case_complexity", "spatial_voting", "prospect_theoretic_voting_under_review", "primary_election_games", "input_representation_conditions_omitted", "approximation_factor_omitted", "not_empirical_election_evidence", "future_seed_and_marl"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_complexity_representation_publication_status_and_political_inference_check"
escalation_verdict: "pass_after_worst_case_under_review_and_future_simulation_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted complexity-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Complexity and Behaviour in Strategic Models of Elections

## 一句话总结

这篇博士研究概述串联三条理论工作：多议题空间选位给出高维困难与固定维度精确算法，前景理论式参与模型改变候选人策略并产生表示相关的复杂度，初选—普选结构则带来更高层级的均衡与最优反应问题；这些是抽象模型中的最坏情形结果，不是现实选民行为、操纵频率或选举结果的经验预测。

## 三条研究线与证据状态

本文是三页 Doctoral Consortium 概述（pp. 3996--3998）：

1. **Spatial Voting [2]**：作者报告的既有多议题候选人选位工作；
2. **Prospect-Theoretic Voting**：稿中明确标为 `Under review`；
3. **Primary Elections [3]**：作者报告的多阶段选举复杂度工作。

§2 给出结论级摘要，没有完整定理条件、归约证明或算法伪代码。不同工作线的发表状态和证据强度不能合并成一篇已完整证明、已经验验证的统一系统。

## 多议题空间选位

### 模型

选民和候选人表示为 \(\mathbb{R}^d\) 中的点；每位选民在 \(\ell_p\)-norm 下支持距离最近的候选人（§2.1，p. 3997）。研究问题是候选人如何选择政策位置。

### 作者报告的复杂度与算法

- 即使只有一个新候选人与一个固定对手竞争，计算最优政策位置也为 NP-hard；
- 当议题数 \(d\) 固定时，作者给出 \(O(n^{d+1})\) hyperplane-enumeration 精确算法；
- 二维情形有专门的 \(O(n\log n)\) radial-sweep 精确算法；
- 对一般 multi-candidate setting，作者称得到 approximation guarantees，但本概述没有给 approximation factor、目标函数细节或适用条件；
- 同类几何技术被称可扩展到 \(k\)-approval 与 Borda 等 positional scoring rules。

“固定 \(d\) 可处理”与“一般输入下 NP-hard”针对不同参数条件，并不矛盾。上述复杂度和运行时间只在所引工作的正式输入编码、几何一般位置、数值精度等条件下才有完整含义；三页稿未列出这些条件。

## 前景理论式投票

### 参与机制与战略效应

该在审工作采用一维 Hotelling–Downs setting，把 incumbent position 作为 reference point。选民只有在“弃权带来的感知 regret”超过个人 participation cost 时才参与（§2.2，p. 3997）。

作者报告该机制通常产生 non-convex voting regions，即便 value functions 为线性也会破坏经典 Median Voter prediction。无论候选人以 vote share 还是 victory margin 为目标，对称选民分布下都可能理性选择 extreme positions。这些是模型推论，不是对真实选民心理或候选人极化原因的实证识别。

### 输入表示相关的复杂度

- voter preferences 以显式 cumulative distribution function 给出时，计算最优候选位置为 NP-complete；
- 只提供 probability density functions 时，作者报告 #P-hard；
- 有限 \(n\) 个选民、两候选设置中，作者给出 \(\tilde O(n)\) geometric sweep 求 best response；
- multi-candidate case 只概述 recursive boundary-tracking method；
- equilibrium computation 被报告有 \(\tilde O(n^4)\) 算法。

不能把 CDF 与 density 两种输入形式下的类别互换，也不能把“概述方法”写成已经在本稿给出完整算法。该工作仍是 `Under review`，这里记录的是作者在概述中报告的主张，而不是三页稿内可独立复核的正式定理包。

## 初选中的战略复杂度

§2.3 研究 primary election 后接 general election 的多阶段结构。在 first-past-the-post voting 与 fixed tie-breaking 下，作者报告：

- 决定 pure Nash equilibrium 是否存在为 \(\Sigma_2^P\)-complete；
- 计算 best response 为 NP-complete；
- sequential primary elections 中决定 subgame-perfect equilibrium 是否存在为 PSPACE-complete。

三页概述没有给出 party 数是否固定、策略/后期行为如何编码、阶段数量、参与规则和输入规模等完整条件，因而不能脱离完整论文把这些类别泛化到所有初选制度。仓库已有 [The Complexity of Strategic Behavior in Primary Elections](./complexity-strategic-behavior-primary-elections.md) 的独立全文笔记，专门记录表示方式、阶段和参与假设；该链接是导航，不把全文细节冒充为本概述自身的披露。

## 复杂度不等于现实政治预测

NP-hard、NP-complete、#P-hard、\(\Sigma_2^P\)-complete 与 PSPACE-complete 描述的是规定输入表示下的 worst-case exact computation。它们不表示：

- 每位真实选民都会或需要求解相应问题；
- 战略投票或操纵在现实中必然频繁；
- 某次选举一定不存在均衡或会产生特定结果；
- 某种初选、投票规则或候选位置在规范意义上更好或更坏。

固定维度、少量政党、结构化偏好、近似算法、启发式或制度约束都可能改变实际可计算性。本文也没有真实选举数据、行为实验、民调拟合或因果评估。

## 持续与未来工作

§3（p. 3997）计划把 primaries 视为 Multi-Stage Games with Selection and External Decisions（SEED），并研究：

1. 在 candidate viability 与下游 general-election outcome 不确定时的 voter decision-making；
2. factions / interest groups 等 coordinated voting blocs 对均衡存在与结构的影响；
3. 两阶段结构如何改变 Hotelling–Downs 等 spatial model 中的 candidate positioning；
4. 用 MARL 模拟 SEED 环境中的 boundedly rational agents，以探索解析均衡难以获得时的动态。

这些都是待开展的研究问题。当前稿没有 SEED 算法、MARL 环境、训练结果，也没有“仿真已验证理论预测”的证据。

## 复现边界与 AAMAS 关系

三页稿缺少完整实例编码、数值精度、定理条件、归约、近似比、伪代码和证明；理论复核需要回到各工作线的完整版本。其 AAMAS 价值在于把 computational social choice、algorithmic game theory、bounded rationality 与 multi-stage agent interaction 放到统一研究议程中。

本笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ELCK5589.pdf) 核对 §1--3 的复杂度类别、运行时间、在审状态和未来计划，并保持理论模型与现实政治推断之间的边界。
