---
title: "MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QPUC1624.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_manual_source_check"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["simulation_scope", "cache_parameter_sensitivity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (Spark revision; manual primary-source check)"
reviewed_at: "2026-07-29"
---

# MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization

## 一句话总结

MeCo 为相似的多机器人任务缓存并复用历史计划，以减少重复 LLM 规划；论文在 MeCoBench 中报告相对 SOTA 的成功率、规划时间和 token 消耗改善。

## 方法与证据

- §3.2 任务写作 `T=(C,E)`，环境元组按原文为 `E=(R,O,D,K)`；同节另以 `S` 描述任务约束，本文保留这一原文记号而不强行合并。
- Figure 1 与 §4 给出缓存检索、相似性判定、S-Planner 复用、失败反馈续写和成功计划回写的闭环。
- §4.2 区分低/高工作区重叠：前者使用子任务可复用比，后者以区域映射与阈值决定复用；§4.5 采用有上界 `k` 的 LFU 风格缓存更新。
- 在 RoCoBench 六任务及 MeCoBench 中，Figure 2 的设置平均重复 100 次；Figure 5 比较 RoCo、Central、HMAS-2、ReAct 及对应 MeCo 组合。摘要报告总体成功率约提升 30%、规划时间约节省 55%、token 消耗最多减少 70%；§5.3 另报告 token 跨任务平均减少约 73%，该数只指 token 指标。

## 局限与复现

- 证据来自桌面型多机器人基准和相似任务变体，未包含真实机器人部署。
- 收益依赖任务相似度和缓存上界 `k`；低相似 S3 情境下论文报告约 6% 的规划时间开销增加。
- 当前论文文本未见完整代码下载链接；严格复现需补齐相似性阈值、缓存实现、轨迹验证和 LLM 配置。

## 与 AAMAS 的关系与核验说明

工作连接 LLM 协同规划、机器人任务复用与多智能体系统效率。Spark 初审指出记号和指标口径问题；本笔记逐项按 §3.2、§4、§5.3、Figure 2/5 和摘要人工复查并修正，不扩展为一般部署保证。
