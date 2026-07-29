---
title: "Robust Direct Preference Optimization for Offline Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "safety_verification", "generative_agents"]
dblp_key: ""
doi: "10.65109/UTXZ7394"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UTXZ7394.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03f"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "offline-preference-coverage", "uncertainty-model-assumptions", "not-safety-guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Robust Direct Preference Optimization for Offline Learning

## 一句话总结

Robust DPO 对每个 action 从估计 reward 扣除由比较图 Laplacian 推导的不确定性半径，再进行 KL-regularized DPO；在 Zipf coverage gridworld 报告较 DPO 高 6.9% return、低 73% violations，HH-RLHF/Qwen2.5-0.5B 的 post-hoc weighting 保持表中 preference accuracy。其保护仅在 true reward 落入构造 uncertainty set 的假设下成立，不能证明 LLM 输出安全或真实人类偏好被覆盖。

## 方法与证据

- max--min objective 的 interval inner minimizer 为 \(\hat r-\kappa\)，故 policy 按 \(\exp(-\kappa/\beta)\) 下调不确定 actions（§3）。
- \(\kappa\) 来自 pairwise-comparison graph Laplacian pseudoinverse；Theorem 3.1 依赖 connected graph、BTL/MLE、bounded rewards与 identifiability（§3.1）。
- 表格 Qwen post-hoc weighting 的 accuracy CI 均为 .58 [.48,.67/.68]，只提升 logp gap；不足以证明泛化/安全（§4）。

## 适用边界与复现

- 复现须公开 comparison graph/coverage、BTL fit、\(\delta,\beta\)、Laplacian penalty、datasets与 seeds；特别测试 disconnected graph、偏好噪声、OOD prompts和 reward misspecification。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UTXZ7394.pdf) 人工核对公式、定理条件与两组实验；未将 pessimism 写成通用安全保证。
