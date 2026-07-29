---
title: "On Quantitative Analysis of Responsibility in Multiagent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "safety_verification", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/PVFH7189"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PVFH7189.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "causal_attribution_not_normative_blame", "finite_paths_only", "memoryless_strategies", "simple_prisoners_dilemma_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# On Quantitative Analysis of Responsibility in Multiagent Systems

## 一句话总结

本文在有限路径、概率转移的多智能体联合计划中，以 probabilistic ATL 变体区分 causal active、passive、contributive responsibility，并以可满足 history 的比例、概率质量和语言熵量化责任大小；三种测度在简化重复囚徒困境上给出不同排序，说明二元“是否负责”不足以表达计划与时间下的因果贡献，但不构成法律/道德 blame 的自动分配规则。

## 方法与证据

- 系统是 transition system：各 agent 同时选 action，joint action 以概率分布转移；agent 采用 memoryless strategy，joint plan 由 coalition strategy 相容的 histories 给出（§2）。逻辑仅含 bounded paths 与 bounded-until，故不覆盖无限 horizon、history-dependent policy、部分可观测、学习中策略变化、连续控制或未建模的外部因素。
- CAR（active）要求其他 agent 不能避免 outcome 而该 agent 若改行动可避免；CPR（passive）是在其他人动作固定时该 agent 改行动可避免；CCR（contributive）要求 agent 属于导致 outcome 的 coalition 且去掉它不能达成（§1）。这些是模型内的反事实因果条件，结论依赖 action space、state abstraction、coalition 和 joint plan 的指定，不能直接解释意图、过失、授权、知情或法律责任。
- 通过在逻辑语义中加入 \(\langle\Gamma\rangle CAR_{i,\pi}(\psi)\)、CPR、CCR operators 表达三种责任；文章称判定任一类型的算法在 PSPACE（§2）。extended abstract 未给完整语义推导、proof、model-checking algorithm、输入编码/参数化复杂度或实际可运行实现，因此只能记录该复杂度主张。
- 三种量化：proportional measure 是满足相关性质的 histories 数占总数；probabilistic measure 是其概率质量的归一化；entropy measure 用有限词语言增长率，避免某些随 horizon 变长时概率都趋零却难度不同的情形（§3）。对 CAR，文中以可达 outcome 的正 histories 与 coalition 可避免 outcome 的负 histories 组合；CPR/CCR 的完整计算交给外部 full version，不能臆补公式。
- 实验是 two-agent repeated prisoner’s-dilemma 变体：各 agent 以 0.75 cooperate、0.25 defect，比较不同 time bound 与 reward/payoff/fine formula 的 CAR/CPR/CCR 曲线（图 1–3）。论文观察不同测度给出不同结果；未报告真实审计案例、baseline、seeds/置信区间、规模/性能、人工评价或责任归因准确度。

## 适用边界与复现

- 适合已形式化的联合计划、仿真或模型检查中，用于比较模型内反事实责任，而非直接处罚人或部署到高风险治理。采用前必须明示 outcome formula、horizon、coalition、baseline plan、策略与概率；同一行为在这些选择改变后可能得到不同责任值。
- 复现应实现有限 probabilistic transition system 和 memoryless strategy profile，逐条实现 CAR/CPR/CCR 的逻辑语义；枚举或符号计算 compatible histories，分别取得 count、概率质量及 language entropy。需从所指 arXiv full version 补齐各测度的 precise definitions、算法和 proof，并重建囚徒困境的 transition/reward/payoff/fine 及 0.75/0.25 policy。
- 应测试更多 agent、不同 coalition、稀有高危事件、非独立/非平稳转移、partial observability、history-dependent/learned policy、不同 horizon 与 specification；报告状态爆炸、数值精度、模型误设敏感性、时间/内存和不同 measures 的排序稳定性。还应与 Shapley/power-index 类基线比较，作者也将这一联系列为未来工作。
- 责任量一旦用于告警、问责或资源惩罚，必须保留证据链与完整模型版本，允许被归因方质疑 transition/strategy/coalition 假设，并由人类复核。避免把概率较低、可替代者较少或被简化掉的背景条件错误地转化为个人 blame；应做群体偏差、遗漏变量和申诉影响评估。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 MAS 责任建模与 formal verification extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PVFH7189.pdf) 核验三类因果责任、概率 ATL/有限路径/memoryless 前提、PSPACE 判定陈述、比例/概率/熵测度和重复囚徒困境展示；没有将形式化因果归因扩写为真实场景的道德、法律或自动问责结论。
