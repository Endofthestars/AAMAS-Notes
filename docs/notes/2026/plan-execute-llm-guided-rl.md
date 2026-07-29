---
title: "Plan-and-Execute: LLM-Guided Reinforcement Learning with Cross-Modal Fusion for Long-Sequence Decision Making"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/WKWD5060"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WKWD5060.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "llm_planning_assumptions", "benchmark_only_evaluation", "cross_modal_grounding", "planner_failure_unreported"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Plan-and-Execute: LLM-Guided Reinforcement Learning with Cross-Modal Fusion for Long-Sequence Decision Making

## 一句话总结

PLEX 令 LLM 迭代把自然语言任务分解为有逻辑/时间约束的 subgoal sequence，RL executor 再用语言 embedding 对视觉 patches 做 multi-head cross-attention 形成策略状态。摘要在 MiniGrid 与 MiniHack 报告比 PPO、A2C、NovelD 更好的长程稀疏奖励表现（例如 MiniHack WoD-hard 0.62 vs NovelD 0.10）；这不证明 LLM plan 正确、视觉 grounding 可靠或能适用于开放世界与现实控制。

## 方法与证据

- planner 是 LLM，职责是将语言 instruction 动态分解为顺序 subgoals；executor 的 RL policy 分别接收图像与语言表征（§2）。摘要没有指明 LLM 身份/版本、prompt、temperature、plan validation/retry、subgoal completion detector、上下文管理、调用成本或 planner hallucination 的处理，因此无法判断规划质量和责任边界。
- 图像按 patches flatten/linear-project 并加 positional embedding；sentence embedding 作为 Query，对 visual sequence 的 Key/Value 使用 multi-head cross-attention，输出融合 state \(s\) 给 policy（Eqs. 1–3）。这种融合不本身保证语言—像素对齐、遮挡/扰动鲁棒性或动作与 subgoal 的因果联系。
- MiniGrid 图 1 比较 A2C、PPO、NovelD、PLEX；文字称 KChard 等长程设置 PLEX 更高 reward/样本效率，而简单任务 curiosity 可接近。图中没有给具体均值、seeds、CI、训练/LLM query budget或对 planner/cross-attention 的拆分消融，故不能量化“significant”或归因给任一模块。
- MiniHack Table 1：LCmedium PPO/NovelD/PLEX 0.90/0.91/0.91；LChard 0.42/0.54/0.71；WoDmedium 0.01/0.15/0.68；WoDhard 0.0/0.1/0.62。它支持四个特定任务的得分比较，不能推出开放域、持续学习、真实视觉、对抗指令、安全执行或 generalization；论文结论的“open-domain settings”超过所呈现 benchmark 证据。

## 适用边界与复现

- 适合测试 language-guided hierarchical RL 与视觉—语言 fusion 的研究原型；不应把它用于无人监管的现实机器人、工具调用、安全关键决策或将 LLM plan 当作已验证指令。执行前需解析、约束检查和可撤销的低层 safety layer。
- 复现需固定 LLM/model/prompt/decoding/上下文、subgoal schema与终止/重规划规则、sentence encoder、visual patch/attention/policy architecture、RL algorithm/reward、MiniGrid/MiniHack tasks、baseline configs、seeds、frames、LLM调用数/延迟/成本和 per-task success/CI。还需检验同任务在不同自然语言措辞、无效/冲突指令与 planner error 下的表现。
- 应做 visual corruption、partial observability、longer horizons、OOD objects/layouts、plan errors/loops、instruction injection、token/latency budget、human oversight与计划可审计性测试；比较 LLM planner、固定 planner、oracle subgoals和纯 RL，报告 grounding/error/recovery，而不是只给最终回报。对于现实具身系统需动作/工作空间约束、碰撞监测和 emergency stop。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM agent、规划、multimodal RL 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WKWD5060.pdf) 核验 planner–executor 架构、cross-attention、MiniGrid 叙述和 MiniHack Table 1；并保留该 PDF 的 DOI 排版异常，采用会议目录对应的 `10.65109/WKWD5060` 作为索引 DOI。
