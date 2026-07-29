---
title: "xTED: Cross-Domain Adaptation via Diffusion-Based Trajectory Editing"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "marl_coordination", "applications"]
dblp_key: ""
doi: "10.65109/BENP4894"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BENP4894.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "robot_manipulation_evaluation", "synthetic_trajectory_editing", "negative_transfer_risk", "not_safety_certified"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# xTED: Cross-Domain Adaptation via Diffusion-Based Trajectory Editing

## 一句话总结

xTED 不在 policy 模型内部做跨域适配，而是先用 target trajectories 训练结构化 diffusion model，把 source \((s,a,r)\) trajectories 加噪再去噪，得到更贴近 target prior 的编辑数据供 BC/IQL 等下游算法使用。摘要在 MuJoCo 18 个设置和 WidowX 真实机器人三项任务报告相对 target-only 的收益并抑制 raw-source negative transfer；编辑后的轨迹不是经过真实动力学验证的安全动作，实际部署仍需闭环与安全检查。

## 方法与证据

- architecture 分别编码/解码 state、action、reward，并用 self-attention 与结构化 cross-attention：state/action 相互查询，reward 查询 joint state-action，以表示 MDP 的因果依赖（§2）。这是一种网络归纳偏置；摘要没有给出生成一致性、物理可行性、reward 保真度或 OOD trajectory 的定量验证。
- pipeline 是：(1) 用 target data 训练 diffusion target prior；(2) source trajectory 按 \(\kappa=K_k/K\) 加噪；(3) 用该 prior 去噪为 edited source，再并入下游 policy learning（§1–2）。\(\kappa\) 控制保留 source 信息与向 target 靠拢的权衡；过强去噪可能丢失任务语义，过弱则残留 dynamics/morphology gap，摘要未给选择规则或失效边界。
- real-robot 用 BC，在 Airbot source 与 WidowX target 的 Cup/Duck/Pot manipulation 任务。Figure 2/§3 称 raw source 在 Pot 可使成功率降至 0%，xTED 将 Cup 从 43% 提至 97%，并在三任务优于基线；图中未给 trial counts、置信区间、失败类别、碰撞/力限制、感知条件或独立复验。
- simulation 把 xTED 与 IQL 合用，在 HalfCheetah/Walker2d 的 gravity/friction/thigh-size gaps、18 个设定、5 random seeds 比较。Table 1 总计 target-only 716.1、target+raw 727.3（+1.6%）、edited 833.2（+16.4%）；raw source 在 5/18 设定受负迁移影响，而 edited 在 18 个设定 best/on-par（§3）。平均 normalized score 并不代表每个工况、真实传感器或长期操作都改善。

## 适用边界与复现

- 适合离线跨域 RL/IL 数据增强研究，尤其 source/target 任务语义相近但动力学有差异时；不应在未经约束和在线验证的情况下，把编辑 trajectories 直接用于安全关键机器人、车辆、医疗或工业控制。
- 复现需提供 target/source 数据、状态/动作/奖励的尺度及编码、diffusion schedule/\(\kappa\)、结构化 attention、训练 checkpoints、BC/IQL 配置、MuJoCo gap 注入、WidowX/Airbot 标定和相机设置、每任务 trial/seeds及成功判据。应验证去噪前后 action bounds、接触/动力学一致性、reward consistency 和 task semantics，而不只报告 policy score。
- 应测试任务/目标不匹配、观测与相机漂移、source corruption、罕见状态、不同数据量和 \(\kappa\)；报告 mean/CI、失败模式、raw/edited distribution distance、OOD detection 和计算成本。真实机器人需 workspace/速度/力约束、碰撞检测、紧急停止、人工监督和安全 controller；高成功率不等于安全认证或跨硬件泛化。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 embodied/offline RL 跨域 adaptation 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BENP4894.pdf) 核验结构化 diffusion、noise-then-denoise pipeline、MuJoCo Table 1 与 WidowX 结果；没有把编辑数据的 benchmark 收益写成真实动力学正确性、机器人安全或所有 domain gap 的解决方案。
