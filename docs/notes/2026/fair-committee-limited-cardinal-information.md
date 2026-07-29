---
title: "Fair Committee Selection under Ordinal Preferences and Limited Cardinal Information"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/KFMY7437"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KFMY7437.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02k"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["metric_preference_assumption", "group_quota_scope", "distortion_not_realized_fairness", "distance_query_requirement"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fair Committee Selection under Ordinal Preferences and Limited Cardinal Information

## 一句话总结

论文研究附群体最低代表名额的 ordinal fair k-center：只用 agents 对候选的完整排序并查询少量距离，在 metric 假设下实现常数 distortion；给出 `O(k²)` 查询的 3-distortion 及 `O(k log²k)` 查询的 5-distortion 算法。

## 方法与证据

- agents/alternatives 是同一 metric space 中的 points，agents 只报告与未知距离一致的 complete rankings。选择 k 个 centers，须满足每个 group `G_i` 至少 `α_i` 名代表，social cost 是任一点到 committee 的最大距离（Definition 1.1）。
- 质量以 distortion 衡量：算法成本与拥有完整 cardinal distances 的最优可行委员会成本的最坏比值（Definition 1.2）。论文指出不查询 cardinal values 时，对 `k≥3` 不可能做到 constant distortion。
- 先从 fair-oblivious Gonzalez-style greedy 得 progressive cover，再用 bipartite projection graph 的 left-perfect matching 把中心映射到满足 quotas 的 groups。对任一前缀 `T_ℓ`，`λ_ℓ` 是图可有 left-perfect matching 的最小半径（§2）。
- 将候选距离缩为 `k²` 个，可得 3-distortion/`O(k²)` queries。为进一步减 query，使用可二分的单调 predicate `P(ℓ)≡4λ_ℓ≤cost(T_ℓ)`，选择相邻的 L/L+1 候选；Theorem 2.1 给 5-distortion 与 `O(k log² k)` queries（§2）。

## 适用边界与复现

- 结果依赖 rankings 与某个 metric 一致、agents=candidates、groups 为 partition、硬 quota 可行，以及能查询准确 cardinal distances；现实投票/代表选择中的非 metric 偏好、策略性报告、交叉身份、资格与隐私不在模型内。
- group quota 是代表性的一种形式，而 egalitarian k-center 是最小化最大距离；两者不自动对应程序公平、比例代表、实质性代表性、群体福利或歧视风险。
- distortion 是相对不可观测 cardinal optimum 的 worst-case 理论比，不能直接说明具体委员会在真实偏好、政治合法性或治理结果上的质量；5-distortion 还以较少 queries 换取较松保证。
- 复现应提供 k/groups/quotas、ordinal profile 与 metric generation、query oracle、Gonzalez order、projection graph/matching、predicate/pivot/binary search、tie-breaking，并报告查询数和成本相对完整 cardinal optimum 的对照。

## 与 AAMAS 的关系与核验说明

这是偏好信息受限下的公平委员会选择理论。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KFMY7437.pdf) 核对 Definitions 1.1--1.2、§2 与 Theorem 2.1，保留 metric/查询/配额条件，不将 distortion 泛化为现实代表性保证。
