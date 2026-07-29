---
title: "RAC: Request-adaptive Configuration for Efficient Speculative Decoding"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/SGXL4097"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SGXL4097.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "single_target_model_family", "benchmark_throughput_evaluation", "request_history_dependency", "serving_overhead_unreported"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# RAC: Request-adaptive Configuration for Efficient Speculative Decoding

## 一句话总结

RAC 将每次投机解码的 draft model 与 speculative length 选择建模为 MDP：state 合并当前请求的 embedding/task/input length/perplexity 与最近 \(k\) 个请求的执行反馈，diffusion-based SAC policy 以相对自回归 token speed 为 reward。它在 Vicuna-33B、HumanEval/GSM8K/Hybrid 上报告最高 2.021× 相对 AR、1.37× 相对 vanilla speculative decoding 的速度提升；这不直接说明端到端延迟、成本、生成质量或多租户服务表现。

## 方法与证据

- state \(s_t=[f_t,h_t]\)：当前特征 \(f_t\) 由语义 embedding、task type、input length、不同 draft model 下的 perplexity 组成，\(h_t\) 汇总过去 \(k\) 个请求的配置和性能（§2）。历史相关性是其核心假设；若请求流突然变化、跨用户混合、历史不代表当前或特征在线计算昂贵，选择可能退化或引入隔离/隐私问题。
- action 是 draft-model pool 与 speculative lengths 的组合；reward 是该配置 token generation speed 与平均 autoregressive speed 的比值。策略使用 diffusion-based policy integrated with Soft Actor-Critic（§2）。目标仅优化 tokens/s，未在摘要中将 acceptance rate、TTFT、尾延迟、GPU memory、能耗、draft/feature/RL 推理开销、队列效应或输出等价性纳入 reward。
- 实验以 Vicuna-33B-v1.3 为 target、Vicuna-160M/68M 为 draft pool，候选 speculative length 为 3–10；基准为 HumanEval、GSM8K、Hybrid，并比较 fixed SD、Lookahead、PLD、SAM-Decoding、Assisted Generation、SWIFT（§3）。这是非常具体的 model/hardware/implementation 条件，摘要没有给设备、batch/concurrency、sampling、prompt length 分布或精确质量校验。
- Table 1 的 RAC tokens/s 为 HumanEval 59.343（2.021×）、GSM8K 54.472（1.819×）、Hybrid 50.030（1.695×），平均 1.845×；vanilla SD 平均 1.432×，故后者相对的最大差异约为 1.37×（§3）。这些是吞吐 speedup，不是对模型准确性、代码可执行率、数学正确性或用户体验的结论。

## 适用边界与复现

- 适合探索已有 target/draft 模型池内的在线推理配置选择；不应把 benchmark speedup 宣称为任何 LLM、所有请求流或生产 SLA 的保证。对于安全/高正确性任务，应单独验证投机采样的分布等价性、输出验证与回退路径。
- 复现需公开 target/draft 权重与版本、tokenizer/decoding、硬件和软件栈、batch/并发、各数据集 prompt 与 warm-up、state feature/perplexity 的计算预算、history length/重置规则、action space、SAC/diffusion 网络和训练轨迹、seeds及所有 baseline 调参。报告 tokens/s 之外的 TTFT、p50/p95 latency、memory、能耗、acceptance rate和输出一致性。
- 应做 workload shift、长上下文、streaming、不同温度/采样、缓存命中、异质用户和多 GPU/多租户测试；对历史反馈做 tenant isolation、过期/漂移检测和 ablation。若该控制器在请求间保留特征或文本派生表示，部署还需数据最小化、访问控制和审计。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 RL agent/LLM inference optimization 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SGXL4097.pdf) 核验 MDP state/action/reward、diffusion-SAC、Vicuna 设置与 Table 1；没有把速度数字写成质量提升、普适部署收益或无隐私/系统代价的结论。
