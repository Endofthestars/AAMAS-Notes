---
title: "MASPY: A Python Framework for Developing BDI Agents with Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["agent_engineering", "planning_scheduling", "marl_coordination", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/YIGW5980"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YIGW5980.pdf"
code_url: "https://github.com/laca-is/MASPY/wiki/Navigation-on-2D-Grid/"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05n"
spark_draft_verdict: "source_grounded_with_figure_navigation_count_page_artifact_and_claim_overreach"
spark_qa_verdict: "needs_revision_corrected_for_class_example_navigation_training_execution_artifact_and_evidence_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["demonstration_without_quantitative_outcomes", "figure_one_not_navigation_configuration", "limited_two_thousand_episode_training", "unlimited_training_optimality_not_proven", "training_resource_saving_not_measured", "explainability_and_adaptivity_not_evaluated", "rl_algorithm_reward_exploration_and_hyperparameters_missing", "scenario_configuration_missing", "baseline_and_ablation_missing", "runs_seeds_and_uncertainty_missing", "communication_and_failure_metrics_missing", "reproducibility_manifest_missing"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_bdi_rl_control_flow_training_execution_optimality_evaluation_artifact_and_reproducibility_boundary_check"
escalation_verdict: "needs_revision_corrected_for_figure_case_training_execution_claim_evaluation_and_reproducibility_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted BDI-RL and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# MASPY: A Python Framework for Developing BDI Agents with Reinforcement Learning

## 一句话总结

MASPY 把 AgentSpeak-like declarative programming、BDI reasoning、environment/communication infrastructure、pre-execution Q-table training 和实时 GUI 放进 Python framework；导航 demo 展示了 learned exploration 与 target-known A* planning 的切换，但没有量化 outcome、baseline、重复实验或完整 RL/复现配置。

## 框架定位

MASPY（Multi-Agent System for Python）用于开发 BDI multi-agent systems，并利用 Python 生态接入 machine-learning tools。作者把它与 Jason-RL 的差异概括为 Python integration，也把它与 SPADE、PADE、Mesa、BDIPython、PROFETA 等放在功能覆盖层面比较（p. 4074）。

这些是 framework integration 与 accessibility 主张。论文没有在共同任务、规模或性能指标上对上述 systems 做 head-to-head evaluation，因此不能由 related-work 描述推出 MASPY 更快、更易用、更可扩展或更正确。

## 五个核心 classes

MASPY 由五个 classes 组成（pp. 4074–4075）：

- **Admin**：system configuration、execution 和 logging；
- **Agent**：管理 beliefs、goals 和 plans，并运行 BDI reasoning cycle；
- **Environment**：表示 agents 感知和行动的 context；
- **Communication**：通过 communication channels 交换 messages；
- **Learning**：把 reinforcement learning 接入 agent，使其在训练过的 environment 中选择 learnable actions。

Figure 1 用 three agents、two environments、communication channels 和 learning classes 说明这些 classes 如何交互。它只是架构示例，不是后续 navigation case 的 agent 或 environment 数量。

## GUI 的可观察范围

配套 graphical interface 在每个 reasoning cycle 显示（p. 4075）：

- agent intentions；
- exchanged messages；
- perceptions；
- environment actions。

作者说该界面支持 real-time monitoring 与 debugging。论文没有 user study、debugging-time comparison、trace completeness 或 explainability metric，因此 GUI 可视化不等同于 BDI/RL 决策已经得到解释性验证。

## 2D navigation case

案例把 **several agents** 放入带 randomly generated obstacles 的 2D grid，目标是找到 target position（p. 4075）。agent：

- 只能向四个方向移动；
- 只能感知 current position；
- 通过 communication 分享逐步发现的信息；
- 在 Pygame interface 中以 blue squares 显示，black squares 是 obstacles，red cross 是 target。

论文没有给出 grid dimensions、agent 数量、obstacle density/distribution、target sampling、communication delay/loss 或 episode termination rule。

## 训练与执行边界

### Pre-execution learning

每个 agent 在执行前独立使用 Learning module，为给定 map 构建 Q-table。训练限制为 2000 episodes，因此只得到 partial knowledge，没有单个 agent 学到完整 optimal path（p. 4075）。

论文没有说明：

- 具体 RL algorithm 名称；
- state/action encoding；
- reward 与 terminal condition；
- exploration policy；
- learning rate、discount、schedule 或 initialization；
- 不同 agents 的 map/seed 是否相同。

作者称 unlimited episodes 最终会学到 optimal policies，但没有给出收敛假设、证明或训练曲线；这只能作为作者主张。

### Frozen execution

训练只发生在 execution 前。执行时 agent：

- 从 trained model 选择 best prediction/action；
- 用 environment perceptions 更新 internal map beliefs；
- **不修改 trained Learning module**。

因此这是 offline/pre-execution learning 与 online BDI belief update 的组合，不是 online RL。

## Learned exploration 与 A* 的 BDI 分流

Listing 1 给出两个都由 `Goal("move")` 触发、但 context 不同的 plans（p. 4075）：

### `make_move`

当 context 只有 agent position、尚不知道 target 时：

1. `get_best_action("Map", (position,))` 查询 trained policy；
2. agent move、perceive 并 update map；
3. 新信息通过 communication 分享；
4. 如果发现 target，broadcast 相应 belief。

### `best_move`

当 context 同时包含 target 与 agent position 时：

1. `astar_explore(position, target)` 在当前不完整 map 上求 best-known path；
2. move 后 perceive、update map 并通知其他 agents；
3. 若 movement attempt 失败，使用更新知识和已失败 paths 重新运行 A*。

这个设计展示了同一 goal 如何因 beliefs/context 不同产生不同 intention。论文没有比较纯 RL、纯 A*、无通信或混合策略的 success、path length、messages、time 或 compute。

## 证据边界

三页 demo 没有报告：

- navigation success rate、path length、completion time 或 collision/failure rate；
- training episodes 与 resource/time/memory 的实际成本；
- baseline、ablation 或 alternative planner/learner；
- number of runs、random seeds、mean/variance、confidence interval 或 significance；
- knowledge coverage、Q-table quality、A* replanning frequency；
- communication volume、latency、loss 或 inconsistency handling；
- robustness、scalability 或 generalization 到不同 maps。

所以“partial training combined with symbolic reasoning can save training resources”“transparent and explainable”“adaptive”没有在本文中得到量化验证。

## Artifact 与复现边界

论文称 MASPY open-source，提供 documentation、runnable examples，以及 [Navigation on 2D Grid Wiki](https://github.com/laca-is/MASPY/wiki/Navigation-on-2D-Grid/)（p. 4074 footnote）。

正文没有 pin：

- commit、tag 或 release；
- Python/package versions 与 environment lock；
- exact grid/config file；
- random seeds、Q-table artifact 或 training command；
- 与 Figure 2 对应的 executable run manifest。

链接提供了继续核验的入口，但三页稿本身不足以精确重放案例。

## Future Work

作者计划（p. 4075）：

- 继续扩展 MASPY modules；
- 探索 distribution mechanisms；
- 接入更复杂 learning；
- 为 graphical interface 增加 capabilities。

这些是 future plans，不是当前版本已经实现的结果。

## 页码与核验说明

PDF 逐页核对：p. 4074 为 identity、Abstract、Introduction/Related Work、framework overview、五 classes 与 Figure 1 开端；p. 4075 为 GUI 续文、完整 navigation case、training、Listing 1、Conclusion/Future Work；p. 4076 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YIGW5980.pdf) 核对 class architecture、training/execution boundary 与 BDI plan switching；`reviewed` 不表示 optimality、resource saving、explainability、adaptivity 或 navigation performance 已经验证。
