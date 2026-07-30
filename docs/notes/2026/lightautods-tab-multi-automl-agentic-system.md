---
title: "LightAutoDS-Tab: Multi-AutoML Agentic System for Tabular Data"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "planning_scheduling", "human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/QBKY1209"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QBKY1209.pdf"
code_url: "https://github.com/sb-ai-lab/LADS"
demo_url: "https://youtu.be/sDUo_Ke2xs0"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06a"
spark_draft_verdict: "source_grounded_with_required_table_router_statistics_interpretability_and_generated_code_execution_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_eight_vs_nine_task_count_post_hoc_internal_maximum_missing_aide_and_unreported_evaluation_controls"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["eight_dataset_vs_nine_task_type_count_inconsistency", "normalized_score_definition_unreported", "single_scores_without_runs_variance_seeds_or_significance", "router_selection_protocol_unreported", "post_hoc_internal_method_maximum_not_router_result", "aide_plate_defect_result_missing", "baseline_configuration_and_budget_unreported", "hardware_runtime_token_and_cost_unreported", "leakage_and_pretraining_contamination_controls_unreported", "full_interpretability_and_productivity_author_claims", "generated_code_execution", "sandbox_dependency_network_and_secret_controls_unreported", "uploaded_data_privacy_unreported", "artifact_provenance_and_rollback_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_table_fairness_router_protocol_leakage_generated_code_execution_uploaded_data_privacy_provenance_and_rollback_check"
escalation_verdict: "require_reproducible_router_protocol_leakage_controls_and_execution_privacy_governance_before_strong_claims_or_deployment"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted evaluation-fairness and generated-code governance check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# LightAutoDS-Tab: Multi-AutoML Agentic System for Tabular Data

## 一句话总结

LightAutoDS-Tab 在 LLM 生成代码与 LLM 配置 AutoML 两条路线间编排 tabular ML pipeline；正文给出 8 个 Kaggle 数据集的单点成绩，但没有统一 router 选择结果、重复试验或预算控制，且“8 datasets”与“7 classification + 1 regression + 1 multi-target”计数矛盾。

## 系统与资源

论文提供 [代码](https://github.com/sb-ai-lab/LADS) 和 [demo video](https://youtu.be/sDUo_Ke2xs0)。用户上传 csv、xlsx 或 parquet，并用自然语言描述目标。

系统包含 Interactor、Planner、Generator、Validator、Improver、Executor 与 Interpreter 等 specialized agents。Router 选择：

1. **LLM-driven generation**：Planner 制定计划，Generator 用 Scikit-learn、CatBoost、TabPFN 等生成代码，Validator 检查，Improver 迭代；
2. **AutoML configuration**：LLM 解释问题和数据，为 LightAutoML、FEDOT 等生成配置；作者称架构可扩展到 AutoGluon。

Executor 执行和调试代码；Interpreter 生成非技术摘要，最终报告记录 pipeline decisions、generated code 和 trained model。双面板分别面向 expert 和 non-expert。

## Table 1 精确结果

| Dataset | LAMA+LLM | CodeGen | FEDOT+LLM | AutoKaggle | AIDE |
|---|---:|---:|---:|---:|---:|
| Titanic | 0.745 | 0.766 | **0.780** | 0.767 | 0.744 |
| Sp. Titanic | **0.798** | 0.788 | 0.790 | 0.771 | 0.793 |
| House Prices | **0.886** | 0.871 | 0.882 | 0.862 | 0.883 |
| Monsters | **0.774** | **0.774** | 0.733 | 0.723 | 0.721 |
| Ac. Success | **0.836** | 0.828 | 0.833 | 0.820 | 0.835 |
| Bank Churm | 0.883 | **0.885** | 0.881 | 0.856 | 0.786 |
| Ob. Risk | **0.905** | 0.888 | 0.904 | 0.896 | 0.896 |
| Plate Defect | **0.886** | 0.878 | 0.883 | 0.823 | — |

表中每行至少一个内部方法高于已列 baseline，但这不是统一 router 在不知道答案时实际选中该方法的结果。论文没有给 router 的 features、threshold、policy、fallback 或独立 routing accuracy，不能后验逐行取三个内部方法最大值来证明统一系统优越。

Plate Defect 的 AIDE 缺失，不能当作 0 或完整公平对比。

## 实验口径问题

正文说使用 **8 datasets**，随后写成 7 classification、1 regression、1 multi-target，算术上是 9；论文没有解释某个 dataset 是否同时属于两类。正式笔记保留这一原文矛盾，不自行修正。

数据按 classic（至 2024）和 modern（2024 后）各半划分，并提到 GPT-4o、GPT-4o-mini 的 knowledge cutoff。另称 GPT-4o 与 GigaChat2Max 的 CodeGen 对比详表在 GitHub；正文没有这些详细数值。

正文未报告：

- normalized performance score 的公式与归一化参照；
- runs、variance、seeds、confidence interval 或 significance；
- baseline version、configuration、search space；
- hardware、time limit、token limit、API cost 或总计算预算；
- router selection protocol 和 validation/stopping threshold；
- leakage、competition data access 或 pretraining contamination control；
- failure rate、runtime、branching cost 或 trained-model calibration。

因此 “superior”“outperforming”只能限定为 Table 1 的单点结果，不能扩展为统计显著或跨任务鲁棒结论。

## Interpretability 与 productivity

Interpreter summaries 和最终报告提供 traceability 接口，但论文没有用户研究、explanation faithfulness 或 debugging outcome。“full interpretability”与提高 data-scientist productivity 是作者结论，没有相应测量。

## 代码执行与数据治理

Generator 产出代码、Executor 直接执行和调试，且用户上传数据。论文未报告：

- process/container sandbox、resource limit 与 tool allowlist；
- dependency lock、package provenance 和 malicious package 防护；
- network egress、credential/secret isolation；
- uploaded dataset 的 consent、retention、access 和外部 LLM transmission；
- generated code/model/report 的 provenance、approval、versioning；
- failed iteration、unsafe artifact 和 trained model 的 rollback。

高风险评级来自可执行生成代码和数据处理治理缺口，不表示系统必然不安全。

## 页码核验

- p. 4155：身份、资源、摘要、架构图与动机；
- p. 4156：Table 1、两条路线、agents、UI、实验文本与结论；
- p. 4157：致谢和参考文献，无新增结果。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QBKY1209.pdf) 核验；`reviewed` 不表示统一 router、统计显著性、full interpretability、代码执行安全或数据隐私已验证。
