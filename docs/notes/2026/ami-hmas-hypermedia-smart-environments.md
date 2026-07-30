---
title: "AmI HMAS: A Hypermedia MAS for Goal-Driven Interactions with Every-day Smart Environments"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["agent_engineering", "generative_agents", "argumentation_reasoning", "planning_scheduling", "applications", "safety_verification", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/MAXW5671"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MAXW5671.pdf"
demo_url: "https://youtu.be/qPZIZ1Rz6eY"
code_url: "https://github.com/aimas-upb/llm-agents-for-ami/tree/aamas2026demo"
supplementary_url: "https://tinyurl.com/AmI-HMAS-AAMAS2026-sup"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05z"
spark_draft_verdict: "source_grounded_with_required_supplementary_evidence_confirmation_authorization_and_physical_execution_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_main_text_metric_absence_confirmation_scope_author_conclusion_and_device_governance_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["virtual_device_demo", "main_text_quantitative_results_absent", "supplementary_results_not_reviewed", "specific_llm_and_prompt_unreported", "task_set_baseline_variance_seeds_and_cost_unreported", "plan_correctness_and_invalid_request_results_unreported", "physical_execution_validation_unreported", "state_conflict_and_concurrency_unreported", "confirmation_not_full_authorization", "access_control_unreported", "prompt_injection_and_tool_abuse_unreported", "unsafe_action_and_rollback_unreported", "privacy_and_security_unreported", "user_study_and_generalization_unreported", "smart_environment_actuation_high_stakes"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_supplementary_evidence_confirmation_authorization_access_control_prompt_injection_unsafe_actuation_rollback_privacy_and_physical_validation_check"
escalation_verdict: "hold_for_governance_and_evidence_disclosure"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted smart-environment actuation governance and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# AmI HMAS: A Hypermedia MAS for Goal-Driven Interactions with Every-day Smart Environments

## 一句话总结

AmI HMAS 把 HomeAssistant deployment 映射成 RDF/Thing Description hypermedia environment，由三个 agent roles 发现设备、解释请求并规划动作，再用 signifier memory 复用过往 affordance；论文展示了虚拟 light、blinds 和 sensors 的 end-to-end demo，但正文没有 benchmark 数字，也未报告真实设备安全、授权、prompt injection 或 rollback 验证。

## 资源与贡献边界

论文提供：

- [demo video](https://youtu.be/qPZIZ1Rz6eY)；
- [AAMAS 2026 demo code](https://github.com/aimas-upb/llm-agents-for-ami/tree/aamas2026demo)；
- [supplementary material](https://tinyurl.com/AmI-HMAS-AAMAS2026-sup)。

本笔记依据三页正文审查，只确认 supplementary link 被列出，没有读取或引入其中的结果。正文把贡献概括为：

1. 把现有 HomeAssistant deployment 映射为 semantic、navigable HMAS environment；
2. 通过 signifier 记录和复用过去 interaction experience；
3. 用 LLM-supported agent roles 处理 request interpretation、environment exploration 和 action planning，并把用户留在 plan validation loop 中。

## HomeAssistant 到 Hypermedia MAS

Mapping engine 的对应关系是：

| HomeAssistant | HMAS / Web of Things 表示 |
|---|---|
| `area_id` | workspace |
| device | uniquely addressable W3C Thing Description artifact |
| entity attributes / state | readable Property Affordances |
| entity service | Action Affordance |
| service input | explicit JSON schema |
| state change | WebSub event notification，以 RDF payload 推送 |

每个 physical area 成为 workspace，内部包含 devices、sensors 和 services。Agents 通过 W3C WoT Discovery 发现映射后的环境；整体还使用 Agents & Artifacts 思路以及 SPADE agent framework。

这说明了互操作表示和 discovery workflow，不等于已证明所有 HomeAssistant integrations、device schemas 或状态变化都能正确映射。

## 三个 agent roles

### EnvExplorer

EnvExplorer 发现并编目 environment，索引可用 artifacts 的 affordances，跟踪 PropertyAffordance state changes，并管理 past-affordance usage experience 的记录与回忆。

### UserAssistant

UserAssistant 接收请求，根据 EnvExplorer 已知 capabilities 判断 feasibility，分类 request type，把可行请求交给 InteractionSolver，并以用户可理解的形式展示返回的 invocation plan 供确认。

### InteractionSolver

InteractionSolver 是主要 reasoning component，生成能够解决请求的 ActionAffordance invocation plan。LLM 支持 planning；solver 也会让 EnvExplorer 找到与当前请求相同或相似的 past-experience signifiers，从而缩小相关 affordances。

论文写到 confirmed plans 被标记用于经验存储，execution lifecycle 由 UserAssistant 管理。这只说明计划确认、存储与生命周期流程，不能扩大为完整 authentication、authorization、policy enforcement 或 safe-execution guarantee。

## Signifier memory

Signifier 把三项绑定：

- artifact affordance；
- intent；
- execution context。

它用 RDF 表示，并用 SHACL 描述 context conditions。新请求与现有 signifiers 的匹配同时考虑 intent similarity 和 context similarity。

该机制旨在让过去计划为相似请求提供 affordance hints 和 adaptation fast path。正文没有给 memory size、matching threshold、stale experience handling、错误 signifier 清理或 poisoning 防护。

## Demonstrator

Demo 使用带 virtual devices 的 HomeAssistant deployment，包括：

- smart light；
- motorized blinds；
- indoor / outdoor environmental sensors。

展示流程包括：

- 自动生成 TD-based Hypermedia Environment；
- 在浏览器检查 RDF model；
- agents 探索并发现 artifacts；
- 检查 light state；
- 为 light 与 blinds 的 multi-command request 做 LLM planning；
- 把确认经验存成 signifiers；
- 在 low-light 条件下处理不同措辞的 implicit request。

作者展示两条路径：LLM-based environment exploration/planning，以及利用 stored signifiers 提供 affordance hints、再做 plan adaptation 的 fast path。

## 正文没有量化结果

论文说 supplementary material 另外讨论 planning method、success rates、latency 和 signifier reuse rates，但三页正文没有提供：

- task 数量或 benchmark protocol；
- success、latency 或 reuse 的数值；
- baseline 或 statistical comparison；
- failure cases 或 trial-level results。

因此不能仅凭 supplementary link 的存在声称这些指标已经在本轮审查中得到验证。

## 未报告的复现与效果证据

正文未报告：

- 具体 LLM、model snapshot、prompt、temperature 或 decoding；
- benchmark、task distribution、device coverage 或 context variation；
- baseline、ablation、variance、random seeds、token/cost；
- plan correctness、invalid/impossible request 的实验结果；
- signifier matching threshold、误匹配率、staleness 或 reuse failure；
- real physical-device execution、latency、network failure 或 recovery；
- concurrent requests、state races、conflicting plans 或 multi-user arbitration；
- user study、cross-home/device generalization 或 long-running deployment。

作者结论称该框架 “successfully” 结合 classical agency、agentic AI workflow 与 hypermedia modeling，并有 real end-user impact potential。正式笔记把它记录为作者结论和潜力，不当作用户效果或部署可靠性实证。

## 实体动作与安全治理

系统能够生成并调用智能环境的 Action Affordances。正文没有说明：

- HomeAssistant authentication、per-user authorization 或 least privilege；
- 高风险设备/action allowlist 与参数约束；
- prompt injection、malicious device metadata 或 tool abuse 防护；
- unsafe plan 的 policy checker、simulation/dry run 或 human escalation；
- 执行中状态变化、partial failure、rollback 或 fail-safe；
- signifier provenance、approval、expiry、revocation 或 poisoning defense；
- household privacy、request/log retention、secrets handling 或 audit access。

用户确认一个返回计划不等于这些治理机制已经存在。高风险评级来自可触发现实设备动作的潜在后果及正文证据缺口；它不表示 demo 已造成安全事件，也不表示作者声称系统可无人监督部署。

## 页码核验

- p. 4149：身份、摘要、应用问题、相关 benchmark 动机、三项贡献起点；
- p. 4150：HomeAssistant mapping、三个 agent roles、signifier memory、virtual-device demo、supplementary link 与作者结论；
- p. 4151：致谢与参考文献，没有新增实验结果。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MAXW5671.pdf) 核验；`reviewed` 不表示正文未提供的 benchmark、physical execution、authorization、prompt-injection defense、rollback、privacy/security 或真实用户效果已经验证。
