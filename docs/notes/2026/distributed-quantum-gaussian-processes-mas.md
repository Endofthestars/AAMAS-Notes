---
title: "Distributed Quantum Gaussian Processes for Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/ADPL7324"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ADPL7324.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["quantum_simulator_on_classical_hardware", "no_nisq_complexity_benchmark", "local_dataset_independence_assumption", "nonconvex_stationary_point_guarantee", "elevation_and_synthetic_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Distributed Quantum Gaussian Processes for Multi-Agent Systems

## 一句话总结

DQGP 让多个 agent 在各自数据分区训练 projected quantum-kernel Gaussian Process，并以 torus manifold 上的 distributed Riemannian ADMM 聚合为 consensus hyperparameters；它在 NASA SRTM elevation 与合成 QGP 数据上的经典量子模拟器实验中通常优于两个 classical distributed GP baseline，但没有在量子硬件上测量复杂度或实现 quantum advantage。

## 方法与证据

- 经典 GP 训练需 (O(N^3)) 时间与 (O(N^2)) 级存储；分布式 GP 将数据分给 (M) 个 agent、分别训练 local model 并聚合，论文假定各 local datasets 代表不同区域且 local models statistically independent（Assumption 1、§2.4）。
- quantum kernel 用 parameterized encoding circuit 将 classical input 送入 Hilbert space。作者采用 Projected Quantum Kernel（PQK）：量子状态先由 observable expectation 映射为 classical features，再施加 outer kernel，以避免 fidelity kernel 的 (O(2^q)) state-overlap 代价（§3.2.1--3.2.2）。
- 因 rotational circuit parameters 位于 (T^P=S^1\times\cdots\times S^1)，DR-ADMM 在 torus 上以 projection/retraction/log map 和 parameter-shift gradient 执行 local update、central Karcher/circular-mean aggregation 与 dual update，强制各 agent 的 (\theta_m=z) consensus（§3.1、Algorithm 1）。
- Theorem 1 在 local QGP negative log-likelihood (L_p)-smooth、投影和梯度有界、penalty (\rho) 足够大等假设下，证明 DR-ADMM 收敛到满足 KKT 的 stationary point，primal/dual residual 消失，收敛率为 sublinear (O(1/S))；这不是 nonconvex global optimum 保证（Theorem 1）。
- 评测使用四个 NASA SRTM non-stationary elevation tiles（二维经纬度输入、elevation 输出）和从 QGP prior 采样的合成数据，(N=500,5000)，20 次重复，比较 Full-GP、FACT-GP、apxGP，以 NLPD/NRMSE 为指标（§4）。
- 汇总 SRTM 结果中，论文报告 DQGP 相比 FACT-GP/apxGP 的 NRMSE 下降 51.1%±17.8%/65.2%±16.1%；也承认在部分 (N=5000) 数据集 FACT-GP 的 NLPD 更低，原因是其 block-diagonal posterior 近似的不确定性估计更稳定。合成 QGP data 对 DQGP 更有利，因生成分布本身使用 quantum kernels（§4--5）。

## 安全边界与复现

- 所有数值结果来自 Qiskit/PennyLane 的 classical quantum state-vector simulators 和 sQUlearn；论文明确说 simulator 上的 complexity 不代表 current NISQ hardware，因此未做 quantum-hardware complexity analysis。预测精度表格不能支持“已实现量子加速”“quantum supremacy”或实际多 QPU scalability 的结论。
- 分布式收益依赖 local data independence、中心 server push-pull consensus、可靠通信及完整 local gradients。现实多机器人/传感网络往往有 overlapping/non-IID data、漂移、缺失、延迟、bandwidth/隐私限制、异步或 Byzantine participant；这些并未被 theorem 或实验覆盖。
- Theorem 1 给出在平滑/有界和足够大 penalty 下到 stationary KKT point 的收敛，不保证 quantum circuit training 避开 barren plateau、到达全局最优或在噪声量子硬件上维持性能。NISQ measurement noise、shots、gate errors、compilation/connectivity 和 distributed quantum communication 成本均未实测。
- SRTM elevation regression 与 synthetic QGP 不是端到端 autonomous decision/control 评估。GP uncertainty 质量（NLPD）会影响下游探索/安全决策，且部分大样本数据上 DQGP 可能比 FACT-GP 更保守；不得将 NRMSE 改善外推为机器人、环境监测或高风险任务可靠性。
- 复现应固定 SRTM tiles/splits、normalization、Chebyshev/Hubregtsen circuits、qubits/layers/observables、outer kernels、(\delta,\rho,L)、agent partitions、ADMM stopping/consensus protocol、simulator versions/shots（若迁移硬件）、20 replications 与 NLPD/NRMSE。硬件实验还必须报告 wall-clock、queue/communication、noise mitigation、energy/cost和同精度 classical baseline。

## 与 AAMAS 的关系与核验说明

这是 quantum-kernel GP、分布式优化与多 agent consensus 建模工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ADPL7324.pdf) 核对 DQGP、DR-ADMM、Theorem 1、SRTM/合成设置、Table 1--2 与 simulator disclosure；没有将模拟器性能表述为量子硬件速度优势或真实自主系统效能。
