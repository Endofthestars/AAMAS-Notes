---
title: "Argumentative Human-AI Decision-Making: Toward AI Agents That Reason With Us, Not For Us"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["argumentation_reasoning", "human_agent_interaction", "generative_agents", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/EKAW8904"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EKAW8904.pdf"
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-04n"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_source_scoped_revision"
spark_consistency: "pass"
risk_level: "medium"
risk_tags: ["blue_sky_vision", "high_stakes_applications", "llm_argument_mining", "formal_solver_interface", "human_agency", "no_system_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Argumentative Human-AI Decision-Making: Toward AI Agents That Reason With Us, Not For Us

## 一句话总结

本文把计算论证与 LLM 的结合组织为 argumentation mining、synthesis 和 reasoning 三类任务，并提出一种以可争辩论证图为人机接口的研究愿景：LLM 负责从自然语言生成结构化论点，形式化求解器负责可接受性判断，人在图上补充、反驳或调整论点后重新计算结论；论文没有实现或评测完整系统，不能据此声称这种架构已经提升高风险决策质量。

## 方法与证据

- Table 1 将协同任务分成三类：argumentation mining 从文本抽取论点单元、支持/攻击关系和立场；argumentation synthesis 生成论点、前提、反驳和摘要；argumentative reasoning 用形式语义做 claim verification 与 explainable decision-making（§2，pp. 3881–3882）。
- 作者的互补性论点是：LLM 缓解计算论证依赖手工知识与结构化输入的问题，计算论证则把 LLM 产生的内容外化为可检查的 argumentation framework，并由确定性求解器进行形式推断（§1–2）。
- “Contestable Architectures”提出三个组件：生成与评估分离、论点节点到来源文本的端到端 provenance、用户修改论点强度或攻击关系后对可接受性标签进行双向传播和重算（§3，p. 3883）。
- 医疗示例中，初始论点支持用药 X；医生加入“患者有禁忌 Z”的反驳后，求解器可能把结论改为避免 X。这个例子说明预期交互机制，不是临床实验结果（§3，p. 3883）。
- 论文把医学和科学同行评审作为可能应用，并明确把“是否节省时间、是否比人或 AI 单独决策更少出错、用户能否定位并修正错误、是否增加认知负担”列为尚待回答的评估问题（§3，pp. 3883–3884）。

## 适用边界与复现

- 这是 Blue Sky 研究议程，没有实现统一系统，也没有数据集、基线、用户实验、决策准确率、延迟或成本结果；文中引用的已有 mining/synthesis/reasoning 工作只能支持技术组件正在形成，不能替代对所提完整范式的验证。
- 可编辑论证图不自动保证来源真实、LLM 抽取无幻觉、argument strength 合理或形式语义符合临床/法律规范。形式求解器只能对给定表示执行语义，无法自行修复遗漏证据、错误关系或价值冲突。
- 作者明确列出的后续验证问题包括：协同决策是否更少错误并产生更稳健的论证、人是否能定位与修正错误且修正能否正确传播、系统是否改变认知负担，以及如何避免过度依赖或信任侵蚀；现实设计还要明确人机角色与对话协议、终止条件、计算时效/资源、敏感数据隐私和专业规范（§3，pp. 3883–3884）。
- 若要验证本文没有实现的完整架构，还需把论点—来源 span 追溯、跨任务 error propagation、求解器语义配置、对照条件和上述人因指标落实为可复现实验；这些是从作者挑战清单导出的验证需求，不是论文已经交付的组件。
- 作者明确区分该范式与事后 XAI：目标是让推理过程本身成为可修改对象。但“更可修改”是否意味着用户更理解、更信任或更少犯错，仍须人因研究证明。

## 与 AAMAS 的关系与核验说明

论文连接计算论证、生成式智能体和 human-agent interaction，强调由人设定目标、价值与规范约束，代理处理论点和证据的组合复杂度。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EKAW8904.pdf) 核对摘要、Table 1、§2 三任务分类、§3 架构组件、应用示例和挑战；未把愿景、引用工作的结果或形式可争辩性表述为已验证的人机决策改进。
