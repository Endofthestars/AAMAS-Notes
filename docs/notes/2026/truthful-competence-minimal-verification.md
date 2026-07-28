---
title: "Truthful Reporting of Competence with Minimal Verification"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "norms_trust_governance", "human_agent_interaction"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CZFV1739.pdf"
preprint_url: "https://arxiv.org/abs/2602.14076"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["verification_noise_scope", "dominant_strategy_scope", "penalty_bound_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Truthful Reporting of Competence with Minimal Verification

## 一句话总结

论文研究自报能力/成绩、只可抽查少数人的机制：在完美验证下刻画 dominant-strategy truthful、真诚者不受罚与有限惩罚之间的 audit–bias Pareto 前沿；噪声验证下改用 proper scoring rules 给出不同强度的可行方案。

## 方法与证据

- agent 的私有 competence $t\in[0,1]$，报告 $\hat t$；principal 决定 audit 概率与基于报告、验证结果的 grade。目标同时控制期望验证率、最大/平均 bias（真诚时期望 grade 减 type），同时要求 truth-telling 为弱 dominant strategy（HR1）、真诚者不被处罚（HR2）及 realized grade 不低于 $-\xi$（HR3）（§2）。
- 完美验证下，Monotone-Cutoff Verification（MCV）以 cutoff $\gamma$：低报告不审计并得 $\gamma$；高报告随报告增大而提高 audit 概率，查出不一致给 $-\xi$。所有 MCV valid（Proposition 3.3），并且任何 valid mechanism 都被某个 MCV 弱支配（Theorem 3.4）。
- 因而给定类型分布与惩罚下限，选择 $\gamma$ 即可显式权衡验证率与 bias；有限责任 $\xi=0$ 时，只要存在正概率的最低类型，零 bias 与非全审计不能同时达到（Corollary 3.7）。当分布未知时，adaptive MCV 以 leave-one-out histogram 选 cutoff，在不增加 verification 的前提下使平均 bias 至多比目标多 $1/n$（Theorem 3.9）。
- 噪声验证仅假设结果均值为真实 type，分布可未知并可相关，原始 HR2 放宽为期望不受罚 HR2'。Linear/PV mechanisms 把 proper scoring rule 做到每个 agent 的**期望** grade 中，从而保持 HR1；PV 以 $\kappa,\theta$ 控制 bias、audit 与允许惩罚，满足 HR3 当且仅当 Proposition 4.5 的参数条件成立。
- Histogram mechanism 可在已知精确离散 type histogram、类型间隔和放宽 HR1 至“唯一 truthful Nash equilibrium”时，做到零 audit 的均衡与任意小 bias；它并非 dominant-strategy 结论（Proposition 4.7）。经验图示使用 SAT、FICO 统计和 Beta 分布来展示 tradeoff（§5）。

## 局限与复现

- “完美验证最优”仅针对 HR1–HR3 的 valid mechanism 类与无噪验证；不能延伸为带噪审计下同样的全局最优性。
- 噪声部分的核心保证是 proper-scoring-rule 诱导的期望真实性；必须保留验证结果均值为 type 的假设，以及 PV 的参数/惩罚约束。
- Histogram mechanism 额外知道真实总体 histogram、类型离散且有最小间隔，并将 dominant-strategy 改为 unique Nash equilibrium；不适用于不可信统计或独立私下报告的通常场景。
- 复现应分别实现 MCV、LV/PV 与 Histogram，不要混合其信息与均衡假设；测量按类型的 audit 概率、最大/平均 bias、负 grade 下界，并以多种分布与噪声核检稳健性。

## 与 AAMAS 的关系与核验说明

该文将 audit design、评分和策略真实性用于 agent competence reporting。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2602.14076) 核对了 Proposition 3.3、Theorem 3.4、Corollary 3.7、Theorem 3.9、Proposition 4.5 与 Proposition 4.7 的结论范围。
