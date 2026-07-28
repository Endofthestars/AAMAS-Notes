---
title: "Online Learning of Numeric Action Models for Planning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/DJKY6536"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DJKY6536.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["online_exploration_with_action_failures", "deterministic_full_observability_assumption", "linear_numeric_model_scope", "optimistic_model_not_safe", "benchmark_only_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Online Learning of Numeric Action Models for Planning

## 一句话总结

NOAM 在没有预收集 trace 时在线学习 numeric PDDL action model：它用 N-SAM 维护只允许已被保证可执行动作的 safe model，同时以 SVRAM 从成功/失败 transition 学习会冒险的 optimistic model，并用信息导向探索补全模型；在九个经典/合成规划域中通常有效，但 optimistic execution 会失败，且“safe”保证仅覆盖确定、全可观测、线性模型假设，不能外推为真实 agent 的安全探索方案。

## 方法与证据

- 问题设定中 agent 已知 state representation 与 actions、未知 action model；每个 episode 接收一个 planning problem，完整观察 action 前后 state，并把 inapplicable action 视为失败且 state 不变。动作前置条件是 Boolean literals 与 linear inequalities 的合取，effects 是 Boolean literals 与 linear equations 的合取（§2.2）。
- NOAM 对每个 lifted action 保存成功与失败 transition。先用 (M_{safe}) 规划；失败后用 (M_{op}) 规划/执行；若仍失败或无 plan，再执行固定步数的 informative exploration 并更新两模型（Figure 1、§3）。
- (M_{safe}) 使用 N-SAM：success pre-states 的 numeric convex hull 构成 safe precondition。Theorem 1 证明，在真实前置条件是 linear inequalities 合取的类别中，任何满足该 hull 的状态都可安全执行；失败例不会扩展这个 safe hull（§3.1）。
- SVRAM 从成功与失败 transition 学 optimistic model：借助 (M_{safe}) 将失败归因于 Boolean/numeric precondition，Boolean 部分从宽松模型逐步收紧，numeric precondition 用 SVM 分离正负例形成 hyperplanes，numeric effects 以 linear regression 学习。论文给出 numeric precondition learner 的数据相关 runtime bound（§3.2、Theorem 2）。
- 在 Depot、Driverlog、Rovers、Satellite、Farmland、Sailing、Counters、Sword、Pogo 九域，80 episodes、5-fold 下评估 model precision/recall/effect MSE 与计划求解率。(M_{safe}) 的 precondition precision 始终为 1；(M_{op}) 常有更高 recall/求解率却可能产生不可执行计划，例如 Pogo 中 76% test plans inapplicable，而 safe model 解出 81%（Table 2）。
- full NOAM 在多数 ablation 域最好，但不在全部域最好；Rovers 中随机探索高 11%，Rovers/Satellite 中 SVRAM+Info 优于 NOAM。Sword 的 effects 因只见 count=0 而把 increase 学成 assign，(M_{op}) MSE 达 3.77；Farmland 有 4% numeric-goal precision failure 被结果表省略（§4.2--4.3）。

## 安全边界与复现

- safe guarantee 是 model-theoretic：对 deterministic、full-observable environment，真实 action preconditions 可表示为 linear-inequality conjunction 且 observations/implementation 正确时，safe model 规划动作可执行且预测状态正确。它不覆盖传感误差、漂移、随机效应、部分可观测、延迟、执行器故障、对抗输入或非线性动力学。
- (M_{op}) 明确不是安全模型，其目的正是允许 potential failures 来探索；“action failure”在论文中被简化为 action 后 state 不变。真实机器人、金融、医疗、运维或任何不可逆环境不能将失败动作当作无害 observation，需 sandbox/digital twin、action allowlist、预算/速率限制、监控、fail-safe 与人工批准。
- benchmark 成功不能证明未知真实 domain 的模型已经完整。论文仅测九个满足线性/可生成实例条件的规划域；safe model 过度保守还会使 planner timeout，optimistic model 存在 invalid plans。数值精度误差与数据 coverage 均会改变结果。
- 复现应固定 PDDL/domain generator、训练/测试 split、episode/action limits、planner portfolio、VAL version/tolerance、SVM/liblinear/linear-regression 设置、random seed（论文用 42）、failure labels、exploration budget和所有五折结果；需额外报告 failed-action count、damage/cost、model coverage、OOD/噪声/非线性压力测试，而不只报 solve rate。

## 与 AAMAS 的关系与核验说明

这是 online action-model learning、numeric planning 与 information-guided exploration 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DJKY6536.pdf) 核对 NOAM pipeline、Theorem 1--2、九域设置、Table 2--3、PPO comparison 与已报告的失败/精度现象；没有把 benchmark 内的 safe model 或 optimistic exploration表述为生产环境安全保证。
