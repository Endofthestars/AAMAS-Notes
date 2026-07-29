---
title: "Robust Value Maximization in Challenge the Champ Tournaments with Probabilistic Outcomes"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/TEVB4201"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TEVB4201.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["worst_case_not_expected_value", "independent_match_outcomes", "binary_popularity_values", "adaptive_observability_requirement", "chromatic_number_dependence", "nonadaptive_hardness", "tournament_model_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Robust Value Maximization in Challenge the Champ Tournaments with Probabilistic Outcomes

## 一句话总结

论文研究 Challenge-the-Champ（CtC）赛制中对抗结果带概率时的 risk-averse 目标 Value Not At Risk（VnaR）：固定或自适应地安排 challenger 次序，最大化任意不确定比赛结果实现下都能保证的“popular winner”比赛数，而非期望观赏价值。对固定（non-adaptive）seeding，即使 binary popularity 且最优 VnaR 达理论上界，也有强近似困难；若每场结果公布后可重新选下一位 challenger，则依热门选手之间不确定边图的 coloring 给出加性保证，并至少取得上界一半。结果适用于特定 CtC、独立 match outcome 和 worst-case 偏好，不能直接解释为体育收入最大化或概率风险（如 VaR/CVaR）的通用优化。

## 方法与证据

- CtC 的第一个选手是 champ，依次迎战后续 challengers；比赛 value 是赢家 popularity，本文取二值 0/1。strength graph 的有向边权 \(p_{ij}\) 给 \(i\) 胜 \(j\) 的概率，边权 1 是 deterministic；论文假定不确定 match outcomes 相互独立（§1.1）。
- VnaR(\(\sigma\)) 是对所有不确定结果 realization 都至少得到的总 value，即概率 1 的下界，不是 expected revenue、胜率、分位数 VaR 或可容忍小失败概率的风险度量。偶然高价值/高概率但可能失败的 seeding 在此目标下可能没有优势。
- Proposition 1.1 给任意算法上界 \(n_p+n_u-1\)，其中 \(n_p\) 为 popular players、\(n_u\) 为被至少一名 popular player 确定击败的 unpopular players；其余 unpopular players 不贡献上界（§1）。这依赖二元 player-popularity value 建模。
- Theorem 1.2 及后续结果表明 non-adaptive polynomial-time seeding 具有加性/乘性近似 hardness，即使 optimal VnaR 已达该最大上界；论文也给简单固定 seeding 的较弱保证（§1）。因此不能期待一个通用、事前一次性排表的高质量 robust solution。
- 对 adaptive seeding，Theorem 1.5：若 popular players 上由不确定边构成的图 \(G_p\) 有 \(k\)-coloring，可得至少 \((n_p+n_u-1)-(k-1)\) 的 VnaR；Theorem 1.6 得至少 \((n_p+n_u-1)/2\)（§1）。可获得性/计算该 coloring 本身可能困难；小不确定边数时文中给 \(O^*(4^q)\) 算法。
- adaptive 的能力来自每场结果后再决定下一 challenger，类似动态配对，而非预先固定 bracket。该信息/控制权限在许多公开赛、转播合约、参赛可用性或公平规则下可能不允许，因此理论差距不应直接用于固定日程赛事。

## 适用边界与复现

- 适用于把“任何 upset realization 下仍保证最低数量的热门胜者/比赛价值”作为首要目标，且组织者可在历史 outcome 后合法改变下一场对手的顺序的 CtC/stepladder 决策。
- 若目标是平均收入、观众效用、公平、冠军质量、奖金、日程/休息约束或参赛者激励，应另建模；VnaR 可能偏向牺牲期望价值以换取极端 worst-case 下界。
- 复现需固定 strength graph、edge probabilities/独立性、popular labels、哪些边可认为不确定、seeding 是否 adaptive、outcome observation timing、VnaR evaluation（枚举/对抗 outcome realization）、coloring 算法与实例规模；分别报告 expected value 和 VnaR。
- 后续应研究相关/时间变化的胜负、非二元 matchup value、部分观测、日程公平约束、可有限次数重排的现场赛制，以及与 CVaR/机会约束等较平滑风险目标的比较。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 tournament design、鲁棒优化和近似算法工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TEVB4201.pdf) 核验 VnaR 定义、Proposition 1.1、non-adaptive hardness 和 Theorems 1.5–1.6；没有把 worst-case VnaR 表述为期望收益最优、现实赛制公平性或带相关概率结果的普遍保证。
