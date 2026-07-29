---
title: "Robust Multiagent Collaboration Through Weighted Max-Min T-Joins"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "resource_allocation"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LCPB6005.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02d"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["approximation_bound_scope", "metric_space_assumption", "upper_bound_not_solution", "pdf_doi_placeholder"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Robust Multiagent Collaboration Through Weighted Max-Min T-Joins

## 一句话总结

论文研究加权 max--min T-join/2k-matching：选择偶数顶点集合，使其最小权完美匹配尽可能大，从而形式化最坏配对下的鲁棒性；给出贪心上界、对 T-join 的对数近似，以及基于 ear decomposition 的另一上界。

## 方法与证据

- 在正边权连通图诱导的 metric 上，max--min T-join 寻找偶数顶点集 T，使 T 上的 minimum-weight perfect matching 成本最大；等价表述是选择最大权 valid subgraph，要求每个 cycle 中选中边权不超过该 cycle 总权的一半（§1、§3）。
- 对固定大小的 max--min 2k-matching，算法从任意顶点出发反复加入距当前集合最远的顶点，并计算各偶数前缀的最小权匹配。Theorem 2.1 给出最优值不超过 `2(1+H_k-1)·opt_2k` 的上界；计算该上界需 `O(nk+k^4)` 时间（§2）。
- Theorem 2.2 将其用于未固定大小的 weighted max--min T-join：以 `k=floor(n/2)` 时的前缀值给出 `2(1+H_floor(n/2)-1)` 因子的对数近似，文中给出总运行时间 `O(n^4)`。
- 对一般加权图，作者先收缩 bridges，再用 2-edge-connected 图的 ear decomposition 构造 valid edge set。Theorem 3.2 给出上界 `μ(G) ≤ Σ_i max(P_i)`；但单个耳的 `max(P)` 等价 knapsack，通常 NP-hard，只能以 FPTAS 近似（§3）。
- 学校交换、城市合作等是动机例子；扩展摘要没有针对真实伙伴匹配数据的评测，也未证明这些具体应用满足图、距离或最坏匹配的建模假设。

## 适用边界与复现

- 结果针对正权连通图/metric、完美匹配成本和形式化的 worst-case 目标；不自动编码协作技能、偏好互惠、容量、稳定性、参与者同意或现实公平。
- `2 ln n`/调和数因子是相对最优目标的近似/上界保证，不是对原问题给出精确最优配对，也不表示实际系统的鲁棒性比例提升。
- 耳分解结果需桥收缩和 2-edge-connectivity；其 `max(P)` 子问题仍要处理 knapsack 近似误差。文中“实验更紧”没有在扩展摘要提供实例、统计或设置，不能独立验证。
- 复现应给出图/距离构造、权重尺度、目标 k、贪心起点与 tie-breaking、minimum-weight matching solver、ear decomposition、FPTAS 的 ε、比较基线和实例分布；若用于人员或机构配对，还需额外评估伤害、偏差及参与者约束。

## 与 AAMAS 的关系与核验说明

这是鲁棒组合优化在多智能体协作中的理论建模。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LCPB6005.pdf) 核对 §1--3、Theorems 2.1--2.2 与 3.2。官方目录没有 DOI，而 PDF 页眉/引文中的 `10.65109/V1X2Y3Z4` 为占位格式，故元数据 DOI 暂留空，未将其写成可用标识。
