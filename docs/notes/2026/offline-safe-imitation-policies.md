---
title: "OSIL: Learning Offline Safe Imitation Policies with Safety Inferred from Non-preferred Trajectories"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "marl_coordination", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AGSA2170.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["offline_learning", "safety_claim"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# OSIL: Learning Offline Safe Imitation Policies with Safety Inferred from Non-preferred Trajectories

## 一句话总结

OSIL 从非偏好轨迹和混合风险离线轨迹中学习安全代价与模仿策略，在 CMDP 框架中权衡任务回报和成本约束。

## 方法与证据

- §3.1 定义多成本 CMDP；数据包括高风险非偏好轨迹和不作单一成本假设的联合轨迹。
- §3.2 学习成本表示；§4.1–4.2 结合模仿损失、成本 critic 与拉格朗日形式训练策略（Figure 2，Eqs. 9–14）。
- §4.3 的 Theorem 1 讨论近似 KL 约束下的性能下界；它不是对真实部署安全的无条件保证。
- Figures 1、3–4 在速度约束和导航任务中比较安全成本与回报；主要汇总使用 5 个种子、均值和 95% CI。
- Figures 5–7 检查非偏好数据规模、对比损失和局部轨迹长度的敏感性。

## 局限与复现

- 性能依赖联合数据包含足够高回报轨迹；较小联合数据集会退化（§5.2）。
- 证据主要来自离线基准和仿真任务，不能外推为真实物理系统的安全证明。
- 正文未给出完整代码可用性、种子和全部超参数；复现应至少核对 §3–5、Figures 1–7 与定理条件。

## 与 AAMAS 的关系与核验说明

工作连接安全约束学习、具身决策与多智能体协调。Spark S1 建立原文证据链，独立 Spark S2 复核了定理适用范围、图表比较与复现边界；未出现需 Terra 升级的冲突。
