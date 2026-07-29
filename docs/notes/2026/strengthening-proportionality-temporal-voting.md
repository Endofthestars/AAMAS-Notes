---
title: "Strengthening Proportionality in Temporal Voting"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/SWJZ9796"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SWJZ9796.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04j"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["temporal-voting", "approval-voting", "proportional-representation", "axiomatic-design", "social-choice"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Strengthening Proportionality in Temporal Voting

## 一句话总结

本文在每轮选一名候选人的 approval temporal voting 中扩展 JR/PJR/EJR 以外的比例代表公理，建立强弱版本 EJR+、FJR、FPJR 与 core 的蕴含/可满足性层级，并证明 EJR+、FJR 总可实现。

## 方法与证据

- 形式化 (n) 位 voter、\(\ell\) 轮、每轮一个 winner 的时序选举；群体的代表性依据跨轮共同认可候选人与成员/群体 satisfaction，而不是将每轮独立投票（§2）。
- 论文给出 temporal EJR+ 的可多项式验证与构造规则，证明它严格加强 EJR 且每个 temporal election 都有满足 EJR+ 的 outcome（§3）。
- 对 FJR，修改 Greedy Cohesive Rule，证明每个 temporal election 均存在并可计算满足 FJR 的 outcome，且 FJR 蕴含相应 EJR（§4）。
- 引入 FPJR 与 core 的时序强弱版本，梳理全部公理蕴含与反例；若每位 voter 每轮至少认可一位候选人且 \(n\mid\ell\)，Serial Dictatorship Rule 可多项式给出 strong FPJR，但该保证不在一般情形成立，且 sFPJR 与 EJR+/FJR 不可简单互推（§5–§8）。

## 适用边界与复现

- 结论是 approval ballot、固定 voters/candidates、每轮单一胜者与论文定义 cohesion/satisfaction 下的规范性保证，不推导偏好真实性、策略性投票或动态参与者环境的福利。
- 复现需记录每轮 approvals、轮数与 voter 数、采用的 strong/weak 公理、cohesive group 枚举或验证算法，以及 GCR/SDR 的 tie-breaking；现实推荐或治理应用还要另行处理曝光、学习反馈和激励。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SWJZ9796.pdf) 人工核对 temporal axioms、层级关系和 EJR+/FJR/sFPJR 的可满足性条件；未将公理满足直接表述为现实投票的全面公平。
