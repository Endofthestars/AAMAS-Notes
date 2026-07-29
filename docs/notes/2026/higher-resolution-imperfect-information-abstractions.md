---
title: "Beyond Outcome-Based Imperfect-Recall: Higher-Resolution Abstractions for Imperfect-Information Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/AKDO5185"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AKDO5185.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "low"
risk_tags: ["theoretical_abstraction_scope", "resolution_bound_not_performance_guarantee", "numeral211_benchmark_scope", "asymmetric_vs_symmetric_evaluation", "abstraction_pathology", "froi_not_scalable_algorithm", "poker_domain_assumptions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Beyond Outcome-Based Imperfect-Recall: Higher-Resolution Abstractions for Imperfect-Information Games

## 一句话总结

论文把 poker hand abstraction 建模为 signal-observation abstraction，提出 resolution bound 衡量抽象算法理论上可区分的信息集，并指出只看当前/未来结果的 outcome-based imperfect-recall 方法会丢失历史。FROI 将历史 outcome 信息纳入等价类，在三阶段简化 Hold’em 中优于 PAOI；但 FROI 本身是抽象/上界而非已解决可扩展聚类算法，且更细的 bound 不保证每次求解都更优。

## 方法与证据

- Signal observation abstraction 把原始 infosets 合并为玩家不可区分的 abstracted infosets；若合并后遗忘过去 signal observations，则为 imperfect recall。论文以 refinement 关系定义粒度，并将算法能达到的最细可区分结构称为 resolution bound（§3--4）。
- Theorem 4.2（改写自既有结果）只在两人、对手不抽象等限制下关联 refinement 与策略竞争力。作者明确说明更细 resolution bound 不保证生成抽象一定性能更好；它主要用于识别过粗上界的缺陷（§4.1）。
- PAOI 依据当前及未来 phase 的 win/tie/loss outcome features 聚类；FROI 是 k-ROI 的 full-history 特例，将历史 phase 的 outcome features 也纳入。论文认为 EHS/PAAEMD 的 resolution bounds 为 PAOI，历史丢失在后期造成 excessive abstraction（§4.2--4.3）。
- 直接实验用自构造三阶段 Numeral211 Hold’em，而不是完整 HUNL。Table 3：无抽象的 phase 1/2/3 infosets 为 780/29,640/1,096,680；PAOI 为 100/2,250/3,957，FROI 为 100/2,260/51,228，lossless isomorphism (LI) 为 100/2,260/62,020。
- 以 CFR 求 abstracted game 的 \(\epsilon\)-Nash 后回原游戏测 exploitability。五组不同初值的 EHS/PAAEMD 都明显差于 PAOI；PAOI 又明显差于 FROI/LI，FROI 在非对称评估中接近 LI（§5、Fig. 4）。非对称评估让一方不抽象而有理论解释，但大游戏中空间开销很大；对称评估会受 abstraction pathology 影响，细抽象可反而更差。

## 适用边界与复现

- 适用于有限、两人零和或类似 poker 的不完全信息博弈中分析 hand/signal abstraction 的信息损失；不直接给出任意 IIG 的均衡求解器或一般机制设计方法。
- resolution bound 是抽象算法可达的细化上界，不是特定聚类实现的实际性能、运行时间或 exploitability 上界；FROI 仍是 abstraction target，作者把面向 FROI 的算法开发列为未来工作。
- 实验采用特定的三阶段 Numeral211、bucket 数和 CFR；不能证明在 HUNL、多人 poker、不同 action abstraction、不同求解误差或其他 IIG 中同样成立。
- FROI 提高 class count（phase 3 为 51,228，对 PAOI 的 3,957），可能削弱压缩的规模收益。实践报告应包括内存、construction/solver time、bucket size、CFR error 和原游戏 exploitability。
- 复现应固定游戏规则/chance signals、SOOG 编码、PAOF/k-ROF、LI/PAOI/FROI construction、phase bucket budgets、CFR stopping/\(\epsilon\)、asymmetric/symmetric protocol、opponent abstraction、initial values 与 exploitability evaluator，并在多游戏尺寸验证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的不完全信息博弈抽象与策略求解论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AKDO5185.pdf) 核验模型、resolution bound、Tables 2--3 和 Numeral211/CFR 实验；没有把 FROI 的更细上界或该基准结果误写为无条件、更高效或通用更优的博弈策略保证。
