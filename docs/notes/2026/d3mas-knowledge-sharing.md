---
title: "D³MAS: Decompose, Deduce, and Distribute for Enhanced Knowledge Sharing in Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/WQMU8577"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WQMU8577.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["embedding_routing_dependency", "retrieval_threshold_sensitivity", "commercial_api_dependency", "benchmark_protocol_ambiguity", "prompt_token_only_cost", "no_openworld_evaluation", "no_prompt_injection_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# D³MAS: Decompose, Deduce, and Distribute for Enhanced Knowledge Sharing in Multi-Agent Systems

## 一句话总结

D³MAS 以异构图统一任务分解（Decompose）、跨 agent 推理依赖（Deduce）和分布式记忆检索（Distribute），试图让团队只共享“最小充分”信息；在 MMLU、HumanEval、SRDD、CommonGen 上报告高于所比基线的准确率、并按自定义重叠度将冗余降约 46%，但结论依赖 GPT‑4、BGE‑M3、阈值检索和任务/agent embedding 路由，且正文的模型与评测协议描述存在不一致，不能把它当作已验证的通用、低成本或安全知识共享方案。

## 方法与证据

- 框架把 task、reasoning、memory 节点及 `decompose/trigger/depend/retrieve/ground/relate` 边放入三层 heterogeneous graph（§4.1）。task layer 将 query 递归拆至单 agent 可处理的子问题并按 agent profile--task embedding capability 匹配；reasoning layer 显式记录 premise/conclusion 重叠以复用他人结论；memory layer 为每 agent 维护 local subgraph，跨 agent 聚合 top-\(k\) 相关节点（§4.2--4.4）。这些是文本/embedding/规则化依赖关系，不是对推理正确性或知识真实性的形式证明。
- “冗余”被操作化为：多个 agents 检索同一 knowledge item 的 memory redundancy、cosine similarity 超过 0.85 的 reasoning redundancy、以及重叠 sub-task assignment 的 task redundancy（Figure 1，§1）。报告的 47.3% 既有 duplication rate 与平均 46% reduction 仅对这套阈值/表示/HotpotQA+MMLU 的 4--8 agent 分析成立；不同 embedding、同义改写、互补证据或成本函数会给出不同数值。
- 实施使用 GPT-4 作 language generator、BGE-M3 retrieval embeddings；memory retrieval threshold 0.65、top-5，message passing 最多 10 iterations 或收敛，agent 数按任务复杂度为 4--8，embedding dim 512、层数 3（§5.4）。任务分配依赖 cosine similarity，错误 profile/embedding 或跨域 query 会令 subtask/知识路由偏差；系统没有提出未知任务、来源可信度、冲突证据或恶意 memory 的完整处置机制。
- 四项主基准是 57-subject MMLU、164-problem HumanEval、CommonGen 与 ARC-Challenge；然而结果段/表格使用 `SRDD` 名称（§5.1、Table 1），正文没有在此处解释它与前述 ARC-Challenge 的对应。每 configuration 运行五次、报告均值和标准差（§5.4）。
- Table 1 给 D³MAS 85.3±2.1 MMLU、89.8±1.5 HumanEval、86.2±1.6 SRDD、76.8±1.8 CommonGen；相对 MACNET 的表内数字增幅分别很大（§5.5）。这些分数跨选择题、代码 pass/fail、生成/科学题直接并列，不等于真实多 agent 工作流的可靠性、source fidelity 或端到端用户成功率。
- 消融在 GPT-4 上移除 task/reasoning/memory/message passing/三层结构都会让 MMLU/HumanEval 降分，其中 flat architecture 从 85.3/89.8 到 64.1/68.7（Table 2）。作者还称 10--30% noisy memory 和随机 agent failure 下 D³MAS 保持 80% accuracy、baselines 降至 45%（Figure 6），但正文未给 noise 生成、故障模式、样本量或置信区间，故只能视作初步受控扰动证据。
- Figure 7 的“成本”是 prompt token consumption，报 MMLU 85.3% / 0.7M tokens、HumanEval 89.8% pass@1 / 1.6M tokens（§5.8）；不含 completion、embedding、图/message-passing、API 价格、延迟、工具调用、失败重试和维护成本。正文称所有模型用 GPT-4，Table 1 标题又称 GPT-4 与 Gemini-2.5-Pro 都评估，Figure 3/结果段还提及 GPT-5、DeepSeek-V3.1 等八模型但未给可审计的原始数值/协议。笔记保留这一报告不一致，而不将其解读为跨模型已充分复现。

## 适用边界与复现

- 适用于研究如何把一组可标注的子任务、推理中间结论和可检索知识显式协调，以减少小型 LLM team 中重复工作；不应直接用于开放网页代理、实时控制、机密/高影响决策或不受信任的多方知识融合。
- 复现应公开 task decomposition、agent profiles、图 schema 与所有节点/边更新、BGE-M3 version、similarity/retrieval thresholds、top-k、agent-count policy、memory sources、GPT API snapshot/prompts/temperatures、message-passing stop rule、五次 runs/seeds、三类 redundancy 的原始匹配和 token accounting。需要澄清 `ARC-Challenge`/`SRDD` 与 GPT‑4/Gemini/八模型图的确切协议和每一结果的模型/数据对照。
- 应对跨域/OOD、同义/多语 query、长时多 session、冲突/过期/不可信来源、hallucinated intermediate reasoning、prompt injection、恶意 agent/memory、agent dropout 的相关性、检索阈值/agent数扩展及真实总费用/延迟做独立对照。冗余下降也必须与事实覆盖、引用正确性、协作公平和有益重复核验之间的 trade-off 一起报告。
- 若用于有风险的工作流，memory node 需保存来源、时间、权限与置信度，agent 之间需最小权限和审计，所有外部动作应有独立 verifier、冲突升级和人工批准。少检索/少通信不能压过必要 cross-check，结构化图也不能防止错误证据在团队内传播。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM 多智能体协作、知识共享与通信效率论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WQMU8577.pdf) 核验三层异构图、冗余定义、GPT‑4/BGE‑M3/阈值与 agent 数、四个主基准、Table 1/2、噪声/agent-failure 图和 prompt-token 口径；同时如实记录 ARC/SRDD 与模型评测表述的不一致，未将其受控 benchmark 结果扩写为跨模型、开放环境、真实总成本或对抗安全保证。
