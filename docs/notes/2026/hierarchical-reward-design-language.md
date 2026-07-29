---
title: "Hierarchical Reward Design from Language: Enhancing Alignment of Agent Behavior with Human Specifications"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/JTHG8732"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JTHG8732.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["simulated_domains_only", "predefined_option_requirement", "llm_reward_code_risk", "syntax_filter_not_semantic_verification", "task_feasibility_filter", "small_human_study", "reward_hacking_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Hierarchical Reward Design from Language: Enhancing Alignment of Agent Behavior with Human Specifications

## 一句话总结

论文提出 Hierarchical Reward Design（HRD）与其语言实例 HRDL：为 option-based hierarchical RL 分别生成 high-level \(\tilde r_H(o_{prev},s,o)\) 与 low-level \(\tilde r_L(s,o,a)\) preference reward，而非只生成 flat \(\tilde r_{flat}(s,a)\)。L2HR 用 GPT-4o 从任务和行为语言生成 reward code、训练并筛选可完成任务的策略；在三个长时程模拟域中比语言 flat reward 更常保留可行性且更贴合指定行为。优势依赖可用、语义正确的 option 表示，且不构成真实机器人上的安全保证。

## 方法与证据

- HRD 将 world MDP、有限 option 集、候选高/低层 reward 对、学习程序与 fitness 组成 reward-search 问题。低层 policy 以 \(s,o\) 选 primitive action，高层 policy 以前一 option、state 选下个 option；实现用 PPO 训练低层、DQN-style 方法训练高层（§3.2）。
- HRDL 额外给 task reward、subtask pseudo-reward 与自然语言 specification，但 reward 生成阶段不访问 fitness \(F\)。其目标是在 task/伪奖励基础上找到可最大化最终 policy fitness 的 \((\tilde r_H,\tilde r_L)\)（§3.3--§4）。这避免直接对人评过拟合，却也使生成时没有语义对齐 oracle。
- 论文证明 flat reward 是 HRD 的特殊情形；某些依赖前一 subtask 的选择偏好只能由 \(\tilde r_H(o_{prev},s,o)\) 表达，某些 option-conditioned 执行偏好只能由 \(\tilde r_L(s,o,a)\) 表达（Properties 1--2，证明在扩展稿 Appendix）。结论针对给定信息接口的 flat \(s,a\) reward，不是说任意带历史/状态扩充的非层级方法必然无能为力。
- L2HR prompt 提供任务描述、暴露 state/action/option 语义的 environment context、行为 specification、编程约束及 reward scale；不提供 task reward code。它一次生成 \(k\) 个候选，检查 Python syntax 与只引用允许变量，然后先训练/筛选 low-level policy 的 subgoal completion，再训练 high-level policy，并返回通过 task-reward threshold 的组合（§4）。
- 该过滤不是安全或行为验证：作者明确未使用 iterative reflection/evolutionary search，且候选只因编译、变量白名单和训练阈值而保留。LLM reward 仍可能奖励 proxy、破坏约束或受环境实现细节影响（§4.2）。
- 实验比较 Task-only、Language-to-Flat（Flat）与 L2HR（Hier），每个 LLM 配置由 GPT-4o 每 trial 生成 8 个候选、重复 3 次即 24 个；域为 8-subtask Rescue World、8-subtask iTHOR pick/place、5-subtask single-agent Overcooked Kitchen（§5.1--§5.2）。
- 在成功完成任务的候选中，Rescue World 的 expert-level total alignment 为 Hier 69.23%、Flat 12.50%；iTHOR 为 62.50%、Flat 0%；Kitchen 为 92.86%、Flat 10%。Hier 在 Rescue World/iTHOR 的 high-level alignment 分别为 76.92%/87.50%，而 Flat 为 12.50%/0%（Table 1）。均值只对成功 LLM 候选计算，不能与所有生成样本的无条件表现混同。
- 30 个通过 attention check 的 Prolific participants（两域均分）盲评视频的 1--5 对齐分：Rescue World 的 persistence 为 Hier 4.76、Flat 2.42，overall 4.64 vs 3.46；Kitchen chopping 为 4.47 vs 1.70。完美人评 policy 比例也偏向 Hier（Table 2），但样本量小、仅两模拟域且观众非专家（§5.4）。
- 作者列出真实机器人/交互式 AI 验证、先进 reward generation/human feedback、以及 option discovery 为未解问题，并强调 HRD 只是 demonstrations、rankings、user corrections 等对齐方法的补充（§6）。

## 适用边界与复现

- 适用于任务有稳定、可审计的 temporal abstraction/options，且人类要求包含子任务顺序、持续性或 option-specific 执行方式的长时程 RL；option 标签若含混或错误，层级 reward 会系统性放大该错误。
- 不应把自动生成的 reward code直接用于实体机器人、医疗、车辆或其他安全关键控制。至少需 sandbox、代码静态检查、白/黑名单 API、reward/trajectory adversarial testing、运行时 shielding、人工批准与紧急停机。
- 复现应冻结 GPT-4o 版本、prompt、环境暴露变量、options、PPO/DQN 超参、\(k=8\) 候选与三次重复；报告所有候选的 syntax/variable/task-completion/alignment 漏斗，而非只报告成功者，并在 Rescue World、iTHOR、Kitchen 逐一复现 Table 1。
- 推广评估应增加 option 消融和历史扩充 flat baseline、跨任务/扰动/语言改写测试、概率与人评置信区间、真实硬件低风险试验，以及 reward hacking/约束违反率；再结合 demonstrations、偏好比较和在线纠错决定是否可部署。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 human-centered RL、reward design 与 agent alignment 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JTHG8732.pdf) 核验 §3--§5 的 HRD/HRDL 定义、Properties 1--2 的范围、L2HR 流程、Table 1--2 与 §6 局限；未将模拟环境与小规模视频人评的改善表述为真实世界安全或通用语言对齐结论。
