---
title: "Automated Negotiation and Multimodal Time-Series Forecasting for Efficient Procurement"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["game_theory_mechanism", "planning_scheduling", "resource_allocation", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/VKYZ9649"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VKYZ9649.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05k"
spark_draft_verdict: "needs_revision_after_source_access_table_column_and_comparison_errors"
spark_qa_verdict: "needs_revision_corrected_for_full_table_strategy_attribution_and_procurement_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["procurement_financial_decision_support", "simulation_not_enterprise_deployment", "timecap_prior_work_boundary", "rl_method_vs_time_based_evaluation_mismatch", "inventory_reduction_only_metric", "oracle_perfect_demand_reference", "synthetic_indirect_business_model", "dataset_split_and_run_count_missing", "no_variance_or_significance", "supplier_behavior_under_specified", "no_cost_service_quality_or_failure_evaluation", "no_autonomous_purchase_authority"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_full_table_strategy_attribution_prior_work_percentage_point_and_real_procurement_risk_check"
escalation_verdict: "pass_after_table_columns_rl_evaluation_timecap_oracle_and_deployment_boundary_corrections"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted procurement-risk check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Automated Negotiation and Multimodal Time-Series Forecasting for Efficient Procurement

## 一句话总结

这篇 demo 把 multimodal demand forecasting、business model、procurement plan、utility construction 与 bilateral automated negotiation 串成 DDA pipeline，并在 simulation 中报告较高 inventory reduction；但 Table 1 实际使用 NegMAS time-based strategy 而非方法段所称 RL negotiator，且缺少运行次数、统计不确定性和真实供应商/企业验证，不能据此承诺现实库存、成本或自主采购效果。

## Delivery Date Adjustment 与谈判模型

论文聚焦 Delivery Date Adjustment（DDA）：采购方与 suppliers 短期协商 delivery dates，使到货更贴合 demand、减少 carried inventory（p. 4059）。

negotiation scenario 写为 \(\lambda=(A,D)\)，其中：

- \(A\) 是 negotiators；
- \(D=(\Omega,U)\)；
- \(\Omega\) 是 possible agreements；
- \(\phi\notin\Omega\) 表示 disagreement，\(\Omega^+=\Omega\cup\{\phi\}\)；
- 每个 \(u_i:\Omega^+\rightarrow[0,1]\) 是 agent \(i\) 的 utility；
- each agent 知道自己的 utility，不知道 opponents’ utilities；
- time pressure 可用 discount factor 或 rounds/seconds limit 表示。

本文采用 bilateral Alternating Offers Protocol：agents 交替提出 offers，直到 accept、某 agent 离开，或 timeout 导致 failure（pp. 4059–4060）。

## Forecast-to-negotiation pipeline

系统是 sequential pipeline：

1. historical time-series 与 news/social-media/text 等 supporting modalities 输入 forecasting module；
2. forecast 得到 future demand 等 procurement-plan control variables；
3. business model 把预测转成 procurement plan；
4. delivery schedule 与该 plan 的 similarity 被用作 negotiation utility；
5. automated negotiation 调整 delivery dates 和 quantities。

作者称换新 application 时主要需要替换 business-model stage，但三页稿只评估当前 case studies，未验证这种 portability。

## Multimodal forecasting 的既有工作边界

论文给出 \(M\)-modal observation、forecast horizon 与 MSE training objective，并描述：

- trend/seasonal decomposition；
- sample-wise 与 feature-wise multimodal augmentation；
- component-specific decoders；
- cross-modal fusion。

这些 forecasting components、Figure 2 和详细方法明确指向引用 [4] TimeCAP（p. 4060）。本 demo 的主要贡献应理解为把既有 forecasting approach 集成进 procurement/negotiation pipeline，而不是重新提出并完整验证一个新的 forecasting architecture。

三页稿也没有独立报告 MAE、MSE、MAPE 等 out-of-sample forecasting metric。

## RL 方法陈述与实际 evaluation 不一致

方法段说 “we trained an RL-based negotiator [10] for DDA”（p. 4060）。但 Evaluation 明确说 negotiations 使用 NegMAS [7] 中实现的 time-based strategy [6]。

因此 Table 1 是当前 time-based-strategy simulation 的 system-level comparison，不能归因于 RL negotiator，也不能声称 RL training 带来了表中 inventory reduction。论文没有给 RL state/action/reward、training runs、hyperparameters 或 RL-vs-time-based comparison。

## Evaluation 设置

### Direct use case

第一种 trading scenario 中，buyer 从 suppliers 购买 product，再直接卖给 customers，business-modeling phase 被称为 trivial。实验使用引用 [4] 的 datasets；论文摘要称 simulations based on real-world data，但三页稿未给 dataset sizes、splits 或说明这些 series 如何映射成真实 procurement orders。

### Indirect use case

第二种 case 使用 synthetic business model，含 20 个 factors，例如 energy prices、metal prices、ICT stocks、bitcoin 和 Covid incidents。它测试多个 variables 共同影响 procurement plan 的设置，不是真实企业 procurement deployment。

## 完整 inventory-reduction 结果

Table 1 的列为 `Oracle | Negotiation | +Forecasting | +Multimodal`；`+Forecasting` 使用 DLinear [11]，Oracle 使用 perfect demand knowledge（p. 4060）：

| Product | Oracle | Negotiation | +Forecasting | +Multimodal |
|---|---:|---:|---:|---:|
| Petroleum | 31% | 10% | 10% | 24% |
| Gold | 17% | 8% | 8% | 17% |
| Gas | 34% | 10% | 19% | 29% |
| Silver | 20% | 8% | 16% | 20% |
| Indirect | 23% | 8% | 12% | 23% |

在 Indirect row，Negotiation 的 8% 到 +Multimodal 的 23% 是 **+15 percentage points**；相对增幅为另一种计算，不能称作“仅提升 15%”。Gold、Silver 与 Indirect 的 +Multimodal 数值等于 Oracle，Petroleum/Gas 仍低于 Oracle。

Oracle 是不可直接取得的 perfect-demand reference，不是现实 forecasting system 或可部署方案。

## 结果能说明什么

表格支持在这组 simulation cases 中，multimodal pipeline 相比 Negotiation-only：

- 四个 direct products 的 inventory reduction 均不低于 Negotiation；
- Petroleum、Gold、Gas、Silver 分别高 14、9、19、12 percentage points；
- synthetic Indirect case 高 15 percentage points；
- 相比 DLinear，Petroleum、Gold、Gas、Silver、Indirect 分别高 14、9、10、4、11 percentage points。

这些是表内 arithmetic，不提供 statistical uncertainty。没有 run count 或 distribution 时，不能判定差异稳定性或显著性。

## 证据缺口

三页稿没有给出：

- [4] datasets 的具体 selection、sample size、split、forecast horizon 与 preprocessing；
- negotiation count、random seeds、repetitions、variance、confidence interval 或 significance；
- inventory-reduction baseline/denominator 的完整计算公式；
- outcome space、offer representation、reservation utility、deadline 与 opponent strategy 的实际参数；
- procurement-plan/business-model 的方程和 20-factor weights；
- supplier capacity、strategic response、delivery failure、quality、contract terms 或 renegotiation；
- total cost、lead time、service level、stockout、waste、risk 或 fairness metrics；
- forecast error 到 negotiation outcome 的 sensitivity analysis；
- code、config、data mapping 与 end-to-end reproducibility package。

## 现实采购风险边界

simulation inventory reduction 不能直接外推为：

- 真实企业 ROI、cost saving 或 inventory guarantee；
- supplier 会接受 proposals；
- delivery timeliness、quality 或 continuity 不受损；
- news/social-media signal 在 distribution shift 下可靠；
- business model/utility 已包含法律、合同、合规与供应链风险；
- system 可自动签约、下单、改交期或动用预算。

实际 procurement 仍需 data provenance、forecast uncertainty、supplier/contract constraints、approval limits、human review、audit log、rollback、segregation of duties 和异常处理。Oracle matching 也不能成为放权依据。

## 页码与核验说明

PDF 逐页核对：p. 4059 为 abstract、application domain、DDA 与 AOP/formal negotiation 开端；p. 4060 为 negotiation continuation、multimodal forecasting、system architecture、Table 1 与 Evaluation；p. 4061 仅为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VKYZ9649.pdf) 核对完整表格、prior-work attribution、strategy mismatch 和 procurement-risk boundary；`reviewed` 不表示系统已在真实采购中验证，也不授予 autonomous purchase authority。
