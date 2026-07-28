---
title: "Diverse Mini-Batch Selection in Reinforcement Learning for Efficient Chemical Exploration in de novo Drug Design"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LHWU6232.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["reinforcement_learning", "experimental_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# Diverse Mini-Batch Selection in Reinforcement Learning for Efficient Chemical Exploration in de novo Drug Design

## 一句话总结

本文在 REINVENT 风格的 on-policy 分子生成中，从大批轨迹挑选代表性小批更新，以在昂贵奖励评估下改善化学探索的多样性。

## 方法与证据

- §2 的 Algorithm 1 先并行采样 `B` 条轨迹，再选取 `k` 条评估回报并更新策略。
- §3–3.2 比较 DPP、MaxMin 和 k-medoids；§4.1 用 Morgan 指纹、scaffold 与 atom-pair 信息构造相似性核。
- 在 DRD2、GSK3β 和 JNK3 三项任务中，主要设置为 `B=640`、`k=64`，并比较原始、IMS 与 TanhRND 奖励（§4.1）。
- Figures 1–3 报告平均外部奖励、diverse actives 与 scaffold 多样性；轨迹比较采用 10 次独立运行。

## 局限与复现

- 证据限于 REINVENT 和三项 de novo 药物设计任务，不能直接外推到其他强化学习领域。
- 正文未给出显著性检验或完整实现链，应谨慎解读小幅方法差异。
- 复现至少需任务、三类选集器、三种奖励设置、`B/k` 参数，以及 §2–4.1 与 Figures 1–3。

## 与 AAMAS 的关系与核验说明

工作关注高成本反馈下的自主学习效率与探索覆盖。Spark S1 从原文建立方法、参数与图表证据链；独立 Spark S2 复核范围、统计边界与复现信息，结论一致。
