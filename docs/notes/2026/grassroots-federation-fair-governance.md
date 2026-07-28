---
title: "Grassroots Federation: Fair Democratic Governance at Scale"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/HPKS5194"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HPKS5194.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["eventual_stabilization_assumption", "formal_protocol_not_deployment", "bounded_children_assumption", "no_empirical_governance_evaluation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Grassroots Federation: Fair Democratic Governance at Scale

## 一句话总结

本文为会动态加入、离开、分裂或合并的重叠社区 DAG 定义 persistent 与 eventual representation fairness，并提出 Greedy Fair Protocol（GFP）来维护 sortition assembly；证明是在 admissible、最终稳定的 timed run 和若干简化边界下成立，不是已验证的数十亿人数字民主系统。

## 方法与证据

- federation 的节点是社区、边表示成员关系；个体可属多个社区，社区可属多个父级。小社区直接治理，大社区以抽签选择 rotating assembly（§1、§5）。
- persistent fairness 要求每个 child 在任意时刻保有其按比例取整后的最低席位；eventual fairness 要求结构稳定后，个人参与频率与 child 平均席位渐近趋于比例公平（§6）。
- GFP 维护与参与历史相关的颜色/ratio，出现席位或结构变化时贪心选择“最欠代表”的合格成员；Theorem 7.1 说明 eventual equal personal participation 蕴含 eventual fair representation（§7）。
- Proposition 8.2 与 Theorem 8.4 声称在 eventually stabilizing 的 admissible GFP run 中满足 eventual equitable participation/fairness，同时协议维持 persistent floor（§8）。

## 局限与复现

- 定理不是对持续 churn、敌对 Sybil identity、策略性加入/退出、私密投票、恶意客户端、网络分区或现实政治权力不平等的处理保证。
- authors 明示采用简化假设，例如每 federation 的 child 数上界；assembly size 与稳定性条件也决定收敛。有限时间内公平误差、延迟、消息与存储成本没有实证评估。
- “公平抽签”还依赖身份唯一性、随机源、资格定义、可审计性、程序正义与少数群体保护，这些都不能从席位比例定理推出。
- 复现应实现 timed transition system/GFP，针对 churn/adversarial trace 报告 persistent violation、收敛时间、个人频率误差、通信成本；作者把放宽简化假设等列为未来方向（§9）。

## 与 AAMAS 的关系与核验说明

这是多智能体制度设计与自治治理的形式化协议工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HPKS5194.pdf) 核对动态模型、公平定义、GFP 和 Theorem 7.1/8.4 的适用前提；未将其当作现实政治或链上治理的安全性、合法性或公平性认证。
