---
title: "Reducing Overestimation by Measuring Critic Disagreement in Multi-Critics Architectures"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/FYIR8341"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FYIR8341.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["critic_disagreement_proxy", "alpha_hyperparameter_dependency", "mujoco_d4rl_scope", "no_real_world_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Reducing Overestimation by Measuring Critic Disagreement in Multi-Critics Architectures

## 一句话总结

Ensemble Std（ES）在多 critic actor-critic 的 bootstrapped target 中，把 critic target estimates 的标准差当作 uncertainty proxy，并从最小 Q target 再减去 α·std；它在 MuJoCo 与 D4RL 的 TD3/SAC/TD3+BC 实验中改善若干数据 regime，但依赖 ensemble disagreement 与 α 的有效校准。

## 方法与证据

- 对 K 个独立 critics，ES 先采用 pessimistic minimum target Q_min，再以 critic predictions 的标准差 σ_Q 作为 disagreement，并使用 `y = r + γ [Q_min − α·σ_Q]`（Eq. 2--3）。critic 以该 target MSE 更新，actor 用所有 critics（如平均 Q）反馈更新（§3.2）。
- 其意图是在 critics 一致时保留学习信号、在 uncertainty/OOD actions 较高时额外保守；这是假设 disagreement 与 value error/不确定性相关的 regularization，并不是可证明的 epistemic uncertainty calibration（§1、§3）。
- 在线评估把 ES 插入 TD3/SAC，在六个 MuJoCo continuous-control tasks 上对比；离线评估把 ES 插入 TD3+BC，在 D4RL Hopper/Walker2d/HalfCheetah/Ant 的 Random、Medium、Expert 数据集测试。REDQ 作参考但未插入 ES（§4.1）。
- D4RL Table 2 中，ES 相对 TD3+BC 的平均改进为：Random 下 α=0.2/0.5/1 为 11.5%/7.8%/11.8%，Medium 最好为 α=0.1 的 4.3%，Expert 最好为 α=0.5 的 6.5%；部分设置显著性标记为 p<0.05。并非每 task/α 都提高。
- 分析指出 noisy Random 数据较适合较强 penalty，而 Expert 数据较适合较小/中等 α；Cheetah 是 disagreement 本来较低、额外 regularization 边际作用小的例外。离线训练时间表显示多数 ES 设置接近或低于 TD3+BC，但个别设置有开销（§4--5、Table 3）。

## 适用边界与复现

- critic standard deviation 只反映这组网络、初始化、replay data 与训练动态的内部差异；共享架构/数据产生的相关误差可能让 consensus 仍然错误，不能把低 disagreement 当作真实性或安全证据。
- α 会因 dataset quality、task 与 base algorithm 改变；论文也以不同 regime 的最优 α 展示此点。部署应做 held-out/OOD calibration，而不是固定复用一个数值。
- 证据限于 continuous-control MuJoCo 与 D4RL，且离线结果受 dataset、normalization、seed、网络和 TD3+BC config 影响；未覆盖视觉、语言、离散动作、多智能体博弈、真实机器人接触或安全约束。
- 复现应报告 ensemble size/independence、Q-target action sampling、α sweep、UTD、replay/data split、5 seeds、return variance、p-test 方案及 wall-clock；现实控制还须独立验证 constraint violations、OOD detection 与 fail-safe behavior。

## 与 AAMAS 的关系与核验说明

这是面向 actor-critic 稳定性的多估计器 RL 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FYIR8341.pdf) 核对 Eq. 2--5、D4RL Table 2、runtime Table 3 与 §5 分析；没有将 target overestimation 的 benchmark 缓解表述为现实系统安全保证。
