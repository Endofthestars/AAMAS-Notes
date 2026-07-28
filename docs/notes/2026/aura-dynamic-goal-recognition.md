---
title: "General Dynamic Goal Recognition using Goal-Conditioned and Meta Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TTUH1381.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["simulation_only", "adaptation_assumptions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# General Dynamic Goal Recognition using Goal-Conditioned and Meta Reinforcement Learning

## 一句话总结

论文把固定域、固定目标集的目标识别扩展为通用动态目标识别（GDGR），并以 AURA 的记忆与适配流程处理持续变化的域和目标。

## 方法与证据

- §3 将 GDGR 定义为随时间变化的目标识别问题序列，允许域理论、动态目标集和观测序列分别变化。
- §4 的 AURA 包括初始化记忆、域适配、目标适配、识别推断与记忆更新（Figure 2、Algorithm 1）。
- GC-AURA 基于 goal-conditioned RL 处理固定域的新目标；Meta-AURA 基于 MAML-TRPO 处理跨域快速适配，并用 KL/Wasserstein 的轨迹—策略距离匹配目标。
- §5–6 在 MiniGrid、PointMaze 与 Panda-Gym 中报告多种观测率下的 F-score、Accuracy、Precision 和 Recall，并与 DRACO、GRAQL 等比较。

## 局限与复现

- 实验为可访问奖励与环境动力学的单智能体仿真，不能直接支持真实闭环或一般多智能体部署结论。
- Meta-AURA 假设域共享状态和动作空间；为避免遗忘，当前设计固定共享元参数，未形成持续在线更新方案。
- 正文未报告显著性检验，部分训练和效率细节在附录；复现应覆盖 §3–6、Figure 2、Algorithm 1 与 Figures 3–7。

## 与 AAMAS 的关系与核验说明

该工作连接在线意图推断、代理建模与自适应决策。Spark 双通道审核分别核对定义、流程、环境和适用范围，未发现与原文冲突的性能或泛化断言。
