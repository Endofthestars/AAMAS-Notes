---
title: "Interbank Lending Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "applications"]
dblp_key: ""
doi: "10.65109/HTED8429"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HTED8429.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["stylized_financial_market_model", "no_credit_default_risk", "linear_interest_response_assumption", "complete_information_assumption", "equilibrium_not_financial_forecast", "no_regulatory_policy_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Interbank Lending Games

## 一句话总结

本文将每个 lender 在多个 borrower 间连续分配现金的选择建模为精确 potential game：借款方利率在中央银行利率走廊内随总供给/需求线性变化，lender 最大化利息收入。该特定模型的 potential 严格凹，故有唯一 pure Nash equilibrium；作者给出 \(O(mn+m\log m)\) 的 strongly-polynomial 算法，并证明若干 best-response/pseudo-gradient 动态收敛。结论依赖简化的利率、信息与违约设定，不能当作真实银行间利率预测、流动性压力测试或利率走廊政策推荐。

## 方法与证据

- 游戏 \(G=(m,n,\mathbf c,\mathbf d,r_{max},r_{min})\) 有 \(m\) 个 lenders 和 \(n\) 个 borrowers；lender \(i\) 选择非负向量 \(s_{ij}\)，总额不超过 cash budget \(c_i\)，borrower \(j\) 有 demand \(d_j\)（§2.1）。策略空间是紧的连续凸集；agents 是 lenders，borrowers 不策略性报价或选择交易对象。
- borrower interest rate 由利率走廊与对该 borrower 的聚合供给/需求的线性函数决定（Eq. 2）；lender utility 是所获借款利息（与把未贷出资金按 \(r_{min}\) 存入央行的等价写法）（§2.1）。过度供给会使报价低于 \(r_{min}\)，因而不在 NE；该设计排除了信用质量、违约、抵押品、期限、交易成本、双边谈判、市场分割和利率冲击。
- 作者构造 exact potential \(\Phi\)（Theorem 2.1），然后以紧性保证 maximizer 存在（Lemma 3.1）并证明 \(\Phi\) 在策略空间严格凹（Lemma 3.2），得到唯一 pure NE（Theorem 3.3）。唯一性是该连续静态函数的性质，并不表示实际市场有单一稳定利率或观测到的结果会收敛。
- 将 equilibrium 写成最大化严格凹 potential 的约束优化问题，并用 KKT 条件给出显式结构；所有 borrowers 在 NE 有相同 interest rate（Theorem 3.5）。这来自对称的全市场供给—需求规则，而不是跨银行、期限或信用等级的一般无套利定律。
- Algorithm 1 先按 lender budget 排序并迭代识别低预算集合，再按闭式 allocation 构造 \(\mathbf s^*\)；作者证明其输出唯一 NE，时间 \(O(mn+m\log m)\)，即 strongly polynomial（Theorem 3.6）。该复杂度计数不包括获取真实需求/余额/信用信息、通信、执行与合规成本。
- 对异步离散更新，eager \(\alpha\)-uniform best response 从任意初始状态收敛（Theorem 4.1），randomised 版本几乎必然收敛（Theorem 4.4）。同步更新使用 projected pseudo-gradient，文中证明相应 discretised dynamics 也收敛（Theorem 4.6, Prop. 4.7）；连续时间 best-response 用 Lyapunov 函数收敛（Theorem 4.8）。这些是精确 best response、可行投影与固定模型参数下的数学动态，不保证异步结算、噪声报价、延迟或战略信息操纵的收敛。
- 论文说明结论在严格凹 potential 结构下成立，并只讨论“lending amount/interest rate equilibrium”（§1, §5）。没有用真实 interbank trade 数据校准、回测危机时期、度量系统性风险/社会福利，也没有评估中央银行政策的因果效果。

## 适用边界与复现

- 适用于分析受控教学/研究市场中，有限 liquidity budgets 与线性利率反馈如何给出唯一 resource-allocation equilibrium。若要接近实际金融网络，需先加入债务到期、信用限额、风险权重、抵押品、结算优先级、网络曝光、监管资本、违约与宏观冲击。
- 不应用此模型直接设置利率走廊、授信额度、流动性处置或风险资本。金融应用须由持牌机构、风控与监管人员审查，并进行真实数据校准、情景/压力测试、模型风险治理、对抗性与极端市场测试、审计以及人工升级路径。
- 复现应固定 \(m,n,\mathbf c,\mathbf d,r_{min},r_{max}\)、Eq. 2 利率函数、utility/potential、排序 tie rule 与 \(\alpha\)/更新选择；数值验证 KKT、统一 equilibrium rate、Algorithm 1 的 \(O(mn+m\log m)\) 构造和四类动态从多初始点收敛。报告余量、供给/需求、potential gap、迭代数和精度。
- 应测非线性/分层利率、异质 lender 风险、borrower strategic demand、部分可观测、随机故障、双边网络、离散结算和 default contagion；并比较 equilibrium 与监管目标、消费者/银行分配影响及 systemic-risk 指标。

## 与 AAMAS 的关系与核验说明

这是以 potential game 分析连续资源分配的 AAMAS 金融市场模型工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HTED8429.pdf) 核对游戏、利率走廊/供需函数、exact potential、严格凹唯一 NE、统一均衡利率、Algorithm 1 的复杂度和各动态收敛定理；没有将这些抽象模型结论写成真实银行数据证据、危机预测、无违约保证或政策有效性结论。
