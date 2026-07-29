---
title: "Pareto-Guided Exploration for Multi-Objective Multiagent Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "resource_allocation"]
dblp_key: ""
doi: "10.65109/AAWR9928"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AAWR9928.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03r"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "pareto-metric-choice", "continuous-control-benchmark", "anchor-count-sensitivity", "team-composition-search"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Pareto-Guided Exploration for Multi-Objective Multiagent Learning

## 一句话总结

MAPLE 同时保留两类信号：每个偏好向量下的 TD3 标量化 actor--critic 学习，以及按团队期望向量回报做 Pareto dominance 的选择。共享 archive 保存“能组成非支配团队”的策略，让中间 trade-off 不因单一偏好下非最优而被丢弃。

## 方法与证据

- 问题是 cooperative MO-Dec-POMDP，团队有向量 episode return，偏好 $\lambda$ 下以 scalarised expected return 训练，但最终以 team outcomes 的非支配集合覆盖 Pareto frontier（§1–2）。
- $K$ 个 anchors 各以 TD3 优化固定偏好；CEM 在 anchor 周围采样局部参数变体；候选团队混合 anchors、variants 与 archive policies，NSGA-II 对其期望向量回报排序。出现在非支配团队的 policies 入 archive，并可刷新 anchor centres（§3）。
- Assurance ItemGathering 的 Table 1（10 seeds）报告 MAPLE HV $0.63\pm0.042$、sparsity $0.018\pm0.01$；MOMAPPO 为 $0.51\pm0.063/0.01\pm0.067$，MO-AIM 为 $0.61\pm0.044/0.021\pm0.033$。摘要还称 Allelopathy 有类似覆盖改善，并指出 anchors 过少限制探索、过多会稀释优化压力（§4）。

## 适用边界与复现

- Pareto coverage 依赖目标缩放、HV reference point、采样的 team compositions 与 archive 容量；更高 HV 不自动对应部署时某个用户偏好的最优策略。将期望回报用于 dominance 也可能掩盖风险/方差。
- 复现需公开环境、目标定义/归一化、偏好 vectors、TD3/CEM/NSGA-II 参数、archive update、team sampling、HV reference point、sparsity 实现、10 seeds 与 Allelopathy 明细。动态偏好、非合作与更大团队仍需额外验证。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AAWR9928.pdf) 人工核对 MAPLE 流程和 Table 1；未将两个连续控制 benchmark 的 front coverage 改进泛化为通用多目标协作保证。
