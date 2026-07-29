---
title: "First-Order and Second-Order Model Counting Meet Stable Marriages, Stable Roommates, and Stable Diners"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "argumentation_reasoning", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/SJZA5231"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SJZA5231.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["fixed_k_requirement", "bounded_treewidth_and_degree_requirement", "type_based_preference_assumption", "strict_preference_scope", "logical_encoding_overhead", "unbounded_k_hardness", "approximate_matching_sampling"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# First-Order and Second-Order Model Counting Meet Stable Marriages, Stable Roommates, and Stable Diners

## 一句话总结

论文把 stable marriage、stable roommates 与 stable seating 统一到固定 (k) 类偏好画像：用二阶逻辑 MSO2 与 Courcelle 的计数扩展，在座位图树宽和最大度均有界时多项式地计数并均匀采样稳定座位；用带计数量词的两变量逻辑 C2 的 lifted model counting，在固定 (k) 时多项式地计数稳定婚姻/室友匹配，并可近似均匀采样。结论依赖小而固定的偏好类型数及图结构/逻辑片段，不是任意偏好市场的通用高效算法。

## 方法与证据

- (k)-class profile 将每个 agent 指派到至多 (k) 个类型；同类型 agent 有相同偏好，且其他类型对同一类型内个体不作区分。(k=n) 退化为一般情形，(k=1) 为完全同质偏好；压缩后偏好描述仅有 (O(k^2)) 规模（§1、§3）。这种对称性是 tractability 的根源。
- 对 stable seating，顶点是座位、边是相邻关系，类型以自由集合变量表示；论文用 MSO2 写出偏好、互相想交换的 blocking pair 与稳定性。对固定 (k)，且座位图树宽和最大度有界，Courcelle 的计数版本给出 decision、construction 与 counting 的多项式算法（§4）。这涵盖 (2\times n) 矩形桌，解决 Berriaud 等 WINE 2023 所列的该类开放问题。
- seatings 的计数先得到类型标注数：为各类型集合引入权重，以多元插值取出给定类型人数对应的系数，再乘以各类型人数的阶乘以恢复可区分 agent 的安排数（§4）。这是逻辑计数到实际排列计数所需的显式校正。
- stable seating 的采样逐座位加入 Selected 类型 evidence，用条件计数计算下一个类型的概率；类型都选完后再在每个类型内部均匀置换 agent。论文声称该过程产生均匀稳定 seating（§4），但前提仍是固定 (k) 和有界树宽/度。
- 对 stable marriage，使用左右两侧、类型及 matching relation 的一元/二元谓词，借助 C2 的计数量词表达一对一匹配和 blocking-pair 禁止；把个体的类型与侧别写为 unary evidence。公式在固定 (k) 下大小不随 agent 数增长，C2 的 WFOMC 因而可在 domain size 的多项式时间计算（§5.1）。
- stable roommates 去掉二分侧别，增加 matching relation 对称性和每人恰有一个 partner 的约束；所得仍是 C2，故固定 (k) 的稳定室友计数同样多项式（§5.2）。论文也将该编码扩展讨论到相互关联的多重 matching，但没有给出独立的大规模实证基准（§5.4）。
- 采样 stable marriage/roommates 时，论文援引固定 C2 sentence 的 lifted sampling 结果：在给定 unary evidence 下可多项式时间“approximately uniformly”随机采样满足结构（§5.3）。因此不要将 matching 的近似均匀保证误写成 seating 部分的精确均匀保证。
- 一般偏好下 stable marriage 计数为 #P-complete、stable roommates 计数为 #P-hard；当 (k) 成为输入的一部分时，stable seating 即使在 paths/cycles 也 NP-hard（§1、§3.1）。固定 (k) 是不可省略的条件。

## 适用边界与复现

- 适用于偏好本来就可合理聚成少数可审计类别的配对、宿舍、课程/活动分配或座位安排；部署前要检验类型内不可区分与共同偏好的假设，而不是由算法便利性强行合并异质个体。
- 座位结论还要求固定 (k)、有界 treewidth 与有界 maximum degree；规则餐桌、窄网格可受益，稠密或任意邻接图不能直接继承复杂度保证。matching 结论不依赖座位图，但仍限制在相应 C2 编码和固定类型数。
- 复现应分别实现：类型画像与人数 evidence、matching/seat graph 稳定性审计、MSO2 或等价动态规划计数、C2/WFOMC 编码；对小实例穷举比对 counts。seating 采样要做频率检验验证均匀性；matching 采样应报告与精确小实例分布的距离，因论文的陈述是近似均匀。
- 实际机制还需报告福利、群体公平、未匹配率、策略性申报、隐私和可申诉性。稳定解数量多不等于分配公平，类型压缩也可能掩盖受保护群体内的差异。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 中将逻辑模型计数引入多智能体 matching、资源分配与稳定性分析的理论工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SJZA5231.pdf) 核验摘要、§3--§6 的 (k)-class 定义、MSO2/Courcelle 与 C2/FOMC 编码、(2\times n) 开放问题结论及两类采样保证；未将固定参数下的理论可解性表述为一般偏好实例的可部署性能结论。
