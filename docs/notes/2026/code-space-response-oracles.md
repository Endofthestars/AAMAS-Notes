---
title: "Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/IKJF6607"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IKJF6607.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03c"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "llm_generated_executable_code", "prompt_and_model_dependency", "benchmark_scope", "code_sandbox_required"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models

## 一句话总结

CSRO 将 PSRO 的 best-response oracle 限制为有效、可执行的 Python 程序，由 LLM 合成代码策略；可用 LinearRefinement 或 AlphaEvolve 迭代改进。RRPS 和 Repeated Leduc Hold'em 的固定启发式评估表明部分变体可与基线竞争，但“可读代码”不等于正确、安全或已验证，且性能依赖模型、提示词、评估群体与严格沙箱。

## 方法与证据

- 两人对称零和 PSRO 维护 policy population，并对 empirical meta-game 求混合 \(\sigma\)；CSRO 让 LLM 基于游戏/API/对手描述生成可保持内部记忆的 Python best response（§2）。
- 为缓解上下文限制，系统使用自然语言对手摘要或只保留 \(\sigma\) support 最大的 top-k policies；LinearRefinement 在 utility 非正时循环修正，AlphaEvolve 让 LLM 作为程序 mutation operator（§2）。
- RRPS（5 seeds）中 LinearRefinement(code) 的 AggScore 为 122.1±9.8、PSRO-IMPALA 为 −532.1±41.5；Leduc（3 seeds）中 AlphaEvolve 的 PopExpl 为 4.4±0.6、CFR+ 为 0，指标和对手集合见 Tables 1--2。它们不是跨游戏、跨 LLM 或安全代码的证明。
- 作者明确依赖 base LLM 和 prompt quality，高维 observation games 的可扩展性未解决（§4）。

## 适用边界与复现

- 适合小型、API 明确、可隔离执行的策略研究。任何 LLM 代码都应进行 AST/API allowlist、资源/网络隔离、deterministic replay、单元测试和对抗审计；禁止直接进入生产控制。
- 复现应版本化模型、prompt、候选/迭代预算、摘要/top-k、AlphaEvolve selection、seed、opponent pool及 PopReturn/PopExpl/AggScore；独立评估混合策略 exploitability。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IKJF6607.pdf) 人工核对 CSRO、两种 refinement、表格结果与限制；未将代码可读性写成可验证或安全保证。
