---
title: "EFX Allocations Exist on Triangle-Free Multi-Graphs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "argumentation_reasoning", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/XYOA9688"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XYOA9688.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "low"
risk_tags: ["triangle_free_skeleton_requirement", "graphical_valuation_scope", "monotone_goods_only", "pseudo_polynomial_general_case", "cancelable_valuation_polynomial_time", "existence_not_general_efx"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# EFX Allocations Exist on Triangle-Free Multi-Graphs

## 一句话总结

论文证明：在 graphical multi-graph valuations 中，只要 skeleton（任意两 agent 有至少一条共享边则连边的简单图）无三角形，就始终存在完整 EFX allocation。对 monotone valuations 给出伪多项式构造算法；对 cancelable valuations（严格包含 additive）才给多项式算法。该结果扩大了 EFX 已知存在的图类，但不解决一般任意 valuation/任意图中 EFX 是否存在，也不覆盖 chores、非单调偏好或需要非 incident 商品价值的资源分配。

## 方法与证据

- 每件 indivisible good 是 multi-graph 的一条边，agent 是节点，agent 只评价与自身 incident 的边；可有平行边。triangle-free 指 skeleton girth 至少 4，而非禁止两 agent 间多件 goods（§1–2）。
- EFX 要求任意 \(i,j\)，从 \(j\) 的 bundle 删除任意一件 good 后，\(i\) 都不再 envy；比 EF1 的“存在一件可删”强（§1）。存在性是在这一定义、完整分配和 goods 的单调估值下成立。
- Theorem 3.1（摘要/§1.1）给 triangle-free multi-graphs 上 EFX existence；monotone valuations 有 pseudo-polynomial computation，cancelable valuations 有 polynomial computation。伪多项式依赖数值尺度，不能被称为一般多项式高效算法。
- 算法先将每对 agent 的平行边划为两个从指定 agent 视角 EFX-feasible 的 unit bundles；Phase One 维持 partial EFX、各 agent 不嫉妒未分配 incident unit bundle、envy graph 最长路径至多一（§1.1）。
- 余下 phases 在 envy-star 结构上对 unit bundles 作局部分配/撤回/交换；triangle-free 性质保证涉及不同邻居 bundle 时不会产生三角耦合，使这些调整保持 EFX 并最终完成分配（§1.1）。这是构造证明，不是实际市场的动态/策略激励机制。
- cancelable 估值满足两 bundle 同时去掉相同 good 后的严格偏好不反转，additive 是其严格子类（§2）。若 valuation 只有 oracle、非 cancelable、含互补/替代导致该性质失效，论文的 polynomial-time 结论不适用。

## 适用边界与复现

- 适用于共享资源可自然表示为两方 incident edge、且 interaction skeleton 无三角关系的分配问题，如某些双边共享设施/边界资源模型；适合寻求 exact EFX 而非仅 EF1。
- 不能据此断言一般多方资源、三角/高聚类网络、任意非加性 valuation 或 chores 都有 EFX。真实分配还可能需效率、预算、权利、可拆分性与策略防操纵约束，本文不处理。
- 复现应固定 multigraph/skeleton、agent valuation representation、unit-bundle divider、tie-breaking、envy graph、所有 phases 的 invariant/termination checks；分别报告 pseudo-polynomial numeric dependence 与 cancelable-instance runtime。
- 后续应探索含 triangle 的最小反例/更多图类、一般 valuation 的存在边界、可验证的 valuation oracle complexity、EFX 与 Pareto/NSW/strategyproofness 的联合可达性。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的公平分配与算法博弈论工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XYOA9688.pdf) 核验 triangle-free multi-graph 模型、Theorem 3.1 的 existence/复杂度范围和三阶段技术概览；没有将 restricted graphical valuation 的结论外推成一般 EFX 存在或现实资源机制的激励兼容保证。
