---
title: "Application of Artificial Intelligence for the Retrieval, Processing and Generation of Knowledge from Clinical Data"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["argumentation_reasoning", "applications", "safety_verification", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/CFJJ1446"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CFJJ1446.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05c"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_with_proposal_status_and_clinical_safety_boundary_reinforced"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_proposal", "clinical_decision_support", "llm_multiagent_system", "clinical_knowledge_graph", "computational_argumentation", "formal_acceptability_not_clinical_truth", "planned_metrics_and_termination_analysis", "no_implementation_or_experiment", "no_privacy_safety_bias_or_regulatory_evidence", "no_clinical_validation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_clinical_truth_formal_acceptability_termination_traceability_and_safety_governance_boundary_check"
escalation_verdict: "pass_as_proposal_with_no_clinical_correctness_safety_or_deployment_inference"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted clinical-safety check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Application of Artificial Intelligence for the Retrieval, Processing and Generation of Knowledge from Clinical Data

## 一句话总结

本文是以 Clinical Knowledge Graph（CKG）与计算论证为中心的临床多智能体系统博士提案；架构、形式语义、质量指标和终止性分析均属拟议研究，尚无实现、临床验证或安全治理证据。

## 研究缺口

提案位于临床决策支持 MAS、可解释 AI 与医学计算论证的交叉处（§§1–2，pp. 4011–4012）。

作者认为，已有临床 MAS 能整合病历、指南和文献，但证据优先级往往隐藏在内部规则或启发式权重中，没有显式表示论点、反驳以及选择 warranted conclusion 的形式标准。LIME、SHAP、CAM/Grad-CAM 等归因方法主要解释单一模型的特征影响，不能直接表达跨证据协商过程。Dung 框架和 ASPIC+ 等计算论证方法提供可辩驳推理工具，但仍缺少与检索、语义规范化和统一质量评测相连的端到端临床 MAS。

因此，博士计划试图连接：

1. 临床证据检索与语义规范化；
2. 支持、攻击和反驳关系明确的论证图；
3. 形式可接受性计算；
4. 从结论回溯到证据来源的设计链路。

这些是提案所定义的研究问题，不是已完成系统的能力清单。

## CKG 中心的四类代理

§3.1（p. 4012）提出以下分工：

- **Orchestrator Agent**：接收初始临床查询、启动 deliberation，并管理论证生命周期；
- **Retrieval Agent**：从临床记录和文献检索证据，再将抽取信息标准化并映射或写入 CKG；
- **Argument Construction Agent**：把知识图谱中的结构化事实转换为主张、支持论据、反驳以及初始 argument graph；
- **Evaluation and Verification Agent**：应用计算论证的 acceptability semantics，并计算拟议的论证质量指标。

CKG 在设计中承担结构化知识库角色。预期流程可概括为：

`临床问题 → 编排与检索 → 证据规范化至 CKG → 构造支持/攻击图 → 计算形式可接受性 → 返回结论及证据链`

论文没有数据库 ID 级追踪、证据粒度规范、消息协议、运行日志或可复现实例。因此“traceable links”是设计目标，不能写成已展示的审计能力。

## 三项博士研究目标

### Objective 1：架构与形式化

计划正式定义代理角色、消息类型和协调规则，并设计能从 CKG 导出的临床论证表示。正文举例可采用简化 Toulmin 或 ASPIC+ 方案，再选择 grounded 或 preferred acceptability semantics。

文中的 `guarantees stability and traceability` 出现在拟选择语义的目标描述中。提案没有给定理、证明、完整操作语义或实现，因此不能据此声称系统已经获得稳定性和可追溯性保证。

### Objective 2：指标与评估协议

计划提出超越文本质量的核心指标，包括：

- acceptability；
- traceability；
- 识别并处理 counterarguments 的能力；
- 对证据小幅变化的 robustness。

正文没有指标公式、数据、benchmark、实验协议、baseline 或数值结果。

### Objective 3：实验与比较验证

计划研究：

- 系统是否在有限步内终止；
- 在什么条件下能返回带 warranted justification 的建议；
- 在证据强冲突或不足时，什么条件导致系统不能得到 acceptable conclusion。

这些是待调查和待证明的问题。当前论文没有终止性证明、算法、运行轨迹或临床场景实验。

## 形式可接受性不是临床真值

形式论证语义回答的是：给定某套论点、攻击关系和语义规则，哪些 arguments 被接受。它本身不证明：

- 输入证据真实、完整或具有足够医学质量；
- 因果方向正确；
- 结论符合最新临床指南；
- 治疗对具体患者安全；
- LLM 忠实地解释证据而没有幻觉；
- 推荐会改善患者结局。

同样，论证图到来源的可追踪路径也不自动保证来源可靠或推理正确。提案提到 evidence strength、guideline alignment、safety/risk 和 patient preference 等评价视角，但没有把它们实现为临床安全边界、禁忌规则、失败降级或人工复核机制。

## 当前成熟度与治理缺口

三页稿没有提供：

- 系统原型、算法实现、代码仓库或部署方式；
- 临床数据集、抽取与切分协议、对照系统或统计结果；
- 医生或患者研究、指南一致性核验或患者结局；
- 隐私、去标识化、访问控制或安全评测；
- 偏差分析、伦理审批、监管合规或责任划分；
- 人工复核闭环、异常处理或部署失败策略。

因此不能把 clinical usefulness、robustness、verifiability、termination、safety 或 deployment readiness 写成已经验证的结果。

## 与 AAMAS 的关系与核验说明

该提案的 AAMAS 相关性来自专门代理分工、协调协议、知识图谱、可辩驳推理和形式语义，以及在高风险人机决策中构造显式 justification 的目标。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CFJJ1446.pdf) 核对 §§1–3（pp. 4011–4012）。目前可以复核的是问题定义和研究计划；形式正确性、临床有效性和安全性仍没有可核查的实现或实证证据。
