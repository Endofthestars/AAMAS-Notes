---
title: "Individual Rationality in Constrained Hedonic Games: Additively Separable and Fractional Preferences"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/ICRJ7770"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ICRJ7770.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "low"
risk_tags: ["theoretical_complexity_scope", "individual_rationality_only", "coalition_count_and_size_constraints", "parameterization_dependence", "weight_encoding_dependence", "no_constructive_deployment_claim"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Individual Rationality in Constrained Hedonic Games: Additively Separable and Fractional Preferences

## 一句话总结

论文刻画在必须形成恰好 \(k\) 个联盟或满足联盟大小约束时，是否存在 individually rational (IR) 划分的计算复杂性。对 IR，分数型与可加型 hedonic games 等价；但求解从一般权重下的 NP-complete 到受限图参数/权重下的 XP 或 FPT，结论是精细的理论分界而非一般联盟形成算法保证。

## 方法与证据

- IR 要求每个代理在其所属联盟的效用至少与单独成团相当（这里即非负）。约束变体分别要求恰好 \(k\) 个非空联盟（\(k\)-ASHG）或每个联盟有给定 lower/upper size bound（ASHG-SCC）（§2）。无约束时全体 singleton 是平凡 IR 解，难度来自这些形成约束。
- ASHG 的效用是联盟内 pairwise valuations 之和；FHG 再除以联盟大小。Lemma 3.1 说明对“效用是否非负”的 IR 可行性，这两个模型等价，因此后续只分析 ASHG；该等价不自动推广到效用大小、其他稳定性概念或福利比较（§3）。
- Theorems 3.2--3.3：对每个 \(k\ge2\)，两种约束变体判定 IR 存在性均 NP-complete，即使 valuations 对称；前者甚至在特定 split graph 上，后者在 clique 且仅六种 unary-valued weights 时成立（Table 1）。
- 当 weights unary encoded，Theorem 4.1 给出以 preference graph vertex-cover number 为参数的 XP 算法 \(n^{O(vc(G))}\)；但 Theorem 4.2 表明即使对称/unary/split graph，联合参数 \(k\)、负边数和 \(vc(G)\) 仍 W[1]-hard（§4）。因此“权重多项式有界”不等于 FPT。
- Theorem 4.3 对 **仅 \(k\)-ASHG** 给出以 \(vc(G)\) 和最大 weight \(\omega_{max}\) 为参数的 FPT，通过枚举 vertex cover 划分并以 N-fold ILP 扩展独立集；算法亦可处理非对称 valuations。该 FPT 表述不能直接迁移给 size-constrained variant（§4）。
- 在更一般 tree-like 图上，Theorem 5.1 显示即使 \(k=2\)、对称 binary weights，以 treedepth 参数仍 W[1]-hard；Theorem 5.2 则对 binary valuations 的 \(k\)-ASHG、以 treewidth 参数给出 XP DP，若再参数化最大度数则 FPT（Corollary 5.3）（§5）。

## 适用边界与复现

- 适用于研究者需要判断固定联盟数量/容量下 IR 划分的可计算性，或基于 preference graph 的结构参数选择算法。它不提供真实团队/市场中偏好采集、动态谈判、策略操纵、支付、公平或福利最优的实证结论。
- NP/W[1]/XP/FPT 的含义取决于问题变体、编码（一元/二元/一般权重）、\(k\)、图类和参数组合；将某个正面算法结论抽离这些前提会导致错误复杂性推断。
- 理论中的 pairwise valuations、精确非负阈值和已知 preference graph 在实践中未必可观测；估计误差或不完整偏好会改变 IR 判定，且 IR 仅排除代理偏好 singleton 的情况，不代表 Nash/core stability 或公平。
- 复现应正式实现 \(k\)-ASHG/ASHG-SCC 的输入编码和 IR check，小实例枚举所有划分核对 Lemma 3.1；对 unary/vc 实现 DP，对 \(vc+\omega_{max}\) 实现 N-fold ILP，对 binary/tw 实现 tree-decomposition DP，并分别报告参数、运行时间和适用变体，不能用随机实验替代复杂性证明。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的联盟形成与参数化复杂性论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ICRJ7770.pdf) 核验 Table 1、Lemma 3.1、Theorems 3.2--5.2 与 Corollary 5.3；没有把受参数和编码限制的算法结论误述为普适的联盟分配或稳定性方案。
