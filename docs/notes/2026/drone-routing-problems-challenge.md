---
title: "Drone Routing Problems Challenge"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["planning_scheduling", "marl_coordination", "robotics_embodied", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/HXAJ9978"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HXAJ9978.pdf"
code_url: "https://drp-challenge.com/"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05o"
spark_draft_verdict: "source_grounded_with_cross_edition_resource_allocation_and_score_comparability_overreach"
spark_qa_verdict: "needs_revision_corrected_for_competition_scope_cost_layers_cross_edition_causality_topics_and_physical_safety_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["competition_not_solver_evaluation", "formal_distance_objective_differs_from_step_score", "max_steps_and_fixed_one_hundred_penalty_ambiguity", "cross_edition_comparability_not_established", "planning_vs_rl_causal_claim_not_tested", "payload_battery_and_dynamic_routing_not_formalized", "solver_and_compute_details_missing", "seeds_variance_and_confidence_intervals_missing", "collision_and_failure_breakdown_missing", "benchmark_version_pin_missing", "real_map_topology_not_physical_flight_validation", "uav_safety_and_airspace_constraints_missing"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_formal_objective_challenge_score_cross_edition_planning_rl_reproducibility_and_physical_uav_boundary_check"
escalation_verdict: "needs_revision_corrected_for_cost_metric_cross_edition_causality_motivation_reproducibility_and_deployment_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted benchmark-score and physical-UAV boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Drone Routing Problems Challenge

## 一句话总结

DRP Challenge 把多无人机配送路由表示成 real-map-derived non-grid topology 上的 MAPF-like benchmark，并以 3 张图、30 个固定实例、每实例 10 次运行的 step-based cost 排名；它是仿真竞赛规范与历史榜单，不是新 solver、真实 UAV 飞行安全或碳减排验证。

## 竞赛定位

Drone Routing Problems（DRP）研究多机 collision-free routing。该 demonstration paper 描述 competition environment、formal problem、evaluation criteria，以及 AAMAS 2024/2025 两届 top-three leaderboard（pp. 4080–4081）。

论文不是提交一个新算法，也没有进行 physical drone delivery experiment。官网为 [DRP Challenge](https://drp-challenge.com/)，稿件还提供 [demo video](https://www.dropbox.com/scl/fi/01is8ref0934h4bnsl4qn/DRPDemo.mp4?rlkey=sgogcr92bhmfz2t3fb4712u9f&st=ma3b226q&dl=0)。

## Environment 与 observability

环境不是传统 4-connected grid，而是 graph \(G=\langle V,E\rangle\)（pp. 4080–4081）：

- nodes 表示 navigable locations，并带 planar coordinates；
- edges 表示可通行连接，距离来自 real-world maps；
- drone 可位于 node，也可处于 edge 上的 continuous intermediate coordinate；
- 每个 agent 有 unique departure node 和 destination node；
- 只有当另一 drone 出现在 adjacent node 时，agent 才能检测其位置；
- 一旦进入 edge，方向必须保持到达 next node。

episode 持续到发生 collision，或所有 agents 到达各自 destination。

## Feasibility constraints

formal DRP 给出两类 collision constraints（p. 4081）：

1. 任意两机在同一时刻不能处于同一位置；
2. 两机不能同时以相反方向 traversing 同一 edge。

在 finite horizon \(T\) 下，drone \(i\) 的 trajectory 为
\(path_i=(l_i[0],\ldots,l_i[T])\)，且 \(l_i[0]=s_i\)。到达 goal 后，后续 steps 保持在 goal。

## Formal objective 与榜单评分必须分开

### Formal DRP objective

论文在 Section 2.2 用 cumulative Euclidean movement distance 定义 trajectory cost：

\[
cost(path_i)=\sum_{t=0}^{T-1}\|l_i[t+1]-l_i[t]\|_2.
\]

目标是在所有 agents/episodes 都于 horizon 结束时到达目标的约束下，最小化 aggregate movement cost（p. 4081）。

### Challenge evaluation score

Section 2.3 的实际榜单 protocol 不直接使用上述 Euclidean sum，而是：

- 三张 maps：`map_3x3`、`map_aoba01`、`map_shibuya`；
- 组合不同 drone counts 与 start–goal assignments；
- 共 30 problem instances；
- 固定配置位于不可由 participant 修改的 `problem/problems.py`；
- 每个 instance 执行 10 independent iterations 并取 average。

per-drone evaluation cost 使用：

- 成功到达时的 number of steps；
- collision 时 piecewise formula 写为 `max_steps`；
- 紧随公式的正文又说 collision 或 failure-to-reach 被赋予 fixed cost **100**。

因此可把文字规则理解为 failure penalty 设为 100，但三页稿没有单独披露 `max_steps` configuration，留下符号与固定值的呈现歧义。final score 是 30 个 instance average costs 的总和，lower is better。

## 历史榜单

Table 1 报告（p. 4081）：

| Edition | Rank | Approach | Cost | Method |
|---|---:|---|---:|---|
| 1st（AAMAS 2024） | 1st | RL | 11,902 | QMIX |
| 1st（AAMAS 2024） | 2nd | Planning | 12,014 | Improved heuristic function |
| 1st（AAMAS 2024） | 3rd | Planning | 12,220 | Priority-based search |
| 2nd（AAMAS 2025） | 1st | Planning | 10,903 | Improved CBS |
| 2nd（AAMAS 2025） | 2nd | Planning | 10,991 | Improved Dijkstra |
| 2nd（AAMAS 2025） | 3rd | Planning | 11,355.8 | Shortest path + genetic algorithm |

第一届有 8 teams，第二届有 17 teams。论文没有说明两届 map/configuration/version、hardware 或 solver budgets 是否完全相同，所以不能把 cost 降低或 team 增长直接解释为 solution quality 的受控提升。

## Planning 与 RL 的解释边界

QMIX 赢得第一届；第二届 top three 都是 planning methods。作者将其解释为：

- instances 在 map size 和 robot count 上变化；
- RL 经常需要 retraining；
- planning 可跨 graphs 和 agent counts 使用而无需额外 training。

这是对 leaderboard pattern 的解释，不是 controlled ablation。正文没有在同一 solver budget、training set、compute 和 hyperparameters 下比较 RL 与 planning 的 generalization。

## Motivation 不等 implemented constraints

Introduction 提到 payload capacity、battery life 和 dynamic routing requirements，也把 sustainable routing 与减少 logistics carbon emissions 作为应用动机（p. 4080）。

但 formal rules 和 evaluation metric 没有展开：

- battery discharge/charging；
- payload-dependent dynamics；
- wind/weather；
- no-fly zones 或 airspace regulation；
- communication loss；
- sensing uncertainty；
- vehicle dynamics 或 flight controller。

因此不能写成 challenge 已经实现这些真实配送约束，也不能由 simulator score 推出 carbon reduction。

## 证据与复现缺口

论文没有报告：

- `problem/problems.py` 与 maps 的 commit/hash/version；
- `max_steps` 的独立 configuration；
- leaderboard solver code、parameters、training data 或 convergence rules；
- hardware、compute budget、wall time、energy 或 memory；
- 10 iterations 的 seeds、variance、confidence interval 或 distribution；
- collision/failure counts 与按 instance breakdown；
- 跨 edition protocol compatibility；
- physical flight、communications、weather 或 safety test。

榜单数字说明提交在所报 protocol 下的排名，不足以比较实际部署成本、robustness 或 safety。

## Simulator 到 physical UAV 的边界

real-world-derived map distances 只提高了 topology 的现实关联，不等于真实无人机已经：

- 遵守动力学、续航、载荷和飞控限制；
- 在 sensing/communication uncertainty 下避碰；
- 通过 weather、airspace、emergency handling 或 certification；
- 完成 real delivery 或量化 emissions。

实体应用仍需 validated dynamics、hardware-in-the-loop/flight testing、communications and fail-safe design、regulatory review 和 safety case。

## 页码与核验说明

PDF 逐页核对：p. 4080 为 identity、Abstract、Introduction、Rules and Guidelines、website/demo；p. 4081 为 formal Definition、Evaluation Criteria、Table 1、Competition Results 与 Acknowledgments；p. 4082 为 References。论文没有 Future Work section。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HXAJ9978.pdf) 核对 formal objective、实际 score 与六行榜单；`reviewed` 不表示 solver superiority、cross-edition improvement 或 physical UAV safety 已经验证。
