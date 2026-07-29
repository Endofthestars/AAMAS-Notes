---
title: "Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of the Model Context Protocol"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "safety_verification"]
dblp_key: ""
doi: "10.65109/GMHB4353"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GMHB4353.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "tool_using_llm_agent", "mcp_style_abstraction", "martingale_assumptions", "deterministic_tools", "not_security_or_correctness_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of the Model Context Protocol

## 一句话总结

本文把 MCP-style tool chain 中 response 相对每步 ideal fact set 的语义失真累加；在有界 branching、response stability 和几何时序衰减的假设下，以 Doob martingale/Azuma concentration 得到累计失真相对其期望的高概率偏差为 \(O(\sqrt{T})\)，而非随链长超线性放大。Qwen2-7B-Instruct 与 Llama-3-8B-Instruct 配合确定性 MCP tools 的实验与该趋势相符；这是对定义的 metric 与假设模型的条件性分析，不保证工具输出真实、MCP 安全、权限正确、无 prompt injection 或端到端任务成功。

## 方法与证据

- 每步失真 \(\Delta_t=(1-\lambda)d^w_{set}(R_t,I_t)+\lambda d_{emb}(R_t,I_t)\)：前者为 extracted facts 的 weighted Jaccard distance，后者为 normalized cosine embedding distance，二者均在 \([0,1]\)；累计 \(D(T)=\sum_t\Delta_t\)（Eq. 1, §2）。因此结论依赖 ideal fact set、fact extraction、embedding、weights 和 \(\lambda\) 的选择；它并未直接测 API 行为、事实真值、工具副作用或用户目标。
- 依赖假设为 branching \(\beta B<1\)、\(\phi(i,j)=\beta^{j-i}\) 的 influence、response stability，以及 sensitivity \(\alpha\) 的 temporal decay。由此构造 \(Z_t=E[D(T)\mid\mathcal F_t]\)，其 increment 由 \(1+\alpha/(1-\beta B)\) 限制（§2）。若长程依赖不衰减、工具共享隐状态/外部世界变化、模型自适应重试或 errors 有系统性偏差，这些前提可能不成立。
- Theorem 2.1 给任意 \(\eta\) 的单侧 concentration inequality；等价地，以至少 \(1-\eta\) 概率，\(D(T)\) 不超过 \(E[D(T)]\) 加上依赖常数放大的 \(\sqrt{2T(1+\gamma^*)\ln(1/\eta)}\)。它约束的是相对期望的波动而非期望本身：如果 per-step mean distortion 很高，总失真仍可线性增长；\(\beta B\to1\) 时 bound 仍有效但变保守。
- 实验使用 Qwen2-7B-Instruct、Llama-3-8B-Instruct 和 deterministic MCP tools；图示设 \(\beta=0.7,\lambda=0.5\)，每 model 50 chains。作者报告累计 distortion 与约 0.5 的 per-step linear trend 相符且均落在 \(O(\sqrt T)\) envelope 内；\(\lambda\) 从 0 到 1 减少约 80% measured distortion，\(\beta=0.98,T=60\) 时未出现指数失败（§3）。这不能区分“metric 更宽容于 paraphrase”与真实 factual correctness 的改善。
- 摘要给出的实践含义是缩短未 re-grounded chain、降低 lossy paraphrase/summarization、在线监控 distortion proxy 并调整 cadence。完整 proof、metric estimation 和扩展实验被指向 arXiv full version，未在本笔记以外核验；摘要没有攻击模拟、真实互联网/API、复杂 MCP server、权限模型或高风险实际决策评估。

## 适用边界与复现

- 适合把它作为 tool-chain fidelity 的诊断框架或再 grounding 的候选触发信号；不得将 \(O(\sqrt T)\) concentration 当作事实核验、工具可靠性认证、MCP 协议安全审计、数据保密/合规保证或医疗、金融等高风险自动化授权。
- 复现需公开任务/ideal facts、fact extractor 与 weights、embedding model/normalization、\(\lambda,\alpha,\beta,B\) 的估计与 validation、tool definitions/versions、prompts/decoding、chain construction、models、50-chain sampling/seeds和完整 raw trajectories。应分别报告 \(E[D(T)]\)、deviation、coverage、calibration及 factual/tool-task metrics，而不是只给 envelope plot。
- 应检验 non-deterministic/failing tools、network delay、tool output distribution shift、long contexts、parallel/fan-out calls、memory/retries、malicious/poisoned tool responses、prompt injection、access-control errors 和 real MCP servers。生产系统仍需 schema/input validation、least privilege、provenance、sandboxing、independent fact checking、human approval、logging/rollback和 incident response。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM agent/tool-use 理论与实证扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GMHB4353.pdf) 核验 hybrid metric、dependence assumptions、Theorem 2.1、两种模型与 deterministic-tool experiments及作者列出的 re-grounding implications；没有把相对期望的 concentration 或 embedding similarity 写成 MCP 安全、真实工具正确性或部署可靠性证明。
