---
title: "The Impossibility of Strategyproof Rank Aggregation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DTZH2224.pdf"
preprint_url: "https://arxiv.org/abs/2602.06582"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["impossibility_scope", "computer_aided_proof", "strategyproofness_definition"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# The Impossibility of Strategyproof Rank Aggregation

## 一句话总结

论文研究以 Kemeny distance 衡量操纵收益的社会福利函数（SWF）：证明若干匿名/一致性/strategyproofness 的组合不可能，并以 SAT 求解加 Isabelle/HOL 形式化验证支撑主不可能性结果。

## 方法与证据

- SWF 把每位 voter 的完整严格 ranking 聚合为一个 output ranking；Kemeny-strategyproofness 要求任何单一 voter 偏报后，输出不能比诚实输出更接近其真实 ranking（§1–2）。
- Theorem 1：当 $m\ge4$、$n\ge9$ 且 $n\notin\{10,12,14,16\}$ 时，没有同时 majority-consistent 和 strategyproof 的 SWF。majority consistency 仅在 profile 的多数关系本身是 ranking 时要求输出该 ranking（§3）。
- 作者还报告更小的计算机辅助 base cases：$m=4,n\in\{3,4\}$ 的 majority-consistency 不可能性已由 Isabelle/HOL 核验；但这不是 Theorem 1 原始人手推导的一般范围（Remark 2）。
- Theorem 2：没有同时匿名、unanimous、strategyproof 的 SWF，条件为 $m\ge5$ 且 $n$ 为偶数，或 $m=4$ 且 $n$ 为 4 的倍数。其 SAT base cases 是 $(m,n)=(5,2)$ 与 $(4,4)$，再经归纳推广，并以 Isabelle/HOL 验证（§4）。
- Theorem 2 不能直接推广到任意奇数 voter 数：作者明确指出在 $m=4,n\in\{3,5\}$ 有满足这些公理的 SWF；若改为更强的 near unanimity，才得到部分奇数 $n$ 的延伸（Remark 4）。
- 对 Kemeny rule、distance scoring rules 与 positional scoring rules，论文以 incentive ratio 衡量操纵强度；前两类有至少 $m^2-m$ 的下界，而 positional scoring 在 $m\ge3$ 时可为无界（§1、§5）。

## 局限与复现

- 所有结论针对 deterministic single-ranking SWF、完整严格偏好和 Kemeny-distance 策略性；它们不自动覆盖随机/集合值聚合、其他 ranking distance、弱序或受限偏好域。
- 不可把 Theorem 2 简化为“所有 $m\ge4,n$ 都不可能”：其 $m=4$ 需 $4\mid n$，而 $m\ge5$ 的一般结论要求偶数 $n$。
- 对 computer-aided result 的复现应分别检查 SAT encoding、UNSAT/MUS 证据、归纳提升和 Isabelle/HOL 开发；只重新运行 SAT solver 不等价于核验全部推广步骤。
- incentive ratio 描述最坏情形操纵增益，不是某一数据集上的平均操纵频率或用户行为预测。

## 与 AAMAS 的关系与核验说明

该文将社会选择中“抗操纵”要求用于多 agent 的 ranking aggregation。笔记基于作者公开的 [AAMAS 版 PDF](https://cgi.cse.unsw.edu.au/~plederer/research/SPRA.pdf) 和 [arXiv 记录](https://arxiv.org/abs/2602.06582) 核对了定理中的 $m,n$ 量词、SAT base case 与 Isabelle 验证边界。
