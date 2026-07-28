---
title: "Fairness over Equality: Correcting Social Incentives in Asymmetric Sequential Social Dilemmas"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "norms_trust_governance", "game_theory_mechanism"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CZPZ7833.pdf"
code_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["simulation_scope", "asymmetry_assumptions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fairness over Equality: Correcting Social Incentives in Asymmetric Sequential Social Dilemmas

## 一句话总结

论文研究奖励范围、能力或角色不对称的顺序社会困境，修改公平内在激励以避免把自然的不平等机会误当成应被纠正的不合作。

## 方法与证据

- 摘要与 §1 指出，既有公平方法常假设智能体激励相同且能持续获得全局信息；在非对称条件下，这会错误激励背叛。
- 工作构建熟悉 SSD 的非对称变体，并作三项修改：按潜在奖励范围重定义公平、按智能体环境影响加权内在社会项、以局部社会反馈替代对其他智能体内部信息的依赖。
- 摘要报告：在论文的非对称场景中，该方法比比较方法更快形成合作策略；局部社会反馈可在不要求全局访问的条件下匹配全局访问设定的表现。
- §2 将 SSD 与囚徒困境、效率/平等/可持续性/和平等指标联系起来，强调上述结论针对其定义的社会困境与信息结构。

## 局限与复现

- 结论来自论文构造的非对称 SSD 和实验协议，不能直接外推至所有现实不平等、组织激励或多智能体任务。
- 局部反馈和影响权重的定义是方法假设；适用性取决于奖励范围、可观察性和环境影响是否能被正确建模。
- 复现需遵循论文的非对称环境、内在激励、局部反馈和比较设置；本笔记不添加原文未给出的统计或安全保证。

## 与 AAMAS 的关系与核验说明

该文连接 MARL、社会规范和协作机制。内容仅整理官方论文摘要与引言中提出的改造和实验范围，未将公平概念表述为普适伦理判断。
