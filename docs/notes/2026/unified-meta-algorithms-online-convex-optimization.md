---
title: "A Unified Framework for Analyzing Meta-algorithms in Online Convex Optimization"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/FZOF9395"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FZOF9395.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["asymptotic_regret_scope", "oracle_feedback_assumption", "adversary_model_assumption", "convexity_lipschitz_requirements", "domain_geometry_dependence", "no_empirical_benchmark"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Unified Framework for Analyzing Meta-algorithms in Online Convex Optimization

## 一句话总结

论文建立一套在线优化 meta-algorithm 框架，在 linear/convex/strongly convex 函数、full-information/semi-bandit/bandit/zeroth-order oracle、fully adaptive/oblivious adversary，以及 static/dynamic/adaptive regret 间转换算法和界。核心是把若干已有技巧写成通用定理，并给出 deterministic zeroth-order 下的新 adaptive/static regret 结论；所有结果都受凸性、Lipschitz、域几何和反馈 oracle 假设约束。

## 方法与证据

- 形式化为有限 horizon \(T\) 的 agent--adversary game：每轮 agent 选 \(x_t\in K\)，adversary 选 loss \(f_t\) 与 query oracle，agent 可作若干 queries。框架区分确定/随机 oracle、确定/随机算法、fully adaptive/oblivious adversary 与多类 comparator/regret（§1--§3）。
- Theorem 2：任何对 fully adaptive adversary、确定 subgradient semi-bandit feedback 的 online linear optimization 算法，可转换为在线 convex（\(\mu=0\)）或 strongly convex（\(\mu>0\)）算法，保持同阶 regret；依赖 \(\mu\)-quadratization/线性化条件（§4--§5）。
- Meta-algorithm 1（FTS）与 Theorem 3 将 full-information first-order 反馈算法转成只需 semi-bandit 的算法，随后与 Theorem 2 合用。不是“少数据总是等价”，而是论文定义的可查询函数/域和 feedback 下的上界转换（§6）。
- Theorem 5 将 fully adaptive adversary 下确定 semi-bandit 算法，与 oblivious adversary 下随机 semi-bandit oracle 相联系；需要特定随机化/期望与 adversary 顺序，不能用于能观察随机性后即时反应的现实攻击者（§7）。
- Meta-algorithms 2--3（FOTZO/STB）以 smoothing 和 one-point gradient estimator 从 first-order/semi-bandit 生成 zeroth-order/bandit 算法（Theorems 6--7）；误差界依赖平滑半径、维度、\(\operatorname{diam}(K)\)、内切球等几何量（§8--§9）。
- Theorem 8 使用 two-point estimator：在 Lipschitz 函数类上，将 stochastic first-order 转为 deterministic zeroth-order 且同阶 regret。应用到 OGD/Improved Ader，论文列出确定 zeroth-order 凸函数 adaptive regret \(O(\sqrt T)\) 和 strongly convex static regret \(O(\log T)\) 等新结果（§10--§11）。
- 全文为证明/推导型工作，未报告真实数据或运行时 benchmark；结论强调可恢复文献中的多种界与简化证明，最终常数、oracle 实现成本和有限样本表现需要另行评估（§11--§12）。

## 适用边界与复现

- 适用于在线学习理论研究者将已有基算法移植到明确的反馈/对手设置，或审计一个 regret 声明是否真的满足它所用 oracle、随机性和函数类条件。
- 不应把 \(O(\cdot)\) regret 界直接当作生产 A/B 性能、延迟、鲁棒性或安全保证；带宽、噪声偏差、非凸/非 Lipschitz loss、约束违反、查询成本和对手适应性均会打破或显著改变前提。
- 复现应实现论文的 agent/oracle 定义、full-to-semi、first-to-zero、semi-to-bandit 与 two-point transforms，数值验证各 theorem 的条件和边界项；在 OGD/Ader 上分别记录 static/dynamic/adaptive regret、query 数、维度与平滑参数敏感性。
- 工程应用须先验证 oracle 是否真能提供所需点的值/梯度，加入安全约束、数值稳定性与有限预算评估，并与直接 bandit/gradient-free baselines 比较，不应仅依据渐近阶选择方法。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的在线决策、优化理论与算法分析论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FZOF9395.pdf) 核验 Figure 1、Theorems 2--8、四个 meta-algorithms 与 OGD/Ader 应用；没有将其在模型内的 regret 转换误称为实证系统改进。
