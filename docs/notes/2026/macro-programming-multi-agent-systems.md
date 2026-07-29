---
title: "Macro-Programming Multi-Agent Systems: A Framework for Artificial Collective Intelligence"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["agent_engineering", "generative_agents", "marl_coordination"]
dblp_key: ""
doi: "10.65109/SAXG2906"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SAXG2906.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04k"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["macro-programming", "collective-intelligence", "micro-macro-link", "multi-level-design", "blue-sky"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Macro-Programming Multi-Agent Systems: A Framework for Artificial Collective Intelligence

## 一句话总结

这篇 Blue Sky 论文主张以系统级目标、结构或行为的宏观描述，加上从 macro 到 micro 的映射、反馈与验证，作为工程 emergent collective behaviour 的 MAS macro-programming 研究议程。

## 方法与证据

- 框架区分 micro（agent capabilities/mechanisms）、meso（组织、邻域、norms）与 macro（global goals/outcomes）层次；宏程序经 compilation/projection、middleware 与 downward causation 间接塑造 agents，而 emergence 由微观行为产生宏观结果（§1、§2、Fig. 1）。
- 文章综合 sensor-network/IoT/swarm macro-programming、组织式与规范式 MAS、holonic/multi-level modelling、collective intelligence 等脉络，提出 macro-to-micro inverse design 与 micro-to-macro prediction/validation 的共同挑战（§1–§3）。
- 它讨论宏观 abstractions 可如何组织 optimization、learning 与 generative AI 的搜索与解释，并列出语言、compiler/projection、运行时反馈、建模、验证、benchmark 与 human–AI collaboration 等开放研究机会（§2–§4）。

## 适用边界与复现

- 这是 6 页 Blue Sky Ideas 的概念综合与研究议程，并未提出或在统一 benchmark 上评估可直接部署的 macro-programming language/compiler；图示是架构性说明而非已证实端到端流程。
- 后续实现应明确宏观 specification language、micro-level action/communication model、macro-to-micro synthesis semantics、environment assumptions、emergence metrics、feedback/adaptation loop 与对照基线；不同 MAS 范式间术语不能直接视为可互换。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SAXG2906.pdf) 人工核对其 Blue Sky 定位、multi-level 框架和研究机会；笔记明确保留其方向性而非实证性能结论的性质。
