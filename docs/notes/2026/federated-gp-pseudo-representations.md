---
title: "Federated Gaussian Process Learning via Pseudo-Representations for Large-Scale Multi-Robot Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/YQEA8075"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YQEA8075.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["independent_spatial_data_assumption", "pseudo_dataset_information_leakage", "connected_synchronous_network", "centralized_variant_requires_coordinator", "kernel_model_scope", "offline_terrain_dataset_evidence", "no_formal_privacy_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Federated Gaussian Process Learning via Pseudo-Representations for Large-Scale Multi-Robot Systems

## 一句话总结

pxpGP/dec-pxpGP 让每个机器人先把本地数据压缩为经 sparse variational GP 优化的 pseudo-dataset（带边界与点间排斥正则），再以 warm-start、adaptive residual-balancing 的 proximal-inexact consensus ADMM 协同学习 GP hyperparameters；集中式由 coordinator 聚合 pseudo-data，去中心版在连通图中 flooding/邻居共识。作者在合成数据与 NASA SRTM terrain（16–100 agents）上报告优于 gapxGP/dec-gapxGP 的参数和预测表现。它不传原始数据，但 pseudo-representations 仍可泄露信息，且论文没有差分隐私/安全通信证明或真实联机机器人部署。

## 方法与证据

- 精确 GP 的 NLL 训练为 \(O(N^3)\) 时间、\(O(N^2+DN)\) 存储；框架用 SSE kernel，学习 length scales、signal/noise variance（§2）。模型/核选择、stationarity 和高维输入会直接影响预测与不确定性，并非对任意机器人感知模型有效。
- Assumption 1 要求每 agent 持有来自不同输入区域、统计独立的 local dataset；Assumption 2 仅禁止 raw datasets、允许 parameter/summary exchange（§2）。实验以空间/顺序均分数据满足前者；重叠、相关、非 IID、移动机器人重访同一区域时保证与性能未被验证。
- 每个 local sparse GP 生成 pseudo-data，边界 penalty 防止 inducing points 越出本地区域，repulsive penalty 避免聚团；集中 pxpGP 将 pseudo-data 上传 central node 并广播，去中心 dec-pxpGP 经邻居 flooding 共享（§3）。pseudo-data 是由局部观测拟合出的表示，不能自动满足隐私法规或对 membership/model inversion 安全。
- global optimization 是 synchronous proximal-inexact consensus ADMM，使用 warm-start hyperparameters、primal/dual residual stopping 与 adaptive penalty；dec 版假设连通无向图和邻居迭代（§3）。通信失败、异步更新、时变拓扑、拜占庭节点与带宽/能耗限制未在文中评测。
- 数值实验用合成 GP（\(N=16,900/34,900\)）及三张 NASA SRTM terrain tiles（每 tile 30,000 train、每 agent 300 test），fleet sizes 16/49/64/100；去中心图是每节点最多两个邻居的最小连通/低混合速度场景（§4）。这是离线地形回归，非真实多机器人采样与控制闭环。
- 作者报告 pxpGP/dec-pxpGP 在大 fleet 下更接近合成 ground-truth hyperparameters，并在 SRTM 上有较低 NRMSE/NLPD、较少 ADMM rounds；结论依赖该 partition、inducing-point 规则与 baseline/configuration（§4.1–4.3）。性能图表不能证明真实环境的地图更新、碰撞规避或任务效用改善。

## 适用边界与复现

- 适用于空间上可分区、数据量大而希望用紧凑 GP 表示协同估计的多机器人环境建模原型，尤其当集中 raw-data 聚合不可行而可交换模型摘要。
- 使用前应进行 privacy threat modeling、加密/认证、差分隐私或安全聚合评估；pseudo-points/outputs、超参数和迭代消息都可能暴露局部环境信息。不要把“federated”直接视为隐私合规或安全保证。
- 复现应固定 kernel、pseudo/inducing size和边界/repulsion权重、ADMM tolerances/penalty update、warm start、网络拓扑、partition、seeds、SRTM tiles和 train/test split；同时报告 NRMSE、NLPD、hyperparameter error、wall-clock、bytes/round、rounds和失败/断链敏感性。
- 后续应测非 IID/重叠/动态数据、异步与时变通信、真实多机器人 onboard compute、稀疏/丢包网络、隐私攻击/防护和与控制/active sensing 闭环的端到端收益。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的分布式/联邦 GP 与多机器人环境建模工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YQEA8075.pdf) 核验数据/通信假设、pseudo-data/ADMM pipeline、16–100 fleet 实验与 SRTM 范围；未将不传 raw data 误写为形式化隐私、安全通信、异步鲁棒性或真实机器人部署验证。
