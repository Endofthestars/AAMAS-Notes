---
title: "Learning to Maintain Safety Through Expert Demonstrations in Settings with Unknown Constraints: A Q-Learning Perspective"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/RJIB1203"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RJIB1203.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["demonstration_coverage_dependency", "discriminator_miscalibration", "online_unsafe_exploration", "simulation_only", "safety_cost_proxy", "no_formal_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Learning to Maintain Safety Through Expert Demonstrations in Settings with Unknown Constraints: A Q-Learning Perspective

## 一句话总结

SafeQIL 以人类安全示范的状态分布为支持集，用 discriminator 对在线状态的“像示范/可能安全”程度做软估计，并在示范外状态给 SAC critic 加 demonstration-informed 上界与安全 penalty，使策略在继续在线优化任务 reward 时更悲观。它在 4 个 Safety-Gymnasium 仿真任务中降低环境 safety cost；但学习到的是示范覆盖下的风险代理而非真实未知约束，仍需在线探索，不能构成零违例或部署级安全保证。

## 方法与证据

- 问题假定 task reward 可观测、约束 cost/约束本身不可观测，专家示范被视为安全执行；论文明确不恢复实际 constraint set 或 cost function，而是学习安全状态/动作附近的策略（§1–2）。因此“安全”与示范质量、一致性和覆盖度绑定；若专家遗漏危险区、做出风险行为或目标任务改变，代理就会失真。
- SafeQIL 把每步 return 写为：状态被判为安全时使用环境 task reward \(r_d(s,a)\)，否则用 action-independent safety reward/penalty \(r_s(s)\)，再以此学习 Q（§3）。论文的 theorem 依赖 binary safety indicator、示范外 \(r_s\le0\) 等条件；实际算法使用 probabilistic discriminator，作者也说明该不等式不再保证成立。
- 实现以 SAC 为 backbone，维护 online replay buffer 与 demonstration buffer；discriminator 估计 state 属于示范分布的概率，safety reward 由其映射为负值。对示范外 online states，以 cosine-similarity 检索的最近示范状态 Q 值作 local upper bound；示范内仍按 SAC 更新（§4.2, Alg.1）。这可抑制 OOD 价值过估，但 nearest-state 相似度不是动力学可达性、碰撞距离或物理约束证明。
- 算法仍在环境中采样 online actions，再用事后 reward/state 更新（Alg.1）。训练期间没有 shield、barrier/filter、可验证 reset 或硬约束执行器；在真实系统上这种探索本身就可能造成不可接受的安全事件。
- 评测为 SafetyPointGoal1-v0、SafetyPointCircle2-v0、SafetyCarButton1-v0、SafetyCarPush2-v0 四个 Safety-Gymnasium 仿真任务；每 task 用 40 条键盘控制的人类示范，训练后 40 个 evaluation episodes，3 个 independent seeds 报 mean±std（§5.1）。没有真机、传感噪声、延迟、失效、迁移或长期非平稳测试。
- 对比 ICRL、VICRL、SAC-GAIL、SAC/PPO 与人类示范；ICRL/VICRL 在 PointGoal 上从其原论文/实现的 3/9 组配置 extensive tune，SafeQIL/SAC-GAIL 用 Stable-Baselines3 SAC，baseline 只调每 task regularization coefficient（§5.1）。各方法的调参范围和训练交互预算仍会影响 reward–cost trade-off 的公平性。
- PointGoal：SafeQIL reward/cost 为 5.27±1.85 / 34.22±2.71，SAC 为 27.47±0.21 / 49.15±2.21；Circle：27.06±4.10 / 29.28±8.41，而 VICRL cost 更低 5.49±0.81（Tables 1–2）。作者按 reward 与 cost 的 trade-off 选“best”，因此不能只用成本或单一胜者概括。
- interaction-heavy Button/Push 中 SafeQIL 分别为 reward/cost −3.81±3.05 / 70.11±72.96、−0.62±0.65 / 57.20±30.02；VICRL 在 Button cost 34.65±23.36、Push 55.80±71.45 但 reward 为负（Tables 3–4）。高方差、负 reward 和仿真 cost 说明“更安全”不等于完成任务、稳定控制或无事故。
- PointGoal ablation 移除 cosine retrieval 或 constraint term 时 cost 标准差增大（30.25±19.10、29.02±14.03 vs original 34.22±2.71），支持组件对该设置的稳定性作用（Table 5），不证明 discriminator 已校准或对未见约束可靠。作者明确限制是示范 coverage/quality、hard-OOD discriminator miscalibration 与简单 closest-demo anchor 可能导致过/欠保守（§7）。

## 适用边界与复现

- 可作为从安全示范中做 state-level pessimistic value learning 的仿真研究基线；高风险机器人、交通、医疗或工业系统不应以它单独替代已知约束、法规、独立 hazard analysis、formal monitor 或 human override。
- 实际部署前应先以 deterministic safety shield/CBF、碰撞/速度/力/工作区硬限制、可信状态估计、emergency stop 和 runtime monitor 约束所有动作；SafeQIL 输出只能作为 shield 内的性能策略。需记录训练与运行时 cost violations，而非只报告最终平均值。
- 应在示范缺失/噪声/冲突、OOD 初始状态、动态障碍、传感/动作延迟、domain randomization、不同 reward scales 和 adversarial discriminator inputs 下评估，报告每 episode 最大/累计 cost、违例率、CVaR、任务成功、恢复时间与置信校准。3 个 seed/40 episodes 不足以论证稀有失效风险。
- 复现应使用作者公开仓库，固定 Safety-Gymnasium版本、40 条人类轨迹与采集协议、state preprocessing、discriminator architecture/loss/threshold-to-penalty mapping、SAC/critic/entropy/replay/nearest-demo/cosine配置、interaction budget、ICRL/VICRL/SAC-GAIL tuning grids、seed/episode 与 cost/reward metric；还应运行真值约束已知的对照，量化 learned support 与真实安全集的偏差。

## 与 AAMAS 的关系与核验说明

这是从专家示范学习未知约束下安全行为的 inverse constrained RL 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RJIB1203.pdf) 核对 Q-value safety/reward mixing、discriminator/upper-bound SAC 算法、4 个 Safety-Gymnasium 任务、示范与评测 protocol、基线、表格/ablation与作者明确限制；没有把示范分布相似度、仿真 safety cost 或平均改善误写为真实约束识别、无在线风险或形式化安全认证。
