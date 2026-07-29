---
title: "Incentive-Aware AI Safety via Strategic Resource Allocation: A Stackelberg Security Games Perspective"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["safety_verification", "game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/JUJH9710"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JUJH9710.pdf"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04n"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass"
spark_consistency: "pass_after_terra_boundary_revision"
risk_level: "high"
risk_tags: ["blue_sky_vision", "ai_safety", "strategic_auditing", "payoff_estimation", "strong_attacker_assumption", "cross_domain_transfer", "no_algorithm_or_experiment"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_ai_safety_boundary_check"
escalation_verdict: "pass_after_targeted_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted safety-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Incentive-Aware AI Safety via Strategic Resource Allocation: A Stackelberg Security Games Perspective

## 一句话总结

本文把 AI 安全监督重述为有限资源下的 Stackelberg Security Game（SSG），提出用随机化审计应对训练反馈投毒、把有限人类/弱模型评审分配到不同风险域、以及按任务风险和模型能力进行部署路由；它是一份跨生命周期的研究议程，没有给出新的求解算法、系统实现或实验，因而不能视为 SSG 已经提高 LLM 安全性的证据。

## 方法与证据

- 标准 SSG 中，防御者先承诺有限资源的混合策略，攻击者观察策略后选择目标；每个目标按 covered/uncovered 状态给双方定义 payoff。论文借此把监督者视为 defender，把恶意贡献者、攻击输入或 worst-case failure mode 视为 attacker（§1–2.1，pp. 3887–3888）。
- 训练阶段：攻击者选择要污染的 preference/data items，防御者承诺审计策略；作者强调随机化或多样化审计，以减少固定抽查规律被利用，并提出高影响样本、异常标注者和一致性检查等目标（§3.1，pp. 3888–3889）。
- 评估阶段：把 coding、medicine、law 等域视为不同 payoff 的 targets，把人类专家、弱 LLM 和测试工具视为异质 defender resources；SSG 决定资源分配，jailbreak/red-team 则作为域内战术测试（§3.2，pp. 3889–3890）。
- 部署阶段：把任务或应用域视为 targets，把不同模型/团队的能力、成本、延迟和风险视为资源约束，在恶意输入或最坏失败假设下选择模型路由；作者要求进一步处理在线风险学习与多阶段动态（§3.3，p. 3890）。
- 论文引用物理安全 SSG 的真实部署与成本收益作为动机，但没有给出 AI 管线的已实例化 payoff、求得的均衡或可执行审计策略、部署系统或比较实验结果（§1–2，Figure 1）。

## 安全边界与复现

- 论文明确列出的核心难点包括：在噪声、串谋和数据漂移下用因果影响估计训练数据投毒 payoff，在策略仅部分可观测时部署随机化审计，校准 tail-risk utility 与 failure prior，建模异质审核资源误差，把组合型任务映射成 targets，以及从有限 jailbreak/red-team traces 学习 attacker model（§3.1–3.2）。
- 标准 SSG 假设很强的攻击者能够观察防御策略并选择使自身收益最大的目标。论文指出完整审计策略可观测性并不现实，但管线中哪些样本或标注者会被复查等规律可能被部分学习；固定审计规律的有限泄露仍可能被利用。作者把较弱或更现实 attacker model 下能得到何种保证列为开放问题（§3.1，pp. 3888–3889）。
- 部署场景的任务空间是开放且时变的，失败可能延迟出现或由模型交互产生；标准单阶段、离散目标和目标独立 payoff 假设未必成立。作者把在线学习 payoff 和同时优化部署策略留作研究挑战（§3.3）。
- 从机场、巡逻或野生动物保护中的 SSG 部署成功，不能直接推出其在 LLM 训练、评估和多模型路由中同样有效；参与者可观测性、攻击面、影响测量和反馈速度均不同。
- 实证化至少需要：明确 defender/attacker/action/target、审计预算与可观测性、payoff 获取和不确定区间、攻击者响应模型、与均匀/风险启发式/确定性审计的对照、投毒检测和 tail-risk 指标、成本延迟，以及分布漂移和串谋压力测试。

## 与 AAMAS 的关系与核验说明

论文把安全博弈、资源分配和 AI 治理连接到 AAMAS 长期的 security games 传统。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JUJH9710.pdf) 核对 Figure 1、§3.1–3.3 三个方向、各节 key challenges 与结论；保留了 SSG 跨域迁移、强攻击者、payoff 估计和无实验验证的边界，未把“proactive、risk-aware、resilient”愿景表述为已证明的部署保证。
