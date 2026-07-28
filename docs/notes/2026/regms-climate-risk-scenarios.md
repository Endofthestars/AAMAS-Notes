---
title: "ReGMS: Retrieval-Grounded Multi-Agent Scenario Analysis for Climate Risk"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "norms_trust_governance", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RAVT8220.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_manual_source_check"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["climate_data_scope", "qualitative_compliance"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (Spark revision; manual primary-source check)"
reviewed_at: "2026-07-29"
---

# ReGMS: Retrieval-Grounded Multi-Agent Scenario Analysis for Climate Risk

## 一句话总结

ReGMS 通过检索增强的多智能体分工生成气候风险情景，并将 NGFS 路径、物理风险信息和 IFRS S2/TCFD 披露检查纳入生成—审计循环。

## 方法与证据

- §3.1 使用 NGFS Phase V 的 Current Policies 与 Net Zero 2050 路径，并结合 NASA NEX–GDDP–CMIP6 派生的危险指标构造 APAC 情景；论文明确使用 2046–2050 的未来模型值，但没有完整披露 2020–2045 的所有数据处理细节。
- §3.2–3.3 设置设计、过渡、物理、量化耦合、合规和审计智能体，访问共享知识库；合规/审计反馈可触发重写。
- 过渡轨迹将 NGFS 碳价作为外生约束，量化与审计组件检查单调性、边界和一致性；§4 比较集中式 planner、非耦合智能体、单一 LLM 与消融。
- Table 1 使用碳价 RMSE、hazard–adaptation 的 Spearman 相关/差距和趋势指标评估；结论仅适用于论文定义的情景、地区与标准文本。

## 局限与复现

- 评估集中在 APAC 和两条 NGFS 情景，不能推断跨区域气候预测或监管合规的普遍有效性。
- 合规检查为论文定义的规则化流程，未提供统一数值化合规分或完整检索库/脚本/参数版本。
- 复现需重建 NGFS、NEX–GDDP–CMIP6、IFRS S2/TCFD 知识库，以及多智能体编排、约束规则和 §3–4、Figure 1、Table 1 的评估过程。

## 与 AAMAS 的关系与核验说明

该工作将检索、多智能体协作和约束推理应用于气候情景分析。Spark 修订要求避免把未来数据可用性缺口写成绝对事实，也不将审稿风险标签误作为论文结论；本笔记已按该范围表述。
