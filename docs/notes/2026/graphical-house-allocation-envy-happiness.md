---
title: "Minimizing Envy and Maximizing Happiness in Graphical House Allocation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/OKCY3441"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OKCY3441.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "formal_allocation_model", "local_envy_definition", "complexity_results", "not_real_world_policy_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Minimizing Envy and Maximizing Happiness in Graphical House Allocation

## 一句话总结

本文研究带友谊图的住房分配：只有相邻 agent 会产生 envy；先最小化 envious agents 数量，再在所有最优解中最大化获批房屋的 happy agents 数。若每人恰好/至多批准一所房，两目标均可用最小费用最大匹配多项式求解；允许两所批准房时最小 envy 已 NP-hard，并给出依赖稀疏性、平衡分隔符和 vertex cover 的精确算法。

## 方法与证据

- 实例包含 agent 图 \(G=(A,E)\)、房屋集合 \(H\) 与每个 agent 的批准集合 \(P_a\)，分配 \(\phi:A\to H\) 必须 injective（§1）。agent \(a\) 只有在自己未获批准房、且某相邻者获其所批准的房时才 envy；非邻居的结果不影响该定义。
- Optimal House Allocation 最小化至少 envy 一名邻居的 agents 数；Optimally Happy House Allocation of Agent Network 在此最小值上再最大化 \(\phi(a)\in P_a\) 的 agents 数（Definitions 1–2）。因此幸福不等于偏好排序/福利，envy 也不是全局 envy-freeness、补偿、可解释性或程序公平的完整度量。
- 当所有 \(|P_a|=1\) 时，作者将可行分配与 envy 违反编码为 bipartite matching，最小费用最大匹配能在多项式时间解决两个目标（§2）。摘要声称边界紧：允许 \(|P_a|\le2\) 时，Optimal House Allocation 即使在 complete bipartite graph 也 NP-hard；在 3-regular graph、\(|A|=|H|\) 且所有 agent 偏好相同时亦 NP-hard。
- 对一般图，摘要给出 \(O(2^{|A|+2|E|}\,\mathrm{poly}(|A|+|H|))\) 的精确算法，基于猜测每个 agent 所 envy 的邻居集和非 envy agent 的 happy 状态，再归约为匹配。对有 \(f(n)\)-balanced separators 的图，得到平面图 \(2^{O(n)}\) 等界；并对 vertex cover 大小 \(k\) 给出 \((2^m)^k\mathrm{poly}(|A|+|H|)\) 算法（§2）。
- 文稿只概述结果而未展示完整算法、归约或实验；所谓“现实动机”来自宿舍、住房和云资源的类比，但没有真实偏好数据、用户研究、分配质量比较或机制实施评估。复杂度和精确运行时均应以完整论文证明为准。

## 适用边界与复现

- 适合研究局部社会比较下的稀缺物品分配、算法边界与结构参数；不应直接用于公共住房、宿舍或云资源的自动决策。实际部署还需要资格/法律约束、租金或容量、优先级、反歧视、公平申诉、隐私和可审计性，而这些不在模型内。
- 复现需明确图、房屋数、批准集合、注入式分配、envy/happy 计算、并列的 lexicographic objective；实现 matching reduction 和各结构算法，并检验摘要列出的 graph restrictions、参数和输入编码。三页扩展摘要缺少证明和完整伪代码，不能据此单独验证 NP-hardness 或运行时。
- 应测试随机、稀疏、真实社交网络和极端偏好实例，报告最优值、耗时、内存、参数敏感性及与全局 envy/福利指标的偏离。还要研究不完整/策略性偏好、分配可撤销性、解释和对受保护群体的影响；局部无 envy 不能证明整体公平或满意。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 fair division、资源分配与图算法扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OKCY3441.pdf) 核验局部 envy/happy 定义、\(|P_a|=1\) 的匹配算法、\(|P_a|\le2\) 的 hardness 和结构化精确算法概览；没有把抽象模型结论写成真实住房政策或公平保证。
