---
title: "Perception-Based Beliefs for POMDPs with Visual Observations"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/XUFR9329"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XUFR9329.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["known_dynamics_requirement", "vision_factorization_assumption", "classifier_calibration", "synthetic_benchmark_scope", "uncertainty_threshold_sensitivity", "planner_runtime_limit"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Perception-Based Beliefs for POMDPs with Visual Observations

## 一句话总结

PBP 将图像分类器给出的视觉状态后验直接用于 vision POMDP 的 belief update，使已有 HSVI/POMCP 等 belief-based planner 不必枚举巨大图像空间；其与标准更新等价仅在观测因子化假设和完美分类器成立时，实证则限于三个中等状态空间视觉基准，且在分类器对噪声图像过度自信时仍会显著退化。

## 方法与证据

- 问题设定要求已知 POMDP dynamics、未知视觉 observation function，并假定视觉观测只依赖相应的视觉 state component（Assumption 1，§3）。论文也说明：若图像还能泄漏非视觉状态信息，PBP 禁止策略使用该信息，所得策略仍可有效但可能次优；这不是对任意视觉决策过程的无损建模。
- perception model 是从 \((z_v,s_v)\) 数据训练的图像分类器，近似 \(Pr(s_v\mid z_v)\)。作者将其乘入 predictive belief 并归一化；视觉图像先验在推导中抵消，对状态采用 uniform prior（§4.1）。Theorem 1 只证明分类器恰好输出真实后验时，新更新与标准 POMDP belief update 重合。
- 面对不精确感知，threshold UQ 在不确定度超过 \(\epsilon\) 时忽略视觉预测、回退到 uniform distribution；weighted UQ 则按不确定度平滑混合分类器与 uniform 分布（§4.2）。若 classifier support 与经 dynamics 传播后的 belief 无重叠，系统改用全状态 uniform fallback，因此它避免空 belief，但不是恢复真实状态估计。
- 框架分别说明接入 point-based planner、particle filter 及 deep RL latent belief 的方式（§4.3）；核心评测实际实例化为 HSVI 和 POMCP。planner 还用 \(D_{plan}\) 估计视觉 observation model，acting 则用未见的 \(D_{act}\) 图像，故并非端到端地从开放世界原始视觉学习。
- 三个基准为带真实交通灯图像的 Intersection、自定义 5×5 FlowerGrid（102 类花图）、以及带“地面湿滑”视觉隐变量的 FrozenLake 4×4/8×8，discount 0.95（§5.1）。感知 DNN 在各自 test set 的准确率均超过 0.8；这不代表复杂自然视觉、连续状态或真实车载感知表现。
- 在相同规划预算下，PBP-HSVI 各基准表现不低于其他非 Oracle 方法，且只略低于完全可观测 Oracle；tPBP/wPBP 多数也有竞争力。tPBP-POMCP 虽优于 NoPerc，却明显较弱，作者归因于当前实现的 scalability 而将其从后续实验排除（§5.2）。DQN/PSRL 的 interaction 与 wall-clock 预算并不完全同构：HSVI 为 300 s，POMCP 每 step 600 s，而 DQN/PSRL-DQN 限 300,000 interactions。
- 对 salt-and-pepper additive noise（约使 classifier accuracy 降至 0.4）和 pure noise，PBP variants 在 FlowerGrid 与两种 FrozenLake 的退化通常较慢；Intersection 却因 classifier 对噪声的错误高置信预测而退化，UQ 不能检测这种失校（§5.3）。不同阈值和不确定度函数的最佳选择也随环境变动，wPBP 减少调阈成本但不是一致最优（§5.4）。

## 适用边界与复现

- 适用于结构和动力学可以明确建模、视觉变量语义可标注、且希望保留 belief-based planning 可解释性的 VPOMDP；不应把它当作未知动力学、端到端视觉控制、任意因果混杂图像或实时安全驾驶的直接方案。
- 部署前需验证 Assumption 1，评估分类器的 calibration/OOD/遮挡/天气/传感器噪声，并审计 uniform fallback 被触发的频率与后果。高置信错误尤其危险：系统会把错误视觉证据强力写入 belief，而 UQ 未必报警。
- 复现应发布三个环境、视觉数据的 \(D_{perc}/D_{plan}/D_{act}\) 划分和 state labels、classifier architecture/training/calibration、known dynamics、HSVI/POMCP 实现、\(\epsilon=0.1\)、MCDO、所有计算预算、10/1,000 episode 汇总差异和各类噪声生成/比例。应报告置信区间、多个数据划分、真实 OOD 与 runtime/memory，不能只报告平均 value。
- 用于高风险自主系统时，belief 与感知不确定性应只是安全监测输入，还需独立传感器交叉检查、可验证的 action constraints、fallback policy 和人工升级路径；图像分类成功或规划 value 不能单独构成安全保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 POMDP planning、视觉感知与不确定性融合论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XUFR9329.pdf) 核验因子化假设、完美分类器条件下的 Theorem 1、TUQ/WUQ 与 uniform fallback、HSVI/POMCP 实例化、三项基准、预算设定及 corrupted-image 反例；没有把受限的 benchmark 结果扩写为通用视觉 agent 的鲁棒性或部署安全承诺。
