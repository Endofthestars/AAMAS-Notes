---
title: "Issues with Measuring Task Complexity via Random Policies in Robotic Tasks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/FDIK3367"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FDIK3367.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["synthetic_planar_manipulators", "random-weight-guessing_dependence", "fixed_network_prior", "six-task_scope", "sac_baseline_scope", "no_general_complexity_metric"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Issues with Measuring Task Complexity via Random Policies in Robotic Tasks

## 一句话总结

该文以六个具有已知相对难度的平面机械臂 reaching 任务检验基于随机权重猜测（RWG）的复杂度度量：PIC/POIC 有时把两连杆臂判得比单连杆更容易，或把稀疏奖励判得比稠密奖励更容易，均与控制结构和 SAC 训练结果冲突；因此它提供的是对这类度量失效的受限反例与评测框架，不是已经解决非表格 RL 任务复杂度的通用指标。

## 方法与证据

- 作者考察 RWG 的随机策略回报分布，以及两个信息论量：PIC 是策略参数与回报的互信息，POIC 是策略参数与最优性变量的互信息；论文沿用“值越高、任务越容易”的解释（§2）。随机权重从固定标准正态先验抽样，策略不训练，运行后汇总 episode return。
- 为了有可核验的难度顺序，实验构造六项同构的 reaching 任务：长度 1.00 m 的单连杆、长度 1.65 m 的单连杆、总长度同为 1.65 m 的两连杆，各自配稠密/稀疏奖励（§4.1--4.2）。控制复杂度预期是更多关节更难、较长单连杆更难，且稠密奖励应比稀疏奖励易学；这是一组用于 sanity check 的结构化假设，而不是跨全部机器人任务的客观排序。
- 每个任务最多 50 steps、500 training episodes；RWG 取 \(10^4\) 个两层各 32-neuron MLP 随机策略，并以 \(10^5\) 个离散 bins 估计指标（§4.1）。训练核验使用 SAC；两连杆稀疏奖励还报告了 SAC+HER，学习曲线每项为 5 runs（§4.3、Figure 2）。
- 稠密奖励下，Table 1 的 PIC 反而给两连杆最高值、给 1.00 m 单连杆最低值；论文据 SAC 学习曲线和随机策略分布判定这与“二连杆最难、短单连杆最易”的预期相反（§4.4）。POIC 对两个单连杆的排序也违反其长度带来的误差关系。
- 稀疏奖励内部的 PIC/POIC 排序恰与预期一致；但跨奖励比较时，2-link 的 POIC 又暗示稠密奖励更难，和 SAC 曲线中稠密奖励较易的结论相冲突（§4.4）。作者以 bootstrap 1,000 次和 Welch t-test 检查表中差异，报告 p 值量级为 \(10^{-5}\)，所以这里的重点不是简单采样噪声。
- 讨论将失配归因于 RWG 对参数先验/有效搜索区域的依赖，以及没有表示训练中动态探索和 state visitation complexity（§5）。提出的改进方向是任务相关 inductive bias、沿学习轨迹重复 RWG，或在已知最优策略时用到最优策略的 optimal-transport 距离；三者均仍带来架构、探索策略或最优策略已知等额外依赖。

## 适用边界与复现

- 可用于审计深度 RL benchmark 或 curriculum 的“难度标签”是否真正经得起具有已知结构关系的同族任务检验；不可把本文当作 PIC/POIC 在所有任务中都无效的证明，也不能从六个二维、全可观测、无摩擦/重力的 reaching 任务推出真实机器人的学习难度。
- 指标结果会受网络架构、随机先验、return binning、奖励尺度、目标初始化及是否使用 HER 影响；稀疏成功区域尤其可能让随机策略几乎只采到低性能区。不同指标的量纲或排序也不应直接替代安全风险、样本成本、控制能耗或现实部署可行性。
- 复现应固定三种机构与目标初始化、dense/sparse reward、50-step horizon、所有 SAC/HER 超参数、MLP prior、\(N=10^4\)、\(M\)、bin 数和随机种子；发布原始 returns、PIC/POIC entropy terms、1,000 次 bootstrap、Welch-test 结果及每项 5-run 训练曲线。还应改变先验、网络、奖励塑形、动作噪声和部分可观测性，并与非 RWG 的难度/探索度量交叉验证。
- 若把任务复杂度用于机器人课程或资源分配，应保留人工审查和实际训练验证；错误排序可能让 agent 跳过必要的中间技能，或在安全关键任务中错误估计探索/训练预算。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的强化学习评测、机器人操控与可靠 agent-engineering 论文：它把“任务复杂度”这一常用于 benchmark 和 curriculum 的判断对象化为可反驳的实验主张。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FDIK3367.pdf) 核验 RWG/PIC/POIC 定义、六任务构造、SAC/HER 训练范围、Table 1 的排序冲突、bootstrap/t-test 和作者提出的三类改进；未将其有限实验写成通用复杂度理论或现实机器人安全结论。
