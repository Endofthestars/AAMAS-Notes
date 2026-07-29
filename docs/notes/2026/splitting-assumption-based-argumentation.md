---
title: "Splitting Assumption-Based Argumentation Frameworks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/LPCA5015"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LPCA5015.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03g"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "formal-semantics-scope", "splitting-set-required", "no-implementation-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Splitting Assumption-Based Argumentation Frameworks

## 一句话总结

论文给 ABA frameworks 的 modification-based splitting：先解下层 subframework，再依 accepted/rejected/undecided assumptions 构建上层 reduct；对 undecided 依赖引入 fresh self-loop assumption，避免错误传递。作者证明指定 semantics 下局部 extensions 的组合与原框架 extensions 对应；这是形式分解性质，尚无实现性能评测。

## 方法与证据

- 先在 induced SETAF 定义 splitting/reduct：移除已 defeated arguments/attacks、投影跨界 attacks，并以 self-attack 处理依赖 undecided arguments 的 collective attacks（§3）。
- ABA 层为 undecided 可导句引入 fresh assumption/rule，并修改包含其的 rules；Example 3 给出所得 preferred extension（§4）。
- 作者称每步可高效并可构建在 ABA/SETAF solvers 上，但 implementation/evaluation 是 future work（§5）。

## 适用边界与复现

- 复现需明确 ABA language/rules/assumptions/contraries、splitting set、semantics和 reduct construction；对比全局 solver 的 extension equality与运行时。不可将局部求解自动视作所有 ABA variants 或实务推理加速。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LPCA5015.pdf) 人工核对 SETAF/ABA transform、未决处理与结论；未将可实现性写成已验证性能收益。
