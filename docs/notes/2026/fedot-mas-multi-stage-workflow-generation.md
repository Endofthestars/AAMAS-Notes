---
title: "FEDOT.MAS: Generating Multi-Agent Systems for Complex Tasks with Multi-Stage Validation"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["agent_engineering", "safety_verification", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/OOIG5670"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OOIG5670.pdf"
code_url: "https://github.com/ITMO-NSS-team/FEDOT.MAS-Demo"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05n"
spark_draft_verdict: "source_grounded_with_static_validation_comparability_cost_and_stability_overstatement"
spark_qa_verdict: "needs_revision_corrected_for_local_static_checks_percentage_point_results_baseline_cost_security_and_reproduction_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["generated_code_execution", "web_file_and_browser_tool_permissions", "sandbox_and_isolation_not_reported", "single_table_baseline_comparability_unknown", "runs_seeds_and_uncertainty_missing", "llm_judge_identity_prompt_and_calibration_missing", "stage_ablation_and_error_catch_rates_missing", "token_saving_measurement_missing", "benchmark_contamination_not_addressed", "average_cost_without_baseline_or_variance", "validation_not_security_proof", "reproduction_manifest_missing"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_pipeline_static_runtime_quality_validation_gaia_comparability_cost_generated_code_security_and_reproducibility_check"
escalation_verdict: "needs_revision_corrected_for_static_check_result_comparability_cost_security_evaluation_and_reproducibility_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted generated-code, evaluation, and cost-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# FEDOT.MAS: Generating Multi-Agent Systems for Complex Tasks with Multi-Stage Validation

## 一句话总结

FEDOT.MAS 从自然语言 specification 生成可复用的 executable Python multi-agent workflows，并通过七阶段、static/runtime 双反馈循环逐层修复；论文在 GAIA 报告高于 MAS-GPT 的三档 accuracy，但缺少重复运行、严格 baseline 配置、阶段消融、judge 细节和生成代码 sandbox/permission 证据。

## 生成对象与贡献边界

本文把 multi-agent system 定义为 **LLM-orchestrated pipelines where specialized agents coordinate through generated code**（p. 4077）。系统输入 natural-language task description，输出 complete executable Python workflow。

生成目标是 **task classes**：一组结构相似的 tasks 共享 agent topology，但输入参数不同，例如“retrieve and summarize a web page”。贡献不只是单个 function，而是 agents、state、tools、dependencies 和 coordination logic 的整体代码。

论文把 FEDOT.MAS 与 ADAS、AFlow、SwarmAgentic、GPTSwarm、传统 code generation 和 MAS-GPT 区分，但没有在统一 protocol 下逐一 benchmark；相关工作描述不能单独证明全面优越。

## 七阶段 pipeline

系统按七个 stages 执行，并在不同成本点阻止错误传播（pp. 4077–4078）：

1. **Meta-Planning**
2. **Code Generation**
3. **Static Validation**
4. **Emission**
5. **Execution**
6. **Runtime Validation**
7. **Quality Assessment**

有两个 feedback loops：

- static debugging，最多 10 iterations；
- runtime refinement，最多 3 cycles。

execution timeout 为 600 seconds。

## Meta-Planning

GraphMetaAgent 使用 Claude Haiku 4.5。system prompt 描述所选 MAS framework primitives、可用 MCP tools 和 state-management patterns（p. 4078）。

它输出 JSON plan，包括：

- agent roles 与 descriptions；
- tool assignments；
- state graph structure；
- data flow；
- input/output state keys。

plans 映射到 framework primitives：agents 成为 nodes，dependencies 成为 edges，custom `TypedDict` state 配合 annotated reducers 处理 communication。planner 根据 tool count 与 reasoning steps，在 linear pipeline、conditional branching 和 parallel execution 中选择 architecture。

## Code Generation

GraphCoderAgent 把 validated plan 转成 Python code，使用四类 templates：

- **State**：`TypedDict` 与 annotated reducers；
- **Node**：agent functions、structured outputs 与 MCP tool bindings；
- **Graph**：nodes、edges 与 entry point；
- **Tools**：web search、file analysis、browser automation 等 MCP server configuration。

这些 templates 约束代码结构，但论文没有报告 template validity rate、unsupported task patterns 或跨 framework portability。

## Static、runtime 与 quality validation

### Static Validation

Stage 3 在本地、**不调用 LLM 或 API**，运行：

- `py_compile`；
- `ruff`；
- type checker。

论文明确说它在昂贵 execution 前捕获 syntax 和 import errors。GraphDebugAgent 用 patch mode 做 line-level changes，最多 10 次；作者声称相对 full rewrite 节省 80–90% tokens，但没有给原始 token accounting、sample size 或计算方法。

### Emission 与 Execution

Stage 4 写出 code 并做 version tracking。Stage 5 异步执行 workflow，并设 600s timeout（p. 4078）。version tracking 与 timeout 是工程控制，不等于 generated code 已被 sandboxed 或安全验证。

### Runtime Validation

Stage 6 检查 execution results，最多触发 3 次 targeted refinement。作者列举 static analysis 不能捕获的 semantic errors：

- wrong API parameters；
- data-transformation errors；
- file-format assumptions。

论文没有给各 error class 的发生数、catch rate、false positive/negative 或修复成功率。

### Quality Assessment

Stage 7 用 LLM judge 评估 answer completeness 与 execution efficiency；low-quality result 触发 code regeneration。

正文没有披露 judge model、version、prompt、rubric、threshold、temperature、calibration、human agreement 或 bias analysis，因此质量判定本身不可独立重放。

## GAIA evaluation

评估使用 GAIA 的 165 tasks，按难度分为 52 / 86 / 27 个 Level 1 / 2 / 3 questions（p. 4078）。

论文披露配置：

- Gemini-2.5-Flash via OpenRouter；
- static/runtime iteration limits 10/3；
- timeout 600s。

Table 1 报告：

| Method | Level 1 | Level 2 | Level 3 |
|---|---:|---:|---:|
| FEDOT.MAS（Ours） | 49.0% | 24.4% | 15.4% |
| MAS-GPT | 32.1% | 19.8% | 11.6% |
| 差值 | +16.9 pp | +4.6 pp | +3.8 pp |

差值是 percentage points，不是相对百分比。该表支持“在所报口径下数值更高”，但正文没有说明：

- MAS-GPT 是否使用相同 base model、tools、retrieval/data access、timeout 和 token budget；
- baseline 是作者复跑还是引用结果；
- judge 与 answer-scoring protocol 是否完全相同；
- runs、random seeds、repeated tool outcomes、variance、confidence interval 或 significance。

因此不能把单表写成稳定可复现增益、严格 controlled head-to-head 或全面 state-of-the-art。

## Cost 声明

作者报告 FEDOT.MAS **average cost $0.32 per task**，并称其与 similar-scale state-of-the-art MAS operating costs comparable（p. 4078）。

论文没有提供：

- MAS-GPT 或其他 baseline cost；
- input/output/tool tokens 与各 stage/API 的 breakdown；
- mean 的 run/task distribution、variance、median 或 tail；
- failed/retried tasks 是否计入；
- provider pricing snapshot；
- cost significance 或等价区间。

所以“without a significant increase in cost”只能理解为作者的定性措辞，不能解释为统计检验结论。

## Generated-code safety 边界

系统生成并异步执行可绑定 web search、file analysis 和 browser automation tools 的 Python code。论文描述了 syntax/type/runtime/answer-quality checks，但没有说明：

- process/container sandbox；
- filesystem/network boundary；
- tool allowlist 与 least-privilege permissions；
- credentials、secrets 或 untrusted content handling；
- prompt injection、malicious webpage/file 或 generated-code policy；
- resource quotas（timeout 之外）、audit、human approval、rollback；
- dependency provenance 或 supply-chain checks。

不能据此断言系统存在某个具体 exploit；但多阶段 validation 也不能替代 security validation。生产使用需要隔离执行、capability controls、schema enforcement、secret protection、human approval 和 adversarial testing。

## 评估与复现缺口

除上述问题外，三页稿没有报告：

- stage ablation 或 feedback-loop causal contribution；
- static/runtime/quality stage 的 catch-rate 与 failure breakdown；
- GraphMetaAgent/GraphCoderAgent prompts、sampling 和 versions；
- contamination/leakage control；
- exact MCP servers、tool versions 和 credentials policy；
- task-level predictions、logs、seeds 与 evaluation script；
- environment lock、commit/tag 与完整 run manifest。

论文提供 [code/demo repository](https://github.com/ITMO-NSS-team/FEDOT.MAS-Demo) 和 [demo video](https://youtu.be/1w8bBWGHjeQ)，为进一步核验提供入口，但三页稿没有 pin 与 Table 1 对应的 exact artifact state。

## Future Work

作者只明确提出：根据 execution results 扩展 validation criteria（p. 4078）。这尚未实现，也没有在本文给出新增 criteria。

## 页码与核验说明

PDF 逐页核对：p. 4077 为 identity、Abstract、Introduction、MAS/task-class 定义、七阶段概览、双 feedback loops 与 System Architecture 开端；p. 4078 为 Stages 1–7 细节、GAIA Table 1、cost、Conclusion/Future Work；p. 4079 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OOIG5670.pdf) 核对 pipeline、GAIA 数字、percentage-point differences 与安全/成本边界；`reviewed` 不表示 baseline 公平性、validation 因果效果、成本等价、生成代码安全或 production readiness 已经验证。
