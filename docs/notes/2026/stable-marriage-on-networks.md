---
title: "Stable Marriage on Networks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/PKVJ4128"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PKVJ4128.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["weakened_invitation_ic", "local_stability_only", "restricted_efficiency_not_global", "network_report_assumptions", "strict_preferences_assumption", "theoretical_model_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Stable Marriage on Networks

## 一句话总结

论文研究双方均可经社交网络邀请新参与者的 stable marriage。为避免邀请者被更好 candidate 挤出，Dynamic Deferred Acceptance（DDA）每轮在 closed alliance 内做邻居限制的 DA，匹配后将剩余邻居分享给未匹配者；作者证明其达到本模型可兼容的弱边界，但性质是单方完整 IC、另一方仅邀请 IC、Stable-1 与 BFC 限制下的局部效率，而非传统全局稳定、双边完全策略无关或全局 Pareto 效率。

## 方法与证据

- 模型将男女双方置于同一无向 social network；初始 \(N_0\) 外的 agent 只有沿已报告有向 invitation chain 从 \(N_0\) 可达才 qualified 参与。每个人有对对侧加单身的 strict preference，agent 可隐瞒真实邻居（报告邻居集为真实集子集）和偏好（§3）。这假定网络、身份、偏好排名和邀请传播可被可靠定义/报告，未处理 ties、不可验证关系、重复账号、拒绝邀请、隐私或跨平台传播。
- 经典稳定性在网络中被改为 distance-\(k\) blocking pair；Stable-1 只排除相邻双方彼此更偏好的 blocking pair，Stable-2/Stable 则更强（§4.1）。因此 Stable-1 允许非邻居、甚至经更长路径可获知的双方形成阻塞对；不等同于传统 stable marriage 的无 blocking pair。
- 完整 IC4M/W 要求真实偏好与邻居报告都是 dominant；作者改用 ICI4M/W：对每个真实邻居报告，存在某个（可能不真实的）偏好报告使其至少不差（Def.4）。ICI 不能解释为“人人如实报告全部信息”；它只给 invitation 的存在性激励，且不保证偏好 truthful。
- Theorem 1：ICI4M/W 不能与 Stable-2 或 asymmetrical Stable-1a 同时满足；完全图时 Stable-1 与传统稳定一致，亦不存在同时 Stable-1、IC4M、IC4W 的机制（§4.1）。这是该形式化下的 impossibility，不代表所有现实网络匹配都必须牺牲更强稳定性。
- 效率也被限制到 bipartite fully-connected coalition（BFC）：每个 coalition 内男性与女性两侧均互为邻居。论文定义 local optimal Stable-1、local weak Pareto efficiency；若放宽到 almost BFC 或全局弱 Pareto，与 invitation IC/Stable-1 不可兼容（Prop.1–2, Thm.2–3）。所以“efficiency”只针对固定 BFC 中局部重分配，不能当作市场整体 welfare/公平/参与率最优。
- DDA 在每轮选策略无关顺序 \(P\) 中尚在市场的最早 agent，执行 propose/refusal 动态扩展 alliance，直至 alliance closed；该联盟内匹配，所有成员离场，并把离场联盟的 remaining neighbors 连接给未匹配者（sharing），随后继续下一轮（§5.2, Alg.1）。分享可让原本非邻居之后相配，但修改了剩余图；现实系统需说明信息可共享性、同意/隐私、身份校验与传播延迟。
- men-propose DDA 的 Theorem 5–8 证明：IC4M、ICI4W、Stable-1、男性 local optimal Stable-1 与男性 wPE4M-L；women-propose 对称（§5.3）。重要的是，论文不是证明 men-propose DDA 同时 IC4W：另一侧只有 ICI4W，且 local optimal/wPE 指标按 propose side 表述。
- 这是一篇定理、构造和反例论文，没有真实 dating/recruitment 平台数据、用户实验、网络生成模拟、复杂度基准或部署指标。应用到招聘/服务匹配的介绍不应误读为对 match quality、邀请率、群体公平、操纵、隐私或市场覆盖的经验验证。

## 适用边界与复现

- 适合作为“邀请可战略性影响可达市场”的双边匹配理论基线；实现前必须明确初始种子、可报告网络、资格可达性、strict/acceptable preference、proposal side、顺序 \(P\)、sharing edge 更新与离场规则，并复现其定义下的 blocking/BFC 检查。
- 产品不能声称 traditional stability 或双方 truthful strategy-proof。界面/条款应如实说明：匹配只保障当前更新网络的邻接 Stable-1，某方的 invitation incentive 允许其改变偏好报告，且非邻居阻塞、全局 Pareto 改进与 strategic collusion 没有被排除。
- 若用于真实推荐/招募，应加入 verified invitations、anti-sybil/rate limit、关系与偏好的 consent/privacy 控制、对方同意、ties/incomplete lists、退出与时间变化、群体公平/包容性审计，以及对隐藏邻居、联合谎报、延迟传播和网络不完整的稳健性测试。
- 复现应依据论文定义枚举小型 profile 检验 Theorem 1/2 的反例，实施 closed-alliance propose/refusal/sharing 和报告独立排序；对所有报告 profile 验证 IC4M、ICI4W、Stable-1、BFC local optimal/wPE-L，而不要用普通 DA 稳定性或全局 welfare 指标替代这些更弱性质。

## 与 AAMAS 的关系与核验说明

这是 social-network diffusion 下的双边 matching mechanism design 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PKVJ4128.pdf) 核对 qualification/report 模型、IC/ICI 与 distance stability 定义、不可能性边界、BFC 局部效率、DDA alliance/sharing 流程，以及 Theorem 5–8 的单方/局部性质；没有把其理论局部保证误写为真实平台效果、传统稳定、双边完全策略无关或全局效率。
