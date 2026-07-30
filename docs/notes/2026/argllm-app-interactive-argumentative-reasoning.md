---
title: "ArgLLM-App: An Interactive System for Argumentative Reasoning with Large Language Models"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["argumentation_reasoning", "generative_agents", "human_agent_interaction", "safety_verification", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/NWEK7590"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NWEK7590.pdf"
demo_url: "https://youtu.be/vzwlGOr0sPM"
app_url: "https://argllm.app"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05r"
spark_draft_verdict: "source_grounded_with_prior_evaluation_breadth_default_full_rag_and_faithfulness_boundaries"
spark_qa_verdict: "pass_with_final_note_expansion_for_unreported_accuracy_faithfulness_contestability_usability_robustness_and_grounding_evaluation"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["prior_argllm_results_not_demo_evaluation", "decision_accuracy_not_evaluated", "faithfulness_and_contestability_not_evaluated", "usability_and_cognitive_load_not_evaluated", "llm_generated_arguments_and_base_scores_may_be_false", "formal_qbaf_strength_not_world_truth", "user_supplied_trust_not_verified", "pdf_grounding_and_citations_not_evaluated", "full_autonomous_rag_not_current", "multi_agent_variant_not_current", "uploaded_pdf_privacy_unreported", "api_key_handling_unreported", "prompt_injection_and_malicious_document_risk", "sensitive_decision_support", "user_score_and_graph_manipulation", "provenance_access_audit_and_retention_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_prior_evaluation_qbaf_world_truth_faithfulness_user_contestability_document_grounding_prompt_injection_api_key_and_sensitive_decision_boundary_check"
escalation_verdict: "needs_revision_corrected_for_current_scope_evaluation_faithfulness_document_trust_security_and_sensitive_decision_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted formal-reasoning, faithfulness, and document-security check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# ArgLLM-App: An Interactive System for Argumentative Reasoning with Large Language Models

## 一句话总结

ArgLLM-App 把 LLM 生成的支持/攻击 arguments 组织成可调 QBAF，让用户通过图、slider、Add buttons 或 chat 修改论证并重新计算 binary decision；该 demo 没有报告决策准确率、faithfulness、contestability 或 usability，形式化强度计算也不保证生成论点、base scores 或现实结论为真。

## Demo 与 prior-work 边界

ArgLLM-App 是 binary decision-making 的 interactive web prototype，不是本稿提出的新 base model，也不是当前 multi-agent system（pp. 4101–4102）。

Introduction 引用 prior ArgLLM work [3]，称其在 claim verification 上 effective，并可与 chain-of-thought 等技术竞争。那些结果属于 AAAI 2025 的既有研究，不是本 demo paper 重新运行或报告的 evaluation。

本稿主要描述 UI、QBAF configuration、human modification 与 document input，没有 quantitative experiment section。

## QBAF 形式

Quantitative Bipolar Argumentation Framework（QBAF）定义为（p. 4101）：

\[
(A,R^{-},R^{+},\tau),
\]

其中：

- \(A\) 是 finite set of arguments；
- \(R^{-}\subseteq A\times A\) 是 attack relation；
- \(R^{+}\subseteq A\times A\) 是 support relation；
- 两个 binary relations disjoint；
- \(\tau:A\rightarrow[0,1]\) 是 base score function。

arguments 在 graph 中是 nodes，attack/support 是 red/green edges。underpinning LLM 通过 direct questioning 设定 base confidence，即 \(\tau\)。

final argument strength 由 gradual semantics
\(\sigma:A\rightarrow[0,1]\) 计算，通常从 base scores 初始化，再根据 attackers/supporters 的 strengths 迭代更新。

## 支持的 semantics

ArgLLM-App 可选择（p. 4102）：

- DF-QuAD；
- Euler-based semantics；
- Quadratic Energy semantics。

Figure 1 示例使用 DF-QuAD。选择一个 formal semantics 能让给定 graph/base scores 的计算规则明确，但不能验证输入 arguments 或 \(\tau\) 的事实正确性。

## Depth 与 breadth

prior ArgLLMs 把 QBAF 限制为以 claim 为 root 的 trees（pp. 4101–4102）：

- depth 1：claim 只有一层 attackers/supporters；
- depth 2：一阶 evidence 自己也有 attacker/supporter；
- prior setting 的 breadth 为 1。

ArgLLM-App 提供：

- QBAF depth 1 或 2；
- breadth up to 4，即每个 argument 最多四个 attackers 与四个 supporters，数量相同。

系统把 depth 限为 2 的理由是避免 overloading users。这是 design rationale，不是通过 cognitive-load user study 得出的阈值。

## 用户交互与 reassessment

用户可以（p. 4102）：

- 用 base-confidence slider 修改 argument 的 \(\tau\)；
- 通过 Add buttons 添加 supporter 或 attacker；
- 直接在 QBAF visualization 操作；
- 通过 chat 提供信息，由系统转成相关 argument 的 attacker/supporter。

修改 graph 或 base scores 后，ArgLLM-App 按选择的 semantics 重新评估 binary decision。

这提供了可 contest 的操作界面，但论文没有研究用户能否可靠发现错误、修改是否提升准确率，或不同用户是否产生一致结果。

## Document-based QBAF generation

用户可以上传自己认为 trusted 的 PDF（pp. 4101–4102）：

1. PDF 被 parsed to Markdown；
2. content 被 incorporated into LLM prompts；
3. LLM 使用文档内容生成 QBAF。

系统没有说明如何验证 PDF 是否 trustworthy、如何检索精确 supporting passage、如何附 citation，或如何处理冲突来源。

这是 user-supplied document augmentation，论文称其 “in the spirit of RAG”。让 agents autonomously find relevant sources 并 extract arguments 的 full RAG integration 明确属于 Future Work。

## 当前能力与 Future Work

当前 realization 只支持（p. 4102）：

- OpenAI base LLMs；
- single LLM；
- one binary decision；
- single user；
- PDF input。

Future Work 才包括：

- higher depth；
- other document formats；
- alternative base-confidence methods；
- other LLM providers；
- multi-agent variants with different LLMs；
- multiple decisions/question answering；
- autonomous source finding/extraction 的 fuller RAG；
- multiple concurrent users。

这些未来方向不能列为当前已实现功能。

## 本稿没有评测什么

三页 demo 没有报告：

- decision accuracy；
- 与 prior ArgLLM/CoT 的复现实验；
- generated argument factuality；
- base-score calibration；
- explanation faithfulness；
- user contestability effectiveness；
- usability、task time 或 cognitive load；
- robustness 或 sensitivity to depth/breadth/semantics；
- PDF grounding、retrieval、citation 或 hallucination metrics；
- adversarial/prompt-injection testing。

app 能展示和修改 reasoning artifact，不等于 artifact faithfully 暴露了 underlying LLM 的内部因果过程。

## Formal reasoning 与 world truth

QBAF semantics 对当前 \(A,R^{-},R^{+},\tau\) 计算 \(\sigma\)。如果 LLM：

- 生成了 false/misleading argument；
- 遗漏关键 evidence；
- 错分 attack/support relation；
- 给出 miscalibrated base score；

formal computation 仍可以产生数值上确定的结果。这个结果对构造的 QBAF 有定义，不构成现实世界 claim truth 或 decision correctness guarantee。

同样，用户能 contest graph 表示界面允许 intervention；论文没有证明人类一定能识别错误或避免 automation bias。

## Security、privacy 与治理缺口

三页稿没有说明：

- uploaded PDF 的 confidentiality、retention、deletion 与 access scope；
- user API key 的 storage、transmission 和 redaction；
- prompt injection 或 malicious PDF defenses；
- PDF parser/file handling security；
- argument/source provenance 与 immutable audit trail；
- sensitive legal、medical、financial 或 policy decisions 的 refusal/escalation；
- 多次调整 slider/graph 后的 manipulation detection；
- user identity、authorization 与 session isolation。

把文档称为 trusted 不会自动使其可信，也不阻止恶意指令、错误内容或偏见进入 prompts。

## 资源与页码核验

论文称 web application 公开于 [argllm.app](https://argllm.app)，并提供 [demo video](https://youtu.be/vzwlGOr0sPM)；三页稿没有给出 code repository。

PDF 逐页核对：p. 4101 为 identity、Abstract、Introduction 与 Preliminaries；p. 4102 为 Figure 1、depth/breadth continuation、ArgLLM-App Features、Figure 2 与 Future Work；p. 4103 为 Acknowledgements 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NWEK7590.pdf) 核验；`reviewed` 不表示 decision accuracy、world truth、faithfulness、contestability 或 document security 已经验证。
