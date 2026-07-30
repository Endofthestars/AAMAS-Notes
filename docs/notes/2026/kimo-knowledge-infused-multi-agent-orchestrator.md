---
title: "KiMO: Knowledge-infused Multi-agent Orchestrator"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["agent_engineering", "planning_scheduling", "argumentation_reasoning", "human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/WTIF5096"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WTIF5096.pdf"
code_url: "https://tinyurl.com/3es9zyhj"
demo_url: "https://tinyurl.com/yfa8ctwn"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06a"
spark_draft_verdict: "source_grounded_with_required_example_only_evaluation_type_consistency_and_executable_workflow_governance_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_zero_point_eight_nine_example_continuous_improvement_and_semantic_safety_claims"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_page_demo_without_experiments", "illustrative_scores_not_benchmark", "task_dataset_baseline_and_ablation_unreported", "gnn_training_and_score_calibration_unreported", "workflow_correctness_latency_scaling_and_cost_unreported", "continuous_improvement_unvalidated", "type_consistency_not_semantic_safety", "custom_executable_agents_and_tools", "sandbox_permissions_and_access_control_unreported", "ontology_and_registry_poisoning_unaddressed", "feedback_retraining_contamination_unaddressed", "provenance_versioning_rollback_and_override_audit_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_example_score_type_check_executable_tool_permissions_knowledge_poisoning_feedback_contamination_provenance_and_rollback_check"
escalation_verdict: "require_governance_and_evaluation_evidence_before_strong_deployment_or_performance_claims"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted executable-workflow governance and evaluation-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# KiMO: Knowledge-infused Multi-agent Orchestrator

## 一句话总结

KiMO 用 planning ontology 生成子任务，再用 agent registry、GNN 和 beam search 组装异构 agent/tool workflow；三页论文完整展示制造异常检测 UI，但没有系统实验，0.89/0.34 只是示例分数，type-consistency Verifier 也不能视为语义正确或安全保证。

## 定位与资源

KiMO 是 DYNO 的 sub-component，面向 LLM、statistical、symbolic 和 reactive components 的显式编排。论文提供 [代码](https://tinyurl.com/3es9zyhj) 与 [demo video](https://tinyurl.com/yfa8ctwn)。

双层 knowledge infusion 为：

1. planning ontologies：编码 domain-specific hierarchical task decomposition；
2. agent registry：记录 capabilities、compatibility、I/O 和 infrastructure constraints。

## Stage 1：PlanGen

PlanGen 接收 task description \(\tau\) 与 metadata \(M\)，产生

\[
s_i=\langle g_i,m_i,D_i\rangle
\]

其中 \(g_i\) 是 goal，\(m_i\) 是 sequential/parallel execution mode，\(D_i\) 是 knowledge dependency。它使用 Llama 3.2 3B、LoRA 与 retrieval-augmented fine-tuning（RAFT），并以 plan ontology 为条件。

制造示例把 defect detection 分为 collect sensor data、preprocess signals、run CNN inference；专家可在 canvas 中修改 goal、dependency 和 mode。

## Stage 2：AgentGen

AgentGen 为每个 subtask 构建

\[
w_i=\langle A_i,T_i,I_i,O_i,E_i\rangle
\]

即 agents、tools、inputs、outputs 和 connections。三阶段是：

1. **constraint filtering**：按 capability 与 requirement 从 registry 筛候选；
2. **GNN scoring**：在 subtask/agent/tool heterogeneous graph 上计算 suitability；
3. **beam search**：宽度 \(k=5\)，搜索 agent–tool configuration 和 edge pattern。

文中用 AnomalyPredictor 0.89、StatisticalDetector 0.34 展示打分，但没有 dataset、protocol、ground truth 或统计信息，故只能记为示意，不能当 benchmark。

Verifier 在并入 global workflow 前检查 **type consistency**。这不验证任务语义、业务约束、工具副作用或安全性。执行日志会用于 retrain GNN；论文没有报告这一反馈闭环带来的实际提升。

## 交互平台

Planning View 展示 task、metadata 与 decomposition graph；Agentic Workflow View 展示 filtering、GNN、beam search、agent nodes、tools 和 data streams。用户还能加载 custom template、修改 workflow，或从 registry 选择 tools 创建 custom agent。

这支持 human inspection/editing，但论文没有报告 expert study、修改质量、override audit 或错误恢复。

## 完全缺失的评测

正文没有 experiments/results section，也没有报告：

- task set、dataset、ontology/registry size；
- GNN features、training data、objective、calibration 或 update schedule；
- orchestration success、workflow correctness、latency 或 scaling；
- baseline、ablation、failure taxonomy；
- runs、variance、seeds、confidence interval 或 cost；
- human study、cross-domain generalization；
- log retraining 前后的 improvement。

因此 “interpretable”“flexible”“continuous improvement”属于设计或作者主张。

## 可执行工作流治理

平台可构造并执行 custom agents/tools，但论文未报告：

- sandbox、tool allowlist、least privilege、network/secret control；
- ontology/registry update authorization、signature 或 poisoning defense；
- executable component provenance、version pinning 与 dependency integrity；
- feedback log 的质量门控、contamination detection 和 model rollback；
- workflow approval、human override identity 与不可抵赖 audit trail；
- partial failure、semantic verification 和 safe rollback。

高风险来自可执行工作流和反馈训练的潜在后果，不表示 demo 已造成事故。

## 页码核验

- p. 4152：身份、资源、动机、双层知识注入和架构图；
- p. 4153：PlanGen、AgentGen、0.89/0.34 示例、Verifier、日志重训与 UI；
- p. 4154：致谢和参考文献，无新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WTIF5096.pdf) 核验；`reviewed` 不表示性能、泛化、continuous improvement、语义安全或执行治理已验证。
