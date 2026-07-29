---
title: "Conservative Equilibrium Discovery in Offline Game-Theoretic Multiagent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["marl_coordination", "game_theory_mechanism", "agent_engineering"]
dblp_key: ""
doi: "10.65109/XEYY6214"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XEYY6214.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04h"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["offline-game-solving", "psro", "equilibrium-selection", "dynamics-ensemble", "regret"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Conservative Equilibrium Discovery in Offline Game-Theoretic Multiagent Reinforcement Learning

## 一句话总结

COffeE-PSRO 将 offline game-solving 看成候选近似均衡的保守选择：以固定轨迹训练 ensemble dynamics，使用模型分歧衡量策略及潜在单边偏离的不确定性，并在 PSRO 中偏向真实游戏 regret 更可能较低的解。

## 方法与证据

- 离线数据通常不足以覆盖一个候选 profile 及全部 unilateral deviations，故不能验证 true-game equilibrium；方法以低 regret 的相对概率而非直接验证作为目标（§1、§4）。
- ensemble MLP 学 transition、reward、observation 和合法动作；response objective 在回报、当前 response target 的不确定性和潜在 strategic deviations 的不确定性间权衡，并给出 pessimistic-regret heuristic 的 meta-strategy solver（§1、§4）。
- 论文在 sequential bargaining game 实验称 COffeE-PSRO 较 tested offline baselines 输出更低 regret 的策略，并分析 model fidelity、dataset variation 和算法组件的关系；证据范围主要为该实验域（摘要、§1）。

## 适用边界与复现

- ensemble disagreement 是模型不确定性的代理，不是实际 regret 的可认证上界；固定数据若遗漏关键偏离，保守惩罚仍可能选到错误均衡。
- 复现需公开轨迹数据生成/coverage、game 参数、ensemble 数量和训练、uncertainty/reward 权重、PSRO population、MSS heuristic、regret 的真实 simulator 评估及 seeds。应在多类 mixed-motive games 比较而非只依赖 bargaining。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XEYY6214.pdf) 人工核对问题表述、ensemble 与 COffeE-PSRO 设计；未将离线估计的低 regret 表述为已验证 Nash equilibrium。
