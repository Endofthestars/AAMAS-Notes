---
title: "Revisiting the Evolution of Cooperation in Complex Societies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "norms_trust_governance", "marl_coordination"]
dblp_key: ""
doi: "10.65109/OUAB7380"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OUAB7380.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_societal_model", "normative_interpretation", "aggression_claim_scope", "not_human_subject_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Revisiting the Evolution of Cooperation in Complex Societies

## 一句话总结

论文在 Junior High Game（JHG）这一策略网络模型中，以复制子动力学比较三种信息范围：更丰富的信息可稳定互惠与合作，也可能让针对弱者的策略性剥削在模型中持续存在。

## 方法与证据

- JHG 将 agents 置于具不对称权力、有限资源、相互依赖和演化互动网络的社会中；每个 agent 在合作、攻击、忽视他人及自我防御之间分配 token（§2）。
- 作者枚举策略，并用 replicator dynamics 检查小规模入侵者能否击败采用另一策略的居民；这分析的是给定模型和策略集合中的演化稳定性，而不是人类行为数据（§2）。
- 设定一（societal-response）只观察社会总体反应，always-defend 会入侵所考察的其他策略，合作崩溃。设定二（direct-interaction）保留双边历史，Cooperative、Preferential、Parasite 为演化稳定策略；文中报告 Parasite 在混合群体可稳定在约 30--40%（§3、Figure 1）。
- 设定三（indirect-interaction）允许观察他人之间的互动。作者报告社会可通过合作与规范整合取得较高生产率，但结果依赖初始条件；在某些 norms 下，有限地剥削较弱个体的策略具有优势，且 exploiters 主导的社会可能达至最高生产率（§3）。
- 结论是 Axelrod 式互惠洞见在更复杂的模拟社会中仍有作用，但信息扩展改变而非消除了攻击/剥削的出现方式（§4）。

## 适用边界与复现

- 这是 JHG、所枚举策略与复制子动力学下的模型结果；它不证明现实社会、组织、国家或平台中信息透明会造成、正当化或预测攻击行为。
- “生产率最高”是模型内指标，不能与公平、伤害、权利或可接受性互换。即便模型中 exploitation 有优势，也不能成为针对弱者采取现实干预的规范依据。
- 结论对 token 分配规则、网络演化、可见信息范围、初始策略组成、payoff 和策略库敏感；扩展摘要未提供完整代码、参数或稳健性扫描，不能据此判断跨模型可重复性。
- 复现应公开 JHG transition/payoff、各 scope 的可观测与交互权限、所有策略伪代码、replicator 方程/初始化、入侵判据、随机种子、生产率定义，以及对策略库和初始 norms 的敏感性分析。

## 与 AAMAS 的关系与核验说明

这是多智能体博弈、网络结构与规范演化的建模研究。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OUAB7380.pdf) 核对 §2--4、Table 1--2 与 Figure 1；所有关于合作、攻击和弱者剥削的表述均限定为该模拟模型中的结果。
