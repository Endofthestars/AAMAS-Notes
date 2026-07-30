---
title: "An Agentic Voice-Based Assistant for Interactive Conversation and Guidance in Real-World Environments"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "planning_scheduling", "human_agent_interaction", "safety_verification", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/RGWK4224"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RGWK4224.pdf"
demo_url: "https://vimeo.com/1153194189"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06c"
spark_draft_verdict: "design_demo_without_quantitative_evaluation_or_governance_validation"
spark_qa_verdict: "needs_revision_corrected_video_page_and_preserved_unvalidated_confidence_safety_privacy_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_page_demo_without_quantitative_evaluation", "no_user_study_or_real_world_task_metrics", "confidence_formula_threshold_and_calibration_unreported", "explicit_control_graph_not_correctness_proof", "safe_grounded_authoritative_real_time_and_scalable_author_claims", "continuous_listening_and_public_space_voice_privacy", "transcript_session_and_feedback_governance_unreported", "unsafe_or_stale_tool_guidance_unmeasured", "prompt_injection_and_rag_poisoning_unreported", "manual_version_provenance_and_freshness_unreported", "qr_link_integrity_unreported", "staff_escalation_emergency_and_accessibility_boundaries_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_physical_tool_guidance_confidence_safety_continuous_listening_privacy_rag_poisoning_document_provenance_qr_integrity_and_staff_escalation_check"
escalation_verdict: "design_demo_with_unreported_evaluation_and_governance"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted physical-guidance safety and voice-privacy check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# An Agentic Voice-Based Assistant for Interactive Conversation and Guidance in Real-World Environments

## 一句话总结

AVA 是 makerspace walk-up kiosk 的 agentic voice assistant：STT/TTS 接收语音，显式 state-based control graph 依据 intent 与内部 confidence 选择回答、澄清或引导探索，RAG 检索本地 manuals/safety procedures，最后用语音和动态 QR code 输出；三页论文没有实验、用户研究或任何量化结果，因此不能把 “grounded”“safe operation”“real-time”“scalable”或 control graph 结构视为正确性、安全性或生产部署证据。

## 架构

AVA 分为四个部分：

1. **Speech Interface**：用 speech-to-text 与 text-to-speech 做双向语音交互；continuous listening 配合 silence-based segmentation 支持 hands-free walk-up use。
2. **Agent Core**：显式状态图依次处理 perception、intent inference、session memory、deliberation/confidence estimation、action selection 与 LLM response generation。intent 分为 general environment query、tool-specific request 和 session termination。
3. **Knowledge Service**：对 curated tool manuals、procedures 和 safety guidelines 做 RAG；文档带 metadata，检索内容与 session memory 一同注入 LLM context。
4. **Visual Output**：生成 QR codes，链接到 manuals、resources 或 feedback form。

论文称 action selection 在 LLM 之外由 agent state 控制；但没有提供完整 state graph、规则、confidence formula、threshold 或 policy parameters。结构化控制接口提高了可检查性，不自动保证选对 action 或生成正确答案。

## Confidence-aware deliberation

系统维护 internal confidence estimate：

- confidence 高时直接给出所谓 grounded response；
- confidence 低或请求不完整时主动询问 clarification；
- 还可 redirect/guided exploration。

正文没有说明 confidence 的计算方法、值域、threshold、calibration、abstention、error recovery 或 safe fallback，也没有验证 confidence 与事实正确性的关系。因此不能把 confidence 写成校准概率或可靠拒答机制。

## 八步 Demo 流程

1. **Walk-Up Engagement**：访客在 kiosk 用自然语音建立 session；
2. **Exploratory Discovery**：回答“这里能做什么”等开放问题；
3. **Targeted Guidance**：对特定 tool/process 给出短语音指导并强调安全使用；
4. **Contextual Deep-Dive**：显示链接 manuals/safety documentation 的 QR code；
5. **Adaptive Multi-Turn Dialogue**：用 lightweight session memory 支持追问；
6. **Clarification Under Uncertainty**：请求含糊时主动澄清；
7. **Project Ideation Support**：建议 project 和 tool combinations；
8. **Feedback and Session Closure**：结束时邀请反馈并显示 feedback-form QR code。

这是论文所述的 live demonstration journey，不是 task-completion study 或用户安全评测。

## 完全缺失的评测

正文没有 experiments/results/user-study section、table、benchmark 或 quantitative metric。未报告：

- speech recognition/TTS accuracy、noise/accent/language robustness；
- retrieval precision/recall、document relevance 或 answer faithfulness；
- factual correctness、hallucination、unsafe guidance 或 refusal rate；
- confidence calibration、threshold quality、clarification success；
- latency、availability、concurrency 或 cost；
- usability、accessibility、task success、productivity 或 staff workload；
- safety-procedure compliance、incident simulation 或 QR/link integrity；
- baseline、ablation、runs、variance 或 failure taxonomy。

因此 “real-time”“grounded”“authoritative”“safe operation”“scalable and consistent support”“continuous system improvement”只能标作设计/作者主张。反馈入口本身不证明系统已经形成有效的 improvement loop。

## Physical-space safety

Makerspace guidance 可能涉及 robotics、fabrication、electronics 与其他实体 tools。论文没有报告：

- 对 hallucinated、incomplete 或 stale instructions 的检测；
- manual source ownership、version、effective date、approval、refresh 和 rollback；
- tool state、user skill、PPE、local hazard 与现场条件确认；
- staff escalation、emergency stop、out-of-scope refusal 和 human override；
- QR destination allowlist、signature、redirect/tamper detection 与 link expiry；
- noisy environment、accent/language、hearing/speech disability 与 minors 的适配；
- incident log、liability、safety officer review 或 physical validation。

将 curated document 注入 RAG 或链接 “authoritative” manual，不能证明检索片段、LLM summary、spoken instruction 或 QR destination 始终正确。

## Voice、session 与反馈治理

Continuous listening、transcription、session memory 和 feedback 可能处理声音、对话内容和个人信息。正文没有披露：

- visible recording indicator、consent 与 bystander handling；
- on-device/cloud STT/LLM、external API transmission 和 data residency；
- raw audio/transcript/session/feedback retention、deletion、encryption 与 access；
- identity separation、minor data、sensitive query 与 audit policy；
- microphone activation control、network/secrets 和 abuse monitoring；
- prompt injection、spoken adversarial instruction、RAG/document poisoning；
- feedback contamination、review gate、versioning 与 rollback。

这些都是未报告控制，不表示系统已经发生录音泄露、误导或攻击。高风险来自 public physical-space voice collection 和 tool-safety guidance 的潜在后果。

## “部署”边界

论文把 AVA 描述为 deployed as a walk-up kiosk in a Makerspace，说明 demo implementation context；没有地点规模、运行时长、用户数、incident、production SLO、security review 或 certification。它不能被外推为经过生产验收的 deployment，也不能证明可泛化到 innovation labs、educational facilities 或其他 physical environments。

## 页码核验

- p. 4167：题名、作者、摘要、引言、应用场景、系统开头和 demo video 脚注；
- p. 4168：架构图、agentic behavior、BDI/neurosymbolic 对比和八步 demo flow；
- p. 4169：致谢与参考文献，没有新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RGWK4224.pdf) 核验；`reviewed` 不表示 confidence、回答正确性、physical safety、voice privacy、QR integrity、可扩展性或生产部署已经得到验证。
