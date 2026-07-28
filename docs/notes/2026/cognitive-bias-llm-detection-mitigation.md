---
title: "Exploring Cognitive Bias Impact, Detection and Mitigation in Large Language Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "safety_verification", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/ZAVA7707"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ZAVA7707.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_prompt_induced_bias", "limited_bias_taxonomy", "binary_task_scope", "warning_prompt_mitigation", "not_human_psychology_measurement"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Exploring Cognitive Bias Impact, Detection and Mitigation in Large Language Models

## 一句话总结

本文用 prompt template 在 BigBench Hard 衍生二元任务中诱导 acquiescence、availability、bandwagon 三类“cognitive bias”，再让模型/RAG ReAct agent 检测并用 bias-aware warning prompt 缓解；结果说明这些 textual interventions 会改变准确率，但不证明 LLM 具有/消除了人类心理意义的认知偏差，也不覆盖真实高风险决策。

## 方法与证据

- 三阶段框架：Module 1 比较 unbiased、prompt 中直接诱导 bias、以及先答后 follow-up 注入 bias 的性能；Module 2 进行 binary bias detection 和 bias-type classification；Module 3 在偏置后插入 context-aware warning 后重测（§4）。
- 数据来自 maveriq/bigbenchhard，聚焦 navigate 与 sports_understanding；构建 3,748 instances，含 unbiased 与 band-biased 等条件，使用明确的 bias-inducing prompt templates（§4.1、Table 1--2）。
- detection 比较 reasoning model QwQ 与 LLaMA 3.3 70B ReAct/LangChain + retrieval；论文称 QwQ 领先，而 ReAct with structured reasoning/external knowledge 可接近 dedicated reasoning model（§5.2）。
- mitigation 使用生成的 warning 指出可能 bias、鼓励 alternative perspective。各模型相对 biased condition accuracy 提升，部分超过原 unbiased baseline；作者将其解释为 intervention 促使更审慎 reasoning，而非只移除 bias（§4.3、§5.3）。
- 作者指出 acquiescence impact 最显著，并在 conclusion 承认只测试三类 bias、binary decisions 和有限 prompt settings；未来需扩展到 collective decision/voting、多轮动态策略与更多 biases（§5--6）。

## 安全边界与复现

- 这些是人为插入文本 cue 对 benchmark answers 的影响，不是对模型内部认知机制、人类心理状态、社会偏见、意图或真实决策过程的测量；“cognitive bias”应按 operational prompt behavior 解读。
- warning prompt 可能引入额外线索、改变 task formulation 或过拟合模板；超过 unbiased baseline 不能证明在分布外、安全关键或人与模型互动中可靠缓解偏差。
- 三 bias/二元任务覆盖远小于认知偏差 taxonomy，且 ground truth、工具检索资料和 model versions 会影响 detection F1/accuracy；不得将其直接用于医疗、法律、招聘、金融等实际公平/合规结论。
- 复现应发布所有 templates、BigBench task splits、model versions/temperatures、RAG corpus/retrieval settings、warning generation prompts、exact scoring、seeds 与 counterfactual ablations；实际部署需 domain validation、human oversight、fairness/harms auditing 与 abstention/escalation。

## 与 AAMAS 的关系与核验说明

这是 LLM 可靠性、RAG agent 与 bias-aware prompting 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ZAVA7707.pdf) 核对三模块、3,748-instance setup、三 bias、RAG detection 与 conclusion limitations；没有把模板诱导的 benchmark 行为表述为真实心理偏差或通用风险缓解。
