---
title: "The Web Tool Trap: Understanding and Mitigating Over-Reliance in Browsing Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/HZER2072"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HZER2072.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03p"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "benchmark-protocol", "web-source-reliability", "tool-selection", "model-specific-intervention"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# The Web Tool Trap: Understanding and Mitigating Over-Reliance in Browsing Agents

## 一句话总结

BrowseBench 专测浏览代理对 web tool 的过度依赖：不需要时仍搜索、检索到错误内容后轻信、复杂问题缺少分解。作者以 DPO、attention refinement 与 hierarchical query decomposition 分别干预三类问题；这些结果说明“能搜索”不等于“知道何时应搜索或如何核验”。

## 方法与证据

- BrowseBench 有 1,500 个真实信息检索场景，覆盖文化社会、科技、生物医学、环境、金融五域各 300 题；每题标 3--6 keywords，并以专家 decision paths 验证（§2）。
- 指标包括：不必要搜索率 USR、把误导内容纳入答案的 FIIR、相对专家分解路径的 Task Decomposition Deviation (TDD)（§2）。这使评估不只看最终正确性。
- 在 greedy decoding、zero-shot、统一 minimalist prompt 下，Table 1 报告 Claude-3.7-Sonnet 的 USR/FIIR/TDD 为 24.8/28.0/2.4，Llama3.1-70B 为 52.9/67.7/4.7；作者据此归纳 excessive conservatism、over-trust 与 planning deficiency（§3）。
- 对 Qwen-2.5-72B-Instruct：以 10K preference pairs 训练的 DPO 使 USR 低 7.2；query-aware AR 使 FIIR 低 12.4；HQD 使 TDD 低 1.4。三者合用时 FIIR 低 14.1，但 USR/TDD 有轻微折中（Table 2, §4）。

## 适用边界与复现

- “unnecessary”与专家路径本身是标注判断，不能单独充当实时真实性判据；不同地域、时间敏感性、工具质量或风险偏好会改变合理检索策略。FIIR 也取决于所构造误导网页和引用归因规则。
- 复现应发布题目、稳定/时变知识划分、专家路径与标注协议、网页快照/时间戳、工具实现、decoding 参数、DPO 数据、AR/HQD 实现及多次运行方差。部署时应把 tool-use policy 与来源可信度、跨源核验和不确定性表达分开评估。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HZER2072.pdf) 人工核对 benchmark、指标和 Tables 1--2；未把摘要中的单模型干预结果当作所有浏览代理的可靠性保证。
