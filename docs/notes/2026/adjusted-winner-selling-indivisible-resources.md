---
title: "Adjusted Winner: from Splitting to Selling"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/QQCP5375"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QQCP5375.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["two_agents_additive_common_scale_assumption", "sale_price_and_cost_model_dependence", "fptas_specific_to_awns_rho", "spliddit_simulation_not_real_mediation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Adjusted Winner: from Splitting to Selling

## 一句话总结

本文将两人 Adjusted Winner (AW) 中原本必须拆分的一件物品替换为：在卖出成本预算内出售若干不可分物、再分配销售收入；它定义 DSIRS/AWNS 的福利差与福利比目标，证明若干变体难解，并只为最小福利比的 AWNS-ρ 给出 FPTAS。该结果依赖两人、加性且可比的共同基数效用与外生销售价格/成本，不能恢复经典 AW 的 envy-free、equitable、Pareto-optimal 三重保证。

## 方法与证据

- DSIRS 将资源分为出售集 `S0` 与两人的完整物品 bundle；出售收入按比例分配以尽量平衡福利，出售总成本不得超预算，且双方福利严格为正。价格被假设不超过两人中较高效用，卖出成本与效用独立（§3.1）。
- 对给定 `S0`，AW-derived plan 在剩余物上运行 AW，但在将要 split 前停止，或收入已足以平衡 gap 时停止。AWNS-d 最小化福利绝对差，AWNS-ρ 最小化 `max(W1,W2)/min(W1,W2)`；相应 `-c` 版本在给定差/比限制下最小出售成本（Definition 3.9、3.11--3.14）。
- Proposition 3.6 表明 envy-free plan 不一定存在；Proposition 3.7/Corollary 3.8 说明最小 gap/ratio 与 envy-freeness 互不推出。Theorem 4.2 和 Corollary 4.3 给出 AWNS-d-c、AWNS-ρ-c 的常数近似不可得（除非 P=NP）；Corollary 4.4 称相关优化/判定版本弱 NP-hard（§3--4）。
- Theorem 5.2 给出 AWNS-ρ 的 FPTAS，采用动态规划和缩放；论文称部分完整证明在 full version。模拟以 Spliddit 的 4--15 物品实例随机抽两人，用 `ε=0.1`、固定 seed 42，在六种价格/成本设定下比较预算与平均 ρ/gap；这只展示模型内 sensitivity（§5--6）。

## 局限与复现

- 理论假设恰为两人、私有加性效用、同一可比较基数尺度、可分销售收入和中立 mediator；真实继承/离婚估值往往不可比、有互补性、法律限制、税费、市场流动性、谈判/策略操纵和多方利益，均不在模型保证内。
- 出售价格、销售成本、预算和收入分配规则决定结果。以“价格不高于两人最大效用”的假设不能说明实际成交价或交易可行；售出本身也会损失物品的情感/使用价值，不能将所得福利比解释为真实公平或接受度。
- FPTAS 仅为 AWNS-ρ，而非所有 AWNS 目标；论文明确 exact envy-freeness 不总存在，最均衡和 envy-free plan 可不同，也未证明 Pareto optimality。使用时须先指定要优化的公平定义，不能援引经典 AW 的全部性质。
- 复现应取得 full-version proofs，固定 tie-breaking、价格/成本 modes、budget、Spliddit snapshot、二人抽样规则、seed 42、forced allocation/sale variants 和 ε；报告各实例而不只均值，并在人类调解中另行评估可解释性、偏好 elicitation、交易成本及分配接受度。

## 与 AAMAS 的关系与核验说明

该文研究不可分资源的两人公平分配与资源出售。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QQCP5375.pdf) 核对 DSIRS/AWNS 定义、Proposition 3.6--3.7、Theorem 4.2/5.2 及 Spliddit 模拟范围；未把模型内福利平衡外推为真实纠纷的 envy-free、帕累托最优或社会可接受结果。
