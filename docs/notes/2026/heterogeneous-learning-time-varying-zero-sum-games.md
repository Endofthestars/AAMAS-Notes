---
title: "Last-iterate Convergence of Heterogeneous Learning in Time-Varying Zero-Sum Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/VFNO5777"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VFNO5777.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "theoretical_zero_sum_game", "decomposable_time_variation", "best_response_opponent", "asymptotic_step_size_conditions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Last-iterate Convergence of Heterogeneous Learning in Time-Varying Zero-Sum Games

## 一句话总结

本文研究异质 learning：row player 用 Mirror Descent（涵盖 Hedge/PGD），column player 对当前策略作 best response。对 \(C_t=A_t+E_t\) 的 decomposable time-varying zero-sum games，若 Nash-policy sets 以速率收敛、扰动 \(E_t\) 衰减且 MD 步长满足 stochastic-approximation 条件，则最后迭代的 semi-duality gap 收敛；周期游戏中 MD 可收敛而 OGDA 失败。结论是对具有 full best-response feedback 的二人零和抽象的条件性理论，不是一般自博弈、多智能体或非平稳现实系统的稳定性保证。

## 方法与证据

- 每轮 row strategy \(x_t\in\Delta(I)\)、column strategy \(y_t\in\Delta(J)\)，column payoff \(x_t^\top C_t y_t\)。game class 要求 \(C_t=A_t+E_t\)：\(A_t\) 的 row Nash sets 有 limiting point并以 \(O(1/t^q)\) 靠近，\(E_t\) 以 \(O(1/t^\epsilon)\) 消失，\(A_t\) 一致有界（Eq. 1, §2）。任意 rapid/non-decomposable/对抗性 payoff variation 不在定理范围内。
- Algorithm 1：对手每轮取针对 \(x_t\) 的 exact best response \(y_t\)，MD 用 \(C_ty_t\) gradient 和 Bregman divergence 更新 \(x_{t+1}\)。这不是两个独立同类 learners 的自博弈；best response 的计算/观测可得性、噪声与近似误差是关键但摘要未分析。
- Assumption 1 要求 \(\sum1/\lambda_t=\infty\)、\(\sum1/\lambda_t^2<\infty\)、\(\sum t^{-\min\{\epsilon,q\}}/\lambda_t<\infty\)。Theorem 1 给 \(V_t(x_t)-v_t^*=o(\lambda_t/t)\)（§3）。这是 semi-duality gap 的渐近速率，取决于正确 step-size/variation rates，非有限时刻、实际 reward或 exploitability 的无条件界。
- 数值部分只生成一个 entries 在 \((-5,5)\) 的 \(100\times200\) limiting matrix，并在 convergent perturbed games 比较 Hedge/PGD 的不同步长；constant step 不收敛、合适衰减步长收敛（Figure 1）。摘要未给 seeds、noise、对手近似、周期游戏实证或与现代 MARL benchmark 的评估。

## 适用边界与复现

- 适合分析 time-varying two-player zero-sum 的 asymmetrical update dynamics；不应据此为 GAN、市场、网络控制、对抗训练或多主体部署宣称收敛/稳定。那些场景可能非零和、多人、部分观测且无精确 best response。
- 复现需实现 decomposable \(A_t/E_t\) generators、Nash-set/\(q\) 与 perturbation/\(\epsilon\) conditions、distance-generating \(\psi\)、exact BR、Hedge/PGD parameterization、\(\lambda_t\) schedules和 semi-duality metric；分别复现 periodic/convergent cases，报告最后迭代、平均迭代、seeds、finite-time gaps及 condition violations。
- 应测 approximate/stochastic BR、bandit gradients、non-convergent/cyclic \(A_t\)、larger/multi-player/general-sum/continuous games、delayed feedback和 misspecified variation rates；明确何时算法切换/重启。实践系统须独立监控策略质量和安全，不能以渐近 theorem 替代验证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 game learning/last-iterate convergence 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VFNO5777.pdf) 核验 decomposable definition、Algorithm 1、Assumption 1、Theorem 1与 Figure 1；没有把限定理论写成一般异质 MARL 或真实时间变化系统的保证。
