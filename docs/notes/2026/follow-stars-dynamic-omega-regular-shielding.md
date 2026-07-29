---
title: "Follow the STARs: Dynamic ω-Regular Shielding of Learned Probabilistic Policies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/WLFP2035"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WLFP2035.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["known_transition_graph_requirement", "strategy_template_assumption", "omega_regular_model_scope", "abstract_model_mismatch", "almost_sure_vs_sure_scope", "runtime_parameter_tuning", "simulation_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Follow the STARs: Dynamic ω-Regular Shielding of Learned Probabilistic Policies

## 一句话总结

STARs 用从已知 MDP 图和 ω-regular 规格综合出的 strategy template，在运行时重归一化 learned stochastic policy 的动作分布；可调参数 \(\gamma\) 用于在 liveness 强制频率与名义奖励之间取舍，并支持规格/动作可用性变化。其正确性是模型内结论；LunarLander 只在严重简化的 2D 抽象上构造 shield，87% 的落在 helipad 是 200 次模拟的经验结果，不能视为真实连续系统的安全或必达保证。

## 方法与证据

- 目标覆盖整个 ω-regular 类，而不仅是“永不出错”的 safety：strategy template 规定 unsafe actions、co-live actions 与 live groups，shield 根据有限 history 的 counters 对 nominal action distribution 截断/重归一化（§1--3）。它是 post-shielding，会覆盖 policy 的动作而不是重新训练；规格错误或 transition graph 遗漏仍会被忠实执行。
- Theorems 1--3 将 shielded policy 满足 template、从而（几乎）必然满足 \(\Phi\) 及最小干预性质联系起来；Theorem 4 在 rewardful MDP 的额外前提下给 nominal reward 的 \(\epsilon\)-closeness，Theorem 5 对 sure satisfaction 给可通过 \(\theta,\gamma\) 调整的 even-color visit frequency（§3--4）。结论依赖正确的 MDP/game graph、可综合 winning template、起点/赢域等前提；almost-sure 情况的频率还取决于未知 transition probabilities，作者明确不保证任意 \(\delta\)。
- FactoryBot 使用 383 个随机 grid（189 Far、194 Close，尺寸 5--13），以 100,000 steps 度量平均 reward 与 Büchi visits；增大 \(\gamma\) 提升 Büchi frequency 却降低接近最大平均 reward 的程度，且距离使 trade-off 更陡（§4.1、Fig. 4）。这是可调行为而不是无需调参的“最小干预”。
- Overcooked-AI 实验基于已知有限 MDP，LTL recipe 译为 Büchi objective；枚举的 game graphs 为约 68,000 至 2.2M states，最大 synthesis 约需一小时的部署前计算（§4.2）。该可扩展性不等于面对未知环境、部分观测或在线动力学变化仍可快速重算。
- LunarLander 中真实环境是隐藏 8D 连续 MDP，作者明确说无法计算 provably correct shield；他们仅离散 x/y 为 60×60 grid，并假设各控制动作使 lander 走一个 cell（§1.1、§4.3）。该抽象忽略真实复杂动力学，故形式化模型内保证不能迁移到该实验。
- LunarLander 的 PPO baseline 训练 50,000 steps，200 随机 seeds 下 unshielded/safety shield/STARs 在 helipad 落地分别为 10.5%/31%/87%，成功落地平均步数为 5868/8082/4650（§4.3）。这些不含置信区间、真实飞行器、传感误差或 OOD 条件；87% 也直接说明并非必达。

## 适用边界与复现

- 适用于有可信离散 transition graph、可形式化为 parity/LTL/ω-regular objective、且能接受运行时动作改写的离线验证或受控 CPS 研究。部署前应对模型覆盖、规格、template synthesis、winning region 和 actuator failure update 做独立审查。
- \(\gamma\) 与 \(\theta\) 是任务/上下文相关控制量：提高 liveness 强制可损失 reward，过低又可能使关键进展稀疏。名义策略如果本已满足 objective，intervention 的意义和测量也不同；“minimal”限于论文的 action-distribution distance/理论条件。
- 不应把基于 2D LunarLander abstraction 的成绩推广到连续控制、真实航空、机器人安全认证或未建模 failures。连续动力学、延迟、随机转移、感知误差、未知 action availability 与 spec conflicts 都需再验证。
- 复现需固定 MDP/game extraction、automaton/parity translation、strategy-template solver、nominal policy、\(\gamma,\theta\)、runtime update logic、FactoryBot generator/Far-Close 划分、Overcooked layout/recipe 和 LunarLander 改动/60×60 abstraction/200 seeds。报告是否是 sure 或 almost-sure、template/graph size、synthesis/online latency、reward/频率分布、覆盖动作、失败轨迹和模型偏差压力测试。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 runtime shielding、formal verification 与 learned policy adaptation 论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WLFP2035.pdf) 核验 STARs、Theorems 1--5、已知有限 MDP 前提、383 FactoryBot instances、Overcooked 的状态规模及 LunarLander 抽象/200-seed 数值；没有把模型内 ω-regular 满足或 87% 模拟落地误写为真实连续系统的通用安全保证。
