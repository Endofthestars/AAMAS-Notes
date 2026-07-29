---
title: "RoboGPT-R1: Enhancing Robot Task Planning with Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/NOXT1107"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NOXT1107.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["benchmark_aligned_sft_data", "reference_trajectory_reward", "simulated_planning_only", "no_real_robot_validation", "no_control_safety_validation", "out_of_domain_performance_gap", "plan_execution_gap"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# RoboGPT-R1: Enhancing Robot Task Planning with Reinforcement Learning

## 一句话总结

RoboGPT-R1 以 Qwen2.5-VL-3B 为骨干，先在与 EB-ALFRED 对齐的数据上监督微调，再用 GRPO 和与参考动作序列的 LCS 奖励做强化微调，提升 EmbodiedBench 的文本化/视觉任务计划成功率。它只评估规划序列，不包含真实机器人闭环执行、碰撞或控制安全验证，不能将基准成功率视为可安全操控能力。

## 方法与证据

- 输出被约束为可执行的 reasoning/plan 格式；RFT 奖励由格式、动作类型/有效性与基于预测—参考轨迹 normalized LCS 的准确性组成，以处理步骤顺序（§3）。LCS 是模仿目标序列的可验证代理，不直接衡量物理可执行性、力/碰撞安全或任务完成后的世界状态。
- Base dataset 由 REBP 的公开数据处理而来，直接从 EmbodiedBench 的 EB-ALFRED tasks 蒸馏并用于 SFT；Aug 来自 ALFRED trajectories，作者称其在动作空间、视觉、任务类型/长度上与 EB-ALFRED 接近但不完全相同，RFT 使用其并保留 Base 防遗忘（§4.1）。因此 EB-ALFRED 的提升应按 benchmark-aligned 训练条件理解。
- 训练为全参数 SFT（8× Ascend 910B3 64GB，约 1.5 h）后 GRPO RFT（4× NVIDIA H20 96GB，约 25 h）（§4.1）。这与“低推理成本”不同：训练资源和数据构建成本不可忽略。
- Table 1：EB-ALFRED seen 六类任务平均 success 55.33%，高于 REBP 35.00%、Qwen2.5-VL-72B 43.67% 与 GPT-4o 51.67%，但低于 GPT-4.1 64.67%。EB-Habitat unseen 平均仅 22.00%，虽高于基础 Qwen2.5-VL-3B 14.67%、7B 15.00% 与 REBP 18.33%，仍明显落后 GPT-4o 57.00%、GPT-4.1 50.67% 和 Qwen2.5-VL-72B 50.33%。
- Ablation：base 3B 为 1.33%，SFT 后 42.00%，SFT+RFT 为 55.33%；long-horizon 从 26% 到 50%。仅用 Aug 做 SFT 为 6.00%，而 Base SFT 后在 Aug 上 RFT 为 55.33%，支持该训练配方在此目标/近邻数据关系下的作用（Tables 2--3）。
- 奖励消融中 LCS 达 55.33%，优于 Step Accuracy 43.67% 和 REBP Acc. 48.33%，long-horizon 为 50%（Table 4）。这些比较固定了该论文的 backbone、数据和更新预算，未分离参考轨迹质量、评价器偏差或执行反馈。

## 适用边界与复现

- 适用于在受控基准或仿真中，将视觉/语言指令转成离散高层子任务序列的研究；计划应在接入机器人前由状态估计、技能控制器、碰撞检查、可达性和执行监控独立验证。
- EB-ALFRED 是 seen、且 Base SFT 数据与其直接对齐；EB-Habitat 22% 的 unseen 结果显示跨环境泛化有限。论文未报告实体机器人、物理交互、动态障碍、传感器噪声、动作延迟、恢复行为或人机共处安全测试。
- LCS 可奖励与参考计划相近的输出，但存在多条等价有效计划；可能抑制新策略，且格式/序列正确不保证物体识别、affordance、抓取、接触或失败恢复正确。
- 复现需固定 EmbodiedBench 版本、seen/unseen protocol、Base/Aug 构成与蒸馏来源、Qwen checkpoint、提示/动作语法、SFT/RFT 超参数和奖励权重、GRPO 采样、seeds、全部基线调用日期/API 版本；报告每类 success、无效格式率、计划长度、推理/训练资源、执行器拒绝率和未见环境分布。
- 真实部署前必须在数字孪生和受限工作空间进行闭环验证，设定速度/力/区域限制、碰撞和不确定性阈值、人工接管与急停；高层计划分数不能替代机器人系统安全论证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的视觉语言模型、强化微调与具身任务规划论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NOXT1107.pdf) 核验训练来源、Tables 1--4 和硬件；没有将 EmbodiedBench 计划成功率写成真实机器人动作执行或安全保证。
