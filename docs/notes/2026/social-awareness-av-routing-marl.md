---
title: "Autonomous Vehicles need Social Awareness to Find Optima in Multi-agent Reinforcement Learning Routing Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/FTHN6981"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FTHN6981.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02l"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["simulated_traffic_only", "marginal_cost_computation_cost", "av_routing_not_vehicle_control", "social_welfare_reward_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Autonomous Vehicles need Social Awareness to Find Optima in Multi-agent Reinforcement Learning Routing Games

## 一句话总结

论文在 MARL route-choice 仿真中把 AV 对其他道路使用者的边际旅行时间加入 reward；在两路 toy network 与 Saint-Arnoult 路网模拟中，这种社会成分比纯自利 travel-time reward 更快接近系统最优/较低旅行时间。

## 方法与证据

- 对 joint route action `u`，marginal cost matrix 的 `M_(i,j)` 是 agent j 存在与被移除时 agent i travel time 的差；j 的 reward 附加经 `tanh` 变换的其他 agents 边际 travel time，再以 β 与自身体旅行时间结合（§2、Eq. 1、Algorithm 1）。
- 作者区分 AV-group marginal（只计对 AV 的影响）和 system marginal（计 AV 与 human agents）。为每个 AV 移除后重跑环境来得到矩阵，故每个 joint action 须额外运行一次每个 AV 的模拟；TRY 中 10 agents、2 routes 时，若所有 joint actions 出现，需要 `1024×10` 额外 runs（§2）。
- TRY 中使用 UCB、MAPPO、IDQN，Figure 2 报告约 100 iterations 后 joint action 已接近最优。Saint-Arnoult/URB 中 111 agents、10 名换为 AV 的 agents 以 UCB 学 300 iterations；Table 1 报 system/AV group 的平均 travel times 在 system marginal 下最低（§3）。
- 作者的“social awareness”是特定边际拥堵 reward shaping，而非对人类社会意图、礼让、安全交互或法规遵从的感知/理解。

## 适用边界与复现

- 研究是 route selection 的 SUMO/RouteRL 仿真，不涉及车辆操控、感知、碰撞规避、乘客安全、现实路况或与人类驾驶者的部署交互；不能由此推断 autonomous vehicle safety。
- 边际矩阵靠反事实移除 agent 重跑获得，计算成本随 AV/候选 joint actions 增长；复杂网络中可能难以在线精确计算，且 reward 依赖仿真模型对需求/拥堵的保真度。
- 系统总旅行时间改善不自动解决各群体的公平、路线负担转移、隐私、可解释性或人类道路使用者的利益；β 和社会范围（AV group/system）是规范性设计选择。
- 复现需发布 RouteRL/SUMO/URB 版本、路网/OD/需求、AV/human 数量和渗透率、reward/β、边际矩阵计算、MARL hyperparameters/seeds、训练/评估时长及每群体指标；任何实地试验须独立安全验证与交通管理批准。

## 与 AAMAS 的关系与核验说明

这是交通路由场景的多智能体 reward shaping 研究。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FTHN6981.pdf) 核对 §2--3、Algorithm 1、Figure 2 和 Table 1，并将结论严格限定在仿真 route-choice。
