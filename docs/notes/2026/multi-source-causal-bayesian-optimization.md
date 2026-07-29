---
title: "Extending Multi-Source Bayesian Optimization With Causality Principles"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "applications"]
dblp_key: ""
doi: "10.65109/JWIE9181"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JWIE9181.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02p"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "causal_graph_assumption", "ground_truth_for_evaluation", "limited_real_network_evaluation", "clinical_policy_non_deployment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Extending Multi-Source Bayesian Optimization With Causality Principles

## 一句话总结

MSCBO 将多信息源 Bayesian optimization 与因果 BO 合并：每个来源配有因果 DAG、观测与 Gaussian Process，以成本敏感 Knowledge Gradient（CKG）选信息源，并用 POMIS 限制候选干预集；随后以 \(\epsilon\)-greedy 在观测和干预间分配全局预算。摘要在 PSA 与 46-gene E. coli 因果网络及噪声场景中报告其通常不劣于 MSBO/CBO、在可利用因果结构时成本效率更高，但这取决于给定 DAG、成本与 ground truth 的正确性，不能直接作为临床或政策干预建议。

## 方法与证据

- 用户提供每个来源的 DAG/观测、来源成本、观测与干预成本、用于评估的 ground truth 和总预算。MSCBO 以每来源 GP 建模，使用调整后的 cost-sensitive KG 衡量信息价值，并以 Posterior Optimal Minimal Intervention Sets（POMIS）从因果结构缩小干预空间（§1）。
- 每轮优化各来源 CKG，选取最大者；\(\epsilon\)-greedy 决定观测或干预。观测时从所选网络取 \(k\) 个样本并更新其因果模型；干预时取最优干预集、计算 posterior value、更新模型与全局最优；累计成本超过预算则停止（§1，步骤 1--4）。
- 实验对比 MSCBO、非因果 MSBO 和单源 CBO，在来自相关研究/BN Repository 的递增噪声网络上测试，并展示 statin 对 PSA 与 E. coli 46-gene 网络的 base case 和最噪情景（§2、图 1）。摘要称最坏/基线场景下 MSCBO 可比，在较大复杂网络和可用因果知识时更省成本、收敛更快；未给出图中精确数值、重复次数、置信区间或统计检验。

## 适用边界与复现

- 适合已拥有可辩护因果结构、明确来源保真度/成本且能实施受控干预的研究优化；DAG 漏边、混杂、测量偏差、来源不可迁移或成本误设都会使 POMIS 和 CKG 的优势失效甚至产生危险推荐。
- PSA 和基因网络是方法学示例，不是临床疗效、处方或生物实验结论。真实部署需独立因果识别、伦理审批、安全约束、干预可逆性和领域专家监管。
- 复现应锁定 DAG、结构方程/噪声、source fidelity/cost、budget、GP kernel/超参数、CKG 优化、\(\epsilon,k\) 与 POMIS 实现；报告所有 seed 的 simple/cumulative regret、总成本、干预次数、对 DAG 错设和成本扰动的敏感性，并与随机/单源/非因果强基线比较。

## 与 AAMAS 的关系与核验说明

该文为资源受限自主体的因果信息采集与干预规划提供了优化框架。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JWIE9181.pdf) 人工核对 MSCBO 输入、CKG+POMIS、迭代过程、PSA/E. coli 评测和比较对象；未把其摘要中的相对曲线解读成现实干预的有效性或安全保证。
