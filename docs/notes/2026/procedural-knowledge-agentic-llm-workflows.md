---
title: "Procedural Knowledge Improves Agentic LLM Workflows"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/VEVZ5917"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VEVZ5917.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["arbitrary_code_and_api_calls", "human_coded_htn_dependency", "simplified_benchmark_scope", "sandbox_required", "prompt_constraints_insufficient"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Procedural Knowledge Improves Agentic LLM Workflows

## 一句话总结

ProcLLM 把程序性知识编码成 hierarchical task network（HTN），将复杂 agent goal 分解为有序 abstract/primitive tasks，再让 LLM 在 file/tool environment 中执行；手写 HTN 在四项基准显著提高成功率，甚至小模型可超过无 HTN 的大模型，但提升高度依赖人工程序知识，且系统允许任意代码/API 调用，论文明确要求在隔离环境复现。

## 方法与证据

- HTN 的 methods 将 abstract tasks 分解为有序 subtasks；ProcLLM 每轮先更新 task list，再向 action-LLM 提供当前 state、trace 与 task context。LLM 输出 internal verify 或 external read/write/append actions，外部动作以 JSON 调用（§3--4、Algorithm 1）。
- 测试三种条件：Human-TN（手写 task network）、LLM-TN（Gemini 2.5 Pro 生成）、No-TN（单一最终任务，类似 reflexion agent）；horizon 为 100，成功由人工编写 simulators/tests 自动验证（§5）。
- 四个 benchmarks 为简化 Travel Planner（43 single-city flight/hotel/return-flight instances）、synthetic Recipe Generator、PlanBench 改造 BlocksWorld 与 synthetic Unit Movement。Travel Planner 对 GPT-oss-120b，Human-TN 的 flight1/flight2/hotel success 为 0.814/0.605/0.395，No-TN 均为 0；Nemotron-70b 也从近零提升（Table 1）。
- 在 Recipe Generator，20 个实例中 GPT-oss-120b 从 No-TN 0% 至 Human-TN 25%。BlocksWorld 随 block 数复杂度上升时，120b Human-TN 仍约 70% 而 No-TN 低于 5%；Unit Movement 的 Human-TN 也提高不同模型/难度的成功率（§5.2--5.4）。
- LLM-TN 通常优于 No-TN、但弱于 Human-TN；task networks 常减少总 iterations、但增加每 iteration 开销。作者观察到 No-TN 会在读 request/spec 间循环，及一个 agent 试图在 Python script 内安装缺失 library 的未预期副作用（§6--7）。

## 安全边界与复现

- 实验集中包含简化 TravelPlanner、synthetic tasks、人工 tests 和可控 files/tools；成功率不证明开放网页、生产 API、企业 workflow 或高风险行动环境的可靠性。
- 手写 HTN 是重要 expert input，论文并未证明能自动从任意文档可靠抽取、验证、更新或冲突消解 procedural knowledge；LLM-TN 的不足也表明程序细节/coverage 是瓶颈。
- HTN/prompt 限制不是 security boundary：任意 code/API ability 可能产生 package install、文件/网络副作用、credential exposure、resource exhaustion 或 tool misuse。必须以 allowlisted tools、least privilege、egress controls、sandbox、auditable logs、human approval 和 rollback 约束。
- 复现应固定 task networks、prompts、models/versions、tool schemas、horizon、environment snapshots、verifier、seeds、timeouts 与 success definitions；在无网络/无权限 sandbox 运行，测量副作用、cost、loop/timeout rate 与 adversarial prompts，而不只报 task success。

## 与 AAMAS 的关系与核验说明

这是将经典任务网络程序知识加入 LLM agent workflow 的规划/工程工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VEVZ5917.pdf) 核对 ProcLLM、四项基准、Table 1、LLM-TN 对比和 sandbox 警告；没有将 benchmark 成功或 HTN 约束表述为 agent 安全保证。
