---
title: "PREFINE: Preference-based Implicit Reward and Cost Fine-tuning for Safety Alignment"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/SDRB4374"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SDRB4374.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["offline_cost_labels_underlie_preferences", "counterfactual_label_noise_and_coverage", "simulated_continuous_control_scope", "safety_constraint_not_guarantee", "baseline_runtime_comparability"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# PREFINE: Preference-based Implicit Reward and Cost Fine-tuning for Safety Alignment

## 一句话总结

PREFINE 以少量低 cost/high reward 轨迹与高 cost 轨迹的偏好比较，将已训练的可微 RL/IL policy 通过 DPO 风格损失加 SFT anchor 做离线安全微调；在 DSRL 的 12 个仿真连续控制任务上常能降低归一化 cost 并保留 reward，但“没有数值 cost”只适用于优化输入形式，实验偏好和评估仍由原始 cost threshold 构造，且不构成部署安全保证。

## 方法与证据

- 先从 DSRL 的高 reward、低 cost 部分以 BC 训练并冻结 reference policy `π_ref`；用累计 cost threshold 将同一离线数据确定性切成 preferred `D_p` 与 non-preferred `D_np`，文中默认 `N_p=100`、`N_np=20`。因此训练时不拟合显式 cost model，但监督来源仍是基准提供的 cost 标签（§3、§5.1）。
- 对 `D_p`/`D_np` 的 state-action，PREFINE 从当前 policy 采 counterfactual action，形成同 state 的对比；DPO 项鼓励 preferred action 概率高于 counterfactual，SFT 项锚定高 reward 行为。作者认为 policy-sampling 比 dataset+policy 混采的二值 label mismatch 更低，但这依赖离线集对当前 policy state distribution 有足够局部覆盖（§3.2--3.3、图 2）。
- 实验从 DSRL 的 38 项任务中因算力选 12 项：Safety Gym 7 项、BulletSafetyGym 5 项；每个 dataset 用 3 个 cost thresholds、5 seeds，比 BC、PPL、SafeDICE、CPQ。指标是 normalized reward/cost，cost ≤ 1 为满足约束（§5.1、表 1）。
- 作者报告 Safety Gym 全部任务满足 cost 阈值、Bullet Gym 80%，并在 Walker2dVelocity 上称 PREFINE 约 1.5 小时、SafeDICE/CPQ 超过 10 小时；该时长排除 evaluation，使用同一 V100、splits/seeds，但部分 baseline 是 reference code 或作者重实现，故是该设置下的比较（§5.2--5.3、图 3--4）。

## 局限与复现

- 安全偏好并非真实人类在无 cost 情况下提供：它由已知累计 cost 阈值生成。真实偏好若不一致、延迟、上下文相关或将 reward/safety 混合，DPO 对比目标及结果未被验证；unsafe 数据“稀少”也不能消除收集它本身的风险。
- counterfactual action 来自不断变化的 policy，却以原轨迹/阈值推断 preferred direction；状态覆盖不足、动作改变后动力学不同或逐 action 与逐 trajectory safety 不一致时，会产生错误比较。论文也承认 safe trajectory 中并非所有动作安全，并以 SFT 缓解而非证明解决。
- DSRL 是离线 Safety Gym/BulletSafetyGym 连续控制。没有真实机器人、驾驶或手术数据，没有传感器噪声、分布漂移、罕见灾难、在线监控/recovery 或 CMDP hard-constraint 证明；normalized cost ≤ 1 只是基准阈值，不是系统级安全认证。
- 复现应锁定 DSRL version/每个阈值的 split、BC reference policy/VAE 架构、`β`/`λ`、policy-sampling temperature、训练步数、seeds、硬件和是否计入生成/评估成本；独立执行各 baseline 原始实现并报告每 task/threshold 原始 reward-cost、违约尾部风险和置信区间。

## 与 AAMAS 的关系与核验说明

该文研究离线连续决策 policy 的偏好式安全适配。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SDRB4374.pdf) 核对 DPO+SFT 目标、policy-sampled counterfactual、DSRL 12-task 范围、基线与报告时间；未将仿真 cost 降低解释为无显式监督或真实环境的安全保证。
