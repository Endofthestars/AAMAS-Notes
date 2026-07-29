---
title: "Interactive Bayesian Deception under Strategic Timing"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/GUCM1758"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GUCM1758.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["stylized_game_assumptions", "separable_utility_assumption", "bayesian_prior_specification", "commitment_assumption", "infinite_belief_space", "no_empirical_deception_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Interactive Bayesian Deception under Strategic Timing

## 一句话总结

论文建模一名知情 Principal 通过设计变点前后信号来影响 Agent 何时宣告随机 change point，而 Agent 同时可选择停止时间与主动探测控制的动态 Stackelberg 博弈。对固定信号，Agent 的最优停止是广义单侧阈值规则；Principal 的最优收益可化为终端后验信念效用的 concave closure。结果是理论性信息设计刻画，金融评级等仅为动机示例。

## 方法与证据

- 状态 change point \(\Lambda\) 服从双方已知的零修正几何先验。Principal 承诺信号 kernels \(\pi\)，Agent 根据历史形成 posterior，并选择 stopping time \(T\) 和适应性的 probing/control \(F\)，以平衡 false alarm 与 detection delay；Principal 的效用可偏好更晚/更早检测（§1--§2）。
- 这是两层 endogeneity：信号过程由自利发送者选择，接收者又能改变观测质量。均衡为 Principal 先行的 Stackelberg 结构，不涵盖发送者无法承诺、双方同时学习、多个接收者或对手可观察 Agent 私有探测的情形（§1.2、§2）。
- Theorem 1：在可分效用与给定 \(\pi\) 下，Agent 用 Wald--Bellman/backward induction 选最小 continuation cost 的控制；最优检测时间由 Shiryaev statistic 对 belief-dependent boundary \(B(\mu_t)\) 的单侧 crossing 决定。边界随 belief/控制变化，非经典固定 CUSUM 阈值（§3--§4.1）。
- Theorem 2：将 Principal 对高维 signaling scheme 的优化约化为可行终端 posterior 分布的优化，最大期望效用为 \(\hat V\) 的 concavification \(\hat{\hat V}(\mu_0)\)。不同于静态 persuasion，被 concavify 的 \(\hat V(\mu_{T^*})\) 已吸收 Agent 的最优停止和主动探测（§3、§4.2）。
- Proposition 1：相对 deception-neutral scheme，严格收益仅当 prior 处 concave closure 严格高于原效用；Proposition 2 指出 Agent 的自适应 probing 会降低 Principal 可达的最大收益，因为其减少可操纵的不确定性（§3）。
- 文中给出有限状态 illustrative example 展示严格 timing-deception benefit；没有仿真基准、金融/网络攻击数据、行为实验或计算求解器评估。作者也指出 countably infinite belief space 使最优 posterior distribution 的显式刻画困难（§3、§5）。

## 适用边界与复现

- 适用于研究型的动态信息设计、变点检测、审计/告警时机博弈，其中先验、效用、信号控制集和探测成本能明确建模，且发送者承诺假设可接受。
- 不应直接据此推断真实金融机构、评级机构或安全告警系统中的欺骗能力：现实包含不完美承诺、监管披露、多人博弈、连续/非平稳状态、模型错设、审计预算与法律约束。
- 复现应固定几何先验、false-alarm/delay/Principal utility、signal alphabet/kernels、control set/cost、belief discretization和终止截断；数值实现 Bellman recursion、阈值边界与 Bayes-plausible posterior splitting，并检查 concavification 的上包络。
- 若用于防欺骗设计，可将结果作为“主动测量能限制信息操纵”的机制洞见，但需要独立的异常检测、审计随机化、可验证日志、披露义务与现实数据压力测试；不能把理论最优策略当作自动指控或执法依据。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的动态博弈、贝叶斯说服和顺序推断论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GUCM1758.pdf) 核验模型、Theorems 1--2、Propositions 1--2、阈值与 concavification 结论及 §5 局限；没有将动机性金融欺骗例子误表述为实证结果。
