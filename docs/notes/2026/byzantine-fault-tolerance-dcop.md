---
title: "Byzantine Fault Tolerance in Distributed Constraint Optimization Problems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "norms_trust_governance", "resource_allocation"]
dblp_key: ""
doi: "10.65109/JZVR6522"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JZVR6522.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synchronous_message_passing_assumption", "replica_majority_assumption", "random_byzantine_attack_evaluation", "faulty_agents_cannot_directly_control_assignments"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Byzantine Fault Tolerance in Distributed Constraint Optimization Problems

## 一句话总结

本文定义 FT-DCOP，并将 Max-Sum 与 per-variable replication/同步验证结合为 Repl-Max-Sum；在每个 utility function 的知情 replica 多数正确、每组至少 `2k+1` replicas、故障 agent 不可直接改变变量赋值的条件下抵御最多 `k` Byzantine replicas。随机恶意消息实验显示其恢复无故障 Max-Sum 的结果，但通信量约可达九倍。

## 方法与证据

- FT-DCOP 显式区分 correct/faulty agents，目标是在不预知故障身份时让正确 agent 求解；Theorem 4.2 表明若知晓任一 utility function 的 agent 集合中正确数不超过故障数（`g ≤ 2k`），不存在 `(g,k)`-complete algorithm（§4）。
- Repl-Max-Sum 为变量复制，synchronous multicast 后用 deterministic Max-Sum message 的一致性/多数验证过滤故障 replica；设每 replica set 至少 `2k+1` 且至多 `k` faulty，借此避免直接使用 Byzantine consensus（§5）。
- 在 graph coloring 和 truck appointment scheduling 中，故障 agent 对 q/r message 发送经归一化的随机值，fault 数到 `n/3`；比较标准 Max-Sum 和 Repl-Max-Sum 的解质量、收敛迭代与消息数（§6）。
- 论文报告 Repl-Max-Sum 的结果与 fault-free Max-Sum 相同，而标准 Max-Sum 易受扰；代表设置 `n=24,b=0` 下每 iteration 约 1301.5 vs 144.6 messages，即约 9 倍开销（§6）。

## 局限与复现

- 保证依赖同步消息、复制集多数、确定性消息及故障不直接操纵最终变量 assignment；作者明确若恶意机器人可无视计算结果改动作，FT-DCOP formulation 未必适用。
- 实验攻击只是随机消息，不覆盖协同/自适应、equivocation、延迟/丢包、Sybil、网络分区或 resource exhaustion；不能以此宣称现实分布式系统已具 Byzantine 安全。
- replica/multicast 通信与同步等待在大规模/低带宽系统的延迟、成本和可用性需要独立衡量。复现应公开 factor graph、replica placement、seed、攻击策略、timeout 与完整消息/延迟分布。
- 作者提出真实应用的更广实验与直接操纵赋值的情形为 future work（§7）。

## 与 AAMAS 的关系与核验说明

该文连接 DCOP、容错和分布式多智能体优化。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JZVR6522.pdf) 核对 FT-DCOP、Theorem 4.2、Repl-Max-Sum 的前提和实验通信开销；未把随机故障实验外推为通用 Byzantine security 认证。
