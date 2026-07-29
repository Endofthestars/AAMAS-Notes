---
title: "Strategic Interactions in Multi-Level Stackelberg Games with Non-Follower Agents and Heterogeneous Leaders"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "resource_allocation"]
dblp_key: ""
doi: "10.65109/KXDZ6376"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KXDZ6376.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02j"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["conceptual_framework", "endogenous_congestion_assumption", "no_algorithm_or_experiment", "ev_infrastructure_policy_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Strategic Interactions in Multi-Level Stackelberg Games with Non-Follower Agents and Heterogeneous Leaders

## 一句话总结

论文提出一个三层、异质领导者的 Stackelberg 概念框架，把不参与市场但会随拥堵调整路线的 non-follower agents 显式纳入；以 EV charging 为例，讨论选址、竞争定价、EV/non-EV 流量如何通过内生拥堵相互耦合。

## 方法与证据

- 框架区别：entrant 可做长期基础设施选址，incumbent providers 只做短期价格决策；EV drivers 是战略 followers，non-EV drivers 不参与充电市场但选择路线并共同塑造拥堵（§2、Figure 1）。
- Level 1 是 EV/non-EV drivers 在价格与拥堵下选择路线/充电；Level 2 是 providers 预期下游拥堵响应来竞争定价；Level 3 是 entrant 预期两层反应来选址（§3）。
- 核心主张是把 non-followers 当作外生背景流会扭曲 equilibrium incentives、利润与部署结论；本文通过层级结构表述这种 bidirectional coupling，而不是仅向已有模型加入固定 demand（§1--3）。
- 该 3 页 extended abstract 没有给出明确的 payoff/约束方程、均衡 existence/uniqueness 定理、求解算法、数值实例、基准比较或真实 EV/交通数据结果；因此它是建模框架和研究议程，而非已量化验证的优化方法。

## 适用边界与复现

- 适用性取决于能否准确指定不同 leader 的行动集/时序、driver cost 与行为、交通-充电耦合、流量守恒与均衡概念。任何这些部件的变化都可能改变预测结果。
- non-follower 的“非市场”身份并不等于其利益无关紧要；在实际 EV 基础设施规划中，出行可达性、价格负担、社区影响、弱势道路使用者、配电网约束和数据治理都需要独立建模/审查。
- 文中没有把框架实例化为可复现模型或进行经验验证，不能据此推荐充电站选址、收费或市场进入决策。
- 后续复现/落地应先公布网络、需求、各类 agents 的 utility/choice model、long/short-term timing、congestion function、equilibrium solver 与 existence conditions，再与真实数据、敏感性、分配影响和政策约束交叉验证。

## 与 AAMAS 的关系与核验说明

这是面向拥堵耦合市场的多层博弈建模。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KXDZ6376.pdf) 核对 §1--3 和 Figure 1，并明确记录摘要没有算法、定理或实验评估。
