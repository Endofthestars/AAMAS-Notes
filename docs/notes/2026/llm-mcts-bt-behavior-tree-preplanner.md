---
title: "Behavior Tree Generation with LLM-MCTS-BT as a Pre-Planner Bridging Priors and Uncertainty"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "planning_scheduling", "generative_agents"]
dblp_key: ""
doi: "10.65109/VHJF3771"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VHJF3771.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "llm_planning", "mcts_search", "behavior_tree", "alfworld_simulation", "llm_based_evaluation", "not_robot_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Behavior Tree Generation with LLM-MCTS-BT as a Pre-Planner Bridging Priors and Uncertainty

## 一句话总结

本文把行为树（BT）生成建模为由 LLM 动态提出结构修改、由 MCTS 选择/扩展/评价/回传的组合搜索；以层级 task decomposition、Fallback recovery 和 condition–action coupling 为 priors。ALFWorld 的 40 个 household tasks 中，作者报告在有/无先验环境信息时 task completion 为 82.5%/75.0%，高于 Zero-/One-shot 和 CoT baselines。该结果来自模拟环境及 LLM-based quality evaluation，不证明生成 BT 在真实机器人上正确、安全、可执行或对未知世界稳健。

## 方法与证据

- search state 是 BT structure，初始为简单 Sequence root；action 为 node substitution、Fallback insertion 和 leaf extension，目标最大化 multi-criteria function（§2）。LLM 以当前 BT、task \(\tau\)、initial environment \(E_0\) 和三项 design principles 动态生成候选 action；其合法性、覆盖和 prompt/model sensitivity 未在摘要量化。
- 三项 structure priors 分别是以 nested Sequence/Parallel 进行 hierarchical decomposition、以 Fallback 插入 alternative execution branches、以 leaf condition/action 做 precondition verification。BT 的模块化/可解释表示不等于所选 action 的语义、物理前置条件或安全约束被验证。
- evaluation score 是 LLM 对 reactivity、efficiency、safety、correctness、robustness、modularity、interpretability 的 \(-2\ldots2\) rating 加权平均（Eq. 2）；MCTS selection 用 UCB，expansion 后以该 LLM assessment 替代 stochastic rollout，backup 使用 depth-decayed reward（Eq. 3）。因此 search objective 受同一类模型 judge 的偏差、权重和评分可重复性影响，不能当作独立安全/正确性 oracle。
- 40 个 ALFWorld/ALFRED household tasks，比较 Zero-Shot、One-Shot、CoT，可选 Expert Policy trajectories；作者称本法无需 expert demonstrations。Figure 2 报 82.5%（with prior）和 75.0%（without prior）的 task completion，并以 LLM approval/ranking 支持结构质量。摘要没有 task split、LLM versions/prompts/decoding、search budget、seeds/CI、执行失败分类或真实 robot 评测。
- 所谓 partial observability 是该 ALFWorld setting；不能推出对视觉/传感噪声、持续状态变化、操控误差、碰撞、用户干预、权限或工具失败具有 robustness。扩展摘要也未给 BT verifier、runtime monitor 或 formal safety guarantee。

## 适用边界与复现

- 适合将其作为受控 simulator 或人工审阅下的 pre-planning/BT-authoring 辅助；生产机器人不可直接执行 LLM-generated tree。须独立做 action schema/type validation、precondition/effect checking、collision/force/geofence constraints、sandbox/digital twin、human approval和 runtime failure recovery。
- 复现需固定 ALFWorld/ALFRED version、40 task list、prior-information protocol、LLM generation/judge models与 prompts/temperatures、\(P\) principles、action grammar、MCTS \(C\)、budget/depth/\(\lambda\)、criteria weights、baselines/expert-policy availability、seeds和 raw traces。报告 completion CI、search calls/cost/latency、invalid tree rate、judge-executor disagreement和 per-task failures。
- 应在 held-out tasks、long-horizon/multi-object tasks、world changes、ambiguous language、noisy observations、action/tool failures、adversarial prompts与 real/sim-to-real robots 上测试；由 independent execution and safety evaluators 替代 LLM-only judgment，并审计 Fallback 是否真的覆盖危险分支。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM planning/BT 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VHJF3771.pdf) 核验 search formalization、LLM action/score、MCTS phases、40-task ALFWorld setup与 Figure 2 数值；没有将模拟 completion 或 LLM approval/ranking 写成真实机器人安全保证。
