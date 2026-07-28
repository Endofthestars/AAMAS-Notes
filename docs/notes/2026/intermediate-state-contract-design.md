---
title: "The Power of Information for Intermediate States in Contract Design"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/EYFD4743"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EYFD4743.pdf"
preprint_url: "https://arxiv.org/abs/2604.15636"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["mechanism_assumption_scope", "constructive_separation", "information_observability"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# The Power of Information for Intermediate States in Contract Design

## 一句话总结

论文在委托过程加入可观测中间状态，比较只依最终 outcome 付款的标准合同、可在中间状态付款的 pay-halfway 合同，以及可见不利中间状态即终止的 terminate-halfway 合同。

## 方法与证据

- 模型是两阶段 principal-agent delegation：初始动作导致中间状态，后续动作产生最终 outcome。中间状态既可包含状态内最终行动的质量，也可揭示初始行动的信息（§2）。
- pay-halfway 以中间状态和最终 outcome 共同决定支付；terminate-halfway 则允许 principal 在特定中间状态停止过程。两者都包含标准 outcome-only 合同为特例（§2）。
- Theorem 4 给出构造：为激励同一 welfare-optimal action profile，标准合同与 pay-halfway 的支付比可趋于无穷大；这是支付/构造分离，并非所有实例都有无限收益（§4）。
- 对确定的一阶段过程，pay-halfway 可利用中间状态推断初始动作，文中给出相对标准合同的紧界讨论；若只有一个初始动作或中间状态无法提供该信息，其优势会消失（§4、Claims 2–3）。
- terminate-halfway 在构造的确定过程可相对最优标准合同达到 $\Omega(N_1N_2)$ 利润倍数；在构造的随机一阶段过程也有 $\Omega(SN_2)$ 分离（§5，Theorems 5.1–5.2）。
- §3 给出上界/断点分析，说明中间状态合同的改善也与状态、初始动作和最终动作数量有关，而不是无参数限制的优势。

## 局限与复现

- 结果假设中间状态可被 principal 准确、及时观察且允许据此支付或终止；若状态有噪声、被操纵、不可验证，机制可实施性与激励结论需要重新分析。
- 大倍率是存在性/紧反例结果，依赖指定的状态转移、奖励、成本和动作数量；不能读为每个委托问题都应使用或都会从中间合同获益。
- pay-halfway 的主信息渠道是辨识初始动作，因此在随机一阶段中这种信息丢失时不一定有效；terminate-halfway 的优势机制则是排除不利状态，两者不可互换。
- 模型以理性 agent、已知分布、可转移支付和及时终止为前提，不覆盖有限责任、动态 renegotiation、多 agent 相互作用、隐私或法律约束。
- 复现应枚举论文构造及随机/确定变体，分别计算 standard/pay/terminate 的 action profile、支付、welfare 和 principal profit，并随 $S,N_1,N_2$ 报告比率；不能只复用单一数值实例。

## 与 AAMAS 的关系与核验说明

工作研究在多阶段决策中利用过程信息进行机制设计。笔记使用作者公开的 [arXiv HTML 原文](https://arxiv.org/html/2604.15636v1) 作主文本，并将构造性分离、上界和可观测性假设分开记录。
