---
title: "CoMoU: A Trust-region Model-based Method for Efficient Offline-to-online Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/JCLP2243"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JCLP2243.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "model_based_rl_assumptions", "offline_online_distribution_shift", "simulation_benchmarks", "theorem_conditions_required"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# CoMoU: A Trust-region Model-based Method for Efficient Offline-to-online Reinforcement Learning

## 一句话总结

CoMoU 在 offline-pretrained dynamics model 的 online fine-tuning 中约束新旧 transition model 的 KL 变化，用 KKT 得到旧模型预测与 replay-buffer empirical transition 的加权更新，避免 distribution shift 时突变。摘要在 D4RL 的 Hopper/Walker2d/HalfCheetah 上报告较高 sample efficiency 和稳定回报；其 bounded-difference、asymptotic-unbiased 结论取决于有限长度/有界价值和 buffer transition distribution 收敛到真实动力学等前提，不能直接视为真实系统无崩溃保证。

## 方法与证据

- 模型更新最小化 replay buffer \(\rho_D\) 与参数 dynamics \(p_\phi\) 的 KL，同时限制 \(D_{KL}(p_{\phi\,old}\Vert p_\phi)\le\epsilon\)。迭代式为旧预测与 \(\rho_D\) 的 \(\lambda/(\lambda+1)\)、\(1/(\lambda+1)\) 加权组合（Eq. 1，§2.1）。其实际可用性依赖 transition density 表示、KL 可计算性、\(\lambda/\epsilon\) 选择、replay coverage 与模型错误，而不是单纯加入约束就能保证稳定。
- 完整流程以 MOPO offline initialization，在线交互数据加进 replay buffer，受约束更新 dynamics，并由 model rollouts 更新 policy/value（Figure 1）。模型 rollout 的 compounding error、探索引起的安全/数据风险、offline data quality与 policy update implementation均未由摘要单独控制。
- Theorem 2.1 给真实环境中相邻 model-optimal policies expected return difference 的上界，含 \(\sqrt{2\epsilon}(r_{max}+V_{max})H\) 和 model–real transition 的 L1 errors（Eq. 2）。因此它不是零性能下降：上界会随 horizon、奖励/价值界和 model error 增大，且比较的是理论模型最优 policy 的特定 quantity。
- Theorem 2.2 仅在 \(\rho_{D_t}(s'|s,a)\) 对真实 \(p(s'|s,a)\) 的统一尾部收敛条件（Eq. 3）成立时，证明 \(p_{\phi_t}\to p\)（Eq. 4）。online data 是否满足覆盖/收敛并未由该定理保证；“unbiasedness”不可脱离这一假设。
- 实验是 D4RL Random/Medium/Medium-Replay/Medium-Expert、Hopper/Walker2d/HalfCheetah，比较 ACA、PEX、ODT、MOORe；Figure 2 曲线平均 3 seeds，Figure 3 比 MBPO 与 Naive Tuning，Figure 4 改 \(\tilde\lambda\)（§3）。没有真实机器人、OOD dynamics、成本/安全约束、CI或显著性；图示优势不能泛化为所有 O2O RL。

## 适用边界与复现

- 适合研究 model-based offline-to-online fine-tuning 中的更新幅度控制；不应依此在未验证的真实设备或安全关键控制上放开在线探索。“trust region”限制 learned model 改动，不等于状态/动作安全屏障。
- 复现需给出 D4RL 版本/normalization、MOPO initialization、transition model/distribution parameterization、KL/\(\epsilon\)/\(\lambda\)、replay sampling/offline-online mixing、rollout horizon、policy/value learner、all baseline tuning、seeds和每环境完整曲线。检验 Eq. 3 的覆盖近似、model prediction errors及 Theorem 2.1 的 bound 是否实际非松。
- 应评估 offline dataset 缺口、非平稳/部分可观测 dynamics、model misspecification、OOD actions、不同 online budget、replay contamination和 hyperparameter sensitivity；报告 worst-seed crashes、model calibration、real transitions 与 synthetic rollouts 比例。真实系统还需有独立 safety constraints、action limits、monitoring和回退策略。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 model-based/O2O RL 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JCLP2243.pdf) 核验 constrained update、Theorems 2.1–2.2、D4RL/MuJoCo 设定和 3-seed 曲线；没有将条件性理论或 benchmark 稳定性写成现实无崩溃、安全或普适最优性保证。
