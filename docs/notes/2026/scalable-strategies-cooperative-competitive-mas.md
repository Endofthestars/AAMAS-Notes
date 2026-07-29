---
title: "Scalable Strategies for Cooperative and Competitive Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["marl_coordination", "planning_scheduling", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: "10.65109/JCOC8756"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JCOC8756.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05g"
spark_draft_verdict: "source_grounded_draft"
spark_qa_verdict: "pass_with_simulation_publication_and_full_paper_boundaries"
  spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_dissertation_summary", "adversarial_swarm_dual_use", "staged_factorisation", "centralised_design_decentralised_execution", "llm_generated_heuristics", "two_manuscripts_under_review", "jax_simulation_only", "no_quantitative_results_in_dc", "robustness_and_scalability_author_reported", "graph_ssm_ongoing", "no_real_drone_or_safety_validation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_completed_study_publication_simulation_dual_use_robustness_and_deployment_boundary_check"
escalation_verdict: "pass_after_author_reported_completed_status_and_simulation_only_boundary_reinforcement"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted simulation and safety-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Scalable Strategies for Cooperative and Competitive Multi-Agent Systems

## 一句话总结

这篇 Doctoral Consortium 文稿把 scale 当作协调架构的首要约束，以 staged factorisation 和 Centralised Design, Decentralised Execution 汇总 LLM-HELPS、GA–DP 与 scenario-conditioned composition 三项研究；证据只来自 JAX 对抗资产保护仿真的定性概述，DC 稿没有规模、指标或结果数值，两项研究仍标为 manuscript under review，不能据此推出真实无人机防御、通信退化鲁棒性或安全关键部署能力。

## Scale-first staged factorisation

作者认为，小队中的 differentiated tactical roles 与大规模 homogeneous swarm rules 之间存在空档。其替代 end-to-end joint policy learning 的思路是：

- 把全局 coordination 分解为可组合的 sub-problems；
- 在 offline optimisation 阶段发现、优化 modular heuristics；
- 将复杂计算移出 execution；
- 以 lightweight decentralised policies 在线执行；
- 把 communication 作为 optional enhancement，而不是结构性前提。

文稿称这一 Centralised Design, Decentralised Execution（CDDE）设计有助于在 bandwidth limitation、agent loss 或 degraded connectivity 下维持协调。三页稿没有给 bandwidth、agent-loss protocol 或 robustness metrics，因此这些只能作为作者的设计主张（§§1–2，p. 4032）。

## JAX simulation 的证据范围

作者称所有 studies 都在 high-performance JAX simulation 中评估：defending team 需要拦截沿 nonlinear trajectories 接近的 attacking swarm，以保护 fixed asset（p. 4033）。

DC 稿没有披露：

- attacker/defender team sizes；
- scenario distribution、initialisation 或 dynamics；
- success/robustness/scalability metric；
- baseline result table 或 numeric outcome；
- trials、variance、confidence interval；
- runtime、memory、communication load 或 hardware；
- code、physical vehicle 或 real-world trial。

因此，“coordination at previously intractable scales”“robust to agent loss and environmental uncertainty”“minimal overhead”“bounded requirements”“generalisable”等均是作者在摘要和结论中的报告，不能由本 DC 独立复核为量化结果或保证。

## 三项研究的摘要粒度

### LLM-HELPS

LLM-guided Hierarchical Evolutionary Learning with Permutation-invariant Surrogates（LLM-HELPS）让 LLM 在 offline 阶段提出 interpretable low-level heuristics，再进行 hierarchical composition 和 evolutionary optimisation。permutation-invariant surrogate fitness model 用于减少每个 candidate 都执行 full simulation 的需求。作者称该阶段在 moderate scales 展示 coordinated defence。

参考文献 [5] 标为 **manuscript under review**。本稿没有 heuristic prompts、surrogate architecture、evaluation error、搜索参数或结果数字。

### GA–DP

第二项研究先为 small sub-engagements 演化 strategy，再通过 hybrid Genetic Algorithm–Dynamic Programming（GA–DP）把 small-team chromosomes 作为 compositional units 组装成 large-scale formations。作者称这保留 higher-order behavioural dependencies，并通过 polynomial-time decomposition 使组合优化可处理。

参考文献 [4] 标为 **accepted for publication**。仓库另有该 AAMAS research paper `GYJS4496` 的[独立笔记](./drone-defense-small-team-strategies.md)。本笔记没有从完整论文倒灌 DP complexity、GA parameters、team sizes、win rates 或 baselines。

### Scenario-conditioned composition

第三项研究把 static assembly 扩展为 adaptive deployment：geometric dispersion metric 描述 adversary configuration，dynamic programming 把 swarm 分成 spatially coherent sectors 并分配 sub-team strategies。作者报告这种 conditioning 随 swarm size 增长改善 robustness 与 scalability。

参考文献 [6] 同样标为 **manuscript under review**。DC 稿没有给 metric、场景规模或定量结果，不能写成已经独立复现。

作者将三项工作称为 completed studies；这表示 dissertation 中的阶段定位，不代表三者都已发表、通过同行评审，或作为一个固定端到端 pipeline 统一部署。

## Ongoing Graph-SSM

当前工作尝试将模块整合为 neuro-symbolic Graph-SSM controller：

- graph-neural backbone 表示 swarm relational structure；
- state-space module 以 linear scaling 建模 temporal dynamics；
- network 选择 previously discovered heuristics，而不是直接输出 raw control actions。

目标是支持 adversary 改变空间构型时的 adaptive re-partitioning，同时保留 heuristic interpretability。该部分明确是 ongoing work，没有 architecture specification、training protocol 或结果。

## Future directions

文稿把以下内容留作未来研究（p. 4033）：

- multiple assets 间的 game-theoretic resource allocation；
- partial observability；
- low-bandwidth 或 delayed communication；
- environmental degradation 与 sim-to-real discrepancy；
- heterogeneous multi-target protection；
- distributed disaster response。

因此，当前结果不能支持 degraded communication、部分可观测、真实动力学迁移、多资产防护或灾害响应能力。

## 双用途与安全边界

本文场景是抽象的 adversarial swarm coordination / asset-protection simulation。本笔记不补充现实目标选择、载荷、拦截轨迹、部署程序或行动建议。

JAX/HPC simulation 不能替代 vehicle dynamics、sensor uncertainty、identification error、communication security、collision avoidance、human oversight、法律授权、fail-safe 或独立安全评估。文稿没有现实 drone experiment、operational readiness、safety certification 或 field deployment。

## 页码与核验说明

PDF 页脚确认：p. 4032 为摘要、问题与 scale-first/CDDE 框架；p. 4033 为 JAX task、三项研究、Graph-SSM ongoing、future directions 与结论；p. 4034 为 References，其中 [4] accepted、[5]/[6] under review。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JCOC8756.pdf) 核对方法摘要、publication status、仿真范围和未来边界；`reviewed` 不表示 under-review manuscripts 已验证，也不表示现实对抗系统可部署。
