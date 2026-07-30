---
title: "EVMapSim: A Network-level Electric Vehicle Charging Simulator"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["planning_scheduling", "resource_allocation", "agent_engineering", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/WOKO4552"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WOKO4552.pdf"
demo_url: "https://www.youtube.com/watch?v=MTlZAShsqrE"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05q"
spark_draft_verdict: "needs_revision_for_figure_transcription_risk_taxonomy_uncertainty_and_policy_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_figure_columns_aggregate_scale_anxiety_proxy_upper_series_page_map_taxonomy_and_external_validity"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["simulation_not_field_validation", "one_minus_soc_not_psychological_anxiety_measure", "figure_upper_series_undefined", "uncertainty_intervals_and_significance_tests_missing", "aggregate_one_hundred_thousand_not_single_run_scale", "real_journey_queue_outage_repair_and_driver_validation_missing", "distance_graph_omits_traffic_congestion", "grid_price_weather_and_emissions_not_modelled", "parameter_sensitivity_unreported", "station_data_freshness_and_coverage_unreported", "failure_correlation_unmodelled", "wait_time_and_route_deviation_numeric_results_unreported", "policy_and_reliability_standard_external_validity_gap", "future_rl_and_coordination_not_current_capabilities"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_figure_transcription_anxiety_proxy_uncertainty_external_validation_infrastructure_safety_policy_and_future_capability_boundary_check"
escalation_verdict: "needs_revision_corrected_for_aggregate_results_proxy_metric_uncertainty_taxonomy_external_validity_and_policy_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted simulation-evidence and infrastructure-policy boundary check; Codex source and figure reconciliation"
reviewed_at: "2026-07-30"
---

# EVMapSim: A Network-level Electric Vehicle Charging Simulator

## 一句话总结

EVMapSim 用 SimPy 在 344-node UK road abstraction 上模拟 10,000 辆 EV 的导航、排队与充电，并比较正常、10% 随机故障和 10% targeted hub failures；图中 targeted scenario 的 stranded count 最高，但结果来自模型，`1−SoC` 只是 anxiety proxy，不能直接证明真实英国驾驶者心理、充电网络可靠性或政策效果。

## Simulator 定位

EVMapSim 是 UK-level discrete-event, agent-based charging simulator 与 demo，不是 field study、实时运营系统或已部署的 infrastructure policy tool（pp. 4095–4096）。

每辆 EV 是 shared charging-resource environment 中的 autonomous agent，独立作 navigation 与 charging decisions。当前实现不是 RL，也没有实现 multi-agent coordination mechanism；RL agents 与 shared station-availability coordination 都列在 Future Work。

## Network 与 charging data

simulator 使用 ONS geographic data 构建 UK road abstraction（p. 4095）：

- 344 wards 表示 graph nodes；
- edges 按距离加权；
- OpenChargeMap 的 27,423 charging points 分配到 nearest nodes；
- station attributes 包括 connector types、power 与 capacity。

这是一种 ward-level distance graph，不是逐道路、实时交通网络。论文没有说明 OpenChargeMap snapshot date、coverage bias、deduplication、operational-status history 或与真实站点清单的 validation。

## Vehicle population 与行为

SimPy engine 在 24-hour demand distribution 中生成 heterogeneous vehicles（p. 4096），随机化：

- origin–destination；
- initial State-of-Charge（SoC）；
- battery capacity；
- patience threshold；
- connector type，按 UK distribution。

vehicle behavior 是：

1. 使用 shortest-path routing；
2. 当 SoC 达到 threshold 时寻找 station；
3. station selection 考虑 queue length、wait time、charger power 与 route deviation；
4. 到达 station 后才发现 actual equipment status；
5. charging duration 根据 battery capacity、SoC 与 efficiency 计算。

论文称 charging duration 基于 realistic physics models，但三页稿没有给出方程、参数或与实际 charging curve 的 validation。

## 运行性能

一次 10,000-EV simulation 在 14-core CPU、16 GB RAM 的机器上约 8 分钟完成（p. 4096）。

该数字只支持这一个披露配置。它不能自动外推到更大网络、不同 hardware、real-time service latency 或多用户并发。

## 三种 failure scenarios

EVMapSim 比较（p. 4096）：

1. **All Working**：所有 charging points operational；
2. **Random Failure**：10% charging points uniformly random failure；
3. **Targeted Failure**：按 betweenness centrality 选择 high-traffic hubs，停用其中 10%。

当前描述把 failure 设置为场景条件，没有展开 failure duration、repair process、crew/resource allocation、intermittent faults 或时空相关 outages。

## Figure 2：精确结果

Figure 2 使用 24-hour simulation、每次 10,000 vehicles、10 个不同 seeds 的 runs（p. 4096）。图内表格逐像核对如下：

| Scenario | Spawned | Stranded | Mean Anx. | Max Anx. |
|---|---:|---:|---:|---:|
| All Working | 100,000 | 652 | 0.446 | 0.505 |
| Random Failure | 100,000 | 1,001 | 0.452 | 0.510 |
| Targeted Failure | 100,000 | 3,088 | 0.477 | 0.585 |

每个 scenario 的 `100,000` 是 `10 runs × 10,000 vehicles` 的 aggregate spawned count，不是单次仿真规模，也不是 stranded count。

在该模拟设定下，targeted failures 的 stranded、mean anxiety 和 max anxiety 都最高，random failures 居中。All Working 也有 652 个 stranded vehicles，说明 stranding 并不只由注入的 charger failure 产生。

## Anxiety metric 与统计边界

论文定义：

\[
Anxiety = 1 - SoC.
\]

作者明确称其为 simple anxiety proxy。它是 battery-state indicator，不是经过本文验证的心理量表，不能被解释为真实 driver self-reported anxiety、clinical anxiety 或 adoption intent。

Figure 2 legend 还包含 `All Working - Upper`、`Random Failures - Upper` 和 `Targeted Failures - Upper` series，但正文没有定义 `Upper`。因此不能把它自行解释为 confidence interval、standard deviation、maximum 或 statistical bound。

论文披露 10 个 seeds，但没有报告：

- per-run values 或 variance；
- confidence/credible intervals；
- significance test；
- effect-size uncertainty；
- sensitivity analysis。

正文说 simulator 可分析 wait time、route deviations 与 stranding risk，但三页稿没有给出 wait time 或 route-deviation 的数值表。

## External-validity 缺口

Figure 2 是 simulator output。三页稿没有用真实运营数据验证：

- journey completion、queues 或 driver station choice；
- outage frequency、duration 与 repair time；
- initial SoC、patience、battery 和 demand distributions；
- charger status chronology 或 correlated failures；
- road congestion、time-dependent travel time 与 incidents；
- electricity-grid constraints、energy price、charging incentives；
- weather-driven range loss 或 emissions。

它也没有系统扫描 failure rate、vehicle demand、battery capacity、station capacity 等参数。因此 targeted-vs-random pattern 不能直接外推为真实 UK causal effect。

## Policy 与 safety 边界

作者把 EVMapSim 定位为 infrastructure planners、policymakers 和 coordination researchers 的 experimental platform，并说结果可为 resilience planning 与 reliability standards 提供 evidence。

这里的 evidence 应限定为模型内 scenario comparison。制定真实标准还需要：

- verified station and traffic data；
- calibrated driver/vehicle behavior；
- grid、repair 和 operational constraints；
- distributional impacts 与 accessibility；
- uncertainty、stress testing 与 independent validation。

simulated stranding 是 mobility/safety-relevant outcome，但本文没有证明实际 stranding rate、应急响应效果或合规阈值。

## UI 与 Future Work

interface 提供 real-time map 与 analytics（p. 4096）：

- vehicles 按 SoC color-coded；
- status bar 显示 active、driving、charging、completed、stranded counts；
- hover 显示 individual SoC、origin、destination 与 personal charging threshold。

Future Work 包括：

- 适配其他国家的 charging/geographic datasets；
- 加入应对 outages 与 weather-driven range loss 的 RL agents；
- 通过 shared station availability 研究 multi-agent coordination；
- 比较 charging incentive schemes。

这些都不是当前 paper 已实现或评估的能力。

## 资源与页码核验

论文提供 [demo video](https://www.youtube.com/watch?v=MTlZAShsqrE)，但三页稿没有给出 code repository。

PDF 逐页核对：p. 4095 为 identity、Abstract、Introduction and Background 与 System Components 起始；p. 4096 为 Figure 1、Simulation Engine、Driver Behaviour and Charging、Failure Scenarios、Figure 2、Visualisation、Conclusions/Future Work 与 Acknowledgments；p. 4097 为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WOKO4552.pdf) 核验，Figure 2 的 rasterized table 另做视觉逐项转录；`reviewed` 不表示真实 UK anxiety、charger reliability、stranding risk 或 policy effect 已经验证。
