---
title: "Equilibria in Quantitative Bipolar Argumentation Dialogues"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "game_theory_mechanism", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/VBDV4500"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VBDV4500.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02y"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["formal_model_scope", "myopic_deviations", "fixed_objectives", "observable_moves", "no_user_study"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Equilibria in Quantitative Bipolar Argumentation Dialogues

## 一句话总结

论文将 quantitative bipolar argumentation framework 扩展为 MQBAF：每个 agent 对 argument strength 的增/减目标和全预序偏好被编码，agent 选择 utter 哪些 argument，utterance profile 诱导出仅含已发言 argument 的 QBAF。若所有 agent 对任一单边改发言都无严格获利，则为 utterance equilibrium；模型给出定量目标下的稳定性语义，但目前只处理静态完整发言、固定目标、可观察动作和 myopic 偏离。

## 方法与证据

- QBAF 含 arguments、attack/support 边和初始 strengths；MQBAF 另加 agents、每 agent 的带正/负方向 objectives，以及 objectives 上的 total-preorder preference（§2，Definitions 2.1--2.3）。
- utterance profile 是 argument 到发言 agent 的部分函数；induced QBAF 仅保留确实被 utter 的 nodes、边与 strengths，从而使发言改变可量化改变各 objective argument 的 strength（Definitions 2.4--2.5）。
- utterance rationality 要求一个 agent 在其他人发言固定时，对其全部 unilateral utterance deviations 至少弱偏好当前 induced QBAF；所有 agent 都 rational 的 profile 是 utterance equilibrium（Definitions 2.6--2.7）。文中例子用 DFQuAD semantics 计算强度，说明无获利偏离（Example 2.8）。
- 作者明确采用 myopic deviations、observable moves 与 fixed objectives；mixed/subgame-perfect equilibrium、协议约束和动态 dialogue game 是未来扩展（§3）。

## 适用边界与复现

- 适合分析各方能公开引入哪些支持/反驳、并关心可量化 argument strength 的小型对话；equilibrium 只反映模型内偏好/strength，不证明论证为真、对话公平或参与者会服从。
- semantics（如 DFQuAD）、初始 strengths、objective 极性、偏好排序和可发言集合决定结果；未建模隐藏信息、欺骗、成本、时序、信誉、自然语言歧义或对抗性提示。
- myopic 单边稳定不能排除协调偏离、长期策略或协议诱导的不同均衡。没有用户研究、真实对话数据或求均衡的规模/复杂度评测。
- 复现应版本化 QBAF、semantics、agent objectives/preferences、可见性与允许 utterance，枚举小模型的 profile/偏离并审计 induced strengths；添加 mixed/动态策略或真实协商前应明确协议、信息和激励。

## 与 AAMAS 的关系与核验说明

该文连接定量论证和博弈稳定性。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VBDV4500.pdf) 人工核对 MQBAF、utterance/induced QBAF、rationality/equilibrium 与 Example 2.8；未把形式稳定性夸大为现实说服或公平保证。
