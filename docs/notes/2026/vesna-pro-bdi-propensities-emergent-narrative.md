---
title: "VEsNA-Pro: Exploiting BDI Agents with Propensities for Emergent Narrative"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "human_agent_interaction", "generative_agents"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PDPF4024.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["prototype_scaling_scope", "short_dialogue_personality_measurement", "simulation_to_real_world_gap", "compatibility_metric_sensitivity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# VEsNA-Pro: Exploiting BDI Agents with Propensities for Emergent Narrative

## 一句话总结

Pro-AgentSpeak(L) 为 AgentSpeak(L) 的 BDI agent、plan 与 intention 加入可变/不可变的数值“propensity”标注，并以匹配度重写选择规则，使共享 plan library 中的角色表现出不同的性格和情绪轨迹；论文在 VEsNA 游戏原型与短对话中展示行为多样性和人格感知，但不证明真实心理建模或大规模游戏部署效果。

## 方法与证据

- agent 在每一时刻有从 propensity dimensions 到 $[-1,1]$ 的 profile；plan 带有其相关维度的 stance annotation，且可带 post-effect。执行后仅对 mutable dimensions 做 clipped sum 更新，因此人格等可固定、情绪等可随 plan 变化（Definitions 3.1–3.4）。
- 该扩展将 applicability-plan selection 和 intention selection 改为优先选择与当前 profile 最兼容的候选。兼容度可用 L1、dot product 或 cosine；三种度量会给出不同选择。也给出按兼容度采样的随机版本，并加 fairness factor 以避免长期饿死不匹配 intention（§3.2–3.3）。
- 在给定“纯” AgentSpeak(L) 不可对数值 propensity 作比较、选择函数不可读取数值的前提下，Theorem 3.8 说明无限 dense propensity 的行为不能由有限普通 plan library 等价编码；离散为 $m$ 级、$d$ 维时，Theorem 3.10 给出最坏情况下 $\Theta(|A|m^d)$ guarded cases，而扩展表示为 $O(k+d)$。这是受语法与选择器访问限制约束的表示性比较，并非一般 BDI 性能下界。
- 实现基于 Jason 与 VEsNA，propensity 存为 Java objects 并镜像为 beliefs，`pr(...)`/`eff(...)` 由加载时解析；concert 原型使用 Godot，彩色 agents 的计划约 133 个、灰色 baseline agents 约 96 个（§4.1）。
- Concert case study 让 OCEAN profile 的角色在日常与演出、疾病扰动中行动。作者把 active agents 增至 50，报告 propensity 与 stochastic/fairness deliberation 开销约随人数线性增长，标准笔记本上保持交互帧率；该结论来自原型压力测试，并未提供跨硬件、完整吞吐量或更大规模基准（§4.1）。
- Believable-dialogues case study 用 4 段由 agent 自主产生的办公室对话（46 plans）。93 名匿名参与者各任选一段，以改编短版 Big Five Inventory 评估角色 OCEAN；论文报告 Extraversion/Neuroticism 在 8 个 agent-profile 对中 7 个方向一致、Conscientiousness 6/8、Agreeableness 5/8，而 Openness 仅 1/8 被正确解释，且强度常被高估或低估（§4.2、Table 1）。

## 局限与复现

- propensity 的语义、各维度、plan annotations、post-effects、compatibility metric 和 fairness 系数都是开发者指定，不是从行为数据学习出的可验证人格；换 metric 即可能改变行为，因此不能把输出称为客观的心理状态或因果解释。
- 性能证据仅限 50 个自主 NPC 的单一 Godot/VEsNA 原型与作者的“interactive frame rates”观察；不能由此推断大型在线世界、不同硬件、网络同步、复杂 LLM 对话或生产游戏预算。
- 93 人问卷覆盖自选的四段短对话，衡量的是参与者对模型化 trait 的重建相似度。它不检验长期叙事投入、玩家信任、角色一致性、教育/训练效益或真实人物人格准确性，尤其 Openness 结果较弱。
- 理论编码结论依赖禁止数值测试和 selector 访问 propensity 的 pure-AgentSpeak(L) 定义；允许数值 guard、不同元解释器、有限范围或外部状态机时，不能直接照搬该不可编码/爆炸结论。
- 复现应固定 Jason/VEsNA 版本、计划库与 `pr`/`eff` 标注、初始 OCEAN vectors、compatibility/fairness 与随机种子；独立记录每轮选择和 clipped updates。问卷应预注册采样与分析，随机分配对话，并报告完整受试者与 trait-level 数据。

## 与 AAMAS 的关系与核验说明

该文属于 BDI agent programming 与游戏/叙事型人机交互：它将角色倾向直接接入 plan 和 intention 的决策环。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PDPF4024.pdf) 核对形式化定义、选择机制、编码范围、实现和两项案例；不将原型行为或问卷相似度外推为真实人格、玩家体验或生产系统可扩展性。
