---
title: "Robust Autobidding for Noisy Conversion Prediction Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/RXYW3025"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RXYW3025.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["offline_optimization_only", "uncertainty_set_assumption", "ctr_cvr_prediction_shift", "advertising_fairness_not_evaluated"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Robust Autobidding for Noisy Conversion Prediction Models

## 一句话总结

RobustBid 将 conversion-maximizing autobidding 写成对 CTR/CVR prediction perturbations 的 worst-case robust optimization，并为特定 uncertainty sets 推出解析 bidding formulas；在 synthetic、iPinYou-derived 与 BAT benchmark 的离线模拟中，相比非鲁棒策略保持更稳定的 conversion/CPC，但作者明确该 formulation 不能直接用于在线 sequential bidding。

## 方法与证据

- 基线按 budget 与 CPC constraints 最大化预期 conversion；其 bid 依赖 predicted CTR/CVR，因此预测扰动会直接改变 bid（§2.1）。
- RobustBid 用 validation error 构造 CTR/CVR uncertainty sets，在所有允许 perturbations 下优化 worst-case objective。对 individual CTR、individual CVR 与 joint CTR-CVR cases，论文用 convex/dual/KKT 等技术给出可计算的解析 bidding formulas（§2.2、§3）。
- 实验对比 NonRobustBid 与 RiskBid，在 synthetic、iPinYou-based first-price environment 与 BAT 上以 total conversion value（TCV）、average CPC 等评价；noise levels ε_a、ε_b 取 10^-6 到 10^-2，synthetic 使用 T=500/1000 与 100 random seeds（§4.1--4.3）。
- 报告结果显示 RobustBid 在更大 CTR/CVR perturbation 下通常有更高 TCV、更低 CPC，并在复杂 iPinYou/BAT 的多数 ε pairs 降低波动；但结果是由注入噪声、模拟 auction/winning-price 设置和给定 constraints 得出的（§4.4、Table 2）。
- Limitations 明确指出当前提出的 robust optimization 问题为 offline、不能用于 online setup；未来方向是 online extension 与把 uncertainty estimation 纳入 bid（§5）。

## 适用边界与复现

- worst-case guarantee 仅相对所选 uncertainty set、predicted CTR/CVR error geometry、known winning-price/auction assumptions 与 offline objective；真实竞争者响应、delayed conversion、预算 pacing、nonstationarity 和 feedback loop 可能不满足这些条件。
- Robustness to prediction perturbation 不等于广告系统公平、隐私合规、广告质量、用户福利或反操纵保证；论文未评估受众群体差异、sensitive targeting、auction externalities 或平台 policy。
- iPinYou 中原始离散 bid values 被拟合分布替代，BAT 虽较接近真实场景仍是 benchmark data；应报告 dataset 时间切分、auction mechanism、counterfactual/off-policy validity、conversion attribution delay 和 revenue/advertiser trade-offs。
- 复现应公开 CTR/CVR models、validation-derived ε、uncertainty-set 类型、budget/CPC constraints、winning-price simulation、seed 与 α/dual solver precision；在线部署需另做 exploration、pacing、guardrails 与 A/B experimentation。

## 与 AAMAS 的关系与核验说明

这是多智能体市场/机制中的广告自动出价与鲁棒优化工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RXYW3025.pdf) 核对模型、§3 formulas、§4 datasets/metrics 和 §5 offline limitation；没有将模拟噪声下的稳健性表述为生产广告系统或社会层面的保证。
