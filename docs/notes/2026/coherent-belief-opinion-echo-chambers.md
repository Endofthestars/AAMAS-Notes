---
title: "Coherent Belief and Opinion Propagation Produces more Echo Chambers"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "argumentation_reasoning", "human_agent_interaction", "marl_coordination"]
dblp_key: ""
doi: "10.65109/PQIV4263"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PQIV4263.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["abstract_social_simulation", "shared_values_assumption", "echo_chamber_measure_choice", "rewiring_model_dependence", "no_empirical_social_network_validation", "causal_overgeneralization_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Coherent Belief and Opinion Propagation Produces More Echo Chambers

## 一句话总结

论文将 bounded-confidence opinion dynamics 与 propositional-belief merging 合并：agent 只和 opinion 与 belief 都足够接近的 neighbors 互动，并可通过共享 values 让 belief 与 opinion 相互同步。用强连通分量的同质、隔离、强化三条件计数“echo chambers”后，抽象模拟显示同时传播 belief/opinion 会产生更多但较小的 chambers、涉及略少 agents；加入 coherence 时平均数进一步上升，但逐配对参数并非稳定单调。结果是特定符号模型与 rewiring rule 的计算观察，不是对真实社交平台、个体心理或信息治理的因果结论。

## 方法与证据

- 每个 agent 的 cognitive state 是对一个 topic 的标量 opinion \(O\in[0,1]\) 与一组 propositional beliefs \(B\)。belief distance 是模型集合的 Hamming/symmetric-difference distance；concordant neighbor 必须同时满足 opinion tolerance \(\epsilon\) 与 belief tolerance \(\delta\)（§2）。
- OD 用所有 concordant neighbors 的 opinions 做 bounded-confidence averaging；BR 用 belief-revision merge 更新 beliefs。OD/BR 后，OF 可由 beliefs 和 value map 形成 opinion，BA 可筛选/对齐 beliefs 以适合当前 opinion；这四步形成 coherence protocol（§4）。
- “values” 是对所有 Boolean interpretations 的固定评分，用来连接事实 belief 与好/坏 opinion。实验中所有 agents 共享同一、不随时间变化的 values map；因此模型没有价值多元、身份/权力、说服、谎言、媒体机制或策略性操纵（§4.2、§7）。
- 论文用 strongly connected components 作为候选 chamber，并要求：outgoing-edge ratio \(L(C)\le0.5\)（segregation）、maximum within-component opinion distance \(\le10^{-5}\) 或 belief distance=0（homogeneity）、及该最大距离在 component lifespan 中不增加（reinforcement）。这是一个设计选择；作者承认可换成其他 partition/structure（§5）。
- 四设置：S0 仅 opinion dynamics、S1 仅 belief revision、S2 两者、S3 两者加 coherence。固定 \(|A|=100\)、初始 400 directed edges、3 atoms \(p,q,r\)、topic \(p\)、5,000 iterations，\(p_{active}=p_{rewire}=0.5\)、\(\mu=\alpha=0.5\)；随机 beliefs/opinions与 20 seeds（§6--7、Table 2）。
- Table 3 的最终均值：S0 opinion chambers 1.71（97.2% agents involved）；S1 belief 2.03（79.3%）；S2 opinion/belief 为 2.70/2.52（86.8%/74.9%）；S3 均为 3.00（81.7%/80.4%）。更多 chamber 同时伴随较少参与 agents，不能直接称极化/伤害更严重（§8、Table 3）。
- tolerance 增加时 chambers 减少。对 S3 相对 S2，1104/1400（78.86%）实验中 opinion 与 belief chamber counts 增加或不变；但作者明言 pairwise comparison 不显示直接系统性增加关系（Table 4）。所以 H3 仅有总体均值支持，非所有参数/seed 的定律（§8）。

## 适用边界与复现

- 模型中的 belief 是有限 propositional formulas，opinion 是单轴数值，网络 rewiring 为按不一致而 unfollow/follow 的随机规则；它不能表示现实信念证据质量、自然语言歧义、推荐算法、跨议题关联、离线关系、群体身份、平台治理或人类学习。
- echo chamber count 对强连通组件、\(L\le0.5\)、homogeneity thresholds、reinforcement window和是否排除 singleton 极敏感。应报告完整分布、component size、参与比例、网络 modularity/assortativity、扰动持久性与替代 detector，而非只报数量。
- 同一 shared values 假设会人为强化 belief--opinion coherence。若研究现实社会，应允许 heterogeneous/dynamic values、不同 tolerance、asymmetric influence、external news/algorithmic exposure，并以真实可审计数据校准或验证；即便如此也需避免将相关 simulation pattern标成因果机制。
- 用于平台/治理建议前，应进行透明的 stakeholder participation、privacy-preserving data practice、混合方法/实地验证、少数观点和言论自由影响评估，并避免依据模拟自动降低分发或改变用户连接。
- 复现应固定 SOBA version/notebook、agent/edge count、logic atoms/topic、value map、initial-state distribution、\(\epsilon,\delta\) grids、activation/rewiring/\(\mu,\alpha\)、termination/stabilization rule、20 seeds、component detector与统计检验；额外做 rewiring-free、heterogeneous-values、larger graph、different topology和 perturbation robustness ablations。

## 与 AAMAS 的关系与核验说明

这是 opinion dynamics、belief revision 与多智能体社会模拟工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PQIV4263.pdf) 核对 cognitive representation、四个更新操作、echo-chamber measure、实验参数、Table 2--4及作者对 S3 配对结果的限定；没有将抽象模拟的平均 chamber 数误写为真实平台中 belief coherence 必然导致更多回音室的实证或因果事实。
