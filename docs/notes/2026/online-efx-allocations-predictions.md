---
title: "Online EFX Allocations with Predictions"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "agent_engineering"]
dblp_key: ""
doi: "10.65109/PGMH4700"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PGMH4700.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "additive_normalized_valuations", "irrevocable_online_allocation", "prediction_error_assumptions", "two_agent_positive_result"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Online EFX Allocations with Predictions

## 一句话总结

论文研究未知固定数量的不可分物品在线、不可撤销分配：在 additive normalized valuations 下，衡量预测与真实 valuation 的 total-variation error。没有逐物品预测时，两个同质 valuation agents 最好只能保证 \(\varphi-1\approx0.618\)-EFX；对两个同质 agents，若预测足够准确，作者给出常数每步操作的 \(a\)-EFX 算法与误差阈值。这些是特定信息模型的理论界，不意味着真实推荐/分配系统在错误预测、非加性偏好或策略行为下自动公平。

## 方法与证据

- 每个 agent 先给出预测 horizon 与 normalized additive valuation vector；物品到达时真实 value 才揭示且必须立即分配。误差为 true/predicted vectors（对不同 horizon 补零）的 TV distance，accuracy 为 \(1-d_i\)（§1）。
- \(a\)-EFX 指对任意 i,j 与 j bundle 中任意 good，\(v_i(A_i)\ge a v_i(A_j\setminus\{g\})\)；\(a=1\) 是 exact EFX（§1）。
- 两 agent、同质 valuation、无 predictions 时，threshold algorithm 保证且紧为 \(\varphi-1\)-EFX；若 valuations 不同，则对任何 \(a>0\) 的无预测保证都不可能（Theorem 2.1、§2）。
- 对含 predictions 的算法，论文给出预测-only 方案的必要/充分 accuracy bounds，以及使用 true values 与 predictions 时的下界。两同质 agents 且 \(a\in(\varphi-1,1]\) 时，Theorem 2.4 给出 error 不超过 \((4+a-a^2)(1-a)/((2+a)(5-a)(1+a))\) 的正结果，算法每步常数操作；作者同时说明 bounds 之间仍有 gap（§2）。
- 结论依赖在线不可逆、固定但未知 horizon、加性归一化 values与 accuracy threshold；扩展摘要没有用户实验、真实预测器、策略性申报、分配效率或多 agent 正算法的实证。

## 适用边界与复现

- 应区分 ex-post a-EFX 与过程公平、激励相容、效率或群体公平；一个理论上满足 a-EFX 的 allocation 不保证 agents 如实上报预测/真实价值。
- 复现须固定 arrival sequence、T/T' 补零规则、valuation normalization、TV error、a、预测来源与算法；暴力检查每个 i,j,g 的 EFX inequality，并分别报告不可能构造与正算法案例。
- 真实系统应评估 prediction drift、非加性/负价值、预算/容量、分组公平及策略操纵；超出两同质 agents 时不可把 Theorem 2.4 直接外推。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的在线公平分配扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PGMH4700.pdf) 人工核对模型、TV accuracy、Theorems 2.1--2.4 与二 agent 正结果；未将其写成现实公平或激励保证。
