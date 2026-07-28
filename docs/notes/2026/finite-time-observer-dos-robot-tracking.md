---
title: "Output-Feedback Security Tracking for Robotic Systems against DoS Attacks Using Finite-Time Observers"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/LZKK2087"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LZKK2087.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["average_dwell_time_dos_assumption", "measurement_zeroing_attack_model", "uniform_ultimate_boundedness_not_asymptotic_tracking", "single_simulated_usv_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Output-Feedback Security Tracking for Robotic Systems against DoS Attacks Using Finite-Time Observers

## 一句话总结

本文为仅测位置的二阶非线性机器人，在预设 DoS 期间将测量置零的模型下，组合 RBFNN finite-time observer、adaptive nonlinear filter 与 backstepping controller；在平均 dwell-time/LMI 条件下保证闭环最终有界和有界跟踪误差，仿真显示 USV 轨迹更好，但不证明真实机器人网络攻击下的安全或零误差控制。

## 方法与证据

- 系统为二阶非线性 plant，未知项由 RBFNN 近似，外扰仅假设有未知上界；position 可测、velocity 不可测。DoS active 时 `y_a=0`，sleep 时 `y_a=y`，攻击持续时间/频率受平均约束（§2）。
- observer 用 finite-time correction/LMI；Proposition 1 使状态估计误差有限时间进入小邻域。controller/filter 用 observer 估计与自适应增益补偿 RBFNN/扰动项（§3）。
- Theorem 2 在所列参数/LMI、dwell-time 条件下给出所有闭环信号 uniformly ultimately bounded，输出跟踪 reference 但稳态误差有界；并非误差全局渐近为零（§3）。
- 仿真是 3-DOF USV，15 RBF neurons、五个预设 DoS windows，和两篇基线比较位置/速度/控制曲线及表 1 指标（§4）。

## 局限与复现

- DoS 被简化为测量归零并满足平均频率/时长；无认证、重放/注入、延迟、乱序、带宽、丢包模式或攻击者自适应策略。
- RBF approximation、扰动界、input gain、LMIs 和 reference derivative bounds 是结论前提；有限时间仅针对估计进入邻域，控制保证是最终有界。
- 仅单一数值 USV，无实体平台、传感器噪声/漂移、执行器饱和、通信栈或统计重复实验；不能从图形比较推出实机韧性。
- 复现应公开 USV 参数、所有 gains/LMI solver、RBF centres/widths、DoS schedule、扰动/初值/reference、baseline implementations 和每项表 1 计算代码，并加入多种攻击/噪声和硬件试验。

## 与 AAMAS 的关系与核验说明

该文研究网络化机器人在 DoS 下的安全控制。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LZKK2087.pdf) 核对系统、DoS、Proposition 1、Theorem 2 与 USV 仿真；未将模型内最终有界性外推为真实系统安全认证。
