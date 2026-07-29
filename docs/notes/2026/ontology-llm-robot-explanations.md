---
title: "Blending Ontologies and Language Models to Generate Sound and Natural Robot Explanations"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "generative_agents", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/WAZM4282"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WAZM4282.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "human_robot_explanations", "ontology_grounding", "llm_narrative_generation", "lab_mockup", "no_user_study", "not_factual_or_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Blending Ontologies and Language Models to Generate Sound and Natural Robot Explanations

## 一句话总结

本文将 robot experiences 的 plan metrics、ontology-based episodic memory/inference、selective narrative retrieval 与 LLM generation 串成解释流水线：本体负责可追溯的结构化 comparison knowledge，LLM 将检索的 narrative 表达得更短、更易读。金属 SSD case 协作视觉检查的实验报告，相比 ontology-only baseline，生成解释在不同 specificity levels 平均短 33/86/93%，较高 detail levels 的 readability 指标改善 19/76%，与 baseline narrative 的 semantic cosine similarity 均高于 0.7。此处“sound/natural”是对 ontology-grounded narrative 与这些自动指标的主张，不证明每句话事实正确、完整、无幻觉、符合用户理解，或提升实际人机信任与协作安全。

## 方法与证据

- 框架依据 explainable agency 的四项功能：（1）评价候选 plan/experience 的 makespan、cost 等 properties，（2）将比较/分类知识做 ontology inference 并存入 episodic memory，（3）从 memory select/retrieve ontology-based narrative，（4）由 LLM 转写成自然语言（Figure 1, §2）。每一步的错误、缺失 plan properties、过期 memory 与 retrieval miss 都可能让流畅表述偏离真实机器人状态。
- 作者以 explanations 具有 contrastive、selective、social 特性为设计原则：比较 alternatives，按 detail/specificity 选择内容，并通过对话传达。该哲学/设计动机并不等于已证明 LLM 对任意 follow-up 具有 grounding；摘要仅称可通过后续 prompts 调整第四步，interactive scenario 仍待扩展。
- evaluation 记录 lab mock-up 的 industrial collaborative visual inspection of metallic SSD cases 的 robot episodes。以既有 ontology narratives 为 baseline，统计 LLM explanation 的 brevity、clarity 和与 baseline 的 semantic cosine similarity（§3）。未见真实生产线部署、机器人操作性能、安全 incident、ground-truth factual error、不同 LLM/model prompt、n/seeds/CI或 independent human raters 的完整披露。
- 结果称 level 1/2/3 分别平均短 33%/86%/93%；levels 2/3 readability 分别改善 19%/76%；similarity 一直超过 0.7。较短/较易读和 embedding similarity 并不蕴含忠实性、因果解释质量或人类实际理解；baseline 若有遗漏/错误，保持其语义关联同样不能纠正。
- 作者以 150–160 words/min speaking、250–400 words/min silent reading 的下界换算示例时长，并把水平 2/3 baseline 的分钟级阅读/聆听同生成 explanation 的秒级对比。这些是由平均长度推导的可读性说明，非实测用户完成时间、认知负荷、信任或协作成效。摘要明确把 user studies 和 interactive evaluation 列为 future work。

## 适用边界与复现

- 适合在有显式 ontology、可记录 robot plan/metric、且可以追溯支持证据的受控 HRI/XAI 原型中生成解释草稿。高风险协作、维修、医疗/工业安全环境不能仅凭自然语言解释批准动作；应保持状态/provenance 可视化、硬约束、安全 interlock 和人工监督。
- 复现应公开 robot task/mock-up、experience and plan logs、ontology/schema/reasoner、metric computation/classification、episodic-memory representation、retrieval/query selection、LLM/version/system prompt/decoding、specificity templates、baseline implementation及全部 samples。分别由 domain experts 和目标 users 标注 factual support、omissions、hallucinations、actionability、clarity、calibration、trust及 time，而非只报长度/embedding similarity。
- 应测试 sensor/plan uncertainty、stale/contradictory ontology facts、retrieval failure、adversarial or malformed prompts、multi-turn user challenges、different languages/users、distribution shift和 real robot faults。部署时须明确解释不等于控制逻辑，提供引用到 source facts 的审计路径、权限/隐私控制、纠错/升级机制和停止条件。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 explainable robotics/HRI 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WAZM4282.pdf) 核验四步方法、SSD-case lab mock-up、brevity/clarity/similarity结果与 future user-study scope；没有把自动可读性或语义相似度写成解释真实、安全、用户信任或实际协作效果证明。
