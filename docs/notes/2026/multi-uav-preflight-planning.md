---
title: "Multi UAVs Preflight Planning in a Shared and Dynamic Airspace"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KPWJ5508.pdf"
code_url: "https://github.com/amathsow/4DPlanning"
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-pilot-01"
spark_draft_verdict: "pass_after_revision"
spark_qa_verdict: "pass_after_revision"
spark_consistency: "revised"
risk_level: "medium"
risk_tags: ["empirical", "planning"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# Multi UAVs Preflight Planning in a Shared and Dynamic Airspace

## 一句话总结

论文把共享动态空域中的异构无人机配送建模为 4D 往返 MAPF，提出 DTAPP-IICR：按起飞时刻 `t_init` 排序、以最小化总 `flowtime` 为目标，并以冲突图驱动的迭代修复提高规模与动态禁飞约束下的可行性。

## 方法与证据

- §3 用 26 邻接体素、temporal NFZ 与安全距离描述问题；pursuit/head-on/intersection 冲突见 Figure 1。式 (2) 是 temporal NFZ，式 (3) 是安全距离，式 (4) 是 flowtime；论文没有 deadline 约束。
- SFIPP-ST 在安全时间区间上做单机搜索；方向性剪枝在受限时回退全邻居以保留完整性（§4.2–4.3，Algorithms 1–2）。
- DTAPP-IICR 先生成按 `t_init` 排序的初解，再用几何冲突图和 LNS 式重规划消除冲突（§4.4，Algorithm 3）。整体框架没有全局最优性证明。
- §5/Table 2、Figure 3：实验 1 的 300 秒预算用于剪枝评价；实验 2 的 480 秒预算用于规模测试。
- §5/Table 3、Figure 4：动态 NFZ 实验使用 1200 秒主预算；Figure 4 另有 500/900 秒图级设定。4 NFZ、500 UAV 时成功率约 30%，说明方法对密度和时限敏感。

## 局限与复现

- CBS/ECBS 比较与实现版本、完整证明和城市案例统计仍需按原始代码复核。
- 论文给出 [4DPlanning](https://github.com/amathsow/4DPlanning)；可从 §5 的网格、20 实例/配置、速度/半径、`N=10` 和时限设置重建实验。
- 该工作对应 AAMAS 的多智能体规划、调度与城市空域应用。
