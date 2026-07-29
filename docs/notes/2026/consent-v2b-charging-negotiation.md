---
title: "CONSENT: A Negotiation Framework for Leveraging User Flexibility in Vehicle-to-Building Charging under Uncertainty"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "human_agent_interaction", "game_theory_mechanism", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/ODFH4798"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ODFH4798.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_site_simulation", "small_stated_preference_survey", "forecast_model_dependence", "price_and_tariff_sensitivity", "single_shot_strategyproofness", "user_privacy", "battery_degradation_assumption", "energy_market_regulatory_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# CONSENT: A Negotiation Framework for Leveraging User Flexibility in Vehicle-to-Building Charging under Uncertainty

## 一句话总结

CONSENT 是面向 vehicle-to-building（V2B）充电的在线协商机制：用户到达时可在原请求、若干降低目标 SoC/调整离开时间的激励选项和“全部拒绝”间选择，系统用采样式 MPC 估算各选项的建筑侧价值并排程充放电。论文在以 Nissan ATC Silicon Valley 运营记录校准的模拟中，报告其相对 smart charging + free cost 建筑月成本低约 3.5%、用户单价低 22%；这是对单站点数据、调查校准行为和价格假设下的模拟结果，而非现场干预试验。

## 方法与证据

- 每位接入用户提交 departure time 与目标 SoC；机制提供包含无偏离选项 \(l=0\)、三个有界 flexibility option 和 external charging 的“Reject all”。接受后，系统在充电器容量、SoC、动态电价、需求电费及可能放电约束下优化充/放电（§3--§4）。
- 对每个 flexibility level，在线策略从条件生成的未来 EV 到达/离开/负荷轨迹抽样，解一个 sample-average MILP，最小化能量、峰值 demand、未满足 SoC 和电池放电成本；实验中 negotiation 用 10 个 future samples，charging 用 30 个（§4.3、§6）。它是预测依赖的优化，不是已学习的端到端策略。
- 用户费用为实际按时段能耗费用减去共享的协商 utility（系数 \(\alpha\)）。论文声明在其定义下：如实报告更早 departure 或更高 requested SoC 不能提高单次效用（strategy-proofness）；付款下界给出 budget feasibility；存在 reject 选项时 rational user 可自愿参与（Theorems 1--3）。完整证明在补充材料；保证不包含重复博弈、身份操纵、与其他用户串谋或不准确偏好模型（§4.4、§8）。
- 行为模型来自 28 名大学参与者的匿名 stated-preference 调查，估计他们对 SoC/时间偏离的线性 inconvenience 并聚类为四类，随后用 logit acceptance model 模拟选择。该小型、特定人群调查校准并不能证明商业站点真实司机的长期响应或分配公平性（§5）。
- 评估使用 Santa Clara 商业建筑 2023-05 至 2024-11 的负荷、充电器和车辆遥测；从 100 episodes 中一半用于 future sampling、一半用于 test，且只分析工作日。站点模拟 10 个单向和 5 个双向 charger，采用指定 SoC/degradation/external-charging penalties 与 Silicon Valley Power tariffs（§6）。
- Table 1 中，CONSENT 的建筑成本为 \($8480\pm2171\)/月、用户成本 \($0.138\)/kWh、月用户支出 \($254\pm55\)、拒绝率 21.99%。相对 menu-based negotiation 的用户成本 \($0.157\)/kWh、拒绝率 34.89% 有改善；相对 smart charging + free cost \($8785\pm2144\) 的建筑成本低约 3.5%，相对 uncoordinated free charging 低 5.83%（§7）。误差较大且数字来自模拟月度情景。
- 去除 Reject all 的 ablation 会将建筑成本降到 \($8461\pm2155\)，但用户成本升至 \($0.165\)/kWh；在不同 flexibility profile 和 \(\alpha\) 下也出现成本、用户支出和拒绝率权衡。生成一个用户的全部选项平均约 0.8s、每时间步充电决策约 0.99s，运行时随每日车数增长（§7）。

## 适用边界与复现

- 适用于有可控 V2B 基础设施、能合法提供价格/激励、并可清晰保留用户拒绝权的单建筑能源管理；应将 offer 解释为可选合同，而非默认降低用户出行能力。
- 结果依赖一处商业站点、15 个模拟 charger、工作日筛选、外部充电价 \($0.30\)/kWh、需求电费和电池退化成本，以及预测器的独立性假设。迁移到其他电网、车队、充电协议或电价监管环境前须重校准。
- 复现应固定原始遥测的清洗/训练/测试 episode 切分、预测模型、MPC horizon、10/30 sample 数、MILP/CPLEX 设置、charger/SoC/battery 参数、四类 survey weights、offer deviation 菜单、\(\alpha\)、tariff 和所有拒绝规则；报告成本分布、SoC 未达标、峰值、服务公平性、每决策耗时与拒绝原因。
- 部署前需进行伦理/隐私与电力监管审查，清楚呈现 SoC/离开时间/奖励、支持撤回和人工申诉，并用真实随机或准实验评估参与、弱势用户影响、电池寿命、预测偏差和用户在重复互动中的策略性反应。论文也把把单次 strategy-proofness 扩展到动态重复博弈列为未来工作（§8）。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 将机制设计、人与 agent 协商、MPC 调度用于能源资源分配的论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ODFH4798.pdf) 核验选项/MILP、Theorems 1--3、28 人调查、站点数据与模拟设置、Tables 1--3 和运行时间；没有把其机制内理论性质或校准模拟收益误称为经现场因果验证的普适节能/用户福利结论。
