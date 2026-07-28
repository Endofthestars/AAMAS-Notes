---
title: "A Three-Layer Reinforcement Learning-based Approach for Dynamic Task Allocation Under Multiple Task Resource Constraints"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CPZL2237.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-pilot-01"
spark_draft_verdict: "pass_after_revision"
spark_qa_verdict: "pass_after_revision"
spark_consistency: "revised"
risk_level: "medium"
risk_tags: ["rl", "empirical"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# A Three-Layer Reinforcement Learning-based Approach for Dynamic Task Allocation Under Multiple Task Resource Constraints

## 一句话总结

论文以全局分配、个体选择和序列优化三层注意力强化学习处理动态 ST-SR-TA 与多资源约束；其优势是特定模拟环境中的经验结果，并非收敛或最优性保证。

## 方法与证据

- §3 的约束是单机器人/单任务分配、资源可行性与执行后扣减；目标 Eq. (4) 为任务收益减激活和移动代价。
- §4 使用候选池、注意力序列优化和 SAC/SATM 聚合；没有形式化收敛、最优性或复杂度定理。
- Figures 6–9：全局分配和序列优化的消融；Figure 10：零/少/重训练迁移。
- Table 2/Figure 11：Env A 只与 GA、PSO、SAC、Auction 对比；Env B 只与 Auction、Two-Stage 对比。作者报告本方法在两种设置中优于 Auction，且在 Env A 末期优于 GA、接近 PSO；不可把它扩展为所有算法在所有场景的统一优势。
- Table 2 的 `N/A` 表示未报告或不可横向比较，不能合并成统一排名。

## 局限与复现

- 无代码/数据链接；随机种子、重复试验和显著性分析不足，且主要是模拟验证。
- Table 1 给出部分硬件、训练轮次与参数，基线也给出部分配置；完整再现仍需实现级材料。
- 归于 AAMAS 的多智能体协调、规划调度与应用方向。
