---
title: "DomAgent: Leveraging Knowledge Graphs and Case-Based Reasoning for Domain-Specific Code Generation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/HSTL5347"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HSTL5347.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03x"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "coding-agent", "knowledge-graph-retrieval", "case-based-reasoning", "industrial-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DomAgent: Leveraging Knowledge Graphs and Case-Based Reasoning for Domain-Specific Code Generation

## 一句话总结

DomAgent 是面向领域代码生成的检索型 coding agent：DomRetriever 先从知识图谱取得包/函数知识，再用包重叠重排语义相近代码案例，并让 LLM 迭代调用检索工具后据此生成代码。

## 方法与证据

- 输入为任务、表示包和函数关系的知识图谱及案例库；案例库按 package 覆盖和函数 embedding 聚类挑选可执行、非冗余案例，以在紧凑大小下保留多样性（§2–3）。
- 检索先以 query--KG embedding 相似度做 top-down 包/节点检索，再找语义相近案例并按与已检索包的重叠重排；推理 LLM 可通过 `SearchKG`、`SearchCase` 反复修订检索结果，最后把 query、知识和案例拼接生成代码（§3）。
- 在 DS-1000 上，报告 DomAgent + LLaMA 3.1 8B 的 pass@1 为 40.5，基线同模型为 30.4；加入 GPT-4o 的版本为 58.6。Volvo 六个 CAN 信号领域中，GPT-4o + DomRetriever 的汇总结果为 98.04，对照 GPT-4o 为 71.22（表 1–2）。

## 适用边界与复现

- DS-1000 使用 DS-KG 的 505K triples、300 题建案例库、700 题测试；Volvo 验证涉及 776 个 CAN signals。摘要未给出各领域任务标注、执行判定、检索成本或显著性分析，不能将汇总分数等同于通用软件工程可靠性。
- 复现需公布 KG 构建/版本、案例过滤和覆盖阈值、embedding/reranker、工具调用提示与步数、GRPO reward、基础模型版本、DS-1000 split 和每个工业领域的独立测试与安全隔离；生成代码还应运行测试、静态分析和人工审查。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HSTL5347.pdf) 人工核对 DomRetriever 流程、训练描述、DS-1000 划分和表 1–2；代码仓库链接由论文提供，但本笔记未把它视为对全部实验可复现性的独立验证。
