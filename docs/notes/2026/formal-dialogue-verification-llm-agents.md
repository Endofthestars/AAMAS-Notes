---
title: "No Future for LLM-based Agents without Formal Dialogue Verification"
conference: "AAMAS"
year: 2026
track: "blue_sky"
topics: ["safety_verification", "argumentation_reasoning", "generative_agents", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/JFKY8456"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JFKY8456.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04q"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass"
spark_consistency: "pass_after_terra_formal_boundary_check"
risk_level: "high"
risk_tags: ["blue_sky_vision", "formal_dialogue_verification", "raw_text_to_logic_gap", "specification_validity", "regulatory_context", "no_verifier_or_llm_evaluation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_end_to_end_guarantee_and_regulatory_boundary_check"
escalation_verdict: "pass"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted formal/regulatory boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# No Future for LLM-based Agents without Formal Dialogue Verification

## 一句话总结

本文主张把 LLM 智能体的多轮对话转换成显式 move 与逻辑理论，再检查协议、断言和安全性质的联合一致性；它给出了形式骨架与玩具推导，但没有实现 verifier、验证真实 LLM 或证明从自然语言到逻辑表示的端到端安全保证。

## 验证场景与对话结构

- **Direct verification** \(I_a=\{v,\ell\}\)：verification agent（VA）直接与 LLM-based agent（LA）交互、提出主题并获取断言。
- **Observational verification** \(I_b=\{h,\ell\}\)：VA 不介入，只观察 human agent 与 LA 的对话。两种方式最终都产生有序 dialogue trace，供同一个逻辑转换步骤处理（§3.1，p. 3923）。
- move 写成 \(\langle a,\mathrm{Act},\mathrm{Content}\rangle\)，实例包括 `open` \(\langle a,\mathrm{open},\mathrm{Topic}\rangle\)、`assert` \(\langle a,\mathrm{assert},\langle S,c\rangle\rangle\) 与 `close`。
- information-seeking dialogue 的 well-formedness 要求：首项是 `open`，中间是与主题相关的 `assert`，末尾 \(|I|\) 项是 `close`，且发起者发出最终 `close`；允许单智能体 self-reflective dialogue，但重点是上述两类双边场景（Definition 3.1–3.2）。

## 从 trace 到一致性检查

- 转换 \(f:D\rightarrow\mathcal{P}(L)\) 把 assert move 的 support \(S\) 与 conclusion \(c\) 提取为逻辑规则/论证；所有 move 的提取结果合成 dialogue theory \(\Sigma_D\)。
- \(\Sigma_P\) 描述允许的 move、结构和协议规则，\(\Sigma_V\) 描述要检查的行为性质，\(\Sigma_D\) 则来自当前对话。
- 核心检查写为
  \[
  \Sigma_P\cup\Sigma_D\cup\Sigma_V\not\vdash_X\bot.
  \]
  若能推出矛盾，可能是协议违规、对话断言不相容、验证性质被违反，或 \(\Sigma_V\) 本身不充分/过严；该条件不能单独唯一定位是 LA、映射还是 specification 出错（§3.3）。
- Table 1 的示例依次 `open T`、断言 \(p\Rightarrow q\)、断言 \(q\Rightarrow r\)、`close`。若 \(\Sigma_V\) 要求 \(r\) 不得由 \(p\) 推出，联合理论产生矛盾，验证失败。这只是说明性推导，不是真实模型运行日志（§3.4）。

## 交付范围与保证边界

- 论文给出 Definition 3.1–3.2 和上述框架，但没有新的正确性/完备性定理，也未固定逻辑 \(X\)、自然语言映射算法、性质语言、可判定性或计算复杂度。
- 没有 verifier 实现、代码、数据集、LLM 对话 benchmark、基线或实验结果；作者把 dialogue-state extraction、自动验证工具集成与真实行为实证研究列为后续工作（§4–5，pp. 3923–3924）。
- 即使逻辑内部检查正确，保证也只针对 \(f\) 生成的理论和给定 specification。LLM 输出噪声、上下文敏感、遗漏语义或错误提取会使形式模型偏离真实行为；\(\Sigma_V\) 也可能漏掉真正风险。
- 论文援引 HLEG Trustworthy AI 与 EU AI Act 说明安全、透明、问责和操控风险的研究动机。它没有对具体系统执行法律分类、合规测试或认证，因此不能把该框架当作法律合规证据。

## 四个开放挑战

1. **连接形式模型与真实 LLM 行为**：可靠地把有噪声、依赖上下文的自然语言映射成 dialogue state、topic、belief 与 commitment。
2. **建模对人的影响**：对话可能改变人的信念、信心或决策，需要约束有害认知和情绪变化。
3. **处理数量与不确定性**：加入能发现渐进 belief drift、细微影响和累积操控的定量或 uncertainty-aware semantics。
4. **伦理与监管对齐**：让工具提供透明、可审计的证据，但仍需把抽象性质与具体义务、部署情境和人的影响连接起来（§5）。

## 与 AAMAS 的关系与核验说明

本文连接 formal argumentation、dialogue game、agent communication、Trustworthy AI 与生成式智能体安全。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JFKY8456.pdf) 核对 §3 的定义和 Table 1、§4 的适用讨论及 §5 四项挑战；没有把联合一致性条件表述为对原始 LLM 的普遍保证，也未把论文中的监管语境表述为法律意见。
