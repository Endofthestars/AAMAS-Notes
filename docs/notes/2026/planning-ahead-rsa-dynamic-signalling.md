---
title: "Planning Ahead with RSA: Efficient Signalling in Dynamic Environments by Projecting User Awareness across Future Timesteps"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/BRGK2754"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BRGK2754.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["perfect_future_state_assumption", "user_belief_model_misspecification", "alert_suppression_or_delay", "simulation_only_evidence", "safety_critical_overclaim"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Planning Ahead with RSA: Efficient Signalling in Dynamic Environments by Projecting User Awareness across Future Timesteps

## 一句话总结

论文把 Rational Speech Act (RSA) 扩展为 d-RSA：用对用户信念/注意力的预测与有限时域搜索，同时决定何时、以多具体的方式发送告警。在 800 个合成 Drone World 试验中，带 user priors 和 planning 的版本优于三个消融基线；但该证据依赖固定人工词表、已知未来世界状态和近似/预设的用户意识，不能证明在真实高风险场景中可安全延迟或压缩告警。

## 方法与证据

- 系统把环境状态、属性、有限 utterance 词表、时域 H、用户 belief distribution 与 reward 形式化。对每个 critical property，reward 衡量消息后用户 belief 与真实值的对齐（Eq. 3--5）。长消息占用多个 timestep，其间只能发送零注意力的 `(X)`，因此信息量与时机存在显式机会成本（§3--4.2）。
- 基线 Dynamic RSA (d-RSA) 追踪 posterior 成为下一 timestep prior，但使用 uniform user priors 且贪心选当前最优消息。d-RSA + Priors 以已知的用户先验/历史 belief 条件化 Listener；d-RSA + Planning 以 uniform priors 搜索序列；完整 d-RSA++ 将两者结合，枚举 utterance sequence 并最大化累计 reward（Eq. 7--9）。
- 评测是作者构造的 800 个模拟 Drone World trials：4 架无人机、各 6 个属性、共 24 properties、7 timesteps；变化包括 2--4 个 critical properties、出现时间密度，以及预设的初始用户 awareness。为取得每个 trial 的最优方案，作者以 breadth-first search 枚举至 H=7 的序列（§5.1）。这不是现场用户研究，也不是开放文本/生成式 LLM 评测。
- 完整模型相对三种变体的 total reward 更高（pairwise comparisons `p < 0.01`）；planning 关联 \(\beta=0.31, SE=0.02, p<.001\)，belief tracking 关联 \(\beta=0.22, SE=0.02, p<.001\)，组合交互 \(\beta=0.05, SE=0.02, p=.019\)。增益在 critical properties 更多、出现更密集的模拟场景最大（§6.1、Figure 2）。
- 完整模型也产生更多不同具体度的消息，并在低意识 critical properties 上具有更短 first-alert delay；文中以未在时域内提及的属性按 delay=7 计入（§6.2--6.3、Figure 3）。这些是设计的 belief/reward 量，不等于人类理解、信任、正确响应或事故率的实测改善。

## 安全边界与复现

- 核心输入并非由系统可靠地在线观测/推断：实验给定真实世界演化、用户初始 beliefs 与有限的 message-to-property lexicon。作者明确承认 perfect knowledge of user awareness 和 future world states 是为了可控模拟而作的理想化，真实部署须面对不确定规划（§7.2）。错误的用户模型会使系统把用户当作“已知”而发送过于简略的告警，或将真正紧急事项延后。
- 模型为最大化 belief-alignment reward 而允许选择 silence、简短 beep 或延迟某些问题；在飞行、医疗、应急、能源等场景，通信保守性、可执行性、告警确认、冗余通道和法规优先级不能由这个单一 reward 替代。不得把 "更少/更晚的消息" 自动视作安全或更少认知负担。
- breadth-first enumeration 在 H=7 和手工有限词表下可行，不代表随环境规模、语言开放性、消息长度、多人协作或不确定未来扩展后仍实时可用。应报告搜索复杂度、超时/fallback、词表覆盖率、参数与 domain-specific criticality 定义；生产环境还需可信状态估计、在线校准、uncertainty-aware planning、审计日志和人工 override。
- 论文没有人类受试实验、真实无人机/控制室部署、事件检测准确率、用户个体化估计误差、告警疲劳、对抗输入或伤害结果。任何实际主张都应通过分层 urgency、独立用户研究、仿真到现场转移、misspecified-belief 压力测试、recall/false-negative 指标与安全案例审查验证。
- 在高风险界面中，critical event 的强制告警、确认与人工优先权应在优化器之外受硬约束；不得让语言/规划模块自主降低法定或安全关键告警等级。

## 与 AAMAS 的关系与核验说明

这是 human-aware planning 与 pragmatic communication 的 AAMAS 研究论文。笔记基于 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BRGK2754.pdf) 核验 d-RSA 的 temporal belief update、user-prior 与 horizon planning 变体、800 个 Drone World trials、H=7 breadth-first search、回归结果和作者对 perfect-awareness/future-state/hand-crafted lexicon 的限制；未把模拟 reward 或延迟改善表述为真实安全关键部署保证。
