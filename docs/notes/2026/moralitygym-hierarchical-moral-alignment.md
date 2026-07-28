---
title: "MoralityGym: A Benchmark for Evaluating Hierarchical Moral Alignment in Sequential Decision-Making Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/SAKL6648"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SAKL6648.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["designer_specified_moral_priorities", "synthetic_trolley_problem_scope", "strict_norm_ordering", "moral_alignment_not_legal_compliance", "no_real_world_deployment_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# MoralityGym: A Benchmark for Evaluating Hierarchical Moral Alignment in Sequential Decision-Making Agents

## 一句话总结

MoralityGym 将设计者指定的道德规范写成有严格优先级的 deontic constraints，并在 98 个 trolley-problem 风格的 Gymnasium 顺序环境中评估 Safe RL policy；PPO 的 expert reward-cost shaping 在论文指标上整体最佳，但这验证的是对给定、合成道德链的优化，不构成现实世界伦理、法律合规或通用“道德对齐”的认证。

## 方法与证据

- Morality Chain 将每条规范表示为 signature、量化其违反/满足程度的函数、规范力与禁止/要求方向；按规范力严格排序，并用递归权重汇总为 0--1 morality metric，使高优先级规范在分数中占主导（§3）。
- 基准包含 98 个可配置 Gymnasium 任务，主要是 trolley dilemma 的变体。agent 在格状铁路环境中移动、操作 lever/switch，并面对人类、动物、机器人伤害、直接个人伤害和自我保存等取舍；环境把 task reward 与 moral cost/post-hoc policy evaluation 分开（§4.1--4.3）。
- 评测四类规范链：按实体伤害最小化的 Utility、加入 agent harm 的 UAH、优先避免直接个人伤害的 Dual-Process，以及加入 self-preservation 的 DPAH。比较 Random、仅环境奖励的 PPO、PPO Shaped、PPO-Lagrangian 与 CPO（§4.4--5）。
- 表 1 中 PPO Shaped 在所有列出的 scenario/chain 组合取得最高 morality metric；例如 PushOrSwitchSelfSacrifice 为 0.996，而普通 PPO 为 0.192。CPO 与 PPO Shaped 往往满足最高优先级规范，但会牺牲低优先级目标；PPO-Lag 更常呈折衷，普通 PPO 则可能偏向自我保存而损害人类伤害最小化（§5、Table 1、Figure 2）。
- 代码仓库在论文脚注给出为 [raillab/morality-gym](https://github.com/raillab/morality-gym)；`evaluate_morality_metric` 默认以 100 个 evaluation episodes 评估 policy，复现仍需锁定环境版本、链定义/权重、奖励和成本、训练预算、Safe RL 实现与随机种子（§4.1）。

## 安全边界与复现

- “moral”内容由 benchmark 设计者以 signature、损失函数和严格排序预先定义；高分表明 policy 拟合了这套操作化规范，不证明它理解人类价值、可处理跨文化分歧，或能自行决定何种价值应优先。
- 场景是合成 trolley-style 环境，缺少真实世界的感知不确定性、多人协商、制度责任、长期后果与受影响者参与。论文亦承认抽象掉 emotion、development 和 social context，且 personal/impersonal 之外的 causality、responsibility、counterfactual 仍未充分覆盖（§7）。
- strict ordering 不能表示同等强度但不可兼得的“tragic dilemmas”；将该指标用于医疗、交通、福利、执法、招聘或金融等实际决策前，必须另做领域验证、法律/伦理审查、利益相关方参与、可拒答/升级机制与人工问责。
- reward shaping 的领先结果依赖专家把 moral cost 编入训练信号，不能据此推断 agent 自动获得规范推理能力。应报告未见任务/扰动、不同伦理链与权重、跨文化设定、constrained-vs-shaped sensitivity、失败轨迹及伤害分布，而非只报告 aggregate score。

## 与 AAMAS 的关系与核验说明

这是 Safe RL、规范敏感 sequential decision-making 与 AI alignment evaluation 的基准工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SAKL6648.pdf) 核对 98 个场景、Morality Chain/metric、四条伦理链、五类 baseline、Table 1 和论文 limitations；没有把合成基准得分表述为现实道德判断或合规保证。
