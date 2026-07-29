---
title: "AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "generative_agents", "resource_allocation"]
dblp_key: ""
doi: "10.65109/UJUM3065"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UJUM3065.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "supply_chain_decision_support", "deterministic_simulation", "retrieval_from_rl_evaluation_logs", "not_operational_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval

## 一句话总结

本文针对 multi-echelon inventory management，用固定的 stepwise decision prompt 与 safety-stock strategy 指导 LLM ordering；AIM-RM 再将历史 \((state\ embedding, order, reward)\) 按 Euclidean similarity 检索并作为上下文。五个确定性 demand/tier scenarios 中，预载 IPPO evaluation logs 的 AIM-RM 在非-RL methods 中最佳、平均 relative optimality gap 91.27%，而 IPPO/MAPPO 为 42.79/34.04%。这说明特定模拟、提示和日志条件下可改善 LLM agent 的订单决策，不证明最优、鲁棒、可审计或适合真实供应链自主执行。

## 方法与证据

- environment 是 \(M\)-tier chain：每 tier 生产/运输有 capacity、lead time、inventory/backlog，period reward 由 sales/order/backlog/holding costs 构成；每 agent 观察库存、backlog与时间信息（§2.1）。它未包含真实需求噪声、供应中断、价格/合同、质量/损耗、碳/法规、财务约束、数据延迟或人为流程。
- decision module 向 LLM 输入 state、history、natural-language demand description，并要求 order quantity+rationale。PSD 显式列决策步骤；PSS 将 lead-time inventory 与 forecast demand 结合的 safety stock 加入 prompt（§2.2）。prompt 对措辞/模型版本敏感，rationale 不是订单最优性/可执行性的证据；安全库存会在时变需求下失配，作者的 Table 1 正显示其大幅退化。
- AIM-RM memory 为 \(M_m=\{(\phi(s_{m,t}),O_{m,t},P_{m,t})\}\)，embedding Euclidean distance 低于 threshold 的最多 K 条 experience 被检索。AIM-RM(w/ RL log) 用 IPPO evaluation data 的 historical logs 预初始化，w/o RL log 仅在当前 episode 记录（§2.2–3）。这使表现依赖 log provenance/coverage和与测试 scenario 的相似性；使用 evaluation logs 不能与独立真实历史数据或 zero-shot 适配混同。
- 五个 deterministic scenarios 为 uniform/diverse tiers × constant/increasing/decreasing demand，每个平均 total reward 仅为 5 episodes；测试 OpenAI o4-mini medium reasoning，metrics 是 relative gap \(\Delta=|(Opt-r)/Opt|\)（Table 1, §3）。样本数、prompt/temperature、模型调用、seeds/CI、optimal solver与 log/test separation未在摘要完整披露。
- Table 1 AIM-RM(w/RL log) gaps为 60.00/56.02/171.11/95.12/74.09，平均91.27；AIM-RM(w/o)平均138.59，InvAgent variants 122.85/167.33，IPPO/MAPPO 42.79/34.04。固定 prompt + safety stock 仅 Const-Uni 0.00，其他最大425。因 gap 越低越好，AIM-RM 并非总体最优；“comparable to RL”只是部分/定性陈述，表中平均差距仍明显。

## 适用边界与复现

- 适合受控模拟中的 LLM decision support/experience retrieval 研究；不应自动采购、生产、配货或承诺 service levels。真实供应链使用需人类审批、库存/预算/容量硬约束、异常升级、审计、供应商权限与可回滚执行。
- 复现需给 all tier parameters/lead times/capacities/costs、五 scenario/time horizon/Opt definition、o4-mini version/prompt/decoding、PSD/PSS/PMU templates、embedding model/threshold/K、RL log generation与严格 train/eval split、InvAgent/heuristic/RL configs、episodes/seeds/CI及 costs/rewards。分开评估检索质量、prompt effect 和 coordination effect。
- 应测 stochastic/seasonal/adversarial demand、supplier failures、longer horizons、distribution shift、missing/late data、new tiers、cost changes、memory poisoning/irrelevant retrieval、model outages和 human overrides；报告 fill rate/backlog/service/cash/holding/waste、worst case及 total LLM latency/cost。任何生产化必须验证网络/数据安全、商业保密、需求公平和操作风险。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM multi-agent/resource allocation 应用扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UJUM3065.pdf) 核验 multi-echelon model、PSD/PSS/AIM-RM、IPPO-log memory、五 deterministic scenarios及 Table 1；没有把模拟 gap 或 agent rationale写成现实供应链最优性、鲁棒性或自主运营安全证明。
