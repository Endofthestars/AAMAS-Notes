---
title: "Scalable and Safe Multi-Agent Coordination with Reconstructed Level-k Monte Carlo Tree Search"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "safety_verification", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TAVV6081.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_safety_audit"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "high"
risk_tags: ["safety_claim_scope", "simulation_only", "prediction_assumptions"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "safety_claim_scope"
escalation_verdict: "revise_then_approved_with_scoped_safety_language"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass; GPT-5.6-Terra safety audit)"
reviewed_at: "2026-07-29"
---

# Scalable and Safe Multi-Agent Coordination with Reconstructed Level-k Monte Carlo Tree Search

## 一句话总结

本文用保守的 Level-0 轨迹基线、动态交互过滤和安全约束 MCTS 协调无信号交叉口车辆；在报告的 4 车和 8 车仿真中观察到 0% 碰撞率。

## 方法与证据

- §4 以位置、速度和航向描述车辆，使用 15 个离散控制原语。碰撞、道路边界和速度限制构成安全状态/动作谓词（Eqs. 5–6）。
- 动态交互图用战略与空间过滤保留相关邻居；Level-k 递归把低层策略作为预测，形成有限时域的协调规划（§4.2–4.4）。
- §5 的 MCTS 只在显式安全动作集 `A_safe` 内扩展、rollout 和回传（Eq. 26），并以 UCT 选择。
- Tables 1–2、Figures 3–7 报告两个对称无信号交叉口案例：4 车左转和 8 车左转/直行混合；其中表中该方法的碰撞率均为 0%。Table 3 比较的是特定过滤与固定低层策略条件下的计算量，而非一般复杂度定理。

## 安全范围、局限与复现

- Terra 审计确认：论文没有安全定理、递归可行性证明或预测误差鲁棒界。安全筛选只保证在模型化的有限规划时域内排除被谓词判为不可行的候选动作。
- 结果依赖准确预测、动力学、SAT/道路模型和每次滚动规划存在可行安全动作；不能解释为真实交通、部分可观测、异步决策或预测失配下的无碰撞保证。
- 实验限于全局可观测的对称仿真；复现需保留 §4–5、Eqs. 5–29、Tables 1–3、Figures 1–7，以及交互过滤、时间窗和 MCTS 预算细节。

## 与 AAMAS 的关系与核验说明

该工作连接多智能体博弈建模、运动规划和安全约束决策。Spark 双审核对了公式、表图与实验范围；因涉及安全结论，Terra 额外审计并将笔记限定为仿真与建模条件下的证据。
