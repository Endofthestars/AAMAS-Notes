---
title: "HLSMAC: A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ELYZ1330.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_recheck"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "revised_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["benchmark_scope", "simulation_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark revision and recheck)"
reviewed_at: "2026-07-29"
---

# HLSMAC: A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making

## 一句话总结

HLSMAC 将《三十六计》映射为 12 个 StarCraft II 协作场景，并用胜率和场景行为指标评测 MARL 与 LLM 的高层战略理解和执行。

## 方法与证据

- §3 扩展地图、单位能力、对手脚本和终止条件，以承载高层策略；Table 1 列出 12 个场景，Figure 1 给出“谋略—机制—场景”构造流程。
- §4 提供 SMAC 兼容的 PyMARL 接口和分层的 LLM-PySC2 接口；后者支持三种提示层级。
- §5.1–5.2 从 replay 提取 TPF、TDA、CTD、AUF、USR 五类指标，与训练和测试胜率联合分析。
- §5.3 评测 21 个 MARL 算法（前 9 个另作三种子复检）和 4 个 LLM 在 12 场景、3 提示层级、3 次重复下的表现。论文报告约 80% 的 MARL 场景组合为零胜率；Figure 4 中 40% 的指标—场景组合 `R²≥0.6`。

## 局限与复现

- 证据限于 HLSMAC 仿真内的胜率和行为指标，未评估真实部署、安全性或鲁棒性。
- 文中没有显著性检验、置信区间、理论保证或跨场景泛化证明；LLM 结果还依赖提示层级、模型版本与文本到动作链路。
- 复现应覆盖 Table 1、§3–5、Figures 1–6、Table 2，尤其保留地图触发、终止逻辑和提示设置。

## 与 AAMAS 的关系与核验说明

该基准服务于多智能体协同决策和策略能力评测。初次 Spark QA 指出范围措辞问题；修订后 Spark S4 复核场景、规模、指标、数值与实验边界均可追溯到原文。
