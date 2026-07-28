---
title: "Maximin Shares with Lower Quotas"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XLQT3124.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["additive_valuation_scope", "quota_feasibility_requirement", "goods_chores_ratio_direction", "algorithm_specific_tightness"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Maximin Shares with Lower Quotas

## 一句话总结

论文研究带每类物品数量下/上限的不可分物品公平分配：在异质 additive valuations 且配额整体可行时，给出多项式时间的近似 MMS 分配；单一类别的 goods/chores 保证分别为 $2n/(3n-1)$ 与 $(3n-1)/(2n)$，多类别的保证为 $n/(2n-1)$ 与 $(2n-1)/n$。

## 方法与证据

- 实例含 $n$ agents、不可分 items、加性 valuation，以及 item partition 的 categories；每个 agent 在每 category 必须获得介于 $q_C^-$ 与 $q_C^+$ 件。基础可行性要求 $q_C^-n\le |C|\le q_C^+n$，否则连配额可行 allocation 都未定义（§2）。
- MMS 以 agent 在所有 feasible $n$-bundle partitions 中最大化最差 bundle value 定义；allocation 必须每位 agent 获得其自身 MMS 的给定比例。goods 是所有 agent 对每件 item 非负，chores 为非正；两种情形的比例方向不同，不能把 chores 的 $(3n-1)/(2n)$ 当作“较大即更好”的 goods 近似率（Definitions 1、§3）。
- Theorem 1：single-category goods 有多项式 $2n/(3n-1)$-MMS allocation，运行时间 $O(n|M|\log |M|)$。Theorem 2：single-category chores 有 $(3n-1)/(2n)$-MMS allocation，时间相同。这些推广带下限/上限的 cardinality setting，并非任意非加性偏好（§3–4）。
- 对 multiple categories，Theorem 3 给 goods 的 $n/(2n-1)$-MMS，Theorem 4 给 chores 的 $(2n-1)/n$-MMS；论文通过 ordered-instance reduction 和既有只含 upper quotas 的方法处理该泛化，因此多类保证弱于单类（§3–4）。
- 单类 goods 主算法 ApproxGoods 维护多个 bags，使剩余 items 同时满足 value 与 cardinality 不变量；以 move/swap 调整 bag 后分配给 agent。lower quota 使经典 bag-filling 的“移除低值 item”论证失效，正是该算法需要额外设计的原因（§4.1–4.3）。
- Theorem 5 只说明 ApproxGoods 这一个算法在一族 single-category、identical-valuation、$3n$ goods 实例上，不能获得超过 $2n/(3n-1)$ 的保证；它不是该问题所有可能算法的不可突破下界。论文也列出 unconstrained setting 有更强的已知界，并将改进约束情形留作未来工作（§4.4–5）。

## 局限与复现

- 结论依赖所有 valuations 均为 additive 且每件一致地是 good 或 chore；mixed manna、complements/substitutes、预算/ matroid 约束、策略性申报、在线到达和随机 allocation 不在定理范围内。
- 这是 individual share guarantee，不自动得到 envy-freeness、Pareto efficiency、maximum Nash welfare 或跨 category 语义公平；满足每类“件数”下限也不说明技能、价值、时间或多样性约束被满足。
- 近似与基数配额强依赖 $q_C^-n\le|C|\le q_C^+n$，且 multi-category 比率更弱。若任务需要每 agent 不同 quota、跨类耦合、负责人资格或 item compatibility，须重新建模和证明。
- Theorem 5 的 tightness仅对 ApproxGoods；不得据此说 lower-quota MMS 的最佳可达比例已被完全刻画。精确 MMS allocation 在更简单 setting 也可不存在/计算困难，这解释近似目标但不构成实际部署的算法性能保证。
- 复现应固定 agent-specific item values、categories/quotas，并先验证全局可行性；实现 ordered reduction、preprocessing 与 bags 的 move/swap 不变量，逐 agent 以独立 feasible MMS partition 检查获得比例；goods 与 chores 需分开处理符号和比较方向。

## 与 AAMAS 的关系与核验说明

该文扩展了多 agent 不可分资源分配中的 MMS 公平性到下限配额。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XLQT3124.pdf) 核对模型、Theorems 1–5、比例方向、复杂度与算法特定 tightness；不将近似 MMS 外推为一般公平、效率或现实配额制度的完整解决方案。
