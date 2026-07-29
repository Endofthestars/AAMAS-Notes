---
title: "OM2P: Offline Multi-Agent Mean-Flow Policy"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["marl_coordination", "generative_agents", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/WULT4244"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WULT4244.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04g"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["offline-marl", "mean-flow", "generative-policy", "one-step-sampling", "benchmark-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# OM2P: Offline Multi-Agent Mean-Flow Policy

## 一句话总结

OM2P 将 mean-flow generative model 作为 decentralized offline MARL policy，以 reward-aware mean-flow matching 和 Q-function supervision 学习多模态动作分布，并以单步生成避免 diffusion/flow 的迭代采样与额外蒸馏。

## 方法与证据

- 平均速度 mean-flow 用封闭形式更新替代普通 flow matching 的 ODE 数值积分；各 agent 以局部 observation 条件化 policy，在固定离线数据上训练协作 Dec-POMDP（§3–4）。
- 为对齐生成目标和回报，论文组合改造的 mean-flow matching loss 与 Q supervision；generalized exponential-family timestep sampling 和 finite-difference target mean-velocity 估计减少梯度/显存负担（§1、§4）。
- 在 MPE 与 MAMuJoCo offline benchmarks，作者报告近最优表现，并相对所比较方法最高 3.8× GPU memory reduction、10.1× training speed-up；这些是特定实现和硬件下的经验指标（§1）。

## 适用边界与复现

- 单步生成不消除 offline distribution shift、critic 误差或 joint-action OOD 风险；摘要中性能/效率聚合结论需要按环境、数据质量、动作维度和硬件分别复核。
- 复现需公开数据集收集 policy/quality、critic/Q targets、loss 权重、timestep distribution、finite-difference step、网络/agent parameter sharing、采样/吞吐与显存测量协议和 seeds。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WULT4244.pdf) 人工核对 mean-flow 定义、Q 监督和基准范围；未将速度或显存倍数表述为任意离线多智能体部署的普适收益。
