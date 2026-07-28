---
title: "Agents of Diffusion: Enhancing Diffusion Language Models with Multi-Agent Reinforcement Learning for Structured Data Generation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/GGJL7344"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GGJL7344.pdf"
preprint_url: "https://arxiv.org/abs/2601.07152"
code_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["benchmark_scope", "judge_feedback_dependency", "extended_version_difference"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Agents of Diffusion: Enhancing Diffusion Language Models with Multi-Agent Reinforcement Learning for Structured Data Generation

## 一句话总结

AoD 用 prompt optimizer 与 judge 两个自回归 LLM 以自然语言反馈迭代控制冻结的扩散语言模型，从而生成更符合 JSON schema 且保持多样性的结构化文本。

## 方法与证据

- 生成器是冻结的 LLaDA-8B；AoD 不更新 DLM 权重，而在 prompt 空间中更新，试图结合扩散解码的语义多样性与自回归代理的格式控制（§1、§3）。
- 在每轮中，DLM 按当前 prompt 采样候选，judge 依据 schema/rubric 产生文本反馈，prompt agent 根据历史和反馈给出编辑；Algorithm 1 将该循环写为多智能体 RL（§3.3）。
- 论文把 prompt update 作为混合 PPO/REINFORCE 的策略优化，文本反馈充当 surrogate reward；附录给出 prompt-update 收敛论证（Theorem 1）。该结论对应其 prompt-space 更新与论文指定的优化设定，不是 DLM 输出质量的无条件保证。
- §4 比较 AoD 与 diffusion/自回归生成、静态 prompt、仅 prompt optimization、标量奖励及自然语言反馈消融；报告 Similarity、Diversity、Entropy、Novelty、Perplexity 等指标，并在不同 optimizer–judge 组合下测试。
- 论文的扩展版包含附录与更长实验材料；AAMAS 正式版是 10 页，笔记仅使用两者共有的题名、作者、方法与明确标出的实验结论，不把扩展版附录当成正式版额外的已验证贡献。

## 局限与复现

- 输出结构是 JSON 为主；论文结论支持所选结构化数据、rubric、judge、prompt 与基线设置，不能自动扩展为任意代码、表格、数据库模式或事实正确性保证。
- judge 的自然语言反馈本身是控制信号；其可靠性、偏见、提示注入抵抗性和与目标 schema 的对齐将直接影响优化方向。正文未将它证明为独立、可信的外部评估器。
- “model-agnostic”在实验中指替换若干 optimizer/judge 组合的经验稳定性；不是对任意模型、任意上下文长度或任意推理成本的形式保证。
- 融合 score 的提高不能单独证明数据的隐私、安全、下游效用或分布保真。结构合规、多样性、语义相似度和 perplexity 是不同指标，应分别报告。
- 复现需保留 schema/rubric、冻结 DLM 版本、optimizer/judge 型号与提示、迭代轮数、编辑算子、RL 超参数、数据集划分和每项指标；论文正文未提供可核验的官方代码链接，因此不可假定实现细节已公开。

## 与 AAMAS 的关系与核验说明

这是以语言反馈协调专长代理和生成模型的多智能体系统。笔记使用作者公开的 [arXiv HTML 原文](https://arxiv.org/html/2601.07152v1) 作为主文本，并明确标注其为 extended version 的来源差异。
