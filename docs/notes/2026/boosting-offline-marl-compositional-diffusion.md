---
title: "Boosting Offline MARL under Imbalanced Datasets via Compositional Diffusion Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/WOLI7576"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WOLI7576.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_severe_imbalance_protocol", "llm_label_distillation_dependence", "simulation_benchmarks_only", "three_seed_evaluation", "compositional_monotonicity_assumption"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Boosting Offline MARL under Imbalanced Datasets via Compositional Diffusion Models

## 一句话总结

CODI 先用 `gpt-4o-mini` 给少量轨迹片段标注“哪位 agent 表现最好”、蒸馏为标签器，再以 return-to-go 和可组合的 agent-level quality 条件训练 diffusion，生成并拼接平衡协作轨迹；在“每条轨迹仅一名 expert、其余随机”的合成失衡数据上平均恢复 63% 的 expert-gap，但该设定及“个体变好即可组成团队变好”的前提限制了外推。

## 方法与证据

- 在固定 offline Dec-POMDP 数据中，CODI 抽样少于 10% 片段交给 `gpt-4o-mini`，以手工文本描述和“select the best agent”提示产生单个最佳 agent 标签；GRU+MLP 标签器蒸馏后为全数据给质量概率（§3.1）。
- conditional DDPM 以 RTG 与标签训练；推断时把“全体优秀”的 OOD 团队目标拆成训练中常见的单 agent 条件，用 classifier-free guidance 线性组合，再将通过动态一致性检查的片段拼接为轨迹；失败则重采样或重新起始（§3.2--3.3）。
- 构造 protocol：先用 QMIX 获得 balanced expert，然后每个 episode 随机挑 1 个 agent 执行 expert、其余随机，收集 20k 原始轨迹；每种增强再生成 20k，组成 40k 数据。比较 Original、MBTS、MADiff、MADiTS、禁用 compositional 的 CODI 和使用特权 one-hot 标签的版本（§4）。
- 在 MPE CN/World、SMAC 3m、SMACv2 Zerg_3v4，配 BC、50%BC、OMAR、OMIGA，各 3 seeds；Table 1 的归一化平均为 CODI 0.63（论文表述为恢复 expert gap 的 63%）。

## 局限与复现

- 主要压力测试是“恰好一个 expert、其余随机”的人为极端失衡；真实离线数据的质量、行为策略、观测噪声和 agent 数量往往连续且相关，结论不等价于一般 offline MARL 增强。
- LLM 的提示、状态文本化、抽样的 <10% 标注、模型版本和标签准确率会改变下游 diffusion；文中没有独立人类标注一致性、LLM 费用/延迟或跨模型稳健性结论。
- dynamics check、重采样阈值、segment horizon、过滤和 20k 生成预算会决定生成数据覆盖；只报告 3 seeds，部分单元标准差较大，须公开完整配置、seed、原始轨迹与失败/丢弃率。
- 方法假设改善个体行为可组合为改善团队表现；社会困境或非单调协作会失效。作者也把此类情形、更先进生成模型、外部 LLM 知识及开放世界 embodied 系统列为未来方向（§6）。

## 与 AAMAS 的关系与核验说明

该文面向离线多智能体协作的数据质量与生成式增强。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WOLI7576.pdf) 核对 CODI 三阶段、失衡数据构造、基线、Table 1、seeds 和作者声明的假设；没有把模拟基准上的平均归一化分数表述为真实多智能体部署收益。
