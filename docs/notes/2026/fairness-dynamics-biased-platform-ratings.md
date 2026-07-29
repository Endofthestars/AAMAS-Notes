---
title: "Fairness Dynamics in Digital Economy Platforms with Biased Ratings"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "resource_allocation", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/CEJT6762"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CEJT6762.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["evolutionary_model", "binary_rating_and_effort", "demographic_parity_only", "protected_attribute_access", "mean_field_users", "stationary_population_assumption", "policy_parameter_misspecification"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fairness Dynamics in Digital Economy Platforms with Biased Ratings

## 一句话总结

论文以演化博弈建模数字服务平台：用户按 rating 选择 provider，边缘化群体的高努力服务会以概率被错报为低 rating。只优先显示高 rating provider（且不显式照顾群体）时，用户体验（UX）与 demographic parity ratio（DPR）形成 Pareto trade-off；允许推荐列表控制边缘化 provider 数量 \(k_M\) 后，数值结果显示可在几乎不损 UX 的情况下大幅改善 DPR，即使对真实评分偏差只有区间估计。它是机制性证据，不是对任一平台的因果实证保证。

## 方法与证据

- 模型有 dominant 与 marginalised 两类 provider，各自选择高努力 \(H\)（收益 \(b-c\)）或低努力 \(L\)（收益 \(b\)）；平台推荐长度为 \(k\) 的列表，其中至少 \(k_G\) 个高评分 provider，\(k_M\) 个属于边缘化群体。用户随机选择，Good rating 权重为 1、Bad rating 为 \(1-\gamma\)（§3）。
- rating bias \(\epsilon\) 表示 marginalised provider 采取 \(H\) 时被用户错报为 Bad 的概率；\(\gamma\) 表示用户对 rating 的敏感度。评分更新与接单概率再反过来影响 effort 的收益，群体策略用有限人口 Moran process 的稳态分布计算（§3.2--§3.3）。
- 评价包括稳态中高努力比例加权的 UX，以及两群 provider 平均效用之比 DPR（较低/较高，取值 \([0,1]\)）；这是 group-level demographic parity，不是 individual fairness、机会均等、校准或福利总和（§4.1）。
- \(k_M=0\) 的“表面中立”排名下，\(k_G\) 越高，regime C（两组都多数高努力）内 UX 单调提高；超过使 DPR 最大的 \(k_G^{DPR}\) 后，边缘化群体因 biased rating 而更少被展示，DPR 下降。故在该约束下 Pareto front 为 \([k_G^{DPR},k]\)，必须在 UX 与 DPR 之间取舍（§5.2）。
- 当允许 \(k_M\ge0\) 直接调整结果列表中的 marginalised provider 数量时，作者的数值实验发现提高 \(k_M\) 对 DPR 影响显著、UX 通常近乎平坦；在 \(\gamma=0.8\) 下，偏差 \(\epsilon\) 从 0.15 升至 0.5 时，最佳 \(k_M\) 从 3 升至 9。只有低 bias 且 \(k_M\) 很高时，dominant group 的努力激励才明显受损（§5.3）。
- 对未观测的真实 \(\epsilon\)，论文以区间上的 uniform belief 比较最大化期望 DPR 与 maximin DPR；示例 \(k=20,\epsilon=0.35,\gamma=0.65\) 中，即使不确定度达到 0.7，允许 \(k_M\) 变化的最坏/平均 DPR 仍优于固定 \(k_M=0\)（§5.4）。这是模型内稳健性，不表示在未知真实数据分布下无风险。
- 模型展示“没有 reputation incentive”时双方转向低努力、优先高 rating 却不足以让 marginalised group 合作时出现分离均衡、足够优先则两组均高努力（§5.1）。公平干预因而还影响长期服务质量激励，而不是静态曝光配额问题。
- 作者明确的抽象包括固定 provider 数、无限/mean-field user population、间接 reciprocity、二元 rating/effort、忽略 collective action，以及假定人口属性被完全混淆；实际小市场、流失进入、直接关系和可见特征都可能改变动态（§6）。

## 适用边界与复现

- 适用于有重复评分反馈、可追踪供给侧长期激励且平台依法可以处理受保护群体信息的双边市场；先确认 \(\epsilon\) 的错误方向、评分阈值和展示机制是否与模型相符。
- 不能据此直接实施硬配额或仅以 DPR 判定合规。实际治理须评估不同公平定义、provider/consumer 隐私与同意、申诉、地区法律、供给稀缺、价格、服务质量、群体内异质性以及属性推断带来的风险。
- 复现应使用作者公开代码/appendix，固定 \(Z,k,\epsilon,\gamma,k_G,k_M,b,c\)，构建转移矩阵并求稳态；重现 \(k_M=0\) Pareto front、\(k_M\) sweep 和不确定性实验，并以 Monte Carlo 核对矩阵计算。报告 UX、DPR、两组 effort、曝光/成交率和参数敏感性。
- 上线前宜做离线反事实评估、受控小流量试验、阈值与属性误分类敏感性分析，以及持续监测长期 effort、收入、质量、投诉与群体差异；发现对 \(k_M\) 高敏感时使用保守约束与人工治理，而非自动最大化单一指标。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的公平推荐、声誉系统与演化多智能体机制设计工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CEJT6762.pdf) 核验 §3--§4 的模型/指标、§5 的 Pareto、显式反歧视与不确定性结果以及 §6 的限制；没有将数值稳态结论夸大为对 Airbnb、Uber 或其他真实平台的已验证政策效果。
