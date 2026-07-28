---
title: "Teaching an Old Dynamics New Tricks: Regularization-free Last-iterate Convergence in Zero-sum Games via BNN Dynamics"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/ARUH6291"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ARUH6291.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["two_player_zero_sum_scope", "bounded_unbiased_noise_assumption", "robins_monro_step_sizes", "payoff_metric_not_parameter_norm", "neural_approximation_gap", "benchmark_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Teaching an Old Dynamics New Tricks: Regularization-free Last-iterate Convergence in Zero-sum Games via BNN Dynamics

## 一句话总结

论文将经典 Brown–von Neumann–Nash（BNN）演化动力学用于两人有限零和博弈：以正的即时优势更新策略，不引入 reference policy 或正则系数；对扩展式不完全信息博弈，再以对手到达概率加权 counterfactual advantage。其 BNN Actor–Critic（BNNAC）用 actor、critic 和 reach 三个网络近似该更新，在 BRPS、Kuhn Poker、Leduc Poker 及其非平稳变体中相对 APMD/R-NaD 报告较低或更稳定的 NashConv。理论结论依赖无偏、有界方差反馈和 Robbins–Monro 步长：迭代稳定在随噪声尺度为 \(O(\sigma)\) 的均衡邻域，并非任意神经训练或一般多智能体环境的精确收敛保证。

## 方法与证据

- 正规式设定是有限动作的两人零和博弈。BNN 将每个动作相对当前混合策略的正优势 \([u_i(a)-\bar u_i]_+\) 注入策略，并从现有概率质量中按全部正优势回流（§2.3）。它保持 simplex，且该结论针对零和/negative semi-definite 结构，不直接覆盖一般和、合作或多玩家博弈。
- 带噪离散更新用观测 payoff \(\tilde u=u+\xi\)。Assumption 1 要求 \(E[\xi]=0\) 且方差一致有界；由于正部算子凸，期望更新还含 Jensen 型 structural bias（§2.4、§3.1）。采样有偏、重尾、相关或 critic 系统性错误时，论文的噪声分析不能直接成立。
- Theorem 1 在 \(\sum_t\eta_t=\infty,\sum_t\eta_t^2<\infty\) 下，以 payoff/regret Lyapunov potential \(\Gamma\) 给出 almost-sure \(O(\sigma)\) 邻域稳定；Theorem 2 对 \(\eta_t=c/(t+t_0)^{2/3}\) 给出到该噪声地板前的 \(E[\Gamma(\pi_t)]=O(t^{-2/3})\)；Theorem 3 将有偏固定点的 \(\Gamma\) 位移界为 \(O(\sigma^2)\)（§3.2–3.3）。这里的收敛度量是 exploitability/regret 型 payoff measure，而不是策略参数或网络权重的普通范数收敛。
- 扩展式版本把每个 information set 的 counterfactual advantage 乘以对手 reach probability；该权重决定局部偏离对全局博弈的影响（§4.1）。Theorems 4–6 给出对应的 \(O(\sigma)\) 稳定/速率和 \(O(\sigma^2)\) bias 描述，推导同时利用 simplex 内部的正到达概率；未覆盖不满足这些条件的表示、探索机制或估值器。
- BNNAC 使用 logits actor、payoff critic 和 opponent-reach 网络；critic/reach 高频更新，actor 每 \(K\) 步按估计 advantage/reach 更新，softmax 保证策略在 simplex 内（Algorithm 1，§4.3）。这是一种把连续/表格动力学嵌入神经近似的实现，论文没有给出深网络函数逼近误差下同等的端到端收敛定理。
- 实验对正常/四动作 Biased RPS 使用表格实现，对 Kuhn/Leduc Poker 使用完整神经实现；非平稳 RPS 改变三组 matchup payoff，非平稳 Kuhn 改变 bet size。论文报告 BNN 方法在 payoff 变动后维持较低 NashConv、相较正则化基线适应更快或振荡更少（§5）。stationary 情况下作者也说明 R-NaD 偶尔有更低的渐近 NashConv，而 BNN 的理论预测含 noise plateau。

## 适用边界与复现

- 适用于需要两人零和、last-iterate 而非时间平均的模拟博弈学习研究，特别是 payoff 随时间变化且不希望调正则/参考策略超参数的场景。
- 不应从该结果推出“无正则就对任意对抗性 RL 更稳健”。先验证零和 payoff、有限动作/信息集表示、feedback 的无偏和方差、步长调度及 counterfactual reach 估计；一般和、多玩家、部分可观测连续控制和非平稳机制本身都会改变保证。
- 复现应固定 BRPS/BRPS-W payoff、噪声分布与种子、RPS 转换速度（1250/2500 steps）、Kuhn/Leduc 规则、三网络架构/优化器、actor 更新周期 \(K\)、所有步长及 APMD/R-NaD 的正则强度和切换频率；报告 NashConv 均值、方差和 transition 后恢复时间，而非只报最佳单次曲线。
- 部署前应额外评测 biased/correlated/replay-induced feedback、critic/reach 校准误差、近零 reach、不同动作规模、连续动作和多玩家/一般和对局；对安全或高风险对抗决策仍需外部约束、性能监控和 fallback，不可把小型扑克/RPS benchmark 当现实安全验证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 关于演化博弈动力学、零和多智能体学习和神经 actor–critic 的工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ARUH6291.pdf) 核验 BNN 更新、噪声/步长假设、Theorems 1–6、三网络 BNNAC 以及 BRPS/poker 实验范围；没有将其邻域稳定或基准上的 NashConv 改善表述为通用神经 MARL、一般和博弈或真实系统的收敛与安全保证。
