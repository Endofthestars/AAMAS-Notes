---
title: "CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/FMEO2393"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FMEO2393.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03o"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "rag-security", "black-box-threat-model", "knowledge-base-write-access", "defensive-review-only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models

## 一句话总结

CtrlRAG 分析一种 RAG 供应链威胁：若攻击者可向知识库注入文档、但看不到检索器内部参数或分数，仍可能借助公开 reference context 的反馈迭代提高恶意内容被检索的机会。本文的价值在于把透明检索上下文视为泄漏面，并提示部署方需要把写入治理、来源验证和检索异常检测放在同一安全边界内。

## 方法与证据

- 威胁前提是攻击者可把携带虚假信息或操纵性内容的文档注入知识库，同时可观察系统返回的 reference context；与依赖模型参数的 white/gray-box 工作不同，论文研究黑盒反馈（§1）。
- 作者提出两阶段、反馈驱动的文档优化框架：先构造能进入检索上下文的初始载荷，再通过观测上下文中候选文档的相对可见性来迭代调整文本，同时试图保持语言自然性（§1–2）。为避免形成操作性攻击指南，本笔记不记录具体的搜索、替换或提示细节。
- 摘要将该攻击定位为对现有 static、one-shot 方法的补充，并称可在只观察“是否被检索”的极端黑盒条件下工作；完整量化结果与实验设定在链接的扩展版本中，3 页摘要本身未给出可独立核查的成功率表。

## 防护与适用边界

- 该风险依赖知识库写权限或上游内容污染；受控、签名、最小权限的数据导入可直接缩小攻击面。仅依赖 PPL 或模式过滤并不足以替代 provenance、版本审计和人工/规则审核。
- 防护评估应包含：文档来源与写入身份绑定、隔离/回滚、检索结果多样性与突增监控、query--document 相关性和事实一致性复核、对不可信语料降权、输出引用可追溯与用户报告通道。对于安全关键问答，应在生成前验证来源而非仅信任被检索文本。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FMEO2393.pdf) 人工核对威胁模型与论文自述的黑盒定位；此条目仅作防御性风险分析，不提供攻击实施步骤或载荷模板。
