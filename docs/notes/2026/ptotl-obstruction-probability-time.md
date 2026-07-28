---
title: "A Verification Framework for Obstruction, Probability, and Time"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "norms_trust_governance", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/ROUK3224"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ROUK3224.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["formal_model_scope", "perfect_information_assumption", "memoryless_defender", "sub_stochastic_probability_semantics", "per_step_budget_reset", "automotive_case_study_not_deployment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Verification Framework for Obstruction, Probability, and Time

## 一句话总结

本文提出 PTOTL，在 Weighted Probabilistic Timed Automata（WPTA）上同时表达 dense time、概率阈值和 defender 对边的预算受限禁用（obstruction）。其 symbolic zone-graph model checking 对所述 class 终止且正确；一 clock 情况 PSPACE-complete。automotive Moving Target Defense case study 展示如何写出 time/probability/budget property。结论是对已建模 attack graph/WPTA 的形式保证，不是对现实车载 CPS、攻击概率或防御部署效果的实证证明。

## 方法与证据

- WPTA 在 timed automata transitions 上加入自然数 sabotage/deactivation cost；cost 仅是 annotation，不进入 guard/invariant，保留 WTA 的可判定结构（§2）。真实防御动作的延迟、失败、联动、业务中断、检测误差和恢复成本需由模型额外编码。
- PTOTL 有 single top-level sabotage binder：defender 每 step 在 enabled edges 中选成本和不超 budget 的 subset 禁用；budget 每 jump 重置。禁止 outcomes 的 probability mass 被移除而非 renormalize，形成 sub-stochastic successor kernels（§1, §3）。这是 attack-graph/MTD 意图的语义选择，不是通用故障/概率物理模型。
- 论文在 perfect-information 下用 memoryless defender strategy，以保持 decidability（§1, §3）。不能直接处理隐藏 attacker state、部分可观测告警、learned adversary、history-dependent policies、多个相互冲突 defender 或长期累积资源预算。
- timed formula 使用 freeze clocks、probabilistic next、dense-time until/release 与 obstruction/budget thresholds；zone graph 将无限 dense-time valuation 符号化（§2–4）。属性真值完全依赖 attack graph、时间 guard、transition probabilities、edge cost和 atomic labels的准确性。
- Algorithm 1–4 在 probabilistic zone graph 上通过 fixpoint 给 model checking；Theorem 4.1 给 termination，Theorem 4.2 给 soundness/completeness，Theorem 4.3 给 PSPACE（并说明 one-clock PSPACE-complete 的 tight relationship）（§4）。这是 worst-case formal complexity，不等于可立即在大规模工业系统中低成本运行。
- 与 PTCTL/PTATL 比较中，PTOTL 扩展 PTCTL 的 obstruction；相对 PTATL，edge disabling + budget 和 coalition strategy on fixed arena 目标不同，形式一般不可比（§6）。故不能用其结果替代一般多 agent coalition/epistemic verification。
- automotive case study 基于 documented in-vehicle attack paths，演示阻断可界定 attacker 在 deadline 内到 Motion/control 的 reachability probability（§5）。属于示例 model/specification；没有实车实验、运行时 performance、attack coverage、误阻断代价或 safety certification 数据。

## 适用边界与复现

- 适用于在明确定义的 attack graph 中检查“在每-step reconfiguration budget 下，某 deadline 内某资产被达成的概率是否低于阈值”一类属性。
- 不可据 model-check pass 宣称实际系统安全。仍需 threat-model validation、概率/时钟参数校准、攻击面覆盖、配置变更验证、fail-safe analysis、硬件/网络测试、human operational approval、runtime monitoring和安全认证。
- 复现应实现 WPTA guards/invariants/resets/costs、budgeted memoryless obstruction、sub-stochastic semantics、freeze-clock formula、zone graph/fixpoint algorithms，并重建 case-study property；应对 budget、deadline、probability、edge cost与漏失攻击路径做 sensitivity analysis。
- 后续需部分可观测/知识、多个 defender/attacker budgets、history-dependent strategies、累计成本、probability intervals、tool integration与规模评测；论文将 imperfect information等列为扩展方向。

## 与 AAMAS 的关系与核验说明

这是 AAMAS quantitative security verification 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ROUK3224.pdf) 核验了 WPTA/PTOTL、obstruction semantics、zone-graph algorithm、PSPACE result、PTCTL/PTATL comparison及 automotive MTD case；没有把模型内概率界写成现实系统安全、部署效果或认证保证。
