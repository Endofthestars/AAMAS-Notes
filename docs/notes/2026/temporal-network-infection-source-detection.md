---
title: "Catch Me If You Can: Finding the Source of Infections in Temporal Networks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "agent_engineering", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LOWK9942.pdf"
preprint_url: "https://arxiv.org/abs/2412.10877"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["adversarial_model_scope", "randomized_success_condition", "asymptotic_bound_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Catch Me If You Can: Finding the Source of Infections in Temporal Networks

## 一句话总结

论文把时间网络中的感染源发现建模成 Discoverer 与 Adversary 的轮次博弈，以“找到源之前发生的感染数”（price of detection）而非轮数衡量代价，并对多种图信息和源行为条件给出算法与下界。

## 方法与证据

- 时间图中的边只在特定时刻存在；传播采用 SIR 过程。Adversary 选择时间网络、源节点及其感染开始时机；Discoverer 每轮观察一个节点，并获知该节点是否、何时及由哪个邻居感染（§1、§3）。
- 评价目标是 price of detection：为兼顾 Adversary 延迟被发现和一次传播尽量多感染的动机，计数到发现源为止的成功感染数，而不是观察轮数（§1）。
- 一般未知静态图、源行为一致时，论文给出常数成功概率下 $\mathcal O(n\sqrt n)$ 的随机检测算法，并证明任何常数成功概率算法都需 $\Omega(n\sqrt n)$；这是该具体条件下的渐近匹配界（§1、§4）。
- 已知静态图不自动改善一般图的上述量级：文中将相关 lower/upper transfer 区分为定理或推论，而对 treewidth 为 $\mathrm{tw}$ 的已知图给出 $\mathcal O(\mathrm{tw}\,n\log n)$ 的算法（§5）。
- 对已知树且源行为一致，得到 $\mathcal O(n\log n)$ 的常数成功概率算法及无限树族上的 $\Omega(n\log n)$ 下界；这里“已知树”“一致源行为”和成功概率条件缺一不可（§6）。
- 若 Adversary 可在各轮改变源的感染时机但仍不知道 Discoverer 的观察选择（obliviously dynamic），一般图的常数成功概率下界上升到 $\Omega(n^2)$；已知树的 $O(n\log n)$ 结果需允许每轮观察两个节点（§7）。

## 局限与复现

- 这不是从有限观测日志进行统计源估计的通用结论，而是信息结构明确的最坏情形对抗博弈：Discoverer 的观测能力、Adversary 是否知道观察动作、以及成功概率标准都会改变结果。
- $\mathcal O(n\sqrt n)$ 和 $\mathcal O(n\log n)$ 的陈述通常是“以常数概率赢得游戏并在该感染预算内完成”；不可误写成每次运行都保证相同预算的确定性上界。
- 树的匹配界对应 known static graph、consistent source behavior；对未知图、一般图或动态源行为套用该 tight 结论是不成立的。
- 复现应生成带时间标签的图和 SIR 参数，分别实现 Discoverer/Adversary 的信息集；对每种情形报告成功概率、条件感染数分布和最坏构造，而非仅报告平均发现轮数。

## 与 AAMAS 的关系与核验说明

该工作面向在时变交互网络中追溯疾病、污染或错误信息源的 agentic detection 问题。笔记以作者公开的 [arXiv 全文](https://arxiv.org/abs/2412.10877) 为主文本，并将每个近似/下界的图类、源行为、观察能力与概率限定分开记录。
