---
title: "Nanobot Algorithms for Treatment of Diffuse Cancer"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/WHCQ7191"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WHCQ7191.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "theoretical_biomedical_model", "simulation_only", "not_clinical_evidence", "nanobot_capability_assumptions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Nanobot Algorithms for Treatment of Diffuse Cancer

## 一句话总结

本文用二维离散时间趋化随机游走模拟多癌灶纳米机器人递药：KM 只沿内源吸引信号移动，KMA 到达后释放吸引信号加速聚集，KMAR 再以排斥信号把后续机器人从已充分处理的灶点引开。55 个 agent、20 次试验的仿真显示 KMAR 在弥散癌灶安排中兼顾最终处理比例与速度；这只是带强假设的数学/仿真结果，不是人体、动物、药物疗效或临床安全性证据。

## 方法与证据

- 模型为有界二维连续空间、离散时间；每个癌灶是一个点状簇，需求量决定持久内源化学物 M 的强度。agent 在距灶点 \(\epsilon\) 内“plant”，一次性释放治疗药 K；论文明确假定 agent 间没有直接通信（§2）。这把真实肿瘤微环境、血流、组织障碍、免疫/毒性、药代动力学和定位误差抽象掉了。
- 移动由总信号 \(M+A-R\) 的梯度和噪声决定，梯度为零时退化为随机方向；A、R 以瞬时点源扩散并随时间消散，agent 有有限寿命/清除截止时间（§2）。因此“趋化”“扩散”和参数可控性是模型设定，不等同于现有纳米载体在体内可实现的感知、载荷或负趋化能力。
- KM 仅投放 K；KMA 在到达灶点时投放 K+A；KMAR 则依据该点 A 信号相对需求的阈值投放 A 或 R，以避免持续把 agent 吸向已处理灶点（§3）。作者也指出该顺序增加了单个 nanobot 的能力要求，因而越来越具推测性。
- Figure 1 固定 55 个 agents，对三种癌灶/需求排列画出 20 次试验的平均处理比例与标准差，并标示稳定/完成时间。弥散排列下，KMAR 与 KM 有相同最高最终成功率而 KMAR 更快；KMA 处理更快但会过度偏向一处、使其他灶未处理；集中排列下三者都明显优于随机游走且彼此相近（§4）。这些是指定参数和布局下的 simulation comparison，不给置信推断、真实基准或生物实验。

## 适用边界与复现

- 适用于分布式算法、主动粒子和化学信号分配的概念性仿真研究，不能用于诊断、治疗选择、剂量、患者风险评估、监管申报或宣称 nanobot 可安全清除弥散癌症。任何临床相关主张须由独立的药理、毒理、动物和受控人体研究支持。
- 复现至少需实现正文给出的 \(M/A/R\) 浓度、梯度移动、边界重采样、agent 生命周期、三算法的投放规则和 random-walk baseline；公开三种点位/需求布局、完整参数与单位、初始位置分布、随机种子、trial 数、清除时间定义、均值/方差及绘图脚本。扩展版链接到 arXiv，但此笔记只核验了 AAMAS 三页摘要。
- 应做敏感性与失效测试：弱/噪声/延迟信号、错误灶点/需求、异质扩散与流场、障碍物、载荷耗尽、agent 故障、毒性/脱靶累积和多轮治疗。还应比较最优/鲁棒分配规则，并报告对需求估计和阈值的稳定性；“无毒性”“可重复多次处理”等不能由此仿真推出。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多 agent 协调、化学通信和资源分配扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WHCQ7191.pdf) 核验模型、KM/KMA/KMAR、55 agents、20 trials 与 Figure 1 的相对结论；没有把仿真表现写成医学有效性、可制造性、体内可控性或临床建议。
