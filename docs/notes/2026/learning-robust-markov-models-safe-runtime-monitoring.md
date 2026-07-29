---
title: "Learning Robust Markov Models for Safe Runtime Monitoring"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/JAKK2294"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JAKK2294.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["model_structure_knowledge_requirement", "state_space_specification", "asymptotic_convergence_only", "coarse_model_guarantee_gap", "false_negative_residual", "benchmark_simulation_scope", "runtime_cost"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Learning Robust Markov Models for Safe Runtime Monitoring

## 一句话总结

论文从系统路径学习 interval HMM（iHMM），以所有与区间模型一致 HMM 中的最大条件违规风险形成谨慎运行时监控器，并用 conformance-testing 导向采样收紧风险区间。理论保证依赖真实 HMM 的状态/转移空间已知且样本趋于无穷；粗粒度状态模型不享有该保证，实验也出现风险低估，故它不是可直接替代独立安全论证的运行时安全认证器。

## 方法与证据

- 系统同时有随机动态和噪声观测，安全规格是有限线性时序性质；理想监控器对观测 trace 计算未来 horizon 内违规的条件概率。论文将“谨慎”定义为任意 trace 上不低于理想监控器的风险估计（§2--3）。这只是风险报警量，不包含控制器如何纠正或保证避免事故。
- iHMM 为转移/初始概率维护区间；监控值在所有 refine 该 iHMM 的 HMM 中取最大风险。Lemma 2 说明若真实 HMM refine 该 iHMM，则监控器谨慎；Theorem 1 将该判定化为 iHMM/MDP 上的最大有界可达性，阈值决策可多项式计算（§3）。谨慎性取决于真实系统仍在模型不确定性集合内。
- 学习使用 LUI：依据路径频率更新概率与 strength intervals，并假设状态空间和可行转移由领域知识给定。Theorem 2 表明在 iHMM 与真实 HMM 状态空间相同、总处理路径数趋于无穷时，区间收敛到精确概率；Corollary 1 相应收敛到 ideal monitor（§4.1）。这是渐近、正确模型结构的结果，不给有限样本的误报/漏报上界。
- refinement 对风险区间宽于阈值的 trace 邻域重采样；Corollary 2 在相同状态空间且 \(\theta=0\) 时保留上述极限收敛。它改善样本分配而非克服未建模状态、传感器偏差或规范错误（§4.2）。
- 评估含 airport（飞机降落与地面车辆）、evadeV（两机器人）、Snakes-and-Ladders 等 reachability 模型，并比较 SGD regression、conformal prediction、普通 HMM 和无 refinement iHMM。每个方法/benchmark 10 次；多数测试 500 traces，两个最大 airport 模型只测试 200，airportB-7-40-20 在 12 小时内未完成并被省略（§5.1）。
- 作者报告 iHMM 通常更保守、FNR 更低且 refinement 在部分 benchmark 更省样本；但 coarse SnL-10x10 出现 iHMM 风险低估，且最大 benchmark 的输出都远离 ideal monitor，作者避免作强结论（§5.2--5.5）。例如 evadeV-6-3 (SC=0.1) 的学习约 110 s（refinement）或 220 s（无 refinement），单 trace iHMM 风险估计约 20 ms，均说明实时可用性仍需按系统规模验证。

## 适用边界与复现

- 适用于可离散化、可从模拟器或受控系统取得路径、并能以领域知识指定相关状态变量与可行转移的有限 horizon 风险监控研究。部署前必须独立核验模型覆盖范围、规格、报警阈值与 fail-safe 执行链路。
- 不适用于未知/持续变化拓扑、严重 distribution shift、连续高维感知直接输入或无法建模的学习组件；LUI 的收敛条件在 coarse models 不成立。即使估计谨慎，也可能因规格遗漏、观测延迟或真实系统不在 interval family 内而漏报。
- FNR/FPR 相对 ideal monitor 的结果来自模拟 benchmark，不是物理飞机或机器人事故率。模型比较的训练数据、GPU/CPU、超时和测试 trace 数不同，不能将图中优势概括为所有 model-free 方法或所有安全系统的胜出。
- 复现应固定系统/观测变量、状态与转移空间、HMM/iHMM 初始 intervals 与 strengths、规格、horizon、SC/\(\theta\)、采样与 refinement 邻域、model-checker 版本和随机种子；分别报告 FNR、FPR、risk-interval width、对 ideal 的距离、每 trace 延迟、内存、未完成实验及风险低估实例。真实部署还应做故障注入、OOD/传感噪声测试、独立安全审查和人工接管验证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的不确定性下运行时验证与安全监控论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JAKK2294.pdf) 核验 iHMM 风险语义、Lemma 2、Theorems 1--2、Corollaries 1--2、benchmark/超时设置和 coarse-model 限制；没有把渐近模型内谨慎性或模拟指标误写为现实系统的事故预防或端到端安全保证。
