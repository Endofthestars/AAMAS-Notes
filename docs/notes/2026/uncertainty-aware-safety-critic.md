---
title: "Safe But Not Sorry: Reducing Over-Conservatism in Safety Critics via Uncertainty-Aware Modulation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/ERDQ6501"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ERDQ6501.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "safety_critical_domain", "benchmark_cost_evaluation", "uncertainty_estimation_assumptions", "not_safety_certified"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Safe But Not Sorry: Reducing Over-Conservatism in Safety Critics via Uncertainty-Aware Modulation

## 一句话总结

USC 在连续控制 CMDP 的 safety critic 上，用 Gauss–Newton influence 估计 epistemic uncertainty，把保守惩罚集中到高不确定且高成本的 state-action，并对最不确定样本做邻居插值式 refinement。它在 Safety Gymnasium、FetchReach、HalfCheetah benchmark 中报告较低 episodic cost、竞争性 reward 和较好的 cost-map gradient error；这些是软成本约束的经验 trade-off，既不保证约束从不违反，也不构成真实安全认证。

## 方法与证据

- actor–critic 同时训练 reward critic \(Q^R\) 与 safety critic \(Q^C\)，在标准 Lagrangian constraint 下优化（§2）。USC 不提供外部 formal shield/物理安全层；其有效性依赖 cost signal、replay coverage、critic approximation、dual updates和环境是否与训练相符。
- 对冻结的 critic parameters，USC 通过 batch 的 gradient outer products 加阻尼 identity 计算 influence-based \(u(s,a)\)，经 log 与“预测 cost 高于 batch mean” indicator 形成 \(\tilde u\)（Eqs. 1–2）。这把不确定性与模型参数/批次近似绑定，不能自动等同于现实中的危险概率、感知误差、罕见故障或分布外风险。
- critic TD loss 加入由 \(\tilde u\) 加权的 conservative term；每次更新后，对 top-\(n\) uncertain samples 从 joint \((s,a)\) 空间的 confidently predicted neighbours 插值 synthetic cost targets，并用 trust-region-style regularizer refinement（Eq. 3, §2）。摘要未给完整邻居度量、\(n\)、插值/信心判据、计算开销或何时这种伪标签会传播错误。
- Table 1 覆盖 CarGoal/CarButton、FetchReach、HalfCheetah。例：CarGoal2 的 USC reward \(8.84\pm0.62\)、cost \(5.05\pm1.27\)，标准 safety critic 为 \(7.54\pm1.38\)/\(5.65\pm2.00\)；CarButton1 USC reward 6.38、cost 6.01，DDPG 6.20/9.50。摘要的“约 40% violation reduction”是跨任务概括，不是每项一致的降幅或零 cost。
- Table 2（CarGoal2 ground-truth cost map）中 USC gradient MSE \(0.10\pm0.06\)，safety critic 0.58、conservative critic 1.95；contrast error 并非最小（USC 0.08、conservative 0.04）。这支持特定 map 质量指标的改进，不足以证明 policy 在所有安全边界均正确、calibrated 或可转移。

## 适用边界与复现

- 适合研究安全 critic 的偏差/方差和 reward–cost 折中；不能直接作为机器人、医疗、车辆或工业系统的唯一安全机制。安全关键应用必须有独立约束监视、可证明 fallback、人工/硬件限制与事故响应，而非只依赖 learned cumulative-cost estimate。
- 复现需公开 environments 与每项 \(\chi\)/cost definition、DDPG/safety/conservative/USC 实现、network/replay/batch、influence damping、top-\(n\)、neighbour metric/interpolation、trust region、Lagrange updates、seeds和每 episode reward/cost。报告 learning curves、cost constraint satisfaction probability、CI、误报/漏报与计算时间，而不只列平均 episodic cost。
- 应做 sparse/noisy/miscalibrated costs、OOD hazards、partial observability、adversarial/rare failures、sensor drift和跨环境迁移；独立衡量 uncertainty calibration、cost-map accuracy、constraint violation tail risk和最差种子。作者也将 partial-observable/adversarial environments 留为 future work，故不能将当前 benchmark 结果扩展到这些情况。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 safe RL/safety critic 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ERDQ6501.pdf) 核验 influence uncertainty、modulated critic/refinement、Tables 1–2 与比较范围；没有将 episodic-cost 改善写成正式约束保证、零违规或实际部署安全性。
