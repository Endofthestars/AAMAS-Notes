---
title: "DEMamba: Decoupled Enhanced State Space Models with Selective Mechanisms for Multivariate Time Series Forecasting"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "unclassified"]
dblp_key: ""
doi: "10.65109/UIXP4140"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UIXP4140.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02h"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["benchmark_forecasting_scope", "limited_baseline_comparison", "no_multiagent_evaluation", "traffic_dataset_exception"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DEMamba: Decoupled Enhanced State Space Models with Selective Mechanisms for Multivariate Time Series Forecasting

## 一句话总结

DEMamba 是多变量时间序列预测模型：用 patch tokens、1D convolution 建模时间依赖、双向 selective SSM（S6）建模变量间依赖，并以 FFN 捕获 patch 内特征关系；在八个公开基准上与 MambaTS、iTransformer 比较。

## 方法与证据

- 输入经 Instance Normalization 和 patch embedding 得到 `H∈R^(V×P×D)`，通过 n 层 encoder。每层 TVDS Mamba block 将 temporal 与 cross-variate scan 显式解耦：1D convolution 处理前者，双向 S6 处理非因果的变量维关系（§2、Figure 1）。
- 评测数据为 ETTh1/2、ETTm1/2、Weather、ECL、Traffic、Exchange；lookback 固定 96，Exchange 的 horizons 为 12/24/48/96，其余为 96/192/336/720，指标为 MSE/MAE（§3.1）。
- Table 1 仅比较 DEMamba、MambaTS、iTransformer。DEMamba 在 7/8 个数据集的平均 MSE/MAE 最佳；例如 ECL 平均 MSE/MAE 为 0.164/0.262。但 Traffic 上 MambaTS 为 0.422/0.276，优于 DEMamba 的 0.477/0.295（§3.2）。
- 论文称模型因分离扫描而更稳健；扩展摘要未包含参数量、训练/推理耗时、消融、方差、统计检验或更广泛 baselines，因此准确性与效率的总体优越性只能限于所列设置。

## 适用边界与复现

- 这是监督式 MTSF benchmark 工作；尽管发表于 AAMAS，本文未评估 agents、协作、决策闭环或多智能体环境，预测分数不能代表多智能体系统效果。
- 固定 lookback/horizon、归一化、patch size、变量顺序、数据切分和缺失值处理均可能影响结果；Traffic 的反例说明不能宣称跨数据集完全占优。
- 时间序列预测误差不等于用于能源、交通、金融或医疗运营时的风险/收益；此类场景需要不确定性校准、分布漂移、因果约束与领域安全验证。
- 复现应固定八数据集版本与 splits、预处理/InstanceNorm、patch/embedding/层数、S6/conv/FFN 参数、训练预算/seed、每 horizon 的完整表格及 runtime/parameter counts，并与更多近期 MTSF baselines 公平比较。

## 与 AAMAS 的关系与核验说明

该工作将选择性状态空间模型用于预测组件。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UIXP4140.pdf) 核对 §2--3、Figure 1 和 Table 1，并保留 Traffic 数据集上的性能例外。
