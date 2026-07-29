---
title: "Teaching LLMs Naturally: Pedagogical Strategies for Interactive Knowledge Acquisition"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/JGLB4831"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JGLB4831.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["in_context_only_learning", "single_model_single_condition", "synthetic_ontology", "perfect_teacher_access", "llm_judge_extraction", "no_persistence_test", "knowledge_poisoning_unexamined"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Teaching LLMs Naturally: Pedagogical Strategies for Interactive Knowledge Acquisition

## 一句话总结

该文让 GPT-4o teacher 以十种教学话术向 GPT-4o learner 讲授合成“外星物种”本体；top-down 讲解和部分混合策略比同内容 glossary 更能在当前会话后重构本体，但不更新权重、不测跨会话持久性，且本体重构好并未显著提升 20 Questions 的提问效率，因此它证明的是受控 in-context 对话的结构化信息传递，而非 LLM 获得可泛化、可验证的长期知识。

## 方法与证据

- 知识域是由 GPT-4o 生成并固定的 JSON ontology：10 个 alien species、每个 5 个类别特征（Diet、Habitat、Morphology、Locomotion、Social Structure，§4.1）。teacher 的 system prompt 含完整本体，learner 初始没有该信息，只能通过对话得到；这去除了事实错误、检索失败和教师知识不确定性，但与人类教学或开放世界知识更新不同。
- 教学策略按概念 framing（top-down/bottom-up）、提问方向和 initiative 组合：TD、BU、LQ、TQ、Mix-TQ、Mix-LQ、Mix-TD-TQ、Mix-BU-TQ、Mix-TD-LQ、Mix-BU-LQ；glossary 是同内容静态文本 control（§3.1--3.3）。每段对话为 40 个交替 turn（各 20），teacher 每次发言后 learner 写 1--2 句当前理解 summary；这是 prompt-controlled conversational scaffolding，不是 online gradient learning。
- 所有模拟使用相同 GPT-4o、OpenAI API，temperature 0.3、max_tokens 10,000（§4.1）。10 个 training conditions 各实例化一次；知识重构阶段才让每位 learner 对每个 ontology 独立重构 5 次（§4.3）。因此“跨 repetitions/ontologies 稳定”的表述不能替代多次独立 teacher/learner session、不同模型、prompt robustness 或真实人类教师的统计证据。
- 用 GPT-4o（已获完整参考本体）将每轮对话解析为 \((entity,feature,value)\) triplets，多次提取后取多数结果估计 information exposure（§4.2）；重构也按与 reference 的 triplet 对齐评分。该评测可量化预设结构，却依赖同类 LLM judge/解析器，未报告人工标注一致性或对提示格式敏感性。
- 结果称 pedagogical 条件整体在 ontology reconstruction 上优于 glossary，TD 接近完整、低方差；Mixed Learner Questions 平均接近但在实体/深层关系上更不稳定，纯 LQ 最弱（§5）。这支撑在这套固定合成本体与固定交互长度内，明确结构/teacher control 比自由 learner inquiry 更可靠。
- 应用评测是自动化 20 Questions：20 个随机 candidate sets，每个有 8 species，learner 最多问 20 个 yes/no feature 问题，oracle 完全知道 ontology（§3.5、§4.4）。部分策略在问题数上与 full-ontology expert baseline 无显著差异，但论文自身报告 dialogue information 与 20Q steps 无关联，重构 accuracy 与 20Q 也无关联（\(r=-0.044,p=.903\)，§5）。所以“记住事实”并不自动带来更好的策略性使用。
- 作者提出加入 teacher verification/brief formative tests 以发现遗漏，并将人类参与、较短对话和 ontology size scaling 列为未来方向（§6）。文中没有测错误教师、对抗性/敏感知识、conflicting instruction、learner 拒绝机制、跨 session memory、权重更新、真实任务 transfer 或知识遗忘。

## 适用边界与复现

- 适合探索怎样把小型、可结构化、可立即放在上下文中的知识以更清晰的对话传达给 LLM；不能据此宣称模型已被“训练”、将永久掌握新领域，或可由普通用户安全地教授医疗、法律、财务、控制或安全流程。
- 复现需发布所有 ontology-generation/teacher/learner/judge prompts、GPT-4o snapshot/API params、十种策略脚本、40-turn transcript、glossary 对照、triplet extraction 多次运行与投票、五次重构、20 candidate-set/target seeds、Welch/BH 检验与完整原始 scores。须单独统计 API 失败、context truncation、教/学角色混淆和内容格式影响。
- 扩展验证应使用不同模型和模型版本、独立会话/多 seed/多 teachers、现实/带噪知识、跨主题/跨会话保留、source citation、主动 verification、误教/冲突/恶意 prompt、隐私数据以及实际 human teaching。应同时测事实正确性、行动成功、calibration、拒答和知识删除，而不只测同一生成模型能否复述其合成 JSON。
- 若允许用户“教”生产 agent，新知识需区分临时上下文与经批准的持久记忆；须有来源、权限、内容审查、版本/过期机制、冲突检测、可撤销回滚和高风险操作的独立验证。自然对话与较高重构分数不构成可信指令或安全授权。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的人机/社会学习、交互式知识获取与可教 agent 论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JGLB4831.pdf) 核验 GPT-4o 设置、合成 10-species JSON、十策略与 glossary、40 turns、单次训练条件、5 次重构、20Q 协议、相关性结果和作者提出的 verification/human-teaching 后续方向；没有将无权重更新的会话内表现夸写成长期学习、真实人类教学效果或高风险知识注入安全性。
