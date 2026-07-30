---
title: "A Multi-level Explainability Framework for Engineering and Understanding BDI Agents"
conference: "AAMAS"
year: 2026
track: "jaamas"
topics: ["argumentation_reasoning", "agent_engineering", "human_agent_interaction", "safety_verification", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/ZIQG2381"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ZIQG2381.pdf"
logger_url: "https://github.com/yan-elena/agent-logging"
generator_url: "https://github.com/yan-elena/agent-explanation"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06g"
spark_draft_verdict: "conceptual_framework_and_two_level_prototype_without_empirical_or_causal_fidelity_evidence"
spark_qa_verdict: "needs_revision_correct_page_map_preserve_domain_future_scope_and_add_log_governance_gaps"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_page_jaamas_summary", "prototype_supports_implementation_and_design_only", "domain_level_future_work", "individual_agent_dimension_only", "environment_interaction_and_organization_future_work", "non_bdi_subsymbolic_and_generative_llm_future_possibility", "closest_goal_and_event_not_causal_fidelity_proof", "no_user_developer_designer_or_domain_expert_study", "trust_understanding_debugging_and_validation_not_measured", "explanation_fidelity_completeness_coverage_and_bias_unreported", "latency_scaling_baseline_runs_variance_and_failures_unreported", "perception_message_belief_plan_goal_intention_action_logs_may_be_sensitive", "privacy_authorization_retention_redaction_and_integrity_unreported", "missing_stale_logs_mapping_ambiguity_and_causal_over_attribution_unreported", "explanation_uncertainty_correction_and_audit_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_prototype_scope_causal_fidelity_user_outcome_sensitive_logs_privacy_integrity_mapping_ambiguity_correction_audit_and_future_capability_boundary_check"
escalation_verdict: "pass_with_causal_fidelity_empirical_and_log_governance_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted causal-fidelity, empirical-outcome, sensitive-log, and future-scope check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# A Multi-level Explainability Framework for Engineering and Understanding BDI Agents

## 一句话总结

本文用 execution logs、level-specific events、explanation functions 与 lower-to-higher mapping functions，为 Jason/BDI agent 构建 Implementation、Design、Domain 三层自然语言 narratives；开源原型当前只实现前两层并展示一个 example。三页稿没有 user study、debugging/validation outcome 或 causal-fidelity evaluation，因此最近 goal/event 规则是叙事生成机制，不是已经证明忠实、充分和完整的因果解释。

## 三个角色与抽象层

| Level | 主要抽象 | 面向角色 | 当前状态 |
|---|---|---|---|
| Implementation | agent programming-language abstractions；本文采用 Jason | developers | prototype 支持 |
| Design | agent architecture abstractions；本文采用 BDI beliefs/goals/intentions | designers | prototype 支持 |
| Domain | domain knowledge、functional/non-functional requirements | domain experts 与 end users | future work |

不同角色可选择所需 granularity。Implementation level 解释技术和运行细节；Design level 抽象底层实现以呈现系统原则与 architecture；Domain level 计划通过 use cases、user stories 与 system stories 引入 stakeholder/domain knowledge。角色匹配是框架设计，论文没有实测不同角色是否更理解、更信任或更能完成任务。

## Events、narratives 与 explanations

框架在每一层定义三类元素：

1. 依照该层抽象刻画 agent behavior 的 events；
2. 定义同层 events 之间 causal link 的 explanation function；
3. 将 lower-level events 映射为 higher-level events 的 mapping functions。

Execution logs 被转成 natural-language event sequence，即 agent-behavior narrative。用户可阅读 narrative，并对特定 event 请求解释；返回的是与该 event 的 causal link 关联的一组 events。

### Implementation level

Jason-level events 包括：

- environment perception 与 message reception；
- belief base、plan library updates 和 plan selection；
- goal lifecycle：created、suspended、removed；
- intention lifecycle：created、waiting、suspended、removed；
- actions：triggered、failed、finished。

论文给出的第一种 “trivial explanation function” 以 goals 为中心：通过 same intention 寻找 closest identifiable goal 来解释 event。

### Design level

Design events 表示从 Implementation level 映射和抽象出的 beliefs、goals 与 intentions。Explanation function 使用 closest related event：例如 executed action 由 new intention 解释，new intention 再由 new goal 解释。

“closest”与 “same intention”给出可执行的关联规则，但三页稿没有验证它们是否识别真实充分原因、是否遗漏 alternative causes，或在 incomplete logs、并发 intentions 和 ambiguous mappings 下仍然忠实。

## 开源原型与范围

原型由两部分组成：

- 附着到每个 Jason agent 的 logger，代码见 [agent-logging](https://github.com/yan-elena/agent-logging)；
- 处理 logs、构建 narratives 并暴露 Web interface 的 narrative generator，代码见 [agent-explanation](https://github.com/yan-elena/agent-explanation)。

论文称开发了一个 example 展示 tool functionality，但没有把 example 写成 empirical evaluation。当前实现只支持 Implementation 与 Design levels；Domain level 仍需与 requirements methods 集成。

当前工作也只关注 individual-agent dimension。Environment、interaction 与 organization dimensions 是 future work；迁移到其他 BDI technologies 需要调整 Implementation abstractions 和 mappings。Non-BDI、sub-symbolic、generative-LLM agents 及 cognitive-neck layer 只是未来可能方向，不是当前原型能力。

## 实证证据边界

三页稿没有报告：

- user、developer、designer 或 domain-expert study 的 participants、tasks 或 protocol；
- explanation 对 trust、understanding、debugging time、defect finding 或 requirements validation 的影响；
- causal correctness、fidelity、sufficiency、completeness、coverage、bias 或 calibration；
- baseline、alternative explanation function 或 mapping ablation；
- runtime latency、log volume、memory、agent-count scaling 或 concurrent workload；
- runs、variance、statistics、failure cases 或 independent replication。

所以 “increase trust and understanding”“support debugging and validation”“enable stakeholders”是 motivation 与 intended use，不是本文测得的 outcome。自然语言 narrative 也不自动等同于事实正确、用户可理解或适合高风险决策。

## 日志与解释治理

Logger 可能记录 perceptions、messages、belief/plan updates、goals、intentions 和 actions，其中可能包含业务状态、个人信息或 agent-internal decisions。三页稿未报告：

- data minimization、consent、purpose limitation、authorization、retention、deletion 或 redaction；
- log transport/storage encryption、integrity、tamper evidence、provenance 或 access audit；
- dropped、incomplete、stale、out-of-order 或 contradictory logs 的检测；
- lower-to-higher mapping ambiguity、many-to-one information loss 与 versioning；
- causal over-attribution、alternative explanations、不确定性表达和 confidence；
- 用户纠错、developer override、appeal、re-generation 与 audit trail。

这些是当前摘要未披露的 controls，不是已经发生数据泄漏、篡改或错误解释的证据。高影响使用应把 narrative 保持为可追溯的辅助视图，保留原始 events、mapping/version、缺失信息和人工复核。

## 页码核验

- p. 4191：题名、摘要、引言、三层框架与角色概述；
- p. 4192：三层定义、narrative construction、Implementation/Design rules、prototype、结论、资源与 future work；
- p. 4193：参考文献，没有 prototype 或新增评测。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ZIQG2381.pdf) 核验；`reviewed` 不表示 full JAAMAS article、Domain level、MAS/LLM extensions、causal fidelity、user outcomes 或 log governance 已独立验证。
