---
title: "SIGMAS: Second-Order Interaction-based Grouping for Overlapping Multi-Agent Swarms"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MZXX4786.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["simulation_only", "group_inference"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# SIGMAS: Second-Order Interaction-based Grouping for Overlapping Multi-Agent Swarms

## 一句话总结

SIGMAS 从个体的一阶注意力构造二阶交互表示，在无群组标签训练下联合做轨迹预测和重叠群体的潜在群组推断。

## 方法与证据

- §3 将任务写为从历史轨迹联合建模未来轨迹和潜在群组，训练时不提供群组数或真值标签。
- §4 的双编码器先产生一阶互动，再以 `A^(2)=A^(1)A^(1)^T` 表示互动相似性；可学习门控融合个体和群体嵌入。
- §5 在二阶互动上谱聚类，并在 CVAE 训练中结合轨迹目标与群组正则。
- §6.1 在 AgentPy 合成的双群场景使用 120 条、每条 200 步轨迹，按 100/10/10 划分。Table 3 报告 SIGMAS 的 ARI、NMI、F-score 分别为 0.4045、0.4086、0.6968；比较对象包含 AgentFormer 和只用一阶信号的 SIGMAS_IG。

## 局限与复现

- 实验是两群、每群 12 个体的仿真数据，尚不足以说明真实密集人群或机器人群的泛化性。
- 正文未给出完整代码、随机种子、参数搜索或显著性检验，严格复现仍需原始训练和后处理配置。
- 可从 AgentPy 场景、数据划分、ARI/NMI/F-score，以及 §4–6、Figures 3/6/8/9 与 Table 3 开始核对。

## 与 AAMAS 的关系与核验说明

论文将群体智能中的交互建模扩展到空间重叠的多主体群组识别。Spark 双通道审核独立核对了任务定义、实验表格与仿真边界，结果一致。
