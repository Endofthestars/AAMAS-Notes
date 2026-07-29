---
title: "Inequality in Congestion Games with Learning Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/PRIV8934"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PRIV8934.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02s"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "learning_rate_as_advantage_proxy", "simulated_transport_networks", "group_fairness_metric_scope", "not_empirical_equity_causality"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Inequality in Congestion Games with Learning Agents

## 一句话总结

论文在拥塞博弈中令通勤者以不同学习率的 \(\epsilon\)-greedy Q-learning 适应路线，并提出 Price of Learning（PoL）衡量学习期间相对 social optimum 的效率损失、以两个源头群体的平均成本差衡量 source disparity。两源 Braess 网络及 Amsterdam metro 抽象模拟显示：学习率相同则 disparity 近零；不同时，快学群体可持续获益，扩展线路后甚至可能不收敛到 Nash。它提示只看均衡效率会漏掉适应过程，但“学习率”是资源/信息不平等的建模代理，不能直接解释或预测真实社会群体的交通公平。

## 方法与证据

- 定义 \(PoL(t)=C(\pi_t)/C(a^\star)\ge1\)，其中期望社会成本来自当期联合学习策略、\(a^\star\) 为静态 social optimum；source disparity 为两源群体平均成本之差 \(SD(s_1,s_2)\)（§2，式 1--2）。低 PoL 不蕴含零 disparity。
- 每位玩家维护路线 Q table，以学习率 \(\alpha\)、折扣 \(\gamma\) 更新，并用 epsilon-greedy 在探索/利用间选择；学习率异质性是其适应能力、资源或信息差异的抽象（§2）。
- 环境包括加有 fast lane 的 two-source Braess extension，以及按 pre-2018、North-South line 和未来 West-Amstel 三阶段抽象的 Amsterdam metro。边成本为基于 free-flow 时间和容量的函数；时刻表用于自由流时间，网络仍是简化模型（§3）。
- 图 2 表明相同学习率时 source disparity 围绕 0 波动，异质率时更高学习率群体保持优势；图 3 在 metro 扩展后显示持续 PoL/差距，某些率比可阻碍 Nash 收敛。作者因此建议评估扩建时兼顾学习动态并支持较慢适应者（§4）。

## 适用边界与复现

- 学习率不是收入、数字接入、残障、地理位置或真实出行知识的观测量；群体成本差也不涵盖可达性、票价、可靠性、时间价值、安全或程序公平。任何公平解释须有真实分布数据和共同设计。
- Q-learning、固定 epsilon、路线集合、容量/旅行时间函数、起点分组和扩展情景决定结果。现实通勤者会共享信息、受时刻/票价/换乘/拥挤/习惯影响，并可能不符合该独立 agent 模型。
- Amsterdam 是抽象网络而非校准后的 OD demand 或准实验；图示没有完整统计不确定性与稳健性信息，不能作为具体线路项目的因果预测。
- 复现应公开网络、需求、时间/容量、reward、\(\alpha,\gamma,\epsilon\)、seeds 与分组；报告 PoL、所有组成本分布、收敛诊断和置信区间，并对不同信息干预、学习模型、需求扰动和伦理相关群体指标做敏感性分析。

## 与 AAMAS 的关系与核验说明

该文将 MARL 的适应动态引入交通拥塞博弈的效率/公平分析。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PRIV8934.pdf) 人工核对 PoL、source disparity、Q-learning、Braess/metro 环境和图 2--3；未把模拟分组差距误写为现实社会群体的经验证果。
