---
title: "EG-RAG: Retrieval-Augmented Generation with Evidence Graph for Reliable Multi-Document Reasoning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/NJIG6104"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NJIG6104.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["nli_relation_error", "retrieval_truth_assumption", "relative_improvement_metric", "key_sentence_truncation", "benchmark_scope", "no_fact_verification_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# EG-RAG: Retrieval-Augmented Generation with Evidence Graph for Reliable Multi-Document Reasoning

## 一句话总结

EG-RAG 先按 query relevance 每文档选 1--3 个代表句，再以 NLI classifier 的 support/contradiction/neutral 概率建立 sentence graph，按关系子图的 connected components 和内部权重形成 evidence clusters，并把正/负/中性结构序列化进生成 prompt。它在 FaithEval-Inconsistent、HotpotQA、RAMDocs 的 EM 上通常优于 standard RAG；但图表示的是**模型判定的句间蕴含/矛盾**，不是证据来源真伪、时效、因果性或法律/医学事实验证，最终答案仍由 LLM 生成。

## 方法与证据

- pipeline 为 retrieval → 每 document key-sentence selection → pairwise NLI → signed/weighted edges → relation-specific connected components → structured prompt generation（§3、Alg. 1）。句子被排除或压缩后，其中的限定条件/来源上下文不会自动保留。
- 对 selected sentence pair，NLI 输出三类概率，取预测 relation，edge weight 为其置信度乘两句 query relevance；support/contradiction/neutral 分别构图，cluster 内部权重和 \(\Phi_\ell(C)\) 表示强度。cluster 至少保留 2 nodes（§3.3--3.4）。这是一种启发式 aggregation，不是概率独立性、逻辑证明或真实可靠性估计。
- NLI modules 是 RoBERTa-large-MNLI（NLI1）及在 MNLI/FEVER/ANLI 上进一步训练的 DeBERTa-v3-large（NLI2）；NLI Agent 对照用 GPT-4o-mini 做 relation classification（§4.1、§4.4）。NLI 的关系误判、否定/时间/指代/多跳语义错误会直接改变图边与 prompt。
- final prompt 接收 query、selected sentences及 support/contradiction/neutral clusters，旨在压制矛盾并强化支持；LLM 没有被形式约束为只输出 graph 支持内容，引用出处也不等于事实审核（§3.5）。
- benchmark 为 FaithEval-Inconsistent（冲突/操纵 contexts 的 faithfulness）、HotpotQA（multi-document/multi-hop）与 RAMDocs（ambiguous query、false/misleading/noise、support imbalance），主指标为 EM（§2.3、§4.1）。这些是合成/公开评测设置，不覆盖实时网页变动、source provenance、专业知识核验或用户伤害。
- 三种 backbone 为 GPT-4o-mini、Anthropic Sonnet-4、Ministral-8B-Instruct；同一管线也比较 standard RAG、Astute-RAG、Faithful-RAG、MADAM-RAG 等（§4.1、Table 1）。因此“model-invariant”是这三模型上的经验趋势，不是所有 LLM、retriever、语言/领域的保证。
- Table 1：FaithEval 对 standard RAG 的平均相对增幅为 115.63%，HotpotQA 为 26.17%，RAMDocs 为 95.47%；abstract 报跨类平均 79.09%。这些是以 baseline score 为分母的**相对**改变量，低 baseline 会放大百分比，不能读成绝对 accuracy、hallucination reduction比例或真实事实可靠率（§4.2、Table 1）。
- RAMDocs 上 MADAM-RAG 仍优于 EG-RAG；EG-RAG 虽持续超过 Astute/Faithful 类基线，但论文不宣称所有噪声/misinformation condition 最好（§4.2）。
- key-sentence ablation 显示 \(K=1\sim3\) 已可维持主体增益，\(K=3\) 相对 \(K=1\) 仍增加 FaithEval/Hotpot/RAMDocs 2.85%/1.03%/14.11%（§4.3、Fig. 2）。小 \(K\) 更高效但也会漏掉跨句证据，尤其 RAMDocs 对更多句较敏感。
- NLI2 在 FaithEval 通常优于 NLI1，但 HotpotQA/RAMDocs 略弱；GPT-4o-mini NLI Agent 低于两种 classifier。作者将其归为专用/保守 classifier 的任务 trade-off，而不是统一的 best NLI choice（§4.4、Table 2）。

## 适用边界与复现

- 适用于已有合理 retrieval corpus、要在有限多文档中显式呈现同意/冲突语句的 QA/analysis 辅助。部署前仍必须评价 retriever recall、source authority/time/version、sentence extraction、NLI calibration、prompt injection与最终 answer faithfulness。
- “contradiction cluster”只表示 classifier 认为两文本不一致；它不确定哪一方为真，也不会检测两个相互支持的虚假来源、过期信息、复制谣言、遗漏的关键证据、统计/因果误用。高风险输出要回链原始权威来源，并由 domain-specific verification/人类审核决定。
- 只选择 \(K=1\)--3 句适合成本限制，却可能在法律、医学、金融、科学和多条件问题中截断限定语、证据链或反例。应提供可展开的 document context、abstain/ask-clarification路径与“不足以判定”输出，而不是只依 cluster score。
- 结构化 prompt 仍可被 retrieved text 的 injection 或 generator positional bias 影响。生产环境需 content isolation、tool/schema validation、citation-to-claim matching、source trust policies、red-team conflict/noise tests及 monitoring，而非把 NLI confidence 视作安全门。
- 复现应固定 corpus/retriever/document split、sentence selector/relevance scorer、\(K\)、NLI checkpoints/calibration、edge/cluster thresholds/serialization prompt、backbone exact version/API sampling、baseline prompts、EM normalization、seeds/CI以及相对提升的分母；另报告 absolute scores、retrieval recall、NLI confusion和 unsupported-claim rate。

## 与 AAMAS 的关系与核验说明

这是 evidence-structured retrieval-augmented generation 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NJIG6104.pdf) 核对 key-sentence/NLI graph/cluster/prompt流程、NLI models、三 benchmarks/三 backbones、Table 1--2、\(K\) ablation和各任务 trade-off；没有把 NLI 关系图或相对 EM 增益误写为来源真实性、绝对事实可靠率、无 hallucination或高风险决策保证。
