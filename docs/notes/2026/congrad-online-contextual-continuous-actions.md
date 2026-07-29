---
title: "Low Complexity Online Contextual Learning with Continuous Actions"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/TCIC3712"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/TCIC3712.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "online_contextual_learning", "continuous_actions", "iid_contexts", "concave_rewards", "unbiased_gradient_oracle", "theoretical_regret"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Low Complexity Online Contextual Learning with Continuous Actions

## 一句话总结

Congrad 是 continual-action contextual optimization：在固定 \(n\)-dimensional bounded basis policy space 上，按当前 IID context 的 noisy unbiased action gradient 做 kernel-smoothed projected gradient ascent；kernel bandwidth 从宽到窄以先全局、后局部更新相近 contexts。满足摘要列出的 assumptions 时，memory \(O(n)\)、单次 computation \(O(n(k+d))\)（数值积分另计），expected regret \(O(T^{(d+1)/(d+2)})\)，其 \(T\) exponent 与常数 \(B\) 不依赖 action dimension \(k\)。这是对可微 concave reward 与梯度 oracle 的理论，非一般 RL/MDP、黑箱 bandit、非 IID 或真实控制性能保证。

## 方法与证据

- 每轮 context \(c_t\in C\subset\mathbb R^d\) IID from fixed density，action 不影响 future contexts；reward \(r(x,c)\) 对 action concave，agent 得到 \(\nabla_xr(y_t,c_t)+\epsilon_t\) 的 unbiased noisy gradient（§2, Assumptions 1–4）。该 setting 排除 sequential state transition、action-dependent observations、biased feedback、nonconcavity和 adversarial drift。
- comparator 仅是预先设计的 \(\Pi\)：\(n\) 个 orthogonal basis functions 的有界 coefficient linear combination；effective action set 是该 restricted policy class 可实现的 compact set（Eq. 3）。regret 对 \(\pi^*\in\Pi\)，不是所有 measurable policies/global unconstrained optimum；basis approximation error不在主界中消失。
- Algorithm 1 更新 \(\gamma_{i,t}\)，对 current-gradient 按 compact-support kernel \(K_t(c,c_t)\) 在 context domain 积分并投影至 \([-M,M]\)。摘要称 memory \(O(n)\)，而实际 d-dimensional integral 以 quadrature/Monte Carlo 近似时为 \(O(mnk)\) per iteration；原先 \(O(n(k+d))\) 表述不含积分采样/feature evaluation的具体代价。
- Assumptions 5–7 还要求 reward and gradient 对 contexts Lipschitz、basis Lipschitz、kernel mass 在 \(\lambda_t^d\) 常数倍间。取 \(\lambda_t=\eta_t=t^{-1/(d+2)}\)，Theorem 1 给 \(BT^{(d+1)/(d+2)}\) expected regret，\(B\) independent of \(k,T\)，但可依赖 \(d,n,M\)、smoothness、density、noise/basis/kernel constants。
- 无实验部分；应用例（recommendation、cyber-physical、healthcare）只是 motivation。没有对有限 sample constants、basis/kernel choice、large \(d\) curse、gradient estimation、numerical integration、constraint handling、safety或实际 data 的实证。

## 适用边界与复现

- 适合有可靠 gradient feedback 的 static-distribution contextual concave optimization。不要把它直接用于 unconstrained recommendation/exploration、深度 RL、非凸 policy learning、医疗干预或控制执行；高风险 action 需另行约束、安全验证与人类监督。
- 复现需实现 compact \(C\)、density/contexts、concave reward and gradient-noise oracle、basis/\(M\)、kernel/normalization、\(\eta_t,\lambda_t\)、quadrature/MC \(m\)、projection和 \(\Pi\)-restricted comparator；报告 cumulative regret、memory、wall-clock、integral approximation error、\(k,d,n\) scaling、seeds/CI。
- 应测 imperfect/biased gradients、non-IID and shifted contexts、nonconcave rewards、sparse/bandit feedback、constraints/safety sets、high \(d\)、basis misspecification和 kernel sensitivity。报告 action feasibility、worst-case regret和 failures，而非只用 expected regret。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 online contextual learning 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/TCIC3712.pdf) 核验 problem assumptions、Algorithm 1、kernel/basis construction和 Theorem 1；没有把 action-dimension-independent bound 误写为任意连续控制问题的实际效率保证。
