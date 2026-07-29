---
title: "Collaborate, Deliberate, Evaluate: How LLM Alignment Affects Coordinated Multi-Agent Outcomes"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "human_agent_interaction", "marl_coordination"]
dblp_key: ""
doi: "10.65109/UQPO8536"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UQPO8536.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02e"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["llm_roleplay_evaluation", "human_collaboration_claim_scope", "alignment_method_scope", "no_human_subject_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Collaborate, Deliberate, Evaluate: How LLM Alignment Affects Coordinated Multi-Agent Outcomes

## 一句话总结

论文将协作干预代理置于 modified-action MDP（MAMDP），论证标准偏好优化在行动会被合作者抵制或改写时失去原有最优性，并在 LLM 角色扮演的两类协作任务中报告面向“建设性摩擦”的 FAAF 优于若干标准对齐法。

## 方法与证据

- MAMDP 在普通 MDP 外加入行动修改分布 `P_A`：干预代理输出的行动会经合作者策略转换后才影响对话状态。Theorem 1 指出按底层 MDP Bellman optimality 训练的 Ψ-preference optimization policy 未考虑该修改，故不具 MAMDP 最优性（§2）。
- 实验把 Meta-Llama-3-8B-Instruct 干预代理分别用 SFT、PPO、BC、DPO、IPO、FAAF 训练；合作者为不同 GPT-4o 实例，任务为 DeliData Wason Card Selection 和 Weights Task（§3）。
- 在 standard MAMDP（随机修改）与 explicit MAMDP（提示令修改确定发生）下，以准确率、normalized cumulative common ground、performance gain、change-of-mind rate 等指标比较。Table 1 中 FAAF 在 explicit MAMDP 的 Wason coarse accuracy 为 0.526，Weights Task 的 adjusted common ground 为 7.819；作者据此称其较能平衡共同基础与正确解。
- 结果表达的是该角色扮演协议、具体任务、基座模型和训练实现下的相对指标；论文结论也把真实人类受试研究列为下一步，而非已完成验证（§4）。

## 适用边界与复现

- 不能由 LLM 扮演合作者的结果推出人类会接受“摩擦”、改变信念或得到更好协作；共同基础指标与 change-of-mind 也不等同于知情同意、可信度或长期关系质量。
- MAMDP 的理论结论针对被修改的行动空间与指定策略类；它不表明所有 SFT/DPO/PPO 在多智能体系统中均较差，也不自动给出 FAAF 的跨环境安全/鲁棒性保证。
- “friction”可能有时间、认知负担、权力不对称和骚扰风险。用于真人协作时需透明披露、可退出/覆盖机制、领域审核和对受影响群体的独立评估，不能仅以任务正确率部署。
- 复现需公开两任务的 prompts/roleplay rules、GPT-4o 与 Llama 精确版本、训练数据和超参数、MAMDP 的 `P_A`、seeds、指标实现及置信区间；进一步主张需预注册的人类研究与适当伦理审查。

## 与 AAMAS 的关系与核验说明

该工作结合 agent alignment、协作对话和多智能体决策。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UQPO8536.pdf) 核对 §2--4、Theorem 1 和 Table 1；未把模拟结果表述为真实人机协作的因果或部署结论。
