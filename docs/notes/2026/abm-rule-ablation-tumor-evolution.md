---
title: "Identifying Essential Rule Sets in Agent-Based Models Through Systematic Ablation: A Tumor Evolution Case Study"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/OQYW6891"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OQYW6891.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_tumor_model", "output_metric_dependence", "30_day_horizon", "parameter_regime_dependence", "diffusion_framework_requirement", "no_clinical_validation", "ablation_not_causal_biology_proof"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Identifying Essential Rule Sets in Agent-Based Models Through Systematic Ablation: A Tumor Evolution Case Study

## 一句话总结

论文提出针对 ABM 规则集的系统化消融流程：用 full-model 的重复随机运行建立模式指纹的基线变异，再以 Sliced Wasserstein（SW）距离、bootstrap 与非参数检验把删除规则后的差异归为 auxiliary/intermediate/core。案例是含细胞 agent 与药物/营养反应扩散 PDE 的 3D 肿瘤模型；在其 30 天、特定参数与组织尺度指标下，三项生物机制被归为 essential，R7–R10 可同时删去而模式统计上仍近似 baseline。去掉 spatial diffusion 却引发群体爆炸，作者将其作为不可消融的物理框架要求而非生物假设。结论是该模型/指标/时间窗下的结构诊断，不是肿瘤机制的临床因果证明。

## 方法与证据

- 混合模型以 3D cancer cell agents 与 drug/nutrient reaction-diffusion fields 耦合；细胞有 75 维内部状态和敏感/tolerant/resistant/immune phenotype，模拟十项规则：营养增殖、药物死亡、转变、扩散、paracrine、迁移、contact inhibition、代谢竞争、immune surveillance、cooperative resistance（§3.1）。
- 输出指纹聚合 population、空间 clustering/Ripley/Morisita、persistent homology、phenotype entropy、图聚类等组织尺度特征，并比较完整与 ablated model 的 pattern distribution（§3.3–3.4）。某规则“essential”取决于这些特征与 30-day horizon；分子/长期/临床终点可能得不同排序。
- 50 baseline replicates 随机分为两个各 25 的样本、用 500 projections 计算 SW；基线均值 0.364，95% range 0.29–0.44，作者设 auxiliary <0.402、intermediate 0.402–0.478、core >0.478，并以 1,000 bootstrap、Mann–Whitney/Kruskal–Wallis 与 Bonferroni 评估（§3.4、§4.2）。这给的是内部仿真的经验阈值，不是跨模型通用显著性标准。
- 移除 R4 spatial diffusion（M4）使平均终末 population 从 1,184 到 27,591、78% runs 超过 10,000 cells，违反模型所需的物理/质量约束；故作者从后续 pattern comparison 排除 M4（§4.1）。这说明消融首先要区分 framework requirement 与可检验 behavioral mechanism。
- 结果报告 R7–R10 同时移除的 minimal model M22（删 40% rules）SW=0.367、\(p=0.132\)，仍在 auxiliary threshold 内；其运行只快约 4.8%，因为被删规则只占约 7.3% agent time（§4.6）。可解释性/参数维度改善不必然转化为大计算加速。
- 作者也说明其他机制在不同 parameter regime、不同观察尺度、强免疫浸润/强 cooperation 或 90+ 天更长时间可能变 essential（§4–5）。因而“不重要”不是生物学上的永恒否定。

## 适用边界与复现

- 适用于带随机性的 ABM 模型约简：先定义与研究目标对齐的观测指纹，再基于 full-model stochastic variability 校准 rule-removal 的阈值。
- 不应将模拟消融用于直接决定肿瘤治疗或宣称某机制不真实；应由实验/临床数据、外部验证、parameter uncertainty、alternative model structures和更长尺度追踪来交叉检验。
- 复现需固定 PDE grid/solver/timestep、cell rules/parameters、initialization/seeds、run horizon、feature extraction、normalization、SW projections、baseline split/bootstrap/多重检验和 rule-removal variants；报告所有原始特征、失败 run 与运行成本。
- 后续可使用组合/交互消融、global sensitivity、Bayesian calibration、out-of-sample tissue data、多个病程窗口与可被实验反驳的预测；也应将 framework sanity checks 独立于 hypothesis ablations。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 agent-based simulation、模型约简与肿瘤演化工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OQYW6891.pdf) 核验十项规则、基线阈值校准、M4 扩散失败、M22 minimal model 和作者列出的尺度/参数限制；没有将组织尺度仿真中“auxiliary”规则误写为临床上不重要或因果无效。
