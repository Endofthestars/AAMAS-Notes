---
title: "Stability in Online Assignment Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YSRD5548.pdf"
preprint_url: "https://arxiv.org/abs/2510.09814"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["online_arrival_model_scope", "pricing_timing_assumption", "stability_metric_non_linearity", "open_bound_cells"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Stability in Online Assignment Games

## 一句话总结

论文研究带转移支付的在线买方–卖方分配：用 optimality ratio $\lambda$、基于 subset-instability 的 stability index $J$ 和 $\kappa$-approximate core 衡量次优匹配的稳定性，并说明随机在线算法在 ex-post、ex-ante 与平均效用三种口径下的保证并不相同。

## 方法与证据

- assignment game 中 allocation 是 matching 加价格；稳定 allocation 必须对应社会福利最优 matching。作者定义 $\lambda(\mu)=SW(\mu)/OPT$，以及 $J(\mu,p)=1-I(\mu,p)/OPT$，其中 $I$ 是任意子市场可通过重配获得的最大 welfare 损失；$\kappa$-approximate core 则要求任意买卖对的当前双方效用和至少为其配对价值的 $\kappa$ 倍（§2–3）。
- 对任意 allocation，Theorem 3.6 给出 $J(\mu,p)\le\lambda(\mu)$；若给定 matching 后可再选择价格，存在非负价格使 allocation individually rational 且 $J=\lambda$。这是 a-posteriori pricing 的存在性结论，不说明在线决定价格时能看到未来或可实现该价格（§3.1）。
- Proposition 3.7 的同步可用构造 Half 对每个已匹配对平分其生成的 utility，保证 $J(\mu,p_{half})\ge\lambda(\mu)/2$。此外，Proposition 3.9 给出 $\kappa\le J$；文中还给出 $J$ 高但 $\kappa$ 低的构造，故 $J$ 不能替代 approximate-core 的局部稳定含义（§3.1–3.2）。
- 随机算法定义三种量：ex-post 是 outcome support 的最小值，ex-ante 是每个随机 outcome metric 的期望，average 是先取 agent expected utilities 再计算 metric。由于 $J,\kappa$ 非线性，只有 $\lambda_{ante}=\lambda_{avg}$ 一般成立；Proposition 4.2 给出对任一 metric $m_{post}\le m_{ante}\le m_{avg}$ 及 $\kappa\le J\le\lambda$（§4.1）。
- 对任意 randomized matching 加 Half pricing，Proposition 4.3 给出三种口径下 $J^\gamma\ge\lambda^\gamma/2$。但 edge-arrival 中，在论文规定“首条边必然匹配”的广算法类，Proposition 4.4 构造两实例表明至少一例 $J^\gamma\le\lambda^\gamma/2$，刻画动态 threat levels 的困难（§4.2）。
- vertex-weighted arrival 中，表 1 汇总的紧界为：$\kappa$ 的 ex-post/ex-ante 为 $1/2$、average 为 $1-1/e$；$J$ 的 ex-post 为 $1/2$、average 为 $1-1/e$，但 ex-ante 标为未知；$\lambda$ 的 ex-post 为 $1/2$、ex-ante/average 为 $1-1/e$。其中 Ranking 的 average $\kappa=1-1/e$ 是既有结果的重述，Greedy+Half 的 $\kappa$ ex-post/ex-ante $1/2$ 是论文给出的扩展（§4.3、Table 1）。
- edge-weighted with free disposal 中，表 2 给出 $\kappa$ ex-post/ex-ante 为 0、average 未知；$J$ 仅给出下界 ex-post $\ge1/4$、ex-ante/average $\ge0.268$；$\lambda$ 为 ex-post $1/2$、ex-ante/average $\ge0.536$。这些不等号是尚未证明 tight 的下界，而非精确最优比率（§4.3、Table 2）。

## 局限与复现

- 模型为双边 assignment、可转移 utility 与指定的 edge/vertex arrival；不直接涵盖多对多匹配、不可转移偏好、预算/公平约束、战略报告、随机到达分布学习或真实市场的价格监管。
- Theorem 3.6 的等式需在 matching 后选择价格；真实在线市场若必须在匹配时锁定价格，只能使用更弱的 Half 类保证。把后验价格存在性误读为在线可实施机制会扩大结论。
- 三种随机稳定口径不可互换。报告 average 效用下的高稳定度，不保证每个随机实现（ex-post）或“先算每次 stability 再平均”（ex-ante）同样高。
- 表格里 $J$ 的 vertex-weighted ex-ante 和 $\kappa$ 的 free-disposal average 仍未知；论文称一些数值的 tightness 尚未确定。复现/二次引用需保留其是未知、猜想或下界的状态。
- 复现应实现子市场 instability 的优化、approximate-core 检查、Half 定价与随机算法分布；对每个 instance 分别计算三种指标，并验证 vertex-weighted 与 edge-weighted/free-disposal 的假设及表格构造实例。

## 与 AAMAS 的关系与核验说明

该文连接在线资源分配、机制/博弈论和随机 agent 决策，为“次优匹配有多不稳定”提供可比较指标。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2510.09814) 核对定义、定理前提、三种随机口径与两张结果表；精确值、下界和开放项均按原文区分。
