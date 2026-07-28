---
title: "Pareto-guided Pipeline for Distilling Featherweight AI Agents in Mobile MOBA Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HUOT2523.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["hardware_dependent", "single_game_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-29"
---

# Pareto-guided Pipeline for Distilling Featherweight AI Agents in Mobile MOBA Games

## 一句话总结

论文将移动端 AI 部署建模为胜率、时延、能耗、内存和模型大小的帕累托优化，并在 HoK 3v3 中以教师分析、架构搜索和蒸馏选择轻量策略。

## 方法与证据

- §3.1 给出五目标优化和帕累托支配定义；§3.2 定义 HoK 的高维状态与层级动作空间。
- §4 的五阶段流程为架构设计、搜索、蒸馏训练、评估与选择（Figure 1）。教师剖析定位 Encoder/LSTM 等瓶颈，FA 学生以轻量 MLP 和团队级 max fusion 重构（Table 1、Figure 2）。
- Algorithm 1 在教师 FLOPs 的 1%–20% 预算中搜索候选；§4.4 以子动作级 KL 蒸馏，温度为 `τ=4`。
- §5 在固定 HoK 3v3 地图和 8 组英雄组合上评估：胜率来自 3 次、每次 1000 局，端侧时延和能耗从 5000 帧采样。Table 2、Figure 3 和 Table 3 比较 FA、压缩基线与消融。

## 局限与复现

- 结果限于固定地图、英雄组合、游戏版本和 iQOO12/骁龙 8 Gen 3 等测量环境，不能直接外推到其他 MOBA 或硬件。
- 正文未提供代码、模型链接或完整随机种子；训练与端侧测量的硬件依赖会影响复现实验。
- 复现应重建 §3–5、Algorithm 1、Table 1–3、Figure 1–3，并分别记录设备、阈值和多目标选择规则。

## 与 AAMAS 的关系与核验说明

工作将多智能体游戏策略的压缩和端侧可部署性作为显式决策目标。Spark S1 建立公式、流程、实验协议与表图的证据链；独立 S2 复核其与原文相符且未出现越界的统计或泛化结论。
