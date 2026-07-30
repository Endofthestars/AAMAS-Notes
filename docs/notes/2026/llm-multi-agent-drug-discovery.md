---
title: "A Demonstration of an LLM-based Multi-agent System for Drug Discovery"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "safety_verification", "human_agent_interaction", "applications"]
dblp_key: ""
doi: "10.65109/KAPY7208"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KAPY7208.pdf"
code_url: "https://github.com/MolecularAI/langdmta-lab"
demo_url: "https://doi.org/10.5281/zenodo.18195147"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05q"
spark_draft_verdict: "needs_revision_for_risk_taxonomy_benchmark_evidence_internal_public_and_drug_validation_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_high_risk_taxonomy_tool_sequence_benchmark_code_tense_and_biomedical_safety_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["tool_sequence_benchmark_not_answer_validation", "benchmark_metrics_runs_seeds_variance_and_baselines_missing", "llm_judge_not_yet_implemented", "public_foundational_subset_differs_from_internal_system", "proprietary_and_licensed_scoring_not_public", "shown_functions_insufficient_for_routine_daily_use", "molecule_and_synthesis_feasibility_not_systematically_validated", "admet_toxicity_efficacy_wet_lab_and_clinical_validation_missing", "human_approval_workflow_unreported", "prompt_injection_and_tool_misuse_unreported", "local_llm_generated_python_sandbox_unreported", "access_control_ip_and_data_leakage_unreported", "audit_and_rollback_unreported", "chemical_dual_use_governance_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_internal_public_system_tool_sequence_benchmark_molecular_validation_human_approval_local_code_execution_data_governance_and_dual_use_boundary_check"
escalation_verdict: "needs_revision_corrected_for_tool_sequence_evidence_code_release_tense_internal_public_and_biomedical_safety_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted biomedical-tool and code-execution risk check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# A Demonstration of an LLM-based Multi-agent System for Drug Discovery

## 一句话总结

该系统用一个 supervisor 编排 Design、Synthesis、Analyze、Utility 四个 LLM sub-agents 与化学工具，服务于分子生成、评分、逆合成和数据分析；论文提出的是工具路由 demo 与 benchmark strategy，没有报告工具序列准确率、最终答案质量、湿实验或药效安全验证。

## 科学与系统边界

这是 AstraZeneca 开发的 LLM-based multi-agent tool-orchestration system，面向 drug-discovery computational tasks，不是新的 molecular model、autonomous wet lab 或 clinical discovery proof（pp. 4092–4093）。

系统覆盖 analog generation、compound scoring 和 synthesis planning，但这些计算输出不能自动建立：

- molecule chemical feasibility；
- synthesis route 的实际可执行性；
- ADMET、toxicity 或 efficacy；
- wet-lab reproducibility；
- clinical safety 或 therapeutic benefit。

论文所说的 robustness、reliability、reproducibility 与 end-user trust 是构建 benchmark 的动机和目标，不是已经由本文数值验证的结论。

## Supervisor 与迭代路由

用户 natural-language prompt 先交给 supervisor（pp. 4092–4093）：

1. supervisor 选择合适的 sub-agent；
2. 根据请求生成 task description；
3. sub-agent 用 LLM 把指令转成 external tool-call sequence；
4. supervisor 接收并评估结果；
5. 必要时继续路由后续任务，直到产生 final response。

这是多智能体工具编排流程。论文没有给出 supervisor “评估”结果时采用的完整 acceptance criteria，也不能把它理解为独立的科学审核或人类审批。

## 四个专用 Sub-agents

### Design

Design agent 使用 REINVENT 4 的不同 running modes 生成 novel compounds 或进行 scoring（p. 4093）。

许多 scoring functions 属于 proprietary capability 或需要 software license，公开代码只支持部分 basic scoring functions。因此公开版本不能被视作内部 Design capability 的完整复现。

### Synthesis

Synthesis agent 使用：

- **AiZynthFinder**：做 retrosynthesis 并预测 synthesis plan；
- **Precedent Finder**：在 historical reaction database(s) 中寻找相近 reaction analogs。

工具生成的路线仍需要化学可行性、材料可得性、条件、安全和实验结果验证。

### Analyze

Analyze agent 来自 LangChain ecosystem。LLM 生成 Python code，再由 local Python executable 执行，用于 Pandas dataframe 的 manipulation、statistics 或 plots（p. 4093）。

这种能力提高了灵活性，也带来 code-execution 风险。三页稿没有说明 sandbox、filesystem/network permissions、package allowlist、resource limits、prompt-injection defense 或 rollback。

### Utility

Utility agent：

- validates chemical structures in SMILES format；
- 查询 PubChem，把 common molecule name 转为 SMILES。

SMILES format validation 只说明表示形式可被解析，不等同于该分子稳定、可合成、安全或有效。

## 实现栈

agent code 使用 Python 与 LangChain，tools 以 MCP（Model Context Protocol）servers 提供，LLM 使用 GPT-4o（p. 4093）。

MCP 是工具接口协议，不是本文训练的新模型；GPT-4o 也是外部使用的基础模型，论文没有报告 fine-tuning。

## Internal system 与公开版本

公开代码反映内部平台的 structural complexity，但只是 foundational subset（p. 4093）：

- internal API access restrictions 使部分功能不能公开；
- proprietary/licensed scoring 不在公开版完整提供；
- core user group 认为论文所展示的这些功能本身不足以支持 routine day-to-day use；
- additional capabilities 包括 matched molecular pair analysis，另有 multiple internal database integrations 处于计划中。

因此，“为 AstraZeneca scientists 内部使用而开发”和“本稿公开子集不足以支持日常工作”需要同时保留；不能把公开版描述成完整 production system。

## Table 1：五个 benchmark examples

Table 1 位于 p. 4093：

| Question | Sub-agent sequence |
|---|---|
| What is the SMILES of Ibuprofen? | Utility |
| Can you generate molecules similar to `[SMILES string]`? | Design |
| How many compounds have MW between 500 and 600, HBD < 3 in `smiles.csv`? | Analyzer |
| Can you generate molecules similar to Gleevec but with lower logD? | Utility → Design |
| Can you generate molecules similar to Gleevec with lower HBA, higher MW, logD between 1 and 3, number of rotatable bonds ≤ 9? | Utility → Design → Analyzer |

这些是 example questions 与预期路由，不是五项成功率结果。

## Benchmark 实际检查什么

作者构建 typical user-prompt test suite，并提供 optional mock tool outputs（p. 4093）。使用 mocks 时，外部 tool execution 可以完全 deterministic 且更快，但 LLM routing 本身仍需通过 traces 检查。

执行由 LangFuse 追踪，评测把 agent 选择的 tool sequence 与 predefined ground-truth sequence 比较。它检查的是 orchestration 是否按预期选路，不等于：

- final answer 在化学上正确；
- generated compound 满足真实 design objective；
- synthesis plan 可在实验室执行；
- 整个 drug-discovery decision 有效。

LLM-as-a-judge 用于 final-answer evaluation 仍处于 “in the process of implementing”，不能写成已经完成。

## 没有报告的评测结果

三页稿没有给出：

- test-suite 总问题数与覆盖率；
- tool-sequence accuracy；
- final-answer accuracy 或 expert rating；
- runs、seeds、variance 或 confidence interval；
- failure-mode breakdown；
- baseline 或 ablation；
- 与其他 agentic systems 的 cross-system comparison。

作者明确说 benchmark 关注该系统完成其特定任务的能力，不比较 published architectures；不同 toolsets、prompts 与 workflows 紧密耦合，因此 universal “state-of-the-art” architecture 并未定义。

## 生物医药与工具治理缺口

进入真实研发流程前，还需要短稿未说明的控制：

- scientist review 与 final human approval；
- molecular/synthesis outputs 的 staged computational 与 wet-lab validation；
- tool-level authentication、authorization 与 least privilege；
- prompt injection、malicious files 和 tool-output poisoning 防护；
- Analyze agent 本地代码执行的 sandbox 与 resource isolation；
- proprietary data、internal APIs、chemical IP 和 model traces 的 access/retention policy；
- action audit、incident response 与 rollback；
- 对潜在有害化学设计和 synthesis guidance 的 dual-use governance。

LangFuse tracing 提供执行记录能力，但论文没有把它描述成完整的安全审计、审批或回滚机制。

## 资源、结论与页码核验

论文写作时的 Code Availability 表述是 public code **will be released prior to the demonstration**，并给出 [GitHub 地址](https://github.com/MolecularAI/langdmta-lab)。演示材料位于 [Zenodo](https://doi.org/10.5281/zenodo.18195147)。

PDF 逐页核对：p. 4092 为 identity、Abstract、Introduction 与 Agent Overview 起始；p. 4093 为 Agent Overview continuation、Table 1、Benchmarking、Conclusions 与 Code Availability；p. 4094 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KAPY7208.pdf) 核验；`reviewed` 不表示 molecule、synthesis、wet-lab、clinical outcome 或 production governance 已经验证。
