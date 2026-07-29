---
title: "Neuro-Symbolic Decision Making for Autonomous Agents"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["agent_engineering", "planning_scheduling", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/PVRI5073"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PVRI5073.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04z"
spark_draft_verdict: "source_grounded_draft_needs_revision"
spark_qa_verdict: "pass_after_prior_work_proof_and_fidelity_boundary_revision"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "prior_work_summary", "ilp_symbolic_policy", "event_calculus_macro_actions", "online_fastlas_guidance", "transferred_drl_heuristics", "qualitative_results_only", "convergence_proof_conditions_absent", "symbolic_readability_not_fidelity", "future_fidelity_metrics"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_convergence_generalization_and_explanation_fidelity_evidence_check"
escalation_verdict: "pass_after_overview_claim_and_open_direction_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Neuro-Symbolic Decision Making for Autonomous Agents

## 一句话总结

这篇博士研究概述把四条已发表或已接收的工作线串成同一条神经符号决策路线：从轨迹学习符号策略、以时态宏动作引导在线规划、在表格 RL 中在线更新探索启发，再把符号建议迁移进深度 RL 动作选择；三页稿报告的是这些工作的机制与定性结论，不提供完整数值协议或证明，而符号规则与神经策略的行为忠实度量仍是后续研究。

## 研究问题与证据类型

长时域、稀疏奖励、大动作空间和复杂关系结构会增加规划与强化学习的探索难度。作者希望以符号知识提供结构化、可读的启发式，同时保留神经方法的可扩展性与抗噪能力（§1，p. 3990）。

本文是 Doctoral Consortium 的研究脉络概述。§2 的四项贡献分别回顾文献 [18]--[21] 中已完成或已接收的工作，而不是在本稿内重新给出一套可独立复现的完整实验。因此，下文的比较结果均表示“作者在所引工作中报告”，不等于本三页稿提供了数值复核或形式化证明。

## 四条贡献线

### 1. 从 RL 轨迹提取符号策略

作者观察自主驾驶场景中 multi-objective RL agent 的执行轨迹，用 Inductive Logic Programming（ILP）学习可读的符号规格，以表达社会可接受的决策准则；这些表示还用于实现 Answer Set Programming（ASP）planner（§2，p. 3990）。

概述称该 planner 的性能与原 RL agent “comparable”，并把它作为黑箱策略与符号推理之间的可行桥梁 [18]。这里没有性能指标、任务实例、运行次数或统计检验，因而只能保留为所引工作的定性报告。

### 2. Event Calculus 时态宏动作引导规划

第二条工作以 ILP 学习 domain-dependent Event Calculus（EC）理论，从少量执行轨迹归纳 persistent、time-extended macro-actions。它们显式表达跨时间依赖，并被用来引导 POMCP 与 DESPOT 这类 MCTS-based online planners（§2，pp. 3990--3991）。

作者报告在 Pocman 与 Rocksample 中，时态宏动作比 time-independent heuristics 更具表达力和一般性，并改善计算效率与解质量 [19]。三页稿没有定义这些比较指标、实例规模、基线配置或数值，因此不能把该表述扩大为跨领域的规划泛化保证。

### 3. 在表格 RL 交互中在线学习启发式

第三条工作在 tabular RL 训练期间收集批量经验，经 FastLAS 在线归纳并持续修正 ASP heuristics；状态—动作轨迹先映射成高层符号概念，规则再通过概率推理柔性偏置探索，而不是修改 reward（§2，p. 3991）。

概述称这种偏置保留底层 RL 算法的 asymptotic convergence guarantees，并报告 discounted return 提升、收敛更快且计算开销有限 [20]。这些是概述转述的结论：本稿没有给保证成立的假设、证明、超参数、数值、重复设计或开销测量，不能据此声称对任意 RL 算法都成立。

### 4. 把符号建议迁移进 DRL 动作选择

第四条工作从较简单问题实例取得符号启发式，再迁移到更复杂环境。逻辑规格识别 promising actions，并直接介入 \(\epsilon\)-greedy DRL 的探索与利用；它不通过 reward shaping 间接改变行为（§2，p. 3991）。

作者报告该框架在长时域、稀疏奖励和多子目标设置中，相对 reward-shaping neuro-symbolic baselines 改善学习效率与表现；对应工作 [21] 已作为 AAMAS 2026 Extended Abstract 接收。概述没有给环境、基线实现、网络、训练预算和数值。仓库另有 [Sample-Efficient Neurosymbolic Deep Reinforcement Learning](./sample-efficient-neurosymbolic-drl.md) 的独立全文笔记；其细节是对 [21] 的单独核验，不应倒灌成这篇博士概述自身的披露。

## 可读规则不等于行为忠实

ILP/ASP 规则是可检查、紧凑的符号对象，但“人能读懂规则”并不证明它在所有状态下忠实复现原神经策略。规则可能只覆盖部分轨迹或状态，也可能在未见状态下与原策略分歧。

§3 正因这一缺口把 quantitative explainability metrics 列为开放方向，计划度量：

- symbolic representation 与 DRL policy 的 behavioral agreement；
- 规则对相关状态/行为的 coverage；
- 跨状态的 consistency。

在这些指标尚未定义和验证前，本文能支持的是规则的可读性与指导用途，而不是已测得的解释忠实度、安全认证或端到端透明性。

## 开放方向

作者计划研究（§3，p. 3991）：

1. 在探索以外的环节使用符号知识，如 policy refinement、skills/behaviors abstraction；
2. 学习更丰富的 temporal、relational 与 hierarchical representations；
3. 复用符号知识以支持相关任务间 transfer；
4. 建立上述解释忠实度量；
5. 将经验中学习的 symbolic abstractions、constraints 或 heuristics 扩展到更多规划应用。

这些是研究计划，不是已完成的迁移、鲁棒性、安全性或广域泛化结果。

## 复现与外推边界

这份三页稿没有给出四条工作线的完整数据/实例版本、样本量、随机种子、超参数、训练步数、网络结构、统计检验、运行时间、代码或数据链接；也没有附上渐近收敛声明的定理条件与证明。可复现时需要分别回到 [18]--[21] 的完整材料。

现有证据覆盖自主驾驶策略抽取、Pocman/Rocksample 规划、tabular RL 在线启发式和被概述的 DRL 迁移工作。它不支持对所有任务的泛化、现实系统鲁棒性、形式化安全保证或特定多智能体协作性能。

## 与 AAMAS 的关系与核验说明

该研究把知识表示、规划和强化学习连接到自主 agent 的长时域决策。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PVRI5073.pdf) 核对 §1--3、四项贡献与 [18]--[21] 的归属，以及开放方向；所有比较性结论均保留为概述所报告的定性证据。
