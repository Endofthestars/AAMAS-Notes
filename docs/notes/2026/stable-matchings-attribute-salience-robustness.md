---
title: "Robustness of Stable Matchings When Attributes and Salience Determine Preferences"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "safety_verification"]
dblp_key: ""
doi: "10.65109/IQTL2250"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IQTL2250.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["attribute_based_preference_model", "one_sided_salience_perturbation", "fixed_attribute_dimension_assumption", "strict_complete_preferences", "matching_fairness_not_established"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Robustness of Stable Matchings When Attributes and Salience Determine Preferences

## 一句话总结

本文研究两侧稳定匹配中一侧以可观测属性的加权和排序、且权重（salience）会变化的情形：它定义 ⁠\((k,r,p)\)-robustness，并在属性数 (m) 固定时给出验证给定匹配和计算其最大鲁棒半径的多项式算法；全局最鲁棒匹配则由带认证上下界的 anytime search 近似搜索，不能读作对真实录取/招聘偏好或公平性的保证。

## 方法与证据

- 市场为平衡二分图：A 方有静态严格偏好和 (m) 维非负属性向量；B 方以归一化 salience vector 对 A 方属性作内积排序，并使用固定 tie-break。扰动可改动每个 B 方 agent 至多 (k\le m) 个坐标，归一化后以 (\ell_1,\ell_2,\ell_\infty) 距离限制在 (r) 内（§2）。
- 一个稳定匹配是 ⁠\((k,r,p)\)-robust，当任何许可的单个 B 方 salience 扰动都不能产生 blocking pair。对每个潜在 blocker 与坐标 support 枚举可行性问题：(p=1,\infty) 为 LP，(p=2) 为 SOCP；固定 (m) 时，论文证明验证与给定匹配的最大半径均可在多项式时间求解（Theorem 3.2、4.2）。
- 对“最鲁棒稳定匹配”，作者以 rotation poset 构造 lower/upper bounds，并优先展开上界最大的 node；每一步精确评估当前匹配的半径、可剪枝，随时保持 (LB\le\max_\mu r^*(\mu)\le UB\)。若 relaxation 出现 integral solution 才认证全局最优；否则这是可提前停止的 anytime 方法，最坏情形并非多项式（§5.3--5.4）。
- 对给定 robustness target (\tau)，论文以 base radius 的 maximum-weight closure/min-cut 得到可行成本上界，并以 stable-marriage polytope 加 vulnerability cuts 的 LP 得到成本下界；两者夹住满足 (r^*(\mu)\ge\tau) 的最小成本（§6）。
- 固定匹配的稳定 salience profile 在 B 方 agents 间分解为 simplex 内的低维凸多面体；主文给出 factorization/inequality characterization，关于体积计算的完整分析则放在扩展版本（§7，reference [26]）。

## 安全边界与复现

- 结论依赖平衡两侧市场、A 方偏好固定、B 方由线性属性加权诱导的严格完整排序、固定 tie-break 与“每次只扰动一个 B 方 agent”的 worst-case 模型；真实市场常有缺失选择、容量、策略行为、共同冲击、双侧偏好变化和非线性/不可观测因素。
- “多项式时间”明确以 (m) 固定为条件，support 枚举含 (m^k) 项；属性数或可改动坐标增长时，实际规模不应由该定理直接推断。全局搜索以 certified bounds 逼近，除 integral certification 外不能宣称已找到精确最优。
- salience 是模型化的属性重要性，不等于人的真实偏好、资格、价值或应受保护特征的正当使用。用于录取、招聘、医疗匹配或公共分配前，必须独立审查数据来源、代理变量、差别影响、申诉/退出机制、容量和法律规则；稳定与半径都不推出公平、福利最优或合规。
- 复现应固定实例、属性尺度/归一化、双方偏好、tie-break、(k,r,p)、LP/SOCP solver 和容差、rotation poset 生成、成本函数、搜索预算及随机性；同时报告精确 gap、runtime、数值稳定性和对属性/权重扰动的敏感性。

## 与 AAMAS 的关系与核验说明

这是稳定匹配、鲁棒优化和凸几何相结合的机制/算法工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IQTL2250.pdf) 核对属性--salience 模型、Theorem 3.2/4.2、anytime bounds、成本 tradeoff 与 polytope factorization；没有把形式化鲁棒性表述为真实偏好、匹配公平或部署资格的证明。
