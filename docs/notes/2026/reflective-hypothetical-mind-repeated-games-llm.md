---
title: "Solving Repeated Games with Large Language Model"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "game_theory_mechanism", "marl_coordination"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IRTM9736.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_model_five_run_evaluation", "stationary_convergence_assumptions", "prompted_policy_reproducibility", "dynamic_opponent_generalization"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Solving Repeated Games with Large Language Model

## 一句话总结

Reflective Hypothetical Mind（RHM）在重复博弈中以 LLM 生成并评分对手行为假设，再把基于事后 regret 的 self-reflection 接入 policy adaptation；作者在 GPT-4o 上的若干小型博弈报告高于 plain LLM、Reflexion 和 HM 基线的累计奖励，但这不是对一般动态对手或任意 LLM 的求解/均衡保证。

## 方法与证据

- 设定为完全历史可观测的有限 normal-form repeated game。每轮 LLM policy 根据过往 joint actions 选择动作；文中理论目标使用无限期、折扣 payoff，但实验设 $\delta=1$ 并采用有限轮数（§3.1、§4.2）。
- Hypothetical Mind 模块从历史生成候选对手策略（默认 top-$k=3$），让 LLM 在每个假设下预测下一动作；预测正确记 $+1$、错误记 $-1$，以 $\alpha=0.3$ 的 recency-weighted update 更新 value。value 达 $0.7$ 时视作 validated，多假设按预测动作投票（§3.2.1）。
- self-reflection 计算给定已观察对手动作时，当前动作与事后 best response 的 payoff 差作为 regret。policy adaptation 以对 validated hypothesis 的期望 payoff 和 regret 加权评分候选 policy；若没有稳定 gain 则选择/生成替代策略。候选集合如何由 prompt 具体生成仍是 LLM 驱动的启发式过程（§3.2.2–3.2.3）。
- Theorem 1 声明：若对手策略分布 stationary、真实对手模型包含在 hypothesis space，且 reflection regret updates 有界且无偏，RHM 几乎必然收敛到“给定正确对手推断”的 Nash policy，并使 per-round regret 趋零。该结论不覆盖非平稳/策略性响应对手、模型失配或未满足其 stochastic-approximation 假设的 prompt LLM；实验中的 Alternation 等动态策略也不在 stationary 前提内（§3.2.3）。
- 实验只使用 GPT-4o，每种 repeated game 模拟 5 次取平均：IPD、Battle of Sexes 各 10 轮，RPS 20 轮，Colonel Blotto 30 轮。对比 HM（$k=1,3$）、Reflexion、plain LLM；对手包含规则策略、cooperative/human LLM 等（§4.1–4.2）。
- 作者图表报告 RHM 在多数测试对手的 coordination/cyclic scenarios 中累计奖励最高，尤其能摆脱 IPD 中 Tit-for-Tat 诱发的 mutual-defection、对 Battle of Sexes Alternation 更快协调，且在 $n=3$、budget $s=3\ldots6$ 的 Blotto 中领先。plain LLM 在部分 IPD 对手（如 Grim Trigger、cooperative/human LLM）反而最好；这些是小样本、固定模型和自定义对手族上的相对结果（§4.3–4.6）。

## 局限与复现

- “solve”并非计算任意 repeated game 的精确 Nash/均衡策略：动作选择、假设生成、候选策略与 validation 均由 prompt LLM 的文本推理决定。理论的 best-response 论断需要给定准确模型等强假设，不能由经验胜率替代验证。
- 收敛条件要求 stationary opponent，但论文强调的 cyclic/Alternation 对手可能非平稳；真实多 agent 相互适应时对手还会响应 RHM，自身 hypothesis space 是否包含真策略通常不可知。部署时应将动态对手结果看作有限回合实证，而非定理担保。
- 实验只报告 GPT-4o、5 次重复、最多 30 rounds；没有跨模型、温度/seed、prompt、token budget、cost/latency 或显著性分析。累计 reward 的差异不证明鲁棒性、可复现性或泛化到谈判、投资等文中动机领域。
- IPD、BoS、RPS 和三战场 Blotto 的规则、payoff 与内置对手狭窄；Blotto 的 $s=3\ldots6$ 虽组合数增长至 784，但不等于大规模多玩家/不完全信息博弈。反事实 regret 使用已观察动作也不提供环境干预或长期因果信用分配。
- 复现应发布精确 system/user prompts、hypothesis/strategy parsing、temperature、seed、上下文截断、所有逐轮 action/value/regret/validated-hypothesis 轨迹和五次原始结果；应分开评测 stationary 与非stationary 对手，并以可计算 best response/均衡算法校验理论设定。

## 与 AAMAS 的关系与核验说明

该文将 LLM 的 opponent modeling、反思与策略更新组合到重复多 agent 决策中。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IRTM9736.pdf) 核对 RHM 更新规则、Theorem 1 的条件、GPT-4o/5-run 实验协议及四类游戏范围；不将有限样本 reward 或条件化收敛声明外推为通用博弈求解能力。
