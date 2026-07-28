---
title: "Stable Matching: Dealing with Changes in Preferences"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "safety_verification"]
dblp_key: ""
doi: "10.65109/WMAU9924"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WMAU9924.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["strict_complete_preference_assumption", "two_instance_robustness_only", "no_fairness_or_welfare_guarantee", "computational_gap_general_case", "strategic_preference_manipulation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Stable Matching: Dealing with Changes in Preferences

## 一句话总结

论文研究同一批 worker/firms 在两套偏好实例 \(A,B\) 下都稳定的 matching，并按两侧发生偏好任意置换的人数 \((p,q)\) 给出精确的结构阈值：一侧可任意多人改变、另一侧至多一人改变时，robust matchings 仍是 sublattice 且相关 polytope integral；两侧各至少两人改变时这两个结构性质都可能失败。一般情形给出 \(O(n^{p+q+2})\) XP 算法，因此改变人数为常数时可多项式求解，但 fully general decision threshold 仍开放。

## 方法与证据

- 设有 \(n\) workers 与 \(n\) firms，每名 agent 对另一侧有严格、完整的 total order；matching 在任一实例中无 blocking pair 即稳定。robust stable matching 是同时属于 \(M_A\) 与 \(M_B\) 的 matching（§3.1--3.3）。论文主要研究两实例，尽管部分结论延及多个实例。
- type \((p,q)\) 表示相对 original instance，至多 \(p\) workers 和 \(q\) firms 改变偏好。Theorem 7：在 \((1,n)\)（及对称 \((n,1)\)）时，\(M_A\cap M_B\) 是两边 stable-matching lattices 的 sublattice；一侧完全不变、即 \((0,n)\)，可在多项式时间构造 Birkhoff partial order 并以 polynomial delay 枚举（Theorem 9）。
- Theorem 11 给出对 \((1,n)\) 的同步/跨实例 rejection 的 deferred-acceptance 式算法，求 worker-optimal（对称地 firm-optimal）robust matching或报告不存在。Theorem 12 显示该类的 robust fractional stable-matching polytope integral，因而 LP 也可求解。
- 锐利反例阈值在两边各至少两名 agent 改变：Theorem 6 说明 \(p,q\ge2\) 时交集不一定为 sublattice；Theorem 13 说明 \((2,2)\) 的 robust polytope 不一定 integral。因此不能把原始 Gale--Shapley lattice/LP 的整性无条件延伸到多方偏好变化。
- 对一般 \((p,q)\)，Algorithm 3 枚举发生变化 agents 的 partner assignment、检验/截断偏好并运行 stable-matching procedure；Theorem 15 给出 decision、构造及枚举的 \(O(n^{p+q+2})\) time/delay。由此仅在 \(p+q\) 为常数时是 polynomial；全体 agents 可改变时已有 NP-complete 结果，精确复杂性边界仍是 open problem（Figure 1、§4.4）。

## 安全边界与复现

- “robust”不是对任意偏好漂移、未知未来参与者、缺失/弱/并列偏好、容量/不完全名单、动态到达离开或多实例长期序列的鲁棒性保证；它只要求对输入给定的 \(A,B\) 同时稳定。真实招生、就业或器官交换的变化模型通常不止 arbitrary permutation。
- 稳定性只排除 blocking pair，不保证公平、福利、最低后悔、群体平等、参与者可接受性、透明度、隐私、无歧视或无操纵。worker-/firm-optimal 只是在 robust-stable 集合内对某侧偏好最优，另一侧可能更差；不应将其标作社会最优或公平结果。
- 严格完整偏好与一对一、等规模市场是关键数学前提；将不完整偏好、ties、capacity、合同、优先级、资格限制或不愿匹配者直接塞入该算法会改变定理前提。实际系统须先明确 outside option、合法/资格硬约束和拒绝/申诉路径。
- 偏好可能被策略性报告或由敏感数据推断。用算法重算匹配会暴露/放大这些偏差，亦可能激励刻意改序以改变可行 robust set。应使用经过审计的偏好收集、访问控制、影响评估、反操纵规则、版本记录和人工治理，而非把同时稳定当作自动决策许可。
- 复现或应用需报告 \((p,q)\)、两份完整 preference profiles、tie/缺失处理、是否满足 all changes 的实例定义、DA/LP/XP 实现、枚举延迟和当 \(p+q\) 增大时的实际运行时间；对 \((2,2)\) 及以上禁止假定 lattice/LP integral 结构仍成立。

## 与 AAMAS 的关系与核验说明

这是稳定匹配、鲁棒性与离散结构的理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WMAU9924.pdf) 核对 \((p,q)\) 定义、Theorems 6--7、9、11--15、Figure 1 以及 XP 上界和开放问题；没有把“对两份偏好同时稳定”表述为对现实市场的公平、策略稳定或无限未来变化保证。
