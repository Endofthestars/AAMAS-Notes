---
title: "Utility Aware Adaptive Privacy Budget Allocation for Streaming Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "norms_trust_governance", "agent_engineering"]
dblp_key: ""
doi: "10.65109/DZYF2577"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DZYF2577.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["data_dependent_privacy_allocation_scope", "sensitivity_bounding_unspecified", "optimality_rule_mismatch", "small_streaming_dataset_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Utility Aware Adaptive Privacy Budget Allocation for Streaming Multi-Agent Systems

## 一句话总结

APBA 按本地信号不确定性和 agent 对融合估计的影响动态分配 Laplace 机制的每步 epsilon，以在波动时减少噪声；其累计预算界在“每步机制已是 DP 且预算选择可安全组合”的前提下成立，但论文未充分证明依赖原始数据的预算/噪声尺度选择本身不泄露信息。

## 方法与证据

- 对 agent `i`，每步 budget 是剩余 budget 乘以由 `αu_i(t)+(1−α)Δ_i(t)` 归一化的份额，其中 `u` 为本地波动、`Δ=|θ̂−θ̂^{-i}|` 为融合影响；观测以 scale `Δy/ε_i(t)` 的 Laplace 噪声发布（§3–4）。
- Lemma 1 仅使用标准 sequential composition：若每个 `M_i(t)` 已是 `(ε_i(t),0)`-DP，则全时域为 `(Σ_t ε_i(t),0)`-DP。Theorem 1 再以算法强制 `Σ_t ε_i(t)≤ε_total−ε_coarse` 推出含 coarse fallback 的全局 `ε_total` 界（§5.1）。
- Theorem 2 给任意无偏、L-Lipschitz 融合器的噪声误差上界；Corollary 1 还要求 `L=O(1/S)` 才在 agent 数增加时使方差按 `1/S` 消退。Lemma 3 对其定义的加权逆平方误差代理求得最优 `ε_i(t)+ε_coarse∝w_t^{1/3}`，其中 `w=u+Δ`（§5.2–5.5）。
- 两个数据流：Intel Lab（10 sensors、1000 步）和 NREL wind（8 sites、1000 步）。与 Shuffled DP、FedAPCA、variance-weighted 比较；表中 Intel 的 APBA MSE/MAE 为 0.01206/0.08903，NREL 为 5.8088/1.8645，且作者说明稳定 NREL 的改进较小、MSE 劣于 FedAPCA（§6–7）。

## 局限与复现

- 顺序组合不能自动覆盖由当前私有 `u_i(t)`、未扰动 `Δ_i(t)` 或其分配结果驱动的机制选择。若选择/epsilon/noise scale 对攻击者可推断，需证明其是基于先前 DP 输出的 post-processing，或为 allocation decision 另行计入隐私；本文的组合证明把每步 DP 当作既成前提，未展开这一数据依赖问题。
- Laplace DP 还需明确且强制有限 sensitivity `Δy`（裁剪、邻接关系、向量范数/跨时间用户定义）。论文给出符号定义，未在算法/实验中完整给出 bounds；真实连续传感器未裁剪时不能直接获得所宣称的纯 DP 保证。
- Lemma 3 的最优解是 cubic-root 权重，而实际 APBA 规则是对当前 agent 间权重的线性归一化乘剩余预算，并未证明二者相同或近似比；“minimizes variance / optimal”应限于该代理、假设和单调性论证，不能当作对实际策略的全局最优证明。
- `ε_coarse` 被称为可忽略但没有逐次 fallback 的机制、epsilon 及会计细节；coarsened reporting 或纯噪声是否仍反复发布必须明确。评估只含 8–10 个流和 1000 步，且 breach/resemblance 经验指标不是 DP 证明。
- 复现应公开邻接与 clipping、全部 epsilon/alpha/初始余额、`u/Δ` 是否由私有值或 DP 报告计算、coarse fallback 会计、攻击者观察面、fusion rule、seeds 和统一实现的 baselines，并以 privacy accountant 验证长期组合。

## 与 AAMAS 的关系与核验说明

该文面向持续协作感知的隐私—效用分配。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DZYF2577.pdf) 核对分配规则、组合定理、误差/最优性条件和实验数值；它将 DP 结论限定为论文明确给出的机制前提，而非未审计的数据依赖自适应机制。
