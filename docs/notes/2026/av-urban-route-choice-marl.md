---
title: "Optimizing Urban Route Choice for Autonomous Vehicles using Multi-Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["marl_coordination", "planning_scheduling", "robotics_embodied", "applications"]
dblp_key: ""
doi: "10.65109/JTZD1181"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JTZD1181.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04u"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_network_and_equilibrium_revision"
spark_consistency: "pass_after_pdf_layout_and_terra_scope_revision"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "sumo_simulation", "route_choice_marl", "nonconvergence_observation", "counterfactual_marginal_cost", "conditional_equilibrium_preservation", "linear_simulation_overhead", "no_real_world_deployment"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_convergence_equilibrium_and_social_benefit_boundary_check"
escalation_verdict: "pass_after_network_specific_and_simulation_only_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted convergence/equilibrium check; Codex PDF-layout and source reconciliation"
reviewed_at: "2026-07-29"
---

# Optimizing Urban Route Choice for Autonomous Vehicles using Multi-Agent Reinforcement Learning

## 一句话总结

本文概述 RouteRL 路线选择研究：特定 SUMO 网络中的多 AV 同步学习可能长期不收敛或出现行程时间波动，而加入逐车反事实边际成本的社会奖励可在两路线网络加快收敛，并在 Saint-Arnoult 的 UCB 实验中降低系统与 AV 群体总行程时间；这些是仿真和引用项目结果，不是现实城市的普遍因果结论。

## RouteRL 设置

- RouteRL [2] 在共享交通环境中同时建模人类驾驶车辆和 AV。AV 是 RL agents，人类驾驶者使用既有行为学习模型。
- 环境被形式化为 Agent Environment Cycle game：智能体按出发时间依次选路，每次选择交给 SUMO 微观交通模拟器，得到实现行程时间。
- 研究使用两条相交路线的简化网络、Ingolstadt 路网，以及 URB benchmark 的 Saint-Arnoult 路网。真实路网拓扑和微观模拟增强了情境复杂度，但不等于真实道路部署（§1–2，p. 3963）。

## 同步学习的不稳定性

文献 [11] 在简化网络中比较 IDQN、IPPO、ISAC、MASAC、MAPPO、VDN 和 QMIX：

- 部分算法没有达到作者定义的最优解，另一些需要大量训练迭代，作者将其换算为数年现实通勤经验；
- 改变出发时间以引入非确定性、并允许人类驾驶者响应失衡状态后，简化网络即使充分训练也未达到最优解；
- Ingolstadt 仿真中，多回合训练后仍未收敛，行程时间的波动被作者作为系统失稳迹象。

这些结果只说明所测算法、网络、随机性和训练预算下存在慢收敛或未收敛现象，不能推出 MARL 路线选择必然不收敛，也没有形成统一收敛界（§2，pp. 3963–3964）。

## 反事实边际成本奖励

文献 [12] 在自利行程时间奖励上加入 AV \(i\) 对其他参与者造成的边际成本：

\[
\mathrm{MC}_i =
\sum_j T_j(\text{\(i\) present})
-\sum_j T_j(\text{\(i\) removed}).
\]

它依赖逐车移除的模拟反事实，而不是直接观测的真实外部性（§3，p. 3964）。

### 两路线简化网络

- 使用 IDQN、MAPPO 和 UCB，作者报告社会奖励更快收敛到 system-optimal（SO）和 individually optimal solutions。
- 在该特殊网络中，SO 与个体最优解恰好重合；作者称奖励没有改变这些均衡解。该观察不能推出复杂网络中均衡一般保持。

### Saint-Arnoult 网络

- 在这个 URB 网络中，SO 与个体最优 **不重合**。
- 使用 UCB 时，加入边际成本后，总系统行程时间和 AV 群体总行程时间都下降。
- 作者还报告超过 \(50\%\) 的 AV 得到更短的个人行程时间；文中没有给出确切比例、样本量、方差或置信区间。

因此它不是所有算法、车辆或城市网络都同时受益的证据，也不能据此证明现实交通中的因果改善（§3，p. 3964）。

## 计算开销

精确计算每个 AV 的边际成本，需要每轮为每辆 AV 各运行一次移除该车的额外仿真；额外仿真次数随 AV 数量线性增加。论文没有报告实际运行时间或可承受规模，并把只为高影响车辆估计奖励作为未来降本方向（§3–4，p. 3964）。

## Karma 路线仍是未来工作

作者正在研究用非货币 Karma 拍卖和学习型竞价智能体分配路线。既有工作 [14] 报告，在其道路定价设置中，Karma 的系统行程时间可接近货币定价，并因不按收入支付能力分配而被称为更公平；公平指标及迁移范围需要回到原研究核验。

当前论文没有给出学习式 Karma 路线竞价结果，只提出在更现实交通条件下比较效率与公平的计划（§4，p. 3964）。

## 证据与归属边界

- RouteRL 框架来自 [2]；慢收敛和失稳观察来自 [11]；边际成本奖励、两网络结果和“超过 50%”来自 [12]。
- 本稿没有重现完整实验配置、训练种子、结果表、显著性检验或代码版本；正文也没有直接仓库链接和真实城市上线证据。
- SUMO、URB 和现实路网支持受控仿真，不自动提供现实外部效度。公平、鲁棒性以及人类驾驶者与 AV 长期共同适应仍需更广泛评估（pp. 3963–3965）。

## 与 AAMAS 的关系与核验说明

本文连接 MARL、traffic assignment、human–agent coexistence、counterfactual incentives 和公平资源分配。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JTZD1181.pdf) 核对 RouteRL 设置、§2 的算法与网络、§3 第 3964 页双栏中的两种网络结果及 §4 的计算开销和 Karma 状态；未把仿真观察写成现实部署或普遍收敛保证。
