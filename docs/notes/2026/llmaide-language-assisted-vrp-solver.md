---
title: "LLMAide: Language-Assisted Neural Solver for Vehicle Routing Problems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "resource_allocation", "agent_engineering"]
dblp_key: ""
doi: "10.65109/ISOA2063"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ISOA2063.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03u"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "synthetic-vrp", "llm-embedding-ablation", "feasibility-mask", "scaling-unverified"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# LLMAide: Language-Assisted Neural Solver for Vehicle Routing Problems

## 一句话总结

LLMAide 在 RouteFinder 式 neural VRP solver 中，把约束的自然语言描述经 Qwen2-0.5B 编码，与空间 route embedding 进行多尺度、双向 cross-modal attention 和残差融合。作者在 16 个合成 VRP variants 上称其常优于相应 RouteFinder 配置，但仍用 feasibility mask 保证解有效。

## 方法与证据

- 将 capacity 基础问题与 open routes、backhauls、duration limits、time windows 的组合写成 16 variants；任务模板把约束转成语言并得 LLM embeddings（§2）。
- route/language modality 各做 $S$ 级分解，每尺度双向 multi-head attention，动态尺度权重，然后以有残差的 progressive fusion 维护语义和空间信息；decoder 自回归选点、受动态 feasibility masks 约束（§3）。
- 合成 $n=50/100$，与 HGS-PyVRP、OR-Tools、RouteFinder baselines 比；LA-TE 在 $n=50$ 的 13/16、$n=100$ 的 11/16 variants 优于 RF-TE。Table 1 的 CVRP $n=50/100$ gap 为 1.176%/1.423%，VRPTW 为 1.897%/3.431%（相对 HGS best-known）。随机向量替代 LLM embeddings 会下降（§4）。

## 适用边界与复现

- 语言模板编码的是已知结构化约束，提升不表示模型能可靠理解任意自然语言运营规则；实验为合成 50/100 node，未建立真实大规模、延迟和鲁棒性保证。
- 复现需发布实例生成、16 variant 定义、templates、Qwen checkpoint/embedding cache、fusion/decoder 参数、mask、RouteFinder训练、baseline budgets和完整结果。部署时还须独立验证 feasibility、时间窗、驾驶/容量和成本模型。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ISOA2063.pdf) 人工核对架构与 Table 1；未将合成 benchmark 的竞争性能解释为生产调度保证。
