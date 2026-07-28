---
title: "Advancing Multi-Agent RAG Systems with Minimalist Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/QCQC1144"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QCQC1144.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["external_retrieval_and_prompt_injection", "reward_hacking_via_final_answer_score", "gold_evidence_idealization", "benchmark_qa_not_factuality_guarantee", "long_context_and_tool_dependency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Advancing Multi-Agent RAG Systems with Minimalist Reinforcement Learning

## 一句话总结

Mujica 将复杂 multi-hop QA 拆成 Planner 的高层子问题规划与 Worker 的检索/摘要，保留 summary-based history 以缩短上下文；MyGO 则筛选高终局 reward trajectory 后以常规 MLE/cross-entropy 更新 LLM。它在若干 KG/text QA 基准上提高 EM/F1，但 reward 只看最终答案、检索质量和部分理想化 gold-evidence 环境决定上限，不能证明真实 RAG 的事实性、工具安全或通用 agent 可靠性。

## 方法与证据

- Mujica 的 Planner 迭代思考、将原问题拆为可并行的条件独立 subquestions，并依据 Worker summary 再规划；Worker 对每个 subquestion 用 external retriever 取 top-⁠k contexts、检查相关片段并回传 concise answer。两角色可共享同一 LLM、只用不同 instruction prompts，避免两份大模型成本（§2.2、Figure 1--2）。
- 作者将 subquestion dependency 处理为 DAG，而不是 chain：同一 iteration 内独立问题并行，后续问题可依赖前面的答案。ablation 中去除 planner-worker split 或 DAG-like reasoning 都降低 2Wiki-KG/Text EM/F1（Table 4）。
- MyGO 的 reward 是整个 conversation trajectory 的最终答案 F1；先把 entropy-regularized target policy 写为 Boltzmann distribution，再保留 reward 高于动态阈值 (K) 的 trajectories，最后对 curated trajectories 做 MLE。它故意不使用 PPO/GRPO 的 value function、advantage、ratio clipping、importance sampling 或 reward-normalization（§3.1--3.3、Eq. 5--6）。
- Proposition 3.1 说明若阈值足够高，筛选分布 (\pi_{>K}) 可逼近 entropy-regularized optimal policy；Proposition 3.2 讨论 (\alpha\to0) 时的性质。主文自己将其可行性归因于 well-prompted LLM 常能生成一部分清晰成功/失败 trajectory；这是条件化的渐近采样论证，而不是任意 agent/task 的全局训练保证（§3.3）。
- 评测有 2Wiki-MultihopQA、QALD-10（KG），HotpotQA、MuSiQue（text），报告 EM/F1。2Wiki-KG 提供 gold topic entities；Hotpot-Kimi 直接给每题 10 个 gold supporting passages，以近似完美检索。Hotpot 原始设置中 retriever 是主要瓶颈且无 answer aliases，会压低 lexical EM/F1（§4.1--4.2）。
- Qwen2.5-7B 在 Hotpot 上 WarmUp→MyGO 为 40.55/52.35→41.54/53.79 EM/F1，在 Hotpot-Kimi 为 52.51/66.04→54.07/68.48；表 3 同时显示许多 baseline 使用不同 backbone/retriever，作者明确说不能只以分数直接横比。OOD 设定 Hotpot→MuSiQue、2Wiki→QALD 亦有提升（Table 2--3、5）。

## 安全边界与复现

- Planner/Worker 会把检索结果、摘要与历史写回后续 prompt；不可信网页、文档或 KG text 可引入 prompt injection、检索投毒、错误事实、版权/隐私内容和 compounding summary error。角色拆分与 reward 筛选都不是 sandbox 或 trust boundary；应使用来源 allowlist、content isolation、instruction/data separation、citation provenance、tool least privilege、query/result logging 与人类复核。
- F1/EM terminal reward 可被表面匹配、答案格式、数据泄漏或简短投机策略利用，且不奖励检索忠实度、引文有效性、不确定性披露、过程正确性、拒答或伤害避免。高 reward trajectory 不等于可靠 reasoning trace，特别是较长多轮/开放域检索。
- Hotpot-Kimi 的 gold passages、2Wiki-KG 的 gold topic entities 会隔离或减轻真实 retrieval 错误；真实开放检索的表现受 corpus freshness、ranking、coverage、工具成本和对抗内容主导。论文也观察到原始 Hotpot 的 retriever bottleneck，不能把 Kimi/benchmark 增益宣传为 production RAG accuracy。
- 多模型/检索器之间不可由表中 EM/F1 直接比较；复杂 pipeline 对 instruction following/reasoning 有较高要求，小规模 pretrained model few-shot 结果不理想。应报告 exact LLM/retriever/version、corpora、prompts、sampling/threshold schedule、warm-up data、reward/normalization、token/cost/latency、failure traces、citation correctness、injection/poisoning/OOD tests 与 calibration。
- 不得用于医疗、法律、金融、政策或企业决策的无监督答案。高风险应用至少需要 domain corpus governance、实体/事实验证、citation-level audit、confidence/abstention、human approval 和可追溯 rollback，而非只依赖 QA reward。

## 与 AAMAS 的关系与核验说明

这是 multi-agent RAG workflow 与 LLM RL-style post-training 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QCQC1144.pdf) 核对 Mujica Planner/Worker/DAG、MyGO 的 thresholded-trajectory MLE、Proposition 3.1--3.2、2Wiki/Hotpot/Hotpot-Kimi/MuSiQue 设置、Table 2--5 与作者的 retrieval/comparability 限制；没有将 benchmark QA 得分表述为真实检索事实性、工具安全或高风险部署保证。
