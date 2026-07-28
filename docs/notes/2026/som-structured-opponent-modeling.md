---
title: "SOM: Structured Opponent Modeling for LLM-based Agents via Structural Causal Model"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "argumentation_reasoning"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EXQH7884.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["causal_claim_scope", "llm_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-29"
---

# SOM: Structured Opponent Modeling for LLM-based Agents via Structural Causal Model

## 一句话总结

SOM 为 LLM 对手建模显式构造和细化结构图，再沿图推理对手动作，并以成功推理轨迹做个体化适配。

## 方法与证据

- §3.2 用 DAG 形式的结构因果模型表示观测、潜在中间变量与动作；§4 将流程分为模型构建/细化和结构化预测/适配两阶段（Figure 2）。
- §4.2 从观测到动作初始化图，通过反思引入中间变量，再做语义合并、计数增强和 Top-K 剪枝。
- §4.3 按拓扑顺序遍历图，对每个节点检索与其父节点相关的成功推理示例以预测取值。
- §5 的 Tables 1–4、Figures 3–4 在 G0.8A、SAG、Undercover 等游戏场景报告对手预测、胜率、消融与跨模型迁移比较。

## 局限与复现

- 作者明确说明结构由交互观测归纳而来，未完成严格因果识别；这里的 SCM 不应表述为已验证的真实因果机制。
- 评测依赖特定游戏分布、对手集合和基模型（主实验为 GPT-4o）；跨模型迁移证据不等价于一般环境迁移。
- 热身轮数、评估阶段的更新限制及若干设置细节位于补充材料，完整复现需覆盖 §3–5、Figures 1–4 与 Tables 1–4。

## 与 AAMAS 的关系与核验说明

论文面向竞争式多智能体推理中的可解释对手建模。Spark 双审核对了 SCM 定义、两阶段程序、基准和迁移实验，并保留了论文自身对因果主张范围的限定。
