---
title: "Scalable Coalition Formation for Extremely Large Collectives"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["robotics_embodied", "resource_allocation", "game_theory_mechanism", "agent_engineering"]
dblp_key: ""
doi: "10.65109/MGGH7353"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MGGH7353.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05d"
spark_draft_verdict: "source_grounded_draft_needs_revision"
spark_qa_verdict: "needs_revision_for_page_anchor_preemptive_reformation_and_belief_sync_detail"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_program", "extremely_large_robot_collectives", "type_based_coalition_formation", "hedonic_game", "leader_follower_abstraction", "finite_potential_game_author_claim", "static_experiment_only", "trial_count_and_distribution_absent", "communication_requirement_not_network_performance", "dynamic_reformation_future", "no_real_world_deployment"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_page_anchor_nash_stability_optimality_communication_and_dynamic_reformation_boundary_check"
escalation_verdict: "pass_after_p4015_trial_level_optimality_and_static_only_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted scalability-guarantee check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Scalable Coalition Formation for Extremely Large Collectives

## 一句话总结

本文利用机器人类型冗余，把超大规模集体的联盟形成协商压缩到 leader 层，并在最多 10,000 个机器人的静态试验中报告运行时间、total communication requirement 与 trial-level optimal-solution 改善；动态联盟重组、真实通信网络和长期自主仍属于后续研究。

## 问题：规模、异质性与通信

Extremely Large Scale Collectives（ELSCs）包含数千个机器人。联盟形成需要把机器人分成面向任务的团队，组合空间会随集体规模迅速增长；分布式拍卖或协商又会产生大量消息（§§1–2，p. 4014）。

论文利用一个结构性假设：大规模制造的机器人虽然总数很高，但不同能力类型的数量相对较少，同类型机器人因而形成可压缩的冗余。研究据此把逐机器人协商改写为按类型和 leader 分解的协商。

## 三种联盟形成机制

### GRAPE-S

GRAPE-S 使用 anonymous hedonic game。机器人维护所有机器人任务分配的 belief，并依据联盟规模加入对自身有利的联盟。它能处理异构、多能力集体，但全局 belief synchronization 要求大量机器人间通信（§2，p. 4014）。

### LeaderGRAPE-S

LeaderGRAPE-S 依据能力类型关联 leader，并把原问题拆成多个 leader-centric 子问题。每个 leader 对应共享其能力的 follower 子群，子群内部继续使用 GRAPE-S。减少每个 hedonic game 的参与者可以降低协商量，但论文仍认为它的总通信需求对通信受限环境过高（§3，p. 4014）。

### LN-GRAPE-S

Leader Negotiation with GRAPE-S（LN-GRAPE-S）进一步只在 leader 集合 \(L\) 上形成 hedonic game：

- leader 维护各任务已分配能力的 belief；
- 每轮把所需 followers 分配给边际效用最高的任务；
- leaders 广播更新后的 belief，并同步到更新最充分或最近更新的状态；
- belief 更新持续到所有 leaders 对 follower 分配满意；
- 同类型机器人具有相同边际贡献，因而可以用 batch allocation 代替逐机器人谈判。

论文把 LN-GRAPE-S 称为 finite potential game，并称其保证 Nash stability（§3，p. 4014）。这项作者声明只属于给定 leader-level 博弈；三页稿没有在此给出证明，也不能由此推出全局最优、固定收敛速度、网络可靠性、动态重组稳定性或其他两种算法的同类保证。

## 静态预实验设置

Figure 1 与 §4 均位于 p. 4015。图比较 GRAPE-S、LeaderGRAPE-S 和 LN-GRAPE-S 的 algorithmic runtime 与 total communication requirement：

- 集体规模为 1,000、5,000 和 10,000 个机器人；
- §4 说明集体共有 10 种 capabilities；
- 每个机器人提供两种 capabilities；
- `% Tasks` 表示任务数占集体规模的百分比；
- 正文报告 1%、10% 和 50% tasks 的比较；
- 10,000 robots、50% tasks 对应 5,000 个任务。

论文没有披露 trial 数、实例生成器、能力与任务分布、随机种子、运行平台、实现语言、网络拓扑、带宽、延迟、丢包或统计置信区间。

## 运行时间

在作者报告的静态实验中（§4，p. 4015）：

- LeaderGRAPE-S 在 10,000 robots、50% tasks 时平均比 GRAPE-S 快 11 倍；
- LN-GRAPE-S 在 1% 和 10% tasks 时平均比 LeaderGRAPE-S 快 7 倍；
- LN-GRAPE-S 在 50% tasks 时反而平均比 LeaderGRAPE-S 慢 3 倍。

作者把高任务比例下的减速归因于联盟更小、每轮分配的 followers 更少，因而需要更多迭代。这里的倍数只适用于所报告条件，不构成任意规模或任务分布的复杂度证明。

## Total communication requirement

论文报告：

- LeaderGRAPE-S 相对 GRAPE-S，平均低 7 倍，最大值低 10 倍；
- LN-GRAPE-S 相对 GRAPE-S，平均低 825 倍；
- LN-GRAPE-S 相对 LeaderGRAPE-S，平均低 121 倍；
- 在 10,000 robots、50% tasks 时，最大值分别为：

| Algorithm | Maximum total communication |
|---|---:|
| GRAPE-S | 9762.70 MB |
| LeaderGRAPE-S | 960.87 MB |
| LN-GRAPE-S | 6.55 MB |

因此论文给出的对应比值是 LN-GRAPE-S 分别低 1490 倍和 147 倍。来源将其解释为 leader 数量满足 \(|L|\ll N\) 且采用 batch allocation，从而减少消息大小和广播次数（§4，p. 4015）。

这些是实验中的 total communication requirement，不是现实网络带宽、延迟、丢包耐受、拓扑连通性或通信成功率。

## 解质量的报告边界

LeaderGRAPE-S 与 LN-GRAPE-S 分别在所报告全部试验的 100% 和 96% 中产生 `optimal solutions`。原文没有给 trial 总数、目标函数完整定义或实例分布，所以这只是当前试验中的比例，不是所有实例的全局最优保证。

对非最优实例，论文称最低 utility 解仍超过比较算法的 Nash-stable partition 所建立的 50% suboptimality bound（§4，p. 4015）。该句不能改写为 LN-GRAPE-S 自身具有普适 50% 近似保证，也不能消除未最优实例的尾部风险。

## 动态重组仍是后续计划

§5（p. 4015）计划在现实分布式条件验证静态算法后，再让 LN-GRAPE-S 支持：

- 新任务、任务要求变化和机器人故障；
- preemptive、priority-driven coalition reformation；
- 以当前任务优先级、执行阶段、任务依赖和到新任务的距离作词典序多目标排序；
- leader 间协商需要重新分配的 follower 数量；
- 以新任务成功分配数和被扰动旧任务的数量/优先级作评测。

这些机制尚未实现或评测。`viable for real-world missions`、`enables adaptability`、`minimal disruption` 与 `paves the way` 是目标性措辞，不证明真实机器人、通信受限网络、动态故障、长期自治或无结构环境部署已经成立。

## 复现边界与 AAMAS 关系

三页稿还缺少完整算法伪代码、trial count、实例分布、运行硬件、消息计数定义、误差条、统计检验、代码和动态场景协议。

该工作连接 coalition formation、hedonic games、机器人任务分配与大规模分布式协调。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MGGH7353.pdf) 核对 §§1–3（p. 4014）以及 Figure 1、§§4–5（p. 4015），并把已报告的静态结果与计划中的动态重组严格分离。
