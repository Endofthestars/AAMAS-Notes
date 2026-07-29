---
title: "RouterHGC: Optimized Router for LLM-based Multi-Agent Systems via Heterogeneous Graph Contrastive Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "marl_coordination"]
dblp_key: ""
doi: "10.65109/PGWI7290"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PGWI7290.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "llm_multi_agent_routing", "heterogeneous_gnn", "contrastive_learning", "benchmark_cost_measurement", "not_reliability_or_security_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# RouterHGC: Optimized Router for LLM-based Multi-Agent Systems via Heterogeneous Graph Contrastive Learning

## 一句话总结

RouterHGC 将每个 query 的 MAS configuration 选择写成 heterogeneous graph path：query → collaboration mode → agent roles → LLM backbones；HGNN 表示高阶关系，再以 performance–cost reward 选出的高质量/相似 query graphs 为 positives、低准确或高成本 configurations 为 negatives，联合 global graph contrastive 与 local edge losses。五个 benchmarks 的 Table 1 报平均 accuracy 84.17%，HotpotQA 相对 MasRouter inference cost 降 27.4%。这些是特定候选模式、roles、models、reward/cost 和 benchmark 的离线路由结果，不是任意真实 agent service 的质量、时延、隐私、安全或成本承诺。

## 方法与证据

- graph nodes 为 user queries \(V_q\)、collaboration modes \(V_p\)（如 CoT/Debate）、roles \(V_r\)（如 Coder/Reviewer）、LLM backbones \(V_m\)。决策从 query 依次选 mode、roles、role-to-model edges；这将 configuration space 限制为预定义 node/edge/catalog，未涵盖动态 tool availability、agent state、context length、rate limit、permissions或 cross-request resource contention。
- reward 为 \(\alpha\cdot Performance-\beta\cdot Cost\)（Eq. 1）。global InfoNCE-style loss 把当前 query 的 highest-reward configuration 和 semantic-similar queries 的 optimal graphs 作 positives，把低 accuracy 或相对 performance 过高 cost 作 negatives（Eq. 2）；local edge MSE 用 optimal routing-path label \(y_{uv}\) 监督 edge probability（Eq. 3）。标签与模型学习的是该 reward 的偏好，非事实正确性、user satisfaction、fairness、tool safety或 robustness 标签。
- Table 1 比较 Vanilla、CoT、Complex-CoT、SC、Debate、AFlow、DyLAN、RouterDC、MasRouter。RouterHGC 在 GSM8K 96.37、MATH 72.15、HumanEval 90.53、HotpotQA 78.88，CMMLU 82.93（后者低于 MasRouter 83.18），作者计算五集平均 84.17%；摘要所称“highest average”应按这五项/所列 baselines，而不意味着每个数据集第一或 statistical significance。
- 文中称 MATH 相对 MasRouter 增 1.64%，HotpotQA inference cost 降 27.4%。没有披露实际 LLM providers/versions/prices、token accounting、hardware、cache、routing-training cost、latency percentiles、confidence intervals、test contamination/selection protocol或 failure cases；离线 benchmark cost 不能直接推算生产账单。
- future work 是 edge computing scalability/adaptability；摘要未评估 adversarial queries、prompt injection、malicious agent/tool outputs、privacy-sensitive routing、model outages、budget exhaustion或 quality degradation after model updates。

## 适用边界与复现

- 适合以受控 candidate catalog 优化 MAS pre-response configuration 的研究；生产使用需把 router 当建议/调度层，配合 model allowlists、access control、privacy/data-residency policy、tool sandboxing、per-request budget/timeout、fallback、monitoring和 human escalation。选择较便宜模型不能降低高风险任务的验证要求。
- 复现需公开 datasets/splits、query embeddings、heterogeneous schema/nodes/edges、available modes/roles/models、performance/cost measurement、\(\alpha,\beta,\lambda_1,\lambda_2,\tau\)、positive/negative sampling、HGNN/optimizer、optimal-path label generation、baselines及 token/model-version/pricing/seeds。报告 training+inference cost、latency、accuracy/CI、per-domain routes和 abstain/fallback rates。
- 应测 model price/capability drift、新 queries/domains、long/multilingual/adversarial prompts、unseen collaboration patterns、agent/tool failures、parallel load、privacy-constrained choices和 end-to-end factual/task success。审计 reward design 对昂贵但必要的 safety review、minority domains与 latency-sensitive users的影响。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM MAS routing 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PGWI7290.pdf) 核验 four-node graph/path、reward/losses、Table 1 数值、84.17 average 和 27.4% HotpotQA cost claim；没有把 benchmark routing 写成真实服务可靠性、安全或成本保证。
