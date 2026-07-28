---
title: "A Multi-Robot Architecture for Continuous Planning and Execution using BDI Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MCRY4236.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-pilot-01"
spark_draft_verdict: "pass_after_revision"
spark_qa_verdict: "pass_after_revision"
spark_consistency: "revised"
risk_level: "medium"
risk_tags: ["robotics", "empirical"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# A Multi-Robot Architecture for Continuous Planning and Execution using BDI Agents

## 一句话总结

EB2A 在 ROS2 中组合中央协调器、本地 BDI 机器人节点与规划器：已知故障本地修复，未知故障全局重规划；主实验是医疗场景，UAV 只出现在相关工作中。

## 方法与证据

- 设计层定义规划域和 Jason 描述；运行时由 Coordinator 与 Robot Nodes 构成（§3，Figures 1–3）。
- Coordinator 维护全局状态、联盟形成、监控和恢复；BDI 节点执行本地计划。ROS2 与 Jason 通过 rosbridge 集成。
- §4 医疗仿真比较 Baseline、Plan Recovery、BDI Baseline、BDI Plan Recovery；故障率为 0/25/50/75/100%，每配置重复 30 次。
- Figures 7–10 表明 BDI Plan Recovery 相较另外三种配置更稳健，但并非完全可靠；原文边界为“completes most missions (<80%)”。

## 局限与复现

- 仅 ROS/Gazebo 医疗仿真，真实机器人、更多任务拓扑与随机性/时延细节仍需验证。
- 应按 ROS2、rosbridge、四配置及故障率复现，重点核对 Figures 9–10 的趋势。
- 该工作连接 AAMAS 的具身机器人、BDI 智能体工程及持续规划执行。
