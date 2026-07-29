---
title: "Mitigating Constraint Conflict in Offline RL: An Adaptive Weighted Constraint Approach"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/CYXQ3092"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CYXQ3092.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03s"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "offline-distribution-shift", "mixed-behavior-data", "geometric-median-approximation", "d4rl-benchmark"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Mitigating Constraint Conflict in Offline RL: An Adaptive Weighted Constraint Approach

## 一句话总结

AWC 面向由多个行为策略产生的 offline RL 数据：不同动作约束会把 actor 拉向无效平均。它按动作与当前 actor 的距离加权，过滤低权重样本，并以加权几何中位数训练 constraint network；actor 在 Q 目标与该约束之间折中。作者在 D4RL 九任务中称 5 项最高分。

## 方法与证据

- 对同一 state 的数据动作，权重为与当前 actor action 的平方欧氏距离倒数，随后归一化；仅保留高于阈值的候选，以降低远离当前 policy、可能冲突动作的影响（Eqs. 1--3）。
- constraint target 是候选动作的加权 geometric median，因无闭式解而通过最小化加权距离的 constraint loss 学得；actor loss 是 $-\lambda Q(s,\pi)$ 加上向 constraint output 的二范数正则（Eqs. 4--6）。
- D4RL 10 seeds 的 Table 1：AWC 在 halfcheetah-medium-expert 101.1、walker2d-medium 91.5、walker2d-medium-replay 96.8、walker2d-medium-expert 112.8、hopper-medium-replay 102.1 等 5/9 tasks 的均值最佳；其余任务如 halfcheetah-medium 和 hopper-medium 仍低于某些比较法（§3）。

## 适用边界与复现

- “接近当前 actor”是设计偏置，不保证保留全局高价值但暂时远离的行为；几何中位数对 action geometry、过滤阈值、$\epsilon_w$ 与 $\lambda$ 敏感。离线覆盖不足和 Q 外推误差仍未消失。
- 复现需公开 D4RL version/normalization、state-action grouping、candidate threshold、median optimizer、actor/critic/constraint 网络、所有超参/随机种子及每 task 完整分数。安全关键部署还需独立验证 constraints 而非仅以行为接近作代理。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CYXQ3092.pdf) 人工核对算法和 Table 1；未把 D4RL 竞争分数视作现实安全或多源数据鲁棒性的充分证据。
