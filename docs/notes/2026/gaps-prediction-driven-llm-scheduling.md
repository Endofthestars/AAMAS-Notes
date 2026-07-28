---
title: "GAPS: Global-Aware Prediction-driven Scheduling for Large-Scale LLM Inference"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "generative_agents"]
dblp_key: ""
doi: "10.65109/YPTR3460"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YPTR3460.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["discrete_event_simulation_only", "prediction_and_workload_model_dependence", "migration_cost_model_scope", "no_production_or_heterogeneous_cluster_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# GAPS: Global-Aware Prediction-driven Scheduling for Large-Scale LLM Inference

## 一句话总结

GAPS 用全局队列监控、预测 completion cost 的 bias-aware deadline 和选择性迁移调度 LLM inference requests；在 Azure trace 驱动的离散事件模拟中改善 P99/SLO，但结果取决于预测器、迁移成本模型、queueing simulator 和 workload replay，尚无 production 集群或异构部署验证。

## 方法与证据

- 将 P99 latency、SLO violation 与 migration cost 加权为 NP-hard assignment/ordering 问题；GAPS 以 `O(M)` assignment、最坏 `O(NM)` migration 的启发式近似，低利用率按 queue、较高利用率结合预测 cost（§3--4）。
- 用 online MAE/MAPE 误差做 deadline calibration；仅当预期 latency gain 大于迁移成本时迁移，候选来自长预测完成时间/紧 deadline/overload request（§4）。
- simulator 以 Azure code/conversational traces，4/8/16/32 GPU，3 seeds，比 Splitwise、Llumnix、FlashGen 及 NoPred/NoRebal/NoGlobal。报告 P99 最多低 25%、SLO violation 低 10--15 points；throughput 因无稳定优势而未评测（§5）。
- 对预测器人工注入 0--40% error；GAPS 在 30--40% 时渐进退化。论文将生产、heterogeneous/multimodal cluster 留作未来工作（§5--6）。

## 局限与复现

- Azure traces 是 workload 输入，不是实际执行；GPU kernel、KV cache、prefill/decode、network/migration、autoscaling、failure 和多租户公平性的 simulator 实现决定结论。
- P99/SLO 优化权重、utilization threshold、prediction bias calibration 和 migration cost 都是策略参数；不同 SLO、模型、tokenizer、cache/parallelism 或 arrival burst 可改变排序。
- 三 seeds 和模拟统计不足以证明 production tail reliability；没有吞吐稳定优势，也无成本/能耗、公平性或请求取消/重试分析。
- 复现应公开 simulator、Azure preprocessing、predictor/误差注入、所有参数、baseline commits、GPU/cluster model、seed 和原始 P99/SLO/migration/throughput；须在真实 homogeneous 与 heterogeneous cluster 上验证。

## 与 AAMAS 的关系与核验说明

该文研究生成式 agent 服务的集群资源调度。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YPTR3460.pdf) 核对系统、复杂度、simulator 设置、图 3--5 与未来工作；未把 trace-driven simulator 改善外推为生产 LLM 服务保证。
