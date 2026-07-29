---
title: "Role-Based Orchestration of sLLM Agents for Korean Instruction-Following: A Comparison with SOTA"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/GGVB5420"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GGVB5420.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "korean_instruction_following", "small_llm_orchestration", "llm_as_judge", "350_item_evaluation", "cost_estimation", "not_factuality_or_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Role-Based Orchestration of sLLM Agents for Korean Instruction-Following: A Comparison with SOTA

## 一句话总结

RBO 将 Korean-centric small LLMs 排成 Generator → Critiquer → Reviser，并由 rule-based Adaptive Controller 按 format/count/factuality constraints 决定 simple/complex path、Validator 做 Pass/Fail retry。350 个 KoAlpaca items 上，RBO 对 GPT-4o/DeepSeek-V3.2 的总体胜率为 38.8%/43.1%，但在 strict constraint-heavy brainstorming 有局部优势；作者估计其每请求约 1.82 TFLOPs（DeepSeek 17.45）且自有部署 API cost 近零，E2E latency 6.14s 比 GPT-4o 2.56s 慢。结论是特定模型、任务与成本假设下的效率—质量取舍，不证明事实性、韩语文化适配、隐私或主权 AI 安全。

## 方法与证据

- Controller 从 instruction 取 format/count/factuality signals，strict constraint 时走 \(G\to C\to R\)，否则 simple path；Generator restricted to instruction/internal knowledge，Critiquer 产 defect report，Reviser 改稿，Validator 按 schema/count/safety binary check 并 retry（§2）。规则 extraction/validator coverage本身可能漏掉语义、事实、偏见或安全问题；“factuality constraint”不是外部检索/证据核验。
- 实验采用 350 KoAlpaca samples、7 categories；Generator SKT A.X 7B、Critiquer KT Mi:dm 2.3B、Reviser HyperCLOVA X 3B，比较 GPT-4o 与 DeepSeek-V3.2。judge 为 Claude-4.0-Sonnet/Gemini-2.5-Pro/Grok-4 panel 和 blinded human evaluation（§3.1）。摘要未给 sampling procedure、human rater count/agreement、judge prompt/order bias、models/version/date、category counts、CI或 raw outputs。
- overall RBO win rate 是 38.8% vs GPT-4o、43.1% vs DeepSeek；test–retest Pearson \(r\approx0.96\) 描述 independent runs 的一致性，不等价于正确性、显著优越性或真实用户偏好。Brainstorming \(p=0.533\) 据称超 GPT-4o；Generation underperforms \(p=0.170\)，judges 描为 dry/resume-like（§3.2）。
- efficiency claims：RBO 1.82 TFLOPs/request，DeepSeek 17.45；on-premise API cost约 $0、GPT-4o comparable workload估计 $0.46，latency 6.14s vs 2.56s（§3.3）。这些依赖 hardware, token lengths, throughput, electricity, amortization, licensing与 pricing assumptions，且不含 deployment/maintenance/training/validator retries等完整成本。
- RBO 确能提高 count/format adherence 的可能性，但 LLM internal knowledge limitation不能避免 hallucination；sequential critique可抑制 creative diversity。论文没有网络安全、data governance、privacy threat model、copyright、Korean demographic fairness或 high-stakes evaluation。

## 适用边界与复现

- 适合受限算力环境中将 instruction constraint checking 与 draft revision 分离的原型；不要用 multi-agent chain 替代事实核验或安全审查。高风险输出须检索/来源验证、policy filters、human approval、audit logs和 reversible delivery。
- 复现应发布 350 item ids/splits、Korean models/weights/prompts/decoding、controller rules/mode paths、validator/retry limits、judge/human protocol、blinding、win/tie/loss criteria、hardware/token/pricing accounting和 seeds。逐项报告 category metrics/CI、constraint pass rate、hallucination/factuality、latency and retry costs。
- 应测试 unseen Korean dialects/domains、long/multi-constraint instructions、jailbreak/prompt injection、retrieval-required facts、bias/safety cases、model outages和 different cost regimes。比较 learned routing、single-model tool use与 equivalent token/latency budgets，审计每 role 添加的边际质量和风险。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 sLLM multi-agent orchestration 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GGVB5420.pdf) 核验 roles/controller/validator、350-item setup、win rates、TFLOPs/cost/latency figures和 generation weakness；没有将估算成本或 constraint adherence写成事实性、隐私或安全保证。
