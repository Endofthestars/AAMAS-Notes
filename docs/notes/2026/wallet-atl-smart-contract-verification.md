---
title: "Wallet ATL: Towards Reliable Smart Contract Verification"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "game_theory_mechanism", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UKIO4803.pdf"
preprint_url: "https://vadimmalvone.github.io/papers/AAMAS26b.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["formal_model_scope", "wallet_encoding", "abstraction_preservation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Wallet ATL: Towards Reliable Smart Contract Verification

## 一句话总结

WATL 为 ATL 加入 wallet predicates 与财务受限的 strategic operators，使 coalition strategy 同时满足逻辑可行与资金可执行，并在 VITAMIN 中实现 model checking。

## 方法与证据

- WATL 在 Wallet Concurrent Game Structures 上解释：wallet filter 只允许 coalition 中每个 agent 负担得起所需行动的策略，因此可表述 liquidity 相关的战略能力（§3–5）。
- Theorem 5.1：WATL model checking 在 model 和 formula 大小上是 PTIME-complete，与 ATL 相同；该分析注明 wallet values 以 unary 编码，额外 wPre filter 仍为多项式（§5）。
- Meta-agent abstraction 保留目标 coalition 的 individual wallets，而将所有非 coalition agents 合并为一个 wallet sum meta-agent（§6）。
- Theorem 6.1 的 soundness 只适用于所有 strategic operators 都限于该 coalition 的 WATL state formulas；它给出 abstract true/false 对 concrete model 的保留，不是任意 coalition 或任意性质的等价（§6）。
- 实验在生成 WCGS（最多 20 agents）上比较 concrete/abstract verification；较大模型中平均 runtime 改善，论文报告特定配置约八倍 median speedup，但随机 transition 仍存在 outliers（§7）。

## 局限与复现

- WATL 保证的是给定 WCGS、wallet encoding和公式语义下的 model property，不等同于 Solidity/EVM code、oracle、链上执行或经济攻击面的全栈安全证明。
- 钱包值的 unary 编码与 finite model 是 PTIME claim 的组成部分；若改变数值表示或扩展 logic，复杂度可能变化。
- 抽象使用必须固定验证 coalition；应检查是否每个 strategic operator 均满足限制。复现还应保存 WCGS、wallet bounds、formula、VITAMIN version及 concrete/abstract verdict。

## 与 AAMAS 的关系与核验说明

该工作把 multi-agent strategic verification 扩展至财务可行性。笔记基于作者公开 [AAMAS PDF](https://vadimmalvone.github.io/papers/AAMAS26b.pdf) 核对了 PTIME 条件、meta-agent abstraction 和 soundness 量词。
