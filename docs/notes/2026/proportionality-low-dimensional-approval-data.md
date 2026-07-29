---
title: "Proportionality from Low-Dimensional Approval Data"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "marl_coordination"]
dblp_key: ""
doi: "10.65109/YHKI7695"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YHKI7695.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["theorem_assumptions", "query_model_scope", "rlhf_application_not_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Proportionality from Low-Dimensional Approval Data

## 一句话总结

论文研究每位选民只能回答少量候选项批准查询时如何选出比例代表委员会：在有限 voter types、候选区间（CI）或稀疏批准等结构假设下，给出重构 profile 或满足 EJR+/近似 JR 的查询算法与界限。

## 方法与证据

- 目标是从 sparse approval queries 识别满足 justified representation（JR）及其强化版本的多赢家委员会；查询复杂度按被查询候选子集大小与查询次数计（§1）。
- 对至多有 `s` 种选民类型的 approval profile，Theorem 1 给出 poly-time 的 `s`-dimensional、`O(m·log s)` 查询算法来重构 profile；适用的查询维度范围是 `log s` 至 `s`，而非任意 profile 的常数查询保证。
- 对候选区间（含圆上的 CI）偏好，已知共同候选顺序时，作者提出用 `O(m)` 个二维查询满足 EJR+ 的规则；顺序未知时，Theorem 2 给出 `O(m²)` 个二维查询的 EJR+ 算法，并说明非自适应识别比例委员会有 `Ω(m²)` 下界。
- 在每位选民至多批准 `q` 名候选人的稀疏批准设定，Theorem 3 给出 `O(m²)` 个二维查询、满足 `2/q`-JR 的算法；这是近似比例性，并非 EJR+。
- 作者还将二维查询推广到一族 Thiele rules，并以 Euclidean synthetic models 和 Pabulib 参与式预算 profile 评估 metric/heuristics；文中称其实际表现优于最坏情形，但扩展摘要未给出足以独立复算的完整实验表格。

## 适用边界与复现

- 结论依赖 approval-query 接口，以及有限类型、CI/circle order 或每人最多 `q` 个批准等结构；不能据此宣称一般大规模投票、参与式预算或 RLHF 都能以常数提问获得比例性。
- EJR+、JR 与 `2/q`-JR 是形式化代表性标准；它们不直接衡量候选质量、选民理解、策略操纵、隐私成本或真实世界公平。
- RLHF 是引言中的潜在动机，本文没有报告训练语言模型或人类反馈实验，因此不构成对对齐效果的实证结论。
- 复现需明确候选数/委员会大小、查询是否自适应、profile domain 与共同顺序是否已知、`s` 或 `q`、所检验的比例性定义，以及 Euclidean/Pabulib 数据预处理与 rule 参数。

## 与 AAMAS 的关系与核验说明

这是计算社会选择中的查询高效多智能体决策工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YHKI7695.pdf) 核对 §1、Theorems 1--3 和摘要中对实验的限定，未把结构化设定下的理论保证泛化为部署建议。
