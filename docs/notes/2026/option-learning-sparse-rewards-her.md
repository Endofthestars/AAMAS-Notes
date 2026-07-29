---
title: "Enabling Option Learning in Sparse Rewards with Hindsight Experience Replay"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: "10.65109/HIWW4582"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HIWW4582.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "sparse_reward_benchmarks", "reward_relabeling_assumptions", "simulated_robotics", "auxiliary_goal_shaping"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Enabling Option Learning in Sparse Rewards with Hindsight Experience Replay

## 一句话总结

MOC-HER 将 future-goal Hindsight Experience Replay 加入 Multi-updates Option Critic；面对物体位置才决定成败的 manipulation，2HER 额外把未来 end-effector position 当作虚拟交互目标，并以任务完成与 agent-object 接近的加权奖励训练。作者在 Gymnasium Robotics Fetch 中报告 MOC-2HER 最高约 90% success，而 MOC/MOC-HER 低于 11%；这说明特定环境/奖励塑形能帮助 option discovery，并不证明 options 具备可迁移的语义或真实机器人可靠性。

## 方法与证据

- MOC-HER 在每个 episode 后用 HER 的 `future` strategy，从后续 states 抽取 \(k\) 个 achieved goals，重新计算 sparse rewards；buffer 包含 action、active option、state/next state 和 reward（§2）。这假定目标可事后替换、环境 reward 可正确重算；在不可逆、带安全约束或目标依赖隐藏历史的任务中，relabeling 可能无效或改变学习问题。
- 2HER 针对 object manipulation：除了 future object-position goal，还从 future agent end-effector positions 采 virtual goals。任务 reward 在 object 到达 goal 时为 0、否则 −1；interaction reward 在 effector 接近 object 时为 0、否则 −1，最终 \(r=(1-C_r)r_{goal}+C_r r_{object}\)（§2）。\(C_r\)、距离阈值 \(\epsilon\) 与虚拟目标定义会改变最优激励，可能诱导“接近物体”而非稳健完成操纵。
- relabeling 仅限于出现足够 object displacement 的 trajectories，并让每 transition 的 relabeled-goal 数 \(k\) 从高值随训练衰减；HER buffer 与原 MOC buffer 合并后更新所有 options（§2）。这是为效率/稳定性设计的启发式，摘要未报告阈值、schedule、buffer mixing ratio、option termination/interest 的完整配置或消融。
- 在 FetchReach，不同 option 数下 HER variants 可解而 MOC/IOC 在训练范围内未学出可行 policy；在 FetchPush/Slide/PickAndPlace（4 options）2HER variants 一致优于单目标 HER 与原 baselines，图的阴影是 10 runs 标准差（§3）。摘要称 up to 90% vs 11%，但没有列逐任务最终均值/CI、sample budget、sim-to-real、碰撞/力约束或 option reuse transfer。

## 适用边界与复现

- 适合多目标、可重算 goal-reward 的 sparse-reward HRL 仿真研究；不要将 hindsight relabeling 的成功率作为真实机械臂接触安全、物体泛化、长任务可靠性或可解释 skill library 的保证。
- 复现需公开 Fetch/Gymnasium version、goal/observation/reward/\(\epsilon\)、MOC/IOC/2HER 实现、future strategy、\(k\) schedule、object-displacement filter、\(C_r\)、options 数、network/optimizer、seeds、evaluation episodes与成功定义。论文给出代码/完整版本链接，但本笔记仅核验 AAMAS 摘要。
- 应测试不同 object/mass/friction、视觉/状态噪声、目标不可达、奖励误设、variable horizon、更多 options、OOD goals和 transfer；报告 interaction-success 与 task-success 的分离、sample efficiency、方差、failure types与 reward hacking。真实部署需感知/力控、action bounds、碰撞监测、人工监督和安全回退。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 hierarchical RL、option learning 和 robotics benchmark 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HIWW4582.pdf) 核验 MOC-HER/2HER、加权双奖励、Fetch 任务与 10-run 图示；没有把虚拟目标的基准收益写成真实机器人或通用 option 学习结论。
