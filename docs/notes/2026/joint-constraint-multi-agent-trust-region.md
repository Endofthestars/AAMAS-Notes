---
title: "Multi-Agent Trust Region Policy Optimisation: A Joint Constraint Approach"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["marl_coordination", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/ZOYC2112"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZOYC2112.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04e"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["marl", "trust-region", "kl-budget-allocation", "hatrpo", "mujoco"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Agent Trust Region Policy Optimisation: A Joint Constraint Approach

## 一句话总结

本文将 HATRPO 的每 agent 固定 KL trust-region 改为共享总 KL budget：HATRPO-G 按预计改进/KL 比率排序更新，HATRPO-W 以 KKT 条件分配阈值，试图把更大 policy step 给高影响 agent。

## 方法与证据

- 原 HATRPO 对每 agent 设同一 $\max D_{KL}(\pi_i\Vert\bar\pi_i)\le\delta$；本文把约束换成各 agent 最大 KL 之和不超过 $\delta_{total}$，同时保留 sequential optimization（§4）。
- Greedy 方法重复求每位候选 agent 的局部改进并以 improvement/(KL+$\epsilon$) 选择下一个；W 方法通过 KKT 优化 joint threshold assignment。两者都确定 update order 和 agent-specific KL bounds（§4）。
- 在矩阵游戏、双峰微分游戏与 Multi-Agent MuJoCo 上，图 5 报告 HATRPO-G 相对 HATRPO 最终表现 +25.2%、HATRPO-W +22.5%；G 方差较 W 高 39%。论文还报告二者更快达到 99% 最大奖励，训练时间与基线相近（§5）。

## 适用边界与复现

- 保证的对象是固定总 KL 下的优化/实验回报，非真实多机器人安全或全局最优保证；KL 与 advantage 的估计噪声、agent order 和超参数都可能改变分配效果。
- 复现需公开 HATRPO critic/policy 实现、total KL/每步求解、KKT 目标、greedy score、update order、矩阵/微分游戏和 MuJoCo 任务参数、seeds与统计。应比较总样本/计算预算相等的设置，而非只比较迭代数。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZOYC2112.pdf) 人工核对 joint constraint、两种算法和 §5 数值；未把经验收益外推为所有异构 MARL 场景的稳定性改进。
