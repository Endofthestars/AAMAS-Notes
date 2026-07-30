---
title: "Towards Automated Integration of Novel ML Tools Into LLM-Driven AutoML Agents"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "planning_scheduling", "human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/PPZN3366"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PPZN3366.pdf"
code_url: "https://github.com/sb-ai-lab/AutoDS-Tools"
demo_url: "https://youtu.be/H_88VTaxsfs"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06b"
spark_draft_verdict: "source_grounded_with_required_url_evaluation_presenter_role_and_executable_tool_boundaries"
spark_qa_verdict: "needs_revision_corrected_page_map_url_inconsistency_and_absence_of_quantitative_evidence"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_page_demo_without_quantitative_evaluation", "significant_improvement_unsupported_author_claim", "two_inconsistent_repository_urls", "presenter_audit_role_not_audit_evidence", "arbitrary_repository_clone_and_static_analysis", "library_installation_and_supply_chain", "bash_jupyter_and_generated_code_execution", "session_virtual_environment_not_security_sandbox", "uploaded_dataset_privacy_unreported", "network_secret_resource_and_egress_controls_unreported", "dependency_pinning_provenance_approval_and_rollback_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_repository_url_execution_supply_chain_uploaded_data_privacy_session_isolation_and_unsupported_improvement_claim_check"
escalation_verdict: "major_revision_required_before_performance_or_security_claims"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted execution-governance and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Towards Automated Integration of Novel ML Tools Into LLM-Driven AutoML Agents

## 一句话总结

AutoDS-Tools 用六个 ReAct agents、累积结构化报告和 GRAD 图检索，把新的 GitHub ML library 接入 LLM-driven AutoML workflow；演示覆盖 repository analysis、library installation、bash/Jupyter 执行与生成 artifact，但三页正文没有任何定量实验，因此结论中的 “significant improvements” 只是未被正文数据支撑的作者主张，session-isolated virtual environment 也不能视为安全沙箱。

## 资源与 URL 不一致

论文提供 [演示视频](https://youtu.be/H_88VTaxsfs)，但在不同位置给出两个 repository URL：

- 摘要区：`https://github.com/sb-ai-lab/AutoDS-Tools`；
- 正文/补充材料描述：`https://github.com/AaLexUser/AutoDS-Tools`。

本目录暂以前者作为 `code_url`，因为它出现在论文摘要区；这只是编目选择，不表示两个地址已被作者澄清为同一权威版本。复现时应记录实际 URL、commit hash、依赖锁和检索日期。

## AutoDS-Tools 的六个 agents

系统以累积 structured reports 串联六个角色：

1. Analyst 探索 dataset、文件与基本结构；
2. Researcher 通过 Graph RAG 研究指定 library；
3. Manager 综合前两份报告，给 Coder 制定执行计划与 specification；
4. Coder 生成并迭代 data-processing/ML solution；
5. Debugger 捕获和修复错误，并试图避免污染主执行上下文；
6. Presenter 汇总结果，并被描述为审查 reproducibility、data handling、leakage risk 与 output quality。

每个 agent 运行 ReAct loop，交替 reasoning 与 acting；共享 toolkit 包含 bash execution、Jupyter notebook execution 和 GRAD documentation querying。Presenter 的审查是角色职责描述，论文没有给出审计 protocol、结果、日志或 independent validation，不能写成系统已经完成了泄漏或复现验收。

## GRAD：从 repository 到图检索

Graph RAG API Documentation（GRAD）把 API documentation 与使用示例组织进图检索流程：

1. 克隆 GitHub repository 并做 static analysis；
2. 抽取 public API entities，包括 classes、methods、functions，以及 docstrings、signatures 和 type hints；
3. 从 tests、notebooks 与 documentation 中挖掘 examples，去重并关联到相应 API；
4. 将结果送入基于 Cognee 的 GraphRAG knowledge graph；
5. 用定制 LLM prompt 建立 `has_method`、`belongs_to`、`is_used` 等关系和 semantic links；
6. agent 通过 `libq` 提交 GitHub URL 与自然语言问题，获得依据 API definitions 和 usage patterns 合成的回答。

这说明了文档摄取与检索的工程路径，但论文没有测量 API extraction accuracy、example association、retrieval quality、答案 faithfulness 或 stale-version error。

## 演示工作流

Web UI 允许用户提供 GitHub URL 填充 GRAD、通过 integrated Library Installer 安装 Python library、上传 dataset/辅助文件，并在 file explorer 中查看生成 artifacts。界面流式显示 code、tool outputs 和 intermediate analysis。

演示使用 Spaceship Titanic classification、LightAutoML 与 Qwen3-235B-A22B-Instruct。它展示系统如何运行，不是准确率、成功率或效率 benchmark。

## 完全缺失的评测

正文没有 experiments/results section，也没有 table 或 benchmark number。未报告：

- baseline、comparison 或 ablation；
- task success、predictive score、runtime、latency、token/API cost；
- API extraction、retrieval 或 generated-code correctness；
- debugging iterations、failure taxonomy 或 recovery rate；
- runs、variance、seeds、confidence interval 或 significance；
- human study、productivity 或 cross-library generalization。

因此结论所称 “demonstrates significant improvements over existing approaches” 没有正文定量证据。笔记不能把它改写成经验证的性能提升。

## 可执行工具与数据治理

系统接受 GitHub URL，克隆并静态分析 repository，安装 library，执行 bash/Jupyter/generated code，并处理用户上传的数据。论文提到 session-isolated virtual environments，但没有报告：

- container/process sandbox、filesystem boundary、tool/command allowlist；
- network egress、credential/secret isolation 与 exfiltration control；
- repository trust、malicious-code defense、commit pinning、signature/hash；
- dependency lock、package source verification、SBOM 与 supply-chain policy；
- CPU、memory、storage、time 与 recursive-execution limits；
- uploaded data consent、access、external LLM transmission、retention 与 deletion；
- generated artifact provenance、human approval、versioning 与 rollback。

这些是未报告的控制，不是已证明发生的攻击或数据泄露。高风险评级来自系统把不受信 repository、package、可执行代码与数据处理放在同一 agent workflow 中，而证据不足以界定其隔离和恢复能力。

## 页码核验

- p. 4158：题名、作者、摘要、资源、动机与系统总览；
- p. 4159：六个 agents、ReAct/报告链、GRAD、UI、演示设置与结论，并开始参考文献；
- p. 4160：致谢与余下参考文献，没有新增方法或实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PPZN3366.pdf) 核验；`reviewed` 不表示性能提升、复现审计、代码执行安全、供应链安全或上传数据隐私已经得到验证。
