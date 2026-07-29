---
title: "Mind-Inference for Multi-Turn Emotional Support: Distinguishing Personal and Factual with Adaptive Memory"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "generative_agents", "safety_verification"]
dblp_key: ""
doi: "10.65109/CIMN4023"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CIMN4023.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "emotional_support_not_clinical_care", "offline_text_metrics_only", "psychological_inference_risk", "memory_privacy_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Mind-Inference for Multi-Turn Emotional Support: Distinguishing Personal and Factual with Adaptive Memory

## 一句话总结

MIA 是多轮 Emotional Support Conversation 框架：EToM 将用户状态拆为会变化的 Personal（emotion、belief、intention、desire）和较稳定的 Factual（fact、cause、result），PFD 逐轮调整两类信息权重，ORM 更新记忆时删除过时的心理推断而保留事实语境。它在 ESConv、CPsyCounD 上取得更低 PPL 与更高 BLEU/ROUGE，但这些离线文本指标与数据集比较不能证明更好地理解个人心理、减少伤害、识别危机或提供治疗/咨询。

## 方法与证据

- 论文关注 ESC 在多轮中随用户 affect/intention 演化而产生的 stale-memory 问题（§1）。它把单一 latent summary 的混合表示视为缺少可控/可解释 state interface；但 Personal/Factual 的分类本身是系统推断，不是用户确认的事实，且不包含临床诊断、风险分层、同意、隐私保留或对错误记忆的外部校正。
- EToM 的 hierarchy 明确将 emotion/belief/intention/desire 放入 Personal，fact/cause/result 放入 Factual（§2）。这种细粒度分离可供 inspection/weighting，但论文未报告标注定义、inter-annotator agreement、inference accuracy、错误类型、跨文化/语言稳定性，不能认为模型真的读懂“mind”。
- PFD 在 affectively intense turn 增强 Personal grounding、在 clarification/action-planning turn 增强 Factual grounding（§2）；这是 turn-level adaptive fusion，extended abstract 未给 architecture、training objective、threshold、factor weights、calibration 或用户控制。因此其“情感贴合/具体性”是设计动机，非独立的心理测量验证。
- ORM 对 memory history 进行 obsolete judgement，删去过时 Personal states 而保留稳定 Factual context（§2、图 1）。它可减小过期假设向后传播，却有两面风险：错误删除重要的长程脆弱性/偏好，或把错误推断长期保留为“事实”。论文未提供 deletion precision/recall、memory length/成本、数据 retention/encryption、用户查看/更正/删除权或攻击性 conversation 测试。
- 在 ESConv 与 CPsyCounD 比较 PAL、SUPPORTER 等 baselines，MIA 报 ESConv PPL 7.39、BLEU-4 22.25、ROUGE-L 22.44，CPsyCounD PPL 3.87、BLEU-4 25.99、ROUGE-L 42.22；去掉 PFD 后 ESConv BLEU-4 20.13，去掉 ORM 19.72（§3）。这些 overlap/perplexity 指标可支持 dataset response similarity，不衡量同理心、事实性、危机处理、有害建议、用户感受、长期结果或统计显著性；未给 human evaluation、seeds/CI、model/data release、safety protocol。

## 适用边界与复现

- 适合作为受控研究中的多轮支持性对话记忆与状态表示方案，或低风险的同伴式非临床交谈辅助；不应宣称是心理咨询、诊断、危机干预、治疗替代或可独立处理自伤/家暴/急性症状。
- 复现需获取 ESConv/CPsyCounD split/preprocessing/多轮切分、EToM labels/prompt/encoder、PFD architecture与weights、ORM similarity/obsolete threshold、memory update order/generator、training hyperparameters/seeds、baseline implementations 与 PPL/BLEU/ROUGE scripts。除复现表中指标外，应人工审查 Personal/Factual 分离和 deletion decisions，并逐 turn 存档可审计状态。
- 应评估长会话、用户纠正、矛盾或不完整事实、跨文化/方言/少数群体、隐私泄露/prompt injection、情绪突变、错误高置信推断、不同 memory lengths、crisis/self-harm/abuse cues以及 adversarial safety probes。需报告人类同理心/有用性评分、事实错配、过度依赖、harm rate、危机转介 recall/precision与隐私影响，而非只看 n-gram overlap。
- 若面向用户，提供明确非医疗定位、最小化/可删除 memory、用户可见和纠正状态、敏感信息禁止持久化、危机检测与地区化紧急资源、人工支持转接、审计与拒绝危险建议。模型对用户意图/信念的“mind inference”必须低置信呈现，不能作为画像、资格或干预决定的依据。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多轮情感支持与 memory-aware dialogue extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CIMN4023.pdf) 核验 EToM/PFD/ORM、两数据集、报告的 PPL/BLEU/ROUGE 数值与两项消融；没有将离线语言指标写成心理状态准确性、临床安全、危机能力或真实用户福祉证据。
