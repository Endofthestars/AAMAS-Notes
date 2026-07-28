---
title: "Towards Foresighted AI Cooperators with LLM-driven Decision-Time Planning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XALP4331.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["llm_evaluation", "test_time_compute"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# Towards Foresighted AI Cooperators with LLM-driven Decision-Time Planning

## 一句话总结

DTPAgent 以 LLM 的 in-context learning 建模未知伙伴与环境，并在决策时模拟轨迹，为两人协作任务在线挑选动作。

## 方法与证据

- §4 将建模拆为伙伴策略模型（PPM）和转移—奖励模型（TRM）；两者从上下文示例推断。
- 每步更新上下文缓冲，对每个合法动作进行 `M` 次 rollout，再按估计价值选择动作（Algorithm 1、Figure 1、Eqs. 4–5）。
- §5 在 Overcooked 的两人协作场景比较 PBT 类和 LLM 类基线。Figures 2–4、Tables 1–2 覆盖回报趋势、消融、伙伴预测/TRM 误差、模型差异和 rollout 预算。
- 论文报告模拟量增加时的性能趋势，但也明确测试时推理成本随预算上升（§6）。

## 局限与复现

- 主证据仅来自 Overcooked 和双智能体协作，不能推出更大规模多智能体或跨域性能。
- 文中未见显著性检验、完整提示模板、固定种子和可直接执行的实现链。
- 复现需核对 §4–6、Algorithm 1、Figures 1–4、Tables 1–2，并明确记录 LLM、上下文和 rollout 预算。

## 与 AAMAS 的关系与核验说明

工作连接 ad hoc teamplay、零样本协作和决策时规划。Spark S1 与独立 S2 对方法、对比范围、成本及泛化界限的核验一致；未添加原文之外的安全或泛化保证。
