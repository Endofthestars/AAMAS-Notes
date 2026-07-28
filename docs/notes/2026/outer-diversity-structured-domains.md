---
title: "Outer Diversity of Structured Domains"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "applications"]
dblp_key: ""
doi: "10.65109/WNGL6996"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WNGL6996.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["combinatorial_diversity_not_social_representation", "uniform_ranking_distribution_assumption", "swap_distance_metric_dependence", "sampling_estimation_error", "domain_encoding_dependence", "no_empirical_preference_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Outer Diversity of Structured Domains

## 一句话总结

本文以“均匀随机的所有 ranking 到结构化 preference domain 中最近 ranking 的平均、归一化 swap distance”定义 outer diversity，衡量该域在排列空间的覆盖程度。作者给出许多域的最近 ranking 算法、表格/采样比较和固定域大小下的高多样性构造；GS/cat 在其比较中很突出。该指标是指定距离与 uniform 排列分布下的组合几何量，不是选民人口多样性、意见代表性、偏好真实性或选举公平的保证。

## 方法与证据

- domain \(D\subseteq L(C)\) 是允许投出的线性 ranking 集。对两个 ranking，swap distance 是两者相对次序相反的 candidate pairs 数；\(\text{swap}(D,v)\) 取 \(v\) 到域中最近 ranking 的最小值（§2.1）。作者的 outer diversity 将 uniform 随机 \(v\in L(C)\) 的该距离取平均并归一化（Def. 3.1）。
- 因而“outer”关注 domain 外的 rankings 有多接近某个域内 ranking；与 richness diversity（子结构计数）和 inner diversity（如 \(k\)-Kemeny clustering）不同（§1）。指标高表示以 swap metric 看域对排列空间覆盖较好，不表示样本选民更多样、少数群体被代表、候选政策更广或结果更公平。
- 论文考察 classic single-peaked（SP）、cycle SP（SPOC）、single-peaked trees、single-crossing（SC）、group-separable balanced/caterpillar（GS/bal、GS/cat）及 Euclidean variants（§2）。每一个域是由轴、树、图或生成规则定义，故数值首先比较这些数学定义，不能自动检验真实偏好是否属于它们。
- 精确枚举所有 \(m!\) rankings 可算值但很快不可行。作者将大规模计算化为“给定 ranking 到给定 domain 的最近点”；对 4-alignment domain 该问题 NP-hard（Theorem 4.2），说明采样本身不能绕开困难的投影问题。
- 作者给 SP 最近点的 \(O(m^2)\) dynamic program（Theorem 4.3），给 SPOC 和带 \(k\) leaves 的 SP-tree 算法（Theorems 4.4–4.5），但一般 graph single-peaked 问题仍为 NP-complete（Theorem 4.6）。GS-tree 有算法（Theorem 4.7），GS/bal 与 GS/cat 可在 \(O(m\log m)\) 完成（Theorem 4.8）；SC/Euclidean domains 经预处理也可快速查询（Theorem 4.9）。
- 评测以 sample random votes、投影到各域并平均；表 2 采用 \(N=1000\) samples，作者称 standard deviation 小（§5）。这是蒙特卡洛近似，误差随域/候选数/随机种子和最近点实现变化；论文的 SC 采样算法也不是对所有 SC domains 的 uniform sampler（§2.2）。
- 论文报告 outer-diversity domain ranking 与此前 inner-diversity 分析相近，并强调 GS/cat 是所研究域中最 diverse、且具有其他域缺少的局部邻域特征（§1, §5）。这是所选 family、候选规模、swap metric 和 uniform reference measure 下的比较，不应简化为“caterpillar preferences 更真实”。
- 对固定大小域，作者给出满足/接近高 outer diversity 的构造与启发式（Theorem 6.1, §6），并将其用于比较 structured domains 距同尺寸最大值的差距。该优化目标是排列空间覆盖，未纳入可解释性、学习成本、投票规则操纵性或个体福利。

## 适用边界与复现

- 适用于 computational social choice 的合成选举实验、结构偏好域的几何比较，以及需要选择“覆盖不同 ranking”的测试实例。应把它和真实样本频率、人口/群体分层、policy distances、结果稳定性和少数群体保障分开报告。
- 不可用 outer diversity 单独证明一个投票流程包容、公平或民主正当。公共决策还需代表性与参与审计、候选可及性、偏好收集偏差、策略投票、结果对少数群体的影响、透明解释和申诉机制；uniform 置于所有排列上的先验通常没有人口学意义。
- 复现需固定 candidate 数、每个 SP/GS/SC/Euclidean domain 的生成/轴/图、swap distance、normalization、随机种子和样本数；复现 Table 1 最近点复杂度、Table 2 的 \(N=1000\) 指标，以及固定 size 的启发式。对每项给置信区间、采样分布与投影运行时，勿只报单一平均数。
- 应研究加权/经验分布下的 outer diversity、其他 ranking metrics、近似投影、实际选民数据的 out-of-domain rate、domain misspecification、不同 candidate labels/attributes，以及与群体代表性和投票结果公平指标的关系。

## 与 AAMAS 的关系与核验说明

这是 AAMAS computational social choice 中的 structured-preference-domain 分析工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WNGL6996.pdf) 核对 outer diversity 与 swap distance 定义、各域、最近点复杂度/算法、4-alignment NP-hardness、\(N=1000\) sampling、GS/cat 的相对结论和固定大小构造；没有把排列覆盖量误写成社会多样性、真实偏好证据或选举公平保证。
