---
title: "Nested Training for Mutual Adaptation in Human-AI Teaming"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/OFJL6947"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OFJL6947.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03n"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "simulated-partners", "nested-ipomdp-approximation", "latent-belief-model", "user-study-pending"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Nested Training for Mutual Adaptation in Human-AI Teaming

## 一句话总结

本文用有限嵌套 I-POMDP 将“人会随着 AI 调整”纳入训练：先让 Level-1 human policies 面对固定 Level-0 robots，再训练 Level-2 robot 与这些会适应的 human policies 协作，并从交互历史学习 latent belief。作者在 8 个未见自适应模拟伙伴上报告优于 LIAM、LILI、PACE 与 Generalist；尚未有人类用户研究。

## 方法与证据

- 目标场景有多个协调均衡，且双方会相互适应。采用 level-2 reasoning，因为作者称人类信念建模很少超过二层（§2）。
- Level-1：每个 human policy 针对有限个固定 Level-0 robot policies 训练；Level-2：robot policy 对这组 Level-1 adaptive human policies 训练。下层策略固定而非同步共同适应，作者在附录中论证这可避免收敛到单一协调 convention（§2）。
- 历史 $h_t$ 经 $z_t=f_\theta(h_t)$ 压缩为 latent embedding，策略条件化为 $a_t\sim\pi_\theta(a\mid o_t,z_t)$，用以近似 belief update（§2）。
- 在 8 个未见 adaptive partners、10 rounds 的短评估（每轮 5 episodes）中，Proposed Method 平均 success 0.90，对比 Generalist 0.575；延长为每轮 25 episodes 后为 0.935。Table 1 还列出各 partner 成功率，作者解释方法出现“先承诺”以回应 Level-1 partner 的等待，而基线容易在 recipe choices 间震荡（§3）。

## 适用边界与复现

- 伙伴是训练出的模拟策略，不是实际人类；Level-2 I-POMDP、latent embedding 与有限人口均是近似。高模拟成功率不能直接表明人机团队信任、理解或长期安全。
- 复现应提供双人游戏/多均衡任务、Level-0 robot population、Level-1 训练细节、隐变量架构、伙伴种子、10-round protocol、每轮 episode 数、success 定义及所有 baseline 设置。论文自己将 user studies、质性行为分析与 mixed-motive 场景列为未来工作。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OFJL6947.pdf) 人工核对嵌套训练、评估协议及 Table 1；未将模拟伙伴泛化结果表述为真实人类适应性的证据。
