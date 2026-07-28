---
title: "Everyone Contributes! Incentivizing Strategic Cooperation in Multi-LLM Systems via Sequential Public Goods Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "game_theory_mechanism"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SJPO2377.pdf"
preprint_url: "https://arxiv.org/abs/2508.02076"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["spne_assumption_scope", "llm_rationality_gap", "evaluator_reward_misspecification", "benchmark_generalization"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Everyone Contributes! Incentivizing Strategic Cooperation in Multi-LLM Systems via Sequential Public Goods Games

## 一句话总结

MAC-SPGG 让多个 LLM 按顺序读取前序输出，并以带协同奖励、共享任务收益和失败惩罚的公共品回报训练各自的 PPO meta-policy；在论文给定的连续得分与参数假设下，其形式化博弈具有促使正贡献的唯一子博弈精炼纳什均衡。

## 方法与证据

- 每个 agent 依序生成文本贡献 $\tau_i$，可采用 partial observation（仅部分前序信息）或 full observation（完整历史）。其 reward 由个人生成成本、与前序质量有关的协同项、均分的最终任务分数及任务未达阈值时的共同惩罚组成（§3.1–3.2、Definition 1）。
- LLM 本身不被直接当作理论中的理性玩家；实现上以任务/上下文/位置 embedding 形成 belief，PPO meta-policy 输出生成配置向量，再条件化基础 LLM 的文本生成。每个 agent 是单步 rollout 的独立 actor-critic learner（§3.3、Algorithm 1）。
- Theorem 1：若 individual score 在 $[c_{min},c_{max}]$ 且 $c_{min}>0$，成本严格凸、可微且边际成本为正，并且共享回报 $\rho$、协同系数 $\gamma$、失败罚 $P$ 满足论文列出的下界不等式，则存在唯一 SPNE；其结论是每名 agent 正贡献且最终任务分数达到 $B(q)$（§3.2、Appendix B）。该定理不是对任意 LLM 输出、任意 evaluator 或任意奖励参数的保证。
- Theorem 2 在同一均衡/非负贡献条件下给出比较静态：总 welfare 随 $\gamma$ 与 $\rho$ 增大、随任务阈值 $B$ 增大而下降（§3.2、Appendix B）。
- 实验比较 zero/few-shot single agent、majority voting、multi-agent debate、CAMEL、ECON 和 MAC-SPGG；基准为 HumanEval（Pass@1）、MMLU/GSM8K（accuracy）及 SummEval（平均人工评分）。表中最强 MAC-SPGG 设定在 HumanEval、MMLU 或 GSM8K 的领先配置随 PO/FO 而变；SummEval 的最优 MAC-SPGG 为 FO 4.728，而不是 PO（§4、Table 1）。
- 消融分别检查 agent ordering、部分/完整观察与 reward 组件；作者将顺序可见性和特制机制描述为性能来源，但这仍是该模型、evaluator、训练预算和 benchmark 下的经验归因（§4、Tables 2–3）。

## 局限与复现

- 定理把“贡献”压缩为正且有界的 scalar score，并假设所有 agent 的最低贡献严格为正；真实 LLM 可以空答、偏题、相互强化错误，且 token/延迟成本未必严格凸，因此不可据此推断现实协作必然消除 free-riding。
- 任务成功、个人质量和奖励都依赖 evaluator $E$ 与阈值 $B(q)$。若 evaluator 可被投机、与真实目标错配，PPO 会优化该代理回报而非可靠性、事实性或安全性。
- PPO configuration policy 与基础 LLM 输出之间的因果链并没有把理论 SPNE 的完全理性证明自动转化为训练收敛证明；论文的 early stopping 是经验规则。
- 复现应公开 base model/LoRA 与 PPO 参数、PO/FO history 格式、reward 的 $\rho,\gamma,P,B$、evaluator 训练与评分、agent 排序、随机种子、token/调用成本和每项 benchmark 的原始输出；并加入 adversarial evaluator、低质量前序消息和更异质模型的压力测试。

## 与 AAMAS 的关系与核验说明

该文把序列公共品博弈与 LLM 多 agent 协作训练结合，涉及生成式 agent、MARL 与机制设计。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2508.02076) 手工核对奖励、两个定理的条件和实验指标范围。
