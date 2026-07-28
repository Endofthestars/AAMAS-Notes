---
title: "Computing Perfect Bayesian Equilibria, with Application to Empirical Game-Theoretic Analysis"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/WQXT1004"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WQXT1004.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["two_player_scope", "zero_sum_proof_only", "general_sum_empirical_evidence", "equilibrium_refinement_definition", "empirical_game_abstraction", "regret_proxy_metric"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Computing Perfect Bayesian Equilibria, with Application to Empirical Game-Theoretic Analysis

## 一句话总结

PBE-CFR 是针对有限两人 imperfect-information EFG 的 CFR 改造：在每个 information set 用 belief-weighted（believed）regret 更新策略，同时从策略构造满足 Bonanno AGM belief-revision consistency 的 belief system，输出 PBE assessment。论文证明两人零和时收敛到 PBE，并在一般和 GenGoof/Bargain 的 empirical EFG 上观察到小 local regret；把 PBE 当作 TE-PSRO meta-strategy solver 时，真博弈 EVAL regret 常比普通 NE-MSS 更快下降。后两项是特定抽象与实验的近似证据，不能等同于任意一般和/多玩家博弈的 PBE 收敛或现实策略质量保证。

## 方法与证据

- PBE solution 是 assessment \((\sigma,\mu)\)：strategy profile 加上各 information set 内 histories 的 belief distribution。论文采用 Bonanno 2011 的 PBE，即 sequential rationality、reachable sets 的 Bayes compatibility、以及基于 AGM belief revision 的 plausibility-order consistency；它比 Kreps--Wilson sequential equilibrium 的 KW-consistency 弱（§1--2）。因此“PBE”取决于此明确 refinement definition，并非所有教材/软件同一 off-path belief convention。
- PBE-CFR 不只最小化经典 counterfactual regret，而是根据当前 \(\mu\) 最小化每 information set 的 believed regret；每次策略更新后 UpdateBeliefs 依 strategy construct plausibility order 并更新 beliefs，以维持 AGM-consistency（§3、Alg. 3.1）。正确性依赖 EFG tree、perfect recall、可构造 beliefs 和算法中的精确 traversal，不是对 learned/sampled policy 的自动后处理。
- Theorem 4.1 给出 worst-case space \(O(|H|\,|A_{max}|^2)\)、time \(O(T|H|\,|A_{max}|^2)\)。相对 CFR 的 refinement 计算增加 \(|A_{max}|^2\) 因子；这仍会随 tree/horizon/action branching 迅速增大，不能把 polynomial 写成大规模可即时求解（§4）。
- 对**两人零和**有限 EFG，Theorem 4.3 及 Lemmas 4.4--4.6 以 Blackwell/regret matching 证明 average strategy 与 consistent beliefs 收敛到 PBE。该理论结论不覆盖本文一般和实验、三人以上、连续/无限 game、function approximation或 Monte-Carlo estimation（§4）。
- 一般和实验以 PrivateGenGoof4/5 的 TE-PSRO epochs 构造约 1,200/800 empirical games；用 PBE-CFR 的每 information-set 非偏离 regret 最大值（worst-case local regret）度量近似。Table 1 报不同 \(T\) 下平均量级 \(10^{-3}\) 至 \(10^{-5}\)，并随 \(T\) 降低（§5.1、Table 1）。这表明这些实例上可行的近似，而不是一般和收敛定理。
- 应用中 TE-PSRO 将 procedural/simulator scenario 的 empirical model 表示为 EFG；PBE-CFR 或 classical CFR 得到的 PBE/NE 作为 MSS 指导 policy-space exploration。model quality 用真 underlying game 上的 EVAL regret，而非直接真实收益、社会福利、公平性或 calibration（§1、§5.2）。
- 在 Bargain/GenGoof4 中，PBE-MSS 的 EVAL regret curves 与 NE-MSS 比较，优势与 information coarsening程度有关；一些较细/较粗 regimes 曲线接近，论文报告 PBE 与 NE 都可近零 regret、并非各实例压倒性优势（§5.2、Figs. 4--5）。
- empirical EFG 由 TE-PSRO 的 policy set/abstraction 产生，best response 使用 DQN approximation。任何更快 EVAL-regret convergence 都对该 response oracle、sampling、tree abstraction、coarsening以及 test games 有条件；不自动证明底层复杂多智能体系统的 equilibrium 已被完整发现（§5）。

## 适用边界与复现

- 适用于有限、两人、perfect-recall、结构已知且能明确提供 history/information-set/action/payoff 的 EFG。先确认所需的 off-equilibrium belief notion就是 AGM-PBE；若需要 sequential equilibrium、trembling-hand/robustness、机制约束或多玩家方案，应另选/验证 solution concept。
- 不要将一般和的低 local regret或 AGM consistency称为精确 PBE、全局 exploitability=0，或行为/制度预测。一般和、approximate Q best responses、有限 iterations和 empirical game abstraction均可留下偏差；应独立报告每 set regret、Bayes/AGM verifier、exploitability、sensitivity to \(T\)、tree coarsening、seeds与 oracle error。
- TE-PSRO regret 是相对**已知真游戏模型**的评价。现实 market/negotiation/security settings 通常没有可查询真 EFG/payoff，并有 incomplete specification、nonstationarity、model uncertainty、human adaptation和偏好/合法性约束；不可由 simulator equilibrium 推导实际激励相容或安全性。
- 规模化需评估 memory/time随 \(|H|,|A|,T\) 的曲线及 timeout，不只报成功实例；对大树应比较 abstraction、sampling/deep CFR/approximate PBE 的误差界与 out-of-sample policy behavior。
- 复现应固定 game generator/parameters、information partitions/coarsening、utility/chance distributions、CFR/PBE-CFR iteration/averaging/regret matching、belief-update/plausibility implementation、DQN BR architecture/training budget、TE-PSRO epochs/policy populations、EVAL true-game protocol、hardware/seeds以及 table/figure aggregate rules。

## 与 AAMAS 的关系与核验说明

这是 extensive-form game equilibrium refinement 与 empirical game-theoretic analysis 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WQXT1004.pdf) 核对 Bonanno AGM-PBE定义、PBE-CFR belief/regret 更新、复杂度、仅两人零和的证明、一般和 local-regret实验以及 TE-PSRO true-game EVAL-regret metric；没有把一般和实验或 empirical-game convergence 误写成所有博弈的精确 PBE、现实收益预测或制度安全保证。
