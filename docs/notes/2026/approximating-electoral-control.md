---
title: "Approximating Electoral Control Problems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "norms_trust_governance", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/GEOD7219"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GEOD7219.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "electoral_control", "approximation_complexity", "conditional_lower_bound", "not_election_security_deployment_guidance"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Approximating Electoral Control Problems

## 一句话总结

本文系统分类 plurality、Condorcet、approval 下标准 electoral-control optimization problems 的可近似性（weighted/unweighted votes）：approval constructive adding/deleting voters 为 Log-APX-complete；对 voiced rules，constructive delete-candidates 有 \(O(m)\) additive approximation，plurality 下又给 Dense-versus-Random Conjecture 条件的 \(\Omega(m^{1/4})\) lower bound；多种 partition/其他 control problems 则在 \(P\ne NP\) 下不可近似。它是 computation/social-choice 的复杂度地图，既不能证明具体选举安全，也不授权现实中通过增删/分割 voters/candidates 操纵选举。

## 方法与证据

- control optimization 的 objective 是最小化实现 constructive/destructive preferred outcome 所需的 action（add/delete/partition candidates/voters）。选举为 finite candidate set/votes，weights可视作 copies；rules限定 plurality、approval、Condorcet（§2）。这抽象不包含法律、程序正当性、voter rights、信息环境、audit、coalition behavior或现实攻击成本。
- Table 1 覆盖“NP-hard standard control problems”；dash 表示 decision problem in P。结论只针对列出的 rules/action/outcome conventions（constructive/destructive、TE/TP），不能外推到其他 voting rules、random tie-breaking、multiwinner或实际系统。
- approval constructive add/delete voters：借 set covering/covering integer programs得 \(O(\log m)\) approximation，Theorem 3.1 为 Log-APX-complete。该是 additive/optimization complexity 分类，需区分输入 size、number of candidates/voters与允许 unregistered-voter pool；不能以“log approximation”估计实际侵害规模。
- Lemma 3.2 对每个 voiced rule给 constructive delete candidates \(O(m)\)-approximation；plurality Theorem 3.3 在 Dense versus Random Conjecture下，任一算法 ratio为 \(\Omega(m^{1/4})\)。后者是条件性 fine-grained lower bound，非无条件 P≠NP statement；摘要还指出 lower-bound instances有 \(1\le k\le d^\epsilon\)，上下界无冲突。
- Theorem 3.4：若 partition-based decision control \(T\) NP-complete，则其 optimization version除非 P=NP不可近似；Theorem 3.5 列 plurality destructive delete-candidates及 Condorcet constructive add/delete-voters。证明关键是“finding even one solution NP-hard”，不是对所有 elections 都没有可行控制，也不衡量实际安全性。

## 适用边界与复现

- 适合审计 electoral-control vulnerability 的理论/算法研究或为防护设计威胁模型；不要将近似算法用于操纵真实选举。任何现实选举变更应遵循适用法律、独立选举管理、透明审计、平等权利与公共监督。
- 复现需给 voting-rule implementations、control problem variants/TE-TP conventions、weighted encoding、reductions、covering IP formulation/rounding、hardness assumptions，逐 instance verify preferred candidate condition与 cost。报告 exact optimum small cases、approx ratio、runtime、input sizes和 randomized behavior。
- 应研究 realistic constraints（authorized changes、audit detection、cost/uncertainty）、robustness to vote noise/ties、parameterized regimes、other rules/multiwinner setting以及 defense mechanisms；明确攻击-complexity analysis与规范/法律许可之间的差别。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 computational social choice 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GEOD7219.pdf) 核验 Table 1、Theorems 3.1/3.3/3.4/3.5及 conditional lower-bound scope；没有将复杂度结果当作真实选举安全或行动建议。
