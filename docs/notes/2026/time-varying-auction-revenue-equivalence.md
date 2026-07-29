---
title: "Time-Varyingness in Auction Breaks Revenue Equivalence"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "marl_coordination"]
dblp_key: ""
doi: "10.65109/BNYN3177"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BNYN3177.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02f"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["auction_theory_assumptions", "learning_dynamics_scope", "bidder_payoff_not_seller_revenue", "no_empirical_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Time-Varyingness in Auction Breaks Revenue Equivalence

## 一句话总结

论文在随时间变化的、对称独立私有价值拍卖中建模第一价格竞拍者追踪移动均衡的学习滞后；与不依赖分布参数的第二价格 truthful bidding 相比，价值下界（basis value）与区间宽度的相关性可使两种机制的长期竞拍者收益不同。

## 方法与证据

- 经典部分假设 n 位 bidders 的 values 来自共同的连续、对称、独立、私有分布。第一价格均衡出价依赖分布参数，第二价格 truthful bid 为 `b(v)=v`，由此在参数随时间变化时两者的追踪能力不同（§2）。
- 作者令真实参数 `θ*(t)` 时变，bidders 通过连续时间的梯度学习动态估计 `θ(t)`，并以时间平均的期望 payoff 比较 first- 与 second-price auction；这不是静态 Bayes-Nash equilibrium 的 revenue-equivalence 命题（§2）。
- 对 uniform distributions，basis value 为下界 `v_m(t)`，value interval 为 `Δv(t)=v_M(t)-v_m(t)`。Theorem 1 在 K 个状态且两者正相关时给出长期 bidder payoff `w̄_1st(∞) > w̄_2nd(∞)`；反相关时完整版本的 Theorem 2 给出相反不等式（§3）。
- 摘要称 log-normal 实验亦观察到相似相关性现象，但没有提供实验配置、数值或现实竞价数据；作者在 §4 将经验验证、异质学习、非对称和相互依赖 values 列为未来工作。

## 适用边界与复现

- 论文实际比较的是建模下的 bidder long-run payoff，而非直接证明 seller revenue、平台收入或所有拍卖目标的优劣；标题中的 revenue equivalence 应按这一非均衡分析语境理解。
- 结论依赖连续时间学习、同质参数估计、SIPV 分布、所给相关性与无限时间平均。真实广告市场的预算、保留价、参与/退出、策略性学习、异质 bidders、平台规则和反馈延迟会改变结果。
- 正/负相关是理论条件，不能仅从时间序列表面共变就推断某种机制会提高任一方收益，也不构成选择/切换拍卖机制的商业建议。
- 复现需披露 K-state 参数过程、分布与相关性、bidder 数、初值、学习动力学/步长、有限 T 收敛诊断、payoff 计算及 log-normal 实验；经验外推还应做因果识别和机制变更的风险评估。

## 与 AAMAS 的关系与核验说明

这是学习动态下的机制设计与博弈论分析。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BNYN3177.pdf) 核对 §2--4、Theorem 1 及其关于 Theorem 2 的说明，明确区分理论 bidder payoff 与现实平台收入。
