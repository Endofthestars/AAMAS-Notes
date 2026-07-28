---
title: "A Survey of Reinforcement Learning for Autonomous Air Combat: Current Progresses and Limitations"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "robotics_embodied", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GEMF4800.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["survey_scope", "simulation_to_real_gap", "dual_use_safety_context"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Survey of Reinforcement Learning for Autonomous Air Combat: Current Progresses and Limitations

## 一句话总结

这是一篇聚焦 RL/MARL 自主空战的综述，按单/多 agent、全控制/分层控制、观测建模和开放性/可复现性四个轴比较研究，同时强调从仿真到真实系统的未解决缺口。

## 方法与证据

- 综述只覆盖从采样轨迹学习的 model-free RL，并把空战工作按 single-agent/MARL、full-control/hierarchical、MDP/POMDP 传感器假设和开/闭源仿真环境分类（§2–3）。
- CTDE 是文中讨论的多 agent 训练范式：训练可用全局状态或联合动作等特权信息，执行则依赖局部观测；它缓解协调学习但不消除多 learner 的非平稳性与局部可观测性问题（§2）。
- 全控制可直接输出致动器级命令、提高动力学真实性，但训练不稳定且依赖观测精度；分层方法把机动控制与战术 macro-action/任务分配拆层，以改善复用与可扩展协调（§3.2）。
- 完全可观测的 MDP 抽象可加速收敛，却遗漏真实噪声与不确定性；局部传感的 POMDP 更贴近实际，但需处理时序信息整合。雷达/电子战参数常涉保密，限制公开复现的保真度（§3.3）。
- 综述指出闭源平台往往提供更细的雷达、导弹与飞行动力学，却限制独立验证；开放平台更便于标准化比较，但通常简化物理、传感器或任务层级（§3.4）。
- 归纳的持久限制包括简化感知与通信、同质/对称交战场景、真实平台迁移、训练计算量与更大规模协同；这些是综述识别的研究缺口，不是已证明可由现有算法解决的能力（§4–5）。

## 局限与复现

- 文献筛选是代表性而非穷尽性；它不能作为某一算法在真实空战系统有效或安全的实证证明。
- 对比实验必须报告可观测信息、传感器误差、通信限制、飞行动力学、场景对称性、随机种子、训练预算和环境版本；否则跨平台结果不可直接比较。
- 仿真中较高 win-rate 不等于现实部署可行性：sim-to-real、对抗泛化、可靠性、规则和人类监督仍是独立门槛。
- 该主题具有明显双重用途风险；复现应限定于合规仿真、研究评估和防御性安全测试，避免将综述转化为现实武器部署指导。

## 与 AAMAS 的关系与核验说明

该综述连接多 agent 协作、具身控制和高风险仿真应用。笔记基于官方公开 [AAMAS PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GEMF4800.pdf) 核对其分类维度和作者明确列出的局限。
