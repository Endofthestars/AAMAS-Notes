---
title: "PortfoliQA: An Agentic RAG Framework for Knowledge Graph Question Answering via Structured Evidence Portfolios"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: "10.65109/VPTX2262"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VPTX2262.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["subgraph_recall_dependency", "llm_semantic_parsing_error", "plausibility_not_formal_verification", "evidence_selection_bias", "unreported_end_to_end_cost", "benchmark_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# PortfoliQA: An Agentic RAG Framework for Knowledge Graph Question Answering via Structured Evidence Portfolios

## 一句话总结

PortfoliQA 是一个免微调的 KGQA agentic RAG：Planner 把问题拆为逻辑约束并构建 query plan，多个 Aligner 在预取子图中搜集每个候选答案的约束—证据路径，最终 LLM Reasoner 对结构化 Evidence Portfolio 排序。它在 Freebase/WebQSP/CWQ 上优于所列基线，但端到端正确性受 topic grounding、SubgraphRAG 召回、LLM 解析/排序和启发式路径搜索共同限制；“有证据组合”不等于事实已形式化验证。

## 方法与证据

- 初始化先以 semantic matching + LLM-assisted grounding 提取 topic entities，再调用 SubgraphRAG 从大 KG 取其周围的 \(N\) 个相关 triples 作为后续环境（§4.1）。未进入该子图的正确事实/实体无法被 Aligner 恢复；作者在 CWQ validation 中选择 500 triples，子图更小会漏证据、更大则引入干扰（§5.3）。
- Planner 的 semantic_parser 用 LLM 把问题拆为 atomic logical fragments、找 target variable，并用 validation tool 检查 CLQG connectivity；失败后重试，超过次数则 fallback 至至少一条从 topic entity 到 target 的 main chain（§4.2）。连接性检查不保证关系语义、量词、否定、时间限定或 entity linking 正确，fallback 也可能把复杂问题缩成不充分链。
- construction tool 用 abstract predicate 与实际 relation 的相似度加权 fan-out，选乘积 EFO 最小的 main chain，其余形成 side constraints（§4.2）。这是缩小搜索的启发式，不是可证明最优计划；relation embedding/候选 top-N/图的 fan-out 偏差会改变计划与候选集。
- Aligner 先为 main generative constraint 找 top-\(k\) paths，分别绑定候选答案，随后并行完成 side constraints。dual-pool 将达到预期逻辑长度的 path 放入 completed pool，继续探索直到 completed-pool top-k 稳定；每条 path 以 triple structural score 和对整条 constraint 的 embedding semantic score 的 log-rank 之和排序（§4.3）。它减少局部剪枝，却仍依赖长度、beam、score 与单条“best path”选择。
- Evidence Portfolio 为每个 candidate 将每个 constraint 映射为 evidence path 或 `NO_EVIDENCE_FOUND`，按路径分数汇总；最终 LLM Reasoner 按 evidence completeness、quality 和自身的 overall plausibility 给出排名（§4.3–4.4）。因此输出可追溯到已选 evidence，但“overall plausibility”仍可引入模型内部先验；路径存在也只证明 KG 内的断言，不能自动验证 KG 的时效、来源质量或现实真值。
- 评测在共用 Freebase 的 WebQSP 与 CWQ test sets，以 Hit@1 与 F1 比较；主模型为 Llama-3.1-8B 与 GPT-4o-mini，具体 setup/prompts 置于 Appendix C/E（§5.1）。范围是静态 KG 多跳问答，并未评估开放网页新鲜性、对抗性 KG、隐私数据、真实工具副作用或安全关键决策。
- Table 2：PortfoliQA(GPT-4o-mini) 在 WebQSP 为 Hit@1/F1 93.64/82.76，在 CWQ 为 75.29/68.34；Llama-3.1-8B 为 87.09/77.08 和 65.21/60.50。数值支持该 benchmark/配置下的准确率，不可跨模型、KG版本或检索预算直接外推。
- CWQ ablation 中 zero-shot Reasoner 41.18，score-only 54.27，candidate-only 65.55，full portfolio 75.29 Hit@1；将 portfolio 展平为 path list 或 triple bag 分别为 64.84/59.33（Tables 3–4）。dual scoring 去掉 semantic/structural signal 分别降至 66.56/63.34（Table 5）。这些是同一实验管线的组件对比，不能排除子图检索、prompt 或最终 LLM 贡献的耦合。
- 人为退化 CWQ multi-entity 子图（只保留一个 topic entity 与其 triples）后 overall Hit@1 从 87.39 降至 79.07；论文将其解释为 `NO_EVIDENCE_FOUND` 的 graceful degradation（§5.4）。这不等于缺失知识被恢复，仍有约 8.3 个点下降，且退化机制不同于现实 KG 的相关事实/关系错误。

## 适用边界与复现

- 适合作为有版本化、可审计 KG 的复杂问答与证据呈现基线。对法规、医疗、金融、身份或自动执行场景，最终答案应逐条绑定可访问 provenance/time/version，并经过 deterministic constraint checker 或人工复核；不得只凭 LLM 的 plausibility 排序行动。
- 部署时应将 entity/relation grounding、subgraph recall、每 constraint 的 evidence coverage、`NO_EVIDENCE_FOUND`、候选间 score margin、LLM refusal/hallucination 和 KG freshness 暴露给用户。缺证据应返回“不足以断言”，不是把部分 portfolio 伪装为已验证结论。
- 论文没有在正文报告完整的 LLM token、API cost、P95 latency、并发 swarm 资源、重试次数或失败率；生产前应按问题长度、子图大小、beam/\(k\)、模型和缓存测量，并对工具输入做限制，以避免预算失控或恶意图文本/提示影响规划与排序。
- 复现需取得 Appendix C/E 中的 KG snapshot/预处理、topic grounding、SubgraphRAG配置、prompts、retry/fallback上限、relation embeddings/top-N、EFO/beam/dual-pool稳定准则、\(k=50\)、500-triple context、LLM version/temperature/seeds、baseline引用版本和 WebQSP/CWQ 评测脚本；还应在 temporal/poisoned/incomplete KG 与未知关系上报告引用正确率而不只答案分数。

## 与 AAMAS 的关系与核验说明

这是 agentic KG reasoning 与 evidence-aware QA 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VPTX2262.pdf) 核对子图初始化、Planner CLQG/plan、dual-pool Aligner、portfolio/LLM ranking、WebQSP/CWQ 模型与指标、main/ablation/退化结果和 appendix 依赖；没有把结构化证据展示误写为自动事实认证、完全可解释性或开放域可靠性保证。
