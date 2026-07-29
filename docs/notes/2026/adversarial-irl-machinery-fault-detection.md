---
title: "Learning Rewards, Not Labels: Adversarial Inverse Reinforcement Learning for Machinery Fault Detection"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/AXYX4522"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AXYX4522.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "industrial_safety_domain", "offline_benchmark_evaluation", "healthy_data_assumption", "not_safety_certified"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Learning Rewards, Not Labels: Adversarial Inverse Reinforcement Learning for Machinery Fault Detection

## 一句话总结

本文把无标签机械故障检测建模为离线、仅状态的 AIRL：以健康振动序列为 expert，令相邻窗口组成状态转移/代理动作，discriminator 的健康一致性经反转和阈值化形成 anomaly score。作者在 HUMS2023、IMS、XJTU-SY 三个 run-to-failure benchmark 报告早期且稳定的检测；这不是对真实设备、报警成本、误报漏报或安全运行的认证。

## 方法与证据

- 因数据集无记录控制输入，状态为固定长度、归一化 vibration window，下一窗口 \(x_{t+1}\) 被当作 proxy action；健康演化是 expert trajectories（§2.1）。这是一种 state-only imitation 学习建模选择，不能证明自然时间演化就是可控动作或能覆盖工况、传感器和故障模式的变化。
- AIRL 的 generator \(\pi\) 模仿 expert dynamics，discriminator \(D(s,a,s')\) 区分健康/生成转移，并采用 \(r_\theta+\gamma V_\phi(s')-V_\phi(s)-\log\pi(a|s)\) 结构（§2.2）。作者将其称为可解释 reward/health score，但摘要没有提供 reward 可解释性验证、网络结构、训练稳定性、超参数或失败案例。
- anomaly score 是 trajectory 上 discriminator confidence 的反转均值，随后用 Otsu、K-means 或统计规则动态阈值化（§2.3）。摘要开头也以“reward/anomaly score”描述正常与故障方向，故复现时必须固定并检查 \(D\)、reward、反转 score 和阈值的符号/方向；不能只按文字名称判断高分代表健康还是异常。
- HUMS2023 的实验只用 RF2 accelerometer，Days 17–20 健康数据训练、Days 21–27 退化期测试；对比 IF、OCSVM、AE/VAE、LSTM-AE/LSTM-VAE、SS-AD、FRESH filter、CTQN contextual bandit（§3.1）。Table 1 报 AIRL 在 Day 22 File #163 检出，FRESH 为 Day 22 #127、challenge winner Day 23 #175、committee ground truth Day 24 #264；CTQN 报 No Fault（§3.2）。
- 文稿称 IMS/XJTU-SY 有一致趋势，并称 AIRL 在故障后维持约 65% anomaly rate，但未提供各数据集的完整指标、样本/故障定义、split 重复、置信区间、误报率、阈值选择是否泄漏测试标签、计算成本或现场前瞻评估。早于委员会 ground truth 不是自动的“更好”，可能是早期预警也可能是误报。

## 适用边界与复现

- 适合离线状态转移 anomaly-detection 研究和维护决策的辅助信号；不得直接驱动停机、放行、航空/核电等安全关键动作，也不能替代传感器冗余、人工诊断、故障树、监管或安全认证。
- 复现需要三个数据集的确切预处理/窗口/归一化、健康训练范围、RF2 选择、state/proxy-action 表示、AIRL 网络与优化/生成器、\(\gamma\)、阈值与报警规则、所有 baselines/调参、随机种子、每个 benchmark 的完整曲线和按时间的混淆矩阵。务必隔离测试数据和真实 onset 标注，避免以测试期调阈值。
- 应报告 false alarm、miss、detection delay、calibration、uncertainty、漂移、噪声/缺失传感器、工况迁移、未知故障和对抗/异常输入；在多传感器及前瞻现场试验中比较人工维护流程和报警负担。对安全关键用途需有 fail-safe、保守阈值、日志、人工复核与独立验证，不能由三个 benchmark 的 earliest-onset 比较推出可靠性。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 RL/IRL agent 在工业故障检测中的应用扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/AXYX4522.pdf) 核验 state-only AIRL、反转 discriminator score、三个数据集、HUMS2023 的训练/测试窗口及 Table 1；没有把离线 benchmark 结果写成安全保证、生产部署效果或无需人工标签/审查的普适结论。
