---
title: "PyVRP+: LLM-Driven Metacognitive Heuristic Evolution for Hybrid Genetic Search in Vehicle Routing Problems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "applications"]
dblp_key: ""
doi: "10.65109/ISFV2587"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ISFV2587.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["llm_generation_reproducibility", "offline_design_cost", "best_of_multiple_runs", "benchmark_scope", "operator_compatibility", "runtime_hardware_dependence", "code_generation_guardrails"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# PyVRP+: LLM-Driven Metacognitive Heuristic Evolution for Hybrid Genetic Search in Vehicle Routing Problems

## 一句话总结

PyVRP+ 以 GPT-4.1 在固定 PyVRP 函数接口内进化 HGS 的 parent/survivor selection 与 penalty update operators，并通过“领域初始化—诊断—假设—实现—反思”提示框架指导搜索。六类 VRP 基准上的平均成本较原 PyVRP 改善 0.33%--2.70%，但这是经多轮 LLM 生成与筛选的离线设计结果，成本、随机性和实例分布均应一并报告。

## 方法与证据

- Metacognitive Evolutionary Programming (MEP) 先提供 VRP/HGS 知识和常见陷阱，再让 LLM 读取两个 parent heuristics 及其分数，完成诊断、单句可检验 Design Hypothesis、受固定签名/允许 API 约束的代码生成和反思；候选被放回 HGS 评估（§4--5）。
- 每个组件搜索 10 generations、每代 10 offspring、保留 top 5；整个过程用不同随机种子重复五次，并在结果中报告其中最佳 heuristic。LLM 为 GPT-4.1，temperature 1.0，其余如 top-p/max_tokens 使用默认值（§5）。因此结果包含 search seed、模型版本与“best of five”的选择效应。
- 组件级 TSP100（100 instances）中，select_parents、select_survivors、update_penalties 的平均成本改善分别为 2.23%、0.69%、0.12%（Table 1）。完整 solver 再在 PyVRP 的六类 VRP、每类 60 instances 上评估（§5、Table 2）。
- Table 2：PyVRP+ 的平均 cost 相比 baseline 在 CVRP/GVRP/MDVRPTW/PCVRPTW/VRPB/VRPTW 改善 0.33%/2.01%/1.45%/2.48%/0.66%/2.70%。时间并非全部下降：GVRP 0.87→1.89 s，而 PCVRPTW 7.92→4.19 s；应将质量与执行成本分开看。
- Ablation：去 Domain-Aware Initialization 的性能通常低于 full MEP；去 structured Reason–Act–Reflect 的 reactive evolution 在 CVRP、MDVRPTW、VRPB 等会退化（Table 3）。论文支持该提示结构在该搜索设置中的价值，但并未独立检验 prompt、模型采样、代码筛选和评估预算各自的因果贡献。
- 作者区分一次性 design cost 与最终执行成本：每个最终组件发现约需单张 H100 3--4 小时、约 100 次 API calls 和 \$15--20；最终表格主要报告每个实例的 execution time（§6）。这不是零成本自动化，也不等价于不同硬件/不同 API 价格下的总体成本。

## 适用边界与复现

- 适用于可将启发式算子隔离为有严格接口、可自动测试的研究型 VRP/HGS 系统；生成代码必须在沙箱、白名单 API、语法/类型/单测/资源上限和人工审查下运行。
- 论文覆盖六个 PyVRP 变体，且结论本身将未来验证扩展到原 PyVRP 的 48 variants；不应泛化为所有车辆调度、动态请求、真实交通、在线鲁棒性或任意组合优化问题的性能保证。
- 最佳候选来自五次搜索，使用模型和默认采样参数会随 API 版本变化；需报告完整 prompts、知识库、候选代码、有效/失败生成比例、每代评分、seed、token/API/硬件账本及所有 run 的分布，而非仅最佳个体。
- 复现应固定 PyVRP commit、六类实例与 BKS、预算/终止条件、HGS 和评估 seeds、GPT-4.1 快照/temperature/默认参数、代码 guardrails、10×10 population evolution、top-5 保留与五次重复；同时报告 train-search versus held-out instances、绝对目标、耗时、内存、可行率和显著性检验。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 中以 LLM agent 辅助启发式发现和车辆路径规划的工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ISFV2587.pdf) 核验 MEP 流程、GPT-4.1 搜索预算、Tables 1--3 与硬件/成本；没有将离线 best-of-search 结果描述为免费、稳定或可直接部署的通用调度系统。
