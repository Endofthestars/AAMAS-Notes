---
title: "HAMMR: A Human-Aligned Multi-Agent Framework for Language-Guided Robotic Manipulation"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["robotics_embodied", "agent_engineering", "planning_scheduling", "generative_agents", "human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/BHTF7700"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BHTF7700.pdf"
demo_url: "https://youtu.be/DE1d4G4PUCk"
code_url: "https://github.com/RoopsHub/rlbench-multi-agent"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05u"
spark_draft_verdict: "source_grounded_with_required_approval_contradiction_ground_truth_failure_attribution_and_safety_corrections"
spark_qa_verdict: "needs_revision_corrected_for_ground_truth_information_flow_and_simulation_evidence_boundary"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["physical_robot_safety", "mandatory_approval_policy_contradiction", "approval_fatigue_and_automation_bias", "plan_execution_mismatch", "predefined_risk_taxonomy_unvalidated", "rationale_faithfulness_unvalidated", "parameter_edit_validation_unreported", "mcp_tool_permission_and_prompt_injection", "perception_and_motion_failure", "ground_truth_validation_information_flow_unclear", "single_arm_simulation_only", "no_collision_or_safety_metrics", "no_human_oversight_study", "no_baseline_or_ablation", "no_real_robot_or_sim_to_real_validation", "failure_recovery_and_security_unreported", "eu_ai_act_transparency_not_compliance"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_physical_safety_approval_policy_rationale_faithfulness_risk_classification_ground_truth_information_flow_mcp_permissions_and_sim_to_real_check"
escalation_verdict: "needs_revision_corrected_for_approval_contradiction_simulation_scope_human_alignment_ground_truth_failure_attribution_and_physical_safety_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted physical-safety and human-approval governance check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# HAMMR: A Human-Aligned Multi-Agent Framework for Language-Guided Robotic Manipulation

## 一句话总结

HAMMR 把 language-guided manipulation 分成无工具的 explainable planning 与获批后的 Sensing–Perception–Motion execution，在五个 RLBench 单臂任务上取得 \(67/75\approx89\%\) success；论文没有 human-oversight、rationale faithfulness、risk-classification、collision 或 real-robot validation，且“每个物理动作前必须批准”与“低风险动作自主执行”的原文策略尚未统一。

## 资源、愿景与实验证据

HAMMR 的 [演示视频](https://youtu.be/DE1d4G4PUCk) 与 [代码仓库](https://github.com/RoopsHub/rlbench-multi-agent) 均在 p. 4119 给出。

Figure 1 描绘 smart factory：heterogeneous robots、sensors 与 human workers 由 central supervisor 通过自然语言协调。当前实现与评测则是 RLBench / CoppeliaSim 的 single-arm manipulation（pp. 4119–4120）。

MCP abstraction 被作者描述为支持 Gazebo、CoppeliaSim 等 simulators 并便于 transfer to real robots。论文没有 real-robot 或 heterogeneous multi-robot experiment，所以 smart-factory、direct transfer、scalability 与 deployment robustness 都是设计愿景或 Future Work，不是当前证据。

## 四个 agents 与两阶段 separation

HAMMR 包含（p. 4120）：

- **Planner Agent**：中央 orchestrator；
- **Sensing Agent**；
- **Perception Agent**；
- **Motion Agent**。

后三个 specialized agents 按 Sensing → Perception → Motion 严格顺序执行，并通过 high-level MCP tools 与 simulator/robot implementation 交互。

流程分为：

1. **Phase 1 — Explainable Planning**：产生模板化计划、step-by-step justifications、risk class 和可调参数；Planner 此时没有 tool access；
2. **Phase 2 — Autonomous Execution**：批准后，三个 specialized agents 自动顺序调用 tools。

该 separation 限制 Planner 在审批前直接执行动作，但论文没有验证跨 phase state 是否不可篡改、approved plan 与 tool calls 是否一一对应、参数是否在批准后冻结。

## Template、risk class 与参数编辑

Planner 根据 natural-language patterns 识别 task category，并映射到 predefined motion-sequence template。例如 pick task 可展开为：

`open gripper → approach cube → grasp → maintain closed gripper → move to target`。

它为每一步生成 justification，例如先移动到物体上方 15 cm 以实现 collision-free descent。论文没有研究这些自然语言理由是否忠实反映实际 planner、perception 或 controller 的因果过程。

自动 risk taxonomy 为：

- **LOW**：不含 grasping 的任务；
- **MEDIUM**：single-object manipulation；
- **HIGH**：需要 state tracking 的 multi-object tasks。

这是任务类别映射，不是由 collision probability、force、speed、human proximity 或 formal hazard analysis 验证的 risk model。

计划包含 approach height、grasp offset 等参数。用户可用对话修改，例如把 grasp offset 调为 0.02 m；系统称修改会触发 validation 与 plan update。论文没有说明 validation constraints、safe ranges、units、conflicting edits 或 authorization policy。

## 未澄清的 approval policy

Abstract、Introduction 与 Framework 表述为：

- mandatory human approval；
- any physical action 前必须批准；
- only upon explicit user approval 才开始 autonomous execution。

Motivation 段却称 routine low-risk actions execute autonomously，而 novel 或 safety-critical tasks 才生成供 supervisor review/approval 的 explainable plans（p. 4119）。

三页稿没有说明低风险动作是否有一次性批准、预批准 policy、免审批路径，还是该句仅为 intended deployment。正式部署不能同时假定两个版本都成立；这是原文内部未解决的安全与责任边界。

## Sensing

Sensing Agent（p. 4120）调用：

- `load_task(task_name)`；
- `get_camera_observation()`。

观测包含：

- RGB image；
- depth map；
- point cloud；
- camera intrinsics；
- camera-to-base pose transformation。

它还取得 automatically extracted detection prompts 和 ground-truth positions for validation，输出 structured JSON 给 Perception Agent。论文没有说明 ground-truth positions 是严格 evaluation-only、是否包含在 downstream JSON、还是会影响 agent decisions；在真实机器人上这些真值通常不可直接获得。这里应记录信息流与现实可得性未澄清，不能直接断言发生 benchmark leakage。

## Perception 与 Motion

Perception Agent 的 `detect_object_3d()` 封装（p. 4120）：

1. GroundingDINO 产生 2D bounding boxes；
2. LAB color-space verification 检查或纠正 object colors；
3. 从 depth 提取对应 3D points；
4. 转换到 robot base frame。

单物体返回 `position_3d: [x,y,z]` 与 confidence；compound prompt 返回 `objects[]` positions/confidences。

Motion Agent 调用：

- `move_to_position()`；
- `control_gripper()`。

Tools 抽象 inverse kinematics 与 trajectory generation。Agent 维护 gripper-state awareness，并在 failure 时立即停止。论文没有定义 failure detector、stop latency、safe state、retry、rollback 或 emergency-stop integration。

## 75-trial evaluation

作者在五个 RLBench tasks 上使用 GPT-5-mini 作为 reasoning model，每任务 15 trials（p. 4120）：

| Task | Complexity | Success | Table failure cause |
|---|---:|---:|---|
| ReachTarget | Simple | 15/15 | — |
| PushButton | Simple | 15/15 | — |
| PickAndLift | Medium | 12/15 | Grasp misalignment |
| PutRubbishInBin | Medium | 12/15 | Perception noise |
| StackBlocks | Long-horizon | 13/15 | Placement instability |

合计 \(67/75=89.33\%\)，论文取整为 89%。

作者称 failures solely 来自 execution-level perception noise 或 motion inaccuracies，而非 planning errors。三页稿没有说明 error taxonomy、blinded adjudication、多个 reviewers 或 logging criterion，因此这是作者归因，不是独立验证的 failure-causality result。

## Comparison 与缺失证据

论文没有与 MALMM 直接比较，理由是缺少公开 replication resources。也没有其他 end-to-end baseline 或 ablation。

当前未报告：

- random seeds、trial-order、confidence intervals 或 repeated aggregate runs；
- task-instance variation、object/layout perturbation、OOD 或 domain randomization；
- template、risk class、justification、approval、MCP agents 的 ablation；
- human user study、approval time、error detection、automation bias 或 approval fatigue；
- rationale faithfulness 或 plan comprehension；
- risk-classification accuracy 或 hazard-analysis validation；
- collision、near miss、force、workspace violation、stop latency 等 safety metrics；
- end-to-end latency、token/tool cost 或 concurrency；
- real robot、human proximity 或 sim-to-real experiment；
- precise GPT-5-mini version/config、prompts、temperature 或 tool schemas；
- permissioning、authentication、prompt injection、malicious MCP result 或 tool-call policy；
- failure recovery、rollback、audit log 或 incident response。

89% 只反映这五个 simulation tasks 的 75 trials，不等于 smart-factory safety、human alignment 或 real-world success。

## Human alignment、解释与 EU AI Act 边界

Step-by-step plans、risk labels、editable parameters 与 approval UI 能向 supervisor 暴露更多 planning artifact，但论文没有验证：

- justification 与实际决策是否 faithful；
- humans 是否理解计划、发现危险并正确修改；
- explanation 是否降低事故或提高 calibrated trust；
- UI 是否满足 Article 13 或其他适用法律的全部要求。

论文引用 EU AI Act Article 13 说明 transparency 与 human oversight 的动机；引用法规不构成 compliance assessment、conformity evaluation 或 legal approval。

## 高风险物理与工具治理

真实部署的主要风险包括：

- 未统一的 low-risk autonomy / mandatory approval policy；
- repeated approvals 导致 fatigue、rubber-stamping 与 automation bias；
- approved template 与 execution-time perception/tool state 不一致；
- conversational parameter edits 越过 safe workspace；
- LLM prompt injection 或 malicious observation 操纵 tool selection；
- MCP server/tool 权限过大、未认证 simulator/robot endpoint 或 tool-result spoofing；
- Perception confidence 错误、遮挡、depth noise 与 coordinate-transform error；
- Motion failure detector 迟滞或 halt 后未进入物理 safe state；
- simulation ground truth、clean scenes 与 real-world sensing gap。

高风险等级来自 physical actuation 与未闭环的人类审批/工具安全证据，不表示当前 simulation demo 已造成现实伤害。

## Future Work 与页码核验

Future Work 包括与相关 multi-agent frameworks 做 benchmark、扩展 heterogeneous multi-robot settings，并按 simulation 后 real-world 的顺序评估 scalability 与 deployment robustness under human oversight（p. 4120）。

PDF 逐页核对：p. 4119 为 identity、Introduction、Motivation 与 smart-factory vision；p. 4120 为 Framework Overview、two phases、agent/tool pipeline、Table 1、Evaluation 与 Future Work；p. 4121 为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BHTF7700.pdf) 核验；`reviewed` 不表示 rationale faithfulness、approval effectiveness、risk classification、physical safety、EU AI Act compliance、sim-to-real 或 real-robot deployment 已被验证。
