---
title: "The Maritime Shipping Competition (MSC) 2025: Efficient Maritime Cargo Bidding and Transport Scheduling"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["game_theory_mechanism", "resource_allocation", "planning_scheduling", "agent_engineering", "marl_coordination", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/YCVT1762"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YCVT1762.pdf"
code_url: "https://github.com/jbuerman/mable"
demo_url: "https://youtu.be/zgEUSaJccPw"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06e"
spark_draft_verdict: "competition_results_require_reproducibility_real_world_and_emissions_boundary_revision"
spark_qa_verdict: "needs_revision_preserve_exact_table_rank_distinction_and_mable_not_full_competition_reproducibility"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["sample_unit_tournament_count_and_seeds_unreported", "mean_std_without_significance_or_confidence_interval", "approximate_medians", "table_income_not_complete_average_rank_record", "top_three_only_without_full_scenario_breakdown", "mable_source_not_submitted_agent_reproducibility", "ais_based_simulation_not_real_shipping_operations", "robustness_author_claim_without_breakdown", "no_emissions_outcome_or_decarbonization_evidence", "compute_budget_agent_config_and_data_version_unreported", "market_collusion_fairness_contract_and_regulatory_boundaries_unvalidated", "large_income_variability_and_penalty_tradeoff"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_table_rank_sample_unit_reproducibility_robustness_real_shipping_decarbonization_market_fairness_and_contract_governance_check"
escalation_verdict: "insufficient_reproducibility_and_robustness_evidence"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted competition-statistics, reproducibility, and real-world-claim check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# The Maritime Shipping Competition (MSC) 2025

## 一句话总结

MSC 2025 让 shipping-company agents 在 MABLE 的 sequential reverse second-price auctions 中竞标 cargo，再为 9-vessel fleets 排程；冠军取得 £105,000 average income，但标准差 £123,000，论文未报告样本单位、tournament 数、seeds 或完整 rank breakdown。结果是 AIS-based simulator 中的 competition evidence，不是现实合同收益、统计鲁棒性或 decarbonization 证明。

## MABLE 与竞赛任务

[MABLE](https://github.com/jbuerman/mable) 是 Python Maritime Agent-Based Logistics Emulator，模拟没有固定 schedule 的 tramp-trade market。用户定义 ports、shipping companies 与 homogeneous continuous cargo market，例如 crude oil；simulator 随机生成 cargo opportunities。Cargo generation 与 travel times 基于 real-world AIS movement data of large crude-oil vessels。

每个 agent：

1. 在 recurring sequential reverse second-price（Vickrey）auctions 中决定 cargo bid；
2. 为赢得的 cargo 选择 vessel、route 和 schedule；
3. 在 future cargo 和 competitor behavior 不完整的条件下管理 uncertainty。

论文提供 [演示视频](https://youtu.be/zgEUSaJccPw)。MABLE source 可用不等于 competition 完整复现：参赛 agents、submission configs、data snapshot、random seeds 与 tournament commands 没有在三页稿中给出。

## Tournament design

每个 scenario 模拟 two years of operations，monthly auctions，cargo opportunities 等于 competitors 数量的 9 倍；每个 company 管理 9 vessels。

按论文原值，三种 vessel types 为：

- Suezmax：80,000–120,000 DWT；
- Aframax：约 160,000 DWT；
- VLCC：超过 250,000 DWT。

六个 scenarios：

1. Balanced Fleet：3 Suezmax、3 Aframax、3 VLCC；
2. Small Vessels Fleet：9 Suezmax；
3. Medium Vessels Fleet：9 Aframax；
4. Large Vessels Fleet：9 VLCC；
5. One Big Fleet：一家公司 9 VLCC，其余 9 Suezmax；
6. One Small Fleet：一家公司 9 Suezmax，其余 9 VLCC。

两个 heterogeneous scenarios 做 rotation，使每个 agent 恰好操作一次每种 fleet composition。

Income 定义为 contract revenue 减 fuel costs，再减 unfulfilled-delivery penalties。每个 scenario 内按 income 排名，overall ranking 是 across tournaments 的 average rank。

## Table 1 精确结果

Table 1 标题是 “Top teams and performance metrics”，没有 rank column：

| Team | Avg Income (£) | Median Income (£) | Avg Penalty (£) |
|---|---:|---:|---:|
| Mai et al. | 105,000 ± 123,000 | ∼51,000 | 8,000 ± 5,000 |
| Gaskins and Brue | −93,000 ± 135,000 | ∼−43,000 | 0 |
| Flavin et al. | −663,000 ± 598,000 | ∼−272,000 | 338,000 ± 150,000 |

`±` 的 sample unit、样本数和具体计算口径未报告；不能自行称为 standard error、confidence interval，或从它完成 significance comparison。Median 带 `∼`，应保持为 approximate value。

Table 1 是收入/罚金汇总，不是各 scenario rank sequence 或 overall average-rank table。论文也没有给全体参赛 agents 的成绩。

## 三支获奖队伍

- **Winner / Most Interesting Strategy**：multi-start minimum-cost insertion scheduling 加 robust bidding。Auction 前估计 potential cargo cost，用 offline-optimized threshold 优先选择可形成高效路线的 bid；auction 后把 won trades 插入 schedules。它接受小 penalties 以获取 high-value contracts，换来更高 income。论文称其 “proved highly resilient under uncertainty”，但没有单独 robustness protocol 或 breakdown。
- **Runner-up**：genetic algorithm 演化 feasible vessel routes，用 Shapley values 估计每项 trade 对 overall cost 的边际贡献并定 bid。它避免 penalties，但 income 较低。
- **Third place**：simulated annealing 调整 trade allocation 与 route configuration，以 travel cost/route efficiency 为 fitness focus；论文称在 strict scheduling constraints 下仍有挑战。

奖金为 winner £500、runner-up £300、third £100，Most Interesting Strategy 另 £100。

## 评测与复现缺口

三页稿未报告：

- entrants 总数、several tournaments 的具体数量；
- scenario/tournament repeats、random seeds 和 random generator；
- cargo/AIS dataset snapshot、ports/market configuration；
- agent submission code、versions、parameters 和 failure handling；
- hardware、compute/time budget 与公平资源限制；
- per-scenario income/rank、overall rank values 与全体 leaderboard；
- statistical test、confidence interval、sensitivity 或 worst case；
- invalid schedule、unfulfilled trade 和 runtime failure taxonomy。

冠军 “highly resilient”是作者的 competition summary，不是经过独立 perturbation、sensitivity、adversarial 或 significance analysis 的 robustness 结论。

## 现实航运、市场与减排边界

AIS-derived generation/travel data 提高了 simulator context 的现实关联，但不等于 real shipping company deployment。论文没有验证：

- live cargo/port/weather/geopolitical dynamics；
- contract/legal enforceability、charter terms、insurance 与 human operations；
- market manipulation、collusion、strategic identity 或 auction compliance；
- competitor adaptation、公平性与 distribution shift；
- route feasibility、port capacity、maintenance、crew 和 maritime safety；
- operational emissions、fuel type、carbon price 或 lifecycle impact。

MABLE 可记录 extendable economic/environmental metrics，但本文 Table 1 只报告 income 和 penalties；没有 emissions result。因此 “inform industrial practices”与 “support decarbonisation goals”属于动机/作者展望，不能转写为已测减排效果。

这些是未验证/未报告边界，不是发生市场操纵、安全事故或环境违规的证据。

## 页码核验

- p. 4179：题名、作者、摘要、背景、MABLE、competition objectives 与资源；
- p. 4180：Table 1、auction/scheduling tasks、奖金、tournament design、六 scenarios、三队策略和结论；
- p. 4181：致谢与参考文献，没有新增结果。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YCVT1762.pdf) 核验；`reviewed` 不表示 full leaderboard、statistical robustness、real shipping profitability、market governance 或 emissions reduction 已得到验证。
