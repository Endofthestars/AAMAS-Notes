---
title: "Reliable Data Science Analysis with Large Language Models via Multi-Agent Tools Orchestration"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/RPMN5314"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RPMN5314.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "data_analysis_agent", "tool_library_trust_assumption", "sandbox_details_unreported", "benchmark_execution_accuracy"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Reliable Data Science Analysis with Large Language Models via Multi-Agent Tools Orchestration

## 一句话总结

MATO 将自然语言数据分析拆分为预处理、任务规划、工具选择/参数化和 refinement 四个 agents；其核心是让 code agent 从带 source code 的已验证函数库调用工具，而不是直接自由生成全部代码，并在 Python sandbox 执行。摘要在修订过的 InfiAgent-DABench 六类任务上报告最高 98.43% execution accuracy；这验证的是特定基准的可执行结果，不能证明统计结论正确、工具库无害、sandbox 安全或对敏感/真实数据可靠。

## 方法与证据

- MATO state 为 \(S_t=(D_t,V_t,C_t)\)，输入 query 与 CSV。Data Preprocessing Agent 清理/编码；Task Planning Agent 产生 subtask plan；Code Generate Agent 按 semantic similarity 从 \(L_T\) 选工具、阅读其源代码并参数化；不匹配时从零生成代码；Refinement Agent 根据 schema/execution error 修复（Figure 1, §2）。这仍包含 LLM 的 planning、matching、parameterization 与 fallback code generation，故工具调用不能消除语义/统计/安全错误。
- library 覆盖 16 个 task categories，通过 LLM 生成问题/子任务并复用或生成函数；摘要称所有 additions 经过“rigorous validation”，最终 223 functions（§2、Figure 2），但没有定义 validation tests、coverage、版本/依赖、许可、人工 review、可重复构建、权限或 supply-chain controls。工具源代码可读也不等于 agent 正确理解或安全调用。
- 实验在作者“rectified for mathematical consistency”的 InfiAgent-DABench 版本、六类 core data-science tasks，以 ACC 评估；比较 InfiAgent 与 MetaGPT、GPT‑4.1/GPT‑4o/Claude-sonnet-4/Gemini-2.5-pro/Qwen-max（§3）。对 benchmark 的修订、tasks/splits、ground truth、execution environment、模型版本/提示、seeds/CI 和是否含 tool-construction 数据泄漏均未在摘要中完整说明。
- Figure 3/§3：GPT‑4.1 上 MATO 98.43%，MetaGPT 95.28%、InfiAgent 92.13%；Qwen 上 MATO 93.7%、MetaGPT 84.65%、InfiAgent 50.79%。ACC 可反映代码执行/期望输出，却不衡量统计假设、数据质量、因果解释、隐私、偏见、成本、长流程错误传播或面对恶意 CSV/query 的安全性。

## 适用边界与复现

- 适合探索受控数据分析任务的 tool-oriented LLM agent；不应在无人复核下用于医疗、金融、军事、公共政策或生产数据库分析，更不能把“可执行”当作正确、合规或可解释的分析结论。
- 复现需发布/固定 223 tools 与其 source/tests/licenses、16 categories、bootstrap prompt/threshold \(\tau/\theta\)、semantic matcher、agent prompts/models/versions、schema/refinement logic、sandbox image/permissions/resource limits、benchmark rectification、data splits/ground truth及每模型的多次结果。独立审计 tool correctness、dependency/SBOM、sandbox escape、network/file access和数据 retention。
- 应测试 malformed/adversarial data、prompt injection、tool-output poisoning、schema drift、missing/outlier/biased data、统计假设违反、跨域/大数据和多步骤错误恢复；报告 execution、numerical/statistical validity、human analyst rating、p95 cost/latency、privacy leakage与失败模式。生产使用需 least privilege、隔离、provenance、审计日志、人工审阅和明确不确定性。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM multi-agent/tool orchestration 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RPMN5314.pdf) 核验四 agents、223-tool library、InfiAgent-DABench、ACC与 Figure 3；没有把 benchmark execution accuracy 写成分析正确性、可靠安全或真实数据部署保证。
