---
title: "Universal Solvability for Robot Motion Planning on Graphs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VEXW9837.pdf"
preprint_url: "https://arxiv.org/abs/2506.18755"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["discrete_graph_motion_scope", "one_sided_random_error", "augmentation_bound_scope", "continuous_robotics_gap"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Universal Solvability for Robot Motion Planning on Graphs

## 一句话总结

USolR 判断给定无向图与 $p$ 个标号机器人，任意离散 vertex configuration 是否都能通过合法无碰撞 graph moves 互达；论文给出线性随机一侧错误算法、近线性的确定性算法，并研究使不可解图变为 universally solvable 所需的边/点增广。

## 方法与证据

- configuration 将每个标号 robot 映到不同图顶点；valid move 是沿边的 simple path move 或 simple rotation，始终不碰撞。USolR 问所有两个 $p$-robot configurations 是否互达，使用 Yu–Rus 的 FRMP $O(|V|+|E|)$ 可达性子程序（§2–3）。它不是连续平面/三维机器人、任意形状、动力学、时间同步、传感不确定性或真实碰撞几何模型。
- canonical accumulation 将任意配置映到固定大小顶点集上的 canonical configuration，再以 reachability equivalence classes 分析。Lemma 15 证明 NO-instance 中从给定配置不可达的配置至少占一半；这是随机测试能区分的核心（§3–4）。
- Theorem 16：随机抽取配置并做 FRMP 的算法运行 $O(|V|+|E|)$，一侧错误——YES-instance 总输出 YES；NO-instance 可能输出 YES，概率至多 $1/2$。重复抽样可降低 false-positive 概率，但单次结果不构成不可解图的确定性证明（§4）。
- Theorem 19 用至多 $p-1$ 个指定配置比较做 derandomization，得到 $O(p(|V|+|E|))$ 的确定性算法。Theorem 24 进一步按图稠密度：若 $|E|<p|V|$ 为 $O(p(|V|+|E|))$；若 $|E|\ge p|V|$ 为 $O(|V|+|E|)$（§5–6）。
- EAUS 只研究 connected、原本非 universally solvable 的图。论文给出一般图至多 $p-2$ 条新增边即可达到 universal solvability 的上界，并构造无限族需要 $\Theta(p)$ 边（§7，Theorem 27）。这是存在性/界，不是给定 budget 下 EAUS 的完整多项式决策算法。
- VEAUS 允许同时加 $\alpha$ 顶点与 $\beta$ 边；论文为族 $Z_{\alpha,\beta}$ 给出 lower bounds，并推出无限族结论（Theorem 29、Corollary 30）。该部分不等于对任意图找到最小 $(\alpha,\beta)$ 的优化算法，且作者将 disconnected augmentation 留作未来工作（§7–8）。

## 局限与复现

- “universal”只量化图上的离散标号配置，不保证一个具体实际仓库地图、带尺寸机器人、单向通道、动态障碍或调度窗口可执行；把连通图简单嵌入平面也不保留物理碰撞可行性。
- FRMP 子程序与 move model 是所有复杂度的基础；若允许 simultaneous movements、不同 rotation 规则、机器人不可交换标签、occupancy 约束或连续时间，equivalence-class 结论需要重建。
- 随机算法的错误仅发生在 NO 图误报 YES；安全/部署筛查不应直接使用一次 YES 作为通行证明，应采用确定性版本或经过置信度放大的独立检测，并生成具体 move plan 后再验证。
- 边增广的 $p-2$ 上界不包含铺设成本、可行走性、路网法规、机器人数量随时间变化或加边引发的其它调度问题；$\Theta(p)$ 下界只说明有难族。
- 复现应固定 intrinsic vertex order、配置采样、FRMP 实现及 path/rotation semantics；验证 Lemma 15 的类大小、随机错误频率、Theorems 19/24 的边密度分支及 augmentation 构造。还应将 graph solution 与连续多机器人仿真分开报告。

## 与 AAMAS 的关系与核验说明

该文为多机器人离散重排和图规划提供 universal reachability 的高效判定。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2506.18755) 核对 USolR/FRMP、随机/确定性算法、稀稠复杂度分支及 EAUS/VEAUS 范围；不将图论结论外推为连续机器人安全保证。
