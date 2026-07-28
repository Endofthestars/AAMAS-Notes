---
title: "Optimizing Pool Testing for Epidemic Surveillance"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "planning_scheduling", "applications"]
dblp_key: ""
doi: "10.65109/KTGS1394"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KTGS1394.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["known_contact_network_and_sir_model_assumption", "test_accuracy_and_operational_delay_omitted", "simulated_cascade_approximation", "welfare_objective_not_public_health_outcome"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Optimizing Pool Testing for Epidemic Surveillance

## 一句话总结

本文在已知接触图和离散 SIR 传播模型下选择 pooled tests，以最大化阴性池所清除个体的效用；sample-average LP 加 randomized rounding 给出 bicriteria 近似，并以 multiplicative-weights 扩展规模。它说明感染相关性可显著影响该模型内 welfare，但不构成真实疫情检验策略或医学准确性的验证。

## 方法与证据

- 每个 pool 是不超过 `n_p` 的节点子集，`B` 个 tests 在相对传播可忽略的短时间窗内完成；若 pool 中无人处于模型规定的阳性窗口则其成员被 cleared，目标为 cleared utilities 之和（§3）。
- Theorem 4.1 构造实例说明忽略网络相关性的方案可从最优 `Θ(n)` welfare 降至 `o(n)`；Lemma 4.2 显示 transmission probability 的 `Θ(1/n)` 误差也可使 calculated welfare 从 `Θ(n)` 变为 `o(n)`（§4）。
- RoundPool 从 `N` 个 SIR cascades 构造 LP、独立 randomized rounding pools。Theorem 5.5 称在足够 samples 下，以高概率输出不超过 `(1+ε)B` tests 且期望 welfare 至少约 `(1−ε)^2/2` 最优；这是一种 bicriteria 保证而非严格预算/最优保证（§5）。
- 三个网络为 Virginia academic hospital contacts（四周的患者/医护共处）、Aves wildbird 和 Vole trapping。医院实验在 `n_p=4,B=100`、20,000 candidate pools 下报告 correlation-aware welfare 288.891，相比独立随机池 183.511；仅是模拟 cascades/模型内比较（§6、表 1）。

## 局限与复现

- 模型假定潜在接触图、感染 sources、transmission probabilities、恢复/阳性持续期已知，并把所有 tests 视为即时完成；真实网络缺失、行为改变、检测排队、假阳/假阴、稀释效应、再检和隔离决策均未纳入。论文也指出 pool 越大现实准确性可能下降。
- “welfare”是阴性结果可清除的节点效用，不是感染减少、死亡/住院、检测公平或公共卫生收益；对高效用人群的偏置可能与公平目标冲突。
- SAA 理论需要 `Ω(n² log n)` cascades，实践声称线性 samples 足够却基于三图实验；候选 pools 被随机限制（医院 20,000）且 LP/approximate solver 会改变可达解空间。
- 复现应公开去标识接触图构造、SIR/源/时间参数、utilities、candidate-pool sampling、cascades/seeds、ε、budget/pool sizes、solver/硬件，并与有 assay sensitivity、延迟、非重叠/重测和不确定图的临床工作流做独立评估。

## 与 AAMAS 的关系与核验说明

该文是网络扩散下的资源受限 pooled-test 选择优化。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KTGS1394.pdf) 核对 SIR/MaxWelfare 定义、Theorem 4.1/5.5 和三网络实验；未将模型内 clearances 外推为真实检验政策或健康结局保证。
