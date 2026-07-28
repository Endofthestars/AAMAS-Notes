---
title: "Parallelized Planning-Acting for Multi-Agent LLM Systems in Minecraft"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EXAJ9853.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_manual_source_check"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["simulation_scope", "system_integration_dependency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (Spark revision; manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Parallelized Planning-Acting for Multi-Agent LLM Systems in Minecraft

## 一句话总结

论文将 LLM 规划与技能执行置于并行线程，通过集中记忆、单槽动作缓冲和可中断执行，减少 Minecraft 多智能体中的串行响应滞后。

## 方法与证据

- §2.1 和 Figure 1/Algorithm 1 定义规划线程与行动线程：规划产生新动作和中断标志，最新动作覆盖共享单槽缓冲；行动线程按标志中断或继续当前技能。
- §2.2 的集中记忆同步环境观测、团队通信和动作历史；§2.3 用递归 DAG 技能库表示前置约束并展开原子动作。
- §2.1 以延迟表达式比较串行与并行流程，说明在规划和执行重叠的条件下可降低关键路径时延。
- §3 在资源采集、Boss 战和 PVP 等 Minecraft 任务中，使用 Qwen-Plus 与 Qwen-VL-Plus，比较 PPA/RTDM 组件、单/多智能体配置和规模设置。Table 1 的若干任务结果为 10 次 trial 的均值与标准差。

## 局限与复现

- 证据来自 Minecraft 环境及指定模型/基线，不能推出真实具身系统或其他模型族的稳定性、鲁棒性或部署表现。
- 中断频率、通信质量、技能封装和缓冲覆盖策略均是工程依赖；正文未见完整运行脚本、随机种子或精确环境清单。
- 复现应覆盖 §2–3、Algorithm 1、Figures 1/4/5、Tables 1/3，并保留任务、模型、RTDM/PPA 开关和资源配置。

## 与 AAMAS 的关系与核验说明

工作面向多智能体系统的在线协调与 LLM 规划执行。Spark 修订指出原草稿不应使用“不确定性规划/图策略学习”标签；本笔记采用与并行规划、协同、任务规划和具身环境相符的仓库 taxonomy，并限制结论在实验范围内。
