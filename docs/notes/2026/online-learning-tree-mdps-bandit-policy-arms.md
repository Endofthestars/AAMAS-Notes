---
title: "On-line Learning in Tree MDPs by Treating Policies as Bandit Arms"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/PYUD1139"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PYUD1139.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["tree_mdp_assumption", "known_reward_assumption", "stationary_opponent_assumption", "gap_dependent_bounds", "simulation_game_evaluation", "baseline_tuning_dependency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# On-line Learning in Tree MDPs by Treating Policies as Bandit Arms

## 一句话总结

本文把有限 Tree MDP 的每个确定性策略视为 bandit arm，却让共享终端状态的策略复用样本，从而以多项式存储/每步计算实现 LUCB‑T（PAC）与 UCB‑T（regret）。其上界按终端状态而非指数多的策略求和；但保证依赖树状可达性、已知奖励、未知但固定的转移/对手和实例 gap，不能直接推广到一般 MDP、非平稳对手或未知回报的在线 RL。

## 方法与证据

- T-MDP 是有限时域、从起点到每一状态恰有一条 state-action 轨迹的树；算法逐回合从根执行完整策略，不能任意生成某个 state-action 样本（§2）。作者的动机是对固定对手求 best response 的完全回忆不完全信息博弈，而非一般图结构 MDP。
- 假定 reward function 已知，待估参数仅为 transition probabilities，并令每条轨迹的 discounted return 有界于 \([0,1]\)（§1–2）。未知奖励、观测噪声、部分可观测状态别名、对手适应或环境漂移均不在理论模型内。
- LUCB‑T/UCB‑T 概念上把策略当 arm；核心是以可到达的 terminal state 对共享观测建立 policy-value confidence bounds，再用 tree 的自底向上优化找到所需 optimistic/pessimistic policy（§3–4）。这避免逐策略维护独立数据，但不表示算法枚举/学习了所有策略的行为分布。
- Theorem 9 给出 LUCB‑T 的期望停止回合数上界，主项为各终端状态的 \(1/(\Delta^\epsilon_\sigma)^2\) 之和及对 \(\delta\)、状态/动作规模的对数项；Theorem 10 对 UCB‑T 给出按 terminal-state min/max suboptimality gaps 的 \(\log T\) regret 上界（§4）。小 gap、罕见终端状态和理论常数仍可能使样本需求很大；这不是无条件或 worst-case 常数保证。
- Lucb‑T‑Uniform 可去掉某一 \(|\Sigma|\) 因子，但须保留每个终端状态的完整结果序列、使用 \(\Theta(t)\) memory，并可能丢弃有信息的非均匀样本；论文报告它在较大问题反而较差（§4.1.4, §5.1）。
- 评测为 2-player zero-sum hidden-information 的 Kuhn Poker、Leduc Poker 与 Reconnaissance Blind Tic-Tac-Toe；后者约有 \(10^7\)/\(2\times10^7\) 个两方状态（§5）。5-card Kuhn 中 Lucb‑T 低于 naive LUCB 的 stopping time，而 3-card 中则相反（Table 1）；这支持规模相关的实证趋势，不是所有小型实例的支配关系。
- Leduc 与 RBT 的 PAC/regret 图分别平均 50/25 次并显示一个 standard error；对手固定为 CFR+ 求出的 \(\epsilon\)-Nash policy（§5.2, Fig. 2）。PAC 的实际 stopping times 过大，作者改画 learning 中的 value gap；因此并未在这些大游戏上直接实证完整 PAC 终止声明。
- PAC 对照 BPI-UCRL、MDP-GapE 由作者实现并调参；具有最佳理论实例界的 MVP、AMB、StrongEuler 未能找到可运行实现。UCB‑T 还与 MCCFR、OPF、UCT 比较，论文承认 UCT 在小问题可有更低 regret（§5.2）。结论应限于该实现、预算和调参条件。

## 适用边界与复现

- 适合作为树状 episodic decision problem 或固定策略对手下 best-response 学习的理论/实验基线；部署前应证明状态历史确实形成树、回报已知、策略空间和终端事件定义正确，并测量深层罕见分支的覆盖。
- 在一般 MDP、动态博弈、未知 reward、连续状态/动作或安全关键系统中，应另用能处理 state merging、非平稳性、回报估计、模型不确定性和约束的算法；本论文的 gap 结果不能替代安全或鲁棒性验证。
- 复现需固定游戏编码与观察历史、固定对手 CFR+ 的 \(\epsilon\)-Nash policy、reward/discount、confidence-bound 版本、PU 优化、\(\epsilon,\delta\)、所有 baseline hyperparameters、随机种子及 episode budget；分别报告 stopping time、value gap、累计 regret、terminal visit counts、内存和计算时间。
- 应补充未知/噪声 reward、非平稳/适应对手、图状 MDP、稀有转移、不同 gap 与更大深度下的消融，并用统一实现/调参预算比较所有可用基线。

## 与 AAMAS 的关系与核验说明

这是将 bandit PAC/regret 分析用于不完全信息博弈所诱导 Tree MDP 的在线规划工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PYUD1139.pdf) 核对 T-MDP 定义、已知 reward 假设、数据共享机制、Theorems 9–10、Uniform 变体、三个游戏与 Fig. 2/Table 1 的评测协议；没有把实例依赖上界或固定对手仿真结果误写成一般 RL 最优性、未知奖励学习或现实部署保证。
