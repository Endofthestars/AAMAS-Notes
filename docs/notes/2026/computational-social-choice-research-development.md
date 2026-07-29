---
title: "Computational Social Choice: Research & Development"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/CHQP3419"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CHQP3419.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-04s"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass"
spark_consistency: "pass_after_source_reconciliation"
risk_level: "medium"
risk_tags: ["blue_sky_agenda", "engineering_and_deployment", "stakeholder_engagement", "cited_success_stories", "no_new_system_or_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: "not_required"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Computational Social Choice: Research & Development

## 一句话总结

本文提出 COMSOC-R&D 研究议程：从一个具体的现实集体决策问题出发，把社会选择理论推进到设计、实现、测试和应用，并建议用八个工程与实践维度评价这类工作；它是方法论倡议，不是新算法、实验系统或部署报告。

## 什么是 COMSOC-R&D

- 目标是为具体真实问题应用既有社会选择技术，并在需要时开发新方法。
- 重心是把理论转化为实践：实现算法或协议、提供可访问的界面、开展实证评估，并在可能时进入真实部署。
- 判别特征是 **problem-driven**：项目从现实问题或合作方需求出发，沿设计—实现—测试—应用的完整周期推进；作者称其为 project-based，而非先做通用产品再寻找用途。
- 仅运行计算实验、发布通用库或为抽象模型增加结果，并不自动构成 COMSOC-R&D。作者也把偏好匹配领域视为可借鉴的角色模型，而不纳入本文对 COMSOC 的窄定义（§1.1，pp. 3940–3941）。

## 为什么需要这项议程

- 现实决策者常用临时或常识性规则，却未必知道已有的科学方法。论文以参与式预算中的贪心分配和 NSF 望远镜时间分配机制为例，说明公平、效率或可操纵性问题可能被忽视；这些是引用案例，不是本文的新评测。
- 真实应用会暴露抽象模型未覆盖的约束、目标和操作成本，由此反哺理论问题和评价指标。
- 可运行系统、数据、设计经验和失败教训能够形成社区公共资产，也扩大 computational social choice 的社会影响（§1.2，p. 3941）。

## 三个既有成功案例

1. **Method of Equal Shares（MES）**：参与式预算规则从理论研究走向城市采用，并配套产生供实验和公布结果使用的工具。
2. **Panelot 与 sortition**：公平抽签方法和软件已被用于组织真实的公民大会。
3. **Polkadot 的 nominated proof-of-stake**：定制多赢家投票需要同时处理代表性、可扩展性和可验证性等约束，并推动相关算法研究。

三者以及 peer review、排课、卫星资源和食物分配等例子均来自既有工作；本文用它们说明理论—实现—反馈链条已经可能发生，并未把这些部署作为自己的产出（§1.3，pp. 3941–3942）。

## 主要路障

- **Partnering**：研究者与利益相关方缺少长期连接，术语、时间线和成功标准也不一致。
- **Incentives**：偏理论和方法新颖性的评价体系容易低估适配、工程、负结果与过程经验。
- **Operations**：概念原型到可持续工具之间还隔着 UI、安全、规模化、集成、维护和研究结束后的运营。
- **COMSOC 特有困难**：高风险决策没有完美解，最佳实践不足，理论与工程文化存在间隙，既有流程带来 status quo bias，合作方也可能不信任“不了解现场”的理论研究者。

作者建议从本地、小规模试点和长期参与开始，建设合作网络与专门发表空间，并考虑类似 PACE 的应用挑战；这些是行动建议，不是经对照实验验证的解决方案（§2，pp. 3942–3943）。

## 八个建议审稿维度

1. **Modeling and Motivation**：评价模型对应用的忠实度，而不只看形式是否优雅。
2. **Literature**：说明既有 COMSOC 方法在哪里有用、在哪里失效。
3. **Empirical Assessment**：在现实设置中与基线及 status quo 比较。
4. **Data**：重视来自新应用的偏好数据及其领域差异。
5. **Transparency**：披露关键设计步骤、讨论、取舍和迭代经验。
6. **Reproducibility**：承认物理或合同限制，同时尽可能提供界面和可复用工件。
7. **Stakeholder Engagement**：记录需求获取、设计决策和反馈吸收过程。
8. **Implementation and Deployment**：把 UI、流程集成、计算优化和部署经验视为独立贡献。

作者并不要求每篇论文同时满足全部八项，而是要求审稿人按工程与实践工作的实际价值评价，不能用理论论文的单一模板衡量（§3，pp. 3943–3944）。

## 证据、局限与未来愿景

- 本文没有新算法、定理、代码、数据集、实验结果或自身部署；证据由既有案例、社区经验与规范性论证组成。
- 议程尚未给出统一实施协议，也没有量化不同合作、激励和运维方案的效果；高风险决策中的规范冲突仍需逐项目处理。
- 作者希望 COMSOC-R&D 在 AAMAS 等场所与理论工作获得同等位置，并点名偏好感知排课、不确定条件下的对象动态重分配和公平公共交通等方向（§4，p. 3944）。

## 与 AAMAS 的关系与核验说明

这项议程连接 computational social choice、机制设计、资源分配、参与式治理和应用部署。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CHQP3419.pdf) 核对 §1 的定义与案例、§2 的路障、§3 的八个维度和 §4 的愿景；未把引用工作的部署写成本文实验成果。
