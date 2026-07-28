---
title: "Participation Incentives in Online Cooperative Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/VZOJ2040"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VZOJ2040.pdf"
preprint_url: "https://arxiv.org/abs/2502.19791"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["axiom_scope", "valuation_assumptions", "computational_complexity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Participation Incentives in Online Cooperative Games

## 一句话总结

论文研究成员顺序到达、当前联盟价值必须即时且不可逆分配的合作博弈，并提出参与、强留存和早到激励等公理及新的 value-sharing 规则。

## 方法与证据

- OCG 是 $(N,v,\pi)$：非负、归一化、单调 valuation 下，玩家按到达序形成 prefix subgame，规则在每步分完当前价值（§3）。
- 除已有 STAY、Early Arrival（EA）、Shapley-Fairness（SF）外，论文定义：贡献型新玩家即时获得正收益的 PART、既有贡献者应严格获益的 S-STAY、以及经典 Individual Rationality（IR）和 Online-Dummy（OD）（§4，Definitions 5–10）。
- 既有 DMC、Shapley Value、eRFC 各有缺陷；尤其 STAY、EA 和 SF 不能同时满足（Proposition 5）。
- 论文提出 MES、NDMES、ULMES/eULMES 等规则；Table 1 汇总其公理满足性。一般 valuation 下，新规则侧重 PART、EA、STAY/S-STAY 和部分 OD，而非同时保持 SF/IR（§6）。
- Proposition 10 表明对一般 valuation 没有任何规则能够满足 IR；在 superadditive valuation 下，IR 前缀修正规则可保持此前性质，Theorem 5 指出 IR-MES、IR-NDMES、IR-eULMES 保留 IR 与已有公理（§7）。

## 局限与复现

- 公理结果属于在线、不可逆价值分配、给定到达顺序的 cooperative-game 模型；并不直接保证现实组织中的真实到达、贡献、效用或合约可观察。
- EA 是在固定其他人顺序时，早到为优势策略；它不覆盖谎报贡献、身份拆分、联盟外协商或未来价值不确定性。
- 不可能性结果很关键：一般 valuation 下不能宣称方案同时具有经典 IR。IR 结论仅在 superadditive valuation 的修正规则中成立，且以放弃 SF 等权衡为代价。
- 多项算法的 polynomial-time 条件也有范围：Table 1 中部分规则只在 simple OCG 或 subadditive valuation 下为多项式，不能概括为所有 valuation 都高效。
- 复现应枚举小规模 valuation/arrival orders，逐一检验 PART、EA、STAY、S-STAY、OD、SF 与 IR；必须把 general、subadditive、superadditive 与 simple OCG 分开报告。

## 与 AAMAS 的关系与核验说明

工作连接在线机制设计、联盟形成和参与治理。笔记以作者公开的 [论文 PDF](https://cgi.cse.unsw.edu.au/~haziz/OnlineCoop.pdf) 作主文本核验，并将一般 valuation 的不可能性与 superadditive 情况下的修正机制分开记录。
