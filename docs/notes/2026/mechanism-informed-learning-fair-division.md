---
title: "Mechanism-Informed Learning for Fair Division"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "agent_engineering", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/HTOP9978"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HTOP9978.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02l"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["incomplete_preference_imputation", "missingness_model_assumption", "fairness_surrogate_gap", "household_chore_dataset_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Mechanism-Informed Learning for Fair Division

## 一句话总结

MIPL 从不完整的 chore disutilities 预测完整 preferences，同时通过 adjusted winner、round-robin、moving-knife 的可微近似，把分配在真实 complete preferences 上的 EF/PROP violation 纳入训练目标；在日本家庭家务偏好数据的模拟缺失实验中，报告比单纯 imputation 更低的 fairness loss。

## 方法与证据

- 研究不可分 chores 的非负 disutility。EF1/PROP1 分别是从自身 bundle 移除一件 chore 后的 envy/proportionality 松弛；AW 与 RR 在文中对应 EF1，MK 对应 PROP1（§2）。
- Direct preference learning 最小化 masked profile 的 Frobenius reconstruction loss，然后把 imputed profile 交给 mechanism。MIPL 则最小化 `λ·Loss_fair,M + (1−λ)·Loss_pro`，其中 fairness loss 用真实完整 profile 上的最大 EF 或 PROP violation（Eqs. 1--3）。
- 原 mechanism 有离散步骤，训练时用 `M^d_τ` 的 differentiable surrogate（例如 AW sorting 的 SoftSort）；inference 使用原 mechanism 输出 integral allocation。这引入了 surrogate 与实际机制间的潜在 gap（§3）。
- 数据为日本 2,000 名 participants 对 33 household chores 的偏好/所需时间评分，disutility 为二者乘积并归一化。按 agent-wise、chore-wise、top-t 三种 simulated missingness 生成训练/测试；n 为 2/5、训练 profiles 100/1000/10000（§4）。
- Table 1 是 n=2、agent-wise 的 EF loss。作者称多数场景 MIPL 更低，例如 AW(MIPL) 的 loss 为最好 Mean baseline 的 32--70% 且优于 AW(Direct)；但此类结果依赖训练/推理的 missingness 同分布假设。

## 适用边界与复现

- 公平训练损失以未观测的 complete preferences 作为监督真值；现实部署中若缺失不是随机或与敏感偏好、时间压力、语言/数字能力相关，imputation 可能系统性偏误，机制的理论 EF1/PROP1 对预测值并不能保证对真实值成立。
- 家务 disutility 是日本样本上的自报评分乘积，未验证在家庭、工作分配、课程/资源或不同文化群体的可迁移性；数据与分配决定还涉及关系权力、照护负担、同意与申诉，不能仅由 loss 表示。
- Soft approximations 与 `λ,τ` 的选择可能优化 surrogate 而非最终离散 allocation；低平均 EF loss 不是个体没有严重不公的保证。论文也未表明对策略性报告、长期适应、隐私或主观公平感的效果。
- 复现应公开数据许可/去标识、评分到 disutility 的转换、missingness generator 与 train/test split、MLP/optimizer、τ/λ selection、各 mechanism/surrogate、seeds、EF/PROP/EF1/PROP1 的最终真实-profile评估和 subgroup 分布。

## 与 AAMAS 的关系与核验说明

该工作把可微学习和经典公平分配机制相结合。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HTOP9978.pdf) 核对 §2--4、Eqs. 1--3 和 Table 1，保留 incomplete-preference 与 surrogate 假设，而未将实验性 fairness loss 写成真实公平保证。
