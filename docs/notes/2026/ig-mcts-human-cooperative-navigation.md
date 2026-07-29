---
title: "IG-MCTS: Human-in-the-Loop Cooperative Navigation under Incomplete Information"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "robotics_embodied", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/OBKI3637"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OBKI3637.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03c"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "simulated_maze", "learned_human_perception_model", "small_user_study", "eye_tracking_proxies"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# IG-MCTS: Human-in-the-Loop Cooperative Navigation under Incomplete Information

## 一句话总结

IG-MCTS 在 CoNav-Maze 中让拥有局部准确观测的机器人与持有不准确全局地图的人协作：MCTS 同时优化导航奖励和由 Neural Human Perception Model 预测的地图更新信息增益。113 条众包 mapping episodes 训练感知模型；14 名研究生的 within-subject 眼动研究中，作者报告相对 teleoperation/instruction-following 通信降低逾一个数量级（摘要称逾 97%）、认知负荷 proxies 降低且步数可比。这不能证明现实环境的人类理解、信任或导航安全。

## 方法与证据

- action 可为移动或发图；目标函数将 task reward 与 \(\|x_{t+1}-x_t\|\) 信息收益相加。NHPM CNN 预测人对墙的 add/remove probability maps，估计期望信息奖励（§1--3）。
- MCTS 对未探索格以墙概率 0.5 建模；movement 使用 feasibility-weighted backup，communication 用 learned human model（§3）。
- NHPM 在 held-out maze 上优于逐 cell GLPF；用户研究比较三种控制，报告 pupil dilation、blink、attention shifts和 communication/steps，但扩展摘要未给完整效应量、显著性、真实机器人或多样人群评估（§4）。

## 适用边界与复现

- 需公开 maze/data split、NHPM inputs/labels、MCTS horizon/weights、communication cost、baselines、user-study protocol及全部 eye metrics；模型错设会把“信息增益”导向不必要或误导通信。
- 眼动指标是负荷 proxy，不能单独推断理解、信任或安全；真实部署应验证感知/通信延迟、隐私、误导信息和停止/人工接管机制。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OBKI3637.pdf) 人工核对 CoNav-Maze、NHPM、IG-MCTS 和 14 人研究；未将模拟/小样本结果外推为现场安全收益。
