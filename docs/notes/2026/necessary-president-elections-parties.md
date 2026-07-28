---
title: "Necessary President in Elections with Parties"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "resource_allocation"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RYRS8869.pdf"
preprint_url: "https://arxiv.org/abs/2602.10601"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["voting_rule_scope", "nonunique_winner_model", "parameterized_complexity_scope", "theoretical_not_empirical"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Necessary President in Elections with Parties

## 一句话总结

论文研究政党各提名一名候选人时，指定候选人 $p$ 是否无论其他党怎样提名都仍为赢家（Necessary President）；它给出多种计分与 Condorcet-consistent 规则下的多项式、coNP-complete 及参数化复杂度边界。

## 方法与证据

- 输入是候选人被分为 parties、每党恰好提名一人后的 reduced election；问题问当 $p$ 所在党提名 $p$ 时，所有其他提名组合下 $p$ 是否为 winner。采用 non-unique winner 模型：平局并列第一也算 $p$ 赢；因此问题和“唯一胜者”或党可提名多人的模型不同（§2）。
- 对所有能在多项式时间确定 winner 的规则，反例是一个使 $p$ 失败的 nomination，故 Necessary President 属于 coNP（Observation 1）。直接枚举的复杂度受最大 party size $s$ 和 parties 数 $t$ 影响，论文再分别用 $t,s,\tau$（voter types）和 $|V|$ 作参数（§2）。
- Borda、任意 $\alpha\in[0,1]$ 的 Copeland$^\alpha$、Maximin 均给出多项式算法：Borda 的 Algorithm NP-Borda 时间为 $O(|C|^2|V|)$；Copeland 的 NP-Copeland 为 $O(|C|^2|V|)$；Maximin 的 NP-Maximin 为 $O(|C|^2(|C|+|V|))$（Theorems 3.1、4.1–4.2）。这是该精确定义和 winner 模型下的判定复杂度，不是求最佳提名策略的实证表现。
- 对 short positional rules（固定常数个非零名次，包含固定 $\ell$-Approval）和 Veto-like rules（固定常数个末位与其余相同，包含固定 $\ell$-Veto），Necessary President 即使 $s=2$ 也 coNP-complete（Theorems 3.2–3.3）。该“即使”是 hard-instance 限制，不表示每个小党实例都难。
- 对上述两类 positional rules，按 parties 数 $t$ 参数化是 W[2]-hard 且在 XP；按 voter types 数 $\tau$ 则 FPT（Theorems 3.4–3.7、Table 1）。表中的 XP 来自枚举/算法观察，W[2]-hard 不等价于无条件“无法求解”。
- Ranked Pairs 的结论更强：即使 $s=2$ 且 $|V|=12$，问题 coNP-complete（Theorem 4.3）；以 $t$ 参数化时即使 $|V|=20$ 仍 W[1]-hard 且在 XP（Theorem 4.4、Table 1）。论文的 Ranked Pairs winner determination假定采用某种 tie-breaking；结论并非对未指定的所有实现细节自动成立。
- Table 1 还汇总：若规则有高效 winner computation，则联合参数 $(s,t)$ 是 FPT（Observation 2）；该表将“in P”“coNP-complete”“W-hard/in XP”与具体 rule/参数限制逐项区分，不能把某一条硬度推广到所有 voting rules。

## 局限与复现

- 研究是复杂度分类，没有在真实选举数据上测量党派行为、投票率、策略互动、候选撤退成本或公平性结果；它不建议现实选举制度应采用哪一个规则。
- “necessary”量化所有其他党 nomination，且只检查 $p$ 是否在 winners 集合中；若改变为 unique winner、Possible President、允许多提名、多赢家委员会、候选人自行参选或偏好不完整，结论需重新证明。
- FPT/W[1]/W[2]/XP 都是关于特定参数的渐近分析。尤其 FPT 依赖 voter-type 数而非总选民数，实际运行时间中的参数函数仍可能很大；coNP-hard 结论也不排除小规模或结构化 profile 的有效算法。
- Ranked Pairs 对 tie-breaking 的实现与输入偏好表示需固定；复现 reductions 时应验证 party size、voter-count 常数、winner model和多数图锁边顺序，避免把 arbitrary tie 处理混入定理。
- 复现应实现 reduced-election 枚举作小实例 oracle，并分别验证三套多项式算法、short/Veto-like 的 scoring-vector 前提、$\tau$ 的等价 voter preference grouping，及论文 reductions 的 yes/no 对应关系。

## 与 AAMAS 的关系与核验说明

该文服务于多 agent 决策中的候选提名和机制设计，给出“跨所有对手提名仍获胜”的计算边界。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2602.10601) 核对问题定义、非唯一赢家模型、Table 1、算法复杂度与硬度定理；所有结论均保留其 voting rule 和参数化前提。
