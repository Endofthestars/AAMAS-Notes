---
title: "UAM-MARL: Uncertainty-Aware Modality-Enhanced Multi-Agent Reinforcement Learning with LLM-Guided Graph Policies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "generative_agents", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FHAS5003.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_manual_source_check"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["simulation_scope", "llm_and_perception_dependency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (Spark revision; manual primary-source check)"
reviewed_at: "2026-07-29"
---

# UAM-MARL: Uncertainty-Aware Modality-Enhanced Multi-Agent Reinforcement Learning with LLM-Guided Graph Policies

## 一句话总结

UAM-MARL 让 LLM planner–critic 生成并校验子任务图，再结合感知置信度、同调剪枝和图式元策略，在 AI2-THOR 噪声场景中学习协作策略。

## 方法与证据

- Figure 1、Algorithm 1 与 §3.2 给出 planner–critic 分解、图构建、剪枝和策略更新的顺序；critic 用于检查语义矛盾和不可行步骤。
- §3.3 对观测状态建模为 `p(s|o)`，以跨模态置信度检查子目标；§3.4 用感知置信度加权模块奖励。
- §3.5 把初始依赖图解释为单纯复形，用 `G=P_λ(G0)` 剪枝低分周期；§4.5 明确 `λ=0.5`。§3.6 定义父节点集合 `P_i={j | M_ji=1}`，供图式元策略使用。
- §4 在 AI2-THOR 四个场景、噪声感知条件下比较集中 LLM、对话式 LLM、TopoMARL、LGC-MARL 与三类消融。Tables 1–2 报告成功率、完成时长、token、冲突和噪声鲁棒性；完整模型的一组汇总为 SR 0.91、`Tavg=74.6`、token 1.8、冲突 3.2、UR 0.82。

## 局限与复现

- 实验局限于 AI2-THOR 的四个仿真场景与 4–6 智能体，不能直接证明真实机器人或更大规模性能。
- 结果依赖感知编码器、LLM planner/critic、置信度阈值和图构建实现；当前文本未见完整代码仓库或提示模板。
- 复现可从 §3–5、Algorithm 1、Tables 1–2 开始，并固定 `δ=0.7`、`λ=0.5`、奖励参数和训练/噪声设置。

## 与 AAMAS 的关系与核验说明

论文结合 MARL、LLM 规划和图结构协调。Spark 初审发现同调阈值与父节点集合遗漏；本笔记已对照 §3.5–3.6 和 §4.5 修正，并限制结论在论文的仿真评测范围内。
