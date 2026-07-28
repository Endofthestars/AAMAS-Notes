---
title: "RocqStar: Leveraging Similarity-driven Retrieval and Agentic Systems for Rocq generation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: "10.65109/ZQXK7747"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ZQXK7747.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["benchmark_and_generator_dependence", "retrieval_dataset_construction_dependence", "agent_cost_and_retry_dependence", "specification_correctness_not_guaranteed"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# RocqStar: Leveraging Similarity-driven Retrieval and Agentic Systems for Rocq generation

## 一句话总结

RocqStar 用 proof-aware self-attentive embedder 检索相近 proof，再以 coq-lsp MCP 上的 plan→execute→reflect agentic workflow 生成 Rocq proof；在 IMM/CoqPilot 基准中 retrieval 与 multi-agent debate/reflection 改善成功率，但效果依赖 generator、重试、critic、检索语料和 benchmark，且通过的 proof 只证明给定 specification。

## 方法与证据

- 从 BigRocq 挖掘 76,524 statement-proof 对，训练 contrastive embedder 学习 proof-distance 相似性；相对 text/Jaccard retrieval baseline，evaluation set 的 generator performance 最多相对升 28%（§2、§4.1）。
- agent 通过自建 coq-lsp MCP 操作 Rocq，包含 planner、executor、critic/replanner；planning 用 two rounds MAD，超过五次 proof-check 后反思/重规划（§3--4）。
- 在 IMM-300（CoqPilot-derived）比较 generator/retriever；paper 报 agent 能解最多 60% theorems，reflection 令 overall success 从 48% 到 66%，complex group 有更大相对改善；MAD ablation 在 IMM-50 上进行（§4）。
- code、retriever/data 与 checkpoint 按论文链接公开，但 success rate 是在特定模型、prompt、retry budget 与已构造语料下的 theorem-level pass rate（§2--4）。

## 局限与复现

- retrieval 受 BigRocq mining、train/eval split、proof corpus、statement/proof format 与 lexical leakage 控制影响；IMM-50 与 IMM-300 的不同用途不能直接横比。
- agent 的成本、延迟和性能取决于多模型调用、MAD 轮数、critic 强度、五次检查阈值和 pass@ retry protocol；应报告每 theorem tokens/calls/墙钟与失败类别。
- Rocq 接受生成 proof 表示其符合给定 formal statement/axioms，不证明 specification 对真实需求完整、无误或安全；形式验证边界在规格。
- 复现应固定 Rocq/coq-lsp、generator/critic version、prompt、retriever index、seed、benchmark split 与失败日志，并在外部项目和有意干扰的 specs 上验证。

## 与 AAMAS 的关系与核验说明

该文研究 LLM agent 支持的 interactive theorem proving。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ZQXK7747.pdf) 核对 retrieval、agent 流程、IMM 数据和 ablation；未将 proof-generation benchmark 成功率表述为完整软件安全保证。
