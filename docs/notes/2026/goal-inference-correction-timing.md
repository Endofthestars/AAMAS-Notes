---
title: "Enhancing Goal Inference via Correction Timing"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: "10.65109/VZXJ8026"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VZXJ8026.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["physical_hri_task_scope", "offline_data_evaluation", "preplanned_trajectory_assumption", "correction_timing_bias", "simple_goal_structure", "limited_online_control_validation", "participant_generalization"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Enhancing Goal Inference via Correction Timing

## 一句话总结

论文将人何时开始物理纠正机器人作为额外的目标推断信号：以运动历史预测 intervention timing，并把 timing 与纠正起点/初始方向组合，提早推断人想要的抓取放置目标。针对 3,585 条离线纠正轨迹，组合模型在较早纠正时优于只用空间线索；但在已知纠正结束位置时，timing 对细粒度约束几乎无额外收益。

## 方法与证据

- 机器人执行预规划轨迹 \(\xi\)，人可在 \(t_c\) 抓住 gripper 并给出修正轨迹。可用信号为 correction start time、抓取位置、初始方向和 release position；工作讨论 timing 反映人对任务进展、期望、运动可读性/最优性等因素的内部判断（§1、§3）。
- 第一阶段以两层 Transformer 对轨迹历史预测每时步“已/将被纠正”概率；输入包含 expectation alignment、motion consistency、legibility、task progress/optimality 等特征，与只用 optimality 的 Boltzmann baseline 比较。PDF 从该 CDF 导出实际纠正时间 PDF（§4.1）。
- 第二阶段比较 WHERE（空间信息）、WHEN（时机）和 COMBINED。对 correction onset，先用 MLP 从抓取位置/初始速度预测 release position，再以 GMM/贝叶斯后验对候选 goals 推断；\(\alpha=0.8\) 平衡 timing 与空间项。对 correction end，直接用 release location，检验 timing 能否再精化目标（§4.2、§5.3）。
- 数据来自一个经 IRB 审批的物理 HRI 研究：参与者在预规划 RRT* 抓取放置中纠正机器人，任务为不同形状放进四个颜色洞，产生 3,585 条 correction trajectories；只分析每 trial 的首次纠正。轨迹既包含略偏目标、错误颜色等不完美任务政策，也包含成功路径（§5.1）。
- 训练/验证/测试为 60/10/30%，对 50 个随机 split 评估；multi-feature timing model 在 200 runs 中较 Boltzmann baseline 有更好 F1，且在 80/90/100% trajectory completion 的 timing MAE 更好。特征消融显示没有单一特征主导，optimality 对后期纠正稳定重要（§5.2--§6）。
- 对 correction start，COMBINED 在较早时段（70/80/90%）的 goal inference KLD 优于 WHEN/WHERE 单独模型；到 100% 时收益消退。对 release position，COMBINED 不优于 WHERE，因为人通常在真实 goal 附近松手，终点已近乎完整地泄露目标（§6--§8）。

## 适用边界与复现

- 适用于共享自主、实体协作或学习型机器人中希望在完整纠正结束前更早响应的研究场景，且人明确同意提供物理纠正和数据用于目标推断。
- 不应把“较早目标预测”当作机器人可以擅自执行的许可：时机也受犹豫、疲劳、可接近性、信任、风险感知与系统延迟影响；模型把这些归入任务目标会导致错误抢占或伤害用户控制权。
- 复现应固定机器人/控制器、RRT* trajectories、形状-颜色 goals、采样频率、特征定义、Transformer/MLP/GMM、\(\alpha\)、首次纠正筛选、60/10/30 split、200 runs 与 50 random splits；报告 F1、timing MAE、KLD、不同纠正时机的 class imbalance 和个体差异。
- 部署应设置低置信度等待/询问、力与速度限制、即时接管与撤回、参与者隐私保护，以及跨用户、复杂任务、失败/紧急情境和在线闭环实验；作者也指出模型尚未接入 online control，且更丰富任务特征可能必要（§7）。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的人机交互、从物理纠正学习与机器人目标推断论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VZXJ8026.pdf) 核验 timing/space 模型、3,585 条数据、实验 splits/runs、早期 goal inference 结果和作者限制；没有将离线抓取放置结果表述为对任意人或在线安全控制的保证。
