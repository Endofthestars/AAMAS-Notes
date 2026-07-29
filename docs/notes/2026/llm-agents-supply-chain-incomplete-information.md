---
title: "LLM-based Agents in Supply Chain Games: The Role of Incomplete Information and Model Heterogeneity"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "resource_allocation", "marl_coordination"]
dblp_key: ""
doi: "10.65109/UYIA3362"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYIA3362.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "llm_simulation_not_human_evidence", "beer_game_scope", "model_version_sensitivity", "cooperative_information_sharing"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# LLM-based Agents in Supply Chain Games: The Role of Incomplete Information and Model Heterogeneity

## 一句话总结

本文用 DeepSeek‑V3.1、Qwen‑2.5‑32B 与 Llama‑3.1‑8B 扮演 Beer Game 中 retailer、wholesaler、distributor、manufacturer，改变完全/局部/无信息共享以研究 order variance。仿真复现信息共享降低波动的经典方向性模式，并发现只让相邻两家共享信息可产生接近完全共享的稳定性；DeepSeek 最稳定，Qwen 次之，且在 Llama 团队中替换两个关键 agent 可改善整体表现。结论是特定 prompt/model 下的人工社会模拟结果，不是对企业、模型能力或信息政策的因果定论。

## 方法与证据

- 每个 artificial society 是 canonical Beer Game 的四个 firms（S1 retailer 至 S4 manufacturer），在 \(T\) periods 中按 inventory/shipments/orders dynamics 决定 order quantity；每 agent 最小化库存 holding cost 与 backlog cost（§2）。该简化供应链没有价格谈判、capacity/lead-time uncertainty、demand forecast、多产品、contracts、法规、真实 ERP data、strategic misreporting或人类组织流程。
- homogeneous tests 用同一模型占据四个 role，比较 No IS、Full IS、S1–S2/S2–S3/S3–S4 局部 sharing；heterogeneous tests 从全 Llama baseline 出发，以更高 capability model 替换参与 partial pact 的两 agents（§2）。论文把 partial sharing 视作缺乏完全透明时的近似，未定义真实企业中信息字段、权限、泄漏风险、通信成本、隐私/竞争法或 adversarial incentives。
- agents 分别为 DeepSeek‑V3.1、Qwen 2.5‑32B、Llama 3.1‑8B，temperature 1、Chain-of-Thought prompting；每六种 configuration 独立 replication 32 次、20 periods（§2）。没有提供完整 prompts、system messages、API/runtime versions、sampling seeds、token budgets、tooling、context truncation 或 CoT 是否保存/评分，因而难以区分模型 family、规模、prompt 与随机性的影响。
- 以 one-tailed Mann–Whitney U tests 比较 total order variance。Table 1 报 DeepSeek vs Llama 在五种 IS 条件均 \(p<0.001\)，DeepSeek vs Qwen 为 0.002 或 \(<0.001\)，Qwen vs Llama 为 0.004–0.045（§3）。这支持样本内 variance differences；但本文未报告 effect sizes、multiple-comparison correction、variance absolute values/成本、independence check、distribution diagnostics、p-value direction formula 或跨模型成本/延迟。
- Figure 1 的 D‑Llama/Q‑Llama hybrid time series更稳定，order-variance distributions 与纯 Qwen 接近。作者据此称少量高能力 agents 可提升 system-level stability，并称 partial IS 可获 comparable system benefits；证据来自单一 game、20 periods/32 replications及模型模拟，未与 human/企业实验、analytic optimum、传统 inventory policy或 model updates 交叉验证。

## 适用边界与复现

- 可用于探索 LLM multi-agent simulation 对信息结构和模型异质性的敏感性、生成可检验的供应链协作假设；不应用作确定真实企业应共享何种数据、替换员工/供应商、估计业务收益或制定竞争敏感信息政策的唯一依据。
- 复现需公开 Beer Game initial inventory/demand/lead times/costs、全部 role prompt/CoT protocol、model endpoint/version/context/temperature/top-p/max tokens、IS messages的字段/时序、32×20随机 seeds、order-variance definition、all configurations、hybrid replacement roles及统计 analysis。应锁定 model snapshots并存档 raw dialogue/orders，因 hosted-model drift 会改变结果。
- 应扩展到更多 model families/scales/prompt variants、temperature/seed/long horizon、demand shocks/capacity limits/lead-time uncertainty、partial/incorrect/delayed information、incentive conflicts/strategic sharing、human or conventional-controller baselines，以及真实匿名化企业 data。报告 total cost/service level/backlog、information value与privacy/communication cost，而不只看 order variance。
- 在任何现实协作设计中，information-sharing scope 必须依数据治理、保密/竞争法、least privilege、access logging 与独立风险审查决定；模型模拟“局部共享可近似全共享”不能豁免对敏感商业信息、供应商权力不对称和泄露/串通风险的审计。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM-based multi-agent simulation 与供应链协作 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UYIA3362.pdf) 核验四角色 Beer Game、模型/temperature、五种 IS 条件、32 replications/20 periods、Mann–Whitney table 与 hybrid figure；没有把 LLM 生成的 order variance 结果写成真实企业行为、模型普适能力或信息共享政策的保证。
