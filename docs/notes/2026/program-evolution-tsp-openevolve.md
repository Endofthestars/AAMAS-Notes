---
title: "Demonstrating Program Evolution on the Traveling Salesman Problem"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["generative_agents", "agent_engineering", "planning_scheduling", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/NWXS1507"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NWXS1507.pdf"
demo_url: "https://youtu.be/XAZW770jQZ8"
code_url: "https://github.com/strangecreator/openevolve-project/tree/tsp-example/examples/tsp_tour_minimization"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05w"
spark_draft_verdict: "source_grounded_with_required_baseline_provenance_held_out_statistical_compute_and_executable_code_safety_corrections"
spark_qa_verdict: "needs_revision_corrected_for_author_count_combined_score_fixed_resource_baseline_wall_clock_adaptive_overfitting_and_best_result_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["adaptive_overfitting_to_128_instance_pool", "no_held_out_final_test", "single_completed_evolution_run", "best_evolved_result_not_expected_performance", "plus_minus_statistic_undefined", "cross_source_baseline_wall_clock_not_controlled", "combined_score_weights_unreported", "fixed_resource_limits_unreported", "no_seeds_multi_run_or_ablation", "llm_version_prompt_tokens_and_cost_unreported", "total_compute_budget_incomplete", "change_summary_context_information_loss", "generated_executable_code_sandbox_unreported", "solver_correctness_validation_unreported", "resource_abuse_and_supply_chain_risk", "unseen_size_and_distribution_generalization_unreported", "first_reliably_autonomously_systematically_claim_boundaries"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_adaptive_overfitting_baseline_provenance_statistical_interpretation_compute_budget_reproducibility_generated_code_sandbox_and_generalization_check"
escalation_verdict: "retain_single_run_adaptive_pool_scope_only_high_risk"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted experimental-validity and executable-code safety check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Demonstrating Program Evolution on the Traveling Salesman Problem

## 一句话总结

作者用 OpenEvolve 和 DeepSeek-Reasoner 直接进化完整 TSP solver，在一次 8,165-iteration run 中得到平均 tour length \(23.30\pm0.019\) 的 best solver；但同一 128-instance pool 持续参与 selection、没有 held-out final test，基线数字也未说明为同机重跑，因此结果支持本设置下的程序演化演示，不证明独立期望性能、严格速度优势或通用算法发现可靠性。

## 公开资源

论文提供：

- [TSP example 源码](https://github.com/strangecreator/openevolve-project/tree/tsp-example/examples/tsp_tour_minimization)；
- [演示视频](https://youtu.be/XAZW770jQZ8)。

本文依据三页论文核验实验叙述，没有把站外仓库当前状态、依赖版本或可运行性视为已经审计。

## OpenEvolve 演化闭环

OpenEvolve 是受 AlphaEvolve 启发的 evolutionary programming framework。它维护 candidate-program archive，并在每轮执行：

1. 选择已有 program；
2. 调用 LLM 提出 code-level modification；
3. 直接应用修改，得到完整可执行 solver；
4. 在 task-specific protocol 与 fixed resource constraints 下执行评估；
5. 保留改进 variants，丢弃较弱 candidates。

TSP solver 通过统一接口接收 instance 并返回完整 tour。初始 program 来自 nearest-neighbor-guided MCTS。论文使用通过 API 调用的 DeepSeek-Reasoner。

Archive 的 combined score 使用 average tour length 与 total time，但论文没有给出两个量的归一化、权重、排序规则、惩罚函数，或 “fixed resource constraints” 的具体 CPU time、memory、timeout 与 failure policy。

## 长运行的上下文压缩

TSP solver 可能跨多个 source files。为避免把完整修改历史放入 LLM context，系统在每次修改后保存 concise natural-language summary，并在后续把 summary 与当前 solver implementation 一起提供。

该做法减少 context 开销，但论文没有验证 summary 是否保留：

- 先前修改的原因和隐含 invariant；
- 已失败尝试与回归信息；
- numerical、performance 或 security assumptions；
- 多文件之间的状态依赖。

因此它是工程策略，不是已验证的无损 program-evolution memory。

## Instance pool 与适应度评估

每个 instance 是 unit square 中均匀采样的 1,000-node Euclidean TSP。论文构造 128 个 independently sampled instances；每个 evolutionary iteration 从这同一 128-instance pool 随机抽取 48 个评估 solver。

“independently sampled”描述 instances 的生成方式，不代表最终评估独立于 evolution。由于 8,165 轮 selection 反复接触该 pool，archive 可能逐渐适应该固定有限样本。论文把它称为 test set，但没有另设：

- evolution 从未见过的 held-out final instances；
- 新 random seeds；
- 不同 node count；
- 非 unit-square 或结构化 distributions。

所以 best solver 的 pool performance 不能直接解释为 unseen instances 上的 expected performance。

## 完整 run 与展示

结果来自一条 completed evolutionary run：

- 8,165 iterations；
- 每轮 candidate generation 约 2 分钟；
- 每轮在 48 instances 上 parallel evaluation 约 10 分钟；
- 评估使用 12-core CPU。

把每轮两段时间简单相加可估算约 \(8{,}165\times12=97{,}980\) 分钟，但论文没有直接报告总 wall-clock；并行、失败、排队或重启方式也未说明，因此不把约 68 天写成实测总耗时。

演示分两阶段：

- replay completed evolutionary run，显示 average tour length trajectories 与 archive changes；
- 用 best evolved solver 搜索单个 1,000-node instance，显示 current tour、best-so-far tour 和 tour-length trajectory。

可视化帮助检查 search dynamics，但没有形成独立的 algorithmic explanation、causal attribution 或 user study。

## Table 1

论文在 128 个 1,000-node instances 的表格中报告：

| Method | Type | Avg. tour length | Time |
|---|---|---:|---:|
| Concorde | Exact solver | 23.12 | 6.65 h |
| LKH3 | Heuristic | 23.12 | 38.09 m |
| Att-GCRN | SL + MCTS | 23.52 | 43.94 s |
| Rethink MCTS | KNN + MCTS | 23.63 | 3.34 m |
| UTSP | UL + MCTS | 23.39 | 2.67 m |
| Evolved TSP | Program evolution | \(23.30\pm0.019\) | 28.27 m |

正文把前几行描述为 TSP-1000 dataset 上的 representative performance figures reported for existing methods，并把 Evolved 行描述为本演示得到的 best average tour length。三页稿没有说明所有 baselines 都由作者在同一 12-core machine、相同实现、compiler、budget 和 stopping condition 下重跑。

因此：

- tour-length numbers 可用于表中语境下的参考定位；
- time 列不能当作受控同机 wall-clock benchmark；
- `23.30` 是 best evolved result，不是多次独立 evolution runs 的均值；
- `±0.019` 没有定义为 standard deviation、standard error、confidence interval 或其他统计量。

作者自己也说明这不是 definitive state-of-the-art result，并把结果表述为在 specific LLM evolution budget 下具有竞争力。

## 缺失的实验信息

三页稿没有报告：

- multiple independent evolution runs、seeds 或 success rate；
- initialization、LLM、archive、combined score 或 context summary ablation；
- held-out final test 与 adaptive-selection correction；
- DeepSeek-Reasoner exact version、prompt、temperature、token budget 或 API cost；
- full wall-clock、并行 worker 数、memory、compiler、dependency、timeout 或 energy；
- `±0.019` 的定义和样本单位；
- solver tour validity、duplicate/missing-node checks 或 exact optimality gap；
- generated patch tests、sandbox、network/filesystem permissions、rollback 或 malicious-code handling；
- unseen sizes、other coordinate distributions、asymmetric/metric/non-Euclidean TSP。

公开源码有助于后续复核，但不自动补足论文中未报告的 experimental protocol。

## 自动生成可执行代码的风险

OpenEvolve 直接执行 LLM 修改后的完整 solver。若用于更广泛的 automated algorithm discovery，需要控制：

- arbitrary code execution 与依赖/供应链修改；
- filesystem、network、credential 与 process permissions；
- infinite loop、fork bomb、memory exhaustion 或 adversarial resource gaming；
- solver 通过 invalid tour、缓存答案或利用 evaluator bug 提高 score；
- external API model update 导致不可重复的 mutation distribution；
- summary context 隐藏曾发现的 regression 或 unsafe change。

论文没有说明 sandbox、static analysis、unit/property tests、tour validator、resource isolation 或 audit log。高风险等级来自大规模自适应搜索和执行生成代码时的验证缺口，不表示公开 demo 已出现恶意行为。

## 作者主张的边界

“first”带有 “to the best of our knowledge” 限定；“reliably discovers”“autonomously improve”“systematically improve”“competitive”以及“general framework”都应限定为作者对本演示的解释。

一条 completed run 表明该流程可以在给定 instance pool 和 budget 下产生一个有竞争力的 solver，但不能单独证明：

- 多次运行稳定发现同样质量的算法；
- 改进来自可泛化逻辑而非 pool-specific adaptation；
- 任意 optimization problem 都能取得类似效果；
- 无人工 infrastructure、protocol 或 evaluator design 介入的完全自治。

## 页码核验

- p. 4131：身份、背景、贡献主张、GitHub 与视频；
- p. 4132：OpenEvolve、DeepSeek-Reasoner、instance pool、8,165 iterations、展示流程和 Table 1；
- p. 4133：致谢与参考文献，没有新增实验细节。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NWXS1507.pdf) 核验；`reviewed` 不表示 held-out generalization、基线 wall-clock 公平性、统计稳定性、solver correctness、generated-code safety 或通用算法发现能力已经验证。
