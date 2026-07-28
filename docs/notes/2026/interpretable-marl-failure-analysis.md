---
title: "Interpretable Failure Analysis in Multi-Agent Reinforcement Learning Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/GWFE6009"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GWFE6009.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_failure_source_assumption", "differentiable_critic_requirement", "gradient_influence_is_approximate", "threshold_window_sensitivity", "posthoc_probe_critic", "simulated_adversarial_attack_only", "computational_overhead"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Interpretable Failure Analysis in Multi-Agent Reinforcement Learning Systems

## 一句话总结

论文提出两阶段的 MARL 事后故障取证：Stage 1 用每个 policy 的观测扰动 Taylor remainder 首次越阈来提名 Patient-0；Stage 2 用集中 critic 对他人 action 的一阶敏感度和沿敏感方向的二阶曲率，沿短因果窗口反向追踪并生成有向 contagion graph，以修正“下游 agent 先报警”的 domino effect。作者在 Simple Spread（3/5 agents）和 SMAC 3s_vs_3z、MADDPG/HATRPO 下报告合并 Patient-0 准确率 88.2–99.4%。该解释是基于 learned critic 的局部梯度关联，而非已证明的真实因果根因；它假设每个 episode 一个故障入口，且对 critic、阈值、窗口和算法的梯度平滑度敏感。

## 方法与证据

- Stage 1 固定当前 greedy action，以 action commitment cost 对本地 observation 的小扰动计算一阶 Taylor 近似的 remainder；正常 rollout 建立每 agent baseline，failure episode 中最早显著越阈者为初始 Patient-0 候选（§3.1）。它检测的是 policy 局部高曲率/非鲁棒状态，不自动辨别传感器、训练、环境或攻击的物理原因。
- Stage 2 对有 action-value critic 的 MADDPG 使用 \(\partial Q_i/\partial a_j\) 与 \(\partial^2Q_i/\partial a_j^2\)；一阶 magnitude 表示局部影响，正的方向曲率表示小偏差可被放大，并在 detection 前的因果窗口聚合影响作 traceback（§3.1）。HATRPO 没有该 critic 时，论文在 frozen rollouts 上拟合 post-hoc probe critic；任何 critic misspecification 都会进入归因结果。
- 图边 \(j\to i\) 汇合 sensitivity、accelerating-state 频率和时间，阈值后的 cumulative influence 给出 contagion subgraph（§3.2）。这是可读的关联/脆弱性地图，但 gradient influence 仅是近似的局部代理，不可等同干预式、反事实因果证明。
- 核心建模假设是每个 episode 只有一个初始 failure entry，后续失败全由 cooperative cascade 引起（§3）。多个同时故障、共同外部原因、非可微/离散系统或长时延传播是尚未覆盖的情形。
- 使用 worst-action adversarial attack 生成失败；Simple Spread 用 500 base episodes（3 agents 得 6,000、5 agents 得 20,000 intervention variants），SMAC 3s_vs_3z 用 100 episodes/1,200 variants。paired test 比较同一 agent pair 在 critical 与 robust timestep 遭受同强度攻击后的 instability（§4.1），所以证据主要是合成攻击下的诊断有效性。
- Table 1 的两阶段合并 Patient-0 accuracy 为 88.2–99.4%；HATRPO 通常优于 MADDPG。influence/IO 验证并不一致：Simple Spread-5 HATRPO 为 82.4%，SMAC HATRPO 为 59.7%，SMAC MADDPG 为 54.5%（Table 2）。作者将较低值归因于 noisy/diffuse gradient landscapes，说明模型/算法选择会实质影响解释可靠性。

## 适用边界与复现

- 适用于可访问或可拟合集中 critic、能记录 rollout 且需要诊断协作策略脆弱状态的研究/测试环境；适合作为 attack/failure injection 后的辅助取证，而不是唯一安全监控器。
- 在安全关键部署中，不能依据其 Patient-0 标签直接归责、自动隔离或宣告因果根因。应与事件日志、环境传感器、访问控制、独立 anomaly detector、受控 intervention/因果测试和人工审查交叉验证。
- 复现需固定训练算法/检查点、normal rollout baseline、扰动尺度、阈值、causal-window 与 recency weight、critic/probe 架构和拟合目标、攻击动作/强度、episode seeds；分别报告 Stage-1、traceback、combined、correction 与 IO，而非只报 combined accuracy。
- 进一步应测试多源故障、自然故障而非 worst-action attack、观察噪声/通信延迟、critic 校准误差、更多 agents 和更长 horizon，并测梯度/Hessian-vector 计算的在线延迟和资源开销。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 explainable MARL 与安全诊断工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GWFE6009.pdf) 核验两阶段公式、single-source 假设、Simple Spread/SMAC intervention protocol、Table 1–2 的结果与作者列出的限制；没有把 critic-gradient 归因写成通用的因果发现、真实安全认证或自动处置依据。
