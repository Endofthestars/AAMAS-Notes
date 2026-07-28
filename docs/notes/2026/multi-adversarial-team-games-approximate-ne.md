---
title: "Efficiently Computing Approximate Nash Equilibria in Multi-Adversarial Team Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TBAX6220.pdf"
preprint_url: "https://hal.science/hal-04917907v3"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["normal_form_scope", "independent_adversary_assumption", "polynomial_expectation_assumption", "synthetic_experiments"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Efficiently Computing Approximate Nash Equilibria in Multi-Adversarial Team Games

## 一句话总结

论文将单 adversary 的 adversarial team game 扩展为多个相互独立的 adversaries：无通信的同收益 team 对抗每个各自最大化 payoff 的 adversary，并给出 MATG-GDM，在可高效计算混合期望的表示下用多项式时间求 $\epsilon$-Nash equilibrium。

## 方法与证据

- MATG 是 finite normal-form game：team agents 同享对各 adversary payoff 的相反和，但各 adversary 有独立 payoff 与独立 mixed strategy；它不是 adversary 可协调的 two-team game，也不是 Markov/sequential model。NE-GAP 取所有 team member 和 adversary 的单边偏离收益上确界（§2）。
- 算法每轮计算每个 adversary 对当前 team strategy 的 pure best response，team 各 agent 做 projected gradient step；随后解 LP（ExtendNE）得到 adversaries 的策略，并检查 NE-GAP（Algorithm 1、§3）。团队动作独立且无显式 coordination 是模型前提，不是算法自动学习通信策略。
- Theorem 3：在 Assumption 1（任意 mixed profile 的 expected utilities 及相对自身 mixed strategy 的 partial derivatives 均可多项式时间计算）下，MATG-GDM 最多 $\mathrm{poly}(\Gamma)/\epsilon^4$ 轮得到 $\epsilon$-NE，且每轮为多项式时间，因此构成 FPTAS（§3–4）。对指数显式 normal form 或无法计算期望/梯度的压缩表示，此结论不直接适用。
- 证明把 MATG 转为允许 adversaries 相关的 CA-MATG（一个 macro-adversary，payoff 为各 adversary payoff 之和），再将该 equilibrium 的 adversary marginals 映回原 MATG。Theorem 7 说明 CA-MATG 的 $\epsilon$-NE 可诱导 MATG 的 $\epsilon$-NE；Theorems 10–11/Corollary 12 将单 adversary GDM 的迭代界改写为原始 $\Gamma$ 的多项式，避免 macro action space 随 adversary 数指数增长（§4）。
- 该独立性很关键：更广的 two-team games 中第二团队可相关/协调，文中明确指出其 equilibrium 计算已知不可解；Proposition 16 只讨论一类允许 maximizer correlation 的特定两团队变体，不能推广为一般 team-vs-team tractability（§5）。
- 实验在 team/adversary payoff 独立均匀随机的 MATG 上进行，Python/JAX 实现；与 Gambit 的 global Newton 与 Wilson solver 比较，改变 team 数、adversary 数（含 $m\in\{1,3,6,9\}$）和 action 数。运行上限为 100,000 iterations，报告 NE-GAP/终止迭代；作者观察到其规模随独立 adversary 数增长较好（§6、Tables 3–4、Figure 1）。这不是反偷猎、机器人或 hider-seeker 的实环境验证。

## 局限与复现

- FPTAS 是特定 normal-form MATG 的计算结论，要求 team 同目标、adversaries 独立、有限动作和 polynomial-expectation property；策略相关、team 内通信、部分可观测、学习未知 payoff、连续动作、动态转移或多阶段 Markov game 都超出本文定理。
- $\epsilon$-NE 仅限制单边偏离的 gain。它不保证 social welfare、鲁棒性、global team-maxmin optimality、收敛到唯一 equilibrium，亦不代表对手会采用独立 mixed strategies。
- CA-MATG proof tool 使用相关 macro-adversary，但最终映回依赖 marginal argument；不能把实现中的 correlation 解释为原 MATG 对手间可通信。复现应单独验证 NE-GAP 的所有单方偏离。
- 实验 payoff 为随机合成表；硬件、步长 $\eta$、精度 $\epsilon$、初始化和 iteration cap 会显著影响实际时间。论文亦报告较小 $\epsilon$ 时部分配置触及上限，故经验“scalable”不等于任意参数立即收敛。
- 复现应记录 MATG encoding、Assumption 1 的期望/梯度实现、各 adversary BR、simplex projection、LP solver/tolerances、$\eta,\epsilon$、seed、迭代上限和 NE-GAP；并对 explicit normal-form size 与 CA-MATG 指数 action-space 基线分别报告内存/时间。

## 与 AAMAS 的关系与核验说明

该文提供竞争与团队协作并存的一类多 agent equilibrium 计算边界。笔记依据作者公开的 [HAL 预印本](https://hal.science/hal-04917907v3) 核对 MATG、Assumption 1、Theorem 3、CA-MATG 映射与实验；所有算法保证均限制为独立 adversaries 的 normal-form 表示。
