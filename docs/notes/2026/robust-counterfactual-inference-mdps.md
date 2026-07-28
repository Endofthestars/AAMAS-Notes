---
title: "Robust Counterfactual Inference in Markov Decision Processes"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "planning_scheduling", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/TXUQ4572"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TXUQ4572.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["counterfactual_causal_model_assumptions", "known_transition_probability_requirement", "no_unobserved_confounders", "medical_case_study_not_clinical_validation", "worst_case_robustness_not_real_world_safety"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Robust Counterfactual Inference in Markov Decision Processes

## 一句话总结

本文不固定单一 SCM（如 Gumbel-max），而对所有与给定 MDP transition 与观测路径相容的 Markovian causal models 求 counterfactual transition 的 tight interval bounds，再以 pessimistic value iteration 求最坏情形回报最优的 policy；它降低了特定因果机制假设带来的脆弱性，但依赖已知离散转移概率、无未观测混杂等条件，不能把 interval policy 或 Sepsis case study 当作临床因果结论或安全部署许可。

## 方法与证据

- 给定观测 path 中的 transition (s_t,a_t\to s_{t+1})，目标是问若干预到 (\tilde s,\tilde a) 会到达 (\tilde s') 的概率。MDP 可表为 (S_{t+1}=f(S_t,A_t,U_t)) 的 SCM；同一 observational/interventional distribution 一般对应多个 SCM，因此单个 Gumbel-max 机制的 CF probability 不可由 MDP 唯一识别（§2--3）。
- 基于 canonical SCM 的 partial CF inference，作者在 MDP（Markovian、无 unobserved confounders）情形将原本随 MDP 大小指数增长的优化约束化为 counterfactual transition probability 的 exact analytical lower/upper bounds，并按 observed/counterfactual state-action support overlap 和 stability/monotonicity 情形分段推导（§3--4、Theorem 4.2 等）。
- 对每个时间步/transition 的 bounds 构成 interval counterfactual MDP（ICFMDP）。该 ICFMDP 恰好包含与模型/观测兼容的 CFMDPs、而非引入额外伪模型；以 robust/pessimistic value iteration 优化所有允许 CFMDP 中的最坏期望 reward，获得 robust CF policy（§5）。
- 评测覆盖 GridWorld（(p=0.9,0.4)）、Sepsis、Frozen Lake 与 Aircraft。对 100 条 random-policy observation paths 的 worst-case value，论文报告 ICFMDP policy 在五个环境都高于 Gumbel-max（Table 4）；构造 ICFMDP 在五个案例中比 Gumbel-max CFMDP 快 4--251 倍（Table 6）。
- 结果并非所有具体路径都优势：在 Sepsis 的 catastrophic path，Gumbel-max 平均回报可较高，但二者下端均很低；作者的主张是 worst-case causal-model robustness，特别在高随机环境中更稳健，而非每条 path 的平均最优（§6.2--6.3、Figure 5--7）。
- counterfactual stability/monotonicity 会略收紧 bounds；论文比较 CS+M、CS-only 和 none，称 relaxing assumptions 多数环境中略降 policy performance，但仍优于 Gumbel-max 的 worst case（§6.4、Table 5）。

## 安全边界与复现

- “tight”指在论文指定的 compatible Markovian SCM 集合内的识别区间，不替代对真实因果结构的验证。若有 hidden confounding、部分可观测、时间非平稳、连续状态、错误 reward、policy-dependent selection 或 transition estimation error，允许集合与保证都可能失效。
- 主文假定可访问 MDP transition probabilities；作者明确承认从 data 估计时 counterfactual policy 可能对 misspecification 敏感，未来才考虑 confidence-interval uncertain MDP、POMDP 与 continuous state（§7）。
- Sepsis 是 MDP benchmark/case study，非对真实患者、治疗方案、临床数据或临床工作流的验证。反事实 policy 不应直接用于诊断、处方、分诊或资源分配；需临床因果识别、数据治理、外部验证、prospective protocol、监管审查、医生监督与保守 abstention。
- 最坏情形 robust value 只在预定义 interval/奖励中保证下界，可能牺牲平均回报，也不覆盖执行故障、延迟、患者偏好、公平、成本或不可逆伤害。应同时报告 SCM assumptions、bounds width、optimistic/pessimistic policies、reward sensitivity、OOD/hidden-confounder stress tests 与 harms/fairness analyses。
- 复现应固定每个 MDP 的 (P,P_I,R)、observed paths、CS/monotonicity assumptions、closed-form case handling、ICFMDP solver/IntervalMDP.jl version、value-iteration tolerance、sampling counts（200 CFMDPs、每个 10,000 paths 等）及 parallelism；并比较 Gumbel sampling error 与 exact interval runtime，避免把 simulation returns 当作现实因果效应。

## 与 AAMAS 的关系与核验说明

这是 causal/counterfactual inference、robust MDP 与 offline policy analysis 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TXUQ4572.pdf) 核对 canonical-SCM 设定、闭式 bounds、ICFMDP/pessimistic value iteration、五个案例、Table 3--6 与 future-work limitations；没有把形式化区间鲁棒性或 Sepsis 实验表述为临床安全、真实因果识别或部署建议。
