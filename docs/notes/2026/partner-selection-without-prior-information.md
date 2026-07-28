---
title: "Defection at First Sight: Learning Partner Selection in Optional Social Dilemmas without Prior Information"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IBSZ1473.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_revision_manual_source_check"
review_batch: "2026-batch-02a"
spark_draft_verdict: "revised"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "agree_after_revision"
risk_level: "medium"
risk_tags: ["simulation_only", "no_formal_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (Spark revision; manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Defection at First Sight: Learning Partner Selection in Optional Social Dilemmas without Prior Information

## 一句话总结

论文在可退出的重复囚徒困境中，让学习体在新配对首轮没有对手历史信息；20 体仿真显示首轮防御性背叛后，后续互动可学习互惠行动和伴侣选择。

## 方法与证据

- §2.1 的 SDOO 流程是随机配对、进行一轮囚徒困境、选择留存或跳出并重配；新配对不携带对手历史信息。
- §2.2 用常步长蒙特卡洛 Q-learning 和 Boltzmann 探索，分别学习动作策略 `π_PD` 与伴侣选择策略 `π_PS`；策略按互动长度 `m` 区分。
- §3 在 `N=20`、`M=2` 与 `M=3` 的条件下跟踪策略类型和结果。Figures 3–8 显示首轮 All-D 较多、后续互动中 TFT/ALL-C 与 OFT/Stay 增加；M=2 的一项曲线在 500 万 episode 左右合作率稳定在约 75%。
- §4/ Figure 9 显示更长的 `M=3` 子序列出现合作型特征，但在相同条件下整体合作水平低于 `M=2`，因此更大的策略空间并不自动提高总体合作。

## 局限与复现

- 这是给定收益矩阵、学习参数和可选社会困境机制下的仿真观察，不是收敛或博弈稳定性的数学证明。
- 未覆盖真实互动、其他博弈、参数敏感性或完整显著性分析；正文未见完整可执行代码链接。
- 复现需固定 `N=20`、`M=2/3`、Q-learning 与温度参数，并记录按互动长度划分的 All-D/TFT/ALL-C/OFT/Stay 分布。

## 与 AAMAS 的关系与核验说明

工作讨论社会困境中的多智能体协调与关系选择。Spark 初审指出“证明”和更长互动的过度表述；本笔记按 §§2–5、Figures 1–9 将其改为仿真证据，并保留 M=3 的整体合作较低这一反例边界。
