---
title: "Theory of Mind Guided Strategy Adaptation for Zero-Shot Coordination"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/UMCV8852"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UMCV8852.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["overcooked_benchmark_scope", "environment_specific_intent_labels", "online_behavior_inference", "library_coverage_dependency", "no_theoretical_generalization", "policy_switching_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Theory of Mind Guided Strategy Adaptation for Zero-Shot Coordination

## 一句话总结

TBS 为 population-based ZSC 将 partner pool 按 cross-play 相似性作 self-tuning spectral clustering，并为每 cluster 训练 specialist best response；测试时 recurrent ToM 从互动 history 预测人工定义的高层 intent，以 global/cluster concept distributions 的 KL 距离选 cluster 对应策略。它在 Overcooked 的 held-out、随机 reward-shaped VDN partners 上通常优于单一 BR，含部分可观测设置；但属于在线行为**推断与策略切换**、依赖任务特定 intent 标签和训练库覆盖，论文也没有协调/泛化理论，不能泛化为无模型的真实 teammate understanding。

## 方法与证据

- TBS 先以 random reward shaping 构造 diverse partner population，计算 pairwise cross-play similarity 并用 self-tuning spectral clustering 自动决定 \(k\)；随后每个 cluster 训练一个 complement BR policy，而非一个面对全部 partner 的 generalist BR（§2--3）。cluster 是 performance/behavior 相似性的代理，非真实人格、意图或能力的可验证分类。
- ToM 使用 \(k+1\) 个 recurrent models：每 cluster 一个 ToM\(_{C_i}\)，另一个 global ToM。它们由 cluster trajectories 监督，输出预定义 concept（Overcooked 中如 onion pickup/drop、dish delivery）的分布（§3）。因 labels 依赖 environment semantics，方法并不自动从任意传感信号发现 intent。
- 执行时以 global 与 cluster-specific ToM 在 history 上的 Bernoulli concept distributions 计算累计 KL divergence，取最小 cluster 并切换其 BR。每 episode 开始随机选择一个 ensemble policy，因为必须先积累 interaction history 才能推断 partner intent（§3，Eq. 8）。所以“zero-shot”是无梯度更新/无显式通信，而非无在线适应、无 cold-start 风险或静态策略。
- 评测为 Overcooked-AI Onion Soup：两 agent 在 400 frames 内做菜/送餐，dish reward 20，比较七种 layout、fully observable 与 partially observable conditions（§4.1）。不包含真实人类、机器人、非平稳任务、开放队伍、通信、动作延迟或安全约束。
- partner pool 为 10 training agents；evaluation 为 10 held-out agents，均为独立训练、randomly shaped reward 的 VDN agents。主指标是 any-play \(J_{inter-XP}\)；这测试特定训练分布外伙伴，不证明对不同算法、能力、目标/动作空间或人类策略的一般化（§4.1）。
- 全观测下 TBS 在 7 layouts 中 6 个 match/exceed BR；部分观测下 match/exceed BR 于所有 layouts，平均值也更高，但论文图给出 bootstrapped 95% CIs 而非跨任务/算法显著性保证（§4.2、Fig. 4）。
- 移除 adaptation module 或再移除 clustering 的 random cross-play variant 均下降；在 Counter Circuit 增大 pool 5→75、用 25 held-out agents 时 TBS 比 BR 受益更多。结果表明该 benchmark 的 library diversity有用，也意味着 compute/memory/cluster-policy 数随 pool 增长（§4.3、Fig. 5）。
- fixed \(k=2\ldots5\) 的 scaled rewards 约 0.7--0.8；coarse concepts 仍可运行但高层且更细的 concept 优于低层 action labels。此敏感性仍只对 seven layouts 和由作者定义的 labels 有效（§4.3）。
- 作者明确 limitation 为缺少 coordination/generalization theoretical analysis（§5）。

## 适用边界与复现

- 适用于能预先建立可辨识策略库、可定义与标注 high-level partner concepts、且有足够 early history 做选择的两人合作任务。若目标/动作语义、传感、伙伴能力或环境布局与训练不同，cluster/ToM similarity 未必代表互补策略适配。
- 不应将 intent prediction 当作真实心智状态、可信性或安全性判断。ToM 只是从 benchmark trajectories 学到 concepts；误分类、history 短、partner strategy switching 或 adversarial mimicry 会诱发错误 specialist selection和策略来回切换。
- 真实协作需单独处理 partial/noisy observations、communication、delay、multiple/entering/leaving agents、human consent/interpretability、action safety以及 OOD detection。高风险 robot/human setting 应在策略切换外加 constraint/shield、confidence/abstention、fallback generalist、human override与 staged trials。
- 评估不应只用 shared algorithm/random reward shaping 的 held-out agents。应作跨算法/seed/skill/capability/goal/observation shifts，报告 first-decision/cold-start、per-cluster confusion、switch frequency、worst partner、regret vs oracle与 compute latency；同时区分 episode-level random start policy和实际 adaptation time。
- 复现应固定 Overcooked-AI/layout version、VDN/random-shaping pool/held-out seeds、cross-play matrix/similarity/STSC、\(k\)、specialist BR training、44/11/6/action concept vocabulary/labels、RNN architecture/history window/KL aggregation、selection cadence、fully/partial observation mask、400-frame reward、CI/bootstrap与 evaluation protocol。

## 与 AAMAS 的关系与核验说明

这是 ToM-guided multi-agent zero-shot coordination 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UMCV8852.pdf) 核对 clustering、specialist BR、recurrent ToM/KL selector、episode cold-start、Overcooked/VDN held-out评测、pool/cluster/concept ablations和作者的理论限制；没有把 benchmark intent classification或策略选择误写成真实心智理解、无需在线推断的适应、跨域泛化或安全保证。
