---
title: "Formalizing Mental Privacy in LogiKEy"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: "10.65109/PTSF2244"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PTSF2244.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03v"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "formal-normative-model", "mental-privacy-scope", "case-study", "legal-interpretation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Formalizing Mental Privacy in LogiKEy

## 一句话总结

本文在 Isabelle/HOL 的 LogiKEy 中组合 belief、knowledge、necessity、STIT agency 和 directed obligation，形成 Logic for Mental Privacy (LMP)。它把 mental privacy 表为控制他人知晓“自己相信什么”的 claim-right，并借 BCI 平台案例展示：即使没有直接强迫受保护信念，借心理状态访问诱导中间信念也可能间接损害 freedom of thought。

## 方法与证据

- freedom of thought 被编码为其他 agents 有义务不使权利主体不可能相信受保护命题；可覆盖 belief、disbelief、suspension。mental privacy 则把 privacy 对象从外部事实换成对主体 belief 的 knowledge（§2）。
- LogiKEy 用 shallow semantic embedding 将 LMP 的 possible-world semantics 置入 HOL，调用 Sledgehammer 证明、Nitpick 找模型/反模型（§3）。
- Cerebra case study：平台从 BCI/ML 信号推知 Alice 的 belief，并诱导其相信中间命题 $q$，使她自行推断受保护的 $r$。Table 1 给出两个 worlds 的 assumptions；作者自动验证 assumptions 一致、$w_1$ 导出 mental-privacy violation、直接 coercion checker 可能漏掉对 freedom of thought 的间接伤害（§3）。

## 适用边界与复现

- 形式化证明的是所选 axioms/语义下的逻辑后果，不等同于现行法、技术 BCI 能力或实际伤害的经验证明；何种 belief 在权利范围内仍是政策选择。
- 复现需取得 LogiKEy source、LMP operator semantics、Isabelle version/automation设置、Table 1 assumptions及案例解释。应用时应将形式模型与数据最小化、访问控制、同意、审计和司法解释结合，而非仅靠 compliance logic。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PTSF2244.pdf) 人工核对 LMP、LogiKEy 和案例结论；未将该逻辑建模陈述为法律意见或神经数据事实判断。
