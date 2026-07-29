---
title: "Cooperative Multi-Agent Alignment via Boolean Task Algebras and Team Morality Chains"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["marl_coordination", "safety_verification", "agent_engineering", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/SCKG1056"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SCKG1056.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05a"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_with_component_status_and_safety_semantics_check"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_roadmap", "cooperative_marl_alignment", "boolean_task_algebra_extension_in_progress", "ctde_extension_in_progress", "team_morality_chains_planned", "lexicographic_scalarisation_in_progress", "deterministic_policy_class_target", "integrated_pipeline_not_demonstrated", "designer_specified_values", "no_safety_certification"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_component_status_lexicographic_guarantee_and_moral_safety_boundary_check"
escalation_verdict: "pass_after_proposal_semantics_and_no_integrated_safety_result_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted alignment-evidence check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Cooperative Multi-Agent Alignment via Boolean Task Algebras and Team Morality Chains

## 一句话总结

作者把 cooperative multi-agent alignment 拆成“用 agent-level Boolean Task Algebra 表达任务意图”和“用 Team Morality Chain 表达严格规范优先级”两部分，并提议以 lexicographic RL 将任务回报置于最低优先级；现有证据只有两项先前基础 [9]/[10]，协作任务代数扩展、词典式标量化、团队道德链和端到端集成都尚在进行或计划中。

## 对齐分解与总体状态

本文区分（§1，p. 3999）：

- **Intention alignment**：agents 是否完成被指定的任务；
- **Value alignment**：joint behavior 是否遵守优先级有序的 normative constraints。

这种分解和统一架构是本博士概述提出的研究方案。作者在 §5 明确称为 `published results` 的基础只有：

1. [9] 的 goal-oriented cooperative task generalisation；
2. [10] 的 MoralityGym 与 morality chains。

其余核心组件不是已完成的统一算法。正文分别使用 `Contribution (in progress)`、`Planned extension`、`I then plan` 与 `remaining steps` 标记状态。

## 已报告的两项先前基础

### Goal-oriented cooperative task generalisation [9]

作者称先前工作学习 goal-conditioned cooperative representations，可复用目标结构，对 compositional task space 中的新 task instances 做 zero-shot inference，而无需额外训练（§1--2，pp. 3999--4000）。

三页稿没有给 [9] 的环境、任务分布、baseline、指标或数值。这里能保留的是作者对该先前工作的范围性概述，不能把 zero-shot 外推到当前尚未完成的异构 agent-level algebra、CTDE 扩展或任意新领域。

### MoralityGym 与 morality chains [10]

Morality chains 把 moral norms 排成 lexicographic objective：高优先级规范先于低优先级目标。作者称 MoralityGym 提供环境，用于系统地指定和评估这种层级，并报告标准 RL 方法即使面对简单任务也可能难以满足严格层级（§1、§3）。

仓库已有 [MoralityGym: A Benchmark for Evaluating Hierarchical Moral Alignment](./moralitygym-hierarchical-moral-alignment.md) 的独立全文笔记。其 98 个场景、指标和 baseline 结果来自对 [10] 的单独核验，不能当作这篇博士概述对新团队框架的实验。

## Intention：agent-level Boolean Task Algebra

单智能体 Boolean task algebra [8] 以 desirable / undesirable terminal outcomes（goal sets）定义 base tasks，再用 AND、OR、NOT 组合新任务。这提供模块化、可检查的 specification language（§2，p. 4000）。

作者正在把它扩展到 cooperative MARL：

- 每个 agent 的任务由 terminal goal conditions 的 Boolean composition 表达；
- 目标是支持 heterogeneous teams，并能说明“每个 agent 正在尝试完成什么”；
- 学习组件建立在 [9] 的 goal-oriented multi-task cooperative MARL 上。

CTDE 是本概述采用的 modelling assumption。将先前 goal-oriented framework 扩展到 centralized training / decentralized execution，同时保持 task-algebra compositionality，正文明确列为 ongoing work，而不是已经验证的零样本或可扩展性结果。

## Value：Team Morality Chain 与 lexicographic RL

### Team Morality Chain 是计划扩展

作者计划把单 agent morality chains 推广到 Team Morality Chains，让每条 norm 约束 heterogeneous team 的 joint behavior。团队 performance 以 social welfare，即 agent returns 之和评估；morality chain 则独立于 individual tasks 约束 joint policy（§3，p. 4000）。

“sum of returns”只是选定的聚合目标，不证明分配公平、个体权利得到保护或规范在道德上正确。multi-agent MoralityGym-style evaluation environment 同样是后续计划。

### 标量化方法仍在开发

`Contribution (in progress)` 的目标是基于 discrete lexicographic optimisation 与 MORL，推导 reward-weight bounds，使其足以在 **deterministic policy classes** 中诱导 lexicographically optimal policies。作者随后计划用类似 Lagrangian 的思路学习合适权重，但目标是 strict lexicographic satisfaction，而非 thresholded trade-off（§3）。

三页稿没有给具体 bound、定理条件、证明、算法或实验。因此不能写成“已找到保证严格优先级的权重”，更不能扩展到 stochastic policies、函数逼近、部分可观测环境或任意 MARL 算法的安全保证。

## 统一框架：结构已描述，集成未完成

§4 的拟议组合是：

1. agent-level Boolean tasks 产生 goal-conditioned task reward；
2. Team Morality Chain 对 normative objectives 排序；
3. lexicographic solver 先满足更高优先级规范；
4. cooperative task performance 只作为最低优先级项优化。

这描述了设计语义和组件接口。§5 仍把团队 morality chains、lexicographic RL、multi-agent benchmark 与 full pipeline integration 列为 remaining steps，因而没有完成的联合 policy、端到端实验、约束违反率或任务表现。

## “严格优先级”不等于已证明安全

`non-negotiable` 表示设计者希望在目标表示中禁止 task reward 与高优先级 norm 交易，并不证明：

- 所指定规范等于正确或完整的人类价值；
- 规范冲突、不可行任务和错误规格已经解决；
- joint policy 在训练分布外仍遵守规范；
- 系统获得形式化安全认证、法律合规、公平性或部署就绪性。

显式 top-down specification 有利于审计“系统被要求优化什么”，但价值内容仍由设计者提供。当前也没有 stakeholder validation、human study、runtime monitor、failure recovery 或真实安全关键场景证据。

## 状态与复现边界

| 组件 | 本稿状态 |
|---|---|
| [9] goal-oriented cooperative task generalisation | 作者称为已发表基础 |
| [10] MoralityGym / morality chains | 作者称为已发表基础 |
| heterogeneous agent-level Boolean Task Algebra | 进行中 |
| CTDE 下保持 compositionality | 进行中 |
| principled scalarisation / deterministic-policy weight bounds | 进行中目标 |
| Lagrangian-inspired weight learning | 计划 |
| Team Morality Chains | 计划 |
| multi-agent MoralityGym-style benchmark | 计划 |
| 完整 intention + value pipeline | 尚未集成验证 |

本稿没有新框架的完整数学定义、伪代码、定理证明、实验环境、baseline、指标、seed、数值或代码链接。复现需要等待这些组件的正式版本，并分别核对 [9]/[10]。

## 与 AAMAS 的关系与核验说明

研究连接 cooperative MARL、compositional task specification、multi-objective optimisation 与规范约束。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SCKG1056.pdf) 核对 §1--5 的组件状态和统一方案，没有把研究路线图写成已完成的团队安全对齐系统。
