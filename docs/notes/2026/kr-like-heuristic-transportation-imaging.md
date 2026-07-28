---
title: "Scalable Knothe--Rosenblatt-like Heuristic Transportation Plans for Imaging Problems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "resource_allocation", "applications"]
dblp_key: ""
doi: "10.65109/CEMK9641"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CEMK9641.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["two_dimensional_grid_scope", "learned_optimal_composition_constraints", "baseline_reimplementation_and_tuning", "imaging_only_evaluation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Scalable Knothe--Rosenblatt-like Heuristic Transportation Plans for Imaging Problems

## 一句话总结

论文把二维离散概率分布间的 Knothe--Rosenblatt (KR) 耦合推广为由中间分布 composition rule 决定的一族 KR-like 可行运输计划，并训练 KRo-Net 近似最优 rule；理论给出可行性、KR/最优耦合作为特例及若干界，成像实验显示较小 Wasserstein 残差，但这不是对一般维度、任意 cost 或多智能体分配性能的证明。

## 方法与证据

- 在两个 `n×n` 网格概率测度上，composition rule `R(μ,ν)` 产生满足相应边缘约束的中间测度；Algorithm 2 再将两个一维最优运输阶段合成计划。Proposition 1 给出该构造 `O(n²)` 操作，Theorem 2 证明任意合法 rule 所诱导计划属于 `Π(μ,ν)`（§3）。
- Theorem 3 证明特定 `R_KR` 恢复经典 KR plan；Theorem 4 说明取最优 composition rule 时诱导计划是最优运输计划。Proposition 2 仅比较 independent rule 与独立耦合的成本；Theorem 5--6 给出 rule/诱导 plan 的误差与稳定性关系，范围均是文中二维离散定义和假设下（§3）。
- KRo-Net 以 augmented Lagrangian 训练输出满足中间测度约束的 rule，目标针对 `W1`；作者称其他 `Wp` 更复杂。实验将像素归一为概率分布，在 MNIST、USPS、BraTS2020、Brain MRI 上与 KR、Sinkhorn、Sinkhorn-Net 比较，100 次平均并使用同一 PyTorch 2.9.0 重实现，硬件为 RTX 5090（§4--5）。
- 表 1 报告 KRo-Net 在四个数据集具有最小的 transported-to-target Wasserstein 距离；表 2 只比较两个神经网络方法，论文称 KRo-Net 比 Sinkhorn-Net 的训练时间/内存更低。经典 KR/Sinkhorn 是闭式/求解器，作者明确认为与需训练的网络直接比较效率并不公平（§5）。

## 局限与复现

- 形式证明从二维规则网格、离散概率、指定 conditionals 与 composition-rule 可行性出发；高维扩展被放在附录/未来工作。不能据此直接推出连续、高维、稀疏不规则网格、不同 cost 或数值有限精度下仍有相同复杂度与最优性。
- KRo-Net 的“最优”取决于训练能否满足 augmented-Lagrangian 约束并收敛到最优 rule；论文的最优计划定理针对真正的最优 rule，不自动适用于一个有限数据、有限容量、有限训练迭代的网络输出。
- 四个基准均为图像分布，评价是运输后与目标的 Wasserstein 距离；没有下游医学诊断、跨设备泛化、临床效益或多智能体资源分配实验。AAMAS 中提到的机制设计/分配只是潜在应用，未被实证。
- 比较依赖作者在同一框架中的 Sinkhorn/KR/Sinkhorn-Net 重实现和“不可得时简单调参”；应公开 split、seed、网络结构、所有正则/惩罚系数、停止准则、是否把训练成本计入时间、GPU/precision 和每次 100-run 的原始值，并与成熟 solver 的公平设置复核。

## 与 AAMAS 的关系与核验说明

该文为可用于匹配、分配和图像分布比较的最优传输工具提供了 KR-like 形式化。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CEMK9641.pdf) 核对定义、Proposition 1--2、Theorem 2--6 及表 1--2；未将二维构造或成像基准结果扩大解释为一般最优传输或实际多智能体分配保证。
