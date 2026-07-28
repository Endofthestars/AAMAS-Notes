---
title: "GroupDebate: Enhancing the Efficiency of Multi-Agent Debate Using Group Discussion"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/DSDX8860"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DSDX8860.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["gpt_35_specific_evaluation", "prompt_and_tokenizer_dependence", "five_run_evaluation", "benchmark_reasoning_only", "context_limit_baseline_failure"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# GroupDebate: Enhancing the Efficiency of Multi-Agent Debate Using Group Discussion

## 一句话总结

GroupDebate 把多 agent 辩论分组做组内讨论，再交换各组 interim summary，以降低所有人全互看历史造成的上下文膨胀；在 GPT-3.5-turbo-0125 的五类推理 benchmark 上，论文报告 token 最多降 46.9%、特定配置 accuracy 最多升 21.9%，但两项并非所有任务/配置的同时保证。

## 方法与证据

- GD 将 `N` agents 划为多组，组内多轮辩论后共享阶段性结论；用 forget/summary 机制控制跨组上下文，最后生成共识答案（§3）。
- 与 Multi-Agent Debate (MAD)、CoT、CoT-SC(40) 比较，主要评估 total token 与 accuracy；实验使用 GPT-3.5-turbo-0125，所有 baseline 和 GD 各独立运行 5 次取平均（§4）。
- 数据包括 Arithmetic、GSM8K、MMLU、MATH、GPQA；token reduction 的论文最高值依次可达 34.8/45.2/46.9/39.3/30.6%。MATH 上部分 MAD(6,3)/(6,4) 因 GPT-3.5 context limit 无结果（§4）。
- group number、agent/round 和 group-internal rounds 会改变结果；例如 MMLU 的 3+3 strategy 最好，过多 rounds 可降低 accuracy，说明不存在单一固定最优配置（§4--5）。

## 局限与复现

- 结论针对固定模型、prompts、tokenizer、context window 与 reasoning datasets；API 版本、系统提示、采样参数、模型价格和上下文长度变化会改变 token/accuracy tradeoff。
- MAD 在 context overflow 时失败，因此“token 节省”部分也反映 baseline 可运行性差异；应报告 prompt tokens、completion tokens、summary tokens、失败率与 wall-clock latency，而非仅总 token。
- 五次重复不足以证明小差异；复现应公开问题子集、agent personas、temperature、seed、stopping/consensus rule、group assignment 与逐 run 输出，并在更新的闭源和开源模型上再测。
- 作者指出为什么分组提高 accuracy、给定 token budget 下如何选最优参数仍不清楚；应将其作为调度启发式而非通用可靠性机制（§5）。

## 与 AAMAS 的关系与核验说明

本文研究 LLM multi-agent collaborative reasoning 的通信成本。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DSDX8860.pdf) 核对流程、模型、数据集、五次运行、context-limit 失败及参数敏感性；未把 benchmark 指标外推为真实任务准确性或成本承诺。
