---
title: "HyperTensioN and Total-order Forward Decomposition Optimizations"
conference: "AAMAS"
year: 2026
track: "jaamas"
topics: ["planning_scheduling", "agent_engineering", "argumentation_reasoning", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/IREH8205"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IREH8205.pdf"
resource_url: "https://ipc2020.hierarchical-task.net/"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06g"
spark_draft_verdict: "benchmark_summary_requires_eight_configuration_solved_count_and_runtime_boundary_corrections"
spark_qa_verdict: "needs_revision_correct_eight_configs_remove_derived_coverage_and_preserve_unreported_semantic_correctness"
spark_consistency: "pass"
risk_level: "medium"
risk_tags: ["three_page_jaamas_summary", "solved_count_not_runtime_speedup", "eight_configuration_table_requires_exact_mapping", "preprocessing_timeout_inclusion_unreported", "per_instance_runtime_memory_and_plan_quality_unreported", "cpu_os_compiler_source_version_and_commit_unreported", "runs_seeds_variance_and_statistics_unreported", "other_planner_baseline_unreported", "failure_timeout_classification_unreported", "transformation_semantic_preservation_not_established_in_summary", "pullup_safety_not_formally_established_in_summary", "dejavu_cache_pruning_soundness_and_completeness_unreported", "ipc_total_order_results_not_arbitrary_htn_or_partial_order_generalization"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_solved_count_runtime_boundary_transformation_semantic_preservation_cache_pruning_correctness_reproducibility_and_ipc_generalization_check"
escalation_verdict: "pass_with_benchmark_correctness_and_reproducibility_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted benchmark, transformation-correctness, and reproducibility-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# HyperTensioN and Total-order Forward Decomposition Optimizations

## 一句话总结

HyperTensioN 以 Hype 三阶段 compiler 串联 parsing、domain transformations 和 lifted total-order forward decomposition；在 24 个 IPC total-order domains、892 个 instances、16GB RAM 与 60s timeout 下，八种配置的 solved counts 从 370 到 555 不等。该表说明固定门槛内的覆盖差异，不提供逐实例 runtime、speedup、plan quality 或 transformation correctness 证明。

## 论文与竞赛边界

这是 AAMAS 2026 JAAMAS Track 的三页摘要，概述 2025 年 JAAMAS full article 的工作。论文称 HyperTensioN 是 HTN IPC 2020 total-order track winner，并把 TPD 配置的胜出描述为 “small margin”；可通过论文给出的 [HTN IPC 2020 页面](https://ipc2020.hierarchical-task.net/)了解竞赛背景。三页稿没有给 source repository、release 或 commit，笔记也不从 full article 或竞赛网页补入未在本稿复核的结果。

## Hype 与 HyperTensioN

HyperTensioN 最初用于把 classical-planning instances 自动转换为 hierarchical-planning instances，由 PDDL parser 作为 front-end、(J)SHOP description compiler 作为 back-end。Parser 与 compiler 共享 Intermediate Representation（IR）；middle-end extensions 用来弥合 description-language 差异并优化表示，与目标 planner 及输入/输出语言解耦。

随着项目拆分，Hype 控制三阶段 compiler pipeline，可在生成 target representation 前运行多个 middle-ends，甚至重复运行。正文举出 HDDL parser、DOT debugging compiler 等扩展例子；这些是架构示例，不是完整语言/特性支持矩阵。

HyperTensioN 是 lifted Total-order Forward Decomposition（TFD）planner，采用 standard progression search。它跳过 grounding，不预先依据 objects 与 preconditions 实例化全部 operators/methods；该设计减少一种可能昂贵的预处理，但三页稿没有给出 grounding-versus-lifted 的独立 runtime 对照。

## 三项 domain transformation

- **Typredicate**：利用 constant/parameter types 限制无意义 substitution。Transport 示例把 `(at ?obj – locatable ?l – location)` 特化为 vehicle/location 与 package/location predicates，并替换相应 occurrences。
- **Pullup**：若 method 中较早 steps 不可能带来某个 operator-subtask precondition predicate，则把该 predicate 拉到 method precondition，使不满足的 decomposition 更早失败。论文以 predicate symbol 判断 “possibly brought about”。
- **Dejavu**：为 direct/indirect recursive methods 加入 “unobservable” primitive mark/unmark tasks 和检测重复 decomposition 的 predicates；由于 backtracking 会丢失 state 中的 marks，外部 cache 跨 branches 记录已探索失败的 methods 与 unifications，避免重复相同失败分解。

论文还称 compiler 会移除 rigid predicates 并把它们作为 constant information，以压缩 state structure。三页稿描述了这些机制和 benchmark 结果，但没有在本稿中给出 transformation semantic preservation、Pullup safety、Dejavu cache-pruning soundness/completeness 的形式证明；“未报告证明”不表示这些变换实际不正确。

## Table 1：精确结果

Table 1 统计 24 个 domains、892 个 instances 在 16GB RAM 与 60s timeout 下的 solved counts：

| Configuration | N | T | P | D | TP | PD | TD | TPD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Solved instances | 370 | 370 | 391 | 491 | 395 | 540 | 491 | 555 |

配置缩写对应 No extensions、Typredicate、Pullup、Dejavu 及其组合。论文对表格的解读包括：

- Freecell-Learned 与 Monroe-PO 在八种配置下均为 0；
- 七个 domains 不受 extensions 影响，正文只举 Barman-BDI 与 Elevator-Learned 等例；
- T 的 total 与 N 相同，作者称二者 equivalent；
- D、PD 与 TPD 是表现最好的配置组，TPD 的 total 最高；
- Typredicate 的作用集中在 Transport 且需要与其他 optimizations 组合：该行 N/T/P 为 0，TP 为 4、D/TD 为 15、PD 为 25、TPD 为 40；
- Pullup 可能增加 overhead，例如 Factories-simple 的 N/T 为 1，而 P/TP 为 0；与 Dejavu 组合的 D/PD/TD/TPD 均为 3。

这些是 timeout 内 solved-count observations。不能据此生成平均 speedup、百分比 runtime reduction、throughput 或单实例更快的结论；表格也没有比较 plan quality。

## 复现与外推缺口

三页稿未报告：

- CPU model/core count、OS、Ruby/C++/compiler/runtime versions；
- source release、commit、build flags、command 或 environment image；
- parsing/transformation/preprocessing 是否计入 60s timeout；
- per-instance runtime、peak memory、plan length/cost 或 solution quality；
- runs、seeds、variance、confidence interval 或 significance test；
- timeout、memory、compile、unsupported feature 与 unsolvable 的 failure taxonomy；
- 同一设置下的 other-planner baseline；
- domain selection、configuration tuning 或 IPC-specific optimization 的独立敏感性分析。

因此 IPC total-order benchmark 不能自动外推到 arbitrary HTN domains、partial-order HTN、hybrid settings 或 deployed agent systems，也不能证明 completeness、optimality 或通用 runtime superiority。

## 页码核验

- p. 4188：题名、摘要、引言、三阶段 architecture 与 Figure 1；
- p. 4189：Typredicate、Pullup、Dejavu、Table 1、优化影响与结论；
- p. 4190：参考文献，没有新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IREH8205.pdf) 核验；`reviewed` 表示三页摘要的架构、表格和证据边界已复核，不表示 full JAAMAS article、完整复现包或形式正确性已独立验证。
