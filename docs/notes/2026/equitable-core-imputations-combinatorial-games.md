---
title: "Equitable Core Imputations for Max-Flow, MST and b-Matching Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "safety_verification"]
dblp_key: ""
doi: "10.65109/VJNO3737"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VJNO3737.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["owen_set_not_full_core", "characteristic_function_misspecification", "fairness_definition_choice", "np_hard_full_core_problem", "agent_identity_and_group_fairness_gap"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Equitable Core Imputations for Max-Flow, MST and b-Matching Games

## 一句话总结

论文研究 max-flow profit、MST/min-cost branching cost 与 bipartite \(b\)-matching profit 的 cooperative-game allocation。任意 core imputation 可把几乎全部 profit/cost 给单一 agent；作者以 leximin/leximax 作为公平规则，但因直接在**完整 core**求解对 max-flow/MST 是 NP-hard，转而在由底层 LP dual optimal solutions 导出的 Owen set（core 的可计算子集）中求唯一的公平 imputation：max-flow 给出 \(O(mn^2)\) 的组合算法，MST/branching 用 ellipsoid+separation oracle，\(b\)-matching 归约/扩展 assignment-game 方法。

## 方法与证据

- cooperative game 的 core 要求每个 coalition 获得至少其自身可产生的 profit（或在 cost game 中至多其自身成本），从而没有 coalition 有脱离激励。leximin 按升序最大化最小 share、再最大化第二小； leximax 按降序最小化最大 share、再最小化第二大（Definitions 2.1--2.5）。这两者是不同的分配伦理，不是单一客观公平标准。
- 在 max-flow game，agents 是 edges，coalition worth 是其 induced subgraph 的 \(s\)-\(t\) max flow；在 MST/branching，agents 是 root 以外 vertices，worth 是 coalition 加 root 的 min-cost tree/branching；在 bipartite \(b\)-matching，coalition worth 是其 induced subgraph 内 max-weight \(b\)-matching（§2.1）。因此公平对象是网络构件/节点，而非默认的人群或受保护属性。
- 论文给出反例：unit-capacity path 的 max-flow core 可把全部 profit 给一条 edge；MST path core 可把全部 cost 给最远 vertex。故“在 core”保证 coalition stability，却不保证 agent-level share 均衡（§2.1）。
- 对 max-flow，若最优 dual 为 edge length \(\delta\)、potential \(\pi\)，则 \(p_{ij}=c_{ij}\delta_{ij}\) 给 Owen-set imputation，且 Owen set 属于 core（Theorem 3.2）。完整 core 中最大最小 profit / 最小最大 profit 分别 NP-hard（Theorem 3.1），但能有效判断 Owen-set membership（Theorem 3.4）；leixmin/leximax Owen imputation 有 \(O(mn^2)\) 组合算法（Theorem 3.16）。
- 对 MST/min-cost branching，minimum-branching LP 的 dual optimal solutions 定义 Owen set，且其在 core 内（Lemma 4.2）；membership 有 separation oracle。Theorem 4.1 指出完整 core 的相应公平优化 NP-hard；Theorem 4.4 用一系列 LP 与 ellipsoid 求 Owen-set leximin/leximax，组合式多项式算法仍是开放问题。
- 对 bipartite \(b\)-matching，Owen set 来自 max-weight \(b\)-matching dual，非空且可由 optimal dual 构造；作者基于 assignment game 的算法求 leximin/leximax Owen imputation（Theorem 5.4）。文中也注明一般 core 的相关复杂性证据/后续结果，而不是宣称 full-core fair allocation 已可高效求解。

## 安全边界与复现

- 所得公平解是 **Owen set 内** 的 leximin/leximax，不一定是所有 core imputations 中的 leximin/leximax；将其简称为“公平 core allocation”会遗漏这一限制。实际系统如需完整 core 公平目标，必须面对论文给出的 NP-hardness，而非假装该算法已解决。
- core stability 假定 characteristic function 准确地反映 coalition 的生产能力/成本。网络容量、边权、参与者 ownership、可转移支付、外部性、信息不对称、监管、退出成本和 coalition formation 若不符合模型，no-secession 数学性质不等于现实谈判稳定或合同可执行。
- leximin 与 leximax 的选择本身具有规范性：前者直接抬升低 share，后者压低高 share。二者都不保证群体公平、历史补偿、最低生计、风险暴露、地域/性别/组织属性、公平程序或利益相关者同意；不可由算法单方决定。
- max-flow 将 edge、MST 将 vertex 当 agent 时，映射到真实企业/用户/社区可能有 ownership aggregation 和中介关系；拆分或合并网络元素会改变 allocation。应审计 agent identity、数据来源、图模型、权重/容量与前处理，提供解释、申诉和人工复核。
- 复现须固定 profit-vs-cost convention、图、root/source/sink、capacities/weights、\(b\) capacities、primal/dual LP formulation、Owen-set mapping、tie/precision规则和 leximin/leximax 选择；对 MST 的 ellipsoid 实现还应报告 separation oracle、bit complexity和数值容差。论文是理论/算法结果，未提供工业部署、用户研究或 distributional fairness 实验。

## 与 AAMAS 的关系与核验说明

这是 cooperative games、core allocation 与组合优化对偶性的理论论文。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VJNO3737.pdf) 核对三类 game 定义、完整 core NP-hardness、Owen-set dual construction、Theorems 3.1--3.4/3.16/4.1/4.4/5.4 与开放问题；没有把 Owen-set 内的 agent-share 公平误表述为完整 core、群体公平或现实合同稳定保证。
