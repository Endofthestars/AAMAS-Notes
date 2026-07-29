---
title: "Maximizing the Egalitarian Welfare in Friends and Enemies Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/YNPD9144"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YNPD9144.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["stylized_preference_model", "worst_off_agent_objective", "approximation_guarantee_scope", "asymmetric_friendship_dependence", "randomization_metric_dependence", "no_empirical_social_validation", "computational_hardness"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Maximizing the Egalitarian Welfare in Friends and Enemies Games

## 一句话总结

论文研究 Friends and Enemies hedonic games 中使最差成员效用最大化的 coalition partition：Friends Appreciation（FA）先重视朋友数量、Enemies Aversion（EA）先避免敌人。它给出复杂度、近似和若干可解特例；这些是离散、已知偏好图下的算法结果，并不说明真实人际联盟会稳定、公平或愿意遵从所生成分组。

## 方法与证据

- 每位 agent 将其他人二分为 friends/enemies；FA 按 coalition 内朋友数优先、敌人数次之，EA 反过来。目标 ESW 是所有 agent utility 的最小值，而非总福利、Nash welfare、稳定性或个体同意（§2）。
- EA 下，Lemma 1 将非负 ESW 与 strong-friendship graph 的 clique partition 联系起来。Theorem 1 证明任意固定 \(\epsilon>0\)，除非 \(P=NP\)，不存在 \(O(n^{1-\epsilon})\)-approximation，且该困难性在对称实例仍成立；Theorem 2 给出 \((n-1)\)-approximation，Theorem 3 在 strong-friendship graph 无三角形时可多项式精确求解（§3）。近似比是最坏情况、按论文定义的效用尺度给出的。
- FA 下，Observation 2 以最小朋友数 \(f_{min}\) 夹住 optimum；Theorem 4 从 Partition into Triangles 归约证明 NP-hard，即使 friendship 对称也成立（§4.1）。该结论处理显式给定的二元关系，不建模不确定、策略性报告或关系随分组变化。
- WeaklyConn 按 friendship graph 的弱连通分量成团。Theorem 5 给出：若所有 agent 至少有两个朋友，近似比为 \(2-6/(n+3)\)；若存在朋友数至多为一者，最坏为 \(n/2\)。Theorem 6 在所有 agent 恰有一个朋友时可精确求解（§4.2--4.3）；因此“近 2”不能脱离朋友度条件引用。
- RandAlgo 以输入相关概率混合 WeaklyConn 与 OneWeaklyConn；Theorem 7 在“每名 agent 的期望效用的最小值”指标下给出 \(2-5/(n+3)\)-approximation。论文明确区分它与“随机结果中最小效用的期望”：后者更严格，不能从 randomization 获得同样改进（§4.4）。
- 对称 FA 的三阶段算法（包括对低朋友度 agent 的处理与 bipartite \(b\)-matching）在 Theorem 8 下达成 \(2-4/(n+2)\)-approximation；Theorem 9 对称且 strong-friendship graph 是 forest 时精确多项式可解（§4.5）。作者仍把 FA 常数近似或更强不可近似界列为未来工作（§5）。

## 适用边界与复现

- 适用于要在明确、静态的 friend/enemy 声明下研究“最差成员也不太差”的 coalition formation 算法。使用前应先确认目标确为 maximin ESW；若关注总效益、比例公平、稳定性、个体自主、权力关系或长期合作，需另行建模和评估。
- friend/enemy 二元化、所有关系已知、效用词典序规则和对称性假设会强烈影响结果。现实关系可存在中立/强弱程度、误报、隐私、冲突升级、非互惠与动态变化；最优 ESW partition 本身不保证 core stability、无操纵或被成员接受。
- 随机算法的承诺只针对论文采用的“最小期望效用”指标；不得换成随机输出的公平保证。EA/FA 的近似因子也不可跨偏好模型、实例结构或不同效用归一化直接比较。
- 复现应实现 FA/EA utility、friendship 与 strong-friendship graph、ESW 计算及 clique/triangle reductions；分别检查 EA 的 \(K_2/K_3\) covering、FA 的 WeaklyConn/OneWeaklyConn/RandAlgo、对称情形的 \(b\)-matching，并生成满足/违反 \(f_{min}\)、对称性、triangle-free/forest 条件的实例。报告 optimum（小规模可穷举）、近似比、运行时间和每名 agent 的 utility，而非仅总福利。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 hedonic coalition formation 与算法博弈论论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YNPD9144.pdf) 核验 FA/EA 定义、Theorems 1--9、随机近似指标与 forest 特例；没有把静态图上的复杂度/近似结果误写为现实社交公平、联盟稳定或可部署的自动分组建议。
