---
title: "Ratio-Based Signaling for Source-Victim Separation in Swarm Fault Detection"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/UYYF8433"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYYF8433.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["simulation_only", "synthetic_fault_model", "parameter_calibration", "small_seed_counts", "local_communication_assumption", "source_victim_label_assumption", "no_standard_benchmark"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Ratio-Based Signaling for Source-Victim Separation in Swarm Fault Detection

## 一句话总结

论文提出给 swarm agent 同时维护内部与外部“压力激素”：内部占比高的 agent 更像故障源，外部占比高的 agent 更像受害者；用该比率调整隔离阈值，试图避免邻居投票把受害健康 agent 一并隔离。在作者的二维仿真中，30--120 个 agent 的比率信号法较 threshold/voting baseline 更能抑制 cascade；但这是参数校准后的合成故障模拟，尚不是实机安全保证。

## 方法与证据

- 每个 agent 在 10 Hz 连续二维仿真中维护任务性能 (x_i\in[0,1])、内部压力 (H_i^{int}) 与从 (K)-近邻吸收的外部压力 (H_i^{ext})。ratio (r_i=H_i^{int}/(H_i^{int}+H_i^{ext}+\epsilon)) 被解释为故障因果方向的局部 proxy（§3）。
- 发射量由内部压力和严重性能退化驱动，并按邻居外部压力的趋势自适应调增/调低 gain；信号按距离衰减、每时间步一跳传播，吸收受剩余容量限制。每 agent 只向 (K=6) 近邻广播两个浮点量，作者据此给出单 agent (O(K)) 局部通信/处理的尺度论证（§3.4、§6.1）。
- quarantine threshold 随 ratio 分段：(r_i>0.6) 的可能 source 用较低阈值 0.30，混合区 0.35，(r_i\le0.4) 的可能 victim 用较高阈值 0.45；阈值经 calibration grid search 选定。高于阈值即隔离，低于 release threshold 0.25 连续三步后恢复（§3.5）。这既是方法核心，也是需要迁移校准的超参数依赖。
- 评估比较 Baseline、internal Threshold、neighbor Voting 与双流 Hormone，度量 task completion (TCR)、fault quarantine efficiency、cascade prevention、AUC、precision/recall 等；规模实验为 30--120 agents、25% fault、20 s、10 seeds，其他试验有 1、3、5 或 10 个 seeds（§4）。
- 在 (N=120)、25% faults 的表 2 中，Hormone 报告 TCR (72.0\pm0.4\%\)、cascade prevention (96.0\pm0.6\%\)、precision (89.5\pm1.5\%\)、检测 (1.80\pm0.03) s；Threshold 的 TCR 为 (21.3\pm1.4\%\)，Voting 为 (1.8\pm0.9\%\)（§5.1）。这些是同一模拟器内的对比，不构成跨论文或实机 benchmark 的结论。
- 轨迹实验（60 agents、50% fault、单 seed）中，source 的早期 internal/external ratio 均值为 (0.82\pm0.11)，后期被隔离的健康 agent 为 (0.31\pm0.18)；ratio 法 1.2 s 首次隔离，最终隔离全部 30 个 fault 和 2 个 false positives（§5.3）。单条轨迹只适合作机制示例。
- 100% packet loss 时外部流消失，方法退回更接近 internal-only 诊断：120-agent 条件下 TCR 从 66.8% 降到 49.5%，precision 从 90.6% 降到 60.1%，但仍高于该文 Threshold baseline；去掉 ratio-conditioned threshold 的 ablation 也降低 TCR/precision/cascade prevention（§5.5--§5.6）。
- 作者承认没有 source--victim 标准 benchmark，且与文献中 51±18 s latency 的横向比较因实验设置不同而受限；未来工作是 10--20 台 ground robots 的硬件验证、噪声/延迟与更大规模分析（§6.1、§6.3）。

## 适用边界与复现

- 适用于能定义内部健康状态、能接收有限邻居信号、且故障影响确有“源先产生、邻居后吸收”结构的 swarm。若环境扰动会让健康 agent 内生压力很高，或攻击者能伪造/放大信号，ratio 不能直接等同于因果证明。
- 不应将仿真中的自动 quarantine 直接用于真实机器人安全关停；应先通过 shadow mode、人工复核、hysteresis 和可撤销降级动作限制 false positive 的任务/人身代价。
- 复现应使用论文 Zenodo 配置，固定动力学、fault injection、KNN、loss model、所有阈值和 random seeds；实现四种 detector，在小 swarm 逐步审计 (H^{int},H^{ext},r_i)、隔离及恢复事件。报告每个场景的 seed 数、置信区间、precision/recall、TCR、损害 AUC 与误隔离成本。
- 推广前需增加异构传感器/电量、移动遮挡、非独立通信丢包、拜占庭欺骗、不同密度与真实硬件对照；对触发阈值、K、扩散/衰减常数做敏感性和 out-of-distribution 测试。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 swarm robotics、分布式诊断和安全验证工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYYF8433.pdf) 核验 §3 的双流 ratio/隔离规则、§4 的试验设计、§5 的表格和 ablation/packet-loss 结果、§6--§7 的局限和未来硬件验证；未把局部仿真结果表述成已经在实体 swarm 上证明的容错能力。
