---
title: "Dynamically Increasing Agents Set-Size in Bayesian Multi-agent Multi-armed Bandits Framework"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/YQTC6947"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YQTC6947.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["piecewise_stationary_assumption", "likelihood_threshold_tuning", "unbounded_agent_pool", "synthetic_regret_scope", "web_server_distribution_model", "pretraining_baseline_comparison", "runtime_overhead"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Dynamically Increasing Agents Set-Size in Bayesian Multi-agent Multi-armed Bandits Framework

## 一句话总结

LA-MAS 维护一组内部 UCB learners（论文称 agents），按每个 learner 对新 reward 的 likelihood 更新 posterior，并在所有 likelihood 连续低于阈值时新增 learner 而保留旧记忆；LA-MAS-BO 再在线调 UCB exploration 常数。它在指定的非平稳合成与 web-server latency 分布上常降低 regret，但“多 agent”是算法内部的模型池而非自治实体协作，效果依赖 changepoint/likelihood 阈值、环境可复现性与不断增长的内存池。

## 方法与证据

- 每个内部 agent 是一个 UCB1 policy，拥有各自 arm statistics；每一步依 posterior \(p\) 抽一个 agent 所建议的 arm，同时用 \(p_i\) 加权更新所有 agent。奖励在其预计 Gaussian band 中的 likelihood 形成 posterior（Algorithm 1、§3）。因而它假设从单个选中 arm 的 reward 可对所有历史模型作有意义的软更新。
- 若最大 local likelihood 连续 \(M\) 步低于 \(\eta\)，LA-MAS spawn 一个 fresh learner，并临时把 posterior 置为新 agent 的 one-hot，学习 \(\tau\) 步后再均匀重置；LA-MAS-BO 还用 GP/Bayesian optimization 调探索参数 \(c\)（§3）。\(\eta,M,\tau,\epsilon,\delta_{min},\kappa\) 等选择会直接改变误报/漏检变化和 regret，论文未给自动校准或全局 optimality 保证。
- 实验对 UCB1、SW-UCB、TS variants、GLR-klUCB、M-UCB、DAMAS-BO 等比较；“real-world”轨道以 38 个 server configurations 的已测每 content-type/action \(\mu,\sigma\) 重新采样 delay，reward 为负 delay（§4）。这不是线上生产 A/B 实验，不含真实服务流量反馈、排队、用户行为或操作风险。
- 合成 40-arm 设定中，LA-MAS-BO 相对 DIS-TS 报告约 50% lower mean regret；在一项比较中相对第二名 GLR-klUCB 约低 45%（§4）。这些数值取决于人工安排的每 1000 steps environment switch 和采样分布。
- DAMAS-BO 若完整预训练所有环境，后期可取得比 LA-MAS-BO 更低 regret；若仅预训练 3 个环境后测 4 个，LA-MAS-BO 的优势变大。随着 environment count 增加，DIS-TS 也会超过 LA-MAS-BO（§4）。故“dynamic spawning 更好”只覆盖未见模式与该组规模/参数，不是总体支配。
- 24-environment synthetic suite 中，每种环境 1000 steps、\(|A|=40\)、每配置 5 runs；Table 2 的 4000-step 计时：LA-MAS 约 2.9--3.4 s、LA-MAS-BO 4.09--5.97 s，M-UCB 仅 0.06--0.08 s（§4--5）。agent pool 无上限，作者将 bounded pools 列为未来工作。

## 适用边界与复现

- 适用于可用有限 arms、可观测数值 reward、存在重复或分段稳定模式、且能容忍模型池/探索开销的在线配置选择研究。它不直接解决多实体通信、激励、隐私、对抗性 rewards 或去中心化协调。
- likelihood 应与真实 reward distribution 相容；重尾、延迟反馈、非高斯噪声、渐变/周期性变化、异常值、混合环境或最优 arm 变化过快都可能触发错误 spawn/reuse。遗留 models 若无限增长会带来计算、内存和过拟合风险。
- 复现需固定 base UCB/BO、likelihood band、priors、\(\eta,M,\tau,\epsilon,\delta_{min},\kappa\)、environment schedules、reward means/variances、action count、seeds、all baselines/pretraining knowledge、server workload statistics和 metrics。报告 agent-pool size trajectory、检测 precision/recall/delay、regret/Pbest、墙钟/内存及每个未见环境的失败案例。
- 若用于生产 server 调参，应有安全配置白名单、tail-latency/SLO/错误率/能耗约束、canary 与回滚、容量保护和人工变更审计；平均 latency regret 的改善不保证服务可靠性、成本或用户公平。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的非平稳 multi-armed bandit、模型池与自适应资源选择论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YQTC6947.pdf) 核验 Algorithm 1、likelihood/spawning、38-action web-server 模型、40-arm/24-environment 实验、完整预训练及规模反例、Table 2 与 bounded-pool future work；没有把内部 learner ensemble 的有限模拟 regret 优势误写为自治多 agent 协作或生产系统可靠性保证。
