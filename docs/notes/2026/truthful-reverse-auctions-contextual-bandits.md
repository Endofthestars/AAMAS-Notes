---
title: "Truthful Reverse Auctions for Adaptive Selection via Contextual Multi-Armed Bandits"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MBRQ7564.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["incentive_compatibility_scope", "contextual_bandit_assumptions", "regret_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Truthful Reverse Auctions for Adaptive Selection via Contextual Multi-Armed Bandits

## 一句话总结

论文将多 LLM provider 的 query routing 建模为带私有成本的 contextual bandit reverse auction，并以 ROSA resampling 将单调分配规则转为 truthful、个体理性的机制。

## 方法与证据

- 用户是 buyer、providers 报告处理成本；模型质量随 query context 随机变化。目标同时是学习 query 相关质量与激励真实成本报告（§1–3）。
- Reverse auction 的 BIC 需要 allocation probability 随某 provider 报价非增，并配合 Myerson 型 payment；Theorem 2 还要求 virtual cost 严格递增的 regularity 以得到用户效用最优的静态 reverse mechanism（§3）。
- ROSA 是 reverse self-resampling：Theorem 3 表明任意 single-parameter reverse domain 中，单调 ALG 与该 procedure 组合给出 truthful-in-expectation / EPIC 及个体理性所需机制性质（§4）。
- TRCM-UCBOPT 使用满足单调性的 contextual bandit allocation；文中给出 $O(\sqrt T)$ regret 的理论结论，且该 regret/真实性以特定 stochastic contextual model、resampling 和 active-set construction 为前提（§4–5）。

## 局限与复现

- 这不是对现实 LLM 定价、质量、延迟或隐私的无条件最优 router；provider 的成本分布、regularity、reward/context 表示与交易重复结构均是模型假设。
- “truthful”需区分 BIC、truthfulness in expectation/EPIC 与 universal EPIR；不能简写为任意实现都对任意策略严格 dominant。
- 复现应报告 virtual-cost monotonicity、allocation monotonicity、resampling probability、payment estimator、regret oracle及种子；只报 routing accuracy 无法验证激励结论。

## 与 AAMAS 的关系与核验说明

该工作将机制设计用于多 agent LLM provider selection。笔记依据官方公开 [AAMAS PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MBRQ7564.pdf) 核对了 reverse auction、ROSA 和 regret 的条件。
