---
title: "Computational Aspects of Plan-Dependent Model Equivalence: The Case of Knowing-How Bisimulations"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/OKUJ9671"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OKUJ9671.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "low"
risk_tags: ["finite_model_scope", "plan_set_input_dependency", "contraction_preservation_scope", "no_runtime_system_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Computational Aspects of Plan-Dependent Model Equivalence: The Case of Knowing-How Bisimulations

## 一句话总结

本文研究不确定性 knowing-how logic 中、相对于 agent 可辨识计划集合的 LTS 模型等价：以纯结构条件定义 L*Kh-bisimulation，证明其对逻辑的 adequacy，并给出有限模型比较的 coNP-completeness 与可高效构造的保持语义模型压缩。

## 方法与证据

- LTSU 在通常 action transition 之外，为每个 agent 指定其能区分的计划集合；Kh_i(φ, ψ) 表示存在从所有 φ-state 都能强可执行、且必达 ψ 的可辨识计划集合（§1--2）。
- 新的 L*Kh-bisimulation 用 valuation、action 及 plan-set 的结构条件替代旧定义中“命题可定义集合”的语法 clause。它蕴含原 LKh_i-bisimulation；有限-state LTSU 上二者等价，且 L*Kh-bisimilar 模型满足同一 LKh_i formulas（§3）。
- 对 finite LTSU，给定 relation 的 CheckKhiBisim 为 coNP-complete（Theorem 4.5）；以由 valuation 相等组成的关系检查两模型时，KhiBisim 与 pointed 版本 PKhiBisim 也均为 coNP-complete（Corollaries 4.7--4.8）。下界来自 DNF tautology，反例验证程序还能抽取多项式大小的区分公式。
- valuation contraction 合并同一命题 valuation 的 states，并把相关路径抽象成单步 action；其最大 auto-bisimulation 可由 valuation 直接得到。论文还给出借用标准 BML auto-bisimulation 的 contraction；两种压缩都保持 L*Kh 语义（§5）。
- 作者说明 LKh_i model checking 对 state 数及 agent 知道的 plan 数为多项式，而压缩旨在减少这些度量；结尾提出 further work 为 simulation/trace equivalence、保留分支度或 plan 长度的最小化（§1、§6）。

## 适用边界与复现

- coNP-complete 结论针对输入明确给出的有限 LTSU 与计划/不确定性表示；不能直接外推到无限状态、隐式/生成式计划空间，或其他 knowing-how logic。
- “最小模型”是该 bisimulation 保持意义下的 state/plan 表示压缩；并不保证保留原 action 命名、路径长度、branching factor 或所有系统工程属性。
- BML contraction 便于复用既有算法并避免 action renaming，但其 auto-bisimulation 对 LKh_i 并非 maximal；应依需要在压缩率与 action-label 可解释性间选择。
- 复现应固定 finite states、propositions/valuations、transitions、每 agent 的 U(i)、relation Z 与 strong-executability 定义；分别检查 structural clauses、区分公式、contraction 前后 LKh_i satisfaction，并报告 state/action/plan 数变化。

## 与 AAMAS 的关系与核验说明

这是关于多智能体知识、计划与形式模型比较的理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OKUJ9671.pdf) 核对 L*Kh 定义语境、Theorem 4.5、Corollaries 4.7--4.8、§5 contractions 与结论；没有把有限、显式模型的复杂度结果泛化为通用系统验证结论。
