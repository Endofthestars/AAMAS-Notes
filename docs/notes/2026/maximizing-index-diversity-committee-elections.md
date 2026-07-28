---
title: "Maximizing Index Diversity in Committee Elections"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/LLTB9191"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LLTB9191.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["label_quality_dependency", "index_choice_value_judgment", "approval_preference_assumption", "constraint_feasibility_dependency", "computational_hardness", "pabulib_limited_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Maximizing Index Diversity in Committee Elections

## 一句话总结

本文在带标签候选人与 approval preferences 的多赢家选举中，以生态多样性指数最大化委员会的标签多样性，同时保留总分下限或每位选民满意度下限；并提出 Lexicographic Counting (LC) 指数。它给出指数性质与复杂度分类、在 Pabulib 转换实例上展示分数/满意度放宽的权衡；但标签、指数及阈值本身包含规范性选择，标签多样性不等于群体代表性、程序公平或现实结果公平。

## 方法与证据

- 两类模型分别是：在 scoring-rule score 至少为 \(\beta\) 时最大化 index diversity（DSCR），或在每位 agent satisfaction 至少满足 \(h(a)\) 时最大化 diversity（DSAT）（§2, §4）。它们处理的是固定大小、有效 committee 内的优化，先要明确候选标签、approval ballot、评分函数与可行阈值。
- 作者适配 Richness、Simpson、Shannon 等生态指数，并提出 LC：以标签计数的字典序比较委员会；性质包括 Present Label Maximization、Occurrence Balancing、罕见标签优先平衡与 \(n\)-Explainability（§3）。Theorem 1 称 LC 为 1-explainable，Theorem 2 在 1-explainability 与 present-label maximization 下刻画 LC；“可解释”仅指用计数向量比较多样性的形式性质，并不衡量选民理解、价值认同或操纵风险。
- 没有 score/satisfaction 限制时，所有所讨论指数的最大多样性委员会可多项式求解（Observation 5）。但满足每位 voter 最低满意度的 D-DSAT 为 NP-hard；加入 score 下限的 DSCR 则取决于 scoring rule：例如 Approval Voting 下各所考察指数可在多项式时间求解，而 Chamberlin–Courant 等 winner determination 本身困难时会继承 NP-hardness（§4）。因此不能只由“指数可算”推断实际选举优化可扩展。
- 所有优化结果还需要可行阈值。若偏好记录稀疏、标签交叉/缺失、候选质量或票数不可靠，优化器仍会严格地最大化被编码的代理，而非未编码的代表性或利益。
- 实验取 Pabulib participatory-budgeting 数据，将项目 categories/targets（如 urban greenery、adults）作为候选标签，聚合为 plain multiwinner 实例；移除本就达到满多样性的实例，并主要测试 \(k=10\)，长文另报 \(k=6,8\)（§5.2）。这不是实际带预算的 participatory budgeting 决策，也不验证公众接受度、策略行为或分配效果。
- 对 scoreAV/scoreSAV 与 satisfaction 放宽，作者用 abcvoting 及指定规则构造比较；文本报告放宽分数或每人满意度可提高可达多样性，且不同指数/规则变化明显（§5.2, Fig. 2）。例如无约束最优多样性约为 AV/SAV 方案的 70% 以上基线，具体结论依赖指数、规则与实例，不能解释为固定百分比的普适收益。

## 适用边界与复现

- 可用于需要在明确定义的标签维度上平衡候选广度，并能接受分数或个体满意度门槛的委员会/目录/项目选择研究。应先与受影响群体共同定义标签、交叉身份、缺失/多标签处理和指数，而非把生态计数指标当作唯一的多样性规范。
- 实际任命、资助或公共预算前，还需独立审查资格、反歧视、历史不平等、少数群体实质代表、利益冲突、隐私和申诉机制；指数优化不保证个体待遇、比例代表、结果平等或法律合规。
- 复现需固定 Pabulib 快照、实例筛选与 label mapping、committee size、approval conversion、score/satisfaction 基线和放宽规则、指数实现/数值精度、abcvoting 版本、求解器/超时与随机 tie-breaking；报告 infeasible cases、完整分布、每位选民 satisfaction 和标签计数，而非只报平均 diversity ratio。
- 应扩展到多标签/交叉群体、标签错误或策略性标注、不同 ballot/score 模型、真实参与者审阅、规模压力测试与基于受影响群体的公平指标；比较硬 quota、比例代表与指数模型的风险和可解释性。

## 与 AAMAS 的关系与核验说明

这是计算社会选择中将生态多样性指数用于多赢家委员会优化的工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LLTB9191.pdf) 核对两种约束模型、LC 与性质、复杂度结论、Pabulib 标签转换、实验设置与适用边界；没有把标签指数、可解释性定义或特定实例中的分数/满意度放宽收益误写成代表性、公平、民主正当性或普遍可解性保证。
