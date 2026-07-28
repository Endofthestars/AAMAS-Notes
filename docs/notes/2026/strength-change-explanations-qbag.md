---
title: "Strength Change Explanations in Quantitative Argumentation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/OKNZ9792"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OKNZ9792.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["formal_semantics_scope", "synthetic_layered_graph_evaluation", "heuristic_not_complete_solver", "contestability_not_decision_right"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Strength Change Explanations in Quantitative Argumentation

## 一句话总结

Strength-change explanation（SX）回答：在 Quantitative Bipolar Argumentation Graph（QBAG）中，允许改哪些 arguments 的 initial strengths，才能让指定 topic arguments 的最终强度达到目标排序；论文给出 soundness/completeness、最小变化概念及对小型合成分层 DAG 的 gradient-search，但不是对任意真实决策提出可行、唯一或因果正确的申诉方案。

## 方法与证据

- QBAG 含带 initial strengths 的 arguments、attack/support edges；gradual semantics 由 aggregation 与 influence functions 从初值迭代产生 final strengths（§3）。
- SX 是对 mutable set M 内 arguments 的 initial strength assignment 变化；应用后必须满足指定 preorder 的 final-strength ordering。变化量为所有 modified initial strengths 的 L1 差，0-approximate SX 即 optimal SX（Definitions 3--7、§4）。
- 论文证明空变化仅在目标排序已满足时为 SX/最优；基于 directionality、stability、balance 等 semantics principles，分析哪些 ordering 可/不可通过 mutable arguments 改变（§5--6）。
- 对 layered acyclic QBAG，作者实现 Adam gradient-descent heuristic，最多 100 iterations；时间复杂度给为 O(K·(|M|·|Args|+|Edges|))。该算法要求可微 strength function，cyclic situations 仅建议以 difference quotients 扩展、未实证（§7）。
- 因公开 QBAG benchmark 不存在，实验使用随机合成 layered graphs 与附加结构约束的可解图。全可变 constrained setting 取得 100% validity；部分可变时不总能找到 SX，最后配置约 99%（增加迭代后），论文承认可能是迭代不足或 local convergence（§7）。

## 适用边界与复现

- SX 是对所选 graph、semantics、mutable set 与目标排序的形式解释；它不自动说明应当改变哪个现实证据、谁有权修改输入、变化是否可接受，亦不等同于因果反事实、法律申诉或公平纠正。
- 解释质量依赖 initial strengths、attack/support edge 的来源及权重；若这些编码有遗漏、偏见或被操纵，得到的最小 L1 编辑也可能是误导性的。
- 启发式 search 没有一般 complete/optimal guarantee，尤其有 cycles、非可微 semantics、局部极值、有限 iterations 或部分 mutable arguments 时；99% 合成成功率不能推广到应用场景。
- 复现应发布 QBAG generator/layers/edge labels、semantics/aggregation/influence、topic ordering、M、optimizer/learning rate/iterations/seeds、validity 与 ordering correlations；实际用例还需 domain expert 审查、provenance 与受影响者的 contestation process。

## 与 AAMAS 的关系与核验说明

这是 computational argumentation 与 contestable XAI 的形式化工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OKNZ9792.pdf) 核对 Definitions 3--7、§6 性质、§7 heuristic/合成评测及限制；没有将 SX 当作自动决策纠正或真实世界因果解释。
