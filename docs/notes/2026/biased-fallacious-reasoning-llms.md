---
title: "Towards Detecting, Mitigating and Explaining Biased and Fallacious Reasoning in Large Language Models"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["generative_agents", "argumentation_reasoning", "safety_verification", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/GNAS4540"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GNAS4540.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04v"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_model_and_task_separation_revision"
spark_consistency: "pass_after_terra_causal_boundary_revision"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "cognitive_bias_induction", "argument_scheme_classification", "warning_based_mitigation", "system2_interpretation", "limited_statistical_reporting", "future_multi_agent_framework"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_metric_attribution_and_system2_causal_boundary_check"
escalation_verdict: "pass_after_task_separation_and_interpretive_claim_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted metric/causal-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Towards Detecting, Mitigating and Explaining Biased and Fallacious Reasoning in Large Language Models

## 一句话总结

本文汇总两项博士研究里程碑：用 argumentation schemes 与 critical questions 辅助虚假信息分析，以及在模板诱导的三类认知偏见上评估、检测并用提示警告缓解 LLM 错误；现有指标来自特定语料和实验，不能证明模型获得了真正的 System 2 推理、普遍鲁棒性或伦理对齐。

## 研究问题与假设

作者把 cognitive biases（CBs）与谬误论证视为 LLM 复制和放大错误信息的一条来源。研究假设是：增强 argumentative 和 explanatory capacities，能够在 **交互层** 改善偏见/谬误检测与缓解，而不是从模型内部消除偏见。

Dual Process Theory 在文中提供解释框架：zero-shot 被类比为快速启发式的 System 1，chain-of-thought 被类比为显式审慎的 System 2。这是理论映射，不是对模型内部认知过程的测量。文中提到医疗 LLM 诊断准确率下降 \(26\%\) 也来自外部文献 [14]，并非本研究实验（§1，p. 3966）。

## 里程碑一：论证方案与虚假信息

文献 [5] 的 web-based 工具包含两个模块。

### Argument Scheme 分类器

- 修改版 NLAS-MULTI 包含 19 个 argumentation schemes，并增加 `no scheme`，共 20 类。
- RASA 两层分类器先判断 Source-Based、Rule-Application 或 Reasoning argument group，再细分具体 scheme；它被报告为持续优于单层分类器。
- 在这一特定 20 类语料设置中，accuracy 与 F1 报告在 \(0.85\)–\(0.87\) 之间。概述没有说明各自数值、F1 averaging、数据划分、样本量或置信区间，不能把该区间视为事实核验或真实开放论证的整体鲁棒性（§2，pp. 3966–3967）。

### Veracity Generator and Evaluator

- 系统根据识别出的 scheme 生成 Critical Questions，并并行检索 Google、Wikipedia 和 Bing。
- 量化的 LLaMA 3 70B 综合上下文，以 computational argumentation assistant 的形式给出定量和定性真伪理由。
- 80 名 18–65 岁参与者中，\(83.8\%\) 对回答的连贯性和来源充分性表示满意。

这个比例评价的是用户感知的 coherence/source adequacy，不是客观真实性、AS 分类准确率、偏见缓解效果或长期信任；本稿没有给招募、量表、对照组、来源正确性审计或统计不确定性（§2，p. 3967）。

## 里程碑二：认知偏见三模块

### 1. 诱导与影响评估

文献 [6] 在 maveriq/bigbench-hard 的 YES/NO 项上，为每题构造一个 unbiased 版本以及 acquiescence、availability、bandwagon 三个模板诱导版本，并比较单步改写与回答后的两步诱导。被测模型为 LLaMA 3.2、LLaMA 3.3:70B、Qwen 2.5、DeepSeek-V2 和 GPT-4o。

实验报告偏见条件下一致的性能下降，迎合偏见和两步交互尤其明显。LLaMA 3.3:70B 的迎合偏见 accuracy 从 \(0.85\) 降到 \(0.66\)（单步），从 \(0.84\) 降到 \(0.16\)（两步）。这是该数据构造与提示模板下的结果，不是所有对话或现实任务中的一般效应（§3，p. 3967）。

### 2. 检测与分类

- 对比 QwQ、DeepSeek-V1 两个 reasoning models，以及配置为 ReAct agent 的 LLaMA 3.3:70B；三者都使用基于认知理论知识的 RAG。
- 二分类（biased/unbiased）只报告 QwQ 最高、LLaMA ReAct 紧随其后，没有具体 F1。
- 更复杂的四分类中，QwQ 的 F1 分别是 unbiased \(0.65\)、acquiescence \(0.12\)、availability \(0.91\)、bandwagon \(1.00\)。这些是 **QwQ 多类偏见检测** 指标，不是前述五个生成模型的任务准确率。
- 所有模型都难以识别 acquiescence，常把它判成 unbiased（§3，p. 3967）。

### 3. 警告式缓解

以 QwQ 检测结果生成简短、上下文相关的偏见解释，再把警告附加到原偏置 prompt。作者报告各模型 accuracy 提升，并称 GPT-4o 与 LLaMA 3.2 在若干情形超过 unbiased baseline；概述没有逐模型幅度、显著性、误检传播或副作用分析。

“警告触发了更审慎的 System-2-like 推理”和“提高 interpretive robustness”是作者依据准确率变化提出的解释性推断，未测量内部机制或独立鲁棒性指标，不能写成已建立的因果机制（§3，p. 3967）。

## 未来多智能体方向

- 由专门化专家 agents 进行集体推理、投票和伦理审议；
- 在模拟环境中研究论证动态与错误传播；
- 把 AS/CQ 扩展到 CB 分析，覆盖更多偏见和多轮放大；
- 探索人类价值、心理因素与偏见之间的关系。

这些均是未来计划；反思性、value-aligned 和 transparent decision-making 是目标，不是现有两个里程碑已经验证的性质（§4，p. 3967）。

## 证据与复现边界

- [5] 是论证方案/虚假信息里程碑，[6] 是认知偏见影响、检测和警告缓解实验；当前三页稿负责整合研究路线与未来方向。
- 本稿没有项目代码仓库、数据下载、完整配置或部署工件链接。唯一脚注链接指向外部 Cognitive Bias Codex，不是本研究实现。
- 缺少完整实验表、显著性、方差、跨语言和广任务验证；迎合偏见 F1 \(0.12\) 与两步诱导下 accuracy \(0.16\) 也表明当前方法仍有明显薄弱点（pp. 3966–3968）。

## 与 AAMAS 的关系与核验说明

本文连接 computational argumentation、LLM agents、misinformation、cognitive science 与 Responsible AI。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GNAS4540.pdf) 核对 §2 的两个工具模块、§3 的三类实验及 §4 的未来 MAS；未混淆 AS 分类指标、QwQ 多类 F1 和外部医疗研究结果。
