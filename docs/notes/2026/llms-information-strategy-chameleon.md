---
title: "Do LLMs Strategically Reveal, Conceal, and Infer Information? A Theoretical and Empirical Analysis in The Chameleon Game"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "generative_agents", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/AHJH3784"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AHJH3784.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03h"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "prompt-sensitive-gameplay", "strategic-information-leakage", "small-game-evaluation", "model-version-dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Do LLMs Strategically Reveal, Conceal, and Infer Information?

## 一句话总结

在 N-player Chameleon 中，non-chameleons 必须既找出 chameleon 又不泄露 secret。论文给 pairwise concealing/revealing stationary strategies 的上界；四人、16 words、100 局实验中，LLMs 虽常识别 chameleon，却让其 second-chance 猜中 secret，non-chameleon win 仅 0--6%，低于同回复策略的 23%。这是特定游戏和提示下的信息泄露诊断，不代表模型在所有安全、谈判或隐私任务的能力。

## 方法与证据

- concealing 用各 secret response distributions 的 KL 距离上界，revealing 用 L1 距离下界；Propositions 1--2 分别给非 chameleon 胜率上界（§2）。
- 实验固定 GPT-5 为 chameleon，三个 non-chameleons 使用同一模型；GPT-5 non-chameleon identification=.64、win=0、second chance=1（Table 1）。
- 模型/版本、提示词、category、随机性与 cooperative pre-agreement 影响结果；理论仅对给定 stationary strategy class，非通用 LLM 安全结论。

## 适用边界与复现

- 复现须版本化模型、system prompt、turn history、categories/words、sampling及 votes，报告 identification 与泄露/second-chance 两个维度；部署机密场景应有最小披露、访问控制和独立 red-team，而非依赖聊天策略。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AHJH3784.pdf) 人工核对 definitions、bounds 与 Table 1；未把游戏结果泛化为普遍战略能力。
