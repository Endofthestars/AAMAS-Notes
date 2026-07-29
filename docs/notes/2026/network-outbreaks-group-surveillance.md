---
title: "Reconstructing Network Outbreaks under Group Surveillance"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "safety_verification", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/VRPM5709"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VRPM5709.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["independent_cascade_assumption", "pooled_test_noise", "network_data_quality", "mle_nonidentifiability", "synthetic_cascade_evaluation", "sensitive_health_network_data", "no_clinical_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Reconstructing Network Outbreaks under Group Surveillance

## 一句话总结

论文提出 PoolCascadeMLE：在网络传播与 group/pool surveillance 的正负结果下，寻找与测试一致、似然最大的感染 cascade。正 pool 只要求选至少一个感染节点，负 pool 排除所有节点，因此比逐人检测多一层组合选择；作者将多跳问题归约到 Group Steiner Tree、单跳问题用 LP 随机舍入，在合成级联上优于把 pool 强行缩为单点的基线。它是依赖网络和 IC 模型的离线推断，不是对个体感染的临床确诊。

## 方法与证据

- 在无向网络上采用 Independent Cascade（离散 SIR）模型。单种子版本给定 root；每个 pool 阳性表示至少一节点在 cascade 中，阴性表示其节点均不可出现。目标由成功/失败传播概率的负对数构成 MLE cost（§3.1）。
- PoolCascadeMLE 在 \(k=|\Gamma_1|\) 个阳性组下难以近似到 \(O(\log^{2-\epsilon}k)\) 内（除非 P=NP）；作者在 \(p_e\le 1/2\) 时证明最优解可取 tree，将节点/边权构造成 Group Steiner Tree，再经 directed Steiner tree 得 ApproxCascade 的 \(O(k^\epsilon)\) 近似与 \(O(n^2+kn^{1/\epsilon})\) 时间（Theorems 1、3、§5.1）。
- one-hop 版本允许未知多个 seed 只传播一步，也为 NP-hard 且难以 \(O(\log k)\) 近似。其 LP relaxation + independent randomized rounding 的 RoundCascade 有 \((2+2\ln k)\) 近似保证；这属于简化的一跳传播/给定分区模型（Theorems 2、4、§3.2、§5.2）。
- 评估网络包括 BA、\(G(1000,0.02)\)、由 2018-01-01 至 01-08 UVA Hospital ICU EHR 构建的接触网络，以及 Virginia digital-twin small-city 子图。传播与感染是实验生成；F1 和 prevalence error 在 50 个 replicate 上平均（§6.1）。
- ApproxCascade 在所示 diffusion probability、pool size 与 pool ratio 上通常优于 ApproxCascade-Random 和 ApproxCascade-All（均将 pool 退化为单点）；RoundCascade 也在 missing-infection recovery 上优于随机基线（Figs. 2--4）。这些是相对模拟精度，未校准为病例检出率或公共卫生效益。
- 作者展示 pool 的合并会使 MLE 选择与 ground truth 不同的更低成本树；在测试噪声下，构造例可使 NoisyPoolCascadeMLE 与 ground truth 仅有 \(o(n)\) overlap。重叠 pool 可改善推断，但这个现象也说明结果对测试设计/噪声高度敏感（§7）。

## 适用边界与复现

- 可用于研究性的暴发态势估计、废水/气溶胶等 group surveillance 的候选网络假设排序，前提是 pool 成员、接触图、传播参数和检测误差都能审计地获得。
- 不应据此指认个人、实施隔离或医疗决策：pool 阳性本身不识别感染者，contact graph 和 IC 假设可错，噪声与多个等价 cascade 会造成严重非识别性，且 ICU 网络涉及敏感健康数据。
- 复现应固定网络与访问治理、pool 生成/重叠规则、seed、edge \(p_e\)、测试误差、正负 outcome、\(\epsilon\)/Steiner solver、LP/rounding 次数和 50 次 replicates；分别报告 F1、prevalence error、假阳/假阴、运行时和不确定性区间。
- 实际公共卫生使用需与流行病学家共同进行前瞻验证，结合个体确证检测、隐私保护/最小化、置信度与多模型敏感性分析，并将模型输出限制为资源分配的辅助信号而非个体归因。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的网络传播、组合优化与群体监测推断论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VRPM5709.pdf) 核验 Pool/One-Hop 定义、Theorems 1--4、Group Steiner 与 LP rounding、数据集/50 replicates 和噪声局限；没有把合成接触网络上的重建性能表述为真实疫情诊断效能。
