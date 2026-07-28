---
title: "Smooth Routing in Decaying Trees"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BBUZ3605.pdf"
code_url: "https://github.com/buhtig-tf/Smooth-Routing-in-Decaying-Trees"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["complexity_conditions", "ilp_experimental_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Smooth Routing in Decaying Trees

## 一句话总结

论文研究连接会在截止时间失效的图中，如何为固定疏散路径安排平滑时序：不在边上相遇，且每个顶点同时容纳的路径数不超过容量。

## 方法与证据

- 模型以衰减图、给定路径、顶点容量、旅行时间和边截止时间描述调度；特别研究路径、星和树（摘要、§1）。
- Theorem 1 表明 SRDG 在外生衰减路径、所有顶点容量为 1 时已 NP-hard；Theorems 4–6 分别给出星图及无容量树的其他 NP-hard 受限情形。
- 对固定截止时间的路径，Theorem 2 给出动态规划算法；对星图，Theorem 3 给出以最大顶点负载和生命周期为参数的算法。它们不是一般树的多项式算法。
- 论文给出 ILP 以计算令实例可行所需的最小截止时间增量。§5 在人工路径/星图与来自德国河流城市道路网的半人工洪水实例上评估；文中报告 osm 实例上 ILP relaxation 的平均解质量和两种实现的运行时间比较。

## 局限与复现

- 硬度和算法结论依赖网络形状、容量、截止时间/生命周期和最大负载等明确条件；不能笼统归为“树上都难”或“树上都可解”。
- ILP 的实验表现受城市、路径量、容量和期限配置影响，部分实例运行时间可很长；实验不是近似保证。
- 正文给出[代码与数据仓库](https://github.com/buhtig-tf/Smooth-Routing-in-Decaying-Trees)。复现需保留 §1–5、Theorems 1–6、Table 1、Figures 5–7、Tables 3–4 的实例生成与求解器设置。

## 与 AAMAS 的关系与核验说明

工作连接多智能体路径协调、时变网络和疏散规划。笔记将 NP-hardness、固定参数算法及 ILP 实验分开记录，严格保留各自适用条件。
