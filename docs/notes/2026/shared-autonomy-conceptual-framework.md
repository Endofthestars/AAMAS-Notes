---
title: "A Conceptual Framework for Shared Autonomy"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/QRXH6744"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QRXH6744.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02r"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["conceptual_framework", "extended_abstract_only", "human_engagement_modeling", "single_human_single_ai_scope", "no_reported_experimental_details"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Conceptual Framework for Shared Autonomy

## 一句话总结

论文将 shared autonomy 中“谁拥有主动权、对方能否/会否响应、是否进入恢复”的互动语境作为规划状态的一部分，而非把自治等级和升级规则写在 MDP 之外；作者称该结构可约化为标准 MDP，能用 value iteration 等求解器，并使确认、延后、交由人或自主执行成为前瞻性策略选择。这是一套面向单人--单 AI 的概念建模骨架，长文中的形式证明与实验细节均未在 AAMAS 扩展摘要展示，不能据此宣称安全关键共享自主已被验证。

## 方法与证据

- interaction context 编码主动权归属、在人类响应性约束下可能的回应、以及正常执行或恢复；它与任务状态共同演化，使策略能考虑当下互动选择怎样改变未来的参与度、权责和执行质量（§2）。
- 框架受 PACT 式 mixed-initiative paradigms 启发，将互动语义提升到 Markovian planning model；作者称不需枚举 autonomy modes 或递归地建模人类信念/意图，仍可 compactly reduce 到普通 MDP 并以经典 MDP solver 求解（摘要、§2--3）。
- 例子是有雪的桥：人可能需要 teleoperate，即使局部效率并不最优；在参与度下降时，策略可等待、征求确认或自主继续。这说明其优化对象包括未来协调能力，而非只比较瞬时任务回报（§2.1--2.3）。
- 论文明确只讨论一名人和一个 AI，interaction context 是对 initiative/engagement 的抽象，不是 belief state 或递归 ToM。不同领域须各自实例化互动语义、动力学和偏好；完整形式化与实证留待长版本（§4）。

## 适用边界与复现

- 可作为共享控制、决策支持或人机协作系统的建模起点；把 authority、attention、responsiveness 和 recovery transition 显式列为状态/转移/奖励变量，便于审计与解释。
- 其 MDP 约化依赖模型者能恰当指定互动状态、转移、回报与人类响应分布；真实人类的疲劳、不同意、误解、学习、策略性行为和安全风险若未被状态捕获，Markov 假设与最优策略都会失真。
- 该扩展摘要没有具体状态空间、奖励、实验任务、样本量、用户研究或安全指标；“可扩展”“更丰富策略”是作者定位，非本版本可复现实证结果。
- 复现/部署应发布实例化后的状态变量、协议、权限边界、handoff/recovery 条件、human model 的数据来源和不确定性；用仿真、压力测试和真实用户研究评估任务质量、工作负荷、延迟、override、校准、公平与安全，并保留人类否决权和失效保护。

## 与 AAMAS 的关系与核验说明

该文连接人机协作、mixed-initiative planning 与决策理论。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QRXH6744.pdf) 人工核对 interaction-context MDP、桥例、单人单 AI 范围及长文保留项；未将概念框架误写成已完成的机器人或用户实验。
