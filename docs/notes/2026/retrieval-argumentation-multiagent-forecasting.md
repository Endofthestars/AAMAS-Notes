---
title: "Retrieval- and Argumentation-Enhanced Multi-Agent LLMs for Judgmental Forecasting"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/SNBR1486"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SNBR1486.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["historical_news_source_scope", "retrieval_quality_dependency", "forecast_dataset_scope", "similarity_threshold_tuning", "model_prompt_sensitivity", "complementarity_not_guaranteed", "no_calibration_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Retrieval- and Argumentation-Enhanced Multi-Agent LLMs for Judgmental Forecasting

## 一句话总结

论文将多个 LLM agent 对未来事件提出的支持/反对证据表示成 quantitative bipolar argumentation frameworks（QBAFs），按语义相似度合并并聚合强度；再比较纯 ArgLLM、检索增强的 RAG-ArgLLM 与 relation-based argument mining（RbAM）。在 GJOpen 与 Metaculus 上，检索和多 agent 融合常能提高准确率，三 agent 的互补来源尤其有帮助，但收益取决于模型、来源、深度与互补性，不能把“多 agent”当成普适的 forecasting 改进。

## 方法与证据

- 每个 agent 为预测 claim 生成一棵 QBAF：节点是 argument，边为 support/attack，base score 在 [0,1]；组合器用 Jina-V3 embedding 的 cosine similarity（阈值 \(\delta=0.5\)）聚类相似 arguments，合并边并以 average 或 maximum 聚合 cluster 的 base score（§3--§4、§6）。因此解释产物是合并后的论证图，而非单一投票分数。
- ArgLLM 是不检索的基线；RAG-ArgLLM 将检索的摘要放入 argument-generation prompt；RbAM 则把检索文本直接作为 argument，并分类它对 claim 的 support/attack/无关关系（§5）。三种 agent 的信息来源和错误模式不同，不能只按模型名称比较。
- RAG 使用 2023--2024 NYTimes abstracts 或由 GPT-4o-mini 产生五个 query 后从 Guardian API 得到的摘要；每 claim 取关闭日前的 top-5 相似摘要，存于 ChromaDB。作者选择 cutoff 早于预测事件的 base LLM，以减少训练数据泄漏（§6.1--§6.2），但这不等于检索材料本身无来源偏差或时间遗漏。
- 数据为 GJOpen 的 2,923 个改写问答预测对，以及从 Metaculus resolved questions 选出的 388 个 binary 问题（2023-09 至 2024-09 曾开放）；题目/答案经 Mistral-7B 转为自然语言 claim 后人工审阅（§6.3）。评估是 accuracy，未报告概率校准、Brier/log loss 或真实未来部署的前瞻实验。
- 个体 agent 中，检索在 Metaculus 的几乎所有变体提升 accuracy；Gemma-2、depth-1、estimated score 的例子从 68% 到 81%。GJOpen 更不稳定，最大示例是 Llama-3、depth-2、0.5 score 由 63% 到 75%；Guardian 总体较 NYTimes 更常有帮助（§7.1）。这说明 retrieval 的效应是条件性的。
- RbAM 在 GJOpen 表现不佳，作者检查认为摘要本身缺少充分的论证结构而导致低 base scores；在 Metaculus 有一定前景。它是“直接拿摘要当 argument”并不自动可靠的反例（§7.1）。
- 两 agent（同类、混合 ArgLLM/RAG-ArgLLM、或两种来源）融合经常超过至少一个个体，偶尔超过两个；average 聚合通常优于 max。对性能已很强或产生冗余论证的 agent，第二个 agent 可能无益；depth-2 在部分配置反而因无关第二层 arguments 降分（§7.2）。
- 三 agent（一个 ArgLLM + NYTimes/Guardian 两个 RAG-ArgLLM）通过增加互补观点，通常清楚优于其中两个较弱成员，却并非总超过 trio 中最佳单 agent；作者把 source bias/noise、问题类型、interactive debate、部署成本留作未来工作（§7.2--§8）。

## 适用边界与复现

- 适用于需要可追溯地汇集相互冲突证据的低风险预测或辅助研判；每个结论应保留 claim、来源摘要、检索时间、argument relation、合并簇和最终分数，供人审阅与反驳。
- 不适用于把新闻检索+LLM 输出直接当作金融、医疗、政策或安全关键决策。该研究没有证明消息源的真实性、覆盖公平性、概率校准或对 adversarial/过期检索的稳健性。
- 复现应冻结 GJOpen/Metaculus split、claim rewrite、各模型/提示词、cutoff、NYTimes/Guardian corpus、top-5 检索和 \(\delta=0.5\)；分别报告 single/pair/trio、depth、source、average/max 的 accuracy，并增加 Brier score、校准曲线、置信区间及按题类/时间的分层结果。
- 部署前应做来源多样性与冲突审计、时间泄漏检查、prompt/model 版本固定、ablation（禁检索/单来源/随机证据）和人工升级通道；当 agent 不互补或证据薄弱时应拒答或标注不确定，而非强制融合。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 中 argumentation、RAG 与多 agent LLM 用于 judgmental forecasting 的工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SNBR1486.pdf) 核验摘要、§4--§7 的 QBAF 合并、检索与数据设置、个体/pair/trio 结果及 §8 的局限；没有将选择性的 accuracy 改善表述为可靠的实时预测或因果证据验证能力。
