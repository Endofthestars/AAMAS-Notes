---
title: "Fair Contracts in Principal-Agent Games with Heterogeneous Types"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "marl_coordination"]
dblp_key: ""
doi: "10.65109/IAXU7159"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IAXU7159.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03g"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "hidden-agent-types", "linear-contract-assumption", "two-agent-simulation", "normative-fairness-choice"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fair Contracts in Principal-Agent Games with Heterogeneous Types

## 一句话总结

在有限 horizon Markov game 中，principal 向所有 agents 给同质 linear reward-share contract；agents 有不可见、会缩放贡献的 type。principal 慢于 agents 学习，并以 welfare 或全体 wealth variance 正则；两 agent Coin Game 中 variance regularization \(\lambda=1\) 的 1-Gini=.992、welfare=45.5（Table 1）。这并非异质劳动力/社会系统中的公平、无歧视或激励相容保证。

## 方法与证据

- contract \(\alpha_t\) 是每 agent 对潜在 reward 的 share；agent 必须承担行动成本，type \(\theta_i\) 不被 principal 观察（§2）。
- policy-gradient 独立学习，principal 用较慢 learning rate 近似 bi-level response；公平项可为 agent welfare 或所有 parties wealth 的负方差（§2--3）。
- \(\lambda\) 过低导致剥削、过高忽略 principal wealth；实验仅 modified Coin Game、两 agents、多 seeds，未给真实合同/多 type 分布/策略报告（§3--4）。

## 适用边界与复现

- 复现应公开 types、cost/reward scale、contract/action spaces、time-scale、\(\lambda\)、seeds与 Gini/Rawlsian/AIE；测试 agent manipulation、非线性合同、长期参与和群体差异。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IAXU7159.pdf) 人工核对模型、正则与 Table 1；未将模拟公平外推为真实合约公正。
