---
title: "Puzzle it Out: Local-to-Global World Model for Offline Multi-Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IVNK5836.pdf"
preprint_url: "https://arxiv.org/abs/2601.07463"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["world_model_rollout_scope", "path_discrepancy_uncertainty", "theorem_proof_unavailable_in_preprint", "offline_benchmark_generalization"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "theorem_scope_not_independently_proven_from_available_pdf"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check; theorem scope caveat)"
reviewed_at: "2026-07-29"
---

# Puzzle it Out: Local-to-Global World Model for Offline Multi-Agent Reinforcement Learning

## 一句话总结

LOGO 不直接预测高维 joint state，而是先预测各 agent 的下一步局部观测，再聚合推断全局 state/reward；它以两条预测路径的 state discrepancy 为不确定性，对 synthetic rollout 数据低置信度降权后与原始离线数据共同训练 policy。

## 方法与证据

- 在固定离线 transition dataset 上，LOGO 的 predictive model 以每个 agent 的局部 observation/action 与 global state 辅助信息预测下一个局部 observation；deductive model 将局部预测拼接后推断 next global state 和 reward。两个模块均使用 encoder/decoder 结构及 prediction/reconstruction losses，另有将 predictive output 输入 deductive decoder 的正则项（§4.2、Eqs. 2–4）。
- 训练后从 learned world model 生成 $D_m$。不确定度定义为 predictive auxiliary-state encoder 输出与 deductive path state 输出的距离 $u(s,a)=\|\hat s'-s'_{deduced}\|$，不是对真实 transition error 或 OOD risk 的校准置信区间（§4.3、Eq. 5）。
- synthetic transition 的 priority 为截断的 $P_u=C-u$，并以 $\exp(P_u)$ 归一化加权；原始 $D$ 仍均匀采样，文中设定 synthetic 与真实 dataset 总采样概率相等。实现采用 MACQL backbone，并可接入作者的 MPC 变体（§4.3–4.4、Eqs. 7–10）。
- Theorem 1 声称：若 $Q$ 与 reward Lipschitz，且 reward/state/Q 的估计误差分别被 $\epsilon_r,\epsilon_s,\epsilon_Q$ 有界，则 generated 与 true optimal Q 的差不超过 $(L_r+\gamma L_Q)\epsilon_s+\epsilon_r+\gamma\epsilon_Q$（§4.3）。可用 PDF 将证明指向“Appendix ??”，但没有可定位的附录证明；因此只能记录为作者在强假设下的陈述，不能当作已独立核验的 rollout-safety 保证。
- 实验使用离线 SMAC 与 MaMuJoCo，比较 8 个模型/无模型、离线/在线基线，数据质量包括 medium-replay、medium、expert、mixed；主训练 rollout horizon 设为 15，作者报告在所测表格上常有更高回报，尤其 medium 数据（§5、Tables 1–3）。
- 消融显示 weighted sampling 在所列 MaMuJoCo medium 数据上优于 reward penalty；不同 rollout horizon 的表格显示 LOGO 在该 SMAC 设置中 15-step 最高，且其报告的一步 reward prediction error 为 0.0051。MPC 仅在 SMAC 6h_vs_8z 的表格中验证（§5.2–5.4、Tables 4–7）。

## 局限与复现

- 局部观测更易预测、局部拼接可恢复全局互动是架构假设/经验发现；对非局部通信、部分观测别名、agent 数变化或强耦合动力学，路径差很小不必然意味着真实模型误差小。
- synthetic data 的加权只能降低本模型定义的 disagreement 影响，不能阻止共同模式偏差、reward hacking 或多步 compounding error；不能把它解读为安全过滤。
- Theorem 1 的误差上界显式假定误差界与 Lipschitz 常数，且可用预印本未给出所指 proof appendix；它没有证明 learned uncertainty 与真实误差一致，也不建立 policy improvement。
- 结论受 SMAC/MaMuJoCo、已有离线数据构造、网络和 rollout horizon 限制；没有真实机器人、在线交互修正或跨任务 agent-number 泛化的证据。
- 复现应记录 local/global encoder inputs、模型容量与 loss weights、synthetic-to-real sampling ratio、$C$/weight normalization、uncertainty histogram 与真实 rollout error 的相关性、rollout horizon、MACQL/MPC hyperparameters、dataset seeds 和按数据质量分层的结果。

## 与 AAMAS 的关系与核验说明

该文属于 offline MARL 的 model-based dataset augmentation，连接多 agent 动力学建模、规划与 policy learning。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2601.07463) 核对 LOGO、两路径不确定度和 benchmark 证据；同时保留可用版本中 Theorem 1 证明链接缺失的核验限制。
