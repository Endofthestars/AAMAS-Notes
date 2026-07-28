---
title: "SocraticAgent: An Autonomous Agent for Unlocking Latent Knowledge in LLMs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "generative_agents"]
dblp_key: ""
doi: "10.65109/XGHC3223"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XGHC3223.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["benchmark_limited", "llm_judge_dependency", "latent_knowledge_assumption", "fixed_prompt_policy", "hallucinated_recall_risk", "no_fresh_or_private_information"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# SocraticAgent: An Autonomous Agent for Unlocking Latent Knowledge in LLMs

## 一句话总结

SocraticAgent 是一个零样本、固定两动作的 LLM 编排器：先让模型拆解问题并反复补足它声称已知的必要事实，再只依据该召回上下文完成推理。它在三个静态常识问答基准上通常优于普通 CoT 与 Gemini 的网页检索设置；但“潜在知识/召回缺口”的度量本身依赖强 LLM 提取和裁判，且内部自述可能幻觉，对新近、私有或领域外事实仍需可靠检索与外部核验。

## 方法与证据

- 作者把 LLM 视为 agent 的工具和即时环境，而非修改其参数：固定策略先执行 Knowledge Deconstruction，围绕问题列出/修订需要的知识并由 critique 决定是否接受；随后 GroundReasoning 把召回集合 \(K\) 与问题送入 LLM 生成答案（§3, Alg. 1）。这是一种 inference-time prompt/workflow，不训练模型、也没有独立事实数据库或检索器。
- 诊断覆盖 StrategyQA、CommonSenseQA、TruthfulQA，意图隔离“通常已在通用模型中”的多步常识推理，不测 HotpotQA、MuSiQue、BrowseComp 等需要新鲜外部信息的检索任务（§4.1）。因此它支持的是这些基准上的 recall scaffolding，不是对通用 agent 知识、长程规划、工具执行或现实真实性的测量。
- ground-truth knowledge points 从既有工作注释的 reference 中由 Qwen2.5-72B-It 提取；Knowledge Possession Check 要模型逐条定义事实，再由 LLM judge 判对错；Coverage 则从 vanilla CoT 抽取显式事实、与该库存比较（§4.1–4.2）。所谓“模型已拥有 90–97% 而仅使用 57–64%”是此特定抽取—裁判管线的操作化结果，不能等同于可访问的参数事实总量或人类认可的知识状态。
- 自动评估全部采用 Qwen2.5-72B-It 作为 judge。作者人工复核 762 个判断（约数据的 1%）得到 95.54% agreement；在 700 个真人判为正确和 62 个真人判为错误的样本中，judge 的 Type I error 为 2.7%，Type II error 为 24.2%（§4.2）。总体一致率不消除不对称漏判，也不足以排除同模型族偏好、知识点抽取误差或评价泄漏。
- 基线包括标准 CoT、由标注真值 facts 提供的 Oracle RAG、Gemini-2.5-Flash 的网页 Noisy RAG、从既有论文直接引用的参数化 recall 微调结果、Self-Refine 和 Multi-Agent Debate（§4.2）。Oracle RAG 是理想信息上界，不是可部署 RAG；网页检索只在 Gemini 上运行，跨模型比较不应解释成“RAG 普遍更差”。
- Table 2 中，SocraticAgent 将 LLaMA3.1-8B-It 的三基准 mean 从 65.90 提至 76.78，将 Qwen2.5-7B-It 从 71.11 提至 76.14；后者也高于同表 Self-Refine 69.05 与 Multi-Agent Debate 71.73。Gemini-2.5-Flash 的网页检索 mean 为 74.23、vanilla 为 75.07、SocraticAgent 为 78.47；这些是该 prompt/benchmark 配置下的点估计，论文未以此建立所有 RAG 或所有模型的统计优越性。
- 小模型 Qwen2.5-1.5B-It 的 SocraticAgent mean 为 76.55，恰与 oracle-reference 条件的 76.55 相同（Table 2）；这是一个值得复查的基准结果，不表示内部回忆已变成事实来源。对 reasoning-fine-tuned 变体也并非单调有效：DeepSeek-R1-Distill-Llama-8B 略升到 77.25，而 DeepSeek-R1-Distill-Qwen-7B 降至 73.90（§5.4），与固定流程可能干扰既有 reasoning style 一致。
- 作者明确指出固定两动作不必对每题最优，内部召回可能 hallucinate；任务若需要及时或私有信息，RAG 仍不可或缺，并建议学习何时内省/何时检索的 meta-policy，及加入第二 critic 验证 recalled knowledge（§6）。

## 适用边界与复现

- 可作为静态、可由模型已有常识支撑的多步问答的候选 prompting baseline，尤其适合先把隐含前提显式化再作答的任务。它不应替代权威来源检索、数据库查询、代码/计算执行、临床/法律核验或有时效要求的工具链。
- 实际 agent 应把“模型自称知道”当作待验证的中间假设：对高影响结论要求可追溯来源、独立检索/工具交叉验证、置信与冲突处理、权限隔离和 human review；不要把 critique 的 ACCEPT 或更长 reasoning chain 当作真实性证明。
- 复现需固定三个 benchmark 的版本与 split、原始 reference、Qwen2.5-72B-It 的知识点抽取/judge prompt 与解码参数、所有模型精确 checkpoint、vanilla/RAG/Self-Refine/debate/Socratic prompts、deconstruction 迭代上限与停止条件、网页检索日期/结果，以及每类 token、延迟、调用次数和失败样例。应重做人工盲审，并报告 judge 的双向误差而不只报 agreement。
- 应在时效信息、私有企业知识、对抗性错误前提、长上下文、不同语言、领域推理和可验证工具任务上比较 adaptive retrieval 与固定流程，量化事实正确率、校准、成本、时延与幻觉传播；还应进行消融以分辨“额外 token/多轮调用”与知识拆解结构各自的增益。

## 与 AAMAS 的关系与核验说明

这是把 LLM 内部推理过程作为 agent action space 进行编排的工作，连接 agent architecture、知识表示与自动推理。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XGHC3223.pdf) 核对两动作流程、三项基准、模型/基线、LLM-as-judge 管线及人工误差、Table 2 数值、fine-tuned 模型的非单调结果和作者所列边界；没有把基准准确率、内部自述的知识点或 oracle 对照误写成事实验证、无检索需求、低成本保证或现实 agent 可靠性认证。
