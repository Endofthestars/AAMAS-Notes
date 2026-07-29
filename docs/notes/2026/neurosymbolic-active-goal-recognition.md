---
title: "Neurosymbolic Active Goal Recognition in Partially Observable Environments"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "human_agent_interaction", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/NCCT4251"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NCCT4251.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02q"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "keyhole_assumption", "synthetic_grid_world_only", "vlm_confidence_calibration", "observer_policy_training_distribution"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Neurosymbolic Active Goal Recognition in Partially Observable Environments

## 一句话总结

Neuro-AGR 在主动目标识别的 POMDP belief update 中同时推断行动者位置、目标及固定的行为类型：用基于轨迹微调的 VLM 替代手工行动者模型，并用 PPO 在 belief map 上学习观察者的信息采集策略。它在 1,535 个 grid-world 任务上与纯符号方法相当或在部分难例更好，但未加置信阈值的 VLM 混合反而稳定变差；结论依赖 keyhole（行动者不因观察者而改变）假设、合成数据分布和可靠校准。

## 方法与证据

- 基础 PAGR 将观察者决策写为 POMDP，维护 \(j_t(s_t,g)=P(s_t,g\mid o_{0:t},u_{0:t})\)，先用目标条件行动者模型预测、再以观测似然校正；目标 belief 可驱动降低不确定性的信息收集（§1--2）。
- T-PAGR 加入回合内固定但不可见的行为类型 \(\tau\)，从而在 \((s_t,g,\tau)\) 上做联合推断，并以 \(P_\theta(s_{t+1}\mid s_t,g,\tau)\) 描述类型化行动；\(|T|=1\) 时退化为原 PAGR（§2）。
- VLM 由 goal/type 标注轨迹微调，输入像素状态及 \((g,\tau)\) 文本条件预测下一行动，并接入符号 belief update。仅在行动者可见且 VLM 高置信时采用其输出，否则回退到轻量距离式预测器；PPO observer 接收 belief-map 图像，奖励鼓励保持可见并降低目标熵（§3）。
- 评测 1,535 个实例，覆盖 10/12/15 方格、初始距离 3/5/7 和四种 latent types，训练与测试布局分开但由同一生成程序产生。表 1 的 convergence rate 显示无阈值 hybrid 一致低于 pure symbolic；阈值 hybrid 通常在较近距离最佳，RL observer 在较大图或距离 7 的部分难例领先（§4、表 1）。

## 适用边界与复现

- keyhole 假设排除了被观察者察觉、策略性欺骗、协作通信和社会反应；真实人机任务中这些因素会改变行动分布，不能直接沿用后验。
- VLM 的置信度若未校准会污染 Bayes update，论文自己的消融已显示这一点；需要按目标、类型、遮挡、域外视觉与动作稀有性评估 calibration、fallback 和拒答率。
- grid-world、同源程序生成的训练/测试和有限四类行为，不能证明在连续空间、长时任务、复杂视觉、未知目标集或人类数据上的泛化。PPO 还依赖 reward 与训练地图分布。
- 复现应公开生成器、布局划分、可见性、类型/目标先验、belief update、VLM 数据与 prompt/训练、阈值、PPO reward/seed；报告每场景的收敛率、识别时间、校准、VLM 调用成本、失败类型，并进行跨生成器与对抗/反应式行动者测试。

## 与 AAMAS 的关系与核验说明

该文服务于部分可观测的人机交互与自主观察者的主动意图识别。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NCCT4251.pdf) 人工核对 typed belief、VLM 阈值回退、PPO belief-map policy、1,535-instance 协议和表 1；未将合成 grid-world 的收敛率视为真实人类意图识别的部署验证。
