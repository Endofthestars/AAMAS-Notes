---
title: "Procedural Fairness in Multi-Agent Bandits"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/RCLN5951"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RCLN5951.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03d"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "stochastic_bandit_assumptions", "normative_objective", "regret_gap_dependence", "simulation_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Procedural Fairness in Multi-Agent Bandits

## 一句话总结

本文在 MA-MAB 中定义程序公平：每个 agent 获得等量决策 probability mass，并把其份额放在自身最偏好 arms；以 decision-share Nash welfare 打破并列。作者给出 UCB 风格学习、sublinear regret 与 procedural core 结果，并在 7,776 个模拟设置中报告 PF policy 同时取得高 PF/EF/UF scores。该范式是规范性选择，非关于真实参与者感受、激励相容或所有公平定义的证明。

## 方法与证据

- PF 要每 agent 有 \(1/N\) 总 probability mass，且投向其 true-mean favourite arms；EF 最小化 expected reward 不平等，UF 最大化总 expected utility（Definitions 1--3）。
- 学习以 UCB/LCB 保留 favourite candidates，并以 \(t^{-(1-\gamma)}\) 随机探索使 intervals 收缩；Theorem 1 的 regret 依赖 \(\Delta_{min}\)、arms/agents与参数（§3）。
- 定义 procedural core 后，utility-Nash-welfare optimum 未必在其中；指定 tie-breaking 的 PF policy 在 core，且 core 蕴含 PF（Theorems 2--4）。
- 全因子模拟报告 PF policy PF=1.00±0、EF=.98±.02、UF=.97±.05（Table 1），但不含人类实验、策略性申报或真实公共决策。

## 适用边界与复现

- 适用于可估计 stationary arm means 的公共随机选择；equal decision share 不保证结果相等、补偿、可接受性或效率最优。
- 复现需公开 reward matrix/distributions、gaps、UCB/探索参数、tie-breaking、PF/EF/UF score和全部 7,776 setting；测试 nonstationarity、manipulation与协作偏好。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RCLN5951.pdf) 人工核对定义、算法、core 命题和 Table 1；不把形式程序公平夸大为现实合法性。
