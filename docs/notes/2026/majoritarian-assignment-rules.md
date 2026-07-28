---
title: "Majoritarian Assignment Rules"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QERE1891.pdf"
preprint_url: "https://arxiv.org/abs/2602.14816"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["house_allocation_domain_scope", "strict_preference_assumption", "top_cycle_n_ge_5", "computer_aided_enumeration_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Majoritarian Assignment Rules

## 一句话总结

论文把多数制 social-choice 函数引入一对一 house allocation：在严格偏好、人数等于房屋数的分配域，majority graph 几乎决定 profile；Pareto-optimal assignment 都在 top cycle 且 semi-popular，并对 $n\ge5$ 完整刻画 top cycle 可能的五种大小。

## 方法与证据

- 模型是 $n$ 个 agent 与 $n$ 个房屋的一对一双射 assignment，每个 agent 对房屋给出 strict linear order；agent 仅比较自己获得的房屋。两个 assignment 的多数关系由偏好前者与后者的 agent 数比较形成，因此不是带基数效用、可分物品、容量或两边偏好的匹配模型（§2–3）。
- Theorem 1：两个 profiles 诱导同一个（无权）majority graph 当且仅当它们 rotation equivalent。证明还给出多项式时间重构所有兼容 profile 的过程；由此 Pareto-optimality、least unpopularity 和 mixed popularity 都是只依赖 majority graph 的 majoritarian rule（Theorem 1、Corollary 1）。这不表示 rank-maximality 也如此：论文给出同图但 rank-maximal assignments 不同的反例（§3–4）。
- 已知 serial dictatorship 恰好产生所有 Pareto-optimal assignments。论文进一步证明 $PO\subseteq SP$（Proposition 1，$SP$ 为 semi-popular），以及 $PO\subseteq TC$（Proposition 2，$TC$ 为 majority relation 的 transitive-closure maximal elements/top cycle）；故可通过 serial dictatorships 找到 top-cycle 中的元素，但不能据此枚举整个 top cycle（§2、§4.1）。
- Theorem 2 对 $n\ge5$ 给出完整大小与条件：$|TC(P)|\in\{1,2,n!-2,n!-1,n!\}$。所有 agent top choice 各异时为 1；除两名外 top choice 各异，且那两人共享同一第二选择、其不被他人 top-rank 时为 2；其余三种分别由 bottom-choice 的相应 distinct/shared 条件决定（Theorem 2）。这是 profile 的充要分类，不是“任意规模多数图”通用事实。
- Theorem 2 的 $n=5$ 部分使用按对称性枚举所有 profile 的 computer-aided verification，再扩展到 $n\ge6$；论文另明确 $n<5$ 有额外大小：$n=3$ 允许 $1,2,4,6$，$n=4$ 还可能出现 $n!-3$（Remark 3）。因此不能把五种大小不加条件套到小实例。
- 对 Bordes、Gillies、McKelvey 三种 covering relation，三种 uncovered set 都包含于 top cycle，Bordes/Gillies 又细化 McKelvey。$UC\subseteq PO$ 在该域仍成立且可严格；论文对 $n=5$ 约 9,078,630 个 profile（按对称性）穷举、对 $n=7$ 采样 1,000 个 impartial-culture profiles，发现 UC 通常远小于 PO（§4.2、Figures 1–3）。这些是 enumeration/抽样观察，不是对任意 $n$ 的尺寸上界。

## 局限与复现

- 所有定理依赖严格、完整、ordinal 的一对一 house allocation；ties、缺失接受性、房屋容量、随机 assignment、可转移货币或双边稳定 matching 都会改变 majority relation 与结论。
- “majority graph 足以决定”是该 assignment domain 的结构性结果；它不意谓 graph 已经小到可直接穷举：assignment alternatives 有 $n!$ 个，uncovered set 本身也可指数大，论文明确将高效找出/验证 UC 留作问题。
- Top cycle 很大表示可由多数路径到达，不等于某 assignment Pareto-optimal、popular、公平或可被现实机制稳定实施。论文自己举出非常差的 allocation 仍可在 top cycle 的例子。
- 复现应固定 strict preference profile、assignment 编码与 weak/strict majority tie 处理；验证 Theorem 1 的 rotation equivalence、serial dictatorship–PO 对应、Theorem 2 的 $n\ge5$ 前提及 n=5 对称性约简。抽样图应单独报告随机数种子与 impartial-culture 生成法。

## 与 AAMAS 的关系与核验说明

该文连接社会选择、多数关系和资源分配，为无 popular assignment 时选择 assignment 提供结构性视角。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2602.14816) 核对模型、Theorem 1–2、Propositions 1–2 和 uncovered-set 实验范围；所有结果均保留其一对一严格偏好与 $n$ 的限制。
