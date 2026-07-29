---
title: "G2CP: A Graph-Grounded Communication Protocol for Verifiable and Efficient Multi-Agent Reasoning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "safety_verification"]
dblp_key: ""
doi: "10.65109/JHFW8307"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JHFW8307.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02v"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "knowledge_graph_completeness", "entity_linking_error", "synthetic_query_evaluation", "auditability_definition_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# G2CP: A Graph-Grounded Communication Protocol for Verifiable and Efficient Multi-Agent Reasoning

## 一句话总结

G2CP 用共享知识图上的 typed graph operation 替代 agent 间自由文本：消息包含 sender、receiver、performative、操作和会话上下文，Traverse/Update 产生可回放证据；LLM 仅在用户边界做实体链接、意图分类和结果表述。一个 367-node Neo4j 图、500 合成问题与 21 个专家案例上，摘要报告 F1 0.90、每题 768 tokens、hallucination 0.02；这验证的是固定图谱与评测定义下的可追溯协调，并不保证图谱缺失/错误、边界实体链接或开放世界问题的事实正确性。

## 方法与证据

- 消息为 \(\langle s,r,\pi,op,c\rangle\)：performative（Request/Inform/Query/Propose/Confirm/Reject/Update 等）带 typed graph operation 而非自然语言 content；Traverse 按节点、边类型和 hop 扩展子图，Update 在 schema/RBAC 约束下施加图 delta，均返回带 provenance 的结果（§2）。
- commitment semantics 将请求/确认等映射为可履行或违反的社会承诺，并以追加式 audit trail 回放。LLM 限于 entity extraction、intent 分类、深度估计和基于图结果生成回答，agent 协调本身为确定的图操作（§2）。
- 系统包含 Dispatcher、Diagnostic、Procedural、Synthesis、Ingestion 五个角色，在 Neo4j KG 上按 RBAC 运行；HMAC-SHA256 签名消息并记录日志。entity linking 使用 sentence-transformer 及 cosine ≥0.85，故边界层仍可能出错（§3）。
- 对 FTMA、JSON structured MA、single-agent RAG（同为 GPT-4、同图）比较：表 1 在 521 query 上为 G2CP F1 0.90、768 tokens/query、hallucination 0.02、cascading error 0、auditability 1.0；FTMA 为 0.67/2847/0.23/0.31/0.42。数据由 500 个有程序化 ground truth 的合成 query 和 21 个专家验证案例组成（§4、表 1）。

## 适用边界与复现

- 可用于知识图已治理、操作可授权且审计重放重要的流程；“graph grounded”只能保证输出可追到检索到的图节点/边，不能保证图的完整、时效、因果或规范正确性。
- 0.02 residual hallucination 来自边界 entity linking；模糊名称、未覆盖实体、恶意输入、过时图、权限误配和错误 schema 仍会产生错误或不当动作。签名/日志也不替代访问控制、隐私和独立审计。
- 合成 query 与单一 367-node/538-edge 图的 F1/token 优势未证明跨领域、动态图、大图、多个 LLM 或真实工作流的泛化；“perfect auditability”是本文定义的可回放性指标。
- 复现应发布图 schema/版本、查询生成器、ground truth、实体链接阈值/模型、RBAC、操作实现与所有 baseline prompts；报告跨图迁移、知识缺失/污染、链接错误、延迟/并发、授权拒绝及人工审计结果。

## 与 AAMAS 的关系与核验说明

该文为 LLM 多智能体的可验证协作提出通信协议层。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JHFW8307.pdf) 人工核对消息/操作、边界隔离、五角色架构、521-query 设置及表 1；未把知识图可回放性扩展成开放世界真实性保证。
