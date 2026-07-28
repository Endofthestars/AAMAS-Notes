---
title: "Modeling Dynamics under Random Delays in Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/EAJI2382"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EAJI2382.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["known_or_observable_delay_distribution", "nonlinear_decoder_bias", "synthetic_uniform_delay_scope", "world_model_compute_scaling"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Modeling Dynamics under Random Delays in Reinforcement Learning

## 一句话总结

该方法在 DreamerV3 的随机动作执行延迟下，对所有可能已执行动作轨迹的 latent state 取按延迟概率加权的期望，并每 `K` 步合并分支；在 Vision DMC 的独立均匀延迟包装器中提升回报、动态损失和训练稳定性，但低方差的 latent 均值并不保证非线性世界模型输出无偏。

## 方法与证据

- 作者把 observation delay 与 action-execution delay 分开：前者称可通过训练时重标记 transition 消除，后者在推理时仍不确定哪些已发 action 被执行（§1、§4.1）。
- 对 action buffer 中每个 action，按估计的 delay distribution 计算其成为最新已接收 action 的概率；对所有可能执行轨迹 roll out RSSM，再令期望 latent 为这些轨迹 latent 的加权平均。延迟分布以 replay buffer 中延迟计数估计（式 7–9、§4.3）。
- 完整轨迹树随 horizon 指数增长；方法每 `K` 步把分支合为期望 latent，复杂度从 `O(d_a^T)` 降到 `O((T/K)d_a^K)`。`K=1` 最省算力但损失多峰信息，`K=2,4,6` 是文中评测选择（§4.4）。
- 理论上，posterior mean 在二次 latent 损失下是最小均方估计，并按 total-variance/Rao–Blackwell 论证 `Var(ŝ)≤Var(s_τ)`；policy-gradient 方差界还要求 critic 对 latent Lipschitz。对非线性 decoder/reward/critic，论文明确给出由 Hessian 与 latent variance 控制的 Jensen/Taylor 偏差（式 10–22、§4.5）。
- 评测六个 Vision DMC 任务，固定最大 observation delay 8、action delay 上限为 2/4/8，均每 episode 独立取均匀分布；模型基线是 Extended、Latent、DreamerV3，另有 DCAC、D-TRPO、Memoryless。各配置 5 seeds；文中称 `K≥2` 在六任务回报超过其他 model-based 方法，`K=4` 后收益递减，且动态损失/梯度方差更低（§5）。

## 局限与复现

- 需要已知或能从 replay buffer 观察/准确估计的 action-delay 分布。真实系统若只看到延迟观测而看不到动作到达/执行时间，则式 9 的计数估计不是免费可得；分布漂移、相关 delay、队列/丢包、动作重排和 state-dependent delay 均未直接验证。
- 方差减少发生在 latent posterior mean；`g(E[s])=E[g(s)]` 仅在线性 downstream 模块成立。论文对非线性情形给出曲率相关 bias bound，故“无偏”不应推广到预测像素、奖励、return 或最优 policy。
- 行为近似把 latent branches 以均值合并，会抹平真正多峰的物理状态；`K` 是性能—计算折中，最大 delay/horizon 增大时分支成本仍快速增长。正文没有机器人、网络抖动或真实延迟 trace 的部署结果。
- 对 observation delay 可“完全”重标记的说法依赖其通信延迟建模、完整 action history 和未延迟底层 transition 可对齐；一般 sensor/actuator 时间戳噪声、部分可观测和异步多通道下须重新证明。
- 复现应公开 wrapper 的 delay sampling/时间语义、可观测的执行反馈、action buffer、RSSM/DreamerV3 版本、所有 K/预算/seed、模型计算量与跨分布延迟测试，并分别报告 latent variance 与实际任务 return 偏差。

## 与 AAMAS 的关系与核验说明

该文研究带通信随机延迟的世界模型强化学习，适用于具感知/执行时滞的 autonomous agents。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EAJI2382.pdf) 核对期望 latent、分支合并、定理假设和 Vision DMC 协议，未把 latent 方差结论扩大为对全部非线性下游输出的无偏保证。
