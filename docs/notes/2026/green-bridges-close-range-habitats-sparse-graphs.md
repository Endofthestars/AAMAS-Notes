---
title: "Placing Green Bridges Optimally, with Close-Range Habitats in Sparse Graphs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "resource_allocation", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/OYZM4458"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OYZM4458.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["graph_abstraction_of_ecology", "fixed_diameter_two_requirement", "small_habitat_sparse_graph_assumptions", "no_species_or_field_validation", "infrastructure_feasibility_not_modeled"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Placing Green Bridges Optimally, with Close-Range Habitats in Sparse Graphs

## 一句话总结

本文将 wildlife crossing 选址抽象为带成本 graph edge selection：为每个物种的 habitat vertex subset 选边，使诱导子图直径至多 2 且总成本最小。它给出稀疏/平面图与小 habitat 的精确算法及几乎紧的 NP-hardness 边界；结果适用于这个静态图模型，不能直接说明廊桥会改善真实物种迁移、种群健康或项目许可可行性。

## 方法与证据

- `d-Diam GBP-C` 输入为潜在 crossing 图、edge costs、habitat 集合、forced edges 与预算；问能否选含 forced edges 的子集，使每个 habitat (H) 在所选边诱导图中的 diameter 不超过 (d)。主文聚焦第一个非平凡值 (d=2)，无成本/forced-edge 版本记为 `2-Diam GBP`（Problem 1、§1--2）。
- 对 `2-Diam GBP-C`，论文证明：最大度数 (\Delta\le3) 时线性时间可解；(\Delta\le4) 且 habitat size 至多 4 时线性时间可解；planar 图且 habitat size 至多 3 时可在 (O(n^2r^2+r^3)) 时间求解（Theorem 1--3）。
- 平面、size-3 情形利用 habitats 的内外层级和 reducible-habitat reduction，化为每个 habitat 都为 face 的已知可解情形。(\Delta\le3) 情形将三角形分成常数大小、vertex-disjoint zones 后逐区穷举；(\Delta\le4)、size-4 情形构建 habitat intersection graph，其 component 为 path/cycle 或常数大小，再做动态规划（§3--5）。
- 硬度边界：`2-Diam GBP` 即使最大度数 5、habitat size 3 也 NP-hard；若同时要求 planar，habitat size 4 也 NP-hard。归约来自 Planar Cubic Vertex Cover，详证在完整版本（Theorem 4、§6）。
- 预处理会将某些不可替代边标为 forced，移除已满足 habitat/无关边/小 component。论文还指出最大度数 4、habitat size 至少 5 的复杂度仍开放，并提到 path-DP 可推广到 tree/bounded-treewidth intersection structures（§2、§7）。

## 安全边界与复现

- vertex/edge/habitat 是对土地、可建 crossing 和物种活动范围的抽象；直径 2 只是每个 habitat 内的短 graph path 约束，并不包含道路宽度/车流、地形、产权、工程成本不确定性、季节性、捕食风险、气候变化、行为回避、遗传连通性或多物种栖息地质量。
- 算法适用条件是显式图类与小 habitat size，不能把 linear/polynomial-time 结论泛化至一般 road network。尤其从 (\Delta=4) 到 5 或 planar habitat size 3 到 4 已出现 NP-hardness，真实实例应先验证图建模与参数，再明确使用 exact、approximation 或 heuristic。
- 每个 habitat 都要求 diameter exactly bounded by the uniform (d=2)；论文自身将 (d\ge3) 和 adaptive diameter（如相对原图直径的倍率）列为未来方向。不同物种的移动尺度和连通性需求不应被一个固定阈值替代。
- 复现应发布图构造、habitat polygons-to-vertices mapping、edge costs/forced-edge 依据、planarity/degree checks、reduction order、算法/DP 状态及完整版本中的 gadgets。实际选址还需生态调查、野生动物监测、事故/通行数据、生命周期成本、环境影响评估、社区/原住民协商与适应性后评估。

## 与 AAMAS 的关系与核验说明

这是生态网络设计动机下的图算法与复杂度工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OYZM4458.pdf) 核对 Problem 1、Theorem 1--4、intersection-graph 方法、NP-hardness 条件与结论限制；没有把静态直径约束的最优解表述为生态成效或基础设施部署结论。
