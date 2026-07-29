---
title: "DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "applications"]
dblp_key: ""
doi: "10.65109/SBAY6258"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SBAY6258.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["llm_context_limit", "api_cost_and_latency", "prompt_sensitivity", "heuristic_feasibility_scope", "benchmark_and_timeout_dependence", "solver_comparison_scope", "synthetic_mkp_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization

## 一句话总结

DRAGON 在已有全局解上迭代地让 LLM decomposition agent 找出可改进子结构，再让 reconstruction agent 生成局部替代解并经可行性检查整合；它在大规模路由、装箱和合成多背包问题上获得可行且有竞争力的解，但性能依赖分段和 prompt，且每轮大上下文调用的成本与时延使其不适合无约束的实时求解。

## 方法与证据

- 框架不要求 LLM 直接表示整个组合解。decomposition agent 从当前解和积累经验中选择局部子问题，reconstruction agent 在约束下重构，integration 将其合回全局解；不满足约束的解会被 checker 标注原因并存入 memory。停止条件是 1 小时或连续 5 次无提升（§3--4.1）。
- 评估涉及 TSP（TSPLIB EUC_2D，77 个、50--20k nodes）、CVRP（CVRPLIB 19 个、至 5k nodes）、Weibull-5k BPP 与 10 个合成 MKP。路由表的比较统一使用 gpt-4o；测试机器为无 GPU 的 Ubuntu 20.04、i9-10900X 20 cores（§4.1）。
- Table 1：在 TSPLIB 全部 77 个实例，DRAGON 平均 gap 12.24%，略优于 ReEvo(a) 13.10%，并在 500 nodes 以上各组优于该对照；在 CVRPLIB 19 个实例，DRAGON 20.15%，优于 ReEvo(a) 24.17%。这不是每个规模组均最佳，例如 TSP 50--500 nodes 的 DRAGON 9.74% 高于 ReEvo(a) 8.17%。
- 对 Weibull-5k BPP，DRAGON gap 0.33%，低于 FunSearch 0.69%、EoH 0.66% 和 EoH expert 0.55%，但推理时间 487.873 s，远高于 FunSearch 2.292 s（Table 3）。作者指出代码生成方法的离线进化成本未纳入这张表，因而这不是完整成本比较。
- 模型消融比较 gpt-4o、gpt-4.1、o3、r1：o3 平均 gap 最低却有很高 output-token 与时延；r1 在 >10k nodes 时超过 65,536 input-token 上限而未完成；论文因此选择 gpt-4.1 作质量、速度和 token 效率的折衷（§4.3.2）。
- 在合成 MKP（最大决策规模约 3M）上，DRAGON 在大实例维持低于 0.5% gap，CP-SAT 小实例通常更好、最大案例约 3% 且超时。该结果只说明这套合成分布和时限下的折衷，不能证明泛化到实际供应链约束（§4.4.2）。

## 适用边界与复现

- 适用于可明确编码约束、接受分钟级或更长迭代，并能将可行性独立验证的离线/半离线大规模组合优化；不能仅依靠自然语言 agent 结果执行车辆调度、配送或资源分配。
- 作者明确指出重构质量对 decomposition 策略和 prompt 敏感；不当分段或 prompt 会产生次优/退化解，而大上下文的反复 divide-and-conquer 会带来显著计算开销，当前流程对小问题不高效（§4.5）。
- 复现必须固定初始解/元启发式、子问题大小和接受准则、prompt/memory、checker 与反馈文本、模型快照/上下文与 token 上限、API 重试/价格、时限与 early stopping、TSPLIB/CVRPLIB/BPP/MKP 实例、oracle/lower bound 和所有随机种子；报告可行率、每轮改进、API 调用、输入/输出 token、总 wall-clock 与全部实例分布。
- 部署应将硬约束、容量、时间窗、法规、车辆/人员状态和失败回滚置于确定性 solver/checker 中，并用人工审批或保守优化处理不可行/超时结果；LLM 提议只可作为候选局部修改，不能替代约束验证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 中以两个 LLM agents 协作处理大规模组合优化的论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SBAY6258.pdf) 核验数据集、Tables 1/3、模型 token 限制、时限和作者局限；没有将其可行解或部分基准优势描述为所有实例上的最优、低成本或实时调度保证。
