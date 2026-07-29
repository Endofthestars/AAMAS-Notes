---
title: "IntentGuard: Securing MCP-Enabled LLM Agents via Post-Decision Semantic Plan Verification"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "generative_agents", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/PJGH6650"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PJGH6650.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "benchmark_evidence_only", "judge_model_dependency", "tool_metadata_remains_trusted_for_selected_tool", "post_decision_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# IntentGuard: Securing MCP-Enabled LLM Agents via Post-Decision Semantic Plan Verification

## 一句话总结

IntentGuard 提出 Intent–Plan Consistency：不试图让可能已受污染的 MCP planning context 变得可信，而是在执行前检查最终 tool-call plan 是否仍与用户意图一致。其 VISTA 为每一步建立仅含 user query、selected tool、该工具描述和参数的隔离验证上下文，并由 Judge LLM 同时检查工具选择与参数来源；在 7,967 条派生 benchmark 样本上优于所列 baselines，但它依赖 selected-tool metadata 与 Judge 的可靠性，且不能阻止执行时行为、权限或下游系统遭攻击。

## 方法与证据

- 威胁是 Tool Metadata Poisoning：外部 MCP server 的自然语言 tool description 被操纵，使 agent 生成语法/权限都合法、但语义偏离用户请求的调用链（§1）。论文关注 plan-level intent misalignment，不覆盖所有 prompt injection、malicious tool binary、服务端返回污染、credential theft、TOCTOU、supply-chain compromise 或已执行动作的回滚。
- 对 finalized plan \(T_{call}=\langle a_1,\ldots,a_n\rangle\)，VISTA 要求每个 step 都通过 \(V_{step}(q,a_i)\) 才接受整计划（§2.1）。它是 post-decision interceptor，意味着上游 planner 可以未可信；但在 plan 被批准后，工具实现/response/环境状态变化仍可能造成危害。
- 每个 step 的 Isolated Verification Context（IVC）只保留 user query、server name、selected tool、该 tool description 与 generated parameters，丢弃其他 tool metadata（§2.2）。这减小 unrelated poisoned descriptions 对 Judge 的影响；但 selected tool 的 description、server identity、parameter schema 和 user query 本身仍在 trusted computing base 中，论文没有证明这些信息不可伪造或已签名。
- 双重语义检查包括：Tool Intent Validation（从 \(q\) 抽取核心意图、概括 tool 行为、判定匹配）和 Parameter Provenance Validation。后者把每个 parameter 标为 User_Query、Tool_Default 或 Illegitimate，并验证来自 query 的语义未失真；任何 step 失败则 reject（§2.3）。这些判断交给 LLM Judge，因而受 model error、prompt ambiguity、多语言、隐含用户偏好、复杂跨步语义和攻击适配影响。
- MCPIntentEval 由 MCPTox 的 7,967 tool-call responses、7 个 agent models、45 MCP servers、353 tools 派生，标为 intent-aligned / intent-misaligned（恶意诱导或 benign error），并去重（§3）。用 Qwen3-8B 作 Judge、单 A100、3 runs；Table 1 的 VISTA 各 dataset F1 在 94.95–97.93%，例如 DQ14* 为 97.64%（best listed baseline 89.31%），摘要称最高 accuracy +13.13%、F1 +9.48%、false positives 最多少 90%。没有 annotation agreement、held-out real server、adaptive attack、端到端 tool execution、延迟分位数、成本按 plan length 或安全 incident 结果。

## 适用边界与复现

- 适合作为 MCP agent 的执行前 defense-in-depth 层，尤其在 tools 动态发现、需发现 cross-tool hijacking 或明显参数来源异常时；不应作为单独的 authorization、安全沙箱、secret management、tool signing、egress filtering 或人类审批替代品。
- 复现需取得 MCPTox 到 MCPIntentEval 的过滤/去重/labeling 规则、七个 dataset split、all prompts/tool descriptions/plans、Judge system prompt、Qwen3-8B revision/decoding、IVC construction、provenance label procedure、baseline configs、3-run seeds 和 FPR/TPR computations。必须确保 evaluation IVC 与 production IVC 不泄漏 test labels或引入 metadata 差异。
- 应做未知 servers/tools、签名和未签名 metadata、selected-tool description 也被投毒、长多步计划、跨工具 data flow、tool response injection、parameter encoding/Unicode、多语言/歧义 intent、低频高危操作、adaptive attacker 与真实 end-to-end sandbox 的测试。报告 precision/recall/FPR、block/allow 的效用成本、latency/tokens、拒绝原因稳定性和按风险等级的误判。
- 生产防护还需 capability allowlist、schema/type validation、最小权限与短期凭据、可信 registry/metadata signatures、network/filesystem sandbox、transaction preview/confirmation、审计日志与异常 rollback。高影响写入、转账、删除、外发数据等动作应以 deterministic policy 和人类批准覆盖，不应仅依 LLM semantic judge 的“通过”。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 MCP-enabled LLM agent 安全 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PJGH6650.pdf) 核验 Tool Metadata Poisoning、post-decision IVC、双重验证、MCPIntentEval 的规模、Qwen3-8B/单 A100/3 runs 和表 1 的 F1；没有将 benchmark 检测性能写成对所有 MCP 攻击、可信 selected metadata、真实工具执行或生产级安全的保证。
