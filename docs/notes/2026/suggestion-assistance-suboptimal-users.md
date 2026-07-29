---
title: "Suggestion-Based Assistance of Suboptimal Users in Sequential Decision-Making Tasks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "generative_agents", "safety_verification"]
dblp_key: ""
doi: "10.65109/DFPG9276"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DFPG9276.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02i"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["human_ai_assistance", "toy_environment_evaluation", "acceptance_model_assumption", "not_medical_or_legal_advice"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Suggestion-Based Assistance of Suboptimal Users in Sequential Decision-Making Tasks

## 一句话总结

论文研究用户可接受或拒绝建议的顺序决策：最优任务动作不一定是最优建议；在假设用户策略与接受行为可参数化的前提下，用 Bayesian belief updates 估计两者并规划 user-optimal suggestions，在 toy grid world 中优于 task-optimal advice。

## 方法与证据

- 用户任务是 MDP，assistant 提议动作后，用户以 `α(h_t)` 接受，或以自身策略 `π_u` 行动，形成混合 effective policy。文中例子表明 task-optimal 连续建议在低接受率时可让结果低于不辅助（§3）。
- 对 stationary acceptance 与以 `θ` 参数化的 user policy，作者定义 modified MDP `M_(θ,α)`，其转移是建议动作和用户 fallback policy 的加权混合；优化该 MDP 得 user-optimal 而非 task-optimal assistant（Eq. 1）。
- Lemma 3.1 在 user policy 已知、assistant 使用最优 modified-MDP policy 的条件下，给出原 MDP value 的排序 `V* ≥ V^(π_α) ≥ V^(π_θ)`（§3）；它不是未知用户场景下的性能界。
- Zero-shot belief assistant 从参数 belief 采样、规划/缓存相应 policies、基于观测动作按 Eq. 2 更新 posterior（Algorithm 1）。在 grid-world 中，已知用户的 20 张随机 preference maps 上 user-optimal 减少低 α 时的损失；手工环境上 `α≤0.3` 时 belief assistant 接近 oracle（§5、Figure 2）。

## 适用边界与复现

- 结果依赖正确/可学习的 user-policy 与 acceptance parameterization、可观测动作、stationary 或所设衰减规律和可解的任务 MDP。人类拒绝建议还可能反映理解、风险、权力、隐私、价值观与情境，这些不会由该模型自动捕捉。
- 评估仅为 toy grid world/随机 preference maps/手工环境；没有真实用户、长期信任、认知负荷、误导、自动化偏误、弱势群体或高风险专业任务验证。
- Bayesian adaptation 可能通过试探性建议影响用户或错误估计其偏好。真实系统应说明建议依据、允许拒绝/静默/纠正、限制探索成本，并避免将“次优用户”标签用于剥夺自主性。
- 复现需公开 MDP/grid/preference maps、user policy family、prior/parameter grids、planner/cache/sample counts、likelihood update、acceptance schedules、seeds、完整 reward/variance；推广前应进行伦理审查和多样化人类研究。

## 与 AAMAS 的关系与核验说明

该工作聚焦保留用户控制权的建议式 human--AI assistance。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DFPG9276.pdf) 核对 §3--6、Lemma 3.1、Algorithm 1 和 Figure 2，明确区分形式模型和真实人类协作证据。
