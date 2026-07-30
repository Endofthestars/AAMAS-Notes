---
title: "LexiCoord: A Multi-Agent Game for Lexical Ambiguity Resolution between Humans and LLMs"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["human_agent_interaction", "marl_coordination", "argumentation_reasoning", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/PPHI2901"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PPHI2901.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05k"
spark_draft_verdict: "needs_revision_after_source_access_page_map_and_mode_errors"
spark_qa_verdict: "needs_revision_corrected_for_page_mode_metric_and_safety_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["agreement_not_semantic_correctness", "agreement_not_task_success_or_safety", "percentage_denominator_ambiguity", "game_count_not_reported", "human_protocol_and_ethics_not_reported", "dataset_and_clarification_bound_not_reported", "model_prompt_and_sampling_config_missing", "no_baseline_or_uncertainty", "observational_disagreement_not_causal", "high_risk_industrial_claim_not_validated", "doi_truncated_in_pdf", "no_code_repository"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_convergence_metric_human_study_percentage_doi_and_high_risk_safety_boundary_check"
escalation_verdict: "pass_after_convergence_page_mode_denominator_reproducibility_and_safety_corrections"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted convergence and human-study check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# LexiCoord: A Multi-Agent Game for Lexical Ambiguity Resolution between Humans and LLMs

## 一句话总结

LexiCoord 是一个让 humans 与 heterogeneous LLM agents 对 ambiguous word 反复选择、说明并澄清 interpretation 的网页协作游戏；demo 报告 99% sessions 达成全体同选，但没有总局数、ground-truth correctness、任务结果、human-study protocol 或安全验证，因此该数字只表示协议内 agreement，不能证明理解正确或高风险协作安全。

## 把词义解释建模为 coordination game

论文令 \(Agt=\{a_1,\ldots,a_n\}\) 为有限非空 agent set，\(\varphi\) 是 natural-language sentence 中的 ambiguous word，\(I=\{\iota_1,\ldots,\iota_n\}\) 是有限 candidate interpretations。作者把每个 interpretation 看作隐式 semantic disjunction 中的一个 disjunct（p. 4056）。

game 按离散 rounds 运行：

1. \(a_1\) 是 coalition leader；
2. 在 \(t=0\)，leader 发出含 \(\varphi\) 的句子并公开 initial interpretation；
3. 在后续 round，每个 agent 选择 \(I\) 中一个 interpretation；
4. 若某轮所有 agents 都选择相同的 \(\iota^*\)，该轮被定义为 convergent。

这个定义只检查 **all-agree**。它没有核对：

- interpretation 是否对应 external ground truth；
- sentence 是否仍有遗漏或语境外含义；
- agents 是否基于同一理由达成一致；
- downstream task 是否正确完成；
- coordinated action 是否安全。

因此一致地选错也会被计为 convergence。

## Tool modes 与交互协议

每个 session 位于 shared browser room，multiple humans 与固定 LLM agents 一起提交 interpretation 和 brief justification（p. 4057）。

- **Automatic mode**：ambiguous sentence 与 candidate meanings 从 predefined dataset 采样；
- **Manual mode**：coalition leader 自定义 sentence、指定 target word，参与者再提交 interpretation 与 justification。

若未全体同意，系统触发 clarification instance，让 coalition 继续迭代，直到 alignment 或 leader 结束 interaction。平台追踪 win/loss statistics，并记录 resolved/unresolved ambiguities、agent decisions 和 clarification depth。

manual mode 不是人工审核或 ground-truth adjudication；leader 结束 session 也不建立解释正确性。

## 实现架构

LexiCoord 是 Node.js backend 的 client–server application（p. 4057）：

- coalition-leader layer 施加 clarification bounds 并聚合 decisions；
- human-interaction layer 通过 WebSockets 支持 browser clients 的 real-time communication；
- LLM-interface layer 异步查询 heterogeneous cloud models 并 normalize outputs；
- 每个 LLM 通过统一 REST-based prompting interface 接收相同 sentence 和 ambiguity specification，再独立返回 interpretation。

文稿说平台可 standalone 运行，也可嵌入更大 multi-agent pipeline；browser client 之外仍需要 internet access 才能做 cloud LLM inference。论文提供 [YouTube demo](https://www.youtube.com/watch?v=ReFltlZVMu8)，但没有给 code repository、deployment package、API schema 或可复现实验脚本。

## 实验设置与百分比口径

作者称进行了 simulation campaign。每局包含（p. 4057）：

- 2 human participants；
- 2 个 Groq-served LLaMA agents；
- 2 个 Mistral agents。

文稿报告：

- 99% converged，1% failed；
- approximately 70% of convergent cases 在 first attempt 解决；
- “remaining 29%”需要 additional iterations；
- 较长 clarification sequence 很少，主要出现在 non-convergent cases。

这些百分比没有对应 total games、raw counts 或 per-mode breakdown。“70% of convergent cases”与随后“remaining 29%”的分母措辞也没有被精确定义，不能仅靠 \(70+29+1=100\) 自行补出 protocol。Figure 1 展示类别分布，但三页稿没有表格原始数值。

## 观察不等于因果

作者观察到：

- humans 起初同意时，coalition 几乎总是立即 converge；
- humans 起初不同意时，clarification 较长，一些 LLMs 会修改 interpretation；
- early human disagreement 似乎能强化 divergent priors。

没有 randomized intervention、matched control、difficulty adjustment 或 counterfactual analysis，所以这些只能作为该 campaign 中的 behaviour description，不能声称 human disagreement 已被证明导致 LLM failure，也不能推断某种 clarification policy 具有因果效果。

## 未报告的复现与人类研究信息

三页稿没有提供：

- predefined dataset 名称、sentence/ambiguity 数、candidate-generation 方法与 train/test split；
- clarification bound、session count、mode distribution 或 failure raw logs；
- human participant 总人数、是否重复参加、招募、语言背景、demographics、compensation；
- informed consent、ethics review、privacy/anonymisation 或 data retention；
- LLaMA/Mistral 具体版本、system/user prompts、temperature、sampling、seed、rate-limit/error handling；
- human-only、LLM-only、majority-vote 或 no-clarification baselines；
- confidence intervals、variance、significance、cross-model/domain robustness；
- semantic ground truth、expert adjudication 或 downstream task evaluation。

因此 99% 不能作为一般 LLM alignment rate、human–LLM understanding rate 或可复现性能保证。

## 高风险场景边界

论文以 safety-critical/high-stakes industrial environments 为动机，并把 LexiCoord 称为 Human–AI high-risk interaction 的 modular test environment。当前证据仅覆盖 lexical agreement protocol，未覆盖机器人动作、工业控制、physical hazard、authorization、failure containment 或 runtime safety。

现实应用至少还需要 independent semantic/ground-truth validation、domain constraints、human authorization、uncertainty/disagreement handling、safe stop、audit/privacy controls 和 downstream task verification。即使全体 agents converge，也不能直接执行高影响动作。

## Future Work

作者明确说当前系统尚未建模 richer discourse context 或 strategic behaviour，并计划与 formal reasoning framework（如引用的 VITAMIN）集成，让 semantic agreement 成为 safe multi-agent decision making 的前置条件（p. 4057）。这仍是 future extension，不是当前 formal safety verification。

## DOI 与页码核验

PDF 的 ACM reference 和页脚只印出 DOI prefix `10.65109/`，遗漏 suffix；DOI resolver 另行确认 `10.65109/PPHI2901` 可解析到该记录，因此仓库登记完整 DOI，同时保留这一 PDF 排版异常。

逐页核对：p. 4056 为 identity、abstract、Introduction、Game Formalization 和 Tool 开端；p. 4057 为 Tool modes、Implementation、Experiments 与 Conclusions；p. 4058 仅为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PPHI2901.pdf) 核对 game semantics、实现、百分比和证据缺口；`reviewed` 不表示 convergence 已证明语义正确、任务成功或高风险系统安全。
