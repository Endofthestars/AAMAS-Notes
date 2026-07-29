---
title: "Strategic Communication under Threat: Learning Information Trade-offs in Pursuit-Evasion Games"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["marl_coordination", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: "10.65109/XVYB5151"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XVYB5151.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04e"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["pursuit-evasion", "strategic-communication", "partial-observability", "opponent-modeling", "simulation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Strategic Communication under Threat: Learning Information Trade-offs in Pursuit-Evasion Games

## 一句话总结

SHADOW 在 Pursuit-Evasion-Exposure-Concealment Game 中同时学习连续导航、是否查询对手位置和对手位置预测：查询能减少不确定性但暴露 pursuer 位置并可能被消灭，策略据此权衡捕获与隐蔽风险。

## 方法与证据

- PEEC 的终止为捕获、pursuer 被射击或超时逃脱；查询时双方获得带随机噪声的对方位置。SHADOW 由 Navigation、离散 Query Decision 与基于时序记忆的 Opponent Modeling modules 组成（§1、§3–4）。
- 训练 pursuer/evader 20,000 episodes，batch 32，并在 500 held-out episodes 评估；对照无/随机/周期通信和 MultiHead PPO、P-DQN、HyAR、LIAM，且对 opponent model/LSTM 做 ablation（§5）。
- 表 1 中 SHADOW pursuer 的 $P_{win}=0.620\pm0.042$、$P_{shot}=0.350\pm0.041$，较周期 $k=40$ 的 0.576/0.416 更高胜率且较低被射风险；LIAM 为 0.570/0.428。cross-strategy 结果显示对不同 evader 有差异，非全面统治（§5）。

## 适用边界与复现

- “threat”由模拟的射击概率、半径、速度和噪声定义，不能直接支持军事、执法或现实监控部署判断；提高捕获率与降低伤害/合法性不是同一目标。
- 复现需公开非线性动力学、reward/terminal costs、通信噪声、攻击/捕获条件、observation history、network/LSTM/optimizer、baseline tuning、500 test seeds 和跨策略矩阵。高风险应用还需人类监督、规则约束和独立安全审计。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XVYB5151.pdf) 人工核对 PEEC、SHADOW 模块、实验协议和表 1；未将仿真胜率或“成本”定义外推为真实对抗环境的安全承诺。
