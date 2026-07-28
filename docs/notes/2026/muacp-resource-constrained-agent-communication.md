---
title: "µACP: A Formal Calculus for Expressive, Resource-Constrained Agent Communication"
conference: "AAMAS"
year: 2026
track: "research"
topics:
  - "agent_engineering"
  - "argumentation_reasoning"
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PHRW6922.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_theory"
review_batch: "2026-pilot-01"
spark_draft_verdict: "pass_after_revision"
spark_qa_verdict: "pass_after_revision"
spark_consistency: "revised"
risk_level: "high"
risk_tags: ["formal_claims", "consensus", "compression"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "theory_claim_scope"
escalation_verdict: "pass_with_conditions"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass; GPT-5.6-Terra theory audit)"
reviewed_at: "2026-07-28"
---

# µACP: A Formal Calculus for Expressive, Resource-Constrained Agent Communication

## 一句话总结

论文提出资源受限通信演算 µACP：以四个通信原语、TLV 消息结构和资源语义支持有限状态智能体协议的表达、压缩分析与在严格假设下的共识实现。

## 研究问题与方法

- RCAC 模型把内存、带宽、CPU 与能耗纳入通信资源约束（§4.1）。
- µACP 使用 `PING`、`TELL`、`ASK`、`OBSERVE` 与 TLV 选项表达消息；定理 8、10 讨论其对有限状态 FIPA 语义的编码能力（§4–6）。
- §7 以 TLA+ 与 Coq 检查有限状态资源与故障语义；§8 给出微基准、仿真和延迟比较（Table 3）。

## 关键证据与理论边界

| 结论 | 证据位置 | 可安全表述 |
|---|---|---|
| 压缩界 | Theorem 16，p.54 | 对消息分布 D、固定头长、有限 TLV 种类、且 payload 用最优前缀码时，期望编码长度不超过 `H(D)+H_hdr+ceil(log2 k_max)+3`；因此距熵下界为固定加性项。 |
| 共识实现 | Theorem 17，p.54–55 | 在 GST 存在、少于半数崩溃、非故障节点在 GST 后连通且有有界延迟、最终稳定 leader 等前提下，µACP 原语可实现 Paxos 风格共识；安全始终成立，活性只在 GST 后成立。 |
| 实证 | §7–8，Figures 1–6、Tables 2–3 | 论文报告模型检验、机械化验证与仿真；这些结果用于验证理论对齐，不构成穷尽的跨协议性能基准。 |

禁止将定理 16 泛化为无条件“最优编码”，或将定理 17 泛化为拜占庭、任意网络或无同步条件下的共识保证。

## 贡献、局限与 AAMAS 关联

1. 将通信语义、资源预算与形式验证置于同一 MAS 通信框架。
2. 给出有限状态协议的四原语编码、压缩界与共识约化链。
3. 范围限于有限状态/有限嵌套及崩溃或遗漏故障；递归协议、拜占庭容错与完整硬件能耗闭环不在主张范围（§9）。

它连接 AAMAS 的智能体工程、通信语义和形式化推理方向。

## 复现与核验说明

- 优先核验 §4–7 的模型、定理条件与 TLA+/Coq 工件，再复核 §8 的表图。
- 本笔记采用 Spark 两轮独立审校；Theorem 16/17 额外由 Terra 针对原文条件与结论定点复核。
