---
title: "Explainable Representation of Finite-Memory Policies for POMDPs using Decision Trees"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/OQGU5189"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OQGU5189.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03r"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "postprocessing-only", "decision-tree-fidelity", "representation-size-proxy", "finite-memory-policy"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Explainable Representation of Finite-Memory Policies for POMDPs using Decision Trees

## 一句话总结

DT-FSC 是对既有 finite-state controller 的保真后处理：每个 controller node 的 observation-to-action 表和 next-observation-to-memory-node 表都转成决策树。它不改变策略或最优性，但把巨大的表格和迁移原因压缩为可读的特征条件。

## 方法与证据

- 标准 FSC 图只显示 memory nodes，未解释 node 内 stationary policy 的巨大 action table，也常把大量 observation labels 堆在 transition 上。DT-FSC 分别用 DT 表示二者，FSC node 仍承担有限记忆（§1）。
- cheese-maze 示例将墙壁观测映射为动作和下一个 node；决策树展示 `CanGoUp` 未被使用，因而暴露其对策略无关，同时保持原 FSC 的精确行为（§2）。
- almost-sure reachability FSC 由 Storm 获得，quantitative benchmarks 采用已有 learned FSC，并以 dtControl 构造 DT-FSC。以表格行数对 DT node 数衡量 compactness：前者 transition/action mapping 平均缩小 13.5x/1.7x，后者为 5.54x/1.66x；每个 benchmark 的后处理需数秒（§3）。

## 适用边界与复现

- 方法解释的是已有 controller representation，不能解释 policy synthesis 是否正确、环境模型是否可信或 action consequences 是否安全；决策树更小只是 explainability proxy，仍需人类可理解性评测。
- 复现应提供原 FSC、observation feature encoding、dtControl 配置、tree pruning/tie rules、语义等价性检查、size metric 及所有 benchmark 表。特征若不具备领域语义，树也可能难以实际解释。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OQGU5189.pdf) 人工核对转换范围、benchmarks 和压缩数字；未把 representation compactness 表述为决策安全或真实用户理解度证明。
