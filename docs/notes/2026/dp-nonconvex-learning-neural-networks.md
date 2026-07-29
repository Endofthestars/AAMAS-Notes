---
title: "Differentially Private Non-convex Learning: From Generalized Linear Models to Multi-layer Neural Networks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "generative_agents", "unclassified"]
dblp_key: ""
doi: "10.65109/JRBH5415"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JRBH5415.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "epsilon_delta_dp_scope", "well_specified_model_assumptions", "single_output_fully_connected_networks", "ntk_large_width_regime"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Differentially Private Non-convex Learning: From Generalized Linear Models to Multi-layer Neural Networks

## 一句话总结

本文研究单输出 fully connected neural networks 的 \((\epsilon,\delta)\)-DP non-convex stochastic optimization，以 excess population risk 而非仅 gradient norm 衡量效用：对 well-specified GLM 的 bounded/Lipschitz link 和 ReLU、以及两层 sigmoid/ReLU 网络给出 private learning 结果，并借助 Neural Tangent Kernel 为足够宽、样本足够大的多层 projected DP‑SGD 给 excess-risk bound。它说明特定结构/分布/宽度区间的理论可行性，不证明普通深度模型、任意训练配置或真实数据端到端“私密且有用”。

## 方法与证据

- DP 定义为对相差一个 record 的邻接 datasets，任意 output event 满足 \(\Pr[A(D)\in S]\le e^\epsilon\Pr[A(D')\in S]+\delta\)（Definition 1.1）。本文的 utility 是 expected excess population risk \(\mathbb E L_P(w^{priv})-\min_wL_P(w)\)（Definition 1.2），不是 membership-inference 测试、信息泄露实测、group privacy、federated privacy、secure aggregation、fairness或合规证明。
- GLM well-specified setup 假定 i.i.d. \((x,y)\)、零均值 noise、\(\mathbb E[y|x]=\sigma(\langle w^*,x\rangle)\)，先处理 bounded且Lipschitz link，后处理 ReLU（§2）。这排除 model misspecification、heavy-tailed/shifted/adversarial data、unknown/biased labels、non-i.i.d. samples 和任意 output/network architectures；dimension-invariant wording亦受 expected data-matrix rank \(\theta\) 等条件约束。
- 对 bounded link，文中给 \(\tilde O(1/\sqrt n+\min\{1/(n\epsilon)^{2/3},1/(n\epsilon\theta)\})\) 型 excess-risk upper bound；ReLU 给相近但含 \(d\) 的项，并扩展思路到 well-specified 两层 sigmoid/ReLU networks（§2）。这些符号上界的常数、log factors、constraint/radius、privacy accounting和算法步骤在 3 页文稿未完整给出，需以 full version 验证，不能据此比较任意实践设置的实际 loss。
- 对 misspecified ReLU regression，作者提出另一 DP gradient-descent version，样本复杂度为 \(\tilde O(\max\{\sqrt d/(\epsilon\alpha^d),\alpha^{-d^2}\})\) 的表述，保证 population risk 相对 \(c\cdot opt\) 的误差不超过 \(\alpha\)（§2）。这显示 misspecification 处理仍有强维度/近似依赖；不应省略这些条件而称一般 non-convex DP risk dimension-free。
- 多层部分研究 Abadi et al. 的 projected DP‑SGD，利用 NTK 给“各层 sufficiently large width 且 n sufficiently large”时的 excess population risk bound（式 2），由 convergence/sampling、NTK approximation、每 iteration Gaussian-noise privacy error 三项构成（§2）。没有给 applicable depth/width/data scaling、clipping/noise/iterations具体选择、privacy budget accounting、empirical datasets/attack evaluation/benchmark comparison；实验仅称 corroborate theoretical findings。

## 适用边界与复现

- 适合 DP learning 理论与受限模型实验中分析 privacy–utility trade-off，或作为选择 DP-SGD parameters 的理论参考；不应直接把本文当作医疗、金融、基因或用户数据可以任意上传/训练/发布的授权，亦不应以 DP 标签替代访问控制、最小化收集和风险评估。
- 复现需取得完整 algorithm/pseudocode、邻接定义（add/remove或replace）、\(\epsilon,\delta\) accountant、sampling/clipping/noise schedule、projection set、loss/feature norms、link/network initialization/width/depth、\(\theta,R,L,S,m,T\)及各隐藏条件。分别检验 GLM well-specified/ReLU/misspecified/two-layer/NTK multi-layer regime，用独立 privacy accountant验证 budget并计算 population/empirical risk、runtime/memory与bound terms。
- 应比较 vanilla DP-SGD、projected variants和non-private baselines，在真实与合成 data 上报告 calibration/accuracy/robustness、privacy budget sensitivity、clip/noise/steps/width/depth trade-off、membership-inference empirical risk、distribution shift、rare group performance和failure cases。测试更深/更窄模型、multi-output/multiclass、non-i.i.d./misspecified/heavy-tail data与long training，而非只展示适用 NTK regime。
- 生产系统还需 data provenance/consent、purpose limitation、retention/deletion、access and key management、secure execution、model release review、privacy accountant ledger、independent audit与incident response。\((\epsilon,\delta)\)-DP是可量化的统计邻接保护而非零泄露承诺；\(\epsilon\)、\(\delta\)、sampling以及发布的模型/metrics必须向治理方明确披露。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的差分隐私非凸优化与神经网络理论 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JRBH5415.pdf) 核验 \((\epsilon,\delta)\)-DP 和 excess-risk 定义、well-specified GLM/ReLU/两层设置、misspecified ReLU、以及 NTK 下多层 projected DP‑SGD 的三项 bound；没有将条件性理论结果写成任何神经网络的隐私、实用效能或综合数据治理保证。
