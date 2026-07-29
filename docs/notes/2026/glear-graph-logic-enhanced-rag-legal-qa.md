---
title: "GLEAR: A Graph Logic-Enhanced RAG Framework for Legal QA"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/ZNVM5881"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZNVM5881.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["chinese_legal_data_scope", "synthetic_historical_queries", "self_created_freeform_questions", "subjective_evaluation", "graph_construction_quality", "hallucination_remaining", "not_legal_advice"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# GLEAR: A Graph Logic-Enhanced RAG Framework for Legal QA

## 一句话总结

GLEAR 将中国法律案例、法条和历史查询组成异构图，以语义+BM25 双驱检索、贪心关键路径挖掘和上下文注入增强法律 LLM；在五项既有中文法律 NLP 任务和 300 个自建自由问答上优于所比较的 base/RAG，但其路径只是图连接的检索证据而非经过法律有效性验证的推理证明，且作者明确产出仍会 hallucinate、仅供研究、不能替代律师。

## 方法与证据

- 图包含案例、法条、历史 query 三类节点与五类关联（case--case、article--article、case--article、query--case、query--article，§3.1）。case 相似边由术语/语义相似度超过 \(\theta=0.85\) 建立；query--article 部分从 Hualv.com 法条及其对应关系出发，并使用 DeepSeek-V3 生成 virtual historical queries。知识图的质量、时效性和生成 query 的偏差会直接影响后续检索。
- 对输入 query，dual-driven retrieval 将 Sentence-BERT 语义分数与 BM25 相加，先取类似历史 query，再从图中找关联节点（§3.2.1）。key logical path mining 以 greedy 方式反复选择最高权可达边，未定义权重的边赋 1.0，取 \(M\) 条路径（§3.2.2）。这提供可展示的关联链，但并不执行成文法的形式规则推导，也不保证路径是唯一、完整、因果相关或法律上可采。
- 实验覆盖 CAIL2018 的 charge/article prediction 与 prison-term prediction、LAIC2021 的 dispute focus、LEVEN 的 element detection；分别用 F1 或 nLog distance（§4.1）。通用中文模型与多种中文 legal LLM 都接入 GLEAR；standard RAG baseline 将历史案例/法条切块、FAISS 检索，最多取 5 块（§4.2）。传统任务每个数据集独立运行 20 次并报告均值。
- 作者报告相对未增强基座模型，五项任务平均改善分别为 0.13、0.24、0.14、0.19、0.04（F1 或 nLog distance）；相对其 standard RAG 的改善为 0.06、0.11、0.04、0.07、0.03（§5.1）。数值混合了不同模型、不同任务和不同量纲，不能简化为一个可直接比较的“14 个百分点普适增益”。
- 消融以 ChatGLM3-6B 为 base：移除 graph、dual-driven retrieval 或 path mining 均降低五项任务结果；full GLEAR 在该表的 charge/article F1 是 0.42/0.62（Table 2，§5.3）。这支持这套特定图构造与检索流水线内的组件贡献，但不隔离 DeepSeek 生成 query、数据覆盖或模型提示的影响。
- 自由问答由 300 个创建的问题评测，专家与 DeepSeek-R1 按 accuracy/professionalism/comprehensiveness 的 1--10 分评分；论文报告平均分别提高 1.7、1.9、2.1 分（§4.1、§5.2）。这属于有限、主观且未见法律后果/引用正确性/用户结果的评测，不是临床式或司法级准确率认证。
- 作者的限制包括图只到案例/法条等 macro entities，未显式表示犯罪构成要件/量刑因素，可能造成 semantic drift；面对模糊或措辞不准确 query，检索 recall 可明显下降（Limitations）。伦理声明也明示 hallucination 仍显著，严重纠纷应优先咨询真实律师。

## 适用边界与复现

- 适合研究中文法律文本中的 provenance-aware retrieval、关联路径呈现和 RAG 组件比较；不得作为跨法域法律意见、裁判预测依据、自动收费建议、定罪/量刑决定或对用户权利义务的最终判断。
- 上线前应对每项图边保留原始来源、版本/生效日期和构边依据；独立核验检索到的法条是否有效、适用地域/时间是否匹配，且要求模型逐项区分事实、引用和不确定性。生成的 historical queries 不能被误当真实先例或当事人陈述。
- 复现需发布可合法再分发的案例/法条/历史查询、DeepSeek-V3 augmentation prompts与版本、graph schema/edge weights/\(\theta\)、Sentence-BERT/BM25/FAISS 设置、\(K=12,N=5,M=3\)、模型 prompts、20-trial seeds、300 个问答及评分者协议/一致性。还需比较强 retrieval baselines、做时间切分与跨法域/OOD、citation correctness、对抗模糊 query、隐私泄漏及实际律师复核。
- 用于高影响法律服务时，应设置明确“非法律意见”告知、律师审阅与升级、可追溯引用、冲突/过期法条检查、数据最小化和申诉/纠错机制；一个连通图路径或较高 F1 不能单独证明答案合法、完整或无幻觉。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的知识图谱增强 RAG、论证式法律信息检索和可靠 agent engineering 论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZNVM5881.pdf) 核验图源与 DeepSeek-V3 augmentation、双驱检索/贪心路径、五项中文数据集、20-trial 设置、300-question 主观评测、消融、作者列出的粒度/模糊 query 限制及“非 100% 准确”的伦理声明；没有把研究性基准收益写成可直接提供法律意见的能力。
