---
title: "Accelerated Adaptive Decision Making for Autonomous Agents: Optimization and Coverage"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["planning_scheduling", "agent_engineering", "applications", "resource_allocation"]
dblp_key: ""
doi: "10.65109/ARNT2761"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ARNT2761.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05f"
spark_draft_verdict: "source_grounded_draft_needs_mathematical_revision"
spark_qa_verdict: "needs_revision_ocr_regret_formula_corrected_from_pdf"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_dissertation_summary", "expensive_black_box_evaluations", "quantum_regret_bound", "ocr_math_formula_risk", "theorem_assumptions_and_proof_omitted", "query_complexity_not_wall_clock_speedup", "multiobjective_coverage", "prior_work_empirical_summary", "objective_threshold_not_real_world_safety", "multiagent_and_graph_extensions_future_work", "no_self_driving_lab_deployment"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_quantum_regret_formula_theorem_attribution_empirical_safety_and_future_multiagent_boundary_check"
escalation_verdict: "pass_after_visual_pdf_formula_verification_and_query_runtime_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra visual formula and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Accelerated Adaptive Decision Making for Autonomous Agents: Optimization and Coverage

## 一句话总结

这篇 Doctoral Consortium 文稿把有限 black-box evaluation budget 下的科学发现概括为两条已有进展：Q-NLB-UCB 的 input-dimension-free quantum regret bound，以及 MOC-CAS 的 constrained objective-space coverage；三页稿没有展开前者的完整定理证明或后者的实验表，量子 query/regret 改进不等于端到端硬件加速，batch/multi-agent、graph/GNN 与 self-driving-lab 均仍是未来方向。

## Dissertation 范围

文稿关注 autonomous agents 与 expensive black-box evaluators 交互的 sequential decision making。agent 在严格 evaluation budget 下反复选择 experiment/candidate、观察 noisy outcome、更新 beliefs，并在 exploration–exploitation 与 objective-space feasibility constraints 之间权衡（§§1–2，p. 4029）。

dissertation 目前汇总两条 progress-to-date：

1. quantum computing-accelerated nonlinear bandit optimization；
2. constrained multi-objective outcome-space coverage。

## Q-NLB-UCB 的作者报告结果

文稿先把 classical noisy bandit cumulative regret 下界

\[
\Omega(\sqrt T)
\]

归于 [14]，再把既有 quantum work 的

\[
O(\operatorname{poly}\log T)
\]

上界归于 [1,5,17]，其中 \(T\) 是 function evaluations 数量。

对于 Quantum Non-Linear Bandit with Upper Confidence Bound（Q-NLB-UCB），该 DC 稿转述 [15] 的作者结果：

\[
O\!\left(
d_w^2\log_2^{3/2}(T)\log(d_w\log T)
\right),
\]

其中 \(d_w\) 是 parameter complexity；文稿称该 regret bound 独立于 input dimension \(d_x\)。这一数学式由 PDF p. 4030 原始排版视觉核对，避免了文本抽取把 \(\sqrt T\) 和对数指数读错。

作者列出的算法构件包括 quantum Monte Carlo mean estimator、parametric function approximation 和新的 quantum nonlinear regression oracle。三页 DC 稿没有给 [15] 的完整 assumptions、正式 theorem statement、proof、oracle cost model、circuit depth、noise model 或硬件实验。

因此，“input-dimension-free”只说明这个被报告的 bound 没有显式依赖 \(d_x\)，仍依赖 parameter complexity \(d_w\) 和其他未在短稿展开的条件；它不证明任意高维任务都实用，也不等于更低 total computation、wall-clock speedup 或已经实现 quantum-hardware advantage。

## Multi-Objective Coverage

另一条进展不是寻找单一 optimum 或只逼近 Pareto front，而是在每个 objective 有 threshold 的约束下，选择少量 representative candidates，使其 predicted outcomes 广泛覆盖 feasible multi-objective output region（§3.2，p. 4030）。

文稿将 MOC 与以下目标区分：

- sample space 中的 constraint active search；
- 以 Pareto frontier 为中心的 multi-objective optimization。

Figure 1 是两 objective 的概念示例：\(\tau_1,\tau_2\) 定义浅绿色 feasible region，15 个 representative feasible samples 各有半径 \(r\) 的 coverage ball。它不是实验结果图。

## MOC-CAS

Multi-Objective Coverage via Constraint Active Search（MOC-CAS）使用 Gaussian-process posterior predictions，并按 candidate 预计新增覆盖的 feasible volume 的 optimistic estimate 进行选择；当候选得分需要区分时，tie-breaking 通过鼓励 predicted objective values 的 dispersion 促进 diversity。

作者报告 MOC-CAS 相对 competitive baselines 在 SARS-CoV-2 与 cancer 的 large-scale protein-target datasets 上表现更好，数据语境指向 [10]，每个任务使用 five objectives derived from SMILES-based features 的说法指向 [16]。

当前 DC 稿没有给 dataset size、candidate split、baseline 名称和结果表、metric values、variance、statistical significance、GP hyperparameters、预算、代码或复现实验协议。“superior performances”只能作为该稿对 [16] 进展的汇总，不能独立复核。

仓库另有 AAMAS research paper `XTVI9400` 的[独立 MOC-CAS 笔记](./moc-cas-multiobjective-coverage.md)。本 DC 笔记只使用 `ARNT2761` 中出现的摘要粒度，没有把完整论文的实验数字或算法细节倒灌进来。

## Feasibility 不是现实安全

本文中的 feasible/safe set 由 objective space 的 per-objective thresholds 定义。这类 surrogate/predicted feasibility 不能自动升级为：

- 生物或临床安全；
- 分子可合成性和真实活性；
- wet-lab 或人员安全；
- regulatory compliance 或 deployment safety。

文稿也没有 wet-lab validation、真实 materials/drug discovery outcome 或闭环 laboratory deployment。

## Future Research Questions

§4（p. 4030）列出的三条后续问题均为未来工作：

1. **RQ1**：显式区分 expensive real evaluations 与 potentially accelerated estimation/inference，建立 cost structure，判断 acceleration 在什么条件下改善 regret 或 sample complexity；
2. **RQ2**：扩展到 batch 和 multi-agent parallel experimentation，研究 centralized/distributed coordination，在 shared budgets 和 limited communication 下平衡 optimism、feasibility 与 diversity；
3. **RQ3**：扩展到 molecule/protein 等 graph-structured decision spaces，把 uncertainty-aware learned representations（如 GNN）与 optimistic search 结合。

当前 Q-NLB-UCB 与 MOC-CAS 都不能因 RQ2 而写成已有 multi-agent results。本稿没有 multi-agent coordination experiment、limited-communication result、graph/GNN algorithm result，也没有 self-driving-laboratory deployment；后者只是最终愿景。

## 页码、复现与核验说明

PDF 页脚确认：p. 4029 为摘要、研究愿景与 progress-to-date 起点；p. 4030 为 Q-NLB-UCB bound、MOC/MOC-CAS、Figure 1 和 RQ1–RQ3；p. 4031 为 References。文本中的 1–4 是 section numbers，不是页数。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ARNT2761.pdf) 核对公式、方法归属、经验总结和未来边界；`reviewed` 表示 DC 稿的主张及缺口已经核验，不表示 [15] 定理已复证、[16] 实验已独立复现或发现系统已部署。
