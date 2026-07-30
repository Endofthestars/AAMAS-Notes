---
title: "Auditable Institutional Coordination with Episodic Memory for Robust Evacuation under Multi-Source Disruption"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["marl_coordination", "norms_trust_governance", "safety_verification", "applications", "agent_engineering"]
dblp_key: ""
doi: "10.65109/TCMA4845"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TCMA4845.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05j"
spark_draft_verdict: "source_grounded_draft_with_episode_count_and_safety_wording_risks"
spark_qa_verdict: "needs_revision_corrected_for_counting_metric_safety_and_page_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["safety_critical_simulation", "single_city_preliminary_evidence", "episode_counting_ambiguity", "evacuation_rate_not_safety_outcome", "distribution_shift_brittleness", "retrieval_negative_transfer", "topology_repair_boundary", "validator_not_safety_certificate", "schema_constrained_llm", "no_real_world_deployment_validation"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_episode_accounting_full_table_negative_transfer_metric_safety_validator_llm_and_deployment_boundary_check"
escalation_verdict: "pass_after_episode_count_table_page_safety_floor_and_simulation_boundary_corrections"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted evacuation-safety check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Auditable Institutional Coordination with Episodic Memory for Robust Evacuation under Multi-Source Disruption

## 一句话总结

这篇 Doctoral Consortium 文稿在单一 SUMO city 的 preliminary benchmark 中，把固定 institutional action schema、feasibility validator、episodic retrieval、topology-aware repair 和可选 schema-constrained LLM 组合起来；结果显示简单 repair 可修复 topology shift 下的错误重放，但 hazard relocation 会造成明显 negative transfer，且 evacuation rate 不能充当现实人员安全、鲁棒下界或部署证据。

## Institution-level coordination

论文不让 coordinator 逐车控制，而让它周期性选择可解释、可执行的 routing/access rule。当前 institutional action 是（pp. 4053–4054）：

\[
I_t \in \mathcal{I}=\{NOOP\}\cup(B\times E),
\]

其中 \(B=\{north,south\}\)，\(E=\{out\_sw,out\_se\}\)，所以单步 \(|\mathcal{I}|=5\)。在 50-decision episode 中，sequence space 为 \(5^{50}\approx 8.9\times10^{34}\)；这说明小 action vocabulary 不等于整个 planning problem 很小。

每个 proposal 都经过 lightweight validator，检查 schema validity 和当前显式 feasibility，例如不把流量引向 blocked bridge。该 validator 类似 institution-layer shield，但三页稿没有给完整 hazard/risk model、formal safety property、soundness/completeness proof 或 safety certificate。

## Episodic memory、repair 与审计日志

memory bank 保存 in-distribution successful institutions、outcomes 与 compact context cue。对比方法包括：

- **Retrieval-only**：重放 closest episode 的 institution；
- **Adaptive retrieval**：若重放 action 经过 closed bridge，则把 bridge token 确定性换成可用 alternative，再次 validate；
- **Heuristic institutions**：rule-based、validated institutional policy；
- **PPO**：end-to-end coordinator；
- **LLM / LLM+Memory**：只在相同 fixed schema 内可选地提出 institutional action。

为提高 evaluation reproducibility，LLM 的 structured decisions 被 cached，并 offline deterministic replay（p. 4054）。这不是在线自由文本规划器或现实 incident-command system。

institution layer 可记录 retrieved episode id、similarity score、repair edits 和 validation outcome，帮助判断失败是否来自 memory invocation、repair 或 validator rejection。日志增强 diagnosis 与追溯，不证明 proposal 正确、可接受或安全。

## 实验范围与计数口径

当前实验包含一个 ID scenario，以及 hazard-origin shift、topology disruption、combined hazard+topology 三种 OOD shifts。它们都来自 single SUMO city 和 compact institutional schema（pp. 4053–4054）。

原稿的计数层级需要分开阅读：

- **scenario types**：1 个 ID + 3 个 OOD，共 4 类；
- **seeds**：正文称每类 20 seeds，因此每个 coordinator 有 \(4\times20=80\) 个 scenario-seed runs；
- **reported total**：正文括注 480 episodes；\(80\times6=480\) 与 Table 1 的六类 coordinators 分别运行上述组合相容，但这是算术上的 reconciliation，原稿没有明确说明 episode total 按 coordinator 重复计数；
- **table caption**：Table 1 原文另写 “across 20 scenarios”，看起来把 20 个 seeded runs 称作 scenarios，但没有定义该用词。

因此本笔记把实验理解为 4 种 scenario types，而不是 20 种；同时保留并披露 caption、seed 与 episode-total 之间未由原稿解释的术语/计数歧义，不把上述推算冒充作者明确给出的 protocol。

## Preliminary evacuation-rate results

Table 1 报告 mean evacuation rate（ER，p. 4054）：

| Coordinator | ID | Hazard OOD | Topology OOD | Combined OOD |
|---|---:|---:|---:|---:|
| Heuristic institutions | 87.7 | 74.3 | 92.4 | 74.3 |
| PPO | 92.5 | 68.6 | 92.5 | 32.7 |
| Retrieval-only | 87.7 | 72.8 | 39.2 | 72.8 |
| Adaptive retrieval | 87.7 | 44.4 | 92.4 | 73.7 |
| LLM | 89.3 | 46.2 | 92.4 | 74.3 |
| LLM+Memory | 89.1 | 46.5 | 92.4 | 74.3 |

### Combined shift

PPO 从 ID 的 92.5 降到 combined OOD 的 32.7，主要被作者归因于 timeouts；heuristic、LLM 和 LLM+Memory 在 combined column 为 74.3。作者把这一表现称为更稳定的 “safety floor”，但这里仅是当前 simulation/metric 中的 ER：不是 casualty floor、形式化安全下界或部署保证。

### Topology shift

Retrieval-only 在 topology OOD 只有 39.2，因为 once-good institution 可能经过现在 blocked 的 bridge。最小 topology-aware repair 后 Adaptive retrieval 为 92.4，且没有 gradient update。这支持特定 token repair 在该 benchmark 中恢复 feasibility 和 ER，不支持一般的安全修复证明。

### Hazard shift 与 negative transfer

同一 repair 在 hazard-only OOD 可能有害：

- Retrieval-only 为 72.8，Adaptive retrieval 反降到 44.4；
- heuristic 为 74.3，而 LLM 与 LLM+Memory 只有 46.2/46.5；
- 增大 retrieval threshold 的 ablation 改善约 9.8 percentage points，但未报告 variance、confidence interval 或 significance。

作者解释为 mismatched episodes 被过度信任，或 topology 没变化时 repair 做了不必要的 edits。这说明 “memory + repair” 不是单调增益，需要 shift-aware gating 与 backoff。

## 指标与安全边界

论文说也追踪 casualty 与 timeout rates，但三页稿没有报告二者的数值。ER 不能替代 casualty、exposure、congestion equity、clearance time、command feasibility 或整体 safety。

当前证据还缺少：

- variance、confidence interval、statistical test 与 per-seed distribution；
- 多城市、多 network layout 或不同 population dynamics 的验证；
- 真实 evacuation/drill data 和人员行为 calibration；
- 完整约束、sensor/communication failure、uncertainty 与 adversarial conditions；
- validator 的 formal safety proof；
- 实时延迟、human-in-the-loop protocol、fallback、code 与 deployment evidence。

因此结果不能外推为现实 wildfire/flood/earthquake evacuation 已安全部署，也不能证明 LLM、memory 或 institutional rules 可取代 incident commander。

## Future Work 与引用边界

作者把后续工作分为（p. 4054）：

- near-term：学习 shift-aware similarity/gating、只在有帮助时 retrieve，并量化 memory use anomalies；
- mid-term：从 single-step directives 扩展到 staging/dynamic priorities 等 phased controls；
- mid-term：加强 institution-layer feasibility/risk checks；
- long-term：跨 population、network layout 与 urban dynamics generalisation；
- 潜在扩展到 power control 和 emergency resource deployment。

“guarantee safe degradation”出现在作者征求反馈的问题中，不是已实现保证。Reference [27] 是相关 full AAMAS paper；本笔记没有把其可能包含的方法、实验或代码倒灌为这篇三页 DC 稿的证据。

## 页码与核验说明

PDF 逐页核对：p. 4053 为摘要、动机、SUMO/TraCI、贡献概述和 action schema 开端；p. 4054 为 schema 续篇、validator、memory/repair、LLM、Table 1、preliminary results、failure analysis、audit log 与 Future Work；p. 4055 仅为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TCMA4845.pdf) 核对完整表格、计数歧义、negative transfer、validator/LLM 能力边界和 simulation-to-deployment 边界；`reviewed` 不表示现实疏散安全、鲁棒保证或现场部署已经验证。
