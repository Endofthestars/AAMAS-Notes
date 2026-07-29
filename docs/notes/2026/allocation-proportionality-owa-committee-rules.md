---
title: "Allocation Proportionality of OWA-Based Committee Scoring Rules"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "resource_allocation"]
dblp_key: ""
doi: "10.65109/JADB9518"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JADB9518.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03y"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "multiwinner-voting", "owa-rules", "party-election-model", "simulation-study"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Allocation Proportionality of OWA-Based Committee Scoring Rules

## 一句话总结

本文将配额制中的“席位份额应等于支持份额”移植到序数多赢家党派选举：以规则的 scoring vector 定义各党的 aggregate score，并用席位份额与该分数份额的 KL divergence 衡量 OWA committee rule 的 allocation proportionality。

## 方法与证据

- 在 party election 中，每位候选人归属一党。对 OWA rule 的 scoring vector $s$，党 $i$ 的 aggregate party score 是该党候选人在全部选票中所得 $s$ 分数的归一化和；该 surrogate 满足归一化、匿名/中立、可加性、弱单调性，且不依赖 OWA vector（§2–3）。
- 若每党所得 committee seat share 等于该 aggregate score，规则在该 election 上 allocation proportional；由于席位离散，作者以党分数向量与席位向量的 KL divergence 作 degree，而非声称规则一般精确满足该性质（§3）。
- 在 1D/2D Euclidean party-election statistical cultures、4/6/10 个党和六种 OWA rule 上实验。图 1 的结论是 k-PAV 跨设置最稳健；CC 在多党尤其 1D 时较好，HB 居中，Block Voting 与 k-Borda 持续偏向多数党；SNTV 在 committee size 超过党数时会更不成比例（§4）。

## 适用边界与复现

- 指标是依赖 scoring vector 的 rule-specific 代理，且假设候选—党派映射和党内凝聚的偏好生成；它不是一般选举中的公平、策略性或少数群体保护保证。KL 也需要处理零席位/零分量的数值约定。
- 复现须公开 1D/2D 生成器、党数/候选/选民/committee size、每 rule 的 scoring/OWA vectors、winner-tie handling、重复次数、KL 平滑或零项处理和完整结果。应另检验非党派、异质偏好与操纵情景。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JADB9518.pdf) 人工核对定义、KL 指标和实验比较；该文为 extended abstract，并指向更长的 arXiv 版本，笔记未使用未在会议 PDF 中展开的额外结论。
