---
title: "GCMRBench: Goal-Conditioned Multi-Robot Environments and Benchmarks for Advancing Offline Multi-Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/HRLQ1652"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HRLQ1652.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02x"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "pybullet_simulation_scope", "limited_dataset_diversity", "offline_dataset_quality", "future_open_source_commitment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# GCMRBench: Goal-Conditioned Multi-Robot Environments and Benchmarks for Advancing Offline Multi-Agent Reinforcement Learning

## 一句话总结

GCMRBench 是基于 PyBullet/panda-gym 的 goal-conditioned 双臂机器人 OMARL 基准：22 个任务分为协作、多目标、转接、竞争和混合五类，并配套 56 个单/多智能体离线数据集，以任务成功率为主指标。摘要在选定任务上比较 MABC、OMIGA、InSPO，称后两者更能利用中等质量数据；但数据行为多样性和环境随机性仍有限，真实机器人只描述了 inference test，不能以仿真成功率宣称可安全部署。

## 方法与证据

- 22 个双臂任务包括 11 个 cooperation、3 个 multi-goal、3 个 transition、4 个 competition、1 个 hybrid；每臂可作为独立 agent，支持单/多智能体模式和相对可观测性（§1--2）。
- 56 个 offline datasets 包括预训练专家 noisy rollout、30--60% success 的 suboptimal medium、随机、expert+poor mixed 及 human-guided data；任务成功率作为主要评价指标（§2--3）。
- 表 1 在 Lift、Insert(Goal-Changing)、ReachSeq、CompetitionPush、AsynStack 上报告 20k training episodes 后五次运行均值±sample standard deviation。例如中等 Insert-GC：MABC 0.34、OMIGA 0.37、InSPO 0.60；中等 AsynStack 各法约 0.12--0.18，显示任务与数据质量敏感（§3、表 1）。
- 作者称 OMIGA/InSPO 在总体上对 medium data 较好，也观察到训练成功率振荡/峰后退化；完整代码、数据和论文内容承诺未来开源（§3--4）。

## 适用边界与复现

- 适合分析 goal-conditioned offline MARL 在近工业双臂仿真任务的比较；PyBullet 接触、观测、动作、奖励、初始状态和时限与真实 Festo/工业工作站仍有 sim-to-real 差距。
- 数据质量标签和 noisy rollout 生成策略决定 offline distribution；行为多样性与环境随机性有限是作者明确限制，不能将算法排名外推到开放世界或人类示范数据。
- 五个 selected environments 与 20k episode 训练不代表所有 22 task/56 dataset；标准差较大时应报告成功率分布、失败模式、data coverage 和全 seed 曲线。
- 复现应锁定物理引擎版本、任务/goal/观测/action 定义、数据生成 policy、noise、dataset splits、baseline code/hyperparameters 和所有 seeds；在公开资源可得后验证训练/评估隔离，并进行随机化、sensor delay、contact failure 与真实硬件安全测试。

## 与 AAMAS 的关系与核验说明

该文提供多机器人 offline MARL 的环境与数据基准。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HRLQ1652.pdf) 人工核对任务/数据数量、类别、协议、表 1 和作者列明的限制；未把未来开源或仿真结果当作实际机器人部署证明。
