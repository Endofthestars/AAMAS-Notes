---
title: "SLEECinFRET: A Tool to Manage Social, Legal, Ethical, Empathetic, and Cultural Requirements"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["norms_trust_governance", "safety_verification", "argumentation_reasoning", "agent_engineering", "human_agent_interaction", "applications"]
dblp_key: ""
doi: "10.65109/XWPK8237"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XWPK8237.pdf"
demo_url: "https://youtu.be/88ShfVOqchs"
code_url: "https://github.com/mirgit/SLEECinFRET"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05t"
spark_draft_verdict: "source_grounded_with_required_page_formal_evidence_and_realizability_boundary_corrections"
spark_qa_verdict: "needs_revision_corrected_for_external_proof_attribution_page_map_wording_and_formal_to_physical_boundary"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["safety_critical_requirements", "formal_realizability_not_physical_safety", "formalization_not_legal_or_ethical_compliance", "norm_elicitation_errors_and_omissions", "defeater_priority_and_conflict_risk", "test_coverage_not_requirement_correctness", "redundancy_and_sufficiency_checks_missing", "contrary_to_duty_unsupported", "monitoring_and_obligation_inference_missing", "no_usability_or_industrial_evaluation", "no_performance_or_scalability_benchmark", "sensitive_requirement_data_governance", "provenance_change_and_audit_controls_unreported", "pinned_fret_fork_staleness"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_realizability_formal_to_physical_norm_completeness_test_oracle_provenance_and_safety_critical_compliance_boundary_check"
escalation_verdict: "needs_revision_corrected_for_formal_evidence_realizability_test_coverage_norm_governance_and_compliance_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted formal-methods and safety-critical governance check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# SLEECinFRET: A Tool to Manage Social, Legal, Ethical, Empathetic, and Cultural Requirements

## 一句话总结

SLEECinFRET 把带条件、时序 scope 和有序 defeaters 的 SLEEC 规范需求翻译为 FRETish children，使其可与标准需求一起接受 LTL translation、simulation、realizability checking、test generation 与生命周期管理；这些能力检查的是已形式化模型，不证明需求本身完整正确，也不构成真实系统的安全、伦理或法律合规认证。

## 工具定位与资源

SLEEC 用于表达 social、legal、ethical、empathetic 与 cultural requirements。论文把 SLEECinFRET 定位为 FRET 的扩展：在一个项目中管理 SLEEC rules 与标准 FRETish requirements，并复用 FRET 的分析工具和 dashboards（p. 4110）。

实现是官方 FRET 在 commit `ba6e9d2` 上的 fork（p. 4111）。公开资源包括 [代码仓库](https://github.com/mirgit/SLEECinFRET) 和 [演示视频](https://youtu.be/88ShfVOqchs)。

GUI 支持 `in progress`、`paused`、`deprecated` 等 requirement lifecycle states。论文没有报告这些状态与 source-control commit、审批人、审计日志或发布基线如何关联。

## SLEEC 语法扩展

论文加入七种 scope（p. 4110）：

- `in`；
- `before`；
- `after`；
- `notIn`；
- `onlyIn`；
- `onlyBefore`；
- `onlyAfter`。

并支持十种 timing：

- `immediately`；
- `next`；
- `always`；
- `never`；
- `eventually`；
- `until`；
- `before`；
- `for`；
- `within`；
- `after`。

一个带 \(n\) 个 defeaters 的规则形如：

\[
[\mathrm{SCOPE}\ mode]\ \mathrm{IF}\ C_0\ \mathrm{THEN}\ [T_0]O_0,
\]

\[
\mathrm{UNLESS}\ C_1\ \mathrm{IWC}\ [T_1]O_1,\ldots,
\mathrm{UNLESS}\ C_n\ \mathrm{IWC}\ [T_n]O_n,
\]

其中 IWC 表示 “in which case”。后面的 defeater 在更具体条件成立时覆盖前一义务。

## 从一个 SLEEC rule 到 \(n+1\) 个 FRETish children

翻译把上述规则展开为 \(n+1\) 条 requirements（p. 4110）：

- \(C_0 \land \neg C_1\) 时满足 \(O_0\)；
- \(C_0 \land C_1 \land \neg C_2\) 时满足 \(O_1\)；
- 依此类推；
- \(C_0\land C_1\land\cdots\land C_n\) 时满足 \(O_n\)。

论文引用 [3, 11] 作为 translation correctness、formal semantics 和 complexity 的依据，并称翻译新增线性数量、每条为线性大小的 FRETish rules。三页稿没有重新给出完整证明，也没有由此推出端到端分析时间、内存或大型 requirement set 的线性性能。

在工具内（p. 4111）：

- 原 SLEEC requirement 是 parent；
- 自动生成的 FRETish requirements 是同一项目中的 children；
- children 为 read-only；
- parent 修改后 children 自动重新计算；
- children 可使用 LTL translation、simulation、realizability checking 和 test-case generation。

这提供了 parent-to-generated-rule 结构，但论文没有说明跨版本 diff、review approval、stable identifier、rollback 或 children 的 immutable audit history。

## Consistency、realizability 与现实系统

FRET 的 realizability 定义是：对环境的任意输入，存在一个 component implementation 满足 requirement set（p. 4111）。

论文用两个 requirements 说明 consistency 不等于 realizability：

- `a` 成立时要求立即满足 \(p\)；
- `b` 成立时要求立即满足 \(\neg p\)。

它们可在某些 valuations 下同时为真，因而不能仅凭局部可满足性判定冲突；当输入 \(a=b=\mathrm{true}\) 时，没有实现能同时满足两个输出义务，所以 requirement set 不可实现。

这里的 realizability 是针对 FRET 抽象 component、变量和输入空间的逻辑存在性。它不表示：

- 现实硬件、传感器、执行器、网络和人员流程能实现该行为；
- implementation 已正确生成或经过 runtime verification；
- requirement 对真实情境完整、无歧义、无遗漏；
- 系统已获得 safety assurance、human-value alignment 或法律合规。

## Nursing-home window 示例

示例将一个标准 FRET requirement 与一个 SLEEC requirement 放在同一 nursing-home robot 项目中（p. 4111）：

- 室外温度低于阈值时不得打开窗户；
- 用户请求时打开窗户；
- 若用户未穿衣，则为保护 privacy 改为明确义务 `do_not_open_window`。

SLEEC rule 的一个 defeater 生成两条 read-only FRETish children：

1. `user_asks & !user_undressed` 时满足 `open_window`；
2. `user_asks & user_undressed` 时满足 `do_not_open_window`。

与 freezing requirement 合并后，`user_asks` 在低温条件下可能要求开窗，与不得开窗冲突；工具给出 unrealizability counterexample。作者的快速修复是在默认开窗 antecedent 中加入 `!temperature_below_freezing`。修订后 FRET realizability check 通过。

这只说明修订后的抽象 requirement set 对建模输入可实现；不证明阈值、隐私规则、传感器状态或现实护理决策正确。

## Test generation 与 13 traces

FRET 根据 requirements-based coverage 生成执行 traces，包含 input-variable values 与 expected output，用于展示 requirement 应满足或违反的情形（p. 4111）。

当前 window 示例产生 13 个 test cases。数字 13 是单一示例的 trace 数量，不是：

- 13 个真实机器人试验；
- defect-detection rate；
- coverage percentage；
- 与其他工具的 benchmark；
- 对规范正确性或部署安全性的验证。

若 requirement oracle 本身遗漏或错误，生成 tests 也会继承该问题。

## 与现有工具的功能边界

作者把 SLEECVAL 与 LEGOS-SLEEC 描述为更侧重 syntax、consistency、non-redundancy、sufficiency 等 well-formedness 检查；SLEECinFRET 的差异在于 lifecycle、simulation、realizability 与 test generation（p. 4111）。

与 prior work [8] 相比，本工具增加 scope、timing 和 test generation，但当前版本没有该 prior work 的 monitoring 与 obligation inference。

明确限制包括：

- 不直接检查 redundancy 与 sufficiency；
- 不支持 contrary-to-duty obligations，即其他工作中的 `otherwise`；
- 没有 monitoring 与 obligation inference；
- 没有 syntax highlighting；
- 一些 component names 为 hard-coded。

作者计划接入既有工具补足 well-formedness checks，并继续改进 UI。

## 本稿没有评测什么

三页 demo 没有报告：

- domain experts 的 usability、learnability 或 interpretation agreement；
- industrial case study 或 independent validation；
- requirements 数量、defeater 深度下的 runtime、memory 或 scalability；
- defect-detection precision/recall、false positives 或 benchmark comparison；
- translation implementation 与 referenced formal translation 的 conformance test；
- version migration、upstream FRET compatibility 或 fork security maintenance；
- 对现实 safety incident、ethical outcome 或 regulatory compliance 的影响。

作者提到需求来自 industry/project partners，并在 EU project 中改进 UI；这不是 industrial evaluation 结果。

## 高风险治理边界

工具面向 safety-critical、regulated 和 agent-based systems，因此规范层错误可能进入后续设计与测试。高风险点包括：

- domain expert 把价值、法律或文化判断错误地编码为 conditions、obligations 或 defeater order；
- redundancy/sufficiency、contrary-to-duty 与跨规则冲突未被当前工具完整检查；
- “read-only generated child”被误解为 source requirement 已正确；
- 需求修改后自动重算 children，却没有本文披露的审批、provenance、diff、rollback 与审计策略；
- SLEEC rules 可能包含 health、disability、privacy、employment 或其他敏感情境数据；
- 固定在旧 FRET commit 的 fork 可能与上游语义、依赖、安全修复和文件格式漂移；
- generated tests 以当前 requirements 为 oracle，不能发现 oracle 自身的规范遗漏。

高风险等级反映使用情境与未闭环的 formal-to-real-world gap，不表示该 demo 已造成现实伤害。

## 页码核验

PDF 逐页核对：p. 4110 为 identity、Introduction、Contribution、SLEEC syntax 与 translation；p. 4111 为 tool implementation、realizability、test generation、nursing-home example、Related and Future Work 与 limitations；p. 4112 为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XWPK8237.pdf) 核验；`reviewed` 不表示 normative requirements、formal proof implementation、physical safety、human-value alignment 或 legal compliance 已被验证。
