---
title: "Quality-Diversity for Multi-Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: "10.65109/SLJK5791"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SLJK5791.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["mamujooco_descriptor_scope", "adapted_single_agent_baselines", "seed_statistics_not_reported_in_main_text", "archive_metric_dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Quality-Diversity for Multi-Agent Reinforcement Learning

## 一句话总结

MIQD 在 cooperative MARL 的 MAP-Elites archive 中，以片段行为描述符和 state-action 与目标描述符的互信息内在奖励训练条件 critic，试图同时提升回报与 archive 覆盖；在四个 MAMuJoCo 足接触描述符任务上曲线优于所比较方法，但这种“diversity”限于预定义的接触比例网格，尚不等于对策略、角色或现实任务的普遍多样性。

## 方法与证据

- 每个 episode 的 BD 是各脚接地时间比例；MIQD 将全轨迹 BD 改为滑动长度 `K` 的 fragment descriptor，并令 critic `Q(s,u,fd*)` 以环境奖励加 `I(s,u;fd*)` 估计目标行为片段的相关性（式 6–9）。
- 为把多步 descriptor 反馈分摊到单步动作，作者使用互信息 factorization/discriminator；同时从 archive 抽 team policies、随机目标 descriptor，并采用 CEM 与 target cell 邻近 policies 辅助 critic target estimation（§4）。
- 评测为 2-agent HalfCheetah、Ant、Walker、Humanoid MAMuJoCo；BD 维数分别为 2/4/2/2。八个 team policies 并行更新，fragment 长度为 50；对照是 Map-Elites、PGA-Map-Elites、QD-PG、DCG-Map-Elites 的多 agent 改造版本，梯度基线使用 MATD3（§5.1）。
- 三项指标为 archive fitness 总和（QD-score）、已占格比例（coverage）和 archive 最大 fitness。正文图 2 报告 MIQD 在四任务上整体强，尤其 HalfCheetah；去掉 fragment BD、MI reward 或 neighbor policies 的消融曲线下降，且 2-agent HalfCheetah archive 图示更均匀（§5.2–6）。

## 局限与复现

- coverage 与 QD-score 都由网格分辨率、边界、足接触 BD 和存档替换规则定义；高覆盖不能证明策略在未定义的 gait、扰动、任务目标或 multi-agent role 上更具功能多样性。Humanoid/Walker 被压到二维接触比例也可能丢失协调结构。
- “MI reward”依赖其估计器、片段长度、目标 descriptor 采样和 critic 训练稳定性；正文展示互信息 loss 曲线和消融，但没有将所估计 MI 与真实可计算 MI 或行为因果关系校准。
- 多数基线原为单 agent 方法，论文对 crossover 与训练流程做 multi-agent 改造；公平性取决于该改造、MATD3 实现、同等并行/样本预算。正文未明确随机 seed 数、置信区间或统计检验，故曲线差异应视为描述性结果。
- 仅有四个连续协作控制任务，训练使用全局信息而执行局部观测；没有评测通信、异质 agent、竞争/混合动机、更多 agents、descriptor 选择失配或真实机器人迁移。复现应公开 archive bins/范围、所有候选/丢弃策略、MI estimator、CEM/neighbor 细节、seeds、环境版本和总环境步数。

## 与 AAMAS 的关系与核验说明

该文把 quality-diversity search 用于集中训练、分散执行的多 agent 连续控制。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SLJK5791.pdf) 核对 descriptor、critics、对照改造和 metric 定义，将性能结论限定于 MAMuJoCo archive 设定。
