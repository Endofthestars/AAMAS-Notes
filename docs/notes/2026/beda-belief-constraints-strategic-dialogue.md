---
title: "BEDA: Belief Estimation as Probabilistic Constraints for Performing Strategic Dialogue Acts"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: "10.65109/ZJJG5330"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZJJG5330.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "finite_world_set", "belief_estimation_error", "strategic_persuasion_risk", "synthetic_game_benchmarks", "no_human_subject_validation", "no_belief_calibration_or_consent_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# BEDA: Belief Estimation as Probabilistic Constraints for Performing Strategic Dialogue Acts

## 一句话总结

BEDA 不把对话对象 belief 直接塞进 prompt，而是先在有限 event world set 上用微调 BERT 估计“说话者相信什么”和“对方知道什么”，再只把满足 dialogue-act 概率约束的事件交给固定 LLM 生成；它在 Keeper--Burglar、Mutual Friends 与 CaSiNo 基准中提升策略任务分数，但这并不验证模型对真实人的心智状态推断、沟通同意或安全说服，且“adversarial act”本身会带来操纵/欺骗风险。

## 方法与证据

- BEDA 设定 two core acts：Adversarial Dialogue Act 传达 speaker 认为真、且认为 interlocutor 不知道的信息；Alignment Dialogue Act 传达 speaker 认为处于 shared common ground 的信息（§1--§2）。这把复杂战略对话压缩为两个事件筛选条件，未覆盖明确拒答、求澄清、诚实披露不确定性、长期关系、相互理解、文化/权力差异或多方会话。
- 三组件为：有限 world set（conditions/attributes/preferences 等 event inventory）、belief estimator、conditional generator（§2）。从 context，estimator 预测每个 event 是否从 self perspective 为真以及 opponent 是否知道；实现为 fine-tuned BERT，之后固定 LLM 只根据满足对应 act constraints 的 events 生成 utterance。该约束可减少 belief 被 generator 忽略，却把安全性强烈依赖于 world-set 覆盖、event extraction、BERT calibration/错误以及 generator 是否忠实遵守条件。
- CKBG（Conditional Keeper--Burglar Game）是 adversarial task；表 1 中 BEDA 相对 w/o belief 在 GPT-3.5 为 86.9 对 78.4、GPT-4.1-nano 为 73.3 对 52.7、LLaMA3.1-8B 为 46.1 对 36.3、Qwen2.5-14B 为 92.7 对 80.2（§3）。随机 belief 有时也强（如 Qwen 80.9），说明 task cues/生成提示可能贡献显著；文中未给 estimator accuracy、置信区间、seeds、prompt/temperature、world-set size或对 belief-noise 的系统消融。
- Mutual Friends 是 alignment task；Table 2 的 BEDA success rate 分别为 GPT-3.5 41.1%、GPT-4 82.5%、GPT-4o-mini 70.4%、Qwen2.5-14B 64.1%，高于该表的无 belief/CoT/Self Reflect/MindDial 比较（§3）。“success”是 benchmark objective，不能证明用户理解、信任、知情同意、情绪影响或实际协商结果更好；SR/#turn/#token 指标也不代表对话质量或公平。
- CaSiNo 是 mixed setting，正文仅以 Figure 2 展示不同方法的 average agreement reward/rate（§3），没有可审计的原始数值、样本量、统计检验或不同利益分配群体的分析。agreement 本身可能通过迁就/压力获得，不能被视作 mutual benefit 或无操纵。
- 原文为 Extended Abstract，未报告 BERT 的训练数据/标签/评估、world-set 构建与更新、belief posterior calibration、错误事例、真实人类实验、披露/同意、跨语言/文化公平、对手可操纵性、deception detection或高风险领域安全评估。结论仅称 constrained generation 在三项设置的 strategic reliability 更好（§4）。

## 适用边界与复现

- 可用于研究封闭、可枚举事件游戏里如何把明确的 epistemic state 接入对话生成，或作为 ToM/strategic-dialogue 的受控 benchmark 模块；不可直接用于销售、政治劝说、法律/医疗/心理支持、招聘、教育评价、谈判或对弱势/未成年人群的真实人机交互。
- 复现需公开每任务的 world set/event ontology、context-to-label protocol、self/opponent belief annotation、BERT architecture/training split/calibration、act predicates/threshold、LLM snapshots/prompts/decoding、baselines、CKBG/MF/CaSiNo data/splits、所有 seeds、raw utterances、success/agreement metrics与统计。应报告 false belief constraint、constraint violation和 generator 聊天质量，而不只最终游戏分数。
- 必须评测 belief ambiguity/uncertainty、missing/contradictory events、adversarial interlocutors、prompt injection、opponent-aware counterstrategies、misclassification across dialects/cultures、long conversations、multi-party settings、real human comprehension/consent/affect、fairness与harm。加入拒绝/告知/修正机制，比较“更少策略干预”的安全基线。
- 在任何现实部署中，belief estimates 应被当作不确定内部假设而非用户事实；禁止以“对方未知但我认为为真”的条件来秘密优化说服。系统需要用户可见的目的披露、最小化心理画像、明确 opt-out、敏感主题阻断、来源和置信度说明、独立 harm review 及人工升级。较高 benchmark success 或 agreement rate 不构成可靠心智推断、诚实沟通或安全影响的保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的战略对话、belief/ToM 建模与约束生成论文，且为 Extended Abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZJJG5330.pdf) 核验两类 act、world set/dual belief BERT/fixed generator、CKBG/MF/CaSiNo 三项设置、Table 1/2 数字和 Figure 2 的有限报告范围；没有把封闭游戏的策略可靠性夸写为真实用户 belief 识别、可接受的说服、欺骗安全或通用人机对话能力。
