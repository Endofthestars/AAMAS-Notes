---
title: "AutoMETA: A Multi-Agent LLM System for Autonomous Meta-Analysis"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "applications"]
dblp_key: ""
doi: "10.65109/HXKA2256"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HXKA2256.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["medical_evidence_scope", "human_reference_circularity", "eight_cardiology_meta_analyses", "accuracy_coverage_tradeoff", "heterogeneity_instability", "protocol_validity_dependence", "extraction_error_residual"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# AutoMETA: A Multi-Agent LLM System for Autonomous Meta-Analysis

## 一句话总结

AutoMETA 让每篇 primary study 由一个 LLM agent 作页码锚定提取、互评和修订，再由非 agent 统计模块做 DerSimonian–Laird random-effects pooling。它在 8 篇 2004 年心脏科 meta-analysis 上对人工参考的 median relative effect-size error 为 6.4%，优于 single-agent 的 34.0%；但严格筛选会减少纳入研究并使异质性不稳，人工参考也并非真值，因此不能将其输出直接作为医学/政策结论。

## 方法与证据

- 每个 study-centered agent 按人写 protocol 提取带 page/table/figure anchor 的结构化数值；互评处理阈值、单位、分母与 zero-cell，protocol engine 再做规则守卫，最终由集中式统计模块算 DL random-effects、\(Q,\tau^2,I^2\)（§1、§3）。多 agent 协作并不消除 LLM 的解析、换算和 protocol interpretation 错误。
- 语料来自 Scopus 中 2004 年 cardiology meta-analysis：15 篇候选中 8 篇可用，合计 114 个 primary studies，每个实验重复 10 次；诊断结果用 2×2 表，连续结果用 Hedges \(g\)，zero cell 加 0.5 correction（§3.1--3.2）。这不是系统性检索端到端评估，且领域、年份、报告习惯和可访问性均高度局限。
- Full AutoMETA 的 median relative effect-size error 为 6.4%，NoCritique 12.4%、NoProtocol 25.1%、两者去除 28.1%，single LLM 34.0%（§4--5）。相邻配置区间有重叠，证据支持在该语料/流程上有方向性改进，不支持“human-level reliable”在任意综述任务的概括。
- critique 主要发现 threshold inconsistency 24%、inclusion/label ambiguity 22%、denominator mismatch 19% 和 zero-cell omission 12%；复杂论文的 validation pass rate 增加 8--15 points，但总 pass rate 仅 88% vs. 无 critique 87%（Table 2、§4.3）。页码引用和单位问题仍会因 PDF 解析歧义残留。
- 严格 enforcement 提升 effect-size fidelity，却可能保守排除研究：一例 Full 只纳入 \(k=2\)，得到 \(I^2=86\%\) 而人工参考为 0%。Full 的 heterogeneity deviation 甚至高于部分 ablation（§5.1--5.2），故 effect-size 对齐不能代替异质性、偏倚和证据完整性评估。
- §5.4 列出限制：仅 8 篇单年心脏科综述、Full 的 \(\Delta_{rel}\) IQR 很宽且 mean 40.0% 对 median 6.4%、human reference 本身可能有误、以及默认 human protocol 有效完整。任何真实使用都需要人工双抽取、统计/临床审查和可复现审计。

## 适用边界与复现

- 适用于已有明确 protocol、可获取全文、且目标是辅助提取/可追溯对账的研究工作流；不应自动决定纳入排除、医学推荐、临床诊断或监管结论。
- 协作质量取决于 protocol 的完备性、来源可读性、LLM/提示/上下文、peer topology、规则实现和统计模型。DerSimonian–Laird、固定 zero correction、单元定义和阈值选择均是可争议方法决定，不能由 agent 共识自动验证。
- 复现需保存 corpus/许可、Scopus query、人工 reference 与 protocol、全文版本/页码、模型与 prompts、agent 轮次、JSON schema/guards、审计 trace、所有 excluded study 的原因、DL/HSROC 实现和 10 次随机运行；分别报告 per-study extraction correctness、纳入数、effect size、\(Q,\tau^2,I^2\)、失败/拒绝及人工裁决。
- 在医学或高风险决策中，输出只能是待审工作底稿：由独立领域专家复核 PICO、risk of bias、重复研究、异质性、敏感性/发表偏倚和统计模型，并保留人类最终责任。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多代理协作、可审计推理与科学证据综合论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HXKA2256.pdf) 核验 agent/protocol/pooling 流程、8 篇/114 studies/10 runs、6.4% 对比、Table 2、accuracy--coverage trade-off 与 §5.4 限制；没有把对人工参考的有限数值对齐误写为自动医学 meta-analysis 的有效性或临床可用性证明。
