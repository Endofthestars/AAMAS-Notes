---
title: "CraftUtopia: A LLM-based Multi-Agent System for Collaborative Construction in Minecraft"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "marl_coordination", "planning_scheduling", "robotics_embodied", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/PUIJ7087"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PUIJ7087.pdf"
code_url: "https://github.com/craftutopia-demo/CraftUtopia"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05y"
spark_draft_verdict: "source_grounded_with_required_speedup_completion_fidelity_baseline_fairness_ablation_and_security_corrections"
spark_qa_verdict: "needs_revision_corrected_for_exact_mindcraft_results_one_point_five_and_three_point_nine_speedups_and_missing_evaluation_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_build_small_sample_evaluation", "completion_criterion_undefined", "completion_not_geometric_fidelity", "baseline_input_and_budget_not_homogeneous", "relative_runtime_without_absolute_distribution", "variance_seeds_and_confidence_unreported", "no_hierarchy_or_skill_library_ablation", "skill_contribution_unquantified", "manual_intervention_unreported", "llm_tokens_cost_and_configuration_incomplete", "generated_code_and_tool_permissions_unreported", "minecraft_only_scope", "emergent_behavior_only_qualitative", "three_dimensional_reconstruction_error_unmeasured"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_completion_fidelity_baseline_fairness_scaling_statistics_ablation_manual_intervention_generated_code_permissions_and_generalization_check"
escalation_verdict: "escalate_for_reproducibility_and_tool_governance_evidence"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted evaluation-validity and generated-tool safety check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# CraftUtopia: A LLM-based Multi-Agent System for Collaborative Construction in Minecraft

## 一句话总结

CraftUtopia 把单张 2D 参考图转换为 Minecraft blueprint，再由 designer–manager–foreman–worker hierarchy 并行施工；在三种建筑各五次试验中报告 15/15 completion，并在 NCPA 上让 6 workers 比 3 workers 快 1.5×、比 1 worker 快 3.9×，但没有几何 fidelity、绝对 runtime、方差、消融或完整基线配置，因此证据只支持有限 Minecraft demo。

## 资源与两阶段流程

论文提供 [CraftUtopia GitHub 仓库](https://github.com/craftutopia-demo/CraftUtopia)。

系统包含：

1. **Design**：从单张 2D image 生成 Minecraft-compatible 3D blueprint；
2. **Build**：把 blueprint 分为 spatially disjoint subtasks，并由多个 agents 并行执行。

Design 依次：

- 用 TRELLIS 从图像生成 3D model；
- 用 ObjToSchematic 转成 block-based Minecraft schematic；
- 用 LLM 编译成明确列出 blocks 与 coordinates 的 blueprint file。

该链路把单视角 3D reconstruction 的不确定性传给后续 construction。论文没有测量 TRELLIS geometry error、schematic conversion loss 或最终建筑与 reference 的视觉/结构差异。

## 四类角色

CraftUtopia 定义：

- **Architectural Designer**；
- **Project Manager**；
- 可变数量的 **Foremen**；
- 可变数量的 **Workers**。

Manager 把 blueprint 切成不重叠空间区域，并分配给 foremen；foreman 再规划具体 block-placement subtasks 给 workers。Hierarchy 分离 global decomposition 与 local execution，减少所有 agents 直接协调的通信负担。

论文使用 Claude-Sonnet-4.5，但未报告精确 model snapshot、prompt、temperature、token budget、retry policy 或 inference cost。

## Skill library

Construction 会重复 stairs、walls 等 routines。Foreman 初次遇到 routine 时用 LLM 规划，并可把 learned routine 存入 shared skill library；后续 foremen 调用已有 skill，减少重复 LLM replanning。

论文没有提供：

- skill 的表示、参数与版本；
- skill acceptance/test criteria；
- erroneous skill 的 rollback；
- hierarchy-only、skill-only 或 no-skill ablation；
- skill reuse 对 latency、cost 或 success 的独立贡献。

因此 “skill acquisition improves efficiency”是设计机制和作者解释，尚无因果分解。

## 三种建筑与 MINDcraft

评测使用：

- Pyramids；
- Temple of Heaven；
- NCPA。

每个系统/任务进行 5 trials。论文报告：

| System | Input | Pyramids | Temple of Heaven | NCPA |
|---|---|---:|---:|---:|
| MINDcraft | complete 3D blueprint | 2/5 | 0/5 | 0/5 |
| CraftUtopia | single 2D image | 5/5 | 5/5 | 5/5 |

作者还称 MINDcraft 在成功 trials 中，build time 至少是 CraftUtopia 同一建筑 worst-case runtime 的 2×。

这里的输入并不相同：MINDcraft 得到完整 3D blueprint，CraftUtopia 从 2D image 开始。虽然前者输入看似包含更多结构信息，但论文没有给相同 hardware、agent count、time limit、prompt、model、tool/API 或 stopping rule。相对 runtime 也没有 absolute values、trial-level distribution 或 censoring details，不能当作严格同条件 benchmark。

## Worker scaling

论文比较 1、3、6 workers。MINDcraft 在三个 worker counts 下都未完成三个 builds。CraftUtopia 保持 100% completion，并在 NCPA 上报告：

- 6 workers 比 3 workers 快 **1.5×**；
- 6 workers 比 1 worker 快 **3.9×**。

论文没有报告 2.3×；正式笔记不使用该数值。结果也没有给其他两个建筑的完整 scaling table、absolute wall-clock、worker utilization、LLM calls、variance 或 communication overhead。

## Completion 与 fidelity

“100% success”按论文语言指 builds completed。三页稿没有定义：

- 必须放置多少 blocks 才算 complete；
- wrong/missing/extra blocks 的容差；
- blueprint equality、IoU、Chamfer distance 或 visual similarity；
- 人工检查、自动 validator 或 blinded rating；
- 中途 human correction、reset 或 post-processing。

因此 completion 不等于从参考图精确恢复 3D geometry，也不证明 architectural fidelity 或 aesthetic quality。

## Emergent observations

作者观察到 workers：

- 临时搭建 scaffolding 到达高处，并在不再需要时拆除；
- 接近完成时部分 worker 成为 bystander，避免阻碍其他 agents。

这些是 qualitative observations，没有 frequency、detection rule、counterfactual 或 ablation，不能据此证明稳定 emergent cooperation。

## 缺失证据与安全边界

本文未报告 seeds、confidence intervals、failure taxonomy、token/cost、完整 runtime、cross-map generalization、adversarial image、agent communication logs 或 reproducible environment versions。

工具化 agent 还需要控制：

- LLM-generated commands/code 的 sandbox 与 allowlist；
- Minecraft server/world write permissions；
- malicious blueprint 或 skill-library poisoning；
- infinite loops、resource exhaustion 与 conflicting placements；
- shared-skill provenance、review 与 rollback。

高风险等级来自小样本结果、对比设置不完整和生成工具权限未报告，不表示 Minecraft demo 已造成现实安全事件。

## 页码核验

- p. 4140：身份、摘要、资源、角色、Design/Build 与 hierarchy/skills 起点；
- p. 4141：Design 方法、Claude-Sonnet-4.5、三 builds、MINDcraft、worker scaling 和 emergent observations；
- p. 4142：结论与参考文献，没有新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PUIJ7087.pdf) 核验；`reviewed` 不表示 geometric fidelity、跨任务泛化、baseline 公平性、skill 因果贡献或生成工具安全已经验证。
