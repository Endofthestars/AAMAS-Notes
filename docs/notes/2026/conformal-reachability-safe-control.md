---
title: "Conformal Reachability for Safe Control in Unknown Environments"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SEHD8631.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_terra_safety_audit"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "terra_revise"
spark_consistency: "revised_after_terra"
risk_level: "high"
risk_tags: ["safety_claim_scope", "probabilistic_guarantee", "calibration_assumptions"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "safety_claim_scope"
escalation_verdict: "approved_after_scoped_probability_and_assumptions_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (Spark revision; GPT-5.6-Terra safety audit)"
reviewed_at: "2026-07-29"
---

# Conformal Reachability for Safe Control in Unknown Environments

## 一句话总结

ReCORS 将 split conformal prediction、有限步可达性分析和 actor–critic 训练结合，在明确校准与独立性条件下，为有限地平线安全提供概率性下界。

## 方法与证据

- §3.2 使用 split conformal 构造动力学预测误差的覆盖界；§5.2 将这些界传播到有限决策地平线 `K` 的可达集合。
- §5.3 以可微 surrogate、经验覆盖损失和 RL 损失共同更新代理动力学模型与策略；Algorithm 1 逐步增加安全地平线。
- Theorem 1 的适用条件包括：初始状态 `s0` 从 `ρ` 独立同分布采样，且与校准数据独立。若轨迹级 conformal 覆盖为至少 `1-α`，则针对 `N` 个初始状态样本，以至少 `1-δ` 的置信度给出安全概率下界；推导使用有限样本 Hoeffding 尾界。
- §6 在七个仿真安全控制设置中比较验证安全下界、经验安全率和奖励；Figures 1–6 含地平线变化、非线性规范、消融和奖励—安全权衡结果。

## 安全范围、局限与复现

- 这是有限 `K`、给定校准/可交换性条件下的概率保证，不是确定性硬安全、无限时域保证或真实系统的无条件安全证明。
- “distribution-free”在本文语境中不等于任意分布漂移或 OOD 情况都被保证；可达性与代理模型误差、完全可观测和初始分布假设均影响结论。
- 实验只支持七个仿真设定的经验比较，不能宣称对所有未知动力学或所有基线都更优。复现应固定 `α, δ, K, N`、校准划分、初始状态分布与 §3–6、Algorithm 1、Figures 1–6 的设置。

## 与 AAMAS 的关系与核验说明

该文连接可信自治、保形统计和安全控制。Terra 审计要求将“可验证安全”改为上述条件下的概率性有限时域下界，并明确独立性、可交换性及仿真边界；本笔记已据此重写。
