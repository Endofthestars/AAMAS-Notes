---
title: "Learning Semantic and Structure Aware Representation with Large Language Models for Concept Recommendation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/CKWM7360"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CKWM7360.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03t"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "education-recommendation", "llm-generated-definitions", "concept-graph-quality", "offline-metric-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Learning Semantic and Structure Aware Representation with Large Language Models for Concept Recommendation

## 一句话总结

SSRec 为下一知识点推荐补入两类信息：让 LLM 参考 prerequisite/successor 解释含义歧义的概念，再用 GCN + graph contrastive learning 将文本 embedding 适配到知识图结构，和 DKT learner state 一起送入 Transformer。作者称在 Junyi、ASSIST12、ASSIST09 的 HR@1/NDCG@5/MRR 优于基线。

## 方法与证据

- LLM prompt 输入 concept name 及其 predecessors/successors，生成 context-aware definition；预训练语言模型（例 BART）编码为初始 semantic vector，试图消除如 “Table” 的教学语义歧义（§2）。
- 直接文本 embedding 被视为 anisotropic：以 concept graph 的 GCN 作 adapter，并对 edge-dropout 得到的两张图用 InfoNCE 训练，使相同 node 的双视图相近、无关 node 分离（Eqs. 1--2）。
- DKT 追踪 learner knowledge state；concept ID、答题正确性、graph-adapted embedding 与 state 拼接后经 Transformer 预测 next concept。先以 graph contrastive/knowledge tracing/sequence self-supervision 预训练，再端到端微调（Eq. 3）。
- 三真实数据集上比较 SASRec、UniSRec、GCARec 等；作者称所有主指标显著领先，去除 LLM explanation 或 graph contrastive module 都下降；ASSIST09 DBI 从大于 2.0 降至小于 0.7，并用 GPT-4 与 Matching Ratio 评估语义/结构一致性（§3）。摘要未列主指标的具体数表。

## 适用边界与复现

- 教育价值取决于 concept graph 正确性、LLM 定义是否稳定/准确及 learner trace 的代表性；推荐准确率与 GPT-4 打分不证明学习收益、教师可解释性或公平性。LLM 生成内容还需版本与提示审计。
- 复现应固定 datasets/splits、concept graph、LLM/model/prompt/temperature、文本 encoder、GCN/edge-dropout/InfoNCE 参数、DKT/Transformer、baseline tuning、matching-ratio/GPT-4 prompt 与人工教育评估。部署应允许教师审查和对错误先修关系回滚。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CKWM7360.pdf) 人工核对 SSRec 组件、训练阶段与报告的范围；未将离线推荐指标外推为真实教学效果保证。
