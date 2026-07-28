---
title: "Reputation as a Solution to Cooperation Collapse in LLM-based MASs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "marl_coordination", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UEHN4980.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["llm_evaluation", "limited_baselines", "simulation_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# Reputation as a Solution to Cooperation Collapse in LLM-based MASs

## 一句话总结

RepuNet 将直接互动信誉、八卦信誉和网络重连结合，在 20 个 LLM 智能体构成的实验网络中考察其对合作崩塌的缓解作用。

## 方法与证据

- §3 采用“智能体信誉动力学 + 网络动力学”的两层设计：直接互动和间接八卦更新信誉，信誉再影响是否建立或保留有向连边。
- 信誉以目标、场景、角色、叙述和连续评分组成；`ShapeRepuPeer`、`ShapeRepuSelf` 与 `ShapeRepuGossip` 完成更新（§3.2–3.3）。
- §4.1 在囚徒困境、资源共享和投资博弈中使用 20 个智能体、初始孤立图和每场景 5 次重复；指标为合作率、参与率或投资成功率。
- Figure 1 展示机制闭环；Figures 2–4 和 Table 1 比较完整机制与去除 Gossip、Reputation 或 RepuNet 的消融。文中报告的相关性显著性只适用于这些实验设定。

## 局限与复现

- 范围限于 20 智能体和三类博弈任务，不能推及更大规模、长时程或所有 LLM-MAS。
- 主要比较为内部消融，缺少广泛外部基线；提示词细节和部分实现位于附录，且结果依赖特定 LLM 配置。
- 未系统评测对抗噪声、恶意行为或其他安全情境；统计显著性不构成跨场景的强因果保证。

## 与 AAMAS 的关系与核验说明

工作将传统声誉和网络结构机制用于 LLM 驱动的多智能体协作。Spark S1 建立 §3–4、Figures 1–4 与 Table 1 的证据链；独立 S2 复核实验设置、数值和结论边界，结果一致。
