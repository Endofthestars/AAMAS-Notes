---
title: "Coalition Tactics: Bribery and Control in Parliamentary Elections"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/GUXI9713"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GUXI9713.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "election_manipulation_domain", "formal_complexity_results", "not_operational_guidance", "model_scope_limited"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Coalition Tactics: Bribery and Control in Parliamentary Elections

## 一句话总结

本文把比例代表制中的操纵目标从单一政党改为联盟：要求联盟获得足够的 active-vote fraction（J），并可同时要求联盟内某偏好党占足够比例（J+F）。对形式化的 bribery/control 决策问题，作者给出若干多项式时间、NP-hard、W[1]-hard/W[2]-hard 结果；这描述计算复杂度边界，并不提供或验证现实选举操纵策略。

## 方法与证据

- 选举为 \(E=(P,V,\succ)\)：每位选民将一票投给其最偏好、正在参选的党。阈值 \(\tau\) 以上的党是 active parties，目标以 active votes 的份额定义（§2）。该模型未表达选民信念变化、竞选传播、法律、投票制度细节、席位转换、执政谈判或真实联盟形成。
- J 目标要求联盟 \(C\) 的 \(\mathrm{frac}^{\tau}(C)\ge\varphi\)；J+F 还要求联盟内偏好党 \(p_1\) 的份额至少为联盟份额的 \(\rho\) 倍（Definitions 1–2）。J 是令 \(\rho=0\) 的特例；这些是票份额目标，不是“组阁成功”“政策实现”或社会福利。
- bribery 允许改变选民偏好，control 允许增加/删除选民或政党。Table 1 报告：1 与 $ 成本 bribery 为 P；Swap/Coalition Shift 在无阈值时为 P、有阈值时 NP-hard；增加/删除选民的 control 为 P。结论对应列出的 J/J+F 和 cost/threshold 条件，不能泛化为所有投票规则或成本模型。
- 对 party control，删除候选党（DCP）或增加候选党（ACP/AOP 等）在部分无阈值/J 设置中 immune；其余报告 W[1]-hard 或 W[2]-hard（以可增删党数为参数），Table 1 和 §1 说明这些是 parameterized-complexity hardness。hardness 不等于实际实例一定难、也不等于安全或不可操纵。
- 摘要没有给真实选举数据、用户实验、实现运行时、实例规模、启发式算法或社会后果评估；Future Work 明确提出 party split/merge、阈值修改、多个操纵者及更丰富 coalition dynamics（§3）。论文亦提供 extended-version 链接，但本笔记没有用其补充或替代 AAMAS 原文结论。

## 适用边界与复现

- 适合 computational social choice 中比较模型、证明归约、参数化复杂度与防御性制度设计讨论；不应用于设计、执行、规避监管或优化现实选举中的 bribery/control。现实选举相关应用应遵守当地选举法、独立监督与研究伦理。
- 复现需精确实现 voters 的 strict rankings、参选党集合、阈值及 active-vote normalization、J/J+F 目标、所有 cost/budget 编码和增删操作；逐一复核表中定理、归约和参数定义。三页摘要未包含完整证明，必须查读作者给出的完整版本后才可声称重现 hardness/P 算法。
- 应把此抽象与实际制度分开验证：不同席位分配规则、战略投票/弃权、信息不完全、异质成本、合法性约束、多操纵者博弈、组阁与政策结果。报告实例分布、时间/内存、exact/heuristic 成功率以及阈值附近的敏感性，而不把最坏情形复杂度直接转换为经验风险。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 computational social choice/strategic manipulation 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GUXI9713.pdf) 核验 J/J+F 定义、阈值 active votes、bribery/control 分类及 Table 1 的 P、NP-hard、W-hard 概览；没有将形式结果表述为现实政治操作、可行性评估或选举结果预测。
