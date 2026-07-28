---
title: "Algorithmic Collusion at Test Time: A Meta-game Design and Evaluation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/SVWG7670"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SVWG7670.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["algorithmic_collusion_risk", "simulated_pricing_game", "empirical_metagame_scope", "not_legal_or_market_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Algorithmic Collusion at Test Time: A Meta-game Design and Evaluation

## 一句话总结

本文以重复价格竞争的经验元博弈评估测试时算法合谋：把预训练 policy 类型、初始化与在线 adaptation rule 组成 meta-strategy，模拟配对 payoff 并求经验 best response/NE；部分对称 Q-learning/UCB/LLM 设置出现高 Collusion Index equilibrium，但不对称成本下难以维持，结果不是对真实市场合谋或违法的判定。

## 方法与证据

- 用 Collusion Index（CoI）衡量从竞争 stage-game payoff 到垄断 payoff 的价格/收益位置；0% 表示充分竞争、100% 表示完全 collusion（§2）。
- meta-strategy 将 pre-trained initial policy category 与 test-time update/adaptation 结合；通过 repeated pricing simulation 得到 profile payoffs，以 empirical game-theoretic analysis 构造 normal-form meta-game、best-response graph、NE-regret 与 pure/mixed NE（§3）。
- 评估 Q-learning、UCB 和 LLM pricing strategies。Q-learning results 表明在 symmetric-cost meta-games 部分合作型策略可成为理性稳定选择；短 horizon 时 collusion 减弱，asymmetric costs（文中 c1=1,c2=0.8）下不再持续（§4.2）。
- 文章还比较不同 Q-value rescaling/initial beliefs。结论是 pessimistic beliefs 更易产生低-collusion equilibrium，乐观/合作预训练历史与 paired cooperativeness 关联更强的 collusion/re-establishment（§3--4）。
- LLM 部分使用 GPT-5-mini/nano 组合策略及 prompt/history variation；作者也说明因 model deprecations 无法复现某先前结果，改用较新模型，因此结果受 model version 与 prompting 影响（§4.3、§5）。

## 安全边界与复现

- 这是有限 horizon、离散 action、给定 cost/quality/initialization 的 simulated repeated pricing game；CoI/NE 只针对所采样的 meta-strategy space，不能证明真实企业、平台或通用 pricing software 存在串谋。
- 市场合谋的法律/监管判断需要真实 pricing data、因果证据、竞争结构、通信/意图、消费者损害及司法管辖分析；本方法可辅助风险研究，不能取代执法调查或合规审计。
- 经验元博弈会遗漏未采样策略，LLM results 尤其依模型版本、system prompt、history、temperature、tool/data access；“rational”是在建模的 payoff 下，不是对部署主体目的的推断。
- 复现应发布 base-game parameters、horizon、pretraining seeds/hyperparameters、strategy taxonomy、adaptation rules、sampling budget、payoff matrices、NE solver/selection、CoI definition 和 all model prompts/versions；实际部署应加 price guardrails、monitoring、independent compliance review 与 human escalation。

## 与 AAMAS 的关系与核验说明

这是多智能体市场、学习策略与 algorithmic collusion 风险评估工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SVWG7670.pdf) 核对 CoI、meta-game/EGTA、对称/非对称结论与 LLM 复现限制；没有将 simulation equilibrium 表述为现实市场中已发生或法律上成立的合谋。
