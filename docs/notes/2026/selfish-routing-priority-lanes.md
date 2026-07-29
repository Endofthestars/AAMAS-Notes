---
title: "Selfish Routing Games with Priority Lanes"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "marl_coordination"]
dblp_key: ""
doi: "10.65109/DDUV6893"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DDUV6893.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02i"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["nonatomic_linear_routing_assumptions", "edge_specific_pricing", "poa_scope", "transport_equity_not_modeled"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Selfish Routing Games with Priority Lanes

## 一句话总结

论文把每条边的 regular/paid-priority 两类服务加入 nonatomic routing game；在线性延迟下，若优先费等于该边社会最优流的边际拥堵外部性，任一均衡的总边流即社会最优，PoA 为 1；统一价格一般做不到。

## 方法与证据

- 图上每条边的基础 latency 为 `â_e(x)=a_e x+b_e`。priority users 付 `ω_e` 并只受 priority flow 影响；regular users 受两类 flow 影响。用户同时选择路径和服务级别，目标为最小化其 perceived cost（§2）。
- Theorem 2.1 给任意 priority price vector 下的均衡存在性；服务级别的流量拆分可能不唯一，但 Theorem 2.2 声明所有均衡的总 edge latency 与 total cost 相同（§2）。
- 令 `f*` 是无优先服务原问题的社会最优 flow。在线性延迟下，对每边设 `ω_e=f*_e·l'_e(f*_e)`，Theorem 3.1 说明每个优先车道均衡的总 flow 等于 `f*`，故 PoA=1（§3）。
- Theorem 4.1 给出存在的线性实例：任意 uniform priority price、即便可只在任意子集边设置优先服务，PoA 都可任意接近 `4/3`（§4）。

## 适用边界与复现

- 结论依赖 nonatomic flows、线性 latency、连续可分需求、edge-specific fee 及已知社会最优 flow。它不直接处理离散驾驶者、容量/排队、需求不确定性、支付能力、出行目的、执法或道路建设成本。
- “voluntary”指用户可选付费服务，不表示无强制或公平问题：edge-specific congestion fee 与优先服务仍可能在可负担性、地域与群体间产生分配后果，模型不评估这些问题。
- PoA=1 是理论 total-latency 效率，不是道路安全、排放、收入、可接受性或个人福利的保证；uniform pricing 的负面结论也仅针对最坏情形。
- 复现需定义网络/commodities/demands、线性系数、priority cost、均衡求解与 social optimum、服务顺序和 total-cost 衡量；实地政策还需交通数据校准、需求响应、分配影响与公众治理审查。

## 与 AAMAS 的关系与核验说明

这是机制设计与拥堵博弈的理论分析。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DDUV6893.pdf) 核对 §2--4、Theorems 2.1--2.2、3.1 与 4.1，未将其模型内最优性扩展为现实优先车道政策认可。
