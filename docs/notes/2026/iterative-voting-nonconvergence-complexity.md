---
title: "Complexity of (Non-)Convergence in Iterative Voting"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: "10.65109/MDLZ8000"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/MDLZ8000.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["plurality_rule_scope", "coalition_coordination_assumption", "truthful_start_requirement", "lexicographic_tie_breaking", "weighted_stubborn_cycle_model", "static_preference_scope", "complexity_not_runtime_estimate"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Complexity of (Non-)Convergence in Iterative Voting

## 一句话总结

论文首次给出迭代投票收敛/循环检测的复杂度结果：从 truthful profile 出发，在 plurality、群体同时作出“直接且每人获益”的改票下，是否能在给定步数内到达 strong Nash equilibrium 是 NP-complete；在加权 voter 与固定（stubborn）票分数的扩展下，是否存在指定长度的循环也是 NP-complete。即使存在稳定状态，也可能从真实起点永远不可达；因此机制分析不能只检查 equilibrium 是否存在。

## 方法与证据

- 论文把 ballot profile 作为 state graph 的节点、允许的操纵作为有向边；稳定状态是 sink。单人 beneficial action 对应 Nash equilibrium，群体 beneficial action 对应 strong Nash equilibrium。所有结论均用严格偏好、resolute rule 与固定的 lexicographic tie-breaking（§2）。
- 主要的 group action 规定：一组 voter 可同时改票，且每位改票者都严格偏好新 winner；每张改后 ballot 还必须把新 winner 放在第一位（direct）。该协调性与“只改变一张票”的模型不同，不能把结论混用（§1.1、§2.2）。
- Theorem 3.1 给出 plurality 实例：strong Nash equilibrium 存在，但从 truthful state 经任何 beneficial-and-direct 序列都到不了它。因而 equilibrium existence 不是从真实投票过程的可达性保证。
- Proposition 3.2 利用 plurality 的结构表明，给定状态是否稳定可多项式检查：对每个可能新 winner，让所有更偏好它的 voter 同时直接投它即可作为充分检查。这个验证事实使有长度上界的路径证书可在 NP 内核验。
- Theorem 3.3：给定一元编码的步数上限 (\ell)，在 plurality 与群体 direct/beneficial actions 下，从 truthful state 到 stable state 的路径是否长度至多 (\ell) 为 NP-complete；困难性由 Restricted Exact Cover by 3-Sets 归约（§3.2）。这是“最快收敛”决策问题，不是对任意运行轨迹的平均运行时间估计。
- Theorem 4.1：在 plurality 的加权 voter、候选人固定支持分数（stubborn voters）扩展中，是否有给定长度的群体 direct/beneficial cycle 为 NP-complete；归约自 Partition，构造中已令 cycle length 为 3（§4）。这说明检测非收敛本身也可能难，而循环会使最坏情况下的收敛时间无界。
- TB（top-bottom）启发式中，更新者把真实 top candidate 放到 ballot 顶端、当前 winner 放到底端。Theorem 5.3：任意 Pareto-efficient rule、2 voters、3 candidates、每步单人 TB 下没有长度大于 2 的 cycle；Theorem 5.4：若两人同步 TB，任意 (m\ge3) 都存在实例，使每个 second-choice Pareto-efficient rule 出现长度 (m) 的 cycle（§5）。同步更新可根本改变稳定性。
- 论文明确保留开放问题：NP-complete 结果在常数 voter/candidate 数、single-peaked 偏好等限制下是否仍成立，以及 Theorem 5.3 是否可推广到更多 voter/candidate（§6）。

## 适用边界与复现

- 适用于要审计反复改票、意见轮次或 agent collective choice 的机制，尤其要同时记录起始 profile、更新协议、同步/异步语义、tie-breaking 与 coalition 信息；缺任一项都不能判定是否适用本结论。
- NP-completeness 仅针对 plurality 加上特定的群体 direct/beneficial dynamics，循环结果还使用 weighted voters 与 stubborn scores；它不证明 Borda、Condorcet rule、单人 best response 或实际平台的异步 UI 都难或必然不收敛。
- 复现可实现 profile-state graph 的显式枚举（小实例）、plurality score/tie-break、direct-beneficial edge validator、sink 检查与 bounded path/cycle 搜索；分别测试 Theorems 3.1、3.3、4.1 的构造。大实例应用 SAT/ILP/搜索时应报告上界、超时与未证明性，而非把未找到 cycle 当作已收敛。
- 工程上建议用单人或受限异步更新、循环检测与 step budget，并在循环出现时回退到仲裁/随机化/一次性投票；同时评估 coalition 操纵、身份权重、固定票源和策略性偏好申报的治理风险。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 computational social choice 与多智能体动态机制分析工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/MDLZ8000.pdf) 核验摘要、§2 的 action semantics、Theorems 3.1/3.3/4.1/5.3/5.4 及 §6；没有把特定 plurality 与协调改票模型下的理论困难性外推为所有迭代投票部署的经验性能结论。
