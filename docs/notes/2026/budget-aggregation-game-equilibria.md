---
title: "Efficiently Computing Equilibria in Budget-Aggregation Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "planning_scheduling", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/CCMB1463"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CCMB1463.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "low"
risk_tags: ["utility_model_scope", "weighted_case_pseudopolynomial", "equilibrium_selection_open", "no_empirical_deployment_claim"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Efficiently Computing Equilibria in Budget-Aggregation Games

## 一句话总结

本文将参与式预算分配表述为每位参与者掌握一份虚拟预算、只关心总预算分布的 normal-form game；对若干特定偏好类给出精确 Nash equilibrium（NE）的多项式算法，尤其解决 Leontief utility 的一个开放计算问题，但结论并不覆盖任意效用函数或一般加权输入。

## 方法与证据

- 模型中每个 agent 将自己的预算份额分到公共项目，所有个人分布之和构成总体 allocation；NE 表示在其他人遵循建议时，任何 agent 都不愿重分自己的份额（§3）。
- 任一 NE 都满足 individual fair share：每位 agent 至少获得其在最不利他人配置下可保证的效用（Proposition 3.4）；这是一项效用保障，不等同于 Pareto optimality 或其他公平公理。
- 对 linear utilities，NE 就是每位 agent 只给其最高估值项目分配预算；可用线性规划构造与检查带额外目标的 equilibrium distribution（§4）。
- 对 Leontief utilities，作者用 ellipsoid-method variant 与 strong separation oracle 证明可按输入二进制长度多项式时间求精确 NE（Theorem 5.3）；对 binary symmetric separable 及 ℓ1 preferences 也分别给出多项式求解方法（§5--7）。
- 当 agent 权重不同但为有理数时，论文通过 cloning 还原为无权 game；linear、Leontief 与 ℓ1 等情形的保证是关于权重最小公分母的伪多项式时间，而非通常意义上的 polynomial time（§8）。

## 适用边界与复现

- 算法保证依赖指定的 utility representation；论文未证明任意非线性、非对称或任意连续偏好下可高效求精确 NE，不能据此替代一般博弈求解。
- 参与式预算的语境是推荐一个无需事后后悔的个人分配，不自动解决项目可行性、战略性偏好申报、群体代表性、隐私或制度合法性。
- 加权版本的 cloning 会随权重分母膨胀；实践部署应报告权重编码、实例规模、运行时、数值精度与选择哪个 equilibrium 的准则。
- 复现需要固定 agent/project 数、预算归一化、效用模型及参数；对 Leontief 实现 separation oracle/LP/ellipsoid 所需精度，对 ℓ1 实现其显式构造，并另验 individual-fair-share 与无 profitable deviation。

## 与 AAMAS 的关系与核验说明

这是多智能体机制设计与均衡计算工作，面向 participatory budgeting 的分布式建模。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CCMB1463.pdf) 核对模型、Proposition 3.4、Theorem 5.3、§6--8 的效用类别与复杂度边界；没有把特定偏好类的结果泛化为所有博弈。
