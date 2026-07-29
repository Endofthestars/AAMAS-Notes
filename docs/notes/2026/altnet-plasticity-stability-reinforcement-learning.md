---
title: "AltNet: Addressing the Plasticity-Stability Dilemma in Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/KXRD5206"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KXRD5206.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["fixed_reset_schedule", "replay_buffer_dependence", "continuous_control_benchmark_scope", "double_network_compute_cost", "plasticity_proxy_metric", "hyperparameter_sensitivity", "no_real_world_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# AltNet: Addressing the Plasticity-Stability Dilemma in Reinforcement Learning

## 一句话总结

AltNet 用两套“孪生”策略网络轮换：当前 active 网络与环境交互，刚重置的 passive 网络从共享经验学习；到固定间隔后重置 active、让已训练 passive 接管，从而尝试同时恢复塑性并避免重置瞬间的性能坍塌。在 DeepMind Control Suite 的 SAC 实验和 MuJoCo Ant 的 PPO 实验中，它优于比较的重置与非重置基线；结论受固定 reset 周期、回放数据及连续控制基准限制。

## 方法与证据

- 论文将 plasticity loss 定义为网络随训练进行，继续从新经验提升性能的能力下降；性能被作为 plasticity 的 proxy，作者也说明塑性损失的根因尚未确定，诸如 dormant neurons、权重增长和 rank collapse 只是相关现象（§1--§2）。
- AltNet 有两个网络与共享 replay buffer。active 网络采样，passive 网络离策略更新；每 `ResetFreq` 步将 active 完全重置并转为 passive，原 passive 因已从同一轨迹训练而成为新的 active。关键设计是刚重置网络在充分被动训练前永不直接行动（§3）。
- 离策略实验以 SAC 为底座，在 DMC 的 Walker-run、Hopper-hop、Cheetah-run、Quadruped-run 上训练 1M environment interactions；reset interval 固定为 200,000 gradient updates，replay ratio 为 1 或 4，并按网络数与 replay ratio 归一化环境步 reset 频率。比较 SAC、Standard Resets 与 Resetting with Deep Ensembles（RDE）（§4）。
- Table 1 的 normalized AUC 显示 AltNet 在八个“环境×replay ratio”组合中七个最高；跨组合平均 AUC 相对 SAC、Standard Resets、RDE 分别约高 38%、12%、6%。但 Quadruped-run、RR=4 时 RDE 的 AUC 略高，且这些是同一批 DMC 场景的有限 seeds 估计，不是一般 RL 任务的统一保证（§4）。
- 样本效率比较中，AltNet（RR=4）在 Hopper-hop 以及固定 100k/300k/500k interaction budget 上高于所试 SAC replay ratios；论文报告相对最佳 SAC 的 return 比例分别为 52x、1.8x、1.3x。较高 replay ratio 也会增加计算成本且在 RR=32 出现性能退化（§4.1）。
- 消融表明优势不只是双倍参数或更多 policy diversity：将两网络总参数缩至单 SAC 网络规模、或扩展至四网络，都没有带来对应变化。将 buffer 从 1M 缩至 FIFO 400k 会降性能；400k 步后停止 resets 也会退化，同时做两者最差，支持“保留回放+持续轮换重置”的联合作用（§4.2）。
- 在无 replay buffer 的 on-policy 设定，论文于 MuJoCo Ant 训练 PPO/AltNet 10M steps；AltNet 的曲线接近 PPO 的两倍并保持稳定，而 Standard Resets 出现 reset 后坍塌。该结果为 10 seeds（Standard Resets 为 5），说明方法可用于该特定 PPO 场景，但并未覆盖离散动作、多任务或安全约束控制（§4.3）。

## 适用边界与复现

- 适用于长期在线更新、完整重置可恢复学习能力但不能接受控制性能骤降的连续控制 agent；部署至少需有足够算力维护两份可训练网络，并明确 active/passive 切换的故障安全语义。
- 离策略版本依赖共享 replay 数据提供知识连续性；小 buffer、偏移数据或无法留存历史数据会削弱稳定性。on-policy 证据只来自 Ant，不能据此假定对所有 PPO 或无回放算法有效。
- 复现应固定 DMC/MuJoCo 版本、SAC/PPO 细节、网络大小、buffer 规则、200k update 周期和归一化公式、replay ratio、seed 数、eval protocol；报告完整学习曲线、AUC、reset 时刻的性能跌幅、计算量与 wall-clock，而不只取终点回报。
- 真正安全关键控制需在切换前做 policy validation、动作约束/安全 shield、回退控制器和在线异常检测；也应对 reset frequency、队列训练充分度、buffer 老化、非平稳任务与现实传感噪声进行压力测试。作者也将自适应地按环境/replay ratio 选择 reset frequency 列为未来工作（§6）。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 关于持续/在线强化学习的 agent engineering 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KXRD5206.pdf) 核验双网络架构、DMC/SAC 设置、Table 1 的 AUC、样本效率和 buffer/reset 消融、Ant/PPO 比较及 §6 局限；没有把基准曲线稳定性表述为现实系统的安全认证。
