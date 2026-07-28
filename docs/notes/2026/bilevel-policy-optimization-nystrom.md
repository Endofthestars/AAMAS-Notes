---
title: "Bilevel Policy Optimization with Nyström Hypergradients"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "game_theory_mechanism"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NETG3616.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["bilevel_assumptions", "hypergradient_approximation", "convergence_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Bilevel Policy Optimization with Nyström Hypergradients

## 一句话总结

论文把 actor-critic 视为 outer actor、inner critic 的双层优化，并以 Nyström 低秩近似计算 hypergradient 中的 inverse-Hessian-vector product。

## 方法与证据

- BLPO 对 critic 做嵌套近似 best response，再以包含 direct 与 implicit 项的 hypergradient 更新 actor；Nyström 方法避免显式构造完整 Hessian（§1、§4）。
- 线性 value-function critic 令平方损失 inner objective 强凸、解唯一；outer actor 仍一般非凸，因此目标是 local strong Stackelberg equilibrium 的必要一阶条件，不是全局最优策略（§1、§5）。
- Theorem 4.6 的多项式时间、高概率收敛依赖 strong convexity、Lipschitz gradient/smoothness、梯度有界、学习率/内外迭代数和按特征值采样等条件；高概率也来自随机 Nyström 近似（§4）。
- Theorem 5.2 将线性 critic 参数化与折扣 MDP 条件连接到 nonconvex–strongly-convex BLO，从而使上述收敛结果适用于该 AC formulation（§5）。
- 实验在离散/连续控制任务上比较 PPO；性能结果是这些环境与实现下的经验观察，不等价于所有神经 critic 或现实控制问题中的稳定性保证（§6）。

## 局限与复现

- 不可把线性 critic 的理论结论外推到任意深度神经 critic；强凸与正则性条件是保证的一部分。
- 近似 IHVP、inner solve 误差、Nyström 采样 rank/regularization 和 actor/critic 两时间尺度均应被报告。
- 复现应分别测 stationarity、critic best-response 误差、Hessian condition、随机种子和任务回报；仅比较最终 reward 不能验证 theorem scope。

## 与 AAMAS 的关系与核验说明

该文连接 actor-critic、Stackelberg 建模和数值线性代数。笔记基于官方公开 [AAMAS PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NETG3616.pdf) 核对了 BLPO 的 nested/hypergradient 结构和收敛条件。
