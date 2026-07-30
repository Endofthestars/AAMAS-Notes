---
title: "PSTV: Towards Practical Verification of Strategic Ability for Probabilistic Models with Imperfect Information"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["safety_verification", "argumentation_reasoning", "game_theory_mechanism", "norms_trust_governance", "applications", "agent_engineering"]
dblp_key: ""
doi: "10.65109/GQVY6801"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GQVY6801.pdf"
tool_url: "https://stv.cs-htiew.com"
documentation_url: "https://stv-docs.cs-htiew.com"
demo_url: "https://jmp.sh/share/9s8RrRQuxaXKViesRlQr"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06b"
spark_draft_verdict: "source_grounded_with_required_table_truth_semantics_scaling_and_reproducibility_boundaries"
spark_qa_verdict: "needs_revision_corrected_page_map_and_reverified_every_asv_vvote_table_cell"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["model_semantics_not_real_voting_assurance", "first_tool_to_our_best_knowledge_author_claim", "memoryless_deterministic_strategy_scope", "two_voting_model_families_only", "explicit_state_growth_and_timeouts", "single_run_timings_without_variance", "no_baseline_or_independent_tool_cross_check", "memory_parallel_utilization_and_algorithm_validation_unreported", "code_version_hash_and_reproduction_package_unreported", "web_access_upload_security_and_privacy_unreported", "false_assurance_if_model_result_is_overgeneralized"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_table_truth_semantics_explicit_state_scaling_reproducibility_and_false_assurance_boundary_check"
escalation_verdict: "major_revision_required_before_scalability_or_real_system_assurance_claims"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted model-checking semantics and false-assurance check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# PSTV: Towards Practical Verification of Strategic Ability for Probabilistic Models with Imperfect Information

## 一句话总结

PSTV 是 STV 的 probabilistic branch，为 imperfect-information asynchronous multi-agent models 提供显式状态 PATL model checking；两个 voting model family 表明 probabilistic formulas 可得到与 ATL 不同的模型内 truth value，同时也显示强烈的 state/time growth 和 timeout。表中 TRUE/FALSE 只说明公式在给定模型与语义下是否成立，不是现实投票系统的隐私、正确性或安全认证。

## 工具与逻辑范围

论文提供 [PSTV Web 工具](https://stv.cs-htiew.com)、[示例与文档](https://stv-docs.cs-htiew.com) 和 [演示视频](https://jmp.sh/share/9s8RrRQuxaXKViesRlQr)。

输入系统由 asynchronous modules 的 local states/transitions 组成，并通过 asynchronous product 得到 global model。PSTV 做 explicit-state model checking，支持带 non-nested strategic operators 的 ATL/PATL formulas，并可结合 knowledge 与 Shannon uncertainty operators。

论文当前聚焦 imperfect-information memoryless deterministic strategies。“没有其他工具支持 imperfect information PATL model checking”带有 “to our best knowledge” 限定，只能记为作者的查新主张，不能写成已穷尽所有工具的事实。

## 公式与实验设置

ASV 的 probabilistic formula \(\phi_1^p\) 使用 40% threshold。vVote 的 \(\phi_2^p\) 使用 90% probability threshold，并要求相应 Shannon entropy 不超过 1 bit。

测试 timeout 为 3 小时；平台为 96 × 2.40 GHz Intel Xeon Platinum 8260 CPUs、991 GB RAM、64-bit Linux。论文没有说明 96 CPUs 的实际并行策略或 utilization，因此硬件数量不能被解释为 PSTV 获得了相应 parallel speedup。

## Table 1：Simple Voting（2 candidates）

| Voters | States | Generation (s) | ATL time (s) | ATL result | PATL time (s) | PATL result |
|---:|---:|---:|---:|:---:|---:|:---:|
| 1 | 15 | <0.01 | <0.01 | FALSE | 0.01 | TRUE |
| 2 | 133 | <0.01 | 0.02 | FALSE | 0.05 | TRUE |
| 3 | 1,071 | 0.05 | 0.32 | FALSE | 1.20 | TRUE |
| 4 | 8,461 | 0.82 | 4.90 | FALSE | 84.12 | TRUE |
| 5 | 66,855 | 3.12 | 81.52 | FALSE | 527.63 | TRUE |
| 6 | — | timeout | — | — | — | — |

6-voter row 是 timeout，没有逻辑结果；不能补写成 FALSE。

## Table 2：vVote

| Voters | States | Generation (s) | ATL/H time (s) | ATL/H result | PATL/H time (s) | PATL/H result |
|---:|---:|---:|---:|:---:|---:|:---:|
| 1 | 887 | 0.05 | 0.04 | FALSE | 0.16 | TRUE |
| 2 | 39,028 | 1.58 | 1.05 | FALSE | 192.35 | TRUE |
| 3 | 1,717,232 | 102.75 | 80.49 | FALSE | timeout | — |

3-voter PATL/H 也是 timeout，不是 FALSE。

## 如何解释 TRUE、FALSE 与时间

ATL 与 PATL 的 truth value 来自所给 formal model、initial state、formula 与 strategy semantics。PATL 为 TRUE 而 ATL 为 FALSE，说明概率阈值改变了该模型中的战略能力判断；它不证明真实 voting implementation、cryptographic protocol、operational process 或 human behavior 满足相同属性。

这些单点结果支持“在所列实例上运行 PSTV 并观察到 PATL 比 ATL 更耗时”这一有限陈述。它们不支持广义 scalability claim：

- 只评测 ASV 与 vVote 两个 parameterized model families；
- state 数从 15 增至 66,855，以及从 887 增至 1,717,232；
- ASV 在 6 voters 生成阶段 timeout，vVote 的 PATL/H 在 3 voters timeout；
- 没有重复运行、variance 或 confidence interval。

## 复现与验证缺口

论文没有报告：

- 与其他 model checker 的 baseline 或独立 cross-check；
- runs、seeds、variance、warm-up 或 measurement protocol；
- peak memory、state-storage representation 或 memory curve；
- algorithm correctness proof、reference implementation comparison 或 regression suite；
- CPU parallelization、thread count、utilization 或 speedup；
- tool/code version、commit hash、container/image 与 dependency lock；
- downloadable model files、formula files、commands 和完整 reproduction package。

Web 界面支持加载和解析模型，但正文也没有说明 upload、authentication、access control、retention、audit 或 privacy policy。这里记录的是证据缺口，不是说 PSTV 已发生安全事故。

## 风险边界

形式化验证的主要风险是 false assurance：模型抽象、formula、strategy class 或 implementation 若与现实系统不一致，模型内 TRUE 仍可能被误读为现实安全保证。部署用途应额外核验 abstraction fidelity、model provenance、formula review、checker correctness、independent cross-validation、counterexample handling 和 model-to-code conformance。

高风险评级来自结论被过度外推的后果与当前复现链不足，不表示 PSTV 本身已被证明不安全。

## 页码核验

- p. 4161：题名、作者、摘要、引言、应用背景与 formal preliminaries；
- p. 4162：模型图、technology/usage、两张实验表、实验设置和结论；
- p. 4163：致谢与参考文献，没有新增实验结果。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GQVY6801.pdf) 核验；`reviewed` 不表示现实投票安全、完整 strategy class 覆盖、广义 scalability 或独立 checker correctness 已得到验证。
