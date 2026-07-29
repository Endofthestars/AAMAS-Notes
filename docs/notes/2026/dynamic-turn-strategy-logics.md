---
title: "The Dynamic Turn in Strategy Logics"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["argumentation_reasoning", "safety_verification", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/WZKX4761"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WZKX4761.pdf"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04o"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_taxonomy_and_boundary_revision"
spark_consistency: "pass_after_terra_boundary_revision"
risk_level: "medium"
risk_tags: ["blue_sky_vision", "dynamic_strategy_logics", "formal_complexity_boundary", "cross_logic_transfer", "no_formalism_algorithm_or_evaluation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_formal_complexity_boundary_check"
escalation_verdict: "pass_after_targeted_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted formal-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# The Dynamic Turn in Strategy Logics

## 一句话总结

本文提出一条研究议程：拟将 Strategy Logics 从固定 concurrent game model（CGM）上的静态推理拓展到模型动态变化，依次研究更新语义、模型修复合成与验证/合成工具；论文没有交付统一动态逻辑、合成算法、工具、可判定性或复杂度新定理。

## 方法与证据

- 现有 CL、ATL、ATL* 与 SL 能表达联盟或智能体在给定 CGM 中“能否迫使某性质成立”，但缺少直接表达模型更新的算子。作者以软件升级、机器人环境变化和投票协议修改说明“当前安全且更新后仍安全”等需求（§1–2，pp. 3893–3895）。
- 原子交换例子中，原模型里的 Anna 可能迫使交换完成；若给双方增加 reject 动作，Brita 便可拒绝交易。文中的 `[add_reject]¬φ` 是拟议更新情形，用来说明未来逻辑需要表达更新造成的能力变化，不是已经定义并验证的新逻辑结果（Example 2.1、Example 3.1）。
- 作者拟借鉴 Dynamic Epistemic Logic（DEL）的更新直觉：公共公告启发状态限制，arrow update 启发转移限制，substitution 启发事实赋值变化。论文明确说 DEL 的 epistemic model 与 CGM 差异显著，这三类对应只是“不完整的第一近似”（§3.1，p. 3895）。
- 更新算子还可被量化，使逻辑询问“是否存在修复”或“所有允许更新是否仍安全”。这被列为待系统研究的表达力—复杂度权衡，并非本文已经证明的动态 SL 性质（§3.1）。

## 三个相互衔接的挑战

1. **动态能力语义**：拟定义改变动作、动作效果、环境事实、智能体数量及其组合的模型更新，并研究更新算子的语义、表达力与计算复杂度。
2. **自动合成**：在更新语言明确之后，给定初始模型和目标公式，构造使目标成立的语法更新。作者强调“判断某种更新存在”不等于“构造出更新”，两者甚至可能有不同复杂度；最小、便于人理解的修复也是开放目标（§3.2，p. 3896）。
3. **验证与合成工具**：拟扩展 MCMAS、MCK、STV、VITAMIN 等现有模型检验工具，并探索紧凑更新表示、量化搜索及状态爆炸缓解方法。BDD、bounded model checking、partial-order reduction、fixpoint approximation 和 abstraction 都只是候选技术路径（§3.3，p. 3896）。

依赖关系是研究议程本身提出的路线：挑战一可为二、三提供更新对象与语义，挑战二定义工具需要求解的修复任务，挑战三再以可实现性检验前两项的设计取舍。

## 复杂度边界与复现

- 论文回顾的结论属于已有静态逻辑：CL 与 ATL 模型检验在 P，ATL* 在 memoryless 与 perfect-recall 语义下分别达到 PSPACE-complete 和 2EXPTIME-complete，而带 imperfect information 与 perfect recall 的 ATL/ATL* 模型检验不可判定（§2，p. 3894）。这些不是本文对拟议动态 SL 得出的新复杂度结果。
- 论文用 DEL 文献说明量化更新可能显著改变表达力与复杂度：量化公共公告可导致不可判定，而某些复杂 action-model 量化仍可判定且不增加表达力。这只能提示迁移风险，不能推出动态 SL 的对应结论（§3.1）。
- 要把议程变成可复现成果，至少需要公开：更新语言及形式语义、更新候选类、基准 CGM 和目标公式、存在性与构造性任务的判定条件、生成修复的正确性/最小性标准、复杂度证明，以及工具实现和基线。本文没有提供这些产物或实验。

## 与 AAMAS 的关系与核验说明

该议程连接战略推理、MAS 验证、模型/策略修复与安全性分析，也试图统一规范系统、obstruction logic 等已有动态特例。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WZKX4761.pdf) 核对 §2 的静态背景、§3.1–3.3 三个挑战、两个原子交换例子和结论；未把 DEL 类比、拟议算子、工具建议或未来复杂度问题写成已完成贡献。
