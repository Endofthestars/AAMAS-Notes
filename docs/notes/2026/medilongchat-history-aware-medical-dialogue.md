---
title: "Synthesis and Evaluation of Long-term History-aware Medical Dialogue"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/EFXQ8322"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EFXQ8322.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_medical_data", "llm_as_judge", "no_clinical_outcomes", "longitudinal_hallucination", "medical_privacy_governance", "text_only_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Synthesis and Evaluation of Long-term History-aware Medical Dialogue

## 一句话总结

论文提出 MediLongChat：先以经知识引导的虚构病人 profile/疾病--并发症时间线，再按单个 medical event 分解生成多轮问诊、按时间拼接，构造长期病史对话；并设计单会话、跨会话与全史综合三类问答。它有效制造长上下文 memory benchmark，但全部病人和对话均为合成，正确性/真实感主要由 LLM-as-a-judge 评估；这不是医疗器械验证、真实病历分布、临床诊断安全性或患者结局证据。

## 方法与证据

- Stage 1 用 patient persona、疾病/并发症 metadata 与时间规律生成虚构 lifetime records；作者称对 disease--complication association、时间顺序和事件间隔进行 targeted human-in-the-loop review。最终 benchmark 不向被测 LLM 提供中间 record（§3.1）。
- Stage 2 将每一 medical event 拆开：仅用 persona、该事件疾病/时间/干预做 isolated prompt，再生成临床 encounter，最后按 chronology stitch。每次对话约 50 exchanges、约 3,000 tokens；一个 patient history 15--20 dialogues、总约 50K tokens（§3.2）。分解可减少上下文混杂，却也可能削弱真实跨访次共同决策、未记录事件、矛盾与临床工作流的复杂性。
- 语料包含 80 个虚构 patients、个人信息/多次对话及 IDR/CDR/SR annotations。IDR 从单 encounter 抽取事实；CDR 跨多 dialogues 链接事件；SR 根据完整病史和当前症状做 multiple-choice 综合推断，干扰项按 disease/symptom similarity 选取（§3.3）。
- automatic quality proxy：Faithfulness 为 utterance 与提供 context 的 sentence-embedding cosine，Coherence 为相邻相似度变化，Diversity 为 BERTopic coverage/entropy。它们不等同临床事实核验：语义相似/平滑文本仍可能医学错误（§4、Table 1）。
- Correctness/Realism 与部分 Coherence 采用 G-Eval 5-point LLM judge；作者使用多 judge ensemble（Gemini 2.5、GPT-5 mini、Qwen3-235B、DeepSeek-R1），且提及 small human-annotated subset/sanity checks，但未报告大规模独立临床专家/患者对每条医疗建议的 gold adjudication（§4--5、Table 4--5）。
- 与长对话 datasets 比较：MediLongChat 平均 960.9 turns、18.2 sessions、50,217.3 tokens。Stage-2 automatic coherence 0.925、diversity 0.5447；这些仅是作者定义的指标且对非医疗 baselines 采用 relaxed medical-factuality policy，横向“临床正确性”不可等价比较（§5.1、Table 2--3）。
- benchmark 上，IDR/CDR free-form scores 很低（例如最佳 IDR F1 33.49、CDR F1 24.25），SR multiple choice 较高（GPT-4.1 mini 83.75%）。这说明合成长期文本的 retrieval/linking 难度，不证明模型已能安全诊断；MCQ 的受限格式也降低了生成方差（§5.2--5.4、Table 6）。
- 作者列出 synthetic data 对 rare diseases、complex comorbidities、behavioral health 的偏离，LLM judge 的 prompt/baseline 依赖与专家一致性不足，以及未覆盖 images/labs/structured EHR（§6）。

## 医疗安全与复现边界

- 该数据只适合研究/benchmark。任何医疗对话 agent 都应明确非诊疗替代、在高风险症状提供升级/急诊路径、避免自主处方/诊断结论，并由合格临床人员按本地法规、工作流和适用人群独立验证。
- synthetic timeline 可能呈现不现实的 disease prevalence、依从性、访视频率、诊断/治疗路径或因果关系；不能拿合成“correctness”分数代替真实 EHR 外部验证、prospective study、临床专家审查、错误率和患者安全结局。
- 长期 memory 可能泄露或错误绑定敏感病史。真实系统应实现最小必要访问、明确 consent、来源/时间戳、冲突 detection、patient correction、过期信息控制、权限分层和 audit；不要因模型回忆某段文字就视为临床事实。
- LLM judge 会有模型、prompt、verbosity/position bias 与 medical knowledge gaps；评测应增加 blinded multi-specialty clinician adjudication、inter-rater agreement、实测 hallucination/omission/unsafe-advice rates、subgroup fairness、rare/ambiguous cases 与 adversarial history conflicts。
- 复现应固定 data/code revision、metadata sources/human review protocol、generation model/prompts/temperature、persona/disease sampling、event stitching、task construction、context limits、embedding/BERTopic/G-Eval prompts 和所有 judge versions；报告每位 patient/session、split、seed、成本、人工临床复核范围与许可/数据治理。

## 与 AAMAS 的关系与核验说明

这是 healthcare-agent long-term memory 的合成数据与评测工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EFXQ8322.pdf) 核对三阶段生成、80 patient 数据规模、三项任务、指标/多 judge、Table 2--7 与作者限制；没有将合成基准表现、LLM judge 分数或历史推断示例误写成真实诊断能力、医疗安全性、临床有效性或患者获益。
