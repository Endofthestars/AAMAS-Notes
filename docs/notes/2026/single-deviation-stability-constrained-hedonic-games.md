---
title: "Single-Deviation Stability in Additively Separable Hedonic Games with Constrained Coalition Sizes"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/AGJY1522"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AGJY1522.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03s"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "additively-separable-valuations", "coalition-size-bounds", "complexity-classification", "stability-definition-variant"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Single-Deviation Stability in Additively Separable Hedonic Games with Constrained Coalition Sizes

## 一句话总结

这篇工作研究有下/上限联盟规模的 additively separable hedonic games。它区分允许成员离开后原联盟失去可行性的“标准” NS/IS/CNS/CIS 与要求两边仍可行的星号版本；规模约束会使无约束时存在的稳定划分消失，并显著改变复杂度分类。

## 方法与证据

- single-agent deviation 只能加入尚未达到上限的 target coalition；是否限制被离开的 coalition 导致标准与 feasible ($^*$) 两套概念。标准概念考虑更多 deviation，因而更强；Figure 1 给出 NS、IS、CNS、CIS 及其星号版本的逻辑蕴含（§1）。
- 作者先刻画何时存在满足 fixed size constraints 的 partition，并称足够多 agents 时必然可行；然后对各稳定概念给出 existence/complexity 图景（§3）。
- symmetric valuations 保证最强 feasible 概念 NS$^*$ 存在；但即使 symmetric 0/1 valuations，最弱标准概念 CIS 也可能不存在。非对称 valuations 下仅 CIS$^*$ 始终存在（§3）。
- 只有 upper bound $\mu$ 时，任意 $\mu$ 的 CIS 可多项式构造，$\mu=2$ 的 CNS 也可；其它 upper bounds 和稳定概念的存在性一般 NP-complete。非平凡 lower bound $\lambda\ge2$ 且 $\mu\ge4,\lambda<\mu$ 时，Nash stability 为 NP-complete；在非负或非正 ASHG valuations 下，任意 $\lambda,\mu$ 的 CIS$^*$ 可多项式构造（§3）。

## 适用边界与复现

- 结果针对显式加性偏好、固定全局 size bounds 与单人偏离；不直接涵盖多人成团偏离、动态加入/退出、非加性互补或不确定偏好。应用时必须明确是否允许一人离开使旧联盟失去最小人数。
- 复现/使用应固定 valuation encoding、$\lambda/\mu$、singleton convention、每种 stability 的 deviation feasibility、对称性/符号限制，并核对 full version 的 reductions/algorithms。摘要还把 lower bound 至少 2 时 IS/CNS 的复杂度等列为开放问题。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AGJY1522.pdf) 人工核对概念区分和 §3 分类；未将理论存在性/NP-completeness 解释为具体分组系统的推荐结果。
