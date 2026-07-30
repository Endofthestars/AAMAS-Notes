---
title: "LLM-Guided Multi-Agent Evacuation Coordination via Episodic Memory and Cognitive Task Analysis"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "marl_coordination", "planning_scheduling", "robotics_embodied", "human_agent_interaction", "safety_verification", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/SEYR5220"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SEYR5220.pdf"
demo_url: "https://youtu.be/oliDIjvz_Sw"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06c"
spark_draft_verdict: "evidence_insufficient_for_safety_governance_deployment"
spark_qa_verdict: "needs_revision_preserve_seed_episode_wording_table_values_and_timeout_not_casualty_boundary"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["single_synthetic_sumo_road_network", "west_to_east_fire_shift_only", "fixed_150_agent_evaluation", "twenty_seed_vs_episode_wording_difference", "zero_shot_gain_mainly_timeout_not_casualty", "safe_and_save_lives_author_claims", "cta_logs_not_complete_auditability", "reproducible_pipeline_without_reproduction_artifacts", "broad_transfer_not_evaluated", "hazard_sensing_and_communication_failure_unreported", "operator_override_fail_safe_and_accountability_unreported", "prompt_injection_and_episodic_memory_poisoning_unreported", "location_privacy_and_simulation_to_real_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_table_casualty_claim_real_emergency_auditability_fail_safe_memory_poisoning_location_privacy_and_simulation_to_real_check"
escalation_verdict: "evidence_insufficient_for_safety_governance_deployment"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted real-emergency safety and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# LLM-Guided Multi-Agent Evacuation Coordination via Episodic Memory and Cognitive Task Analysis

## 一句话总结

论文在一个 SUMO 合成城市中让车辆执行 stochastic RL policy，再由 LLM Commander 稀疏发布高层 routing rules；Fire-on-West 训练到 Fire-on-East zero-shot 时，episodic memory 将 evacuation rate 从无记忆的 74.2% 提至 82.5%，但 casualty rate 始终约 7–8%，提升几乎来自 timeout 减少。结果只覆盖固定 150 agents、一个 road network 和两个 fire origins，不能作为真实疏散、生命安全、广域 transfer 或完整可审计性的验证。

## 两层协调架构

下层每个 vehicle/user agent 根据局部观察执行 learned stochastic reinforcement-learning policy。上层 LLM Commander 观察 network-level congestion 与 wildfire spread，并偶尔发布 broad routing rules，模拟 emergency-management actions。

比较策略包括：

1. No-Commander (Random)；
2. static Rule-Based heuristic；
3. Fire-on-West 上训练的 PPO；
4. PPO 加 sparse LLM Commander rules，分别关闭/启用 episodic memory。

论文称 user agents 接收 Commander decision 后仍根据局部行为选择疏散，但没有完整公开命令 acceptance policy、冲突处理或 agent 不服从机制。Demo UI 显示 Commander policies、executed actions、rule acceptance rate 与 retrieved episodes。

## Episodic memory 与 CTA

每个历史 episode 形成 summary vector \(e_i\)，编码 fire location、congestion pattern 等 scenario cues，并存储

\[
m_i=(e_i,s_i,o_i),
\]

其中 \(s_i\) 是 Balanced-Flow、South-Exit-Bias 等 strategy，\(o_i\) 是 outcome。给定当前 embedding \(e_t\)，系统以 cosine similarity 检索 top-\(k\) episodes，并偏好相似条件下 evacuation rate 较高、timeout rate 较低的策略。

Memory On 的 memory bank 只由 Fire-on-West training scenario 填充，不含 Fire-on-East zero-shot episodes。论文没有报告 \(k\)、embedding dimension/encoder、memory update/eviction、retrieval failure 或污染防护。

Cognitive Task Analysis（CTA）记录 Commander decision 的 fire side、bridge congestion 等 hints，并用 rule-weighted score

\[
Q_{\mathrm{CTA}}(\sigma\mid s_t)=\sum_j w_j c_j(\sigma,s_t)
\]

总结支持某策略的规则。论文明确说 CTA rules “do not affect control”；日志和 decision-tree summary 提供 inspection interface，但不是控制正确性、不可篡改 provenance、责任追溯或完整 auditability 的证明。

## Table 1 精确结果

表题口径为 mean ± std over 20 random seeds、150 agents/episode；Fire-on-West 是 training distribution，Fire-on-East 是 zero-shot。Memory On 只评测 Fire-on-East。

| Policy | ER Train | CR Train | TR Train | ER Zero-shot | CR Zero-shot | TR Zero-shot |
|---|---:|---:|---:|---:|---:|---:|
| No-Commander (Random) | 51.5 ± 8.2 | 7.3 ± 1.1 | 41.2 ± 7.8 | 48.2 ± 9.1 | 7.5 ± 1.3 | 44.3 ± 8.5 |
| Rule-Based | 78.4 ± 5.3 | 7.2 ± 0.9 | 14.4 ± 4.8 | 71.3 ± 6.8 | 7.4 ± 1.0 | 21.3 ± 6.2 |
| PPO (RL) | 92.6 ± 2.1 | 7.4 ± 0.8 | 0.0 ± 0.0 | 67.1 ± 8.4 | 7.6 ± 1.1 | 25.3 ± 7.9 |
| LLM Commander (Memory Off) | 92.7 ± 1.9 | 7.3 ± 0.7 | 0.0 ± 0.0 | 74.2 ± 6.2 | 7.4 ± 0.9 | 18.4 ± 5.8 |
| LLM Commander (Memory On) | — | — | — | 82.5 ± 4.1 | 7.3 ± 0.8 | 10.2 ± 3.9 |

ER、CR、TR 分别是 evacuation、casualty、timeout rate，并定义为 \(ER+CR+TR=100\%\)。

表题写 “20 random seeds”，§4 写 “20 random episodes”。笔记保留这个措辞差异；论文没有进一步说明两者是否严格指同一组评测，也没有报告训练 episode 总数。

## 结果应该如何解释

PPO 的 zero-shot ER 为 67.1%，Memory Off 为 74.2%，Memory On 为 82.5%；相应 TR 从 25.3% 降至 18.4% 和 10.2%。CR 保持约 7–8%。

作者进一步称所有 casualties 都在不超过 7 steps 内发生、median 为 0，通常早于 coordination 生效；忽略火势或把火势速度提高 16 倍，对 CR 的影响也很小。因而该 benchmark 的政策差异主要是 congestion/timeout 向 successful evacuation 的转换，不是 casualty reduction。

这支持“所列合成 shift 中改善 ER/TR”的陈述，不支持：

- 已减少真实死亡或验证 “save human lives”；
- 已证明 safe emergency routing；
- 已跨 agent count、geography、road network 与 wildfire dynamics transfer；
- 已处理 delayed ignition、sensor error、communication failure 或 human behavior。

## 评测与复现缺口

正文只展示一个 non-orthogonal synthetic city、固定 150 agents 和 West/East 两个 fire origins。未报告：

- 多 road networks、城市、agent counts、hazard dynamics 或真实事件；
- PPO/LLM model version、prompts、temperature、training steps/episodes 与主要 hyperparameters；
- Commander rule acceptance policy、memory \(k\)/embedding、CTA weights 的确定方法；
- baseline 的调参和计算预算公平性；
- significance test 或 confidence interval；表中只有 mean ± std；
- runtime、decision latency、tokens、API cost 或通信负载；
- code repository、data/config、model weights 与完整 reproduction package。

因此 “reproducible pipeline”是作者表述，而不是已提供完整复现工件的事实。

## 真实疏散治理边界

论文没有报告真实 emergency deployment 所需的：

- wildfire/traffic sensing error、forecast uncertainty 与 stale-data detection；
- communication latency/loss、network partition 与 malicious message；
- LLM command validation、geofence/route constraint、independent safety monitor；
- operator authority、override、fail-safe degradation 与 emergency shutdown；
- decision provenance、immutable audit、责任分配和事后复盘；
- prompt injection、episodic-memory poisoning、bad-strategy rollback；
- vehicle/location privacy、retention、access 与 external model transmission；
- simulator-to-reality calibration、field exercise 和 regulator/operator validation。

这些是未报告的控制，不是论文已发生事故或攻击的证据。高风险来自系统面向生命关键决策的定位和结论被过度外推的后果。

## 页码核验

- p. 4164：题名、作者、摘要、引言、视频、两层架构与方法开头；
- p. 4165：Table 1、episodic memory/CTA、结果、Demo Interface 与结论；
- p. 4166：致谢与参考文献，没有新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SEYR5220.pdf) 核验；`reviewed` 不表示真实生命安全、完整审计性、复现包、广义 transfer 或应急部署治理已经得到验证。
