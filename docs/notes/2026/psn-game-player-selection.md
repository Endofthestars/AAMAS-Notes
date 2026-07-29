---
title: "PSN Game: Game-theoretic Prediction and Planning via a Player Selection Network"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "planning_scheduling", "marl_coordination"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NZAP5192.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02v"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "four_agent_evaluation", "masked_game_approximation", "goal_inference_error", "quantitative_results_deferred"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# PSN Game: Game-theoretic Prediction and Planning via a Player Selection Network

## 一句话总结

PSN Game 从各参与者的过去轨迹学习二元 player-selection mask，仅保留对 ego 有影响的参与者来解一个 masked Nash game，从而减少优化变量；当目标未知时，Goal Inference Network（GIN）先从轨迹推断 2D goal。扩展摘要在 4-agent navigation 中定性展示更快且安全的 receding-horizon planning，但将更多参与者、预测/规划指标与量化结果交给技术报告，故不能据此量化速度、精度或安全优势。

## 方法与证据

- 对 ego \(i\)，mask \(M^i\in\{0,1\}^{N-1}\) 决定哪些其它 agent 进入游戏；masked game 仅保留被选 agent 的状态、动力学、参数和成本项，降低求 Nash equilibrium 的变量规模（§2）。
- PSN-Full 输入所有过去状态，PSN-Partial 仅输入已知观测函数 \(h\) 下的轨迹。Prediction loss 结合 binary、sparsity、trajectory-similarity；Planning loss 用 binary、sparsity 与 cost，显式平衡选人稀疏性和预测/规划目的（§3）。
- GIN 从过去（可部分观测）轨迹回归其它 agent 的 2D goal；训练集来自已知真实目标的 Nash equilibrium 轨迹。receding-horizon 算法先推断目标、再生成 mask、再用 differentiable Nash solver 解 masked game 并更新 ego state（§3、Algorithm 1）。
- AAMAS 摘要测试的是 4-agent navigation，图 2 可视化不同 mask 选择。作者定性称其只用 past trajectories、无需 online tuning、可加速且保持安全，并声称跨任务优于选择基线；摘要没有报告数值指标、置信区间、运行时或更多 agent 的实验，明确指向技术报告获取这些细节（§4）。

## 适用边界与复现

- 适合需要反复求解高维动态博弈且可容忍忽略低影响参与者的预测/规划；被 mask 掉的 agent 仍可能在遮挡、突发机动、非合作或长尾交互中变为关键，不能把 selection 当作安全保证。
- 遮蔽近似、轨迹窗口、binary/sparsity 权重、solver 收敛、已知动力学及 GIN goal error 共同决定性能；用 equilibrium 数据训练也可能与实际人类或非均衡行为分布不符。
- 4-agent 图示无法证明大规模实时可扩展性或 collision safety；应将摘要中“state-of-the-art”视为待从技术报告复核的主张。
- 复现应公开动力学/成本、数据生成与目标分布、PSN/GIN 架构和全部损失权重、mask 预算、solver、seeds；报告不同 agent 数/密度/可见性下的预测误差、碰撞/约束违例、运行时与遗漏关键玩家率，并与全游戏和随机/距离阈值选择比较。

## 与 AAMAS 的关系与核验说明

该文面向多智能体动态博弈的近似求解与规划。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NZAP5192.pdf) 人工核对 mask、两类 PSN、GIN、Algorithm 1 与 4-agent 评测；PDF 的 DOI 字段为空，故元数据暂不填充，也未将摘要外的技术报告结果作为已核验事实。
