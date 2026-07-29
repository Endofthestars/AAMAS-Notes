---
title: "Fair Orientations: Proportionality and Equitability"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/EIRQ4510"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/EIRQ4510.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04i"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["fair-division", "orientation-constraints", "proportionality", "equitability", "computational-complexity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fair Orientations: Proportionality and Equitability

## 一句话总结

本文研究物品只能分给相关 agent 的图定向分配，将 proportional share 按每件物品的相关者数量细化，并给出 PROP、PROP1/PROPX、EQ/EQ1/EQX 及 chores-EF1 的存在性、算法与复杂度边界。

## 方法与证据

- 将 agent–item relevance 建模为图/超图的边定向；对 agent (i)，其比例份额是所有相关物品价值按该物品相关者数 (n_e) 加权求和，而非以全体 agent 数平均（§1、§2）。
- 严格 PROP 不总存在；在 simple graph、(1,2)（或负值对应）双值 valuations 下，判定存在性为 NP-complete；任意 relevance 的 binary valuations 则可多项式判定并构造（§1.1、§3）。
- 对 mixed goods/chores，论文构造可多项式计算且兼容 fractional Pareto optimality 的 PROP1 orientation；相较之下 PROPX 可不存在，且即使 simple graph 与 binary valuations 下存在性仍为 NP-complete（§3）。
- EQ、EQ1、EQX 在 orientation constraint 下均不保证存在，simple graph 中其存在性判定 NP-complete；对于 chores，simple graph 存在 EF1 orientation 当且仅当 objectively negative edges 数不超过顶点数，multigraph 版本则 NP-complete（§4、§5）。

## 适用边界与复现

- 结果假定 additive valuations、不可分物品、所有物品必须分配及论文所定义的 relevance；不直接给出现实任务分派的效用估计、公平感或机制激励性质。
- 复现应记录图/超图、每件物品的相关者、goods/chores 与 valuation 编码、采用的公平定义及构造/归约输入；特别要区分 simple graph、multigraph 与一般 relevance 模型。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/EIRQ4510.pdf) 人工核对 refined proportional share、主要存在性/复杂度结论和 chores-EF1 characterization；未将形式公平定义外推为现实场景的整体公平。
