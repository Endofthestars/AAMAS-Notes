---
title: "Multi-Attribute Committee Selection: Diversity, Correlation, and Approximation Guarantees"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/SXGS7111"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SXGS7111.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "multi_attribute_representation", "additive_approximation", "correlated_attributes", "full_version_required_for_ul2", "not_fairness_certification"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Attribute Committee Selection: Diversity, Correlation, and Approximation Guarantees

## 一句话总结

MAPR 选择固定 size committee，使候选人的 categorical attribute distribution 靠近 target；本文将 Hamilton \(L_1\) 扩展到 finite \(L_p\)，用 fractional conic/linear program+dependent rounding 改善 randomized additive upper bounds，并给 first strong additive inapproximability。针对重复/高度相关 attributes 会被重复加权的问题，摘要介绍 full-version 中的 uncorrelated \(L_2\)（\(UL_2\)）：在 uncorrelated时与 \(L_2\)一致、duplicates不改变 winners。它是 target-distribution matching，不构成个体公平、合法代表性、消除偏见或对相关性/操纵的完整防护认证。

## 方法与证据

- candidates有多个 categorical attributes，input含每 attribute value 的 target frequency；committee induced distributions与 target的 \(L_p\) distance被最小化。精确 optimum NP-hard，故用 additive（而非 multiplicative）approximation，因为 optimum可为0（§1–2）。目标本身可能错误、过粗、不可达或忽视交叉身份/individual preferences。
- 算法先对 per-attribute deviations的 \(L_p\) objective 写 IP，fractional relaxation为 conic program（\(p=1\) linear），dependent rounding 精确保持 committee cardinality/marginals；重复 randomized rounding可提高获得bound的概率。Table 1 new bounds是 high probability，old \(L_1\) bound是 deterministic；任何实现需明确 failure probability和重复预算。
- Table 1：new \(L_1\) upper \(\tilde O(\sqrt{d/k})\)，for \(p>1\) \(\tilde O(d^{1/p}/\sqrt{k})\)；Theorem 1 对 constant \(p\ge1\)、任 \(\beta<1/p\) 给 no polytime additive \(\gamma d^\beta\) unless P=NP。边界和notation（\(d,k,\epsilon\)）依赖模型和 asymptotic regime，非直接业务质量/公平误差尺度。
- correlated attributes may duplicate latent feature、使 \(L_p\) outcome偏向重复代表。AAMAS-board example：\(L_2\) 在 Research Area/Faculty 高相关时选不同committee，删任一 redundant attribute会改变winner。作者要求 uncorrelated时与 \(L_p\)一致、complete duplicates消除、continuity；这些性质防止易见 duplicate manipulation，但不自动发现所有潜在偏见/因果相关。
- 摘要称 full version的 \(UL_2\) 满足 formal variant，且将 uncorrelated rule扩到 other \(L_p\) 是 open；没有给 \(UL_2\) definition/proof/empirics。故不可依据此扩展摘要部署/比较具体 correlation-aware rule。

## 适用边界与复现

- 适合 participatory budgeting、admissions/board composition等受控的 aggregate representation optimization辅助；不可自动选人或项目。真实决策需法律/反歧视、程序正义、资格/冲突检查、stakeholder input、透明目标与申诉审计，且不能只依赖 categorical counts。
- 复现需公布 candidate attributes/target distributions/committee size、distance/objective、fractional solver/rounding/repetition、random seeds/failure probability与 exact small optima；逐项报告 total/per-attribute deviations、selection stability、runtime、target feasibility和 sensitivity。
- 应测 target misspecification、intersectional categories、missing/misclassified attributes、rare groups、attribute duplication/near-duplication、correlation estimation error和 strategic attribute design。等候 full version后再实现 \(UL_2\)，并进行 independent fairness/impact assessment。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 multiwinner/social-choice 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SXGS7111.pdf) 核验 \(L_p\) rounding/bounds、Theorem 1及 correlation problem/\(UL_2\) scope；没有把 aggregate approximation或 full-version预告写成已验证公平机制。
