---
title: "Project Submission Games in Participatory Budgeting"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "norms_trust_governance", "resource_allocation"]
dblp_key: ""
doi: "10.65109/TZVZ6294"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TZVZ6294.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["full_information_proposer_assumption", "pure_nash_scope", "limited_real_instance_size", "strategic_manipulation_not_policy_recommendation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Project Submission Games in Participatory Budgeting

## 一句话总结

Project Submission Games 将 PB proposer 选择提交自己哪些项目建模为博弈，效用是最终获资助的自有项目总成本；对 BasicAV、Phragmén、MES 研究 pure NE 存在与 best response 复杂度，并以 187 个现实 PB 实例探索动态，但这不是鼓励 PB 参与者策略性隐瞒项目的制度建议。

## 方法与证据

- 每 proposer 拥有项目集并提交其子集，已知预算、所有 approval ballots、其他 proposer 与 tie-breaking；目标最大化其获资助项目 cost，rule 包含 BasicAV/GreedyAV、Phragmén、MES（§1--3）。
- 文中给出无 pure NE 的构造；Theorems 4.2--4.5 给出多种规则/设置下 NE-existence 与 Best Response 的 NP/coNP/更高层复杂性及 party-list 等充分条件。PSG/1（每 proposer 单项目）中 Theorem 5.1 保证三规则均有 NE，Theorem 5.3 给出 polynomial-time single-project best response（§4--5）。
- 用 187 个现实 PB election instances（因复杂度限制项目数）先检查 full submission，再跑 best-response dynamics，必要时 brute force；多数实例很快达 NE，87% 的 dynamics-found NE 在一次 iteration 内找到（§6）。
- 实验也比较 price of deviation、voter satisfaction 与有限信息变体；作者称有限 ballot 信息在其实例中对 proposer utility 影响小，但不是一般不完全信息 equilibrium 定理（§6）。

## 局限与复现

- 核心理论假设 proposer 精确知道所有 voter approval、竞争者项目及规则；现实 PB 的民调误差、信息泄露、沟通、联合行动、伦理与反操纵规则会根本改变博弈。
- 仅研究 pure NE 与特定 resolute tie-breaking/rules，未保证 mixed equilibrium、学习动态收敛或社会福利/代表性最优。
- 187 个实例受项目数上限和搜索策略影响；“通常有 NE”不能外推为所有城市或作为制度抗操纵结论。复现应公开数据清洗、project-owner mapping、tie-break、initial profile、dynamics/seed 与 brute-force cutoff。
- 作者列出有限 proposer knowledge、竞争者不确定性及其他 equilibrium 概念为未来方向（§8）。

## 与 AAMAS 的关系与核验说明

该文将参与式预算中的提案行为连接到计算社会选择与博弈论。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TZVZ6294.pdf) 核对模型、定理、187 个实例实验和信息假设；未将策略性提案分析表述为现实 PB 操作指南。
