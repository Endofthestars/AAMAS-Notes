---
title: "Maximin Share Guarantees via Limited Cost-Sensitive Sharing"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/LGSS5881"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LGSS5881.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04d"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["fair-allocation", "maximin-share", "limited-sharing", "sharing-cost", "theoretical-results"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Maximin Share Guarantees via Limited Cost-Sensitive Sharing

## 一句话总结

本文允许每件不可分物品至多由 $k$ 位 agent 共享并计入共享成本，研究共享何时恢复 MMS 公平：在 equal-share 成本下、$k\ge n/2$ 且 $n$ 为偶数时保证精确 MMS，并提出对任意成本模型有效的 Shared Bag-Filling 近似算法。

## 方法与证据

- $k$-sharing allocation 要求物品最多分给 $k$ 人且完整分配；utility 按物品价值乘以 $1-c_{i,g}(N_g(A))$ 聚合。equal-share 成本使每个 sharer 获得 $1/|N_g(A)|$ 的价值，generous 模型的成本不高于它（§4）。
- Theorem 5.1：在 equal-share、$k\ge n/2$ 下，偶数 $n$ 有 $u_i(A)\ge MMS_i^n(M)$；奇数 $n$ 保证 $MMS_i^{n+1}(M)$。证明通过两两配对的二人 MMS allocation 并共享合并的 bundles（§5）。
- Shared Bag-Filling 先分配大物品，再把每物品的 $k$ 份作为受 distinct-good 约束的 bag filling；其保证为 $\min\{1,(1-C)(k-1)\}$-MMS，$C$ 是最大 sharing cost，故足够大 $k$ 或足够小 $C$ 可恢复 exact MMS（§5）。

## 适用边界与复现

- 结论依赖 additive valuations、完整分配和特定 goods-based cost；共享在这里表示可多重授予的物品，不处理排他时间、拥塞、战略报告或对实际使用者的排队公平。
- 复现需给出 valuation/cost generator、$k,n,m$、equal/generous cost 定义、MMS benchmark 算法、Shared Bag-Filling 实现和所有边界实例；SMMS 的普遍存在性被论文反例否定，不能把普通 MMS 保证混同为更强的 SMMS。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LGSS5881.pdf) 人工核对模型、Theorem 5.1 与算法保证；未将抽象共享解释为任何现实资源的自动可行调度方案。
