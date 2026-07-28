---
title: "Synthesis of Safety Specifications for Probabilistic Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "planning_scheduling", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/MGLX3286"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MGLX3286.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["finite_mdp_model_assumption", "cpctl_fragment_only", "generalized_slater_assumption", "probability_model_dependency", "gridworld_evaluation_only", "no_real_system_certification"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Synthesis of Safety Specifications for Probabilistic Systems

## 一句话总结

本文为有限标注 MDP 的一类嵌套概率安全公式 CPCTL 综合单一、可依赖历史且可随机化的策略：通过把全局公式满足转换为增广 MDP 中的局部兼容约束，并以 CPCTL-VI 构造可实现值前沿。它对每个构造出的候选给出模型内的正确策略；而“存在解就能找到”的最优性结论依赖广义 Slater 严格可行性假设，实验也仅覆盖两种带滑移噪声的 gridworld，不能视为真实系统安全认证。

## 方法与证据

- 综合问题输入是有限 labelled MDP 与 CPCTL 公式，目标是找出**同一条** history-dependent randomized policy，使初始状态满足整条公式（§3）。这不同于逐个概率子公式分别选择策略的普通 model-checking 解释；策略记忆与随机化均可能必要。
- CPCTL 是 PCTL safe 的受限片段：状态公式由原子命题、否定、合取与概率阈值组成，路径公式采用受限 weak-until 结构（§4）。它允许概率算子嵌套，但并不覆盖一般 PCTL/PCTL safe；论文也将更一般公式的综合困难性作为该片段设计动机。
- 作者构造增广 MDP，把每个原始状态附加子公式的布尔 valuation 与路径公式的概率 counter；动作除选原 MDP 动作外，还为后继状态选这些量（Def. 4）。完整增广状态空间含连续 counter，因而本身无限；算法只逐步导航一个有限构造部分，并非直接穷举所有状态。
- valued policy 对增广变量的选择保持确定，state compatibility 将子公式 valuation 与阈值/合取等关系对齐，path compatibility 用局部 Bellman 型不等式对齐 counter（Defs. 5–7）。Coherence theorem 证明两类兼容性成立时，counter 与 valuation 对应于该增广策略下的概率/状态公式满足（Theorem 2）。这是给定精确 MDP、标签与转移概率下的形式化语义结果。
- CPCTL-VI 从可处理的初始化值向量出发，反复施加 Bellman operator，保留按 valuation/counter 偏序的极大值前沿（§6.1, Alg. 1）。Soundness theorem 表明每轮加入的值向量都有可构造的 memoryful 原 MDP policy，满足相应概率下界与已标记子公式（Theorem 3）；因此它不会把未证明的候选当作可行解。
- 完备/最优性不能无条件表述：Theorem 4 需要广义 Slater 假设，即存在对相关概率阈值严格留有余量的策略；在此条件下，有限次迭代后前沿含有达到目标阈值的向量。阈值恰在可行边界、模型数值误差或严格余量不存在时，论文的该保证不适用。
- 实验实现为 Python，在两种有随机滑移的网格世界中评估嵌套目标 \(P^{\ge p_1}G(P^{\ge0.6}(\neg d\,W\,G))\)：一个 7×7 中央墙环境，另一个 9×10、墙有开口的环境（§7, Figs. 4–6）。报告的是 Pareto 前沿与相应避险路径选择；第二个前沿可非凸，图中不连点以维持 soundness。没有真实机器人、学习模型、感知误差、未知动力学、长期失效或工业场景评估。

## 适用边界与复现

- 适合将明确的概率安全/可达性需求编码到小至中等、转移模型已知且有限的 MDP，并要求策略在嵌套概率约束间保持全局一致的规划问题。它不是从数据学习转移概率、自动提炼现实安全规范或处理开放世界系统的方法。
- 部署到机器人、交通、医疗或工业控制前，应独立验证状态标签、动作集、概率转移、初始状态分布及模型误差；并以 runtime monitor、硬约束/shield、保守置信界、fail-safe 与人工接管覆盖模型失配。CPCTL 满足只保证抽象 MDP 内的公式语义，不等于碰撞为零、法规合规或系统级安全。
- 复现应固定有限 MDP 编码、AP 标签、动作与滑移分布、完整 CPCTL 公式及阈值、广义 Slater 可行性检查、初始化 \(P=1[G\varphi]\) 子问题、Bellman/frontier 的数值精度和 dominance 规则、停止准则与策略记忆更新。应逐项检查输出策略在原 MDP 中的所有嵌套概率约束，而非只画前沿。
- 应扩展到阈值边界无严格余量、模型参数扰动、浮点误差、状态爆炸、不同初始状态、稀有危险转移和非网格模型；报告求解时间、frontier 大小、内存、违反率/最差概率下界与失配后的安全退化，才能判断实际可用性。

## 与 AAMAS 的关系与核验说明

这是概率时序逻辑下多智能体/自主系统规划的形式化方法工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MGLX3286.pdf) 核对 CPCTL 语法、统一策略综合语义、无限增广 MDP、兼容性与 coherence、CPCTL-VI、soundness、带广义 Slater 条件的最优性，以及两种 gridworld 实验；没有把受限逻辑、精确有限模型中的可行性或仿真避险路径误写成一般 PCTL 完备性、现实概率准确性或部署级安全保证。
