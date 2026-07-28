---
title: "Robust Sequential Learning in Random Order Networks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "norms_trust_governance", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/KNSC4490"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KNSC4490.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["asymptotic_bayesian_model_scope", "learning_rate_oracle_assumption", "no_empirical_network_validation", "random_order_not_adversarial_order"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Robust Sequential Learning in Random Order Networks

## 一句话总结

论文研究二元真值、独立有界 private signal、Bayesian agent 且 uniformly random decision order 下的渐近社会学习：给出对有限 adversarial graph modification 的鲁棒性和若干构造，并在能估计顶点 learning rate 的前提下用 randomized greedy/Monte-Carlo 算法以近似最少修改把任意网络增强为 random-order learner；这不是现实社交平台的因果设计结论。

## 方法与证据

- 目标是 random-order asymptotic truth learning：`n→∞` 时除 `o(n)` 外 agent 以趋近 1 的概率学到二元 ground truth；每人结合独立 bounded signal 和较早邻居的预测做 Bayesian decision（§1--2）。
- 论文证明 learning rate `1-ε` 的网络对 `o(1/ε)` 次 adversarial modification 鲁棒，并以 celebrity network 的 `Θ(1/ε)` 删除说明最坏情形近紧；还给出必要的 superconstant independent set 条件（§3）。
- 通过加入 superconstant degree-one “guinea pigs”等方式使 complete graph 获得 random-order learning，并扩展为嵌入可 strategic-order 学习的子图的构造（§3）。
- BoostGraph-MonteCarlo 以影响/learning-rate 估计选择要增强的顶点；定理给出 randomized polynomial-time 与 `O(g(n) log n)` 近似（具体依赖其 `g(n)`、`k=ω(1)`、`T=o(n)` 等条件，§4）。

## 局限与复现

- 结论是渐近、随机 order 和理性 Bayesian 模型下的图性质；不覆盖策略操纵、相关/非平稳信息、错误信念、平台推荐、隐私或真实信息扩散的观察偏差。
- 算法假定能有效访问/估计任意顶点的 random-order learning rate；论文指出一般 Bayesian inference/相关学习判定困难，此 oracle 是实际可用性的关键缺口。
- 没有真实网络或数值实验，不能由定理外推出对市场、公共卫生或社交产品的干预效果。复现应实现 oracle/Monte Carlo 误差界，给出各图族的有限 `n`、修改预算、运行时间及随机 seed。
- 作者将 learning-rate 计算/近似的复杂度和不依赖该 oracle 的替代算法列为后续方向（§5）。

## 与 AAMAS 的关系与核验说明

这是 social learning、网络设计与近似算法的理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KNSC4490.pdf) 核对模型、鲁棒性结论、构造、Algorithm 1/Theorem 4.9 与 oracle 前提；没有将其作为现实网络操控或群体预测的建议。
