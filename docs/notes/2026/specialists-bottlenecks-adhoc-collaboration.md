---
title: "Too Many Specialists: Emergent Inefficiencies and Bottlenecks for Multi-agent Ad-hoc Collaboration"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "human_agent_interaction", "agent_engineering"]
dblp_key: ""
doi: "10.65109/CYXP1261"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CYXP1261.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03q"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "agent-based-simulation", "kitchen-task-abstraction", "trait-modeling", "no-human-subject-validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Too Many Specialists: Emergent Inefficiencies and Bottlenecks for Multi-agent Ad-hoc Collaboration

## 一句话总结

以厨房任务为 ABM 的研究发现：高比例智能体僵化地坚持专长时，会造成等待、贡献不均与按专长分裂的协作网络；“更多专家”并不必然提高临时协作的系统效率。任务的串并行结构、团队规模和沟通成本共同决定这种瓶颈是否显现。

## 方法与证据

- 2D kitchen ABM 中，Steak 是固定顺序的串行 recipe，Onion Soup 是可并行重复子步骤。模型变动 team size、communication cost 及四类随机 traits：agreeableness、collaboration initiative、task distribution preference、skill assertion（§2）。
- 决策经分布式 Affordance--Context--Action loop；skill assertion 表示拒绝专长外任务，以刻画 specialist's dilemma（§2.2）。
- 并行 Soup 随团队变大、沟通成本低而增产但收益递减；串行 Steak 反而在较高沟通成本和较小团队下更快，因为低沟通成本所鼓励的大团队会产生冗余（§3.1）。
- 当 100% agents skill-assert 时，总完成餐数显著下降且 workload imbalance 增大；若专家同时主动沟通并偏好任务分配，影响可部分缓解。网络层面，skill assertion 高时 assortativity 为 0.578 且形成 disconnected homophilous clusters；为 0% 时变为稠密整合网（§3.2–3.3）。

## 适用边界与复现

- 结论来自简化厨房环境和人为赋予的 trait rules，不能直接量化现实工作团队或通用 LLM agent 的最优分工；高 communication cost 的“益处”取决于它恰好抑制冗余组队。
- 复现须开放格网/recipe、trait 分布、ACA action rules、team-size/communication parameter grid、随机种子、完成量与 inequality 指标、网络构图规则。后续需要真实人机团队、异质技能质量、学习/信誉和动态任务到达的验证。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CYXP1261.pdf) 人工核对任务结构、traits 与网络结果；未将 ABM 内的机制解释为现实团队的因果定律。
