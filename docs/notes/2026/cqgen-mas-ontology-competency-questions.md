---
title: "CQGen-MAS: A Multi-Agent System for Competency Questions Generation from Ontology"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/RRYE6579"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RRYE6579.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02o"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "llm_generation_quality", "sparql_execution_not_semantic_truth", "expert_benchmark_ground_truth_assumption", "four_ontology_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# CQGen-MAS: A Multi-Agent System for Competency Questions Generation from Ontology

## 一句话总结

CQGen-MAS 用三个角色把已有 ontology 转为可检验的 competency questions（CQ）：Segmenter 产出语义连贯子图，LLM Generator 以少样本示例生成简单/多跳问题，SPARQL Validator 执行转换后的查询并追踪概念覆盖，未覆盖概念再反馈给 Generator。四个异构本体上，摘要报告其对专家 CQ 的 recall 高于 LLM4KE 与 RETROFIT-CQs，尤其在复杂题上较强；“能执行且有返回”只说明结构相容，不证明问题重要、措辞正确或覆盖了真实使用需求。

## 方法与证据

- 任务输入为以类和属性连接的 ontology \(O\)，输出 CQ 集合。论文将要求写为：每题转换为形式查询后引用的概念属于 \(O\)，并使被题目引用的概念在 \(|D_O|\) 中达到覆盖阈值 \(\alpha\)（§2，式 1--2）。
- Ontology Segmenter 选择 METIS、Louvain 或 Leiden 等图分割方式，形成语义相对连贯的子图，以避免把完整本体塞进 LLM context 时丢失结构、或把图切成孤立三元组后只得到单跳题（§3）。具体选择策略和参数未在扩展摘要中展开。
- CQ Generator 对每个子图使用少量域内高质量 CQ 示例及本体简述，生成单跳和多跳候选；SPARQL Validator 将候选转为查询并在 ontology 上执行，以成功且非空返回作为结构一致性证据，同时以引用类追踪 coverage。失败信息与未覆盖概念回流，形成 generate--validate--expand 闭环（§3）。
- 表 1 按简单/复杂题报告四个本体的 recall：CQGen-MAS 分别为 OneM2M 84.2/77.8、SAREF4ENV 80.0/66.7、VGO 88.9/71.5、VicinityCore 77.8/47.6；LLM4KE 为 16.7/13.3、31.1/3.8、55.5/21.9、24.5/21.4；RETROFIT-CQs 为 81.7/70.4、74.0/38.5、81.4/38.3、68.6/28.6（简单/复杂）。摘要还称多数情形 F1 更优，但未给出 F1 表、完整 LLM-method 配对或消融数据（§4、表 1）。

## 适用边界与复现

- 可用于补全缺失的设计期 CQ、辅助本体复用与测试清单；生成物应进入领域专家审阅流程，而不是自动成为需求规范或权威知识。
- SPARQL 可执行且返回非空，仍可能是过于宽泛、偶然命中、错误翻译或措辞含混的问题；反之，空结果也可能揭示合法但尚无实例的数据缺口。概念出现次数不是语义重要性、覆盖均衡性或用户价值。
- 评测把专家 CQ 视作 ground truth，但作者也指出其覆盖与对齐本身未经进一步验证；四个本体、题型标注、LLM 版本、prompt、分割和 query translation 都会影响 recall。摘要省略的 LLM 组合与消融使可比性有限。
- 复现应版本化 ontology、分割算法/seed/粒度、few-shot 示例、模型与 decoding、CQ-to-SPARQL translator、执行端点及 timeout；盲审语义正确性、可回答性、复杂度和新颖性，报告 precision/recall/F1、覆盖曲线、失败类型、成本与每轮增量，并用未见领域本体和人类需求验证。

## 与 AAMAS 的关系与核验说明

该文把 LLM、验证器和反馈循环组织为知识工程的多智能体工作流。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RRYE6579.pdf) 人工核对三角色、闭环验证、四本体、表 1 的 simple/complex recall；没有将 SPARQL 的非空执行或专家题集匹配夸大为本体语义正确性或需求完整性证明。
