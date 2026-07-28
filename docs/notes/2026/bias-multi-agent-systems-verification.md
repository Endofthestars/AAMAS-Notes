---
title: "Reasoning about Bias in Multi-Agent Systems Verification"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "argumentation_reasoning", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/RTAL7233"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RTAL7233.pdf"
source_url: "https://vadimmalvone.github.io/papers/AAMAS26c.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["fairness_definition_scope", "formal_semantics", "complexity_claim_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source formal check)"
reviewed_at: "2026-07-29"
---

# Reasoning about Bias in Multi-Agent Systems Verification

## 一句话总结

论文把“偏差”建模为偏差敏感属性对非敏感可观察行为的干扰：在并发博弈结构上扩展 ATL/ATL* 为 bATL/bATL*，并给出相应模型检验过程与复杂度结论。

## 方法与证据

- 模型是有限的并发博弈结构（CGS），每个原子命题由偏差标签函数映射到偏差等级的完全格；正文实验性示例是有学生、AI 审核者和人工审核者的录取过程（Definitions 1、6，Example 1）。
- 在两级 `NB ≤ B` 的简化下，`NB` 等价只要求非偏差敏感命题一致。论文进一步定义弱路径等价（只约束最终可观察结果）和强路径等价（逐步保持等价）；Proposition 1 仅证明强等价蕴含弱等价（Definitions 7–8，Proposition 1）。
- 偏差策略在给定 outcome 公式下寻找两条不等价的完成路径，并据此定义 weak/strong bias；bATL* 为联盟策略量词加入 `𝔅w`、`𝔅s` 算子（Definition 9–11）。
- Theorem 3 的正确性对应的是“全体代理”情形与该模型级 bias policy 的等价；它不等于对任意子联盟、任意策略画像或现实数据集的公平认证。
- 对 bATL，Algorithms 1–4 用前驱算子、固定点和有限 outcome witness 前缀处理公式；论文给出可判定性（Theorem 4）和 PTIME-complete 结论（Theorem 5）。对 bATL*，论文以非确定树 Büchi 自动机处理策略树，给出可判定性（Theorem 6）和 2EXPTIME-complete 结论（Theorem 7）。

## 形式化范围、局限与复现

- 这里的“无偏/有偏”是作者选择的非干扰式、命题标签和 CGS 路径等价定义，并不直接覆盖统计公平、因果公平、训练数据偏差或真实部署中的群体伤害；偏差敏感属性及 lattice 标注本身是输入建模决策。
- 模型级定义检查系统是否*允许*偏差行为，正文 Remark 1 也说明它不是固定策略 profile 的偏差结论。将结果解释为某已部署策略的公平性，需要先限制到该策略所诱导的路径。
- Definition 9 将 outcome 不可达作为 bias policy 析取的一支；但 Algorithm 3 对空策略集合的注释写作“Trivially unbiased”。论文的 Theorem 3 亦涉及空/至多一条 outcome 路径的真值情形。使用实现前应明确采用何种空集语义，不能把这两处文字直接混为同一结论。
- 复杂度是针对论文所述有限 CGS、逻辑片段和模型检验输入的最坏情况结论；并不说明为任意 LLM、连续状态系统或从日志自动抽取偏差标签的端到端代价。
- 复现应重建 Definitions 6–11、Example 1 的原子命题/动作/标注、Algorithms 1–4 的固定点和 witness 前缀截断规则，以及 NTBA 构造；论文给出的是算法和理论例子，未在正文给出可核验的软件仓库或实证基准。

## 与 AAMAS 的关系与核验说明

工作将公平/偏差治理问题嵌入多智能体的策略时序推理。笔记以作者公开的[论文 PDF](https://vadimmalvone.github.io/papers/AAMAS26c.pdf)作主文本，并将定理结论、建模假设和定义/算法间需要实现者澄清的空集语义分开记录。
