---
title: "Distributed Course Allocation with Asymmetric Friendships"
conference: "AAMAS"
year: 2026
track: "jaamas"
topics: ["resource_allocation", "game_theory_mechanism", "agent_engineering", "human_agent_interaction", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/YVPS6128"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YVPS6128.pdf"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06h"
spark_draft_verdict: "high_risk_education_allocation_summary_without_quantitative_privacy_fairness_or_incentive_evidence"
spark_qa_verdict: "pass_with_decentralization_quantitative_user_study_and_governance_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["three_page_jaamas_summary", "dedicated_incomplete_lightweight_algorithm_only_high_level", "one_hundred_seventy_seven_student_preference_study_not_deployment", "no_quantitative_feasibility_welfare_fairness_runtime_or_scaling_results", "high_welfare_fairness_scalability_and_robustness_qualitative_claims", "decentralized_local_preferences_not_cryptographic_or_peer_privacy", "communication_clique_metadata_and_disclosure_risk_unreported", "asymmetric_friendship_and_social_status_sensitive_data", "recruitment_consent_ethics_demographics_anonymization_and_withdrawal_unreported", "encryption_authorization_retention_and_audit_unreported", "strategyproofness_truthfulness_manipulation_and_collusion_unreported", "protected_group_popularity_network_inequality_envy_and_individual_rationality_unreported", "human_appeal_override_and_real_course_constraints_unreported", "cited_friendship_academic_performance_not_study_outcome"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_education_allocation_asymmetric_social_data_peer_privacy_communication_metadata_user_study_fairness_incentives_network_inequality_appeal_and_real_constraint_boundary_check"
escalation_verdict: "pass_with_high_risk_privacy_fairness_incentive_and_deployment_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted educational-allocation, sensitive-social-data, privacy, fairness, and incentive check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Distributed Course Allocation with Asymmetric Friendships

## 一句话总结

本文把固定数量课程、严格 seat capacities、课程偏好与非对称 friendship preferences 建模为 ADCOP，并提出分布式 DSA_RC；评价使用 177 名学生的自报偏好和 simulated data，但三页稿只给 “commonly feasible”“high welfare”“fairness”“scalability/robustness” 等定性总结，没有任何可行率、福利、公平性、运行时间或扩展曲线数字。分布式与偏好不集中披露也不等于同伴隐私或密码学隐私保证。

## 分配模型与非对称友谊

问题是 one-sided multi-unit assignment：

- 每名学生必须获得固定数量的 courses；
- 每门课程有不可超过的 strict capacity；
- 学生同时报告 course preferences 与希望一起上课的特定 friends；
- friendship 可以 asymmetric：A 希望与 B 同课即可形成 A→B 的 preference，不要求 B reciprocate。

作者指出 friendship information 比一般 course preference 更敏感，因为不互惠关系和 social status 可能从中推断，学生可能不愿把它完整报告给 administrative office。论文把每名学生建模为 autonomous agent，完整偏好留在本地而不交给 central coordinator。

不过 capacity 是涉及全体 agents 的 global hard constraint；非对称关系也意味着 agent 可能不知道谁把自己视为 friend。论文因此要求 agents 形成 communication clique。这里的 “fully decentralized”描述 central aggregation 边界，并没有说明 peer-to-peer messages、relationship metadata 或 intermediate utilities 对其他 agents 的可见范围。

## DSA、ACLS 与 DSA_RC

- 标准 Distributed Stochastic Algorithm（DSA）面向 symmetric DCOP，没有处理 peers 感知到的 asymmetric constraints。
- Asymmetric Coordinated Local Search（ACLS）协调共享 constraint 的 agents，但假设 asymmetry 仅位于 constraint 两侧的 cost/utility；本文的 asymmetry 更宽，连 constraint 是否存在都可能只被一侧感知。作者指出，直接应用 ACLS coordination 可能暴露关键 friendship information。
- Course capacity 同时是 global 与 hard，促使作者提出 DSA_RC，专门处理 resource capacity constraints。它以 distributed search 寻找满足全部容量且具有高 overall utility 的 assignments。

三页稿把 DSA_RC 定位为 incomplete lightweight algorithm，只给 high-level description；pseudocode、message protocol、termination、convergence、complexity 和 formal analysis 留在 journal version。不能从摘要补写最优性、稳定性、strategyproofness 或隐私机制。

## 177 名学生与评价定义

User study 收集 177 名学生对 available courses 和 specific friends 的自报偏好，并据此构造同时包含 capacities 与 social preferences 的 allocation instances。Figure 1 只是这批自报 friendship network 的 directed graph：A→B 表示 A 把 B 视作 friend，vertex size 由 incoming arcs 数量决定；它不是 allocation-performance 图。

论文定义三类评价：

1. **Feasibility**：满足所有 course-capacity constraints；
2. **Social welfare**：agents 的 aggregate utility；
3. **Fairness**：检查 utilities 的 distribution，作者还把低 dispersion/不同 allocation-order positions 的分布作为公平性表述。

除此之外，论文称在 simulated data 上考察 varying conditions 下的 scalability 与 robustness，并称结果与 user-study trends 一致。

## 定量证据边界

三页稿没有提供结果表或数值，也没有报告：

- course 数量、具体 capacities、每名学生所需 course 数或构造出的 instance 数；
- questionnaire、preference scale、friendship elicitation 与 utility construction；
- feasibility rate、infeasible count 或 constraint-violation count；
- welfare value、normalization、optimality gap 或 baseline comparison；
- fairness formula、dispersion、quantile、order effect 或 protected-group breakdown；
- runtime、iterations、messages、bandwidth、memory 或 students-scale curve；
- simulated-data generator、varying conditions、parameter ranges；
- DSA/ACLS/centralized solver/linear-programming 的实测对照；
- runs、seeds、variance、confidence interval、significance 或 failures。

所以 “commonly finds valid allocations”“high social welfare”“fairness”“scalability”“robustness”“consistent”都是作者的定性摘要。论文称问题 NP-hard、exact linear programming 对数十到数百名学生不实际，但没有在本稿中用 runtime experiment 验证这项比较。

177 名学生提供的是 preference data，不是实际选课 deployment、学生满意度、retention 或 academic-performance outcome。论文引用 friendship 与 academic performance 的既有研究作为背景，不能改写成本算法提升成绩的证据。

## 隐私、公平与激励治理

三页稿未报告：

- study recruitment、context、demographics、informed consent、ethics/IRB、withdrawal；
- friendship/course data 的 anonymization、minimization、retention、deletion 与 reuse；
- agent authentication、message encryption、access control、secure aggregation、audit logs；
- communication-clique 中 peer visibility、traffic metadata 与 relationship inference 防护；
- truthful reporting、strategyproofness、friendship inflation/suppression、collusion 或 identity abuse；
- popularity effects、non-reciprocal rejection、social-network inequality 与 isolated students 的影响；
- protected-group fairness、envy、individual rationality、priority rights 或 distributional guarantees；
- human review、appeal、correction、override 和 explanation；
- timetable conflicts、prerequisites、degree requirements、quotas、waitlists、accessibility accommodations 等真实 course-allocation constraints。

这些是当前摘要未披露的控制，不是已经发生隐私泄漏、歧视或操纵的证据。高影响教育部署需要把 social-welfare objective 与学生权利分开审计，并提供不提交 friendship data 的替代路径、可申诉结果和人工监督。

## 页码核验

- p. 4194：题名、摘要、引言、method contributions 与 model 开始；
- p. 4195：model、DSA/ACLS、DSA_RC、user-study evaluation、discussion 与致谢；
- p. 4196：参考文献，没有新增结果。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YVPS6128.pdf) 核验；`reviewed` 不表示 full JAAMAS article、算法形式保证、定量性能、学生数据治理、广义公平、激励安全或真实部署已独立验证。
