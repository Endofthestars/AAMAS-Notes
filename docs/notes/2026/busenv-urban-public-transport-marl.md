---
title: "BusEnv: A Multi-agent Reinforcement Learning Environment and Benchmark for Urban Public Transportation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "applications", "safety_verification"]
dblp_key: ""
doi: "10.65109/CYHA2042"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CYHA2042.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["single_city_data_scope", "simulator_to_operations_gap", "reward_weight_dependence", "independent_learning_only", "passenger_equity_not_evaluated", "training_carbon_vs_operational_emissions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# BusEnv: A Multi-agent Reinforcement Learning Environment and Benchmark for Urban Public Transportation

## 一句话总结

BusEnv 是以巴西 Salvador 2024-03 至 2025-03 的城市公共交通数据构建的 Dec-POMDP/MARL benchmark：约 70 万乘客、2,000 vehicles、近 400 lines、3,000 stops，按实际需求、路线 travel time 与 traffic variability 模拟公交。每车可 WAIT/MOVE/SERVICE_CENTER，shared reward 混合服务、效率、维护与规则性；九种 MARLlib policy-gradient baseline 在**独立学习、无显式通信/策略共享**条件下比较。它适合研究算法稳定性，但不等于已验证的实际公交优化、乘客公平或减碳干预。

## 方法与证据

- 数据覆盖 passenger OD、board/alight、车辆在边上的时间/速度/客流，并建成固定 topology、随时间变 attributes 的 spatial-temporal graph。虽然基于真实记录，环境仍对 demand、traffic、maintenance/fuel 和 agent actions 做仿真/抽象，而非在线接入真实运营（§3.1）。
- global state 包含车辆位置/状态、stop demand、occupancy、traffic；单车 observation 只有平均 travel time、预测 future demand、occupancy rate、normalized uptime 等局部信号。故是 partial observability，需求预测误差与不可见网络状态被环境模型吸收（§3.2）。
- action space 仅为 WAIT（hold）、MOVE（沿预设 route 至下一站）、SERVICE_CENTER（维护分流）。它不涵盖 route redesign、停站跳停、班次/车辆编排、票价、司机排班、应急调度或 multimodal transfer 决策；论文说这些是未来可模拟的策略而非本次已评测动作（§2--3）。
- shared reward 是 \(r=\alpha_1q+\alpha_2e+\alpha_3m+\alpha_4c\)，分别是服务质量、效率、维护、traffic regularity；论文没有把这些多目标权重转化为经乘客/运营方共同确认的社会福利。不同 \(\alpha\) 可改变等待、coverage、energy、准点与弱势线路之间的取舍（§3.2）。
- 训练 protocol 明确为 independent learners：本地 observation、各自 experience、shared team reward，且没有 explicit policy sharing/inter-agent communication。即使 MAPPO/COMA 等原本可使用 centralized critic，本文所有方法均按这个独立配置跑；结果不是完整 CTDE/协同控制能力的比较（§4.1--4.2）。
- 九个算法均在相同环境/agent configuration 下训练 400,000 steps、50 independent runs。Table 3：最高 final reward 是 MAA2C 77.41±0.24，其次 ITRPO 77.16、MAPPO 75.31；最高 AUC 是 MAPPO 0.924，IPPO 0.917。HAPPO -506.84、COMA -73.69；因此“PPO best”需区分学习曲线 AUC/稳定性与最终 reward，不能泛称所有 PPO 变体最佳（§4.3、Table 3）。
- 论文用 CodeCarbon 展示不稳定训练算法有更高 CO2/energy footprint，并将此与 reward instability 相联。这里的证据是**训练计算**的排放/能耗及环境内 power metrics，不是公交车队实际燃油、尾气或乘客出行替代所带来的因果减排测量（§4.3、Figure 3）。

## 适用边界与复现

- 单一城市/一年数据不代表其他城市的道路几何、客流季节性、支付/换乘制度、车队类型、驾驶行为、法规、无障碍需要或突发事件。应做跨城市、节假日/极端天气、施工、事故、需求激增、数据缺失和网络调整的 OOD evaluation。
- 高平均 reward 不等于乘客公平：论文未报告分社区/收入/残障/夜间/边缘线路的等待、拒载、拥挤、可靠性与转乘负担。部署前需把 equity/coverage/service guarantees 作为明确 constraints 或可审计指标，而非仅由全局 reward 隐式代表。
- RL 直接控制 hold/move/maintenance 会涉及安全、司机规程、法规、乘客信息与调度员职责。实际试点需要离线 replay、conservative/offline evaluation、hard operational constraints、人工批准/override、rollback、实时监控及逐线路 staged deployment，不能由 simulation reward 直接下发控制。
- shared reward 会带来 credit-assignment 和局部/全局目标冲突；independent learners 在非平稳环境可能学到脆弱策略。应对 reward weights、forecast errors、random seed、policy failures、near-term service disruption、passenger equity与数据漂移开展 sensitivity/ablation。
- 复现应固定 raw-data access/governance、preprocessing/split、graph/route reconstruction、demand/traffic stochastic model、observation/action semantics、\(\alpha\) weights、episode day、MARLlib/Ray versions、每算法 hyperparameters、400k/50-run budget、CodeCarbon hardware/region设置；分别报告 simulation operations metrics 与 training compute footprint。

## 与 AAMAS 的关系与核验说明

这是应用型 MARL benchmark。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CYHA2042.pdf) 核对 Salvador 数据范围、Dec-POMDP/动作/奖励、independent-learning protocol、Table 3、CodeCarbon 解释与未来协同扩展；没有将单城仿真 reward、训练期碳指标或局部稳定性误写为真实公交部署绩效、乘客公平或实际 fleet emission reduction。
