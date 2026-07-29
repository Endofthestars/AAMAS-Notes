---
title: "SPADE: Sketch-guided Path Planning Augmented with Diffusion Experts"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/RIHP6974"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RIHP6974.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03x"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "sketch-guided-planning", "conditional-diffusion", "behavioral-cloning", "simulated-occupancy-maps"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# SPADE: Sketch-guided Path Planning Augmented with Diffusion Experts

## 一句话总结

SPADE 面向移动机器人的草图式局部路径规划：以条件扩散模型作为训练期专家，为轻量 U-Net 行为克隆策略提供环境条件下的 margin loss，从而试图兼顾新地图泛化与边缘端单次前向推理。

## 方法与证据

- 状态由局部 occupancy grid、起点和目标点三个 $128\times128$ 二值图组成，动作是路径二值图；基础目标为逐像素 BCE 行为克隆（§2）。
- Cond-DBC 训练一个仅对路径通道去噪、并经 FiLM 接收环境状态的条件 DDPM $p(a\mid s)$。冻结扩散专家比较专家路径与预测路径的去噪误差，以 margin loss 辅助 BC；区别于联合建模 $p(a,s)$ 的 DBC（§3）。
- 作者用十张地图的 20,000 条专家示范训练、在未见工业地图的 2,000 例上评估；报告中等 Cond-DBC（1.9M 参数）相对大 BC/SKIPP（31M）APE 低 39.1%、FID 低 33.5%，同时保留实时边缘推理。表 1 也显示不同形状和模型尺寸并非每项指标均占优（§4）。

## 适用边界与复现

- 评估只覆盖 L/U 两类静态、人工验证的轨迹和 occupancy maps；论文把动态障碍与标注工具用户研究列为未来工作，不能据此推出真实仓储的闭环安全性或偏好覆盖性。
- 复现需公开 ROS 2 标注工具、地图划分与 20k/2k 数据生成过程、FiLM-DDPM 噪声日程、$\lambda$、U-Net 容量、FID/APE/$H_d^{19}$ 实现和延迟测量硬件；还应与规划器和动态障碍场景进行闭环比较。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RIHP6974.pdf) 人工核对问题表示、Cond-DBC 损失、数据划分与表 1；该文为 extended abstract，未将摘要中的离线路径指标表述为现场部署结论。
