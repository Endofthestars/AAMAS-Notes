---
title: "Inference of Altruism and Intrinsic Rewards in Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "human_agent_interaction", "game_theory_mechanism"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DWDD1205.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["qre_behavior_assumption", "multi_group_rank_condition", "context_independent_altruism", "simulated_motivation_inference"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Inference of Altruism and Intrinsic Rewards in Multi-Agent Systems

## 一句话总结

论文在“有效 reward 是自身 intrinsic reward 与他人 intrinsic rewards 的线性 altruism 加权和”的模型中，以跨群组 QRE demonstrations 推断 reward 与 altruism；这是带强行为和结构前提的 MAIRL 可识别性结果，不能从一般人类行为日志直接诊断真实动机。

## 方法与证据

- 每位 agent 有 intrinsic reward 和 context-independent altruism level；有效 reward 线性结合自身与其他 agent 的 intrinsic rewards。模型假定 agent 可获得彼此 intrinsic rewards、intrinsic reward 仅依赖自身动作和 state（§3–4）。
- 以 entropy-regularised quantal response equilibrium (QRE) 建模 demonstrations。单一群组即使 altruism 已知也只可识别到 potential-based shaping；Theorem 1 需要 $n+1$ agents、每 agent 在两个足够不同群组中被观测且所有 pair 满足 rank condition，才能精确分离 altruism、并将 intrinsic rewards 识别到常数/势函数等固有等价（§5）。
- 两个 Bayesian inference 方法对 QRE likelihood/near-equilibrium policy 做后验近似；随机 Markov games 与 Overcooked 模拟中，多群组比不使用群组的 ablation 更易恢复参数，并能以新设 altruism 合成行为（§6–7）。

## 局限与复现

- QRE、已知/可建模 dynamics、线性 altruism、对象无关的 altruism、群组独立 demonstrations 与 rank condition 均是识别的必要建模条件；违反任一项时，参数可解释性不成立。
- 结果针对合成 agents 和紧凑 Overcooked 设定，不测量真实人类偏好、心理特质或道德价值；“altruism”是该 reward 参数化，而非临床或社会科学诊断。
- 复现应公开群组构成、QRE temperature、reward/altruism priors、rank-condition 检查、trajectory posterior 和每个新 altruism level 的 policy/welfare；还应测试关系依赖、state 依赖和非 QRE 行为的错配。

## 与 AAMAS 的关系与核验说明

该文连接 MAIRL、社会偏好与跨群组多 agent 交互。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DWDD1205.pdf) 核对结构模型、识别条件、Bayesian 方法及随机 MG/Overcooked 实验；不将条件化可识别性外推为无条件心理动机推断。
