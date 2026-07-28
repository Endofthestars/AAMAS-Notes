---
title: "MENSA: Leveraging Mental Simulation for In-Context Policy Improvement in LLM Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/BBRH3447"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BBRH3447.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["implicit_world_model_fidelity", "text_environment_scope", "experience_retrieval_dependence", "token_cost_sensitivity", "model_baseline_inconsistency", "no_embodied_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# MENSA: Leveraging Mental Simulation for In-Context Policy Improvement in LLM Agents

## 一句话总结

MENSA 是无微调的 model-based in-context LLM agent：Actor 以文本补全生成短期 action--state forecast，**用 forecast 检索**相关的已执行经验，再把经验放入 action prompt；Executor 将生成动作映射到环境允许动作，Experience Learner 在 episode 后更新经验集。它在文本环境 ScienceWorld 与 NetHack 上优于 ReAct、Reflexion、SSO；但 forecast 并非被证实的真实环境模拟，改进依赖文本状态、检索/分类器、有限 episode 和基准特定动作语法，不能直接推出对具身、开放世界或安全关键 agent 的可靠规划能力。

## 方法与证据

- 每步 Actor 的 prompt 由 one-shot example、检索经验、任务描述和当前 trajectory 组成；LLM response 被解析为实际 action 与未来数步 forecast。forecast 不直接控制环境，而是作为检索 query，帮助找到有用 subtrajectory（§4.1、Figure 1--2）。
- Executor 将 raw action 转成 admissible action；Experience Learner 在每 episode 后从执行轨迹构造/精炼 experiences。经验可按 state similarity 与 target similarity 组合，动态 prompt trimmer 在 context window 紧张时保留相关部分（§4）。
- 作者明确采用较弱主张：LLM forecast 是 task-relevant signal，而不是 faithful world-model。若预测错误、语义/状态抽象与环境不一致或检索到误导经验，整个 in-context policy 仍会退化（§2、§6）。
- ScienceWorld 为文本交互的科学任务；NetHack 测 Crossing Lava（取 key、开门、使用物品、跨 lava），有随机初始位置/实体，stage reward 0--100。adaptation 为同一 variant 连续 5 episodes、之间学习；ScienceWorld transfer 以 5 variants 的 15 trajectories 训练，再测未见 variants（§5.1）。
- 比较 ReAct、Reflexion、SSO。ScienceWorld adaptation 中 GPT-4o-mini 为 70.3 vs SSO 54.5（+15.8），Phi-3-mini 为 32.6 vs 20.7（+11.9）；NetHack GPT-4o-mini 为 50 vs 10，Llama-3-8B 为 32 vs 0（Table 1--2）。结果是环境分数，不是 forecast correctness 或现实任务成功率。
- 表格的模型条件并不完全同质：除 Phi-3-small/Phi-3-mini 及全部 SSO 外，作者用 base models；这些例外使用 instruction-tuned models，因为 SSO 与某些 base model 不兼容。统计显著性来自跨 18 task classes 的 89 scores Wilcoxon signed-rank test，比较/独立样本单位须谨慎解读（§5.3--5.4）。
- 消融中 forecast steps=3 最好；0--3 步时表现提高且 token cost 下降，超过 3 步则后续预测不相关/信息过载，表现和 token cost 都变差（§5.4.2、Figure 6）。target-first 与 state retrieval 组合得分 45.0，且反向相关度排序优于 shuffled（Table 5--6）。
- T-Eval 的 Instruct/Plan 分数用于解释不同 backbone 的敏感性；它是独立 capability benchmark，不直接证明实际 forecast fidelity。论文仅在文本交互评估，并在结论中指出具身扩展需要 perception/action grounding（§5.4.3、§6）。

## 适用边界与复现

- 不能将自然语言续写视为物理、因果或安全模拟器。实体系统应采用经校准的动力学/感知模型、action validation、约束规划、uncertainty estimation、runtime monitor 与 human override；文本 forecast 不可作为直接执行或安全论证。
- 增加 forecast 长度并非总有利，且有显著 token/latency 成本。部署需分别度量 simulator call、retrieval/embedding/classifier、actor prompt、重试与环境交互的成本和 deadline；不能只报告成功率。
- 每 variant 仅五个 adaptation episodes，transfer 仍在同一 ScienceWorld task 的新 variants；没有开放世界、工具 API 漂移、部分可观测、对抗内容、长期 memory 污染、多人交互或具身 robot 的测试。经验检索可能将早期错误固化，应设 provenance、success verification、过期/冲突处理和隔离评测。
- 复现应固定 project/code revision、environment version/task split、LLM checkpoint/API、base vs instruction-tuned condition、prompt/parser/admissible-action translator、seed（论文设为 42）、SentenceBERT/BART models、经验构建/refinement、retrieval ordering、context budget、forecast horizon、episode count 与 token-cost 公式；报告 per-task/seed scores、失败/invalid-action率与完整成本。

## 与 AAMAS 的关系与核验说明

这是 generative agents 的 in-context policy improvement 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BBRH3447.pdf) 核对 Actor/Executor/Experience Learner、forecast 的检索用途、环境/episode protocol、Table 1--6、token-horizon 结果与作者限制；没有将文本 forecast、基准增益或 T-Eval 相关性误写为真实 world model、通用规划能力或具身部署安全保证。
