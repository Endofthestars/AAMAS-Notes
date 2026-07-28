---
title: "Comparing the Fairness of Recursively Balanced Picking Sequences"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WIZK2813.pdf"
code_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["theorem_assumptions", "additive_utilities"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Comparing the Fairness of Recursively Balanced Picking Sequences

## 一句话总结

论文比较递归平衡的物品挑选序列，以 egalitarian price 和近似 maximin share（MMS）刻画不同序列在公平分配上的最坏情形差异。

## 方法与证据

- §2 假设 `n≥2` 个智能体、`m` 个不可分物品、可加效用和总序偏好；递归平衡指每个前缀中任意两名智能体的挑选次数之差至多为 1。
- Proposition 2.1 说明：挑选序列当且仅当递归平衡时，始终产生 EF1 分配。
- §3 定义在固定首轮前缀下的 egalitarian price。引言给出两个结果：相对同前缀的全部挑选序列，所有递归平衡序列有相同价格 `min{m-n+1,n}`；相对同前缀的递归平衡序列，价格为 `min{ceil(m/n), floor(log2 n)+1}`。
- §4 对 regular sequence 给出 MMS guarantee 的刻画（Theorem 4.2），对少量 irregular sequence 另行处理（Theorem 4.5），并由 Theorems 4.6–4.7 给出最优/最差 MMS 序列的描述。

## 局限与复现

- 结论依赖可加效用、挑选偏好与递归平衡/固定首轮前缀等形式条件；不等价于所有实际分配机制的公平保证。
- 论文分析的是最坏情形的理论指标，不能直接推断行为实验、策略操纵或真实偏好获取下的表现。
- 复现需保留 §2–4 中的实例定义、序列集合与 welfare/MMS 比较基准，并逐项核对定理前提。

## 与 AAMAS 的关系与核验说明

该工作位于算法博弈论和资源分配。笔记仅保留 Proposition 2.1 和引言/§3–4 明示的理论结果，并明确其依赖的效用与序列条件。
