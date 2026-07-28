---
title: "Rethinking Priority Scheduling for Sequential Multi-Agent Decision Making in Stackelberg Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "game_theory_mechanism", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RNLD7242.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["priority_order_permutation_scaling", "sequential_observability_scope", "grouping_restriction", "limited_mujoco_evaluation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Rethinking Priority Scheduling for Sequential Multi-Agent Decision Making in Stackelberg Games

## 一句话总结

HPA 将 N-level Stackelberg MARL 的 agent execution order 作为高层 option，按状态动态选择分组 agent 的排列，低层按该顺序观察先前动作并训练；在四个分组 Multi-Agent MuJoCo 任务中获得较高 episode reward，但其收益依赖顺序可观测、共享奖励、分组方式和可枚举排列，不能外推为任意多 agent 的通用最优排程。

## 方法与证据

- 论文形式化 Sequential/ N-level Stackelberg Markov Game：优先级高的 agent 先行动，后续 agent 观察 $(s,a_1,\ldots,a_{i-1})$ 并作 best-response 式更新。通过一阶最优性/反向归纳分析，作者主张一般情形下改变 execution order 会改变对应的 Stackelberg equilibrium point；此结论针对其连续策略、可微 payoff 的推导，并不说明每个状态或每种 order 都严格改变回报（§2–3）。
- HPA 把 $n$ agent 的每个完整 order 抽象为一个 option。高层 option-critic/PPO policy 在 state 中采样 order，termination function 决定是否结束当前 option；低层采用修改输入为 $(s_i,a_1,\ldots,a_{i-1})$ 的 HAPPO，并按选定顺序执行（Algorithm 1、§4）。
- 两层使用慢—快时间尺度：上层每 $k$ 步选 order，累计 external reward 为上层 reward；上层 advantage 均摊为下层 intrinsic reward，并与 external reward 合并。$k=1$ 时退化为没有多步指导；$k$ 过大则无法及时因姿态变化重排（§4.1–4.2、§5.4）。
- 评估使用共享 reward、连续动作的 Multi-Agent MuJoCo：HalfCheetah 与 Walker2d，各用 2×3 或 3×2 分组。为缓解 order 数的阶乘增长，论文仅对 3 个 group 的 $3!$ 排列作 option；比较 MAPPO、HAPPO、HATRPO、STEP（§5.1、§5.3）。
- 报告的 mean episode rewards 中 HPA 在四个任务最高：HalfCheetah 2×3/3×2 为 5176/5345，Walker2d 2×3/3×2 为 4532/4232；对不同固定顺序，图示结果差异明显。ablation 在 HalfCheetah 2×3 中显示上层会在 01 与 10 间切换，作者解释为姿态相关的重排（Figures 4–8）。

## 局限与复现

- order option 数随可排序实体为 $n!$；分组虽降低搜索空间，却排除了组内顺序与跨组交织顺序。作者明确指出 grouping 同时限制某些 sequence 的潜在性能，且 partition 本身影响游戏结果，因此不能声称 HPA 已解决大规模优先级优化。
- 低层依赖后序 agent 接收前序动作，且实验为 cooperative shared-reward MuJoCo。异步通信延迟、部分可观测、隐私限制、竞争激励或真实组织中不能公开前序动作时，其 Stackelberg 信息结构与 HPA 输入不成立。
- “equilibrium shifts”是特定连续策略最优性分析，不等于深度 RL 的有限训练一定收敛到精确 Stackelberg equilibrium，也不保证 learned high-level schedule 的全局最优；论文结果是 finite benchmark return，而非均衡误差/后悔值验证。
- 对比局限在四个分组控制任务，论文未给跨 seed 方差、训练预算敏感性、排列数扩展曲线或真实调度成本；episode reward 不包含切换/协调/通信开销。HPA 高层计算和频繁调整本身也可能改变公平比较。
- 复现应固定 MuJoCo 版本、agent partition、默认/所有候选顺序、$k$、PPO/option-critic 超参、seed 与训练步数；报告每个 order 的结果、上层 option occupancy/termination、均值方差以及在不允许观察前序动作时的退化情况。

## 与 AAMAS 的关系与核验说明

该文研究层级博弈中的动态行动优先级，连接 MARL 协调与顺序决策。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RNLD7242.pdf) 核对 Stackelberg order 设定、HPA 两层算法、四个 MuJoCo 分组结果与作者的排列增长限制；不将基准内 reward 增益外推为一般多 agent 排程或均衡求解保证。
