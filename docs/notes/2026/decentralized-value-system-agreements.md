---
title: "Decentralized Value Systems Agreements"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "argumentation_reasoning", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/FXWO5737"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FXWO5737.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["value_representation_normative_choice", "homophily_segmentation_risk", "confidence_bound_tuning", "survey_inference_limit", "decentralization_not_privacy_guarantee", "no_democratic_legitimacy_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Decentralized Value Systems Agreements

## 一句话总结

本文以 value system 的“alternatives×values interpretation matrix + value-weight vector”表示个人价值观；agent 给出可让步的 confidence bounds，网络中只保留仍可接受的关系，并在每个连通分量以约束 decentralized gradient descent 求一个 group-specific agreement。PVE 与 European Values Study 的既有推断数据上，较小 bounds 形成更多、内部更相似的群体并提高多数个人的模型 utility；这是一种指定表征与优化下的分组聚合，不能证明价值已被正确推断、群体分裂正当、去中心化自动保护隐私，或结果具民主/法律合法性。

## 方法与证据

- value system 定义为 \(V=(\mathcal V,\mathcal A,X,\Omega)\)：\(X\) 是每个 alternative 在每个 value 上的评价矩阵，\(\Omega\) 是 simplex 上的 value importance weights（Def. 4.1, §4）。矩阵被解释为价值的情境含义、weights 为相对优先级；把复杂、争议与权利性价值压为数值矩阵/权重是规范性建模，受问卷、编码和量表影响。
- 每个 agent 为 matrix 与 weights 设置 \(\gamma_i^X,\gamma_i^\Omega\) confidence bounds，并用距离/utility 表示候选 agreement 是否可接受（§4–5）。bounds 是允许妥协的输入，而不是从行为自动得出的真偏好；它们控制谁被分到一起、多少 agreement 产生和谁被排除。
- 算法从 connected social graph 出发，按 homophily/置信条件更新邻接与 mixing weights；当 agents 不再能接受彼此 agreement 时 links 被断开，随后在各 connected component 解 local aggregate（Eqs. 5–7, §5）。作者称 links 可继续发现/维持，不强制永久 segregation；但以相似性断边仍可能放大同温层、让小群体孤立，并没有反映权力、代表性、协商程序或冲突调解。
- 每个 component 上的状态更新是 projected decentralized gradient descent：在 compact convex feasible set 内混合邻居 estimate、沿 private utility gradient 走一步并投影（§3, §5）。收敛论证依赖 connected graph、bounded gradients、递减 stepsize、symmetric/doubly-stochastic mixing 等 Assumptions 1–3；异步、恶意、掉线、策略性报告、非凸 value utility 或动态人口没有该保证。
- 在满足这些条件时，作者写出各分量共同极限为最大化该分量成员 utilities 之和的 agreement（§5）。这是 utilitarian aggregate objective；论文也比较单一 centralized aggregation 的 utilitarian/egalitarian variants，但局部 sum-optimum 不等于逐人 consent、少数权利、程序正义或跨群体公平。
- PVE case 使用 2020 Sùdwest-Fryslân energy-policy Participatory Value Evaluation 的既有 value-system estimates（5 values、6 policy options）；EVS case 使用 2017 European Values Study 的 country-level systems（§6.1–6.2）。confidence bounds 由 pairwise Frobenius/Euclidean distance distribution 的 quartiles（\(Q_1,Q_2,Q_3\)）选择，而非参与者自行验证的个别让步阈值。
- PVE 中 bounds 变小会增加高 utility density、降低群内 distance 且产生更多更小 groups；作者举 \(Q_2\) 在近似 \(Q_1\) utility 下以 8 而非 45 groups 作为可解释性折衷（Table 3–4, Fig. 2）。EVS 也显示 bounds 收紧时 utility range 改变/群内相近（Fig. 3, Table 5）。这些是该数据、estimation 和 bounds 下的模型 output，不能证明实际公民接受群体划分或会按 derived ranking 行动。
- 论文主张去中心化可降低单点集中敏感数据的风险（§1），但 peer-to-peer exchange、mixing/gradient 信息和链接元数据本身仍可能泄漏偏好；文中未提供 differential privacy、secure aggregation、threat model 或攻击评估。

## 适用边界与复现

- 适用于研究多种可解释 value representation 下的多 agreement 生成，或在明确自愿参与、可撤回的模拟/协作式系统中探索群体 trade-off。应把 derived agreements 视为候选输入，交由受影响者、领域专家和合法治理程序审阅。
- 不能用来自动定义公共政策、医疗/国防优先级、内容治理或个人权利限制。高影响场景需要合法授权、包容性代表与抽样、透明说明、独立 facilitation、少数/不可妥协权利的硬约束、申诉/退出、对分群伤害的监控以及审计记录。
- 复现需公开/获准访问 value-system inference、\(X,\Omega\) scaling、network topology、utility formulas、\(\gamma\) selection、distance metrics、mixing matrix、stepsize和 stopping criteria；复现 PVE/EVS 的 Q1/Q2/Q3 与最大 bounds，报告每 group size、within-group distance、每人 utility、边演化及未达成 agreement 的 agents。
- 应研究参与者自己设定/修正 values 和 bounds、纵向变化、跨文化/语言 measurement invariance、策略性或恶意报告、privacy-preserving decentralized optimization、连通性/不平等/极化影响，以及将数值 agreement 与真实 deliberation、consent、decision outcomes 的实证比较。

## 与 AAMAS 的关系与核验说明

这是 AAMAS value-based alignment/collective decision-making 中的去中心化聚合工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FXWO5737.pdf) 核对 value-system 表征、confidence bounds、homophily link/mixing、projected DGD 假设与分量收敛、PVE/EVS 数据、quartile bounds 和 group-count/utility 结论；没有把数值 value agreement 误写成准确的人类价值推断、隐私保护、社会共识、反极化或民主合法性保证。
