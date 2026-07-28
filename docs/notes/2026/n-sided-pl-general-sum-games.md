---
title: "Global Convergence to Nash Equilibrium in Nonconvex General-Sum Games under the n-Sided PL Condition"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "marl_coordination"]
dblp_key: ""
doi: "10.65109/OXGY8396"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OXGY8396.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["conditional_theorem_scope", "n_sided_pl_verification_difficulty", "multiple_ne_possible", "synthetic_convergence_experiments"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Global Convergence to Nash Equilibrium in Nonconvex General-Sum Games under the n-Sided PL Condition

## 一句话总结

论文提出 n-sided PL（每 player block 的 PL 型条件）来分析 nonconvex general-sum game 的 GD/BCD 变体；在该条件及 smoothness 等前提下能收敛至 NE，额外局部关系或 `(θ,ν)`-PL 条件下可接近/达到线性速率。该条件允许多个 NE，且仅有 n-sided PL 不会给出统一 BCD 速率。

## 方法与证据

- n-sided PL 扩展 classical PL/multi-convexity，对每个 `f_i(x_i;x_-i)` 施加 blockwise gradient-dominance；Lemma 2.5 将其 stationary set 与 NE set 对齐，但不蕴含 convexity 或全局 PL（§2）。
- 对 BCD/random BCD，论文给出收敛分析与反例/实验，显示同满足 n-sided PL 的函数可有不同速率；因此不能由该条件单独断言 linear rate（§3.1）。
- Theorem 3.3 等在 Assumption 2.1、n-sided μ-PL 及额外局部 bound 或 `(θ,ν)`-PL 下给 R-BCD 的线性/近线性结论；其余 adapted variants（如 A-RBCD）在进一步假设下处理 BCD 失败或慢收敛情形（§3）。
- 数值例子含 potential/general-sum 与 n-player LQ games，用于展示收敛轨迹，不能证明深度 RL、任意策略梯度或未验证 PL 的游戏也满足结论（§3--4）。

## 局限与复现

- 找 NE 在一般 general-sum games 是 PPAD-complete；n-sided PL 是实质结构限制，实际模型是否满足、常数如何估计通常未解决。
- 结论依赖精确目标、梯度、smoothness、步长与特定 algorithm；非平稳采样、随机估计、约束、function approximation 或非光滑性可破坏前提。
- 多 NE 仍可能存在，收敛点/速率受 initialization 和局部条件影响；不能把“global convergence under condition”简化为任意训练都有唯一或最优 NE。
- 复现应实现所有示例函数/参数、检查条件、报告步长和初值扫描、NE residual 与完整曲线；应在可验证结构的外部 game class 再测试。

## 与 AAMAS 的关系与核验说明

这是多智能体非凸优化和均衡计算的条件化理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OXGY8396.pdf) 核对 Definition 2.4、Lemma 2.5、Theorems 3.3/3.5/3.9 与速率边界；未将其描述为通用深度多智能体训练保证。
