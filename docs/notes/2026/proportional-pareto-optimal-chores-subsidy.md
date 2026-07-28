---
title: "Proportional and Pareto-Optimal Allocation of Chores with Subsidy"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/UYKY7130"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UYKY7130.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["additive_disutility_assumption", "bounded_cost_normalization", "subsidy_budget_scope", "pareto_vs_fairness_scope", "not_strategyproof", "implementation_data_gap"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Proportional and Pareto-Optimal Allocation of Chores with Subsidy

## 一句话总结

本文研究带不同权重的 agent 如何分配不可分 chores，并以现金 subsidy 弥补比例性（PROP）缺口。对 additive disutility、每项对每人至多为 1 的实例，作者给出 polynomial-time 算法：输出 integral、fractionally Pareto-optimal（因而 Pareto-optimal）的 allocation，且总 PROP-subsidy 至多 \(n/3-1/6\)，与此前最佳已知上界相同。该结果是规范性分配模型中的最坏情况保证，不是实际补偿预算、报告真实性、劳动法合规或所有公平概念的保证。

## 方法与证据

- 输入为 chores \(M\)、agents \(N\)、权重 \(w_i>0\)（和为 1）及 additive nonnegative disutility \(d_i\)；PROP 要求 \(d_i(A_i)\le w_i d_i(M)\)（§1–2）。论文假定每个 chore 对每位 agent 的 disutility \(d_i(c)\le1\)，可通过统一 scaling 规范化；结论随该单位缩放，不能脱离成本量纲解读为固定金额。
- 对 integral allocation，agent 的 PROP-subsidy 定义为 \(\max(0,d_i(A_i)-w_i d_i(M))\)，目标是最小化总额。论文给出等权、相同 chores 的 \(n/4\) 级别 lower-bound example；其 \(n/3-1/6\) 是 general unequal-weight setting 的可保证 upper bound，并非声称精确最优或对每个实例都需该金额（§1, §2.2）。
- 算法先解 proportional fractional allocation 的 LP，并取 acyclic consumption graph；由 dual 取得 payment vector，使其构成 market equilibrium（Theorem 2, §3–4）。市场 payment 是证明和 reduction 工具，而非 agent 实际支付、市场价格或真实货币 transfer 的行为模型。
- market equilibrium 的 First Welfare Theorem 给出 fractional Pareto optimality（fPO）。作者仅把 fractional support 上的 chores 进行 rounding，因此所得 integral allocation 与同一 payments 仍构成 equilibrium，进而是 fPO、亦为 PO（Theorem 1, 5）。PO 仅表示不存在另一 allocation 让所有 agent 的 chore disutility 不增且至少一人严格降低；它不意味着无嫉妒、机会平等或对每个个体的比例补贴为零。
- Theorem 3 用 minimum-pain-per-buck/payment 将 rounding 问题规约为所有 agent 具有相同 disutility 的 bounded instance，并证明原实例的 rounding cost 不会超过规约实例。接着将 acyclic consumption graph 拆为小树，独立 rounding（§3, §5）。这是离线已知 disutility 的构造，不处理估值噪声、主观成本不可比、动态任务到达或 agent 策略性虚报。
- Theorem 4 对上述相同 disutility、acyclic graph 情形在 \(O(m+n^2)\) 时间找 rounding，rounding cost 至多 \(n/3-1/6\)。组合 Theorem 2–4 后，Theorem 5 给出 polynomial-time integral fPO allocation，且 \(\sum_i\max(0,d_i(A_i)-w_i d_i(M))\le n/3-1/6\)。作者表述的是上界和存在/计算结果，未报告大规模工程 benchmark、实际付款执行或金额分布。
- 论文明确方法的 reduction 依赖 chores：把 disutility 调整为与 payment 成比例是降低数值；对 goods 需要增大 utility，可能破坏 boundedness，因此该技术未直接扩展到 goods（§6）。未来还包括 non-additive disutilities、goods-and-chores mix 及 MMS/APS 等公平概念。

## 适用边界与复现

- 适用于任务、废弃物责任等可被预先枚举、成本可加且有可解释权重的离线分配。使用前应核验 1-unit normalization、权重来源、每人每项成本，以及是否允许真实可兑现的补偿。
- 不应把“PROP with subsidy”说成无嫉妒、无不平等或无需人工协商。补贴机制还需预算约束、税务/劳动法规、支付时点、不可转让性、隐私、申诉与反操纵设计；若 agents 可虚报 disutility 或权重，本文没有 strategyproofness 保证。
- 复现应实现 Theorem 2 的 LP/dual 与 acyclic-support conversion，验证 market-equilibrium equality，按 Theorem 3 建立规约，依 §5 的 tree decomposition/rounding 计算 cost，并逐实例检查 PROP-subsidy 与 Pareto dominance。应将输出同 MILP 小实例最优、旧 \(n/3-1/6\) 方法及 \(n/4\) lower-bound family 比较。
- 对部署应额外评估实际总预算、个体补贴尾部、任务技能/容量约束、时间与质量依赖、动态重分配、错误成本和参与者反馈；这些约束可能使理论 allocation 不可执行或改变公平判断。

## 与 AAMAS 的关系与核验说明

这是 AAMAS fair division/resource allocation 的理论工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYKY7130.pdf) 核验了 weighted additive chores model、PROP-subsidy 定义、\(n/4\) lower-bound context、market-equilibrium/reduction/tree-rounding pipeline、Theorem 4–5 的 \(n/3-1/6\) 保证及 goods 不可直接迁移的限制；没有将 fPO/PROP-subsidy 写成真实支付、策略真实性或广义公平认证。
