---
title: "Fair Revenue Distribution in Data Markets"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/VHME3099"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VHME3099.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03l"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "submodular-utility-assumption", "oracle-access", "bicriteria-approximation", "strategic-behavior-open"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fair Revenue Distribution in Data Markets

## 一句话总结

本文研究数据市场在最大化总收入时如何给每位数据卖家最低公平补偿：精确的 Fair-Revenue-Max 即使单一买方类型、同一阈值也 NP-hard；当买方对数据集的效用是 submodular 时，作者给出多项式时间的 $\widetilde O(\log m)$ 双准则近似，同时近似市场收入和每位卖家的阈值。

## 方法与证据

- 市场收到买方预测任务，按使用托管数据带来的预测改进收费，并按贡献（如 Shapley share）补偿卖家。多个同样高收入的分配可让同价值、非互补的数据卖家得到完全不同的补偿，因而引入卖家级阈值 $\tau_j$（§1）。
- Fair-Revenue-Max 在收入最大化外要求每个卖家至少获 $\tau_j$；该 share-based fairness 不等同于平均分配，适合异质数据价值和不同标注/整理成本（§1.1）。
- 作者将问题表为有指数变量的线性优化，并证明其 NP-hard。对 submodular buyer utilities，以 Plotkin--Shmoys--Tardos 框架和所需 oracle 解 LP：若最优收入为 OPT，则构造解收入至少 $\mathrm{OPT}/\eta$、每名卖家至少 $\tau_j/\eta$，其中 $\eta\in\widetilde O(\log m)$（Theorems 1--2）。

## 适用边界与复现

- 保证依赖 submodular utility 与 oracle access；隐藏项还依赖买方单位 accuracy 愿付价格的对数。它不是精确公平或预算/个体理性/策略真实性的完整机制设计保证。
- 摘要把买卖双方的策略性报告、超可加数据效用、以及 price of fairness 留为未来工作。复现应提供效用/oracle 形式、阈值输入、PST oracle 和精度、货币上界、运行时间及与无公平约束收入的比较。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VHME3099.pdf) 人工核对题名、硬度结论和双准则保证；未把理论近似保证外推到策略性真实数据市场。
