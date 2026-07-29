---
title: "Stability in Distance Preservation Games on Graphs"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["game_theory_mechanism", "resource_allocation", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/IGTG2329"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IGTG2329.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04h"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["network-allocation", "distance-preferences", "stability", "parameterized-complexity", "graph-games"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Stability in Distance Preservation Games on Graphs

## 一句话总结

本文将 agents 分配到 topology graph 顶点，每位 agent 对部分他人的理想图距离定义成本，系统研究 envy-free、jump-stable 与 swap-stable allocations 的存在性及随 topology、agent 数和偏好图变化的参数化复杂度。

## 方法与证据

- agent 成本为其关注对象的实际距离和 ideal distance 的差之和；稳定性分别禁止换位后羡慕、单方跳到空顶点获益、或双方交换获益（§1）。
- envy-free 仅两 agent 时总存在，三人起可不存在；即使对称偏好且 ideal distances 均为 1 也 NP-complete。clique/star 可多项式解决，但 path、vertex-cover 2 或 depth-2 tree 均有 hardness（§1.1、§3）。
- 对 agent 数有 XP 算法；结合 agent 数与 vertex cover/neighborhood diversity/modular width/diameter 等 topology 参数可 FPT。对称偏好或偏好图无环时 jump 与 swap stable allocations 总存在且可多项式计算（§1.1、§4）。

## 适用边界与复现

- 复杂度结果针对论文定义的总绝对距离偏差、静态图和指定稳定性，不说明现实座位、住房或组织位置的福利、公平与行为可接受性；偏好 elicitation 本身未解决。
- 复现需形式化 graph、每对/有向偏好和 ideal distances、空顶点规则、三种 deviation、参数编码与 reductions/algorithms。实际应用还须处理不完整偏好、容量、动态到达和隐私。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/IGTG2329.pdf) 人工核对模型、主要 hardness/FPT 和存在性结论；未将理论稳定性等同于现实分配的公平或满意度。
