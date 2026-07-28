---
title: "End-to-End Decision-Focused Prediction in Dynamic Bike-Sharing Rebalancing"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "resource_allocation", "applications"]
dblp_key: ""
doi: "10.65109/ITBP8245"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ITBP8245.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_reported_primary_dataset", "omitted_cross_city_results", "mixed_integer_approximation", "baseline_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# End-to-End Decision-Focused Prediction in Dynamic Bike-Sharing Rebalancing

## 一句话总结

PREDICT 将单车需求预测与混合整数调度的实际缺车/满桩损失联合训练；其 Activated Constraint Embedding（ACE）在 Hubway 的 20 个测试情景中优于所列 PTO 与鲁棒基线，但主要报告的跨城市证据被省略，且训练对完整双层 MIP 只是结构化近似。

## 方法与证据

- 单时段下层问题决定每个调度员的站点路径（二元变量）及搬运量（整数变量），满足库存、停靠容量、车辆容量和距离约束，目标是 bike shortage 与 dock overflow 损失之和（§3）。上层预测流量，但以真实流量下的已实现损失而非 MAE/RMSE 训练（式 14–17）。
- ACE 从子问题产生候选整数 routing pattern，对相应 LP relaxation 提取 KKT 条件，并在主问题内以激活变量选择候选；这使学习可计算，但不等价于直接对原始所有整数可行解求导（§4）。为满足 KKT 的线性要求，文中只训练非线性预测器顶端的轻量线性层，底层预测器固定。
- 主实验为 Boston Hubway：95 站、20 位调度员、每人 5 辆容量、50 km 拾取/投放上限，早高峰 6 小时切成 12 个半小时段；60 个工作日需求情景中 40 训练、20 测试（§5.1）。基线是无调度、Poisson+MINLP、TWIST+MINLP 与 scenario-based robust optimization，且 PTO 方案共用 MINLP solver（§5.2）。
- 在该设置中，图 2 显示 ACE 整个规划窗损失最低：相较不调度在 8:00 最多低 56%，相较 Poisson/TWIST+MINLP 各高峰时段至少低 34%，相较鲁棒优化最多低 44%。代价是训练时间约 3050±150 秒（TWIST 为 1214±60 秒），12 段累积决策时间对鲁棒优化最高约 2.8 倍，但文中称每轮低于 35 秒（§5.3）。

## 局限与复现

- 主要表格/图仅给出 Hubway 及 20 个测试情景；作者称在 Ningbo 与 NYC CitiBike 得到一致收益，但明确说结果因篇幅省略，故该主张不能由本文报告的数据独立核验。
- 结果取决于需求情景生成、车辆容量/距离、早高峰时段、预测器冻结方式、候选 routing pool 和 CPLEX 设置。文中没有与可直接处理混合整数下层问题的替代 DFL 方法比较，理由是它们通常假设连续、凸、可微下层。
- 56% 与 34%/44%是不同对照和时段的最大/下界陈述，不应概括成所有城市、全天或真实运营中的固定节省率；作者还承认线性/分段线性嵌入限制模型表达能力（§6）。
- 复现应发布 Hubway 清洗和时间切分、60 个情景、初始库存、路线/距离矩阵、所有超参数与种子、CPLEX 版本/求解容差、候选池演化和逐时段决策；跨城结论需公开被省略的 Ningbo/CitiBike 结果。

## 与 AAMAS 的关系与核验说明

该文将预测和资源重分配的决策质量耦合，服务于城市 mobility 的规划与调度。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ITBP8245.pdf) 核对 MILP、ACE 近似、Hubway 数据切分、对照组和运行时间，未将未展示的扩展数据集结果作为已复现证据。
