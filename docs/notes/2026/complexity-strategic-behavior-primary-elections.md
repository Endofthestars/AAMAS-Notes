---
title: "The Complexity of Strategic Behavior in Primary Elections"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/RXOJ5992"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RXOJ5992.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["worst_case_complexity", "fptp_fixed_tie_breaking", "succinct_ge_representation_dependency", "perfect_information_assumption", "static_preferences_assumption", "not_empirical_political_prediction"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# The Complexity of Strategic Behavior in Primary Elections

## 一句话总结

论文在 FPTP、固定 tie-breaking 的多阶段 primary→general-election 模型中研究 voter strategic reasoning。其 worst-case 结论是：当 party 数作为输入且 GE contingent behaviours 以简洁规则表示时，best-response 阈值问题 NP-complete，给定 profile 的纯 NE 验证 coNP-complete，纯 NE 存在 Σ₂^P-complete；若后期选民可观察并条件化于先前 primary outcome，unbounded stages 下 dominance/SPNE existence 为 PSPACE-complete。它是表示敏感的复杂度分类，不是现实选举操纵发生率或结果预测。

## 方法与证据

- 模型有 \(p\) 个 party、各自 disjoint politicians；每 party 选一个 nominee 后进入 general election。primary 与 GE 都采用 FPTP 和预先固定 tie-breaking（§3.1）。这排除了 ranked-choice/runoff、比例制、delegate rules、endorsement、campaign spending、eligibility disputes、strategic candidates与真实选务规则。
- voter strategy 包含每 party 的 primary ballot（或 abstain）与 GE decision function \(g_i:C\to A\cup\{0\}\)，其中 \(C=A_1\times\cdots\times A_p\) 是全部 finalist profiles；utility 是最终 winner 的 cardinal utility 减 primary/GE participation costs（§3.1–3.2）。该 reduced form 不等于完整 extensive-form plan，作者明确说明完全策略会需要 \(\Theta(m^{pn})\) 空间。
- closed primary 以预先 affiliation 限制可投 party；open primary 允许每 stage 决定是否投票；single-primary 或 multiple-primary participation 分别限制一场或多场参选。正文以 multiple participation 为一般模型，行政细节如 deadline/membership rolls 被抽象掉（§3.1）。现实 crossover、注册成本、信息不对称与执法无法由这些抽象自动覆盖。
- 表示方式决定复杂度含义：显式存 \(g_i\) 表需要 \(\Theta(m^p)\) entries，input 本身已随 party 数指数增长；在 constant-time oracle/简洁 list-form GE rules 时 input 可为 \(O(nm)\)，primary action组合的指数才成为真正计算瓶颈（§3.1, §4.1）。因此不能脱离 representation 宣称“primary best response 总是 NP-hard”。
- Proposition 1 给 best-response enumeration 为 \(O(np+(m+1)^p(mp+n\tau))\)；固定 \(p\)、constant-time GE queries 时对 \(n,m\) 多项式。single-primary participation 时 action space 降至 \(O(m)\)，fixed GE behaviour 也不增加其核心负担（§4.1）。
- Theorem 2：在 party 数为 input、GE behaviours succinct、fixed tie-break且 zero participation cost 时，`BR-≥U` NP-complete；hardness 从 3-SAT，把 variable-party nominee 选择编码 truth assignment、clause voter list rules编码 clauses（§4.1）。这是阈值决策问题的 worst case，不是所有选民实际需要解 SAT。
- Theorem 3：给定 strategy profile 的 pure NE verification 是 coNP-complete；Theorem 5：pure NE existence 是 Σ₂^P-complete，且可用 finalist-based/list GE behaviour、fixed tie-break构造（§4.2）。论文也给 matching-pennies 型例子说明 pure NE 可能不存在；复杂度结论不保证 mixed equilibrium、动态收敛或实务均衡选择如何发生。
- sequential model 允许第 \(k\) stage voter 按 earlier nominee history 条件化，假定 perfect information、static preferences。Theorem 6 将 sequential dominance `SeqDS-≥U` 在 unbounded \(p\) 定为 PSPACE-complete；fixed \(p\) 落在随 stage alternation 的 polynomial hierarchy level（§5）。Theorem 7 对 pure SPNE existence 同样给 fixed stages 的相应层级、unbounded stages PSPACE-complete（§5）。
- 作者明确的后续方向包括 restricted open/closed regimes 的 tractable subclasses、partial/noisy information、belief updates/adaptive learning、candidate positioning，以及 agent-based simulation/bounded rationality（§6）。无真实 election dataset、民调实验、历史因果估计或对特定国家/候选人的预测。

## 适用边界与复现

- 适合作为多阶段集体决策的复杂度/机制设计理论基线。使用时必须声明 voting rule、tie-break、open/closed/participation regime、GE rule encoding与 party number 是否固定；这些改变都可能改变问题规模或可解性。
- 不应把 NP/Σ₂^P/PSPACE 完备理解为选民必然无法作出策略选择、primaries 必然可被操纵，或某真实选举存在均衡。复杂度是最坏情形的精确计算难度；启发式、有限候选集、固定 party 数、偏好结构或机构限制可能可行。
- 真实制度分析需另行加入 voter turnout/registration/frictions、incomplete/noisy information、polls/media、delegates、campaign/candidate strategy、coalitions与随机/非 FPTP 规则，并用审计/仿真研究均衡选择与 distributional impacts；不要将 oracle GE rules当作实际选民可以任意实现的 contingent action。
- 复现应实现 FPTP/fixed tie-break、utility/cost与 open/closed rules、explicit vs succinct/list-form \(g_i\)，再复核 3-SAT、UNSAT、2-QBF/QBF reductions 对 BR/NE-VERIFY/NE-EXIST/SeqDS/SPNE 的对应。应分别测试 fixed \(p\)、unbounded \(p\)、single vs multiple participation及 ex-ante vs history-conditioned strategies。

## 与 AAMAS 的关系与核验说明

这是 computational social choice 与 algorithmic game theory 的初选策略复杂度工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RXOJ5992.pdf) 核对 FPTP模型、strategy/representation与成本、best-response运行时和NP结论、NE验证/存在结果、sequential/SPNE的量词深度与作者限制；没有把抽象 worst-case complexity 误写为现实政治预测、操纵事实或制度优劣结论。
