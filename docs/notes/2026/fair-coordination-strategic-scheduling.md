---
title: "Fair Coordination in Strategic Scheduling"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "planning_scheduling", "resource_allocation"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BOCM2167.pdf"
preprint_url: "https://arxiv.org/abs/2512.13244"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["fairness_definition_scope", "nash_equilibrium_condition", "complexity_bound_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Fair Coordination in Strategic Scheduling

## 一句话总结

论文在相同机器调度中同时施加稳定性与公平性：每个 job-agent 选择机器，研究 credibility（纯 Nash equilibrium）、相同权重的 equality、及一组按权重放宽的 envy/monotonicity 条件下，是否存在可行调度及其带 makespan 门槛的复杂度。

## 方法与证据

- 模型为正整数权重任务分配到 $m$ 台相同机器；agent 的成本是所在机器总负载。主要问题是在属性 $P$ 下寻找 makespan 不超过阈值的 assignment；$P$-Satisfiability 则等价于阈值为无穷大（§2）。
- Credibility 要求 agent 不能单边换机获益，即其当前负载不高于任意目标机器现有负载加自身权重；在该模型中等价于纯策略 Nash equilibrium。Equality 要求相同权重 agent 承受相同机器负载（Definition 1）。
- 论文定义 EF、weak ordered envy-freeness (WOE)、ordered envy-freeness (OE)、strong/weak monotonicity (SM/WM) 等。WOE 只约束分属不同机器的一对轻/重 agent；它不等价于 SM。EF 蕴含 Eq、WOE 与 SM；WOE+Eq 等价于 OE，WM+Eq 等价于 M（§2.3）。
- 对 WOE 系列，Theorem 10 给出：WOE、WOE+Cr、WOE+Eq+Cr 的 $P$-Makespan 可在 $O(n\log n)$ 求解，而 WOE+Eq 为 $O(n^2)$；相应 satisfiability 结果见 Corollary 15（§3.3）。
- 对 SM 及其与 Eq/Cr 的所有四种组合，Theorem 18 同时给出 $P$-Makespan 与 $P$-Satisfiability 的 $O(n\log n)$ 算法（§3.4）。
- 但公平与稳定的组合不总带来易解性：Theorem 20 将 Eq+Cr、WM+Cr、WM+Eq+Cr 的纯存在判定列为 NP-complete；Theorem 21 对一组属性（含无约束、Eq、Cr、WM 及相关组合）的阈值 makespan 判定也给出 NP-complete（§4）。

## 局限与复现

- 结论是相同机器、线性 congestion cost、不可分任务、每任务一个策略 agent 的结果；不直接覆盖异构机器、前置约束、随机 processing time 或 payment mechanism。
- 不能从“某属性 satisfiability 易解”推出其带 makespan 阈值的版本易解。例如基础 identical-machine makespan 与若干 WM 组合的阈值判定仍为 NP-complete。
- WOE、OE、SM、WM 的量词与“是否同机”条件不同；实现时将它们折叠为一般 envy-free 会改变可行集和复杂度结论。
- 复现应将候选 assignment 的负载、单边偏离、同权重等负载及按权重的 pairwise 条件分别检查，并针对每个 $P$ 独立运行构造/判定程序；不应只比较最终 makespan。

## 与 AAMAS 的关系与核验说明

该工作连接了多 agent 协调、拥塞博弈和公平资源调度。笔记基于作者公开的 [arXiv PDF](https://arxiv.org/pdf/2512.13244) 核对了属性定义、等价关系及算法/NP-complete 的精确属性集合。
