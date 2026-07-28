---
title: "Modifying Preferences and Capacities for Stability in Flow Networks: Algorithms and Complexity"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "safety_verification"]
dblp_key: ""
doi: "10.65109/NNOC3454"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NNOC3454.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["centralized_preference_modification", "capacity_change_side_effects", "financial_and_transportation_scope", "utility_model_assumption", "stability_not_fairness_or_legality"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Modifying Preferences and Capacities for Stability in Flow Networks: Algorithms and Complexity

## 一句话总结

本文研究 inverse stable flow：给定一个可行流，中央机构最小幅度地改写节点对弧的效用偏好，或同时调整弧容量，使该流不再有 blocking walk；效用值的 (L_1) 修改下给出多项式算法，而把偏好改动度量为严格排序的相邻交换后，两个模型的最优化问题均为 NP-hard。它是对形式化网络稳定性的优化结果，不是对金融清算、交通调度或参与者权益的部署授权。

## 方法与证据

- stable flow 将 agent 表示为有偏好的 network vertices、合同/路线/债务表示为有容量的 directed arcs。若存在全未饱和的 directed walk，其首尾 agent 都偏好改走该路，则该 walk 阻塞流；没有 blocking walk 才称稳定（§2.1）。
- 模型一只允许修改由 utility functions 诱导的 weak preferences，以总 (L_1) 变化最小为目标。论文把“令一组入/出弧被当前流支配”的最小代价写成单点 LP，证明所得集合代价是可多项式计算的单调 submodular 函数，再通过带边标签二分图的 bipartite-submodular optimization 求最优（Algorithm 1、Theorem 3.3）。
- 若偏好为 strict ordinal lists、代价改为 adjacent swap 数，论文先以 2-SAT 在多项式时间判定是否存在可行修改（Theorem 3.5），但以 Vertex Cover 归约证明最小 swap 的 `Inv-StabFlow-PrefMod-Swap` 为 NP-hard（Theorem 3.6）。
- 模型二同时允许改 capacity 与 preference：只能在 (x(e)>0) 的弧上提高 utility，容量差与效用改动均计入 (L_1) 目标。作者将选择化为 auxiliary network 的 minimum (S\)--\(T) cut，并证明 Algorithm 2 给出最优解且为多项式时间（§4、Theorem 4.1）。把这里的 preference cost 改为 swap distance 仍 NP-hard（Remark 1）。
- 基本可行性并非无条件：若存在未饱和 (s\)--\(t) path，任何 preference lists 下都不稳定；在给定上下界相容时，无未饱和 (s\)--\(t) path 是仅改 utility 能稳定化的充要条件（Observation 1、Proposition 3.1）。作者明确留下“放松模型二仅提高正流弧 utility”后是否仍多项式可解的开放问题（§5）。

## 安全边界与复现

- “中央机构可改变偏好”在文中是 compensation/incentive 的建模假设，不应理解为可以操纵个人、企业或银行的真实意愿。任何激励、债务减免、通行费或容量变更都可能有分配、合同、监管、预算与外部性后果，需独立取得授权和审查。
- 模型使用固定给定流、容量、可量化效用/严格排序及局部 blocking-walk stability。没有表示信息不对称、策略性误报、资金/物理可行性以外的约束、动态需求、风险传播、群体公平或法律优先级；稳定不推出社会福利、公平、偿付能力或合规。
- 模型二的算法依赖关键限制：只提高正流弧的 utility；论文没有证明移除该限制仍可高效求解。严格排序下优化的 NP-hardness 也意味着大规模实际方案需说明 exact/heuristic status 与最优性 gap。
- 复现应发布原网络、flow、capacity、偏好 utility/上下界、blocking-walk 判定、子模函数/LP、auxiliary cut 构造、数值精度和 solver；同时报告修改项、补偿预算、容量缩减造成的服务影响、受影响主体与 counterfactual fairness/robustness 分析。

## 与 AAMAS 的关系与核验说明

这是稳定流、逆优化与组合优化工作，面向金融清算和运输网络等潜在场景。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NNOC3454.pdf) 核对两种修改模型、Algorithm 1/2、Theorem 3.3/3.5/3.6/4.1 与开放问题；没有将理论稳定化解释为实际系统的安全、公平或监管结论。
