---
title: "Learning Robust Policy for Multi-UAV Collision Avoidance via Compact Causal Feature"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AAFZ2582.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass"
review_batch: "2026-batch-02a"
spark_draft_verdict: "pass"
spark_qa_verdict: "pass"
spark_consistency: "agree"
risk_level: "medium"
risk_tags: ["simulation", "safety_claim"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.3-Codex-Spark dual pass)"
reviewed_at: "2026-07-28"
---

# Learning Robust Policy for Multi-UAV Collision Avoidance via Compact Causal Feature

## 一句话总结

CCFL 在 VAE+SAC 的多无人机避障策略中识别并压缩视觉因果特征，以缓解未见背景和障碍外观变化下的表征域偏移。

## 研究问题与方法

- 论文研究训练/测试场景分布变化下的多无人机协同避障；观测、动作和奖励定义见 §3.1。
- CFI 用干预一致性约束分离稳定特征，RFC 以可微掩码和正则压缩冗余通道（§3.2–3.4，Figures 2–4，Eqs. 4–6、8、10–11）。
- 环境为 Unreal Engine + AirSim 的可控仿真基准（§4.1）。

## 实验与证据

| 结论 | 证据位置 | 核验边界 |
|---|---|---|
| 表征迁移是瓶颈 | Table 1 | 森林等测试域的直接迁移下降；仅微调视觉网络的恢复更明显。 |
| 未见场景表现提升 | Tables 2–3 | 报告 SSR、ISR、SPL 等指标改善；限于论文给定的场景干预。 |
| 两模块均有贡献 | Table 4 | 移除 CFI 或 RFC 均降低表现；这是消融证据，不是因果机制的普适证明。 |
| 轨迹更稳定 | Figures 7–8 | 仅是所示仿真案例的可视化对比。 |

## 局限与复现

- 所有主要结论来自仿真；未报告真实无人机硬件实验。
- 泛化干预主要覆盖背景和障碍外观，未覆盖传感器噪声、动力学偏移或通信失配。
- 论文未提供完整的随机种子、超参数与代码可用性证据，复现应以方法、环境和表 1–4 为最低核验对象。

## 与 AAMAS 的关系

该工作把因果表示学习与多无人机协同避障结合，连接 `marl_coordination`、`robotics_embodied` 与 `safety_verification`。

## 核验说明

Spark S1 依据官方 PDF 建立结构化草案；独立 Spark S2 复查了方法、表图、外推边界及复现信息，未发现需要升级到 Terra 的高风险冲突。
