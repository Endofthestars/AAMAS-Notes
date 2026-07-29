---
title: "Mitigating Problematic Social Media Use through Paired Recommender Systems with Contrasting Objectives"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "applications", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/ROHQ5247"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ROHQ5247.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04a"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "social-media", "well-being", "dual-system-rl", "synthetic-simulation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Mitigating Problematic Social Media Use through Paired Recommender Systems with Contrasting Objectives

## 一句话总结

本文在双系统 RL 用户模型与 recommender 的 general-sum Markov game 中，让 PutIn 模块优化接受推荐的 engagement、PutOut 模块奖励避开内容；paired training 使两模块共同更新，仿真中减少作者定义的 addiction-like 行为并维持互动。

## 方法与证据

- 用户决策混合 model-based prioritized sweeping 与 model-free Q-learning，$\beta$ 控制两者权重；环境含 healthy/neutral/recommendation/aftereffect/balanced 状态和三种动作（§2）。
- 两个模块为非平稳 multi-armed bandit：PutIn 对接受/拒绝分别奖惩，PutOut 对避免内容/长时间使用分别奖惩。paired-training 将任一模块的反馈用于同时更新二者（§2）。
- 以每类用户 200 条、每条 100,000 steps 的仿真比较。作者称双模块架构增加 balanced 行为、paired training 进一步稳定，并在 16 arms 时保持效果；行为类别是模型内定义而非临床诊断（§3–4）。

## 适用边界与复现

- 所有结论来自简化合成用户、状态和奖励；“addicted/healthy” 是 RL 分类，不能据此主张对真人降低成瘾或心理健康风险。介入真实 feed 还牵涉自主性、同意、弱势用户保护与平台激励。
- 复现需开放 state transitions、reward tables、$\beta$/MBUS/learning-rate grids、三类人口参数、bandit 更新、随机种子和 bootstrap protocol；进一步评估须采用伦理审批的用户研究、可解释选择、退出机制及福祉而非单一 engagement 指标。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ROHQ5247.pdf) 人工核对模型、仿真设置与作者列出的局限；未将仿真类别或机制推断为临床效果。
