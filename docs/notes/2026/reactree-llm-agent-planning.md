---
title: "ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UCGT7089.pdf"
code_url: "https://github.com/Choi-JaeWoo/ReAcTree.git"
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-pilot-01"
spark_draft_verdict: "pass_after_revision"
spark_qa_verdict: "pass_after_revision"
spark_consistency: "revised"
risk_level: "medium"
risk_tags: ["empirical", "llm_agents"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

## 一句话总结

ReAcTree 用“代理节点 + 行为树式控制流”的动态子目标树替代单轨 ReAct 执行，在部分可观测具身环境中结合两类记忆完成长时域任务规划。

## 方法与证据

- 代理节点执行 `reason / act / expand`；控制流节点提供顺序、回退和并行协调（§3–4）。
- episodic memory 提供子目标轨迹示例，working memory 在节点间共享环境状态。
- §5.1/Table 1：WAH-NL 主实验，与 ReAct、Tree-Planner 等比较 GSR/SSR。
- §5.2/Table 2 与 Figure 3：ALFRED valid-seen/unseen 比较与树结构示例。
- §5.3/Table 3、§5.4/Table 4：记忆和控制流消融；§5.5–5.6 讨论开销和失败归因。

## 局限、复现与定位

- 论文是架构与实证论证，未给出形式化定理、收敛证明或统计显著性框架。
- 无回滚机制时不可逆错误难恢复；歧义指令、搜索与执行失配仍是主要失败来源。
- 代码仓库见上；复现需同时取得附录中的 prompt、bootstrap 轨迹、参数与日志。该工作归于 AAMAS 的生成式智能体和规划调度议题。
