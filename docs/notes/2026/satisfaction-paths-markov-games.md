---
title: "Satisfaction Paths in Markov Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/KCNB4874"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KCNB4874.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "existence_theorem", "stationary_mixed_strategies", "finite_state_action_markov_game", "not_algorithmic_convergence_rate"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Satisfaction Paths in Markov Games

## 一句话总结

本文研究 win-stay, lose-shift 式的 satisfaction path：若当前策略是 best response 则保持，否则允许改变。作者以 grouped satisfaction path 的拓扑分析为桥梁，证明满足凸紧 strategy spaces、analytic payoffs 和所有 subgames 有 equilibrium 的 pure strategy game 存在有限长度 grouped path；再把有限 state/action 的 stationary mixed Markov game 转为 player–state virtual-player pure game，得到从任何初始 stationary mixed profile 到某个 mixed equilibrium 的有限 satisfaction path。它是存在性结论，并未给出可实现的学习算法、寻找路径的复杂度、path length bound 或通用 MARL 收敛保证。

## 方法与证据

- pure game 中 \(\epsilon\)-BR 要求 payoff 不低于最大可得 payoff 减 \(\epsilon\)，\(\epsilon\)-equilibrium 是每 player 均为 \(\epsilon\)-BR（Definitions 1–2）。给定 players 的 partition \(\mathcal P\)，grouped \(\epsilon\)-satisfaction path 只要求：若 group 内所有成员当前都是 \(\epsilon\)-BR，则下一步该 group 的策略不变（Definition 3）；其余 group 如何选下一状态并未规定为一个具体 update rule。
- \(N_\epsilon(s)\) 计数当前全为 \(\epsilon\)-BR 的 groups，\(T_\epsilon(s)\) 是遵守该 stay constraint 的可行后继集（Definitions 4–5）。Theorem 1 在凸紧 strategy spaces、analytic payoffs 下刻画 \(N(s)\) local minimum：已有 BR group 在所有 admissible successor 中仍为 BR。该工具帮助把已固定 groups 视为环境、归约为 subgame。
- Theorem 2 的充分条件还要求每个由任意 group subset、固定其余策略而成的 subgame 都有 equilibrium；由任意 initial profile 存在有限长度 grouped satisfaction path 到 equilibrium。此为对 0-BR/pure-game framework 的存在性定理，不表示每个异步 win-stay/lose-shift implementation、近似 BR、带噪 feedback 或有限 sampling 都会选到该路径。
- 对 stationary mixed stochastic game，作者构造 \((i,x)\) virtual players、各自在 state \(x\) 上选 \(\Delta S_i\) 的 pure game；其 payoff 是从 \(x\) 出发的 discounted return。共享原 agent 的所有 state-indexed virtual players 被放为一个 group。Theorem 3：若每个 \(S_i\) 有限，则任意 initial stationary joint mixed profile 存在 finite-length satisfaction path 至 mixed equilibrium（§3）。
- 摘要没有数值实验、构造性 solver、路径选择策略、runtime/path-length、discount/transition estimation sensitivity或策略 representation 的实践评估。论文称解决先前文献中的 open problem，但本笔记只依据其 extended abstract 核验命题，未独立复核完整证明。

## 适用边界与复现

- 适合 equilibrium dynamics 与 Markov-game 形式理论研究；不能将“存在一条路径”说成 independent MARL、policy gradient、Q-learning、deep MARL 或真实多机器人系统必然收敛，也不能当作有限时间性能、安全或社会稳定保证。
- 复现/审查应形式化 Definition 3 的 admissible successor relation、local-minimum proof、subgame equilibrium premise和 virtual-player mapping；在小型 finite games 中枚举/求解 satisfaction graph、验证初始 profiles 至 equilibrium 的 reachability，并报告 path lengths、branching和计算时间。
- 应研究可计算 path-selection algorithm、worst/expected length、\(\epsilon\)-BR、approximate/noisy best response、asynchrony/partial observability、continuous actions、non-stationary transitions、general-sum reward conflicts 和 non-stationary policies。实际 agent 仍需独立监测 regret/exploitability、constraint violations与安全。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 MARL/game-theory 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KCNB4874.pdf) 核验 Definitions 1–6、Theorems 1–3 和 stationary mixed Markov-game reduction；没有把理论存在性改写成算法、速度或部署收敛结论。
