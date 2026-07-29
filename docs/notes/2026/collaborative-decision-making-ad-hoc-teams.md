---
title: "Collaborative Decision-Making in Ad Hoc Teams"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["marl_coordination", "agent_engineering", "robotics_embodied", "applications"]
dblp_key: ""
doi: "10.65109/HDMX4554"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HDMX4554.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05h"
spark_draft_verdict: "source_grounded_draft"
spark_qa_verdict: "needs_revision_overcooked_subject_and_phase_boundaries_corrected"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_program", "unknown_fixed_teammate_policies", "gpat_difference_reward_hypothesis", "library_skill_coverage_dependency", "overcooked_oracle_gap_subject", "controlled_turtlebot_demonstration", "online_adaptation_proposed", "air_traffic_irl_proposed", "expected_contributions_not_delivered", "full_paper_boundary", "no_operational_or_safety_validation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_gpat_phase_overcooked_subject_real_robot_and_aviation_boundary_check"
escalation_verdict: "pass_after_overcooked_oracle_gap_adaptation_irl_and_real_world_demo_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted adaptation and real-world boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Collaborative Decision-Making in Ad Hoc Teams

## 一句话总结

这篇 Doctoral Consortium 文稿以 GPAT 处理 fixed but unknown teammate policies 下的 zero-shot ad hoc teaming：测试新 team 时不 online-learn，GPI 从预训练 learner-policy library 选择动作，并以 learner difference rewards 试图减轻 teammate-induced dynamics shift；三类模拟与 Turtlebot3 foraging demonstration 属于当前工作，而 USFA/online adaptation、从 air traffic 以 IRL 学 reward、开放基础设施及更广泛现实适用性仍是 proposed 或 expected contributions。

## AHT 问题与控制边界

传统 cooperative MARL 常联合训练固定团队；Ad Hoc Teaming（AHT）只控制一个 learner，要求它与未见且未知的 teammates 协作。teammates 可能因不同训练任务、能力或目标偏好而对 team reward 次优。

文稿定义的 ad hoc MMDP 包含 learner \(a\) 与 teammate set \(N_u=N\setminus\{a\}\)。每个 teammate policy \(\pi_i\) 被假定为 **fixed**，但 learner 不知道它；reward \(r\) 假定 non-negative，作者说明 bounded reward 可经常数平移而不改变最优 policy（Definition 1，p. 4041）。

Zero-shot Coordination 问题给 learner 一组 source AHTs 用于 pretraining，再要求它为未见的新 AHT 合成 policy，且**不在新 team 上 online learning**（Problem 1，p. 4042）。这里的 zero-shot 是部署到该 team 后不更新 learner，不代表对任意未知行为都保证成功。

## GPAT：GPI library 与 difference rewards

GPAT（GPI for Ad Hoc Teaming）首先让 GPI 动态利用 pretrained learner-policy library。经典 GPI 的改进保证来自 fixed dynamics、changed rewards 的 single-agent transfer；AHT 恰好相反：team reward 固定，但新 teammate policies 改变 learner 看到的 effective dynamics。

若要恢复严格的 GPI policy-improvement 条件，需要在新 team 中重新评估每个 library policy，这又需要 online samples。GPAT 没有这样做，而是让 GPI 比较各 library policy 的 **learner difference-reward value functions**（Eq. 1，p. 4042）。

作者的机制假设是：difference reward 更突出 learner 对 team reward 的贡献，因此可能减轻新 AHT 引起的 distribution shift 对动作选择的影响。原文使用 “We hypothesize”，三页稿没有给出一般性保证。

## 当前模拟结果及其失败边界

文稿称 GPAT 已在以下环境评测（p. 4042）：

- cooperative multi-agent foraging；
- multi-agent predator–prey；
- Overcooked。

作者对所有环境假定 linear rewards，并在 foraging ablation 中另外考虑 general reward。结果仅以文字总结：

- library 至少含一些 relevant skills 时，GPAT 可有效实现 ZSC；
- library 没有 relevant skills 时，GPAT 会 struggle；
- 作者称 GPAT 可与 multiple teammates 协作并处理 dynamic environments；
- 在 Overcooked 中，GPAT **significantly outperforms the reported baselines**；
- 与其他实验环境相比，Overcooked 中**所有方法**相对 oracle policy 的 optimality gap 更大，说明该任务更难；
- ablation 被作者用于强调 difference rewards 对 value alignment 与 policy switching 的必要性。

“GPAT 胜过 baselines”和“所有方法距 oracle 更远”是不同主语与不同比较，不能合并成“GPAT 相比其他方法有更大的 oracle gap”。三页稿没有给 baseline 名称、metrics、数值、误差条、seeds、统计检验或完整训练协议；“significantly”本身不足以复核显著性水平。

本文的 GPAT 结果由引用 [12] 承载。仓库另有该 AAMAS full research paper 的[正文级 reviewed 笔记](./gpat-zero-shot-ad-hoc-team-coordination.md)；本笔记不把 full paper 的 team sizes、tables、hyperparameters、置信区间或 robot protocol 倒灌到这篇三页 DC 文稿。

## 当前 Turtlebot 演示：有实物声明，不等于现场部署

文稿明确称在 foraging environment 中使用 Robotis Turtlebot3 Burgers 做了 real-world multi-robot demonstration（p. 4042）。

但 DC 稿没有给出 robot 数量、地图与任务配置、试验次数、成功率、路径或碰撞指标、硬件/定位/控制配置、故障模式、安全流程或长期稳定性。它只能支持“存在受控实物演示”的作者陈述，不能支持跨组织 search-and-rescue、开放环境部署或安全认证。

## Proposed online adaptation

原始 ZSC 设定不在新 team 上学习。为进一步适应变化的 teammates，作者提出把 Universal Successor Feature Approximators 扩展到 AHT：

- 以 teammate-policy encoder \(e(\pi^{-a})\) 产生表示 \(z\)；
- 让 universal learner successor features 额外以 \(z\) 为条件；
- 从新 AHT 的 online samples 通过 IRL 推断 \(z\)；
- 再用 GPI 选择动作。

该方向仍是 proposed extension。文稿称还通过扩展 [2] 的 bound 导出 theoretical results，但没有给 theorem statement、适用条件或 proof，不能写成已经证明的通用 adaptation guarantee。

## Proposed air-traffic IRL 与预期贡献

另一方向拟从 air traffic 等 existing complex coordinating systems 学习。作者希望用 IRL 从 expert demonstrations 或 trajectory data 恢复 reward functions，再据此设计 better-informed AHT policies。

这是研究假设和拟议路径，不是当前集成结果：

- [10] 在本稿中是 aviation IRL survey；
- [11] 被描述为用 real aircraft trajectories 做 multi-task IRL 的工作；
- 本稿没有证明这些 rewards 已接入 GPAT、改善 AHT coordination 或实现 aviation control。

首页列出的 real-world demonstrations、real aircraft data 与 Gym-compatible open-source infrastructure 是 expected contributions，不是全部已经交付。当前可确认 Turtlebot 演示声明和对 [10]/[11] 的引用，但三页稿没有 code repository、航空运行结果或开放软件链接。

## 现实与安全边界

搜索救援、跨组织机器人和 aviation 只是动机或未来应用。文稿没有现场应急任务、partial observability 验证、nonstationary teammate safety、通信/网络故障、collision avoidance、human override、航空运行授权或 safety certification。

因此，不能把 GPAT、online adaptation 或 air-traffic IRL 写成：

- 对任意 unseen teammates 的协调保证；
- 已完成的在线自适应系统；
- 已集成并改善航空控制的方案；
- 可安全用于应急、机器人或航空现场的部署系统。

## 页码与核验说明

PDF 逐页核对：p. 4041 为摘要、research questions、expected contributions、AHT introduction 与 ad hoc MMDP 开端；p. 4042 为 Problem 1、GPAT、当前模拟结果、Turtlebot demonstration、proposed online adaptation、air-traffic IRL 与 Discussion；p. 4043 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HDMX4554.pdf) 核对问题定义、GPAT 的机制假设、当前实验、实物声明及未来方向；`reviewed` 不表示 expected contributions 已交付，也不表示受控演示构成现实部署或安全验证。
