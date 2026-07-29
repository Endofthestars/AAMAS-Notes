---
title: "Towards Fairness in Collective Decision Making: Constraints and Approximations"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/OEOU3703"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OEOU3703.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04t"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_algorithm_strand_revision"
spark_consistency: "pass_after_pdf_layout_and_terra_attribution_revision"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "fairness_axioms", "approximation_guarantees", "two_column_attribution_risk", "results_from_cited_projects", "no_proof_or_experiment_in_overview"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_approximation_scope_and_algorithm_attribution_check"
escalation_verdict: "pass_after_model_scope_and_eca_attribution_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted approximation-boundary check; Codex PDF-layout and source reconciliation"
reviewed_at: "2026-07-29"
---

# Towards Fairness in Collective Decision Making: Constraints and Approximations

## 一句话总结

这篇博士生论坛短文把作者关于公平集体决策的研究组织成三条线：学习增强的 envy-ratio 设施选址、maximum-group-effect 群体公平，以及公交站点中的 JR/core 比例公平；文中技术保证均是对作者已发表或工作论文的概述，本稿没有重给算法、证明或实验。

## 研究问题

集体决策需要在异构偏好和现实约束下同时考虑公平、效率、激励兼容与可计算性。作者以比例代表、无嫉妒和防止系统性不利等公理为入口，追问公平结果是否存在、能否多项式时间计算，以及精确公平不可得时可达到怎样的近似保证（§1，p. 3954）。

## 设施选址中的个体公平

- 文献 [6] 研究直线度量、envy-ratio 目标下的学习增强机制。确定性机制接收预测的最优设施位置，并在预测准确时保持 consistency、预测任意错误时保持 robustness；该项目报告了紧的近似保证。
- 同一项目还给出一个不使用预测的随机机制，其 envy-ratio 近似比严格优于 2，并进一步构造学习增强随机机制。
- “紧界”和“突破 2”都只属于 [6] 的具体模型：前者不能扩展为所有随机机制或所有公平目标，后者也不是确定性机制的一般结论。当前三页稿没有列出完整比值、定理条件或证明（§2，pp. 3954–3955）。

## 设施选址中的群体公平

- 文献 [16] 允许代理属于一个或多个群体，以 group-specific weights 聚合到最近设施的总距离或最大距离，定义 **maximum group effect**。
- 该形式覆盖 social cost、maximum cost、maximum total group cost 和 maximum average group cost。作者报告统一机制对一般目标达到紧近似保证。
- 其中 **Balanced Mechanism** 被报告为闭合 maximum total group cost 与 maximum average group cost 两项目标的近似缺口；这不等于闭合了所有 group-effect 目标。
- 随机机制能达到的最优群体公平近似仍被列为开放问题（§2，p. 3955）。

## 公交站点中的比例公平

文献 [8] 把直线上的公交站点问题扩展到一般度量，并与 proportional fair clustering 建立结构对应：

- **JR（Justified Representation）**：在站点语境中，任何规模足以获得一对站点的联盟，都不应能相对于算法结果通过这对站点获得有利偏离。
- **Core**：不存在规模与人口份额相称的联盟，能够改选另一组站点并让所有成员的通勤成本严格下降。
- 精确 core 在这一一般度量模型中未必存在，因此后续讨论的是放松后的 core 近似，并不矛盾。
- 从比例公平聚类文献 [12] 适配的 **Greedy Capture** 同时获得 JR 和 core 的常数因子近似，但本稿没有给出常数。
- **Expanding Cost Algorithm（ECA）** 对 JR 给出严格优于 Greedy Capture 的保证；论文没有声称它也全面改善 core。
- \(\lambda\in[0,1]\) 的混合算法在 Greedy Capture 与 ECA 的候选站点选择逻辑间插值，形成 JR 与 core 近似保证的参数化权衡，而不是一个同时严格支配二者的算法（§3，p. 3955）。

ECA、Greedy Capture 和 \(\lambda\) 混合算法均属于公交站点工作 [8]；PDF 双栏版面容易使抽取文本把它们与左栏的 envy-ratio 段落错误拼接。

## 开放问题与应用

- 缩小 JR 近似差距，完整刻画按联盟规模和个体成本双重放松的 core 近似，并在比例公平约束下同时优化总成本。
- 研究 veto proportionality 的形式定义、可计算性以及与标准比例公理的关系，并为委员会选择设计跨环境的随机近似算法。
- 将比例表示扩展到多个 LLM 输出的聚合、sortition 和联邦学习参与者选择；这些是研究设想，不是本文已经验证的应用（§3，p. 3955）。

## 证据与归属边界

- [6] 是作者参与的 NeurIPS 2025 forthcoming 工作，[16] 是 AAAI 2026 forthcoming 工作，[8] 是 2026 technical report；本稿对其结果做路线化总结。
- 本文没有定理编号、证明、机制伪代码、实验、数据、图表、代码或部署。近似与不存在性结论必须回到对应原论文核验，不能把这篇 overview 当作独立技术证明。
- 当前稿自身的可见贡献是把公平目标、约束、近似结果与后续问题组织为博士研究议程（pp. 3954–3956）。

## 与 AAMAS 的关系与核验说明

该议程连接 computational social choice、algorithmic mechanism design、facility location、committee selection 和公共资源配置。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OEOU3703.pdf) 核对 §2 的两类设施选址结果及第 3955 页双栏中的公交站算法归属；未把引用项目的保证写成本三页稿新证明。
