---
title: "Learning Truthful Mechanisms without Discretization"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JTXL5273.pdf"
preprint_url: "https://arxiv.org/abs/2506.22911"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["truthfulness_equivalence_scope", "full_expressiveness_assumptions", "reproducible_goods_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Learning Truthful Mechanisms without Discretization

## 一句话总结

TEDI 用连续的 pricing rule 表示 menu，而非枚举离散 outcomes；以 Partial GroupMax 网络参数化对自身 allocation 凸的价格函数，从而在论文的可复制物品拍卖模型中学习 IC、IR 的机制。

## 方法与证据

- 基础模型有 $n$ 位 additive、quasilinear buyer，类型在 $[0,1]^m$；每个 goods 的 allocation 是独立的 $[0,1]$ 概率，且论文**不施加**传统 unit-supply 约束 $\sum_i x_{ij}\le1$（§2、Remark 2.1）。
- pricing rule 为 $p_i(x_i;t_{-i})$。Theorem 2.9 表明：满足 no-buy-no-pay 与对 $x_i$ partial-convex 的 menu mechanism，与其等价的 direct mechanism 是 truthful/IR；反向地，每个 truthful/IR direct mechanism 都有这样的等价 menu。
- TEDI 的 Partial GroupMax Network 是连续、对被凸输入凸函数的 universal approximator（Theorem B.2）；用连续 argmax 推断 buyer 所选 outcome。covariance trick 与 continuous sampling 用于得到可供一阶训练使用的梯度估计（§3）。
- 因此，任何可由 TEDI 表示的上述 menu 的等价 direct mechanism 是 truthful（Corollary 3.7）。在 auctioneer utility 对收款非递减、类型分布 non-degenerate 的额外条件下，TEDI 表示类的 supremum expected utility 等于所有 truthful direct mechanisms 的 supremum（Theorem B.10）。
- 实验是有一次生产成本与复制成本的 reproducible-goods auction；对单/三 buyer、多个 goods 与独立/相关估值分布，论文比较 MenuNet、GemNet、Lottery-AMA、RegretNet、VCG 等，并报告 TEDI 在所列多数设置中具有竞争力（§4、Table 1）。

## 局限与复现

- “truthful”依赖的是 menu 的 partial-convexity、no-buy-no-pay 和等价 direct-mechanism 推断，不能替代对实际数值 argmax、tie-breaking、网络约束是否正确实施的验证。
- full expressiveness 是 supremum/任意精度近似结论，不等于有限网络、有限采样和非凸优化必能找到最优参数；它还依赖 auctioneer 不厌恶更高 payment 与类型分布 non-degenerate。
- 主要模型可复制供给，未直接满足 unit-supply feasibility；文中仅以 production-cost regularizer 表示其近似，不能将实验结果宣称为一般组合拍卖结论。
- 复现需检查价格网络的 convexity/no-buy-no-pay 硬约束、连续 inner argmax 的收敛、IC/IR 数值违例，以及与离散基线相同的候选空间、成本、随机种子和训练预算。

## 与 AAMAS 的关系与核验说明

该工作连接 differentiable economics 与 strategyproof mechanism design。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2506.22911) 核对了 Theorem 2.9、Corollary 3.7、Theorem B.2、Theorem B.10 及实验供给模型。
