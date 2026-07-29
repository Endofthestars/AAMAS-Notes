---
title: "Multi-Agent Combinatorial-Multi-Armed-Bandit framework for the Submodular Welfare Problem under Bandit Feedback"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "marl_coordination"]
dblp_key: ""
doi: "10.65109/NBHM8571"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NBHM8571.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03w"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "submodular-valuation", "full-bandit-feedback", "oracle-complexity", "asymptotic-regret"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Agent Combinatorial-Multi-Armed-Bandit framework for the Submodular Welfare Problem under Bandit Feedback

## 一句话总结

MA-CMAB 研究不可分物品在不通信 agents 间的子模福利分配：每轮仅见总福利（full-bandit），不见每 agent 回报。作者将 noisy offline submodular welfare approximation 的 resilience 接到 explore-then-commit，给出相对 $\alpha$-oracle 的 $\widetilde O(T^{2/3})$ 期望 regret。

## 方法与证据

- 分配为 items-to-agents 的 partition matroid（每 item 至多一人、可有 agent quota）；每 agent valuation monotone submodular，总福利为各 valuation 之和，目标相对 $\alpha$-approximate offline oracle（§3）。
- 定义 $(\alpha,\delta,\eta)$ resilience：若所有可行集合的 oracle value 有 $\epsilon$ 误差，算法仍得 $\alpha f(OPT)-\delta\epsilon$。作者称 Continuous Greedy 在给定噪声界下满足 $(1-1/e,\delta,\eta)$ resilience，后接 pipage rounding（§4）。
- MA-CMAB 先探索 $\eta$ 个 allocations、再以经验 aggregate rewards 调用 resilient oracle；Theorem 4.3 给出 $O(\delta^{2/3}\eta^{1/3}C^{2/3}T^{2/3}\log(T)^{1/3})$ expected $\alpha$-regret，$C=M$ 为 multi-agent aggregation constant（§4–5）。

## 适用边界与复现

- 结论依赖已知可行集合、单调子模 valuations、独立随机 full-bandit feedback 与可调用的 resilient oracle；无通信不代表 agents 可在任意隐私/策略情境下达成该分配。
- 复现需给出 valuation/噪声、$M,N$、quota、oracle实现与 calls、探索集合、$\alpha/\delta/\eta$、regret定义和随机种子。实际分配还须处理激励相容、公平、非平稳与个体反馈缺失。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NBHM8571.pdf) 人工核对设定、resilience 和 Theorem 4.3；未将渐近理论界表述为实际市场中的公平保证。
