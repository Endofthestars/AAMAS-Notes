---
title: "Extremely Large Collective Coalition Formation: Scalability"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "robotics_embodied", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/EENQ4709"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EENQ4709.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["limited_heterogeneity_assumption", "fully_connected_instantaneous_communication", "centralized_simulation_evaluation", "static_tasks_and_robots", "nash_stability_not_global_optimality", "large_task_ratio_runtime"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Extremely Large Collective Coalition Formation: Scalability

## 一句话总结

LN-GRAPE-S 将极大异构机器人集体的任务联盟形成压缩为“capability type 对应的 leader”之间的 hedonic game：leader 成批把同类 follower 分到能带来最大正边际效用的任务，并同步 belief。论文证明有限 potential game 下到 Nash-stable partition 的收敛，并在集中式仿真中报告对最多 10,000 机器人、5,000 任务的低通信量与相对 GRAPE-S 的平均 29× runtime 改善、825×总通信降低。可扩展性来自集体能力种类远少于机器人数量、全连通即时通信及静态可行任务等结构前提，不等于已在真实分布式机器人网络部署验证。

## 方法与证据

- 问题将每个机器人分配给一个任务；机器人至多有两种 capability，任务需要多种 capability 的指定数量（§3）。同一 capability set 的机器人被视作策略等价，随机选出 leader，其余为 followers；这正是把协商规模从 \(N\) 压到 \(|L|\ll N\) 的关键假设（§4）。能力高度多样、个体性能差异大或 capability 互补关系不等价时，压缩可能不再保真。
- 每位 leader 仅考察需要自身 capability 的任务，依据当前未满足需求与可用 followers 计算批量分配，再以 task-capability utility 的边际增益作偏好；各 leader 广播和按更新时间戳/计数同步 belief（§4.1、Algorithm 1）。方法并不处理通信丢失、延迟、网络分区、恶意/故障 leader 或任务执行反馈。
- Theorem 4.1 将系统写成有限 exact potential game：每个严格正的单边 follower 重分配使全局任务效用 potential 同等上升，因此收敛到 Nash-stable partition。该稳定性是“无 leader 有正边际效用偏离”，不是全局最优或任务成功保证。
- Lemma 4.2 给出最多 \(|L|M f_{max}\) 次迭代，保守的每 leader runtime 上界为 \(O(|L|M^2f_{max}S)\)；communication 上界为 \(O(|L|^2M^2f_{max}P)\)（§4.2）。这些界依赖 leader 数和 capability 数小、每轮可传播 belief；任务数/异构类型增长会削弱收益。
- 评测比较 LN-GRAPE-S、GRAPE-S、LeaderGRAPE-S：1,000/5,000/10,000 robots，任务数为集体的 1/10/50%，十种 capability、每 robot 1 或 2 种 capability，每组 25 个可行随机任务实例，共每算法 450 trials（§5.1）。所有算法虽设计为 decentralized，却在 centralized simulation 中评估，并假定 fully-connected topology 与 instantaneous communication。
- 结果称 LN-GRAPE-S 在全部条件下通信最低；10,000 robots、50% tasks、2 Cap/R 的最大通信为 6.55 MB，而多任务比例高时 runtime 会明显变慢。它在 1 Cap/R 条件均得到 100% utility；2 Cap/R 的 1,000 robots、1% tasks 出现平均 89.50%、最低 62.95% utility，且 60% trials 是次优（§5.2–5.3）。因此“near-optimal”是此模拟分布上的经验结果，不能遮蔽某些组合的质量损失。

## 适用边界与复现

- 适用于能力种类有限、任务需求可精确计数、机器人可按 type 聚合的大规模静态多机器人任务分配；通信带宽是首要瓶颈时，leader-level synchronization 值得作为候选架构。
- 上线前须检验物理网络的拓扑、带宽、时延、丢包、leader 选举/故障转移、异步 belief 冲突、任务/机器人动态到离场与执行失败。论文将这些明确留作未来工作，故不能把 MB 级模拟通信量直接当作现场网络预算。
- 复现应固定 capability/task 生成器、可行性筛选、utility 范围、leader 选择随机种子、task ratio、Cap/R、消息编码、停止条件和硬件；同时测 wall-clock、所有消息字节、utility、未满足任务与稳定性，并在相同机器/网络条件下对比基线。
- 进一步应在部分连接、异步和带宽受限网络，以及能力多于两种、更多类型、故障/对抗 leader、任务价值随时间变化与真实 robot/simulation-in-the-loop 上评估；还应评估所得到 Nash-stable partition 相对集中式最优解的质量缺口。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多机器人 coalition formation、hedonic games 和大规模资源分配工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/EENQ4709.pdf) 核验 leader-level 建模、Theorem 4.1/Lemmas 4.2–4.3、复杂度、实验规模和通信/utility 结果；特别保留了“集中式仿真、全连通即时通信”及高任务比例 runtime/局部次优的边界，未将其表述为真实集群的通用最优部署结论。
