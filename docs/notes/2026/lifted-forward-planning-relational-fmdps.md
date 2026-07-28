---
title: "Lifted Forward Planning in Relational Factored Markov Decision Processes with Concurrent Actions"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/GOIS4183"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GOIS4183.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["indistinguishable_object_assumption", "structural_width_exponential", "approximate_policy_error", "synthetic_benchmark_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Lifted Forward Planning in Relational Factored Markov Decision Processes with Concurrent Actions

## 一句话总结

Foreplan 为有大量不可区分对象、可并发行动的 relational factored MDP（rfMDP）构造 histogram/一阶 lifted state-action 表示并用 LP 求值；它将对象数量的增长降为多项式，但总体难度仍受关系结构宽度指数控制，近似版以 ALP 换取更大规模。

## 方法与证据

- 论文用 parameterized random variables（PRVs）描述对象集合和 action PRVs 描述同一时间可对多个对象施加的行动；动机是避免对每个对象子集枚举并发 action（§1、§3）。
- Foreplan 从 relational cost graph 找共同出现且共享 logvar 的 PRV clique；对每个 clique 用 counting random variable 的 histogram 记录联合取值计数，而不是记录对象身份（§4.1）。Theorem 4.7 证明该 compact representation 保持 grounded MDP 的 state semantics。
- exact Foreplan 在此 compact state representation 上建立 LP 求 value function/policy。state representation 的大小为 O(c × 2^w)，其中 c 为 clique 数、w 为最大 clique size（Theorem 5.1）。
- Approximate Foreplan 用 parameterized basis functions 和 lifted backprojections 实现 ALP；在 w 有界时，其运行时间对对象数与 c 多项式、但对每个 cost network 的 induced width 指数（Theorem 6.4），并与 grounded ALP 等价（Theorem 6.5）。
- 实验在 epidemic、fully-connected SysAdmin 与并发 BoxWorld 上比较 XADD symbolic VI/ALP：epidemic 例中 approximate 版本在两小时限制内扩展到 191 人，论文报告在 2--10 人测试上错误 action 比例最高 2.98%，SysAdmin 九台以内返回最优策略（§7）。

## 适用边界与复现

- 提升依赖对象在模型与一阶 Markov history 下不可区分；存在个体身份、异质转移/奖励、长期身份依赖或稠密关系耦合时，histogram compression 可能不再适用或不再紧凑。
- “对对象数多项式”不表示通用可扩展：exact 版仍需遍历与 c 相关的 state space，approximate 版仍对 induced width 指数；需要报告 c、w、induced width 及 LP 规模。
- Approximate Foreplan 的理论保证是给定 state-relevance weights 的 weighted L1 最优 value-function approximation，而非逐状态/逐行动零误差；其 2.98% 数字来自特定合成 epidemic 设置。
- 复现应公开 rfMDP parfactors、reward/basis functions、discount、初始 state、对象数量 sweep、timeout/memory、HiGHS/solver tolerance 与 action-error 的 grounded 对照；现实规划使用还须单独验证建模误差与执行约束。

## 与 AAMAS 的关系与核验说明

这是多智能体规划/MDP 表示与求解工作，核心是把并发行动的组合爆炸转化为关系型计数推理。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GOIS4183.pdf) 核对 Foreplan 表示、Theorems 4.7/5.1/6.4/6.5 与 §7 benchmark；没有将合成加速或近似结果表述为任意现实系统的最优保证。
