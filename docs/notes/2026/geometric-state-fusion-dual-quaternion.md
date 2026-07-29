---
title: "Geometric State Fusion for Autonomous Agents: A Comparative Analysis of Dual Quaternion Observer and Kalman Filters"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/CMZH8882"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CMZH8882.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02u"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "ronin_dataset_scope", "timing_unit_ambiguity", "visual_odometry_assumption", "no_on_robot_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Geometric State Fusion for Autonomous Agents: A Comparative Analysis of Dual Quaternion Observer and Kalman Filters

## 一句话总结

GeoDQ 用 dual quaternion 在 \(SE(3)\) 上联合表示旋转与平移，以 IMU 推进、异步视觉里程计（VO）到来时经 SCLERP 几何融合，并用反馈估计偏置。35 条 RoNIN 轨迹上，表 1 报告 GeoDQ 的位置 RMSE 为 \(0.038\pm0.008\) m，低于 ESKF 的 \(0.141\pm0.021\) 和 UKF-M 的 \(0.231\pm0.038\)，并在稀疏更新下较稳定；这只验证了特定数据/实现下的离线估计，不能替代真实机器人上的传感器失效、安全或泛化验证。

## 方法与证据

- dual quaternion \(\hat q=q_r+\epsilon q_d\) 同时编码旋转和平移；SCLERP 使用 \(\hat q_1\odot\exp(\alpha\log(\hat q_1^{-1}\odot\hat q_2))\)，以 screw/geodesic 方式融合两姿态，避免 Euler 角奇异和人为解耦（§2.1）。
- GeoDQ 以高频 IMU 预测，异步 VO 修正时对当前估计与 VO pose 做 SCLERP；积分反馈更新加速度偏置、比例回路校正速度。Algorithm 1 给出 IMU update、VO-available 分支及 \(b_a,b_g\) 更新（§2.2）。
- 在 RoNIN 的 35 条轨迹（200 Hz IMU、5 Hz VO）对 ESKF、UKF-M：表 1 为 GeoDQ 0.038 m / 2813.6 ms，ESKF 0.141 m / 3189.2 ms，UKF-M 0.231 m / 14624.7 ms。文中称 Numba-JIT 后“2.8 ms per trajectory”，与表中 2813.6 ms 的单位/聚合方式不一致；本文只保留原始数值，不自行换算（§3、表 1）。
- 图 2 展示单条 `a025_2` 的平滑跟踪；图 3 称 update interval 增大时 GeoDQ 可稳定至 30 samples（约 7 Hz），而标准 filters 更易发散。这是具体基准下的可视化/robustness 曲线，不是故障安全保证（§3--4）。

## 适用边界与复现

- 适合 IMU+VO 的 6-DoF pose fusion 原型，尤其当几何一致性和嵌入式计算是设计考量；需要与实际相机、时间同步、标定、延迟和失效检测协同，而不是仅替换滤波器。
- RoNIN、35 条轨迹、IMU/VO 频率、误差指标、Numba-JIT、硬件和超参数决定相对结果；表/正文的计时歧义使“10%/5×”或“sub-millisecond”之类效率外推须谨慎。
- 稀疏 VO 更新实验不覆盖恶意/系统性 VO 错误、遮挡、视觉退化、IMU 饱和、快速运动、在线重定位或闭环控制。平滑轨迹不等价于碰撞安全或导航成功。
- 复现应公开 RoNIN 切分、VO 来源、标定、同步、GeoDQ/ESKF/UKF-M 参数、JIT/硬件与完整 timing 定义；逐轨迹报告位置/姿态误差、实时延迟、内存和失败率，并在独立设备/环境及受控 dropout/偏置实验中验证。

## 与 AAMAS 的关系与核验说明

该文研究自主体的几何感知与状态估计。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CMZH8882.pdf) 人工核对 dual quaternion/SCLERP、Algorithm 1、RoNIN 35-trajectory 设置、表 1 和稀疏更新图；明确保留计时单位的摘要内歧义，未声称真实机器人安全性。
