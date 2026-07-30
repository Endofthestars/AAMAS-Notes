---
title: "SMT4STECTL: Satisfiability-Driven Synthesis from Specifications in Strategic Timed Existential CTL"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["safety_verification", "argumentation_reasoning", "game_theory_mechanism", "planning_scheduling", "agent_engineering", "robotics_embodied", "applications"]
dblp_key: ""
doi: "10.65109/YCFH5927"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YCFH5927.pdf"
demo_url: "https://stectl.ii.uws.edu.pl/demo"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06d"
spark_draft_verdict: "bounded_formal_synthesis_evidence_insufficient_for_real_system_correctness_or_deployment"
spark_qa_verdict: "needs_revision_preserve_bounded_semantics_visual_version_provenance_and_qualitative_figure_only"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["general_stctl_satisfiability_undecidable", "existential_stectl_fragment_only", "partially_terminating_bounded_synthesis", "no_model_only_within_given_bounds", "memoryless_imperfect_information_strategy_scope", "single_uav_formula_family_benchmark", "figure_only_without_numeric_results_table", "no_baseline_repeats_variance_or_timeout", "solver_configuration_and_bounds_unreported", "formal_model_not_real_uav_safety", "web_solver_resource_tenant_and_input_controls_unreported", "result_provenance_storage_access_and_reproduction_package_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_visual_solver_version_bounded_semantics_uav_correctness_web_solver_resource_isolation_provenance_and_deployment_boundary_check"
escalation_verdict: "pass_after_visual_solver_version_and_bounded_correctness_reconciliation"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted visual architecture and bounded-correctness check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# SMT4STECTL: Satisfiability-Driven Synthesis from Specifications in Strategic Timed Existential CTL

## 一句话总结

SMT4STECTL 把 Strategic Timed Existential CTL（STECTL）specification、bounded executions 与模型类编码为 SMT，以合成 continuous-time multi-agent timed-automata model 和未知时间参数；一般 STCTL satisfiability 不可判定，本文算法只覆盖 existential fragment 的 partially terminating bounded satisfiability，所以 “no model” 仅指 given bounds 内无模型，合成出的 UAV automata 也不是现实飞行安全证明。

## 逻辑与算法范围

STECTL 是 STCTL 的 existential fragment。核心 strategic modality

\[
\langle\langle A\rangle\rangle\gamma
\]

表示 coalition \(A\) 存在 joint strategy，使 resulting runs 满足 temporal objective \(\gamma\)。文中还使用 bounded \(EF_I\) 与 \(EG_I\) 表达 deadline 内到达和区间持续。

输出是 continuous-time multi-agent system（CMAS），表示为 timed automata network，支持：

- asynchronicity；
- optional synchronisation；
- strong monotonicity，以保证 action transitions 之间有 time progress；
- imperfect information 下的 memoryless strategies，只依据当前 local state 选 action。

论文明确说 general STCTL satisfiability remains undecidable，并将算法描述为 partially terminating。SMT-based BMC 编码 model class、bounded executions 和 specification：

- encoding SAT 时返回满足当前 encoding 的 system model/parameter valuation；
- 否则只报告 given bounds 内不存在模型。

后一种结果不能写成 STECTL/STCTL 的 global unsatisfiability，也不能证明所有更大 bound、不同 architecture 或不同 strategy class 都无解。

## Full、partial 与 parametric synthesis

工具支持：

- bounded satisfiability：检查当前 requirements/bounds 下是否有模型；
- full model synthesis；
- partial synthesis：补 transitions、time constraints、parameter values 或 individual agents；
- 对 synthesized model 再做 model checking/analysis。

参数作为 SMT symbolic variables，可代表 model elements 或 formula time constraints。作者把同时在 model 与 formula 层做 parametric reasoning 称为该类工具的首次能力；“first tool”带有 “to our knowledge” 限定，是作者查新主张。

“生成 missing parts 以 guarantee system correctness”只能理解为相对给定 specification、STECTL semantics、model class、encoding、bounds 和 strategy assumptions 的满足性，不是现实系统整体 correctness。

## Architecture

正文列出 Web GUI、BMC Module、SMT Solvers、API Gateway 与 microservices；后者处理 identity、task scheduling、parallel execution 和 result storage。

Figure 1 的原始页面可读到：

- Web Client：TypeScript、SvelteKit、Cytoscape.js、Monaco、Blockly；
- API Gateway：.NET 8、C#、Ocelot；
- Identity：.NET 8、C#；
- Solver Manager 与 Solver Task Scheduler：.NET 8、C#；
- Z3 4.8.12、Yices2 2.6.4、CVC5 1.1.2、Interpol 2.5-1254；
- BMC：C++、smtlibv2。

这些是 architecture labels，不表示 Figure 3 对每个 solver 都执行了独立 cross-check；正文没有说明 benchmark 实际采用哪个 solver/configuration。

## UAV benchmark

示例是 two cooperating drones \(D_1,D_2\) 的 surveillance mission：

- \(\alpha\)：在 deadline \(d\) 前到达 target，至少观察 \(p\) 时间，并在 fuel \(f\) 耗尽前返回 base；
- \(\beta\)：增加经过 zone 1 到达/返回的 nested strategic-timed requirement。

Figure 2 给出 \(n=z=2\) 的 synthesized agents：

- \(\alpha\)：\(d=1,p=3,f=5\)；
- \(\beta\)：\(d=1,p=1,f=5\)。

实验覆盖 2 到 5 agents \(n\) 和 fly zones \(z\)，硬件是 i7-1065G7 CPU、16 GB RAM。

Figure 3 只以折线图展示 execution time 与 memory usage，没有 underlying numeric table。正文给出的结论是：在该实验中，formula size 对 resource consumption 的影响比 locations/transitions 更明显，尤其体现在 memory；复杂的 \(\beta\) 多数点高于 \(\alpha\)。笔记不从图像像素编造精确数值，也不把单一 formula family 的趋势外推为普适 scaling law。

## 评测与复现缺口

正文未报告：

- empirical baseline/tool runtime comparison；
- repeats、seeds、variance、confidence interval；
- timeout、failed/unfinished cases；
- synthesis bounds、unrolling depth、state/transition/SMT variable or clause counts；
- benchmark 采用的 solver、options、parallelism 与 stopping rule；
- Figure 3 exact values 或 machine-readable data；
- correctness proof、independent encoding validation 或 solver cross-check result；
- source repository、commit、container、benchmark inputs 和 reproduction scripts。

工具比较部分是 capability-level related-work discussion，不是公平的 empirical comparison。

## Correctness 与真实部署边界

UAV 例子是 synthesized timed-automata model。论文没有建模或验证 flight dynamics、wind、localization、communication loss、sensor error、collision avoidance、energy model fidelity、actuator failure、human override 或 regulation。形式 witness 不能替代 simulation、hardware-in-the-loop、field test 或 certification。

Web/microservice 平台接收 formula/model tasks 并运行 solver、存储结果，但没有报告：

- input validation、formula/model size limit 与 denial-of-service protection；
- timeout、CPU/memory quota、solver sandbox 与 job cancellation；
- tenant isolation、authorization roles 与 audit log；
- stored specification/result access、retention、deletion 与 confidentiality；
- solver/image/dependency provenance、result replay 和 rollback。

这些是未报告控制，不是已发生安全事件。高风险来自 bounded formal result 被误读为完整系统安全的 false-assurance 后果。

## 页码核验

- p. 4170：题名、作者、摘要、引言、application domain 与 tool comparison；
- p. 4171：Figures 1–3、formal synthesis、architecture、UAV benchmark、结果文字与结论；
- p. 4172：致谢与参考文献，没有新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YCFH5927.pdf) 和原始页面视觉核验；`reviewed` 不表示 unbounded satisfiability、普适 scaling、真实 UAV safety 或 Web solver 治理已经得到验证。
