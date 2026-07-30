---
title: "Optimizing Voting Rules for Social Welfare and Beyond"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance", "safety_verification", "human_agent_interaction", "applications"]
dblp_key: ""
doi: "10.65109/SSLT9308"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SSLT9308.pdf"
demo_url: "https://youtu.be/v1vwvr9uC9Y"
package_url: "https://pypi.org/project/optimal-voting/"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05u"
spark_draft_verdict: "source_grounded_with_required_resource_optimality_typo_prior_evidence_and_governance_corrections"
spark_qa_verdict: "needs_revision_corrected_for_missing_web_repo_statement_malfare_psr_randomization_and_independent_evaluation_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["welfare_target_value_choice", "cardinal_utility_scale_and_elicitation", "profile_and_distribution_bias", "preflib_sampling_scope", "in_sample_overfitting", "no_global_optimality_or_convergence_proof", "score_vector_constraints_and_tie_breaking_unreported", "randomized_rule_governance", "strategic_manipulation_unstudied", "interpretability_not_fairness_or_legitimacy", "no_out_of_sample_or_robustness_evaluation", "no_reproducible_runtime_benchmark", "no_user_study", "political_review_and_recommender_high_stakes_use"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_heuristic_optimality_welfare_value_utility_scale_profile_shift_manipulation_randomization_and_high_stakes_governance_check"
escalation_verdict: "needs_revision_corrected_for_heuristic_optimality_prior_evidence_interpretability_fairness_and_collective_decision_governance_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted social-choice optimality and governance check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Optimizing Voting Rules for Social Welfare and Beyond

## 一句话总结

`optimal_voting` 用 Django 界面和 Python package 在给定 profiles、cardinal utilities 与 evaluation target 上搜索 positional scoring rule，并支持 welfare、distortion、自定义目标和随机模式；web 主流程使用 simulated annealing，论文没有全局最优、out-of-sample 稳定性或治理验证，因此“optimal”和“interpretable”不能被理解为普遍最优、公平或具民主正当性。

## 身份与公开资源

这是 AAMAS 2026 Demonstration Track 的三页工具论文，作者提供了 [视频](https://youtu.be/v1vwvr9uC9Y) 与 [`optimal_voting` PyPI package](https://pypi.org/project/optimal-voting/)（p. 4116）。

论文描述一个 Django web interface，但没有给出可访问的 web deployment URL；三页稿也没有提供 code repository link。PyPI package 是本文唯一明确给出的软件分发入口。

## Positional scoring rule

Positional scoring rule（PSR）由长度为 \(m\) 的 score vector 定义。每个 voter 把 alternative 排在第 \(i\) 位时，就给它 vector 的第 \(i\) 个分数；所有 voters 的分数相加，最高者获胜（p. 4116）。

例子：

- plurality：\((1,0,\ldots,0)\)，只给第一名一分；
- Borda：\((m-1,m-2,\ldots,0)\)，每个排名位置都有递减分数。

优化 framing 对 rule 在一组 profiles 上选出的 winners 进行 evaluation。Evaluation function 可使用 profile、utilities 与 result，例如 utilitarian social welfare 是 winning alternative 给所有 voters 的 utilities 之和。

PSR 的 score vector 比 neural voting rule 更容易检查，但“规则结构可读”不证明普通用户能理解其后果，也不证明目标、输入或赢家公平。

## Website 与 package

平台有两个组件（pp. 4116–4117）：

- **Django website**：创建、导入、分析 profiles，运行基础优化，比较 scoring vectors；
- **Python package**：支撑 web backend，并开放更多 targets、solvers 与 deterministic/probabilistic modes。

Web 提供四个 optimization targets，按论文原文为：

- `utilitarian`；
- `egalitarian`；
- `Nash`；
- `malfare`。

三页稿没有定义 `malfare` 的精确公式，本笔记保留原词而不替作者补写含义。

## Profile 与 utility 输入

每个 profile 同时包含（p. 4117）：

- 每位 voter 对 alternatives 的 ordinal ranking；
- 若每个 alternative 当选，该 voter 获得的 cardinal utility。

Ordinal profiles 可以：

- 手工创建；
- 从 Impartial Culture（IC）采样；
- 从 Mallows distribution 采样；
- 从 Single-Peaked domain 采样；
- 从 PrefLib 导入现实 preference data。

Utilities 可从若干 distributions 生成，也可手工设定。论文没有说明不同 utility scales 的 interpersonal comparability、normalization、elicitation error 或 strategic reporting 如何处理。

## Optimization 与可视化

优化可在一个或多个 profiles 上进行。Web backend 使用 simulated annealing，搜索使所选 target 在输入 profiles 上最大化的 score vector（p. 4117）。

作者称 large PrefLib collections 上数千个 annealing steps 可在 seconds 内完成，但没有给出：

- profile / voter / alternative 数量；
- hardware 与 software environment；
- annealing schedule、initialization、stopping rule 或 seed；
- repeated-run variance；
- runtime table 或 scaling curve。

因此这是一项定性性能描述，不是可复现的复杂度或吞吐保证。

Package 另外提供 gradient descent 与 mixed-integer programs。论文没有说明何时使用哪一 solver，也没有报告 global-optimality certificate、convergence guarantee 或不同 solvers 的一致性。

UI 可展示：

- classical scoring vectors 的 winner 与 normalized social welfare；
- optimized novel score vector；
- optimization history；
- alternatives 的 average score 与 average welfare。

Figure 1 把单个 profile 的 social welfare 归一化为 maximum 1；Figure 2 展示对 100 个 Mallows profiles 优化 egalitarian welfare 的界面。这些 figures 是功能示例，不构成跨分布 benchmark。

## Package 的扩展目标

Library 支持（p. 4117）：

- **Custom Optimization Targets**：用户提供给每个 winner/profile 打分的函数；
- **Distortion**：最大可能 welfare 与实际 achieved welfare 的 worst-case ratio；
- **Randomized Scoring Rules**：将 alternative score 解释为相对 winning probability；
- deterministic 与 probabilistic modes。

三页稿没有给出 score-vector 单调性、非负性、normalization、scale equivalence、tie-breaking 或 random-seed/governance 规则。不同约束会改变搜索空间与结果解释。

## 三类 use case 的证据边界

### Profile analysis

用户可比较不同 welfare functions。例如一群人选电影，并把“让最不满意者尽可能满意”定为目标，即选取 egalitarian SW 最大的 movie（p. 4117）。这是说明目标含义的 toy decision，不是 user study。

### 探索 social-welfare theory

作者称 early experiments suggest 一个优化 egalitarian SW 的 novel scoring-rule family。论文没有给 profiles、formula、sample size、solver runs、uncertainty 或 proof；该说法是早期观察。

### Custom targets 与其他项目

论文提到：

- Caiata et al. [13] 的 axiom-violation study；
- Berker et al. [6] 的 consistent ranking target；
- recommendation under fairness constraints [1]。

这些结果属于引用或其他项目。三页 demo 没有重新报告它们的完整 design、numbers、baselines 或 significance，不能把 “significantly outperforming” 改写为本稿独立复现实验。

## “Optimal”的严格边界

本文系统输出的是：在给定 input profiles、utilities、target、constraints、initialization 与 chosen solver 下找到的高分 score vector。

Web 使用 simulated annealing，而论文没有：

- global-optimality proof 或 certificate；
- convergence / approximation bound；
- exact-search comparison；
- train/test split 或 held-out profiles；
- cross-distribution/OOD evaluation；
- hyperparameter/sensitivity/robustness analysis。

所以文件名和界面中的 `optimal_voting` 是工具命名与优化目标，不足以证明返回规则是全局最优或对未来 elections 普遍最优。

## 高风险社会选择与治理边界

论文举例的应用包括 political elections、conference reviewing、recommender aggregation 与 sports scoring。若工具被用于这些场景，风险包括：

- 选择 utilitarian、egalitarian、Nash、malfare 或 custom target 本身是一项价值与权力决策；
- cardinal utilities 的尺度、生成分布或手工输入可改变结果；
- IC、Mallows、Single-Peaked 或 PrefLib 样本可能不代表目标 population；
- 在有限 profiles 上优化可能 overfit，未来 electorate 或 domain shift 下退化；
- strategic voters、agenda setters 或 operator 可操纵 rankings、utilities、target、constraints 或 sampled profiles；
- tie-breaking 与 probabilistic mode 的随机性影响可复现性、问责和公众接受；
- 一个短 score vector 容易展示，不等于受影响群体理解、同意或认为结果公平；
- 目标函数内的 aggregate welfare 不自动覆盖 minority rights、procedural fairness、legality 或 contestability。

三页稿没有 user study、deployment evaluation、manipulation analysis、appeal mechanism 或 public-governance protocol，因此风险等级为高。高风险不表示当前 demo 已造成现实伤害。

## 页码核验

PDF 逐页核对：p. 4116 为 identity、Abstract、Introduction、PSR framing、Contribution 与 web 功能起点；p. 4117 为 profiles、optimization、comparison、library functionality 与 use cases；p. 4118 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SSLT9308.pdf) 核验；`reviewed` 不表示 global optimality、out-of-sample welfare、fairness、legitimacy、manipulation resistance 或部署效果已被验证。
