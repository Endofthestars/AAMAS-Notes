---
title: "Confounding Robust Continuous Control via Automatic Reward Shaping"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "marl_coordination", "applications"]
dblp_key: ""
doi: "10.65109/UUEW5708"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UUEW5708.pdf"
preprint_url: "https://arxiv.org/abs/2602.10305"
code_url: "https://github.com/mateojuliani/confounding_robust_cont_control"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["causal_assumption_scope", "offline_data_confounding", "simulation_evaluation_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Confounding Robust Continuous Control via Automatic Reward Shaping

## 一句话总结

论文从可能有未观测混杂的离线连续控制数据学习乐观状态势函数，再将其用于 Potential-Based Reward Shaping（PBRS）以加速在线 SAC 微调。

## 方法与证据

- 论文的目标是把离线数据中行为策略与转移之间可能的未观测混杂纳入连续控制的奖励塑形；§4 基于 stationary、infinite-horizon Confounded MDP 的 Causal Bellman Equation 学习状态价值上界（Theorem 4.1、§4.1）。
- Algorithm 1 先从离线批次更新观测策略与状态差异模型，再拟合 state potential，并以目标网络稳定训练。该 potential 随后作为 PBRS 项加入在线 SAC 奖励（§4.1–4.2）。
- 论文重新陈述 PBRS 在该 stationary CMDP 设定下的最优策略不变性，并用 Proposition 4.3 的塑形形式连接 learned potential 与在线训练；该性质取决于势函数塑形及建模条件，不能外推到任意 learned reward。
- §5 比较 Causal PBRS、无塑形 SAC、CQL-PBRS、recurrent SAC 与 T-REX-PBRS；环境包含 MuJoCo 与 Adroit Door/Relocate，离线数据来自 Minari，并给出[代码](https://github.com/mateojuliani/confounding_robust_cont_control)。
- 实验通过删除观测空间维度来模拟：离线轨迹的行为者可见被删除维度，但在线代理不可见。作者报告归一化 IQM、mean/median 和每环境 best/final return，并研究被遮蔽维度、conditional-dependence test statistic 与数据专长的影响（§5.1–5.4）。

## 保证范围、局限与复现

- 因果 Bellman 上界与 PBRS 最优策略不变性的陈述受 stationary、infinite-horizon CMDP、离线数据生成过程与论文定义的可观测/混杂结构限制；它不是对任意部分可观测环境、非平稳系统或真实传感器缺失的通用因果识别保证。
- “未观测混杂”实验是以 observation masking 构造。正文也显示：当删除维度对任务回报至关重要时，学到的 causal potential 可能不够有信息量，性能改善会减弱；不同遮蔽维度和数据质量不能互相替代（§5.3–5.4、§10）。
- 使用 expert 离线数据最好，simple/medium/combined 数据的表现不同；因此不能从实验推得任意离线日志都能安全/稳定地提高在线策略。
- MuJoCo/Adroit 回报和 masked-observation 基准不是实体机器人、临床/金融因果决策或安全部署验证。论文将更紧的上界、更多混杂设定和高维图像观察列为后续方向（§6）。
- 复现需固定被遮蔽维度、Minari 数据质量组合、Causal Bellman 模型/目标网络、PBRS 系数、SAC 训练步数和环境级调参；报告 IQM、最终与最好回报，并检查条件独立性/依赖检验，而非只比较单个分数。

## 与 AAMAS 的关系与核验说明

工作连接因果推断、在线决策和连续控制。笔记基于作者公开的 [arXiv HTML 原文](https://arxiv.org/html/2602.10305v1) 核验，并把理论的建模条件、观测遮蔽模拟和经验性能分开记录。
