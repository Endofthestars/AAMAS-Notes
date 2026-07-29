---
title: "Constant-Memory Strategies in Stochastic Games: Best Responses and Equilibria"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/SQOI3711"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SQOI3711.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "stochastic_games", "bounded_memory_strategies", "behavioral_vs_mixed", "theoretical_reductions", "not_practical_marl_solver"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Constant-Memory Strategies in Stochastic Games: Best Responses and Equilibria

## 一句话总结

本文研究 finite stochastic games 的 constant-memory strategies：若对手使用 behavioral \(K\)-memory strategies，则存在 pure \(K\)-memory best response；所有 agent 限于同一有限 \(K\) 时存在 Nash equilibrium。相反，对 mixed constant-memory opponent，赛前随机选一个 behavioral policy 与逐状态随机化诱导策略一般不等价，best responding 可与 infinite-horizon CMDP/POMDP 类难题互相归约。结论界定策略表示的理论差异，不提供一个可扩展、可计算或能训练深度 MARL policy 的算法。

## 方法与证据

- game 有 finite agents/states/actions、stochastic transitions和 discounted cumulative rewards。behavioral \(K\)-memory strategy 从长度至多 \(K\) 的 state/joint-action history 与 current state 映射到 action distribution；\(K=0\) 是 stationary（§2）。best response 被定义为对任何 infinite-memory alternative、从每个 initial state 都不差的策略（Eq. 2）。
- Theorem 3.1：所有 opponents 为相同 finite \(K\)-memory behavioral strategies 时，agent 存在 pure \(K\)-memory best response；Corollary 1 对不同 finite \(K_j\) 给 max-memory response。Theorem 3.2：所有 agents 都采用 finite \(K\)-memory strategies 时存在 NE。摘要不提供 proof algorithms、equilibrium computation complexity、discount/transition representation assumptions或 finite-time learning dynamics。
- mixed \(K\)-memory strategy 是 match 前按 distribution 选一个 behavioral strategy，并在整场保持；这不同于每 state/history 以 mixture probability 随机 action 的 induced behavioral strategy（Definition 2）。Theorem 3.3 说多个 states 时 utility equivalence 一般不成立，故不可把 mixed policy 简化成 state-wise randomized policy。
- Theorem 3.4 将 best response to opponents’ mixed \(K\)-memory profile 归约到 special infinite-horizon POMDP；Theorem 3.5 再将 CMDP optimal solution 归约到 best response against mixed zero-memory opponents。摘要据此称问题可能 even non-computable，依赖已知 infinite-horizon POMDP undecidability discussion；这不是对任意 practical finite-horizon/discretized instance 的直接 runtime lower bound。
- full paper（arXiv）据称另有 IPD、Traveler’s Dilemma、Pursuit experiments与 code，但本笔记只核验 AAMAS 摘要，未复核 full version 的 experiments、proof details或 implementation。

## 适用边界与复现

- 适合 bounded rationality 与 strategy-representation theory；不可把 NE existence 当作 independent learners 学得 equilibrium、memory-constrained agents 可安全协作或 mixed-opponent response 可执行的主张。
- 复现需实现 finite SG、history augmentation、behavioral/mixed strategy semantics、utility calculation和 Theorems 3.1–3.3 的 counter/small examples；对 mixed-zero-memory construction实现 CMDP/POMDP reductions，并区分 exact infinite horizon 与 finite truncation。
- 应报告 instance sizes、\(K\)、state/action cardinalities、discount、strategy support、solver tolerance、time/memory、approximation loss。进一步研究 finite horizon、restricted supports、observability、sampling estimates、approximate best response与 learned finite-state automata，避免把 undecidability转述为所有工程实例不可解。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 stochastic-game/bounded-rationality 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SQOI3711.pdf) 核验 K-memory definitions、Theorems 3.1–3.5 与 behavioral/mixed distinction；没有把归约和存在性结论写成实际 MARL 解法或一般不可计算断言。
