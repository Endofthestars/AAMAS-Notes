---
title: "Timing the Message: Language-Based Notifications for Time-Critical Assistive Settings"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/SAWU6614"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SAWU6614.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_human_model", "llm_comprehension_surrogate", "no_human_subject_validation", "reaction_time_model_assumption", "simulated_domains_only", "notification_interruption_risk", "not_safety_certified"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Timing the Message: Language-Based Notifications for Time-Critical Assistive Settings

## 一句话总结

论文把 time-critical language notification 设计为延迟 MDP：notifier 既选择何时说、说什么 topic，也选择消息的 actionability/comprehension point 与长度；环境在说话、理解、人的 reaction delay 和 follow-through 期间继续演化。其 Convey & React policy 在模拟 Lunar Lander/Highway 中比假设即时理解的 policy 成功率高很多（0.97/0.93 vs 0.22/0.28），但“人”由训练策略、文献反应时和 LLM 生成的理解进度代替，尚无人类驾驶/飞行/厨房实证。

## 方法与证据

- utterance action 用 \((c,M,L)\) 表示：topic \(c\)、消息从开始到足以驱动行动的 comprehension word index \(M\)、完整 conveyance length \(L\)。论文将平均每词约 0.3 秒，消息不再是单时步 action；人可在完整 utterance 前听到可行动 prefix 后启动反应（§3.1）。
- reactive human model 组合 task-completion MDP 与 utterance-reaction model。反应包括理解时点、reaction delay \(N_L\) 与 follow-through duration \(N_M\)；notifier 用近期 state--action history 增广状态，将 delayed feedback 化为标准 MDP，轻量 MLP 以 PPO 训练（§3.1--§4.1）。模型的通用性取决于这些人类参数是否真实且个体化。
- LLM 离线生成按 topic 的 utterance taxonomy，并逐词给 0--100% comprehension progression，找出 \(M\)；线上仅查数据库和 policy。论文明确数值 comprehension sequences 只是 illustrative，真正 human calibration 留作未来（§4.2）。因此不能把 LLM 评估直接等同于认知测量。
- 域为：Lunar Lander（危险区只对 notifier 可见）、三次 merge 的 Highway Driving、和 partial-observation Steakhouse/协作烹饪。人类 task policy 分域训练；默认 Convey & React 同时建模 \(M>0\) 与 \(N_L=2\)（§5.1--§5.2）。
- Table 1：Delay-Free（假定 \(M=N_L=0\)）在 piloting/driving success 为 \(0.22\pm0.04/0.28\pm0.03\)；只考虑 conveyance 的 policy 是 \(0.94\pm0.03/0.87\pm0.11\)；Convey & React 为 \(0.97\pm0.02/0.93\pm0.02\)。每法 5 seeds、每 seed 100 episodes；相对 Delay-Free 有 Holm-corrected \(p<0.01\)，相对 conveyance-only 的增益不显著（\(p=0.16/0.14\)）（§5.3.1）。主要收益是考虑消息传达时间。
- reaction-delay robustness 中，population policy 在训练附近/较短未见 delay 下 success 约 0.96--0.98，但 \(N_L\ge3\) 时显著坍塌，\(N_L=3,4\) 行出现 0 或接近 0；论文承认过长反应无法由 notifier 补偿（Table 2、§5.3.2）。
- Topic-only 短消息在 piloting/driving为 \(0.97/0.93\)，Complete-Utterance 在 driving 达 \(0.97\) 而 notification rate 变高；在快速 piloting 中两者同为 0.97。更加信息化并不始终更好，常被状态变化中断并降低 follow-through（Table 3、§5.3.3）。
- Steakhouse 示例展示 incremental notification “Go down, all stations occupied”：前缀先促成转向，全文随后更新情境知识。它是机制演示而非人类用户研究（§5.3.4）。作者未来方向包括人类验证、fatigue 等个体差异，以及 human-in-the-loop taxonomy refinement（§6）。

## 适用边界与复现

- 适用于低风险、可逆的辅助提醒研究，且能通过真实用户预先测得各人/情境的理解、reaction、follow-through 分布；通知策略应是建议而非自动接管。
- 不可据此直接用于真实驾驶、飞行、医疗或紧急响应。提示词本身可能分散注意、被误解、中断或在错误时刻诱导危险动作；需要独立 hazard analysis、人因研究、法规合规、监控与保守 fail-safe。
- 复现应固定三环境、human task-policy、reaction functions、词速、\((c,M,L)\) taxonomy、LLM prompt/model、PPO/history length、5 seed×100 episode protocol、Holm tests；公开所有 taxonomy 而非仅最终 success，逐一重建 Tables 1--3。
- 推进部署前应做多样化人群的 IRB user study/高保真 simulator，测量实际听觉延迟、attention、信任、误解、疲劳、噪声、语言/口音/无障碍差异与稀有危险事件；并评估 notification 的 cognitive load 和最坏情况，不只看平均 task success。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 time-critical human-agent interaction 与语言辅助决策工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SAWU6614.pdf) 核验 §3--§5 的延迟模型、LLM taxonomy、domain/baseline/统计设置和 Tables 1--3，以及 §6 局限；没有把 synthetic-human 实验的成功率改进误表述为已验证的人类安全效益。
