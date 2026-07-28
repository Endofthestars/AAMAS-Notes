---
title: "LLMEvalRec: An Agentic Framework for Simulating Users to Evaluate News Recommendation Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EFZY6916.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_recheck"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "revised_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["internal_data", "short_evaluation_window"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark revision and recheck)"
reviewed_at: "2026-07-29"
---

# LLMEvalRec: An Agentic Framework for Simulating Users to Evaluate News Recommendation Systems

## 一句话总结

LLMEvalRec 以 LLM 用户代理模拟新闻点击，并用 GUES 优化提示词，目标是在冷启动数据稀缺时比较推荐模型的相对表现。

## 方法与证据

- §2 构成“数据—用户画像—对齐—模拟—指标”的闭环：memory、actor、observer 和 prompt optimizer 共同维护用户画像并产生 click/no-click 行为（Figure 1）。
- §3 的 GUES 以并行 episode 搜索优化指令；论文配置为每轮 2 iterations、每轮 2 episodes、每 episode 5 steps。
- §4 在 MIND、真实业务数据和线上对照中报告 AUC、MRR、NDCG 与 CTR。Tables 1–2 用模型排序比较模拟与真实评测；Table 3 中 Sonnet 3 无 GUES 的 F1 为 0.220、同模型 GUES 为 0.242，Sonnet 3 + Sonnet 3.5 为 0.221。
- Table 4 报告 Rule/Bandit 的线上 CTR（2.92%/3.84%）及与模拟指标的对应关系；该证据支持论文实验范围内的趋势比较，而非绝对效果保证。

## 局限与复现

- 真实业务实验依赖内部新闻日志和候选流，外部复现需有相容的日志 schema；业务窗口约一周，难以推断长期漂移下的表现。
- 结果依赖所用 LLM、指令模板和 GUES 配置，迁移到其他模型族或提示策略需要重新校准。
- 复现至少需用户画像字段、代理组件、GUES 搜索参数和 Tables 1–4 的离线/线上指标；不能将模型排序证据外推成普适生产性能。

## 与 AAMAS 的关系与核验说明

工作把多代理生成、观察和优化用于推荐系统评估。初次 QA 校正了 Table 3 的数值归属；修订稿经 Spark S4 复核后，方法、数据范围和结论均与来源一致。
