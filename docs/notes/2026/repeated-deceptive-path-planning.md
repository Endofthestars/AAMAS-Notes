---
title: "Repeated Deceptive Path Planning against Learnable Observer"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "safety_verification", "marl_coordination"]
dblp_key: ""
doi: "10.65109/DCBH3506"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DCBH3506.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "deception_research", "gridworld_simulation_only", "known_observer_update_assumption", "meta_gradient_dependency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Repeated Deceptive Path Planning against Learnable Observer

## 一句话总结

本文定义 Repeated Deceptive Path Planning（RDPP）：agent 多轮到达真实目标，同时面对会从完整历史 trajectory 学习目标识别器的 observer。Deceptive Meta Planning（DeMP）以 episode-level policy adaptation 加 meta-level initialization 更新，力图持续降低 observer 对真目标的预测概率；在 grid-world 400 episodes 中优于静态/反应式 baselines，但以略长路径为代价，且依赖可微、可反馈的 observer-learning model，不构成现实世界隐私或安全规避能力证明。

## 方法与证据

- RDPP 写作 \(M_{RDPP}=(M_{DPP},\Phi,K)\)：每 episode agent 生成 trajectory，observer 只看其 partial prefix 后对 goals 给预测分布；episode 后 observer 获知真实 goal 和 full trajectory，以负 log-likelihood 更新 \(\phi\)（§2.1）。agent 执行中不直接观测 observer belief，只收到 episode 后 prediction feedback；这假设了反馈可得、observer update mechanism/目标集合相容且训练行为稳定。
- 目标是最大化跨 \(K\) episodes 的 belief-induced reward，故针对一次静态 observer 的 deceptive path 会因相似轨迹累积暴露。论文没有给 attacker 对真实 observer 的访问、目标先验、观测噪声、multiple observers、动态地图/障碍、行动不确定性或 observer 不按预测更新时的 guarantees。
- DeMP 两层优化（§2.2）：episode level 从 \(\theta^{(0)}\) 用当前 observer predictive distribution 构造 deception-aware loss，做 gradient updates 得 \(\theta^{(k+1)}\)；每 \(M\) 个 episode 以 final adapted parameters 的 loss 对初始 \(\theta^{(0)}\) 做 meta update。它旨在预期 observer 的学习而非纯反应，但未公开 loss 细节、二阶/近似 gradient 算法、收敛定理、sample/compute cost、超参数、随机种子或伪代码。
- 评估是有多个 candidate goals、adaptive goal-recognition observer 的 grid-world navigation（§3）。图 3(a) 绘 400 episodes 的 true-goal probability；图 3(b) 比最后 episode，图 3(c) 比 path length relative to optimal。作者说 DeMP 保持最低真实目标预测概率，AM/DEAM/Honest/Naive 随 observer adaptation 退化，并有略高 path cost；图未提供数值表、error bands、runs、地图规模、goal distribution或显著性检验。
- 图 2 展示 baseline AM 使用固定路径而 DeMP 至 50/200/400 episodes 持续改变 trajectory distribution。该 qualitative observation 可支持“多样化减少稳定早期关联”的机制假说，但不证明不可识别、对未知强观察者鲁棒、最短/安全路径、或在交通/军事等真实环境中合规。

## 适用边界与复现

- 可用于受控仿真中研究 privacy-preserving navigation、对抗性 goal inference 与 observer adaptation 的失效模式；不应被用于规避合法监控、执法、平台安全机制或在公共空间中隐蔽行动。任何实际用途须由法律、权限、风险评估与独立监督界定。
- 复现需公开 grid maps/obstacles/start/goals、prefix fraction \(\alpha\)、horizon/discount、reward/deception loss、observer architecture/training/update \(U\)、agent policy、feedback interface、episode/meta update counts \(K,M\)、\(\alpha,\beta\) learning rates、first/second-order differentiation choice、baselines、seeds 与 path-cost normalization。应记录 observation prefix、observer calibration/accuracy 和每 episode true-goal probability。
- 应测试 observer model mismatch、unknown/non-differentiable/ensemble observers、delayed/noisy/partial feedback、changing goals/maps, randomized start, collision and motion constraints, long horizons, multiple cooperative/adversarial agents and compute budgets。报告稳态/最坏 episode disclosure、path efficiency、collision/constraint violations、sample cost及不同 observer updates下的负迁移；消融 meta update 与 episode adaptation。
- 对授权隐私应用，应优先采用数据最小化、可验证匿名化/访问控制、透明告知与安全导航约束，而非把“欺骗 observer”当作默认防护。部署评审应区分保护敏感目的地的正当性与造成监控盲区、逃避问责或误导安全人员的风险，保留审计、人工介入和禁止区域。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的对抗性路径规划与学习型 observer extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DCBH3506.pdf) 核验 RDPP observer update、post-episode feedback、DeMP 的两层更新、grid-world/400-episode 图示与 path-cost trade-off；没有将其模拟中降低预测概率的结果写成现实规避监控、隐私合规或安全路径的保证。
