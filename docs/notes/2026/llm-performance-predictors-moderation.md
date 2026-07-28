---
title: "LLM Performance Predictors: Learning When to Escalate in Hybrid Human-AI Moderation Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "safety_verification", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/KWGX1235"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KWGX1235.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["offline_moderation_evaluation", "cost_model_assumption", "human_review_quality_assumption", "taxonomy_and_label_scope", "distribution_shift", "selective_escalation_not_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# LLM Performance Predictors: Learning When to Escalate in Hybrid Human-AI Moderation Systems

## 一句话总结

本文训练 LLM Performance Predictor（LPP）来预测某次 moderation output 是否会错，并按预测风险把 case 自动通过或升级给人审。LPP 融合 token log-probability/entropy、verbalized confidence 和“证据不足/政策定义不足”等 attribution indicator；在 OpenAI text moderation 与一套 multilingual/multimodal moderation dataset 的离线试验中，常比单一 uncertainty signal 有更低的作者定义 expected cost。它是有标签、固定 taxonomy 和成本参数下的 selective-classification 方法，不证明真实审核系统安全、公平、合规或人审准确无误。

## 方法与证据

- pipeline 是 base LLM structured inference → 0/1/2/3 integer-token schema（no/yes/evidence-inconclusive/definition-inconclusive）→ feature extraction → Ridge meta-model 预测 correctness → threshold trust/escalate（§3）。输出 schema 的 retries、prompt 和 tokenization 会影响 feature；paper 的结论不自动适用于不给 logprob 的模型、自由生成 policy judgement 或不同 taxonomy。
- features 覆盖 post-hoc outcome-token entropy/MSP/top-2 margin、可选 reasoning-sequence statistics、verbalized confidence、及 evidence-deficit/policy-gap attribution（Table 1）。作者报告 CoT 会提高 confidence 而不改善 calibration，因此正式结果使用 direct-answer prompting（§3, §5）；attribution 是 routing aid，而非已验证的错误根因或人类法律解释。
- LPP 的 supervised target 是 LLM prediction 是否与 ground-truth moderation decision 一致；Ridge 在训练数据上拟合，配置使用 downsampling、nested CV 和 held-out test（§3–4）。这需要持续的可靠标注，并可能随规则、文化、语言、对抗行为和模型更新产生 distribution shift。
- datasets 为 OpenAI Moderation Dataset（1,680 English texts、多个类别）及 Multimodal Moderation Dataset（1,500 short videos、多语言/模态，含 text/thumbnail/transcript/video-frame）（§4.2）。这不是真实生产流量、用户申诉、长期 harm、跨平台政策差异或全部 content category 的测量。
- escalation cost 比较由 review time×hourly rate 与每次误判的 projected business loss 构成；作者用 \(c_{rev}/c_{mis}\approx0.64\) 选 threshold，并在 0.4–0.9 做 sensitivity（§3.3）。成本、severity、reviewer quality/queue delay、错误不对称性和平台风险容忍度是外部治理选择，不能由模型优化替代。
- 在 text-only dataset，例示 gpt-4o-mini 的 expected cost 从最佳 baseline $132 降到 LPP $38（71%），且 escalations 331→148；另有多个模型下降，但 multimodal 结果更 model-dependent，Qwen/Llama 有时持平/被其他方法匹配（§5.2, §5.4）。绝对美元来自作者的成本假设，且各模型/数据分布不保证同等收益。
- 作者承认需 ground-truth labels，generalization to RAG/neuro-symbolic architectures 未知，成本随 severity/reviewer/platform 而变，未来需 dynamic resource allocation 与 federated models（§5.5）。

## 适用边界与复现

- 适用于辅助安排审核队列：在明确 policy、可审计 human labels、可校准 cost/risk 和人可 override 的条件下，优先把预测易错或证据/政策缺口 case 送审。
- 不应以 LPP 分数自动删除内容、处罚用户或声称“安全自动化”。高严重度类别需独立升级规则、抽检、申诉和审计；人审也需要质量控制、一致性监测、心理健康保护与公平工作负荷设计。
- 复现应固定 prompts/integer schema/retry、base model version、top-k logprobs、feature set、train/test split、class balancing、cost ratio和 threshold；报告 calibration、minority-error F1、expected cost、escalation rate、false trust 与 unnecessary review 的类别/语言/模态分层。
- 部署前还需 temporal/external validation、policy drift/retraining protocol、adversarial prompt/content 测试、human-AI disagreement/appeal analysis、severity-weighted harm与 review latency/capacity simulation；只有在这些治理条件下，selective escalation 才可成为风险控制的一部分。

## 与 AAMAS 的关系与核验说明

这是 AAMAS uncertainty-aware human–AI moderation 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KWGX1235.pdf) 核验了 LPP/Ridge routing、feature families、两个数据集、成本比、代表性 cost results、CoT exclusion及 limitations；没有把离线 cost reduction 写成生产审核质量、法律合规或无害自动化保证。
