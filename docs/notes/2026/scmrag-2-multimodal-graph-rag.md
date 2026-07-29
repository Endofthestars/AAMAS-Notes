---
title: "SCMRAG 2.0: Efficient and Scalable Multi-hop Graph RAG with Multimodal Knowledge-Graphs and Agentic Self-Correction"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "safety_verification"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AYBA8976.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02j"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["rag_evaluation_scope", "self_correction_not_factuality_guarantee", "external_source_governance", "pdf_doi_mismatch"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# SCMRAG 2.0: Efficient and Scalable Multi-hop Graph RAG with Multimodal Knowledge-Graphs and Agentic Self-Correction

## 一句话总结

SCMRAG 2.0 将文本、图像和结构化数据处理为带 symbolic 与 embedding 双链接的多模态知识图，并用 self-corrective agent 反复检索、核验与扩展证据；摘要在 MMLU 与 MRAG-Bench 上报告优于 LightRAG/RAG-Anything 的指标。

## 方法与证据

- 证据 tuple 为 `(claim, target, topic, z)`，其中 z 是 claim/target/topic 的联合 embedding。symbolic edges 来自共享 topic、target 或显式 metadata references；embedding edges 来自 target/topic 向量超过 cosine-similarity thresholds（§2.1）。
- 检索流程：先取 top-k nodes 生成初答，再计算答案与证据的 consistency score；低于 threshold 时，agent 标注 modality gaps、重写 query，并通过图遍历和/或 external knowledge sources 补证，直至达标或 `T_max`（§2.2）。
- 使用 Qwen2.5-VL-32B-Instruct 作为生成/tool-reasoning backbone、jina-embeddings-v4 编码；对 MMLU 比 LightRAG，Table 1 报 accuracy 86.00% vs 75.40%，MRAG-Bench 比 RAG-Anything 为 60.15% vs 45.52%。
- 摘要报告 full pipeline 在 MMLU 比 Retrieval Only +3.58%、比 Self-Correction Only +2.82%，但没有 token/latency/成本、数据构建、prompt、检索 hyperparameters、方差或显著性检验的完整细节；“efficient/scalable”“factuality”只能按该评测协议理解。

## 适用边界与复现

- self-correction 的 evidence-consistency score 不是事实真值、来源权威性、时效性、偏见或安全性的保证；若 graph/embeddings/外部源本身错误、过时或受污染，循环可强化而非消除错误。
- MMLU 主要是知识/推理 benchmark，不等同于真实多模态 RAG 的 grounded generation；MRAG-Bench 的增长也不能证明任意知识库、语言、文档结构或高风险场景下可靠。
- 外部知识查询及跨模态 linkage 带来隐私、版权、注入攻击、来源许可和审计问题，摘要未描述 trust policy、citation/provenance UI 或 adversarial evaluation。
- 复现应发布数据摄取/claim extraction、graph schema/thresholds、检索/pruning、agent prompts/model versions、external-source allowlist、stopping/consistency rules、seeds、每项成本/延迟与 groundedness/hallucination 人工审计；部署应保留来源链接、用户复核和拒答机制。

## 与 AAMAS 的关系与核验说明

这是多模态 RAG 与 agentic retrieval 的系统工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AYBA8976.pdf) 核对 §2--4、Table 1；该 PDF 标注 DOI `10.65109/GGJL7344`，与官方目录/文件 ID `AYBA8976` 不一致且目录无 DOI，故元数据 DOI 暂留空以避免错配。
