---
title: "Obnoxious Facility Location Problems: Strategyproof Mechanisms Optimizing Lp-Aggregated Utilities and Costs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CUAX9588.pdf"
preprint_url: "https://arxiv.org/abs/2512.18620"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["mechanism_assumption_scope", "strategyproofness_definition", "approximation_bound_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Obnoxious Facility Location Problems: Strategyproof Mechanisms Optimizing Lp-Aggregated Utilities and Costs

## 一句话总结

论文研究一维区间上单个厌恶设施的选址：agent 希望设施离自身报告位置越远越好；在 strategyproof（及 group-strategyproof）约束下，给出覆盖不同 $p$ 的 $L_p$ 聚合效用/成本目标之近似界。

## 方法与证据

- 基础模型是 $n$ 个策略 agent 位于 $[0,1]$，设施位置为 $y$；效用 $u_i=|x_i-y|$，成本 $c_i=1-|x_i-y|$。随机机制下，个体效用与成本先对机制分布取期望（§2）。
- 对社会效用，论文最大化 $\mathrm{su}_p=(\sum_i u_i^p)^{1/p}$；$p=1$ 是总效用，$p=+\infty$ 是最大效用，$p\to0^+$ 以几何均值/Nash welfare 单列处理。有限负 $p$ 在零效用处通常无定义，因此正文只把 $p=-\infty$ 作为最小效用边界情况（§2–3）。
- 对社会成本，论文最小化 $\mathrm{sc}_p=(\sum_i c_i^p)^{1/p}$，但只分析 $p\ge1$ 及 $+\infty$：文中明确将 $p<1$ 的成本聚合排除，因为该非凸聚合会过度奖励把伤害集中到少数 agent（§4）。
- Majority Vote 在两端点间按左右半区人数选择位置；Theorems 1、10 分别给出其对有限 $p$ 的效用/成本 $(2^p+1)^{1/p}$ 近似以及对相应 $L_\infty$ 的 2 近似。结合对任意确定性 SP 机制的下界，论文将这些确定性界表述为 tight（§2、§3–4）。
- 对随机机制，结论是上、下界区间而非普遍紧确：例如有限 $p>0$ 的效用下界来自 Theorem 4，而相应上界由特定 GSP 机制给出；$p\to0^+$ 的几何均值有 uniform 机制的 $\sqrt2+1$ 上界和 $\sqrt{6/5}$ 下界（§3）。
- 随机化分析与机制类别不能混读：Mechanisms 2–4 被证明为 GSP，但随机 lower bounds 的陈述只要求 SP；论文未将所有随机区间宣称为已闭合（§2–3）。

## 局限与复现

- 保证仅适用于单设施、一维规范区间、distance utility/one-minus-distance cost、风险中性期望和可直接报告位置的模型；不自动覆盖多设施、网络/高维空间、预算约束、带货币支付的机制或学习型 agent。
- “tight”应只用于确定性 SP/GSP 的表中范围；随机机制的多数条目仍存在上下界间隙，不能将某一个构造机制的上界称作随机最优。
- $p\to0^+$ 使用的是归一化 power mean 的极限（几何均值），并非未归一化 $L_p$ 和；实现/比较实验时应避免将两种目标直接互换。
- 复现应在同一 profile 上分别计算确定位置和随机分布下的目标值，并检验单 agent 与 coalition 偏报的不增益条件；还应按 $p$、$n$ 和 utility/cost 目标分别报告 ratio，不能用单一平均得分替代 worst-case approximation。

## 与 AAMAS 的关系与核验说明

该文以机制设计刻画策略性 agent 在公共厌恶设施选址中的效率—激励权衡。笔记基于作者公开的 [arXiv HTML 原文](https://arxiv.org/html/2512.18620v1) 人工核对了模型、机制类别和定理适用范围；随机结果按未闭合区间记录。
