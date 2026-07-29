---
title: "Functional Multi-armed Bandit and the Best Function Identification Problems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "resource_allocation", "agent_engineering"]
dblp_key: ""
doi: "10.65109/SFMN9947"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SFMN9947.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["convergence_certificate_requirement", "optimizer_oracle_assumptions", "deterministic_stochastic_model_scope", "synthetic_and_model_selection_benchmarks", "heuristic_neural_network_bound", "finite_budget_identification", "no_general_black_box_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Functional Multi-armed Bandit and the Best Function Identification Problems

## 一句话总结

论文把多个候选优化问题/模型视为 arms，并以各自优化器的已知收敛界构造 lower-confidence bound（F-LCB），从而分配迭代预算以最小化累计优化遗憾（FMAB）或找出最优函数（BFI）。其下界与上界在特定优化类中相差对数因子；但方法必须预先有可用的收敛置信界并能观测目标值，神经网络选择实验的界是启发式的，不能视为通用黑盒模型选择保证。

## 方法与证据

- FMAB 的 arm 是候选优化问题 (P_i=(f_i,X_i,O_i))，每次 pull 对该问题的基优化器多执行一次；BFI 则在总预算后识别最小最优值对应的函数（§3）。这不是直接在动作空间抽样的普通 bandit，也不自动处理任意不可观测训练过程。
- Theorems 3.1--3.2 给出 BFI 与 FMAB 的 minimax lower bounds；同质问题时，凸 Lipschitz、光滑凸、强凸等类分别导出相应的预算—遗憾量级（§3）。这些结论是存在最难实例的类级下界，不是任意一组实际模型的性能预测。
- Algorithm 1 的 F-LCB 初始化每个 arm 一次，并反复选择 (f_i(x_i^{k_i})-g_i(k_i,\delta)) 最小者，其中 (g_i) 是基优化算法的确定性收敛界或高概率界（§4）。因此它用优化误差界同时充当乐观估计和资源分配信号；不同 arm 可使用不同优化器。
- Theorem 4.3 对 (g_i(k)=\beta_i k^{-r}) 给出确定性 FMAB regret：当 (0<r<1) 随预算的 (1-r) 次幂增长、(r=1) 为对数增长、(r>1) 有界；Theorem 4.4 给出确定性 BFI 的停止/预算保证。随机情形以 clean event、置信参数和额外假设推导上界（§4.1--4.2、Table 2）；这些定理依赖正确的 (g_i)、oracle 模型和函数类。
- 实验覆盖凸光滑/非光滑合成函数、带 inexact first-order oracle 的光滑凸函数，以及 CIFAR-100 的神经网络架构选择（§5）。作者公开了复现实验的代码仓库；合成实验主要说明在受控的优化假设下能集中预算到较优函数，不能覆盖非平稳数据或部署资源约束。
- CIFAR-100 以单张 P100 GPU 训练 10 个少于 5M 参数的模型；每个 pull 为 40 次参数更新。Table 4 的 10 次重复显示：预算 50 时 F-LCB 的平均选中模型 rank 为 (2.2\pm2.7)，优于 Hyperband (4.6\pm2.7)、Successive Halving (2.5\pm0.9)；预算 100 时为 (1.1\pm0.3)，350 及以上与 SH 都为 (1.0\pm0.0)。这只衡量给定候选集的 validation-loss rank，未报告显著性检验、跨数据集或总墙钟开销。
- 对非凸 NN 训练，论文承认理论收敛保证不直接适用，并以 (g(t)=2f(x_{1,i})/\sqrt{t}) 启发式定义界、取训练至今的最佳 validation loss 来算 LCB（§5.4）。因此该实验是可行性比较，不构成由理论推导出的神经网络选择 guarantee。

## 适用边界与复现

- 适用于每个候选优化任务都能运行一步（或一个可计量单元）基优化器、观察目标/近似目标，并获得可信 (g_i(k,\delta)) 的有限计算预算资源分配。它适合优化算法组合、受控 hyperparameter/model selection 的研究，不应被包装为无调参的 AutoML 或自治决策器。
- 收敛界若不正确、过松或不可比，LCB 排序会失真；随机 oracle 还依赖采样、置信参数与 clean-event 假设。非凸训练、早停、数据漂移、指标噪声、异构每步成本和不可见真实目标都会破坏其解释。
- 论文的网络实验用 validation loss 选择模型，未评估测试集泄漏、数据/模型治理、鲁棒性、公平性、能耗、并行调度、候选集扩张或真实生产工作流。小预算排名改善不等于模型质量、泛化、安全性或部署收益提升。
- 复现需固定每个 (f_i,X_i,O_i)、基优化器与初值、收敛界/置信参数、每个 pull 的计算单位、总预算与停止阈值；分别复现 deterministic/inexact-oracle synthetic cases。NN 实验还需固定 CIFAR-100 split、10 个候选模型/权重、P100 或等价环境、每 pull 40 updates、validation protocol、启发式 (g)、Hyperband/SH 配置与 10 个随机重复，并报告每 arm 的实际成本、loss 曲线、rank 分布和失败情况。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的资源分配、bandit 式优化调度与 best-function identification 论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SFMN9947.pdf) 核验 FMAB/BFI 定义、Theorems 3.1--3.2 与 4.3--4.4、Algorithm 1、Table 4、实验协议和作者列出的限制；没有把特定函数类的 regret 保证或启发式 NN 实验误写为一般黑盒模型选择、深度网络收敛或生产决策保证。
