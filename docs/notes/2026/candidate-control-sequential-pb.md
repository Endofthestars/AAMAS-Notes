---
title: "Algorithms for Candidate Control in Sequential Participatory Budgeting Rules"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/SZOC7665"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SZOC7665.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02q"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "strategic_control_interpretation", "tie_breaking_dependence", "complexity_assumption", "no_policy_recommendation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Algorithms for Candidate Control in Sequential Participatory Budgeting Rules

## 一句话总结

论文研究 participatory budgeting 中通过加入/删除项目来让指定项目入选（constructive）或落选（destructive）的 candidate control，针对 GreedyAV 与 GreedyCost 给出按选民数 \(n\)、不同成本数 \(c\)、可控制项目数 \(r\) 等参数的复杂度分类。一般问题均 NP-hard；在固定 \(c\) 时有 \(m/c\)-approximation，但除非 \(P=NP\) 不存在 \(m^{1-\epsilon}\)-approximation。它为计算项目“可操控强度”的分析工具提供算法边界，而不为操控公共预算提供正当性或操作建议。

## 方法与证据

- GreedyAV 反复选择在剩余预算内支持数最高的项目；GreedyCost 则按支持数/成本比排序。二者是可多项式计算的 sequential welfare-based PB rules，但控制问题询问改动可用项目集合能否改变指定项目 \(p\) 的胜负（§1）。
- 论文关注构造性与破坏性控制，以及作为项目 performance/robustness measure 所需的最小控制动作。此前工作已表明两条规则下所有相关控制目标/操作组合均 NP-hard（§1）。
- 表 1 给出参数化概览：以项目总数 \(m\) 参数化显然 FPT；\(n+c\) 为 FPT（标记 \(\succ\) 的算法依赖特定自然 tie-breaking），\(c+r\) 为 FPT；若单用 \(n\) 则 para-NP-complete，若单用 \(r\) 则 XP 且 W[1]-hard；其他组合包括 XP 与 W[1]-hard 边界（§1.1、表 1）。
- 近似方面，固定 \(c\ge1\) 时存在简单 \(m/c\)-approximation；但任何 \(\epsilon>0\)，除非 \(P=NP\)，不存在 \(m^{1-\epsilon}\)-approximation。因此作者主张计算实践中的 performance measures 应优先利用 \(r\) 较小的参数化算法，而不是期待强多项式近似（§1.1）。

## 适用边界与复现

- 这是最坏情形计算复杂度与算法分类，不是对任何项目应被移除、加入或优先资助的规范性判断；公共预算中实施候选变更还涉及程序合法性、提案人权利、透明度、公平与公众信任。
- 标注 \(\succ\) 的 FPT 结论需要特定 tie-breaking；实际平台若使用随机、时间顺序或人工决胜规则，结论和控制成本可能改变，必须把 tie policy 视为输入而非实现细节。
- \(m/c\) 与下界是渐近近似比，未说明某个实际 Pabulib 实例上的质量、运行时或行为频率；参数 \(r\) 小的经验观察也不等价于所有城市都适用。
- 复现应实现两个 greedy rule、预算/批准矩阵、添加/删除操作与 tie-breaking，穷举小实例校验 solver，再按 \(m,n,c,r\) 分层报告 exact runtime、最小控制动作、近似比和失败案例；应在真实数据上脱敏并由治理主体审计操控风险。

## 与 AAMAS 的关系与核验说明

该文处于计算社会选择、资源分配与 PB 治理交叉处。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SZOC7665.pdf) 人工核对两条规则、constructive/destructive 控制、表 1 参数化分类及近似界；未将算法可行性转述为对操控或项目选择的政策建议。
