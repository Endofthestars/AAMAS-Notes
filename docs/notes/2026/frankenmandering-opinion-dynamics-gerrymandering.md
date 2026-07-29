---
title: "Frankenmandering: The Confluence and Symbiosis of Opinion Dynamics and Gerrymandering"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["game_theory_mechanism", "norms_trust_governance", "argumentation_reasoning", "resource_allocation"]
dblp_key: ""
doi: "10.65109/QBUW2742"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QBUW2742.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04r"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_formula_and_schema_revision"
spark_consistency: "pass_after_terra_social_harm_revision"
risk_level: "high"
risk_tags: ["opinion_manipulation", "strategic_redistricting", "handcrafted_examples", "ambiguous_piecewise_rule", "hdb_causal_boundary", "no_general_solver_or_complexity_result"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_social_manipulation_generalization_and_formula_boundary_check"
escalation_verdict: "pass_after_ambiguity_and_social_harm_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted manipulation/generalization check; Codex PDF-formula and source reconciliation"
reviewed_at: "2026-07-29"
---

# Frankenmandering: The Confluence and Symbiosis of Opinion Dynamics and Gerrymandering

## 一句话总结

本文把周期性选区划分、区内代表影响与社会网络意见动力学耦合成 Frankenmandering 优化框架，并用两个手工构造的小例子展示整体意见可在八步后平移 \(+1\)；它没有通用求解器、复杂度结论或现实因果验证，不能据此断言真实社会可被同样持续操控。

## 形式模型

- \(n\) 个选民组成 \(V\)，每人有 \(m\) 维意见 \(c_v\in\mathbb{R}^m\)。无向 \(G_{\mathrm{geo}}\) 表示可同区的地理约束，有向 \(G_{\mathrm{soc}}\) 表示谁影响谁。
- \(L[G]:(\mathbb{R}^m)^n\rightarrow(\mathbb{R}^m)^n\) 是依赖影响图的意见更新函数；\(F(c|_D)\in D\) 从区 \(D\) 选出代表。
- 每期依次：（1）选择覆盖 \(V\)、互不相交且满足连通等约束的 \(K\) 个区；（2）每区用 \(F\) 产生代表；（3）加入代表到所有区内选民的影响边 \(H_j^t\)；（4）在原社会图与新区内边的联合图上用 \(L_t\) 更新意见。
- 给定 \(J(c_t)\ge0\)，问题在时域 \(T\) 内选择 \(D_1,\ldots,D_T\)，最小化 \(\sum_{t=0}^T J(c_t)\)（§2.1，p. 3935）。

## 两个构造性例子

### Inchworm

- \(n=10\)，初始意见为 \(\{0,0,0,1,2,3,4,5,5,5\}\)，目标是一轮后成为 \(\{1,1,1,2,3,4,5,6,6,6\}\)。
- \(G_{\mathrm{geo}}\) 是 Figure 1 的平面邻接图，\(G_{\mathrm{soc}}\) 为空。每期只建一个三人区，其余为单人区；代表是区内中位意见者。
- discrepancy response function 在距离小于 3 时把选民向代表移动一步，在距离至少 3 时产生 backfire、远离一步。
- Figure 2 手工选择八期三人区，使 \(t=8\) 的意见恰为初始向量整体 \(+1\)；相同图式可再次重复（§2.2，pp. 3935–3936）。

### 固定区与社会网络

- \(n=6\)，初始为 \(\{0,1,2,3,4,6\}\)，目标为 \(\{1,2,3,4,5,7\}\)。固定区 \(d^*=\{0,1,5\}\)，社会图是每人连接至多两个近邻的链。
- 论文印刷的分段式依次写成：距离 \(<4\) 时靠近、距离 \(<6\) 时远离、距离 \(\ge6\) 或 \(<2\) 时不变。它使 \(<2\) 同时落入第一和第三分支，且第二分支与第一分支重叠；正文只说明 \(<2\) 是 indifference、\(\ge6\) 是 irrelevance，因此公式没有唯一确定所有重叠情形的优先级。
- Figure 3 仍给出一条八步手工轨迹，使意见整体 \(+1\)，之后在所画动力学下可重复。复现者必须先澄清分段区间或执行优先级，不能静默把它改写成论文未明确给出的非重叠规则。

## 这些例子证明到哪里

- 它们构造性说明：在选定 DRF、代表规则、图和小规模意见向量下，存在能够产生持续平移的 district sequence；第二例还说明固定区可以借助社会链传播影响。
- 它们不证明任意图或意见动力学都存在解，不给出最优性、收敛性、复杂度或可扩展算法，也没有真实选民数据、仿真基准或对照实验。
- 新加坡 HDB 的配额、社区互动与社会凝聚只被用作动机和机制类比。论文自己承认该交互“从未被这样研究”，没有识别 HDB 规则对意见或福利的因果效应。

## 操控、公平与开放问题

- 周期性重新划区可把一次选举优势变成长周期意见塑造，并可能避开只检查当期 electoral outcome 的传统 gerrymandering detector；这是风险假设，不是本文在现实系统上验证的检测失败率。
- 需要评估代表性平等、少数群体保护、不同群体承受的影响强度、知情同意与可申诉性，以及限制跨期操控累积的约束。学校分区、广告和去极化等“正面”用途也不能绕过这些治理问题。
- 当前模型缺少代表之间的网络、流动人口、边权、地理/党派等非意见属性、重划区与意见更新的不同时间尺度，以及划区与直接影响的组合。
- 作者把通用解是否存在、计算复杂度、实际 solver、意见分布目标和收敛速度均留作未来工作，只提到 Markov chain、GNN、RL 与 Majority Illusion 可能提供思路（§3，p. 3937）。

## 与 AAMAS 的关系与核验说明

本文连接 computational social choice、opinion dynamics、network influence、resource partitioning 与治理安全。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QBUW2742.pdf) 核对 §2.1 的模型、Figures 1–3 的八步构造和 §3 的限制；同时直接核看第 3936 页公式，保留第二 DRF 的原文重叠歧义，未把手工例子外推成一般社会操控定理。
