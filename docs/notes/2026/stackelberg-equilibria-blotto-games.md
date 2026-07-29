---
title: "Stackelberg Equilibria of Blotto Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/ENTM1651"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ENTM1651.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "pure_stackelberg_strategy", "constant_sum_colonel_blotto", "fixed_epsilon_polynomial_time", "discrete_troop_allocation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Stackelberg Equilibria of Blotto Games

## 一句话总结

本文研究两人 constant-sum Colonel Blotto 的**纯策略** leader–follower 均衡：对任意常数 \(\epsilon>0\)，提出多项式时间 \((1+\epsilon)\)-approximation，改进既有 2-approximation；并可找到使 follower utility 至多为最优 Stackelberg 策略下 \(1+\epsilon\) 倍的纯策略。结果建立在离散 troop、已知 battlefield weights 与可精确计算 follower response 的理论模型上，不是对现实竞选、广告、资源竞争或一般多智能体系统的可部署均衡保证。

## 方法与证据

- game 有 \(k\) 个按权重排序的 battlefields，leader \(A\) 分配 \(n\) 个整数 troops，follower \(B\) 分配 \(m\) 个；较多 troops 获胜、tie 偏向 \(B\)，payoff 为赢得权重之和（§2）。文中明确关注 leader 的 pure commitment；constant-sum 下 mixed Nash/mixed Stackelberg 的关系不等同于该纯策略问题。
- 给定 \(A\) 的 allocation \(x\)，\(B\) 在每个 battlefield 的合理选择是投入 \(x_i\) 以赢得该点或跳过，best response 遂成一个带 troop limit 的 subset/knapsack-style DP（§3）。因此其计算前提包括精确 weights、budgets 与 response model；tie rule、连续资源、成本、观察误差或多对手都会改变问题。
- 核心 relaxed best-response 对前 \(p\) 个 battlefields 穷举 subsets，其余按 \(x_i/w_i\) greedy；相对 optimal DP response 的 utility error 至多 \(w_{p+1}\)（Lemma 3.1）。它用 heavier/light partition、重权重离散化和 equal-weight allocations 的结构，枚举 heavy allocation/response statuses，再以 DP 为 light fields 优化。
- 当最优 leader payoff 很大时沿用既有 2-approximation 推得 \((1+\epsilon)\) 比率；其余将最优 payoff 限于 \([w_1,w_1/\epsilon]\)，令 \(\epsilon'=\epsilon/4\)，离散化 heavy weights，并对 fixed \(\epsilon\) 控制 unique heavy weights、reasonable responses 与 DP 状态数。Theorem 1.1 给任意 \(\epsilon>0\) 的多项式时间 \((1+\epsilon)\)-approximation；这里的“多项式”按摘要定义为关于 troops、battlefields 和最大 weight 的多项式，且 \(\epsilon\) 是常数。
- Theorem 1.2 还控制 follower utility：所得纯 leader strategy 的 follower utility 至多为 optimal Stackelberg strategy 下的 \(1+\epsilon\) 倍，补足旧算法仅近似 leader utility 的缺口。摘要只概述证明并称完整细节在 extended version；未报告现实数据实验、实现、运行时测量或有限 \(\epsilon\) 的经验质量。

## 适用边界与复现

- 适合研究可承诺的离散 allocation competition、算法博弈与 leader–follower planning。不能据此声称政治/体育/广告策略有效、社会福利改善，或在不完整信息、非零和、多人、连续预算、随机 tie 或动态学习中同样近似。
- 复现需实现整数 Blotto instance generator、tie-to-follower payoff、exact follower DP、relaxed-response pivot/subset enumeration、heavy/light threshold、\((1+\epsilon')\) weight rounding、equal-weight allocation canonicalization、response-status checks 与 light-field DP；比较 exact small-instance optimum、2018 2-approximation及新算法的 leader/follower utilities、runtime和 memory。
- 应在不同 \(n,m,k\)、weight distributions、tie conventions、\(\epsilon\)、large/zero optimum、near-equal weights 与 adversarial instances 上测 ratio；另测 approximate DP、noisy/private budgets、continuous relaxations、general-sum/multi-player and repeated variants。若用于实际分配，仍需单独处理激励、合法性、公平、风险和人类决策责任。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 algorithmic game theory 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ENTM1651.pdf) 核验 pure-strategy scope、follower DP、relaxed best response、Lemma 3.1、Theorems 1.1/1.2及 fixed-\(\epsilon\) complexity 表述；没有将摘要中省略的完整证明或应用动机写成现实系统验证。
