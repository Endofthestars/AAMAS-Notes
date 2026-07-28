---
title: "EmoDebt: Bayesian-Optimized Emotional Intelligence for Strategic Agent-to-Agent Debt Recovery"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/OCSI2038"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OCSI2038.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_financial_scenarios_only", "emotion_manipulation_and_fairness_risk", "black_box_policy", "llm_judge_and_prompt_dependence", "not_for_real_debt_collection"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# EmoDebt: Bayesian-Optimized Emotional Intelligence for Strategic Agent-to-Agent Debt Recovery

## 一句话总结

EmoDebt 将 creditor LLM 的七类情绪转移矩阵作为 49 维黑箱策略，以 GP Bayesian optimization 根据模拟协商结果调参；在 GPT-5 生成的 100 个债务案例和 LLM 对手中取得高模拟成功率，但它不是现实债务催收的合规、有效或可部署方案。

## 方法与证据

- CRAD 含 100 个由 GPT-5 生成的 synthetic credit-delinquency scenarios；LangGraph 让 creditor/debtor LLM 对话，独立 examiner 判 accepted、breakdown 或 30 turns timeout（§4.1--4.2）。
- creditor 状态在 happy/surprising/angry/sad/disgust/fear/neutral 间转移；以心理学先验初始化 `7×7` 矩阵，用 Dirichlet perturbation 候选、Matérn GP 与 Expected Improvement 优化。每轮评估 20 个策略，最多 10 iterations（§3--4）。
- 对 GPT-4o-mini/GPT-5-mini creditor-debtor 配对、7 种 debtor emotion strategy，指标为 agreement success、对 creditor 有利的 timeline ratio 和 dialogue turns；报告 EmoDebt 最佳 99.7% success、平均 success 增幅 46.2%，并给出 static-prior/random ablation（§4--5）。

## 局限与治理边界

- 数据、债务人、还款条件和“情绪”均为合成/LLM 模拟，且 examiner 也是 agent；不能证明对真实个人、真实违约、文化差异或法律程序的效果、公平性或伤害风险。
- 目标优化 creditor 成功与效率，容易和借款人的脆弱性、公平待遇、知情同意、反操纵和法规义务冲突。任何现实催收必须有人类监督、适用法律审查、申诉与审计；本笔记不构成部署建议。
- 作者承认 learned matrix 为难以解释的 black box，且 static policy 不适应行为变化或长期关系；LLM 版本、prompt、judge、reward 和停止规则都会改变结果（§6）。
- 复现应发布合成生成模板、所有 prompts、模型版本、候选/seed、审判标准及逐案例结果，并补充 harm、bias、calibration 与对人类/受保护群体的独立评估。

## 与 AAMAS 的关系与核验说明

该文研究对抗性 LLM agent 协商与情绪策略优化。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OCSI2038.pdf) 核对数据合成来源、优化过程、实验协议、指标及作者列出的解释性/伦理部署限制；没有将模拟指标外推为金融或债务催收结论。
