---
title: "DELL: Dual-Knowledge Enhanced LLMs for Precise Decision Making in Healthcare"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "safety_verification"]
dblp_key: ""
doi: "10.65109/LVFL1061"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LVFL1061.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["clinical_decision_support_only", "retrospective_observational_labels", "no_patient_outcome_validation", "dose_safety_not_established", "single_site_dataset_scope", "llm_hallucination_and_prompt_risk", "human_oversight_required"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DELL: Dual-Knowledge Enhanced LLMs for Precise Decision Making in Healthcare

## 一句话总结

DELL 把从临床数据训练的可解释模型所提取的定量规则，连同 LLM 的常识推理，放入 prompt 以预测 sepsis ICU 病例未来 4 小时的 intravenous-fluid（IV）和 vasopressor（VP）给药量。论文在 MIMIC-III 的回顾性“实际给药”标签上报告比 Standard/CoT/few-shot/RAG 更低的预测误差和更高的剂量分箱准确率；这证明的是对历史处置的离线拟合表现，不能证明推荐剂量安全、有效、因果最优或可以用于临床处方。

## 方法与证据

- 任务输入是病人多维离散时间序列，时间步为 4 小时；标签为该窗口内实际 administered IV 总量与 VP 最大剂量。两者按 quantile 各分为 5 个范围，合成 25 个 joint treatment classes（§4.1.1）。因此 ground truth 是既往临床行为，而非由随机试验、反事实策略评估或患者结局定义的最优治疗。
- External Knowledge Distillation 为 25-class、IV/VP 5-class、IV/VP continuous targets 训练 decision tree、regression tree 与 LORE；把 case-specific rule/evidence 翻成自然语言。Internal Knowledge Utilization 通过 task prompt 调用 LLM knowledge；最后由 designed prompt 对外部建议与内部知识的 fully/minor/serious contradiction 作整合（§3, Fig. 3）。这是一套 prompt-and-model pipeline，不是经过药物剂量控制、临床工作流或前瞻性试验验证的闭环治疗系统。
- 数据来自 MIMIC-III：Boston teaching hospital 六个 ICU 的开放数据库（§4.1.1）。论文引用附录说明 extraction、split 与 test selection；主文不足以证明跨医院、不同时间、不同人群、儿科、不同监测设备或不同诊疗规范的外部有效性。
- 五个指标为 \(RMSE_{IV}\)、\(RMSE_{VP}\)、\(ACC_{IV}\)、\(ACC_{VP}\)、\(ACC_{TOTAL}\)：前两者衡量预测与实际剂量的差，后三者衡量落入预设剂量 bin/25-class 的正确性（§4.1.2）。这些不直接衡量死亡率、器官损伤、低血压控制、液体过负荷、不良事件、校准、uncertainty、subgroup harm 或临床可接受性。
- 论文以 DeepSeek-R1 671B/32B/7B，比较 Standard、CoT、few-shot、RAG-G（ICU guideline retrieval）、RAG-Q、CoTD 与多源外部知识 voting（§4.1.3–4.1.4）。每个 setting 重复三次并报告均值/标准差（Table 1–2）；随机性、prompt/template、模型服务版本和实现细节仍会影响复现。
- 作者报告 R1-671B 下 DELL 的 \(RMSE_{IV}=626.70\)、\(RMSE_{VP}=0.49\)、joint accuracy 26%；相对最佳“不含 quantitative knowledge”的 baseline，IV/VP RMSE 分别降低 17.99%/70.83%，joint accuracy 相对 RAG-G 的 11% 超过两倍（§4.2.1）。这些是作者在所述 retrospective test procedure 中的结果，26% joint-bin accuracy 也不应被叙述为临床可靠率或处方成功率。
- 外部知识较少（1–3 sources）时，DELL 并非稳定优于 voting：它虽有较低 \(RMSE_{IV}\)，但其余指标可能更差；至少四个 quantitative sources 后才显示一致优势（§4.2.3, Fig. 4）。这表明效果依赖来源数量、互补性及其噪声/冲突结构，不宜泛化为“LLM 总能融合医疗证据”。
- 作者将系统描述为透明 decision-support，称 clinicians 可监督和 override recommendation（§5）。这属于设计意图而非实际 usability、alert burden、automation bias、override 行为、责任分配或临床安全实证；这些仍需独立评估。

## 适用边界与复现

- 适用于研究性、离线的“从已记录处置中学习定量提示”实验，或供临床专家审阅的假设生成工具。任何输出均应被视为未经验证建议，而非剂量医嘱、诊断或治疗方案。
- 若在医疗环境探索，必须在受监管框架下进行：独立临床专家审阅、明确禁忌症与剂量上下限、病人特异性单位/肾肝功能/体重/共病检查、来源追溯、uncertainty 与失败提示、记录和 audit、前瞻性安全监测，以及适用的伦理、隐私、软件医疗器械和机构审批。不得用 MIMIC 上的误差或 accuracy 代替结局和安全证据。
- 复现应固定 MIMIC cohort/extraction、4-hour aggregation、quantile bins、patient-level split、feature availability time point、外部 model training 与 rule translation；对所有 prompt、LLM version/temperature、knowledge selection 和解析失败做版本控制。还应报告置信区间、患者级而非仅记录级统计、missingness、temporal/external validation、人口亚组与错误案例。
- 进一步研究需用离线 policy evaluation/causal methods、独立多中心与时间外验证、prospective human-factors study、实际 clinical outcomes、toxicity/contraindication checks、calibration/abstention、对 prompt injection/幻觉/冲突指南的压力测试。观察性医生剂量可能含未测混杂，故“更接近记录”不蕴含“更好治疗”——这是由其标签设计作出的方法学推断。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 将 LLM agent 与可解释外部模型结合的精确数值决策研究。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LVFL1061.pdf) 核验了 DELL 三模块、MIMIC-III/4-hour/25-class 任务构造、RMSE/ACC 指标、baseline、Table 1–2 与知识源敏感性；对“无临床结局或安全验证”的说明来自其预测实际给药标签和报告指标的范围，并没有把离线剂量拟合写成临床有效性或部署授权。
