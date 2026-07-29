---
title: "Fair Allocation with Initial Utilities"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "norms_trust_governance", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/DMYL9092"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DMYL9092.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "comparable_initial_utilities_required", "additive_utilities_only", "normative_fairness_choice", "strategic_reporting_not_modeled"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fair Allocation with Initial Utilities

## 一句话总结

本文把不可分物品的公平分配从“相同起点下的平等对待”扩展为“考虑起点差异后的结果平等”：每个 agent 有可比较的 initial utility \(b_i\)，以 \(b_i+u_i(X_i)\) 定义 EF-init/EF1-init。此直接扩展即使 identical resources 也可能无完整 EF1-init 分配，existence 为 NP-complete；作者提出始终存在的 minimum-EF1-init，并用激活低起点 agent 的 round-robin 在多项式时间求出，但公平含义取决于 initial utility 的测量与政策价值判断。

## 方法与证据

- 模型有 \(n\ge2\) agents、\(m\) indivisible resources、nonnegative additive utilities，且每个 agent 另有已知、可跨 agent 比较的 \(b_i\ge0\)（§2）。这是强信息/可比性假设：\(b_i\) 既非 private、不可量纲混合、也不由 allocation 改变；论文不处理 complementarity、budget、entitlements、uncertain need、动态资格或策略性谎报。
- EF-init/EF1-init 用 total post-allocation utility 衡量。对每对 \(i,j\)，EF1-init 允许从 \(j\) bundle 去掉一个 resource 后仍有 \(b_i+u_i(X_i)\ge b_j+u_i(X_j\setminus\{r\})\)；EF-init 不允许删物（§2）。这是 equality-of-outcome 的形式化，但 \(i\) 用自己的 \(u_i\) 评价 \(j\) 的 bundle，且空 bundle 被特殊处理；它并不保证最大 welfare、need proportionality、程序公平或现实权利合规。
- 与 classical setting 不同，complete EF1-init allocation 可能不存在（包括 identical resources），因为 agents 对抵消 initial disparity 所需物品的价值可以不同；判断其存在性 NP-complete（§2）。constant agents 且 utility unary encoding 时，可用 dynamic programming 判定 complete EF-init/EF1-init existence；identical resources 下 EF-init existence 可多项式判定。extended abstract 未给 reductions/DP states/时间界或实现。
- minimum-EF1-init（min-EF1-init）在 \(b_i\le b_j\) 时沿用含 \(b\) 的 EF1 形式；在 \(b_i>b_j\) 时，先以 \(j\) bundle 中某个 subset \(X^*\) 抵消 initial gap，再从剩余 bundle 移除一个 item 作 \(i\) 的 EF1 比较，并用所有 lower-initial-utility agents 对 \(X^*\) 的 minimum utility 限制其价值（Definition 2.1）。它刻意避免只按 \(i\) 的 value 计算补偿；但定义复杂且可能与人类对“补偿/权利”的直觉、优先级或历史不一致。
- 若 resources 对 initial utility 有 diminishing usefulness（\(b_i<b_j\Rightarrow u_i(r)\ge u_j(r)\)），min-EF1-init 与 EF1-init 重合。一般情形作者给 extended round-robin：先激活最低 \(b\) 的 agents，当前 active agents 达到下一 agent 的 initial utility 时激活该 agent，并把 newcomer 插入本轮已选 agents 之后（§2）；作者声称该算法多项式并总产生 complete min-EF1-init。未报告实例实验、真实 initial-utility estimation、用户接受度或 manipulability。

## 适用边界与复现

- 适用于公共支持、教育补救或医疗资源等确实明确追求缩小可审计初始差距的离线不可分资源分配；不应用于将预测分数、敏感身份或不可比较福利指标机械相加后自动决定救助、录取、治疗或惩罚。
- 复现需公开 agent/item set、additive value matrix、\(b_i\) 来源/刻度/比较依据、complete-allocation rule、zero-value edge cases、EF-init/EF1-init/min-EF1-init verifier，及 active-set/picking-order/同轮 insertion 的 exact tie-breaking。以小实例 brute-force 验证 nonexistence/NP case与算法输出；对固定 agent/unary utility DP 和 identical-resource EF-init decision，需要 full version arXiv:2602.14850 的完整算法和 proof。
- 应测试 noisy/uncertain \(b_i\)、scale transformations、disagreement over needs、misreported valuations/initial positions、correlated/sensitive attributes、indivisibility severity、heterogeneous item benefit、alternative fairness/welfare objectives、appeal/override及多轮 allocation。报告谁因估计误差被优先/不利，而不只报告形式化 criterion 满足。
- 高影响分配应由合法的资格/反歧视约束和独立审计先限定 \(b_i\) 的使用，保存数据来源与版本，提供解释、申诉、人工复核和结果监测。min-EF1-init 是一个数学 compromise，不是对“何种不平等应被补偿”或“多少补偿正当”的规范性裁决。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的算法公平分配与计算社会选择 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DMYL9092.pdf) 核验 initial-utility/additive 模型、EF1-init nonexistence/NP-complete、受限 positive results、Definition 2.1、diminishing-usefulness coincidence 及扩展 round-robin；没有将数学 fairness criterion 写成实际福利测量、合法性或公平结果的保证。
