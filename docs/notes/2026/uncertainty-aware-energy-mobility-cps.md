---
title: "Scalable Uncertainty-Aware Decision Frameworks for Energy-Mobility Cyber-Physical Systems"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["applications", "planning_scheduling", "resource_allocation", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/PDLS8233"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PDLS8233.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04v"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass"
spark_consistency: "pass_after_terra_mechanism_and_validation_boundary_revision"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "hierarchical_milp", "uncertain_v2b_control", "calibrated_simulation", "mechanism_guarantees", "private_flexibility", "future_community_coordination"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_feasibility_strategyproofness_and_realism_boundary_check"
escalation_verdict: "pass_after_model_assumption_and_simulation_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted mechanism/validation check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Scalable Uncertainty-Aware Decision Frameworks for Energy-Mobility Cyber-Physical Systems

## 一句话总结

本文把三项既有项目组织成 energy–mobility CPS 决策栈：分层 MILP 安排混合公交车队，滚动时域与 Monte Carlo 处理 workplace V2B 的峰值费用和不确定性，CONSENT 用激励菜单协调私有用户灵活性；证据来自一个月 CARTA 数据和现实数据校准仿真，不是现场全栈部署或无条件机制保证。

## 问题结构

电动交通决策同时受到离散任务分配、charger/depot power、跨时间 SoC、随机到离站和峰值电价约束。V2B 与 V2G 的决策主体不同：V2B 由建筑运营方最小化由账期最高功率决定的 demand charge，同时用户掌握离场时间、最低 SoC 和可调整灵活性等私有信息（§1，p. 3969）。

## 1. 分层混合车队 MILP

文献 [15] 把固定公交服务 blocks 分配给电动、混合和柴油车辆：

1. 先安排受 SoC 与充电约束紧密影响的电动公交；
2. 再由不需要显式充电决策的混合/柴油公交覆盖剩余 blocks；
3. 如果第二阶段不可行，就降级最不高效的电动公交并重求，直到恢复可行。

在 Chattanooga CARTA 一个月数据上，作者报告该方法产生可行混合车队排班，并相对于实际观测部署和 state-of-the-art 基线 [17] 降低运营成本。概述没有给成本差值、运行时间、实例数量或最优性证明，因此只能称该案例中“可行且成本较低”，不能说分层方法对任意车队普遍保证可行和低成本（§2，p. 3969）。

## 2. 稀疏峰值与不确定 V2B

月度 demand charge 由罕见最高峰决定，使 reward 稀疏、长时 credit assignment 脆弱；到达、离开、能量需求和建筑负荷又使确定性计划易失效。

文献 [16] 用 receding-horizon decision making 配合 Monte Carlo plausible-future sampling 估计 peak risk，避免完整 scenario tree 膨胀，并形成面向在线操作的计算—性能权衡。领域优化层处理硬约束与不确定性，学习部分捕获 myopic objective 难以表达的长时 demand-charge 效应。

三页概述没有报告采样量、决策 deadline、实际 latency 或权衡曲线，因此“适合实时”是被引项目的设计定位，不是实时最优或时限保证（§3，pp. 3969–3970）。

## OPTIMUS 校准仿真

OPTIMUS [19] 是 workplace V2B 离散事件测试床，包含随机到离站、SoC、基础设施限制、峰值电价和谈判过程。其现实性锚点包括 EV 行为/灵活性问卷，以及决定峰值形成的真实建筑负荷 telemetry。

该平台能够对罕见峰值和相关需求模式进行压力测试，支持“在校准仿真中检查鲁棒性”；它不等于已经证明罕见事件鲁棒，也不是建筑现场闭环部署验证（§3，p. 3970）。

## 3. CONSENT 与私有信息

CONSENT [14] 为每位战略 EV 用户提供带激励的 flexibility menu，把接受结果连接到后续不确定性感知控制。用户可以私有地选择是否延迟离开或接受较低 SoC。作者称机制在其模型中被构造为满足：

- **Strategy-proofness**：每次谈判中真实报告是占优策略；
- **Individual rationality**：参与相对于退出使用户受益；
- **Budget feasibility**：总激励不超过运营方节省。

“win-win”是设计意图。当前概述没有给出菜单规则、效用/类型空间、完整证明、预算保证的时间口径或不确定性条件，因此只能记录 [14] 声称在其建模假设下满足三项性质，不能由本三页稿独立复核（§4，p. 3970）。

概述还报告激励对齐可减少 schedule rejection、改善用户与运营方结果且不牺牲可行性，但没有拒绝率、效用/成本指标、样本、基线或显著性；这属于 [14] 的经验性主张，不是本稿独立确证的普遍双赢。

## 未来工作

- 扩展到多个建筑、depot 和 fleet 的社区级 V2B，在本地保持硬约束的同时分配长期总功率预算；
- 联合 demand charge 与紧急削减、critical peak pricing、热浪压力等稀疏 demand-response 事件；
- 探索 MARL 的社区协调，但作者明确把罕见事件下的鲁棒性列为开放挑战。

这些不是当前全栈验证结果（§5，p. 3970）。

## 证据与归属边界

- 混合公交 MILP 来自 [15]，在线不确定 V2B 来自 [16]，CONSENT 来自 [14]；本文把三条线综合为从优化、在线控制到激励的路线。
- 证据包括 CARTA 一个月数据、EV 问卷、建筑负荷 telemetry 和 OPTIMUS 校准仿真。概述没有完整参数表、统计结果、代码/数据发布链接或现实系统部署。
- “full stack validated”应理解为现实数据支持的仿真验证，而非各模块在同一现场长期运行，也不能把三个项目各自的性质合并成端到端形式保证（pp. 3969–3971）。

## 与 AAMAS 的关系与核验说明

本文连接 constrained scheduling、online decision-making、mechanism design、private information 与 energy/mobility applications。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PDLS8233.pdf) 核对 §2 的分层回退、§3 的 V2B/OPTIMUS、§4 的 CONSENT 三项性质和 §5 的未来工作；未把校准仿真或被引机制保证写成无条件现场结论。
