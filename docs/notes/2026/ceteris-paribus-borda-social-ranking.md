---
title: "A Ceteris Paribus Borda Solution to the Social Ranking Problem"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/WNSA8391"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WNSA8391.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "axiomatic_social_ranking", "coalitional_preorder_input", "ceteris_paribus_scope", "not_individual_merit_measurement"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Ceteris Paribus Borda Solution to the Social Ranking Problem

## 一句话总结

CP-Borda 从 coalition preorder 中只比较“固定其余成员、替换一个人”的 ceteris paribus pairs：每个可比较 coalition \(S\) 充当 voter，按 \(S\cup\{i\}\) 相对于 \(S\cup\{j\}\) 的胜负累计 Borda score，并据此排序个体。论文证明它是同时满足 Neutrality、受限 Separability、Desirability 与 Cancellation 的唯一 social-ranking solution；这是对给定形式输入和公理的刻画，不是个人能力、贡献、公平或现实合作绩效的客观排名。

## 方法与证据

- 输入是有限 individuals \(N\) 的 coalition preorder \(\succeq\in T(2^N)\)，solution 输出 \(N\) 上 total preorder（Definition 2.1）。support/participants/voters 都由实际出现的 CP-comparisons 限制，缺失 coalition comparisons、噪声、不同 coalition context 或偏好冲突如何处理，取决于该形式定义而非经验学习。
- 对不包含 \(i,j\) 的 voter coalition \(S\)，若 \(S\cup\{i\}\succeq S\cup\{j\}\)，则给出 voter preorder；\(\pi_{ij}\) 计数严格偏好 \(i\) 胜 \(j\) 的 voters。Borda score 为 \(\beta(i)=\sum_j[\pi_{ij}-\pi_{ji}]\)，CP-Borda 按 score 非递增给 total preorder（Definitions 2.2–2.3）。它聚合的只是成对、保持其余成员不变的比较，不能表示非局部协同、规模效应或 coalition 形成的因果效应。
- 四项公理包括标签重命名的 Neutrality、对 disjoint supports 且不产生新 voters 的 Separability、所有 CP 比较中系统性更好的 Desirability 和成对计数相抵时全体并列的 Cancellation（§3）。文稿特别指出 CP-Borda 不满足另一版本的 Neutrality，且其 Separability 比相关 Consistency 的适用范围更窄。
- 主结果称 CP-Borda 是满足这四公理的唯一解，证明使用 coalitional order amplification 与 profile construction；扩展摘要未给完整 lemmas/proofs、计算复杂度、敏感性、战略操纵或真实数据验证。结论同样指出还可用更一般的 coalitional preorder information 定义 alternative Borda scores。

## 适用边界与复现

- 适合 cooperative-game/social-choice 的公理化比较、需要明确 CP 解释时的理论排序；不应直接用于招聘、绩效、薪酬、信誉、政治或公共资源的自动排名。现实使用必须独立论证输入比较的合法性、代表性、偏差、隐私、申诉和可能的操纵。
- 复现需实现 preorder/support/voter construction、\(\pi_{ij}\)、Borda scores/ties及四条公理的精确定义，并重建唯一性证明的 lemmas；对小 \(N\) 穷举测试 neutrality、cancellation 与 separability 的前提。三页摘要不提供完整证明，需查完整版本后才可宣称形式化复现。
- 应比较 CP-Borda 与 CP-majority、ordinal Banzhaf及 lexicographic solutions，在 incomplete/inconsistent/noisy orders、ties、missing CP pairs、coalition-size bias和 strategic reports 下测试稳定性。输出应展示每个分数的 voter evidence、不可比性和对输入变动的敏感性，而不能将排序解释为固有价值或因果贡献。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 computational social choice/cooperative-game social ranking 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WNSA8391.pdf) 核验 CP voter construction、Borda score、四公理及唯一性主张；没有把公理化排序写成实际社会公平、个人 merit 或决策政策证明。
