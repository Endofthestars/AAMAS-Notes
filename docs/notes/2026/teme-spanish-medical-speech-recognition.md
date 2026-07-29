---
title: "TEME: A Multi-Agent Evaluation Framework for Spanish Medical Speech Recognition"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/RHNT7438"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RHNT7438.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02c"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["medical_safety", "llm_judge_reliability", "limited_dataset", "not_clinical_deployment_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# TEME: A Multi-Agent Evaluation Framework for Spanish Medical Speech Recognition

## 一句话总结

TEME 是面向西班牙语医疗语音识别输出的 GPT-4o 多代理评测层：药物、剂量与临床一致性代理分别分级，再由规则化共识层汇总，以暴露 WER/CER 等通用指标可能掩盖的严重临床语义错误。

## 方法与证据

- 两层架构的第一层由 medication、dosage、consistency 三个专门代理评估转写；它们将结果标为 NONE、MINOR 或 MAJOR。第二层 consensus agent 检查代理是否越界，并采用“任一专家发现 MAJOR 即最终为 MAJOR”的确定性规则（§2）。
- 评测对象为 90 段、约 67,000 词、涵盖 10 个专科的西班牙语医疗对话：23 段真实匿名咨询，67 段为经医生验证的现实感合成对话；音频由 Gemini TTS 生成并以 8-bit/8kHz 降质，再分别交给两套 ASR（§2--3）。
- 论文并列 WER、CER、MC-WER、Spanish ClinicalBERTScore、SeMaScore 与 TEME。Table 1 中 Whisper 的 WER 为 3.3%（低于 Omniloy-medical-voice 的 4.7%），但 TEME 总计 21 个 MAJOR errors（后者为 12），呈现词级误差率与临床严重性可能不一致。
- 文中以药名替换、剂量从 “35 mg midday” 变为 “80 mg morning”、以及否定反转为例，说明 TEME 如何判为 MAJOR；这是在其参考转写、提示/规则与代理判断下的评测结果（§2--3）。

## 适用边界与复现

- TEME 是评测辅助工具，而非诊断、处方、临床决策或自动放行系统；MAJOR/MINOR 标签及其共识规则不能替代合格医疗专业人员的审阅、患者安全流程与责任机制。
- 关键判定使用 GPT-4o，论文未报告跨模型/提示稳定性、与多位独立临床评审者的盲评一致性、误报漏报置信区间或对抗性测试；因此“clinically sound”主张应限于该小规模实验，不能视为安全保证。
- 数据集混合真实匿名与经医生验证的合成对话，且使用 TTS 和刻意降质音频；其语言、医院工作流、口音、录音链路及病例谱系代表性均有限，不能推出在真实临床连续部署中的性能。
- 复现应披露合规的数据访问/去标识方案、参考转写与专业标签、每个代理的模型版本/提示/温度、规则与冲突处理、ASR 配置、音频生成/降质参数、分层数据切分，以及由独立临床评审报告的错误类型、敏感性、特异性和不确定性。

## 与 AAMAS 的关系与核验说明

该工作将专长分工与规则共识用于安全关键 ASR 评测。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RHNT7438.pdf) 核对 §2--3、Table 1 和结论；所有安全性描述均限定为离线评测，未将其写成临床部署认可。
