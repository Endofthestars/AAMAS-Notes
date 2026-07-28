---
title: "Multi-Agent Model-Based Reinforcement Learning with Joint State-Action Learned Embeddings"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IXMJ8234.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_manual_source_check"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["world_model_bias", "ctde_assumptions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (Spark revision; manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Agent Model-Based Reinforcement Learning with Joint State-Action Learned Embeddings

## 一句话总结

MMSA 在 CTDE 的价值分解框架中，将联合状态—动作表示学习（SALE）与双 VAE 世界模型想象结合，为多智能体协作训练增加合成轨迹信号。

## 方法与证据

- §4 以 SALE 提取状态—动作表征，并将其注入个体网络和 QMIX 风格的混合价值网络（Figures 1–2）。
- §4.1 用 Dec-POMDP 的变分表述定义 LELBO；§4.3–4.4 的两个 VAE 递归产生隐空间 rollout，并以 KL、重构、TD 和任务项联合训练，含 KL balancing。
- §5 在 MAMuJoCo、LBF、SMAC 和 SMACv2 中比较学习曲线、置信区间与基线；Figures 5–7 和 Table 1 给出性能与消融，去除世界模型、SALE、KL balancing 或全局状态相关模块均出现退化。

## 局限与复现

- 世界模型误差会使想象轨迹偏离真实动态并影响决策；论文未给出收敛或一般化保证。
- 证据限于协作基准和 CTDE/全局状态相关条件，未覆盖对抗或混合博弈。
- 复现需覆盖 §4–5、Figures 1–7、Table 1 及世界模型、SALE、价值混合和 KL balancing 的完整配置；正文未见完整代码/硬件/超参数工件。

## 与 AAMAS 的关系与核验说明

工作连接多智能体模型学习、表示学习和价值分解。Spark 修订去除了不可核验的“首次”与外加风险分级；本笔记保留原文明确的模型偏差限制。
