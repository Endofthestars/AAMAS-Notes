---
title: "Multiagent System for Dynamic Multicriteria Traffic Routing in Urban Environments"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "applications"]
dblp_key: ""
doi: "10.65109/MCOL3382"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/MCOL3382.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["sumo_simulation_only", "full_participation_assumption", "traffic_prediction_dependence", "multicriteria_tradeoffs", "baseline_comparison_scope", "rerouting_user_impact", "no_road_safety_or_equity_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multiagent System for Dynamic Multicriteria Traffic Routing in Urban Environments

## 一句话总结

论文把城市路网分给多个 Area Control Agents (ACAs)，以预测的时间、燃油等动态准则做协作多准则最短路与主动/被动重路由。在 SUMO 网格和 Ingolstadt InTAS 仿真中，它较无优化和一个集中反应式基线改善拥堵相关指标；但不涉及真实道路部署、部分参与者、交通安全或公平性评估。

## 方法与证据

- Master Agent 与 SUMO/TraCI 交互，ACAs 只持有本区域动态交通信息、通过边界请求合作完成跨区 multicriteria shortest path search (MCSPS)。边成本可包括时间、距离、燃油、密度等，路线从 Pareto candidates 选取（§3）。
- 系统以同步 interval 20 s 更新预测、每 60 s 可重路由；预测使用 XGBoost，特征包括车道数、限速、绿灯比例和当前密度。实验让两种方法都对 85% 车辆可重路由，并以相同 prediction models/parameters 做比较（§3--4）。
- SUMO 评估两种场景：10×15 合成网格和由活动模式产生流量的 InTAS，后者模拟 07:00--11:00 晨高峰；每项配置重复 10 次。拥堵 teleportation 被禁用，但 prolonged yield/wrong-lane teleportations 保留以防死锁（§4.1）。
- Table 2：网格中 3 ACA 相比标准场景，time 294.44→232.88 s、fuel 182.26→162.14 g、teleportations 65→0.50，但距离 923.71→927.81 m；InTAS 中 time 927.59→627.82 s、fuel 597.07→420.03 g、teleportations 1183→58.40、距离 5012.36→4795.63 m。2 ACA 往往差于 1/3 ACA，作者归因于长边界导致可能遗漏反复跨区域的路线。
- 单 ACA MCSPS query runtime（Table 3）随区域划分下降：InTAS 1/2/3 ACA 为 4.250/1.073/0.308 s。论文称三区协作示例的总查询约 1.232 s，相比单区 4.250 s 超过三倍加速；这不包括端到端车联网延迟、预测/协调失败或峰值并发。
- 对照 Ho et al. 的集中 reactive k-shortest-path 方法（3 ACA、baseline 仅以 predicted time 规划）。Table 4 在 InTAS：multiagent time 627.82 s vs baseline 865.87 s，fuel 420.03 vs 567.18 g，teleportations 58.40 vs 934.90；其 multiagent run 的 reactive reroutes 为 0，而 baseline 为 957.90，说明优势混合了主动 routing、MCSPS 与架构差异，不能归因于分散化本身。

## 适用边界与复现

- 适用于仿真或受控运营中探索多准则、跨区域协作路由。实际路线建议需要可靠地图、实时事件、法规、道路容量和驾驶员/导航系统接受度，且必须与安全关键交通控制隔离验证。
- 论文列明真实部署的 partial participation 不在范围内；参与率下降时密度预测更关键。交通需求响应、路线服从率、隐私、通信延迟/丢失、事故、施工、紧急车辆、行人/自行车和车辆动力学均未评估。
- “multicriteria”只说明可纳入安全/景观等准则，实验指标实际为距离、时间、燃油和 teleportations；没有道路碰撞风险、弱势道路使用者、区域公平、排放分布或绕行外部性评估，不能称为安全/公平路由。
- 复现应固定 SUMO/InTAS 版本、网格/路网/信号、需求生成、KaHIP 划分与 ACA placement、XGBoost 数据/特征/训练、MCSPS/\(\epsilon=0.99\)、20/60 s intervals、85% reroute fraction、teleportation policy、奖励/路线选择、baseline 配置与十个 seeds；报告均值/方差、网络消息/延迟、各区域与用户的代价分布、服从率和事故扰动。
- 如用于公众，须在影子模式与分阶段试验中由交通主管部门审查，提供退出/人工干预、紧急车辆优先和公平影响监控；仿真 travel-time 改善不能替代道路安全或监管许可。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的协作规划、城市交通路由与多智能体系统论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/MCOL3382.pdf) 核验架构、SUMO/InTAS 协议、Tables 2--4 与部分参与限制；没有把仿真中的拥堵改善误写成真实世界安全、公平或完整交通控制效果。
