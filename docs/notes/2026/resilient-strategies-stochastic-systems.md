---
title: "Resilient Strategies for Stochastic Systems: How Much Does It Take to Break a Winning Strategy?"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["safety_verification", "planning_scheduling", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/JAGQ1479"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JAGQ1479.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04i"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["stochastic-games", "mdp", "strategy-resilience", "disturbance-model", "formal-verification"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Resilient Strategies for Stochastic Systems: How Much Does It Take to Break a Winning Strategy?

## 一句话总结

本文为带 reachability/safety 目标的 MDP 与 stochastic game 定义策略韧性：以扰动多少次可使原本满足概率阈值的策略失效为 breaking point，并在无限扰动时改以扰动频率刻画，给出评估和最优韧性策略合成算法。

## 方法与证据

- 扰动表示对 agent 已选动作的干预（如 actuator fault）；分别定义 expected 与 worst-case 的 transient breaking point，并在有限次数不足以破坏时以平均/频率 breaking point 继续比较（§1、§3）。
- 对固定 memoryless 策略，expected 指标可化归为 induced MDP 上的 stochastic shortest path 或 MEC collapse 后的 mean-payoff/SSP；论文给出多项式判定（§4、Table 1）。
- 为合成最大韧性策略，构造由 agent 选动作、对手选择正常或扰动转移的 stochastic game；expected synthesis 的难度与 stochastic-game SSP 相关（§4.2）。
- worst-case transient 的评估与合成使用逐次 LP/QP，给出 PSPACE 上界；必要时策略需记录剩余扰动数，而 infinite-disturbance 的 frequency case 对相应 reachability 情形可采用 memoryless disturbance strategy（§5、Table 1）。

## 适用边界与复现

- 论文假设显式给定或经学习获得的模型、对称且同成本的间歇扰动、概率阈值及 safety/reachability objective；不保证对未建模分布漂移、部分可观测或真实机器人故障的安全认证。
- 复现需公开 MDP/SG 状态、动作、正常与扰动 transition、目标集和阈值、disturbance cost、breaking-point semantics、MEC/SSP/LP/QP 实现与数值容差。作者把 POMDP、多 agent 与其他 objective 列为未来工作。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JAGQ1479.pdf) 人工核对两类 breaking point、算法化归、复杂度表和 memory requirement；未将理论韧性分数表述为部署环境中的实际故障保证。
