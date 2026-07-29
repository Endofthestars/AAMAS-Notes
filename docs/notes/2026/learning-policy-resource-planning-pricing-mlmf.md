---
title: "Learning-Based Policy Design for Resource Planning and Pricing in Heterogeneous Multi-Leader–Multi-Follower Systems"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["game_theory_mechanism", "resource_allocation", "marl_coordination", "applications"]
dblp_key: ""
doi: "10.65109/BCYL3315"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BCYL3315.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04u"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass"
spark_consistency: "pass_after_terra_completed_vs_proposed_revision"
risk_level: "high"
risk_tags: ["doctoral_research_proposal", "multi_leader_multi_follower", "private_heterogeneity", "nonstationary_learning", "equilibrium_proxies", "planned_marl_evaluation", "no_convergence_or_scalability_result"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_equilibrium_efficiency_and_completed_vs_proposed_boundary_check"
escalation_verdict: "pass_after_stage_and_evidence_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted equilibrium/efficiency check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Learning-Based Policy Design for Resource Planning and Pricing in Heterogeneous Multi-Leader–Multi-Follower Systems

## 一句话总结

本文以 EV 充电为例，把已完成的单服务商选址—定价和三层进入者 Stackelberg 模型，推进为拟议的异构多领导者—多追随者 MARL 研究路线；Stages A–C 的均衡、效率、稳定性和扩展性仍待实验，而不是本稿已证明的结果。

## 问题与研究缺口

拥堵敏感市场中的供应商必须同时预判竞争者和用户对价格、容量、位置与拥堵的响应。既有 EV 充电模型常固定站点、假设同质用户，或把竞争者视为静态/非策略主体；RL 工作也较少解释多个竞争领导者和私有异构用户共同学习时产生的均衡。

本文关注的联合缺口是：多个供应商独立设计政策，用户偏好包含充电方式、价格、排队、出行时间与 range anxiety，且只通过行为显露；需求、道路拥堵和供电使用又相互耦合（§1–2，p. 3960）。

## 已完成的两个阶段

### 单服务商联合选址与定价

作者先在原子与非原子 connected congestion game 中，从单一充电服务商角度联合优化站点位置和价格。相关工作 [3]–[5] 报告，把行程时间、排队延迟和充电费的相互作用一起纳入，比只优化单个参数取得更好结果。

该概述没有给出指标、改善幅度或跨网络稳健性，因此不能把它扩展成多领导者、异构 MARL 或真实部署中的普遍效率提升（§3，pp. 3960–3961）。

### 三层进入者 Stackelberg 模型

第二阶段 [6] 的顺序是：

1. 潜在进入者选择充电站位置；
2. 现有 en-route rapid-charging 服务商竞争定价；
3. EV 与非 EV 驾驶者选择路线和充电选项。

该模型加入多个站点所有者和自适应非 EV 交通。作者报告，忽略非 EV 流量会系统性误估需求—拥堵耦合，进而扭曲定价与基础设施规划；本三页稿没有给出误差方向、大小或适用网络范围（§3 与 Figure 1，p. 3961）。

## 拟议的异构学习框架

- **Followers**：异构 EV 驾驶者作为学习主体，私有偏好不被供应商直接观察，只由行为和均衡结果间接揭示。
- **Leaders**：多个充电服务商在不完整信息下独立学习定价，随后扩展到容量和选址，并预判竞争者与用户的战略响应。
- **Learning**：用 MARL 和 learning-in-games 同时学习领导者政策与追随者策略；这种同步适应会造成非平稳性，论文把它列为挑战，而非已解决的稳定性问题（§4，p. 3961）。

## Stages A–C

1. **Stage A**：固定站点位置和容量，只研究异构追随者下的定价竞争。
2. **Stage B**：位置仍固定，扩展为定价与容量联合决策。
3. **Stage C**：再加入站点选址。

三阶段均是后续路线。计划交付包括异构追随者博弈模型、竞争领导者学习方法，以及对涌现均衡与系统效率的系统实证评估；当前稿没有相应训练结果、收敛证明或效率数值（§4，p. 3961）。

## 拟用诊断与指标

- 用遗憾诊断 coarse correlated equilibrium/no-regret learning；
- 用 best-response exploitability 度量 approximate Nash；
- 用社会成本、拥堵和供应商利润评价系统性能。

这些是 **equilibrium proxies 和评估计划**，不是已经识别出的均衡。哪种均衡概念在非平稳竞争中仍有意义、去中心化竞争造成多大效率损失，以及 no-regret、two-timescale 或 mean-field MARL 如何权衡经验稳定性和理论可解释性，均列为待解决问题（§4–5，pp. 3961–3962）。

## 证据与限制

- 已完成结果来自 [3]–[6]；当前稿重新组织这些阶段，并提出 MLMF 学习框架、评估方案和研究问题。
- Stages A–C 没有实验曲线、超参数、数据集、代码仓库、复杂度、均衡存在/收敛证明或部署证据。
- 私有偏好的可识别性、多个学习速度之间的耦合、代理均衡指标是否可靠，以及从 EV 充电迁移到云、能源和其他出行市场，都需要后续验证。
- 因而不能据此声称拟议 MARL 已经稳定、有效率或可扩展（pp. 3960–3962）。

## 与 AAMAS 的关系与核验说明

该研究连接 Stackelberg games、congestion games、resource planning、pricing 与 MARL。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BCYL3315.pdf) 核对 §3 的已完成模型、Figure 1 的三层顺序以及 §4–5 的拟议阶段和诊断指标；未把研究计划写成已完成的学习或均衡结果。
