---
title: "Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/FKYO8341"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FKYO8341.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["benchmark_only_evidence", "online_memory_self_modification", "llm_extraction_error", "cost_comparison_scope", "manual_hyperparameter_selection", "sql_schema_generalization_limit"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement

## 一句话总结

MACLA 固定 4-bit Llama-2-7B，将 trajectory 经 LLM 分段/抽象为带 goal、precondition、action schema、postcondition 的外部 procedure；再用 Beta posterior 的 expected utility 选择、success/failure contexts 的 LLM contrastive edit、以及可 continue/skip/repeat/abort 的 meta-procedure 组合。四个 agent benchmark 上表内平均 78.1，ALFWorld unseen 90.3；但这是有环境成功信号可验证的受控测试，在线记忆修改、语义合并和 fallback 的正确性未获安全证明，且“2,800×更快”仅是特定硬件和 training-cost 口径的对照。

## 方法与证据

- 每个 procedure 是 \(\langle G,\Psi,\pi,\Phi\rangle\)：LLM 从完整 \((o,a,r)\) trajectory 切出语义 segment，抽取 goal、preconditions、abstract action sequence、postconditions；embedding cosine similarity 超过 \(\theta_{dup}=0.85\) 即合并/扩展 condition sets（§3.1、§4）。错误 segmentation、自然语言 schema、embedding 相近不保证适用条件或动作语义等价。
- procedure success rate 用 Beta\((\alpha,\beta)\) 后验，EU 结合 contextual relevance、success、failure risk 和 information gain；若最大 EU 未过 \(\theta_{conf}\)，或 preconditions 不匹配，则回退 zero-shot LLM step（§3.2、§3.7）。后验只反映日志结果，不是环境安全概率、因果置信度或对 OOD 的校准证书。
- 若一个 procedure 同时积累至少 3 successes 与 3 failures，LLM 做 contrastive extraction，提出 tighter \(\Psi\)、repair \(\pi\)、refine \(\Phi\)，或拆分 modes；成功 trace 稳定包含 ≥3 procedures 时还生成 meta-procedure，其 controller 选 continue/skip/repeat/abort（§3.3--3.4、Alg. 1）。这是真正的 inference-time memory self-modification，不是仅检索静态知识库；没有独立 approval/rollback/sandbox 机制。
- 系统以 ANN \(O(\log N)\) 检索、buffer 1000 steps、每 procedure 至多 15 failure entries、reliability/frequency/recency pruning；LLM API calls/episode 有固定预算，声称 per-step retrieval/scoring/update 不随经验增长（§3.6）。LLM parsing/refinement 和 action formatter 仍是关键 failure/cost sources，fixed budget 也可能导致复杂任务降级。
- 所有实验为 frozen Llama-2-7B（Ollama、4-bit、temperature 0.7），memory capacities procedure 200/meta 50；权重 \((\lambda_r,\lambda_f,\lambda_t)=(0.5,0.3,0.2)\) 由 ALFWorld validation grid search 选出，contrastive threshold 为 3 successes+3 failures（§4）。因此“跨域无 task-specific tuning”不等于无 validation-driven design。
- 覆盖 ALFWorld（2,851 train/274 test，seen/unseen object-location split）、WebShop（1,624/200）、TravelPlanner（1,000/180/45）、InterCodeSQL；指标混合 task completion、quality、TravelPlanner CS/HC，Table 1 把它们按 0--100 scale 列出并报告 Avg 78.1，跨列平均不等于同一现实效用单位（§4、Table 1）。
- 表内 MACLA 在 ALFWorld seen/unseen 为 87.2/90.3，TravelPlanner CS 为 83.3。unseen 高于 seen 3.1 points 支持该 split 上的 compositional transfer，但不能单凭正 gap 排除数据/难度差异、prompt leakage或泛化到新 tools/domains（§4.1、Table 1）。
- ALFWorld ablation：移除 Bayesian selection 降 7.7 seen/9.1 unseen；移除 meta composition 的 unseen 降 11.9；去 contrastive/ontology 也有 3.5/4.6 与 4.3/6.2下降（§4.2、Table 2）。这些是同一数据与 implementation 的 component association，不分别验证 LLM-proposed edit 的有效性/安全性。
- 成本表的 2,800×来自 IPR 5.6 h×8 A100=44.8 GPU-hours 对 MACLA 1×RTX3090 56 s=0.016 GPU-hours 的 ALFWorld memory construction；两系统的硬件、post-training工作与在线 LLM/API cost 不同，不应转写为任何部署总成本/延迟比（§4.3、Table 3）。
- 容量在 100--200 procedures 提升，300 procedure unseen 反而 -0.2；ALFWorld 2,851 trajectories 提炼 187 procedures、约 15:1、3.6MB。SQL 分析显示 reuse 51%、reliability 64%、meta usage 18%，归因 schema-specific names/join complexity/短 query，明确限定其最适合可复用、层级、语义一致任务（§4.4--4.7、Fig. 2--5）。

## 适用边界与复现

- 适用于环境可给出可靠 step/postcondition feedback、任务有重复的可分解 workflow、动作可安全 sandbox 的 agent 任务。不可将 Beta reliability、procedure postcondition 或 memory compression 作为真实网页、数据库、旅行预订、机器人或安全关键工具执行的成功/合规证明。
- 在线 refinement 可能把偶然成功、错误 observation 或 poisoned feedback 写入共享 procedure，过度收紧/放宽条件或损坏 action schema。生产应用需 provenance、immutable raw logs、versioned memory、human/validator approval、canary evaluation、rollback、access control与 memory-poisoning/semantic-collision tests。
- “frozen LLM”只表示不更新权重；LLM 仍做 segmentation、abstraction、action formatting、contrastive edits和 fallback，输出质量/提示词/温度/API model drift 仍会支配行为。应报告 model/provider/version、prompt、token/API latency/cost、quota failures与 malformed action rate。
- 高风险 SQL/web action 必须 use schema/type/permission validator、read-only/transaction sandbox、query limits、tool allowlists和 user confirmation；TravelPlanner 需实时价格/availability/法规验证。不能根据 offline benchmark score直接执行有财务或隐私后果的动作。
- 复现应固定 benchmark revisions/splits、all trajectory sources、Llama/Ollama/quantization/prompt/temperature、embedding/ontology/\(\theta_{dup},\theta_{conf}\)、EU weights/failure cost/info gain、memory/meta/buffer/failure capacities、LLM-call budget、refinement/meta triggers、pruning/rollback policy、seeds与完整 per-benchmark metrics；成本须分别报 GPU、API、wall-clock和在线维护成本。

## 与 AAMAS 的关系与核验说明

这是 memory-augmented LLM agent 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FKYO8341.pdf) 核对 procedure/meta schema、Beta/EU/fallback、online contrastive edits、benchmark/table/ablation、capacity与SQL反例以及成本硬件口径；没有把外部记忆的 benchmark 结果、posterior 或训练计算差异误写为可信长期记忆、安全执行、无在线风险或普适成本优势。
