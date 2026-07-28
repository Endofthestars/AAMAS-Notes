---
title: "Large Language Models for Designing Participatory Budgeting Rules"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "resource_allocation", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LGEP3560.pdf"
code_url: "https://github.com/AnonyMouse3005/LLM-PB"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["llm_generated_code", "dataset_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Large Language Models for Designing Participatory Budgeting Rules

## 一句话总结

LLMRule 用 LLM 生成可执行参与式预算规则，并在进化搜索中以效用和公平目标筛选、变异和评估这些规则。

## 方法与证据

- §3 将规则描述与代码实现组成种群，LLM 生成初始规则和后代；Figure 1 给出规则及其 Python 实现形式，适应度用于种群管理。
- Theorem 1 缩小 Strong-EJR 验证时需要检查的 cohesive group 范围；其结论及后续验证复杂度依赖论文定义的投票/满意度条件。
- §4 在 600 多个来自美国、加拿大、波兰和荷兰的 Pabulib 实例评估，使用小实例训练、大实例作 OOD 测试；默认 LLM 为 GPT-4o mini。
- Tables 2–3、Figures 2–3 比较效用和 Strong-EJR 近似；论文在给定评估协议下报告 LLMRule 生成规则位于或接近若干 Pareto 前沿。作者提供 [Python 实现](https://github.com/AnonyMouse3005/LLM-PB)。

## 局限与复现

- 结果取决于 Pabulib 过滤条件、approval/cardinal ballot、满意度函数、LLM 和进化搜索配置，不能视为对任意公共预算规则的普遍改进。
- LLM 生成规则的可解释性、鲁棒性和公平性质仍需逐一验证；不存在从实验结果推出的所有实例保证。
- 复现需结合 §§3–4、Appendices C–H、Pabulib/pabutools 版本、代码仓库以及训练/OOD 划分。

## 与 AAMAS 的关系与核验说明

论文把 LLM 算法设计用于计算社会选择。笔记保留其真实数据评估、规则验证和代码可用性，同时限定效用—公平权衡在原始实验协议内。
