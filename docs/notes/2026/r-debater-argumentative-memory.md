---
title: "R-Debater: Retrieval-Augmented Debate Generation through Argumentative Memory"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "agent_engineering", "human_agent_interaction"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XWXH6253.pdf"
preprint_url: "https://arxiv.org/abs/2512.24684"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["retrieval_evidence_freshness", "llm_hallucination", "judge_metric_subjectivity", "chinese_debate_dataset_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# R-Debater: Retrieval-Augmented Debate Generation through Argumentative Memory

## 一句话总结

R-Debater 将辩论记忆构造成带论证 scheme/质量标签的检索库：并行分析对手历史中的逻辑漏洞、检索同类论据，再由生成、总结、判断和修改角色迭代生成下一轮辩论发言。

## 方法与证据

- 数据库记录为 utterance、证据、argumentation schemes 与 scheme quality 的组合。检索先由关键词规则粗筛，再以 debate-history embedding 相似度取 top-$k$；对手历史则经 pseudo–first-order predicate、自然语言 reasoning chain 和 logic critic 生成控制信号。这里的“符号”是 prompt 驱动的解释层，论文没有提供形式定理证明或外部事实验证器（§4.1–4.2）。
- 生成阶段以 history、stance、逻辑信号、检索证据/argument schemes 产生候选 utterance；summary agent 汇总争点，judgement agent 从 stance faithfulness、relevance、scheme compliance 给二元反馈，text-modification agent 反复修订直至通过（§4.3）。这将模型自己的 judge 放在生成环中，不能独立保证事实为真。
- ORCHID 是正式中文辩论 transcript。作者从近五年 1,134 场中用 1,000 场建 retrieval corpus，另取无重叠的 32 场、7 个域评测；每场平均约 10 轮，每个 utterance 约 1,000–1,500 汉字（§5.1）。因此结果主要覆盖其 curated、中文、正式赛制数据，而非开放网络辩论。
- 对 GPT-4o、DeepSeek-V3、Claude-3.7-Sonnet 的 zero-shot、temperature 0.2 比较包含 direct LLM、Naive RAG、Agent4Debate。单轮 InspireScore 中，R-Debater 的 overall 分别为 0.822、0.819、0.830；例如 GPT-4o 下 Naive RAG/Agent4Debate 为 0.770/0.783（§5–6.1、Table 1）。Fact 值并非每一基座最高：GPT-4o 下 Agent4Debate 0.631 高于 R-Debater 0.627。
- 多轮对抗模拟只将 R-Debater 与 Agent4Debate 对打，并由 Debatrix 的 Source/Language/Argument/Overall 评分；表中 GPT-4o overall 为 1.23 vs 0.77，DeepSeek-V3 为 1.25 vs 0.75（§5–6.2、Table 2）。这属于自动 judge 的受控模拟，而不是对人类对手、真实胜率或安全性的测量。
- 内部 scheme annotation 相对专家的 Jaccard 为 0.7366、precision 0.8225，scoring agent 与专家的 Pearson/Spearman/Kendall 为 0.6356/0.6533/0.5880（Table 3）。gpt-4o-mini 消融中完整系统 InspireScore 0.831，去 optimization、logic/summarization、argumentation scheme 后为 0.776、0.761、0.528（§6.3、§6.5、Table 5）。
- 20 名大学辩论社成员进行匿名随机化人工评价，R-Debater 的总体偏好率 76.32%，Agent4Debate/LLM/NaiveRAG 为 15.79%/7.89%/0%（§6.6、Table 6）。这是小规模、有经验评审的主观偏好，不能证明所有受众或所有议题更可信。

## 局限与复现

- retrieval 只会提供库中已有的材料；库更新慢、领域覆盖窄、关键词漏检、相似文本但不适用，都会使输出陈旧或错配。检索 grounding 不是 citation verification，LLM priors 与 retrieved evidence 冲突时仍可能 hallucinate。
- 多角色 pipeline 增加延迟、token 与调用复杂度；binary judge 的通过不代表论证正确、平衡或无操纵。部署到教育、公共讨论或政策场景需加入来源追溯、时效校验、人工复核和拒答/不确定性机制。
- InspireScore 与 Debatrix 有主观组成；人工评价仅 20 人，且数据、任务、提示和模型版本均会影响结果。单轮分数、自动多轮 judge 与人类偏好是不同证据，不能合并为真实“辩论胜率”。
- 复现应保存 ORCHID split 与 1,000-item corpus、去重规则、每条 scheme/quality 标注、embedding/retrieval $k$、所有 agent prompts、base-model 版本和调用预算；分别报告 fact-source 可核验率、judge–human 差异、latency/cost、跨语言与跨域表现。

## 与 AAMAS 的关系与核验说明

该文将检索增强、角色化 agent 和计算论证结合，用于多轮辩论生成。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2512.24684) 核对 pipeline、ORCHID split、表格、消融和人评；性能结论严格限定在所列自动指标与小规模中文辩论评测内。
