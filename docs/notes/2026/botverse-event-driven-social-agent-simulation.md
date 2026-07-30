---
title: "BotVerse: Real-Time Event-Driven Simulation of Social Agents"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "marl_coordination", "norms_trust_governance", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/CKXV2098"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CKXV2098.pdf"
demo_url: "https://youtu.be/eZSzO5Jarqk"
code_url: "https://github.com/netsecuritylab/BotVerse"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05s"
spark_draft_verdict: "source_grounded_with_required_mechanism_validation_phase_result_taxonomy_and_future_work_corrections"
spark_qa_verdict: "needs_revision_corrected_for_identity_human_likeness_demo_phase_marl_and_future_work_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["disinformation_generation_and_amplification_dual_use", "live_bluesky_content_privacy_tos_and_provenance_unreported", "synthetic_real_network_boundary", "egress_export_and_isolation_controls_unreported", "sensitive_persona_stereotyping", "malicious_prompt_and_image_risk", "human_likeness_unvalidated", "high_fidelity_and_safety_unvalidated", "scalability_and_fault_tolerance_unbenchmarked", "access_audit_retention_and_release_governance_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_disinformation_dual_use_live_content_persona_isolation_egress_human_likeness_scalability_and_release_governance_check"
escalation_verdict: "needs_revision_corrected_for_synthetic_network_demo_evidence_dual_use_persona_and_security_governance_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted disinformation, isolation, and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# BotVerse: Real-Time Event-Driven Simulation of Social Agents

## 一句话总结

BotVerse 用实时 Bluesky 内容触发隔离式、事件驱动的 LLM social-agent simulation，并提供 persona、memory、Digital DNA 与合成图像管线；500-agent 场景只是演示设置，论文没有验证人类行为逼真度、传播或检测效果、并发性能，也没有闭环误导内容双重用途与敏感 persona 的治理风险。

## 实时接地与隔离边界

BotVerse 从 Bluesky / AtProto 采样实时内容，为 simulation 提供 environmental grounding 与 event triggers；合成代理之间的交互发生在独立环境中，不直接让 bots 与真实社交网络用户交互（pp. 4107–4108）。

因此它不是 live bot deployment，也没有报告在真实 Bluesky 用户上开展的行为实验。论文 Phase B 使用 “genuine users” 一词，这与全文所述 “only allows interactions between agents in a separate environment” 存在未澄清的措辞冲突。三页稿没有说明该词究竟指真实用户还是 simulation 内的 agents，本笔记保留这一歧义，不把它改写为任何一方，并将其列为需要原作者澄清的边界。

这一边界能减少直接干扰真人的风险，但“隔离”是架构描述。三页稿没有说明网络 egress、凭证权限、数据导出或内容发布的技术控制，也没有给出 adversarial escape test。

## 四层架构

系统包含四层（pp. 4107–4108）：

1. **Synthetic Social Observatory**：React / TypeScript 前端，实时展示 interaction graph、agent profiles 与行为轨迹，面向 micro / macro observation。
2. **Orchestration API**：FastAPI 异步服务，通过 REST endpoints 连接前端与 simulation，支持可插拔 LLM backends；论文举例 GPT-oss 与 DeepSeek。
3. **Factory**：PostgreSQL-backed persistence，保存 agents、state 与 interactions，并把数据管理与执行逻辑分离。
4. **BotVerse Simulation Engine**：执行自主行为的 event-driven 核心。

作者称 Factory 可管理 thousands of agents/interactions，并强调 concurrent threads 下的 consistency 与 fault tolerance；论文没有给出吞吐、延迟、并发规模、故障注入或恢复基准，因此这些只能视为架构主张。

## 事件、Digital DNA 与时间行为

行为可由 environmental stimuli 或 internally scheduled events 触发。Digital DNA 把动作编码成序列，例如 `Post → Wait → Reply`，用于形成个体行为模式（p. 4108）。

作者还描述 human-like temporal distributions、burstiness 与 circadian rhythms。论文没有与真实用户轨迹做统计比较、分类盲测或人工评估，所以这些是仿真机制和设计目标，不是已经验证的人类相似性或 high-fidelity 结论。

## Memory、persona 与图像

Memory 选择分数为（p. 4108）：

\[
S=\alpha\cdot recency+\beta\cdot importance.
\]

其中 recency 随时间指数衰减，importance 以 likes、reposts 等 social resonance signals 近似。

Persona 使用高维 JSON profiles，包含 age、gender、country、education 等 demographics，也包含 politics、religion 等 psychographics；这些字段与行为属性在 runtime 注入 LLM prompt。

图像管线先让 LLM 生成与内部决策语义一致的 prompt，再由 Stable Diffusion 生成 synthetic image。论文没有报告 image safety filtering、版权与来源审查、恶意 prompt 防护或生成内容标记机制。

## 500-agent 演示场景

演示设置包含 \(N=500\) 个 agents（p. 4108）：

- 350 个 benign、disinformation-skeptical agents；
- 150 个 disinformative agents。

流程分三阶段：

- **Phase A — Seeding**：disinformative agents 从 Bluesky trends 取得触发信息并生成 deceptive narratives；
- **Phase B — Amplification**：通过 posts、likes、reposts、replies 与 persuasive reasoning 放大叙事；
- **Phase C — Multi-level analysis**：在 micro 层观察 agent trajectories / cognitive states，在 macro 层观察 narrative diffusion。

\(500/350/150\) 是场景配置，Phase A/B/C 是演示流程。论文没有报告实际传播半径、影响人数、检测率、叙事存活时间或干预效果，不能把阶段描述改写为已观察到的定量实验结果。

## 证据边界

三页 demo 没有报告：

- propagation、detection、classification 或 intervention metrics；
- throughput、latency 或 thousands-agent concurrency benchmark；
- random seeds、independent runs、variance 或 confidence intervals；
- 与真实社交用户的 human-likeness validation；
- baseline 或 ablation；
- 精确 LLM / Stable Diffusion 模型版本、参数、temperature 或推理配置；
- isolation、security、fault tolerance 或 consistency 的 adversarial / failure test；
- 对 persona-induced bias 或 stereotype 的测量。

因此论文中的 safe、secure、risk-free、high-fidelity、scalable、thousands、consistent 与 fault-tolerant 均是目标、设计或作者主张，不是本稿量化验证的结果。社会科学、AI safety、policy、crisis response 与 market analysis 等也只是可能用途，不是已验证的 downstream outcome。

## 高风险双重用途、安全与治理

系统明确生成和放大 deceptive narratives，因而具备直接的 disinformation dual-use 能力。即使交互留在 synthetic environment，模型、prompts、图像、persona 与 diffusion traces 仍可能被导出或迁移到真实系统。

三页稿没有说明：

- live Bluesky content 的 privacy、platform Terms、licensing、consent、retention 与 provenance；
- 网络 egress allowlist、真实平台写权限隔离、凭证管理与 export controls；
- deceptive outputs、prompts、images 与 traces 的访问控制和 release review；
- politics / religion 等敏感 persona 如何避免刻板印象、歧视与群体伤害；
- malicious prompt、prompt injection、生成图像与外部内容中的攻击处理；
- audit logs、operator identity、incident response、data deletion 与 retention policy；
- 如何阻止 synthetic disinformation assets 被复用于真实操纵。

这些缺口使该系统属于高风险 reviewed 条目。风险等级是对能力与未披露治理的评估，不表示论文证明系统已经对真实平台造成伤害。

## Future Work 与页码核验

Future Work 包括提高 agent behavioral complexity，并扩展 cross-platform simulations（p. 4108）。

PDF 逐页核对：p. 4107 为 identity、Abstract、Introduction 与四层架构起点；p. 4108 为架构续述、event/Digital DNA、memory、persona、Stable Diffusion、500-agent demo、use cases、Conclusion 与 Future Work；p. 4109 为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CKXV2098.pdf) 核验；`reviewed` 不表示人类相似性、high fidelity、传播或检测效果、scalability、isolation security 或真实部署安全已被验证。
