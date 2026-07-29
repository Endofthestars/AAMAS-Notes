---
title: "Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "generative_agents", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/OITH7375"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OITH7375.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["psychological_construct_simplification", "llm_self_inference", "prompt_regulated_personality_ranges", "llm_as_judge_evaluation", "controlled_deterministic_simulations", "cross_cultural_generalization_gap", "human_validation_absent"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions

## 一句话总结

ASVO 将 LLM agent 的多维 desires、对他人满意度的推断与 Social Value Orientation（SVO）角度结合，再用人格预设区间调节 action prompt，以产生 altruistic/prosocial/individualistic/competitive 行为。其在 School、Workplace、Family 的受控文本模拟中获得更高 LLM-judge 自然度/人类相似度，但这说明框架内的提示一致性，不证明真实人的动机、人格演化或跨文化社会行为被准确建模。

## 方法与证据

- 每步 agent 观察环境和他人行为，以 LLM reflective loop 更新自身 desires 与对他人 desires 的估计；以 self/other satisfaction 的比值计算 \(\theta_{svo}=\arctan(S^{other}/S^{self})\)，再据候选行动的预期 satisfaction 和目标 SVO interval 选行动（§5.2--5.6）。self/other satisfaction 是 LLM 推断量，不是由人类心理测量或外部行为数据校准。
- 当计算出的 SVO 偏离预设人格区间时，系统改写行动生成 prompt，将选择“温和拉回”目标区间（§5.4）。Fig. 5 中四类人格始终处于各自 reference bands，部分反映该设计的 regulatory constraint，而不是人格漂移预测被独立验证。
- 实验在 extended Concordia text simulation 的 School、Workplace、Family 三种情境与微/中/宏社交尺度中执行，比较 ReAct、BabyAGI、LLMob、D2A 与 ASVO（§6.1）。这些是相对受控、确定性场景；行为不是参与者实验、田野观察或可验证的真实组织结果。
- Table 1 的 naturalness 与 human-likeness 由 LLM evaluators 按标准 prompts/rubrics 自动评分。ASVO 的平均值高于基线，例如 School 为 4.802/4.821，Workplace 4.819/4.049，Family 4.725/3.946（§6.2）。评委模型可能偏好同类 LLM 语言风格与框架给出的价值词汇，不能等同人类受试者的判断、预测效度或社会科学外部效度。
- 所有 agent 同一人格的 School repeated experiment 中，altruistic/prosocial 的 cooperation 比例较高；规模从 dormitory 到 class election 后，作者报告 altruistic cooperation 0.15→0.56、prosocial 0.22→0.28（§6.4）。这些比例依赖行为分类、场景叙述和 prompt，没有对照真实基线分布或统计不确定性。
- scalability 测试把 horizon 扩到 6/12/18/24、population 扩到 4/8/16/32；指标随 24 steps 与更多 agents 有下降。作者承认 fixed core desires 不能涵盖人类价值丰富性，且环境仍 controlled/deterministic，未来才探索开放、跨文化和多模态情境（§6.3--7）。

## 适用边界与复现

- 适用于研究中构造可解释的社会模拟原型、探索“显式价值状态如何改变文本行动”的假设，或生成教育/培训讨论素材；不应用于推断个体心理、给人贴人格标签、预测真实群体、自动化人事/教育决策或社会治理。
- SVO 和 desire taxonomy 是规范性建模选择。预设人格区间、满意度 offset/ratio、候选动作、记忆、系统提示与 LLM 版本会共同决定输出；相同叙述可因语言、文化、阶层、关系权力和隐私语境而有不同解释。
- 复现需固定 Concordia 环境/全部 scenario scripts、agent profile、desire list、SVO class ranges/offset/regulation prompts、candidate-action prompts、memory/observation、LLM versions/temperature、judge prompts、行为分类和随机 seeds。应发布原始 trajectories、judge inter-rater agreement、真人盲评、跨文化样本、消融（无 desires/无 SVO regulation/无自他推断）及失败案例。
- 若涉真实用户，需取得知情同意、避免将合成“人类相似”当作心理评估、实施偏见和隐私审计，并保留人工复核与申诉机制；SVO 模拟不是个体价值或道德品质的测量工具。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM social simulation、社会动机与人机交互论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OITH7375.pdf) 核验 ASVO 循环、SVO prompt regulation、Table 1、规模/人格实验和作者的 controlled-environment 限制；没有把自动 LLM 评分、t-SNE 聚类或被约束的 SVO 区间误写为真实人类动机、人格或社会行为的验证。
