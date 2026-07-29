---
title: "ANN-CMCGS: Generalizing Continuous Monte-Carlo Graph Search with Approximate Nearest Neighbors"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: "10.65109/KAUA8981"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KAUA8981.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03f"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "heuristic-metric", "controller-reachability-assumption", "no-convergence-proof", "simulated-navigation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# ANN-CMCGS: Generalizing Continuous Monte-Carlo Graph Search with Approximate Nearest Neighbors

## 一句话总结

ANN-CMCGS 以 ANN radius query 在全局连续状态图中发现经 controller reachability check 的近似 transpositions，替代 CMCGS 的 layered clustering，允许 cycles 和跨决策增量复用。2D/navigation 实验的成功率优于 CMCGS；作者明确未分析 cyclic graph 的收敛和完备性，因此结果是经验性规划改进，不是最优/安全保证。

## 方法与证据

- candidate 只在含新信息（如终止/截断不同）时插入；可达邻居以边连接，backprop 更新其连接和 playout path（§2.1）。
- 为防 cycles 无限循环，每次 playout 选择 node 至多一次且仅沿 path backprop；不同 path 的相反更新使理论分析困难（§2.2）。
- 图 2 固定 budget 下 ANN-CMCGS/CMCGS 在 2D single integrator 为 100%/40%、double 为 100%/0%、unicycle 为 80%/27%；20 episodes 的图 3 error bars 为 SEM（§3）。

## 适用边界与复现

- 需公开 metric/radius、HNSW 参数、controller/reachability、progressive widening、collision/termination与 budgets；检验失败/回退、ANN false neighbors、动态障碍和真实机器人时延。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KAUA8981.pdf) 人工核对机制、图表与未证明的理论限制；未将 success rate 写成安全或收敛结论。
