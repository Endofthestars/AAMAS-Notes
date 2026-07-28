---
title: "Deception and Communication in Autonomous Multi-Agent Systems: An Experimental Study with Among Us"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "human_agent_interaction", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/FRXL8789"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FRXL8789.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["single_model_sandbox", "automated_deception_labels", "small_human_annotation_sample", "text_game_to_real_world_gap", "intent_inference_limit", "reasoning_trace_privacy"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Deception and Communication in Autonomous Multi-Agent Systems: An Experimental Study with Among Us

## 一句话总结

论文在文本化 Among Us 中让 Llama 3.2 agents 进行 1,100 局角色对抗，按 speech-act theory 和 interpersonal deception theory 分析会议发言。数据中 98% utterances 被标为 directives；impostors 在受怀疑时略多 representative statements；被标为欺骗的发言主要是 equivocation（91.2%），会随 ejection 增加，却不能可靠预测胜负。该结果描述单一模型、规则明确的游戏 sandbox 与一个自动标签器下的语言模式，不能据此断言模型有可迁移的“意图”、或现实人机沟通中必然存在同样的欺骗能力。

## 方法与证据

- 每位 player 是一个 Llama 3.2 instance，获得私有角色、可见环境状态和离散动作菜单；task phase 可移动/做任务，impostor 还能 kill/vent；meeting 中只做 Speak，随后私密投票。日志保存 condensed memory、thinking process 和最终 action（§3.1--3.2）。
- 实验覆盖 4--8 players 的 11 个 crew/impostor configurations（如 3v1、5v2、5v3），每种随机角色分配重复 100 次，共 1,100 complete games；每次 meeting 固定 3 轮对话。作者公开 scripts、prompts 和 collected data（§3.3--4）。
- 结果标签用 speech acts（directive、representative、commissive、expressive）与 deception types（falsification、concealment、equivocation、missing）。标签并不是游戏引擎的真值；它们是对自然语言的后验分类（Table 1--2、§5--6）。
- speech-act 选择：50 条 meeting utterances 由两位人类、Gemini、ChatGPT 标注；human--human agreement 72%，Gemini--human 72%，Gemini--ChatGPT 62%，于是全量使用 Gemini。论文的“98% directive”及角色差异都依赖该分类管线（§5.1--5.2）。
- deception 标签同样以 50 条人工样本校验：human--human 73%，Gemini--human 86%，Gemini--ChatGPT 64%；全数据跑三次，87.2% labels 完全相同，作者据此将 Gemini 用于 aggregate analysis（§6.1）。这支持有限的标签稳定性，不等于欺骗意图的 ground truth。
- 在被识别为 deception 的 utterances 中，equivocation 占 91.2%，falsification 2.2%，concealment 0.7%，缺失/不可解释 6.0%。winning/losing games 的类型分布差异不显著（\(\chi^2(3)=4.42,p=.22\)）；以各类计数预测胜利的 logistic regression 也没有显著 coefficient（§6.2、Table 4）。
- 各类 deceptive language 与 ejections 正相关，尤其 equivocation \(r=.56,p<.001\)；这可表示在社交压力增大时语言更模糊，也可能由更多会议/对话机会共同驱动，不能推出欺骗导致胜负或心理状态（§6.2--6.3）。

## 适用边界与复现

- Among Us 被改成完全文本的、规则清晰的合成环境，没有现实人际互动的非语言线索、长期关系、开放世界事实核验、成本或法律后果。游戏内 role-conditioned statement 不应直接等同现实系统的蓄意欺骗。
- 只测 Llama 3.2，一个 prompt/agent architecture，4--8 player 与固定 3-turn discussions；模型版本、system prompt、sampling、memory truncation、action validity、task/地图随机化都可能改变语言分布和 game outcome。作者也明确承认 single-model、text-only 与 Gemini 分类器的限制（§7.1）。
- Gemini 的标签与人类有限样本的一致性只能证明分类近似；equivocation 特别依赖上下文和意图判断。应保留原话、角色可见信息与事件序列，进行更大双盲人工标注、跨标签器/模型/seed 的 calibration，并报告混淆矩阵和不确定性。
- 日志包含 thinking process。部署或复现时须按模型供应商和隐私规范处理，不应将 reasoning traces 当作可靠意图证据或向不必要的读者公开；对人机实验还须取得同意并防止诱导性/操纵性对话伤害。
- 可复现时固定公开仓库 revision、Llama checkpoint/API、prompt、temperature/seed、11 个 configuration、每条件 100 games、meeting turns、分类 prompts/版本与统计模型；另测不同模型、mixed human--AI groups、对抗性 prompt、语言/文化差异和真实可验证事实任务，才可评价外部效度。

## 与 AAMAS 的关系与核验说明

这是 generative agents、通信与信任治理的实验性 MAS 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FRXL8789.pdf) 核对游戏/agent setup、1,100 局设计、分类可靠性、Table 3--4 与局限；没有将自动语言标签或 sandbox 相关性误写为模型内在意图、跨模型事实或现实欺骗风险的因果证明。
