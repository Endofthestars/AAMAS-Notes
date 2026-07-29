---
title: "DEpiABS: Differentiable Epidemic Agent-Based Simulator"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "generative_agents"]
dblp_key: ""
doi: "10.65109/IEON9331"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IEON9331.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["public_health_decision_scope", "differentiable_relaxation_bias", "z_score_output_scaling", "limited_regional_validation", "historical_data_generalization", "parameter_identifiability", "intervention_claim_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DEpiABS: Differentiable Epidemic Agent-Based Simulator

## 一句话总结

DEpiABS 是以可微松弛和张量化实现的细粒度流行病 agent-based simulator：它把社会、健康和行为规则写入可反向传播的计算图，以真实疫情序列做梯度校准，并以 z-score 映射小规模模拟输出。在十个马萨诸塞县的历史 COVID-19 死亡数据和州级 ILI 数据上优于或接近 GradABM，但这不足以将其用于实时干预决策或因果政策效果宣称。

## 方法与证据

- 模型由 Society、Epidemic、Population 三部分组成：日尺度的办公室/市场/医院空间、收入和供给机制；含部分免疫与再感染的 SAID 健康状态；以及基于财务、供给、健康和疫情观察的出行/居家/就医等规则（§4）。这些是结构性假设，并非从数据中逐项识别的真实行为机制。
- 为端到端校准，作者将条件规则、周期 modulo 与随机变量改为可微近似：按精度需求使用 ReLU 比例、tanh 或 logistic relaxation，分类变量/相遇关系张量化，并用 reparameterisation 处理随机变量（§5.1）。可微代理会改变离散传播和行为决策的动力学，梯度可用不等于原始 ABM 的精确模拟。
- z-score output scaling 先用模拟输出的均值/标准差标准化，再按真实序列均值/标准差反变换并平移；论文称这允许以较小人口模拟大规模地区，报告结果使用 500-agent simulation（§5.2、§6.2）。该映射直接对齐前两阶统计量，预测趋势仍依赖模型结构与历史数据稳定性。
- 对照为 C-/DC-/JDC-GradABM；沿用其 COVID-19 十个 Massachusetts counties（人口约 70,000--1,600,000）死亡数据与 influenza-like illness 数据、处理方式、长度和指标。COVID 使用 7 个参数，flu 使用 8 个参数，结果为 5 runs（§6.2.1）。
- Table 2：COVID 的 DEpiABS ND/RMSE/MAE 为 \(0.92\pm0.05\)、\(18.95\pm4.39\)、\(12.97\pm2.25\)，JDC-GradABM 为 \(0.97\pm0.18\)、\(50.99\pm12.12\)、\(30.02\pm5.60\)。Flu 的 ND 为 \(0.32\pm0.05\)（JDC 0.41），但 RMSE/MAE 为 \(1.80\pm0.28\)/\(1.47\pm0.23\)，不优于 JDC 的 1.47/1.22；应按各指标分别解读。
- Sobol 分析发现感染输出中传播/相遇参数的总效应至少比其他组高 45%，死亡主要受个体健康参数影响；运行时随模拟人数和预测长度近线性增长，1000 agents、30 steps 约 1.40 秒，论文称比未优化 Mesa 等价实现快 200--250 倍（§6.1--6.3）。这不是在真实公共卫生 IT、数据延迟或政策流程下的端到端时效评估。

## 适用边界与复现

- 适用于研究中比较机制性假设、以历史监测数据校准小规模可微 ABM，或作为流行病学专家审核下的情景分析组件；不适合单独决定封控、疫苗、医院资源或其他会直接影响公众的措施。
- 十个县和一种 ILI 序列的历史拟合不能保证面对新病原体、变异株、监测口径改变、疫苗/治疗变化、人口流动和行为反应时仍可靠；参数可辨识性、预测区间、外部/时间外验证及反事实 intervention 验证均未由本文结果充分确立。
- \(500\) agents 到真实地区的 z-score 缩放保留的是经转换的输出统计特性，不会自动保留接触网络、稀有事件、空间聚集或资源瓶颈；应单独做不同人口规模、网络、报告延迟和极端流行波的稳健性检验。
- 复现需固定社会/空间/经济规则、SAID 转移和所有先验范围、relaxation 的阈值/温度/松弛量、随机重参数化、500-agent 与 scaling 步骤、训练目标/窗口/优化器、十县与 ILI 预处理、C/DC/JDC-GradABM 对照和五个随机种子；报告逐地区时间外误差、置信区间、校准曲线、敏感性/可识别性、资源占用及政策反事实审查。
- 若用于决策支持，须由流行病学和公共卫生主管部门独立校准与审查，预注册情景/不确定性表达，使用多模型集成和人工复核；模型误差、数据缺失和公平影响必须可见，不能把拟合结果当作政策因果效应。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的机制性多主体仿真与可微校准工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IEON9331.pdf) 核验模型结构、可微近似、缩放、数据范围、Table 2 和性能测试；没有把历史预测误差改写成经验证的干预政策建议或公共卫生安全保证。
