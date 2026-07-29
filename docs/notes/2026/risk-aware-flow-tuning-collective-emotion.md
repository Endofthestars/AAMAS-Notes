---
title: "Risk-aware Flow Tuning for Collective Emotion in Social Media via Multi-agent RL"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "norms_trust_governance", "safety_verification"]
dblp_key: ""
doi: "10.65109/KMUB2012"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KMUB2012.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["social_media_exposure_manipulation", "simplified_diffusion_simulator", "affect_model_proxy", "topic_valence_label_noise", "community_impact_heterogeneity", "engagement_objective_tradeoff", "no_field_trial"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Risk-aware Flow Tuning for Collective Emotion in Social Media via Multi-agent RL

## 一句话总结

论文在 topic-conditioned Independent Cascade 与用户 affect simulator 上，以 CTDE-MAPPO 学习两个曝光流控制量：friction 降低传播概率并加 cooldown，balance 重权候选内容以增加既有 corrective/positive/diverse exposure；目标降低负面曝光峰值、超阈时间/面积与极化，同时保持 engagement floor。它不删帖或封号，但依然会系统性塑造谁在何时看到什么，且“情绪风险”来自简化模型和离线反事实，不能当作对真实用户福祉或平台治理正当性的证明。

## 方法与证据

- 平台在固定的 topic-conditioned IC kernel 上控制 \((friction,balance)\in[0,1]^2\)：friction 通过 probability scaling/cooldown 减速，balance 从现有内容中提高 corrective/positive 与多样 exposure；actor 按 shard 决策、central critic 训练，执行时在 user granularity 生效（§1、§3）。这是 exposure ranking/intervention，即使不移除内容也会改变可见性、发言影响与信息获得。
- 用户 engagement propensity 以 logistic mixed model 估计，sensitivity 以短期负面曝光与 affect change 关系估计，并固定进模拟；用户 affect 更新含负面 exposure、balance hit 与噪声（§2.2--§3）。这些量不是可验证的心理健康临床指标，也不能从观察性 Twitter 数据中建立因果伤害关系。
- 数据为 Kaggle COVID-19 与 mpox Twitter corpora；Sentence-BERT+HDBSCAN/BERTopic 得到 COVID 28 topics、mpox 9 topics，VADER 只作 valence reporting/evaluation descriptor（§2.1、§4.1）。topic/valence、interaction edges和参与行为都有语言、样本、标签和选择偏差；“不进入 per-user decision”也不消除其作为模型环境/优化信号的规范性影响。
- 目标包括 peak negative exposure rate、time/area above threshold 与对 neutral baseline 的 JS polarisation；threshold 在 validation 上取 baseline 80th percentile，MAPPO 的 engagement floor、per-step caps、smoothness 用 primal-dual Lagrangian 处理（§3--§4）。风险阈值、neutral baseline、cooldown 和预算皆为治理选择，不是客观、普遍认可的安全标准。
- Figure 2 报告本方法 Peak 0.237（k-node removal 0.283、uniform downranking 0.418）、Area Above Threshold 1.08（1.84、3.67）、Final Polarization 0.25（0.78、0.81）（§5.2）。这是同一 learned simulator、共同 seeds/engagement floor 下的数值，不能外推为真实平台的情绪改善或减少极化。
- 消融显示 friction-only 的 Time-to-Clear 13（full 11）但 polarization 0.75；balance-only polarization 0.30但峰值更高且 TTC 15（§5.3）。这显示两杠杆在该模型内互补，不提供针对错误信息、仇恨、政治言论或脆弱群体的安全结论。
- 作者承认 simplified diffusion simulator、topic/valence noise、cooldown/budget 的规范性选择和跨 community 异质影响，并建议仅在透明、独立监督下做 small reversible trials（§5.4--§6）。

## 适用边界与复现

- 适用于研究话题级曝光节奏与模拟 contagion/affect proxy 的关系，或为可逆、审计型排序干预建立假设；不应直接在真实社交平台自动调控情绪、政治信息或个人 exposure。
- 不删内容/账户并不等于价值中立：重排、减速、纠偏混合会影响表达、到达、创作者收益和群体话语权。需评估言论自由、程序正义、透明度、用户选择、差异影响、操纵风险与法律权限。
- 复现需固定语料/许可/预处理、topic model、valence、图构建、chronological split、IC/affect/engagement/sensitivity估计、sharding、MAPPO/Lagrangian、threshold/cooldown/budgets、baseline selection与随机 seeds。报告完整行动 trace、所有 shard/topic 的风险/engagement/极化、置信区间、FDR、多种 counterfactual 和失效案例。
- 若考虑实地测试，必须经过独立伦理/法律审查、告知与可退出机制、最小化敏感数据、预注册指标、独立审计、逆向/停止开关和对群体伤害的持续监测；离线模拟优于 k-removal 绝不授权部署。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多智能体强化学习、社会计算与平台风险治理论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KMUB2012.pdf) 核验 flow-layer controls、IC/affect 环境、两份 Twitter 语料、风险指标、Fig. 2--3 数值和作者的 ethics/limitations；没有把模拟负面曝光/JS 指标改善误写为真实心理健康、极化、内容安全或正当平台治理的因果证明。
