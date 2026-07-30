---
title: "ConvPayMAS: Conversational Payment Multi-Agent System with Agent-to-Agent Protocol and Three-Mandate Verification"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["agent_engineering", "generative_agents", "safety_verification", "human_agent_interaction", "applications"]
dblp_key: ""
doi: "10.65109/YDMY4904"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YDMY4904.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05m"
spark_draft_verdict: "source_grounded_with_subagent_hierarchy_phase_and_backend_integration_overstatement"
spark_qa_verdict: "needs_revision_corrected_for_five_subagents_four_phases_security_claims_backend_examples_and_evidence_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["payment_security", "pci_scope_claim_not_certification", "autonomous_payment_authority", "card_data_and_session_key_governance", "conversation_log_privacy", "human_confirmation_revocation_and_spending_limits_unreported", "threat_model_and_attack_testing_missing", "fraud_and_dispute_validation_missing", "latency_cost_reliability_and_scale_missing", "failure_recovery_unreported", "llm_and_prompt_details_missing", "video_without_code_artifact", "production_integration_not_established"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_payment_architecture_mandate_crypto_pci_autonomous_authority_backend_integration_and_production_boundary_check"
escalation_verdict: "needs_revision_corrected_for_subagent_phase_security_compliance_backend_example_evaluation_and_control_gap_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted payment-security and authorization-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# ConvPayMAS: Conversational Payment Multi-Agent System with Agent-to-Agent Protocol and Three-Mandate Verification

## 一句话总结

ConvPayMAS 用 CSA 统一入口、A2A agent messaging、AP2 的 Intent–Cart–Payment mandates 和 MCP payment tools 串起 conversational checkout；论文展示了端到端原型，但没有 PCI audit、threat/fraud testing、量化 reliability 或自主付款控制证据，不能把架构主张解释为认证或 production guarantee。

## 系统定位

ConvPayMAS 面向 agentic commerce，把支付执行封装在 specialized server-side agent 内，使 shopping 与 merchant agents 不必直接处理 sensitive cardholder data。论文声称这样可形成 single payment entry point、isolate PCI scope，并保持 conversational flow（p. 4071）。

这些是原型的设计目标与作者主张。三页 Demonstration Track 论文没有第三方合规认证、安全证明或生产部署评估。

## Agent hierarchy

系统有三个 top-level agents（pp. 4071–4072）：

- **ConvPayMAS**：server-side payment agent，对外提供 conversational payment interface；
- **Shopper Agent**：user-side assistant，解释购买意图并搜索 marketplace；
- **E-commerce Agent**：merchant-side agent，处理 catalog、cart 和 payment initiation。

ConvPayMAS 内部的 **Conversational Supervisor Agent（CSA）** 是 external agents 的 sole entry point；它解析 natural-language requests，再路由给五个 specialized payment sub-agents：

1. List Card：读取 wallet 中的 masked PAN；
2. Create Card：接收 encrypted card data 并启动 OTP；
3. Validate Card：验证 OTP 并激活 card；
4. Charge Card：执行 transaction；
5. Recommender：为 transaction 推荐 card。

此外，Chat Summarizer 压缩 bounded context 内的 conversation history；Guardrail Agent 在对外传输前 redacts PCI/PII；Figure 1 还标出 Session Manager。它们不是第六至第八个 payment sub-agent。

作者用 LangGraph 编排 deterministic payment execution。MCP server 暴露 card registration、session management、wallet 和 payment operations，并连接 Mastercard payment infrastructure。Figure 1 中 MPGS、Agent Pay、MDES 是 service-environment examples，不是本文证明全部完成并验证的 integration suite。

## Protocol 与 disclosed security mechanisms

### A2A 与 session

顶层 agents 使用 Google Agent2Agent（A2A）protocol。论文写道 messages 由 AES-256-CBC 和 session keys 保护，sessions 用 JWT（HS256）管理（p. 4072）。

### AP2 three mandates

作者实现 Google Agent Payments Protocol（AP2）的三类 mandate：

- **Intent Mandate**：记录 purchase intent；
- **Cart Mandate**：由 merchant 签名，包含 items、prices 和 shipping choices；价格改变时需重新签名；
- **Payment Mandate**：把 user authorization 绑定至 cart，并以 hash chain 关联 payment contents。

E-commerce Agent 在创建 transaction session 前检查 JWT signatures、expiry、audience claims 和 hash chain。正文还写 Cart Mandate 使用 HMAC-SHA256。

### Card handling

正文披露的 card controls 包括：

- PAN、CVV、expiry 在 client side 使用 AES-256-CBC 加密；
- MCP server 发放 per-session keys；
- PAN 经 Luhn check，expiry 在 wallet storage 前验证；
- Create/Validate Card 通过 OTP 完成 card activation；
- List Card 只返回 masked PAN；
- Guardrail Agent 在 conversation logs 外传前进行 PCI/PII redaction。

论文没有说明 authenticated encryption、IV/nonce handling、key derivation/rotation/storage、trust roots、revocation 或完整 threat model。笔记不据此断言存在某种具体 exploit，但这些实现与治理信息缺失，意味着不能独立评估 disclosed primitives 是否被安全组合。

## 四阶段 payment flow

论文按四个 phases 描述 live transaction（p. 4072）：

1. **Intent & Discovery**：用户向 Shopper Agent 表达需求；Shopper 创建 IntentMandate 并通过 A2A 发给 E-commerce Agent；merchant 搜索 inventory 并返回 signed CartMandate。
2. **Selection & Payment Mandate**：用户选择 item 和 shipping；Shopper 创建含 JWT 的 PaymentMandate，引用 Cart authorization 和 hashed payment contents。
3. **Session Creation**：E-commerce Agent 验证 three mandates 的 cryptographic integrity；通过后创建 transaction session 并返回 session token。
4. **Payment Execution**：用户携 session token hand off 至 ConvPayMAS；CSA 调用相应 payment sub-agents 与 MCP tools，完成后以 natural language 返回 confirmation。

流程展示 normal path；论文没有列出 mandate mismatch、expired session、partial charge、agent failure、duplicate request、refund、rollback 或 recovery path。

## Demonstration 证据

作者声称 demo 覆盖：

- end-to-end conversational checkout；
- live mandate verification；
- card-security workflows；
- multi-agent coordination；
- autonomous travel-research scenario with pre-authorization。

论文提供 [demo video](https://vimeo.com/1152577656)，但没有 code repository。live showcase 说明流程能在作者环境中运行，不等于：

- A2A/AP2 或 cryptographic composition 已被 formally verified；
- “trusted and secure”得到 attack testing；
- “isolates PCI scope”获得 PCI assessor certification；
- “verifiable dispute resolution”覆盖真实 dispute、fraud 或 liability；
- Mastercard service examples 已全部 production integrated。

## Security、compliance 与 evaluation 缺口

论文没有报告：

- threat model、attack/fraud scenarios、penetration test 或 security audit；
- PCI assessment、scope diagram、data-flow inventory 或 compliance evidence；
- success/failure rate、latency、throughput、cost、availability、scale 或 load test；
- baseline、ablation、user study 或 independent deployment；
- LLM backend、model version、prompts、decoding、guardrail false-positive/negative rate；
- mandate replay/downgrade/mismatch handling、session expiry failure 或 idempotency；
- payment failure recovery、refund/rollback、audit retention 或 incident response；
- source code、commit、dependency lock、configuration 或 test fixtures。

因此不能从 demo 推出 production reliability、安全性或可复现部署。

## Autonomous payment 与治理边界

多 agent 链路把自然语言购买意图推进到 card charge，涉及 financial harm 的高影响决策。正文没有说明：

- 哪一步必须由 human explicitly confirm；
- authorization 如何撤销、过期或限定 merchant、amount、time 和 purpose；
- spending limits、velocity controls 或 risk-based step-up approval；
- Shopper、merchant 或 CSA 被 compromise 时如何 suspend/recover；
- card/session/conversation data 的 retention、access、deletion 和 audit policy；
- dispute、mistaken purchase 和 agent error 的责任与人工申诉渠道。

这些是未报告的 control gaps，不等于本文已经发生漏洞。生产使用需要独立合规审查、least-privilege authorization、human confirmation、revocation、transaction limits、tamper-evident audit、failure recovery 和 adversarial testing。

## 页码与核验说明

PDF 逐页核对：p. 4071 为 identity、Abstract、Introduction、contributions、demo video footnote 与 ecosystem overview；p. 4072 为 agent architecture、sub-agents、LangGraph/MCP、security/protocol design 和四阶段 flow；p. 4073 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YDMY4904.pdf) 核对 hierarchy、mandates、crypto statements 与 evidence boundary；`reviewed` 不表示 PCI compliance、安全性、fraud resistance、自主付款治理或 production integration 已经验证。
