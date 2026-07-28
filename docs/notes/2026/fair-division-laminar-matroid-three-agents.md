---
title: "Fair Division under Laminar Matroid Constraints for Three Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/MMPM6195"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MMPM6195.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["three_agents_only", "additive_valuation_assumption", "laminar_matroid_only", "ef1_not_envy_free", "common_capacity_assumption", "theoretical_no_empirical_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fair Division under Laminar Matroid Constraints for Three Agents

## 一句话总结

论文给出三名 agent、非负加性 valuation、共享 laminar matroid 容量约束下的多项式算法：从层级类别树的叶向根做 Round-Robin with Leftovers，并为三类各遗留两件的 `[2,2,2]` 情形设计专用六件物品分配。其结论是存在完整、可行的 EF1 allocation；这不是 envy-free、效用/公平最大化、策略无关机制，也未覆盖四名以上 agent、非加性偏好或异质 matroid 约束。

## 方法与证据

- 每 agent 对 indivisible goods 有 nonnegative normalized additive valuation；laminar family 的任意两类要么不交、要么包含，每类 \(C\) 给每个 agent 同一上限 \(\theta(C)\)（§2）。可行 allocation 需对每 agent/每类满足 \(|A_i\cap C|\le\theta(C)\)；模型不包括互补/替代、负价值、预算、agent-specific capacities、共享总容量、随机到达或策略性报告。
- EF1 定义为任意 agent 对任意他人 bundle 的 envy 可通过删去后者至多一个 item 消除（§2）。EF1 允许剩余 envy，且删哪个 item 依赖观察者 valuation；不能表述为完全无嫉妒、比例公平、MMS、Pareto 最优或群体公平。
- Main Theorem：只要 feasibility set 非空，三 agent 的任意上述实例都有 polynomial-time algorithm 计算 feasible EF1 allocation（§1, §3）。正文另以 \(\theta(C)\ge\lceil |C|/n\rceil\) 与必要时添加 zero-valued dummy items 说明完整分配的归一化条件；实际应用须先验证原始容量能覆盖所有物品，不能以虚拟项掩盖真实资源不可分配。
- 直接在每个子类独立 modified round-robin 虽能保持子类约束，却可能违反父类聚合容量（§2.1）。作者的方案自叶向根分配，使用 acyclic envy graph 的 topological order 更新下一轮 GRR，并把无法平分的低值 items 作为 structured leftovers 上传（§3）。
- 三 agent 时叶/子树每类可能留下 0/1/2 件；普通 GRR 对三组各两件的 `[2,2,2]` leftovers 可能给一个 agent 同类两件，从而违反 laminar feasibility（§3.2）。Pass_Rule_List 保留 `[1]`、`[2]`、`[2,2]` group 结构，避免将子类容量信息抹平。
- Special_6_Item_Allocation 将六件物品（每个子类两件）划成三对：每对不含同子类两件、不同时包含第二位选取 agent 的 top-two，且对第三位 agent 各含其 top-three/bottom-three 一件；按 \(\sigma(1),\sigma(2),\sigma(3)\) 依次挑 pair（§3.3）。Lemma 1 断言每人恰两件、每组至多一件、forward EF/reverse EF1；这是保证的核心且依赖 strict ordering/tie-breaking 与加性估值。
- Claims 4–6 用每一层 allocated items 等分、剩余仅 `[1]`/`[2]`/`[2,2]` 的归纳证明 EF1 与容量可行（§3.2–3.3）。结论覆盖任意 laminar tree 深度，但不自动适用于 general matroid、matroid intersection、matching/conflict constraints；论文也回顾这些非 matroid 约束下 EF1 未必存在。
- 超过三 agent 时 leftover configuration 数量组合爆炸，作者仅将当前递归框架描述为潜在基础，未给出四人或任意 \(n\) 的 algorithm/theorem（§4）。因此不能把本文宣传为“任意人数 laminar 公平分配已解决”。
- 论文是构造与证明工作：没有真实 course/project/resource 数据、用户研究、运行时间 benchmark、近似 welfare comparison 或实现压力测试。课程/团队/计算资源仅为动机，不能作为对实践公平、效率、满意度或可扩展性的实证证据。

## 适用边界与复现

- 可作为三人、共同层级配额、可加价值的 constrained fair division 理论基线。实际部署必须先将政策准确编码为 laminar tree 和每人容量，验证 `feasibility set nonempty`，处理不可接受 goods、ties、缺失价值、共同资源上限与动态变更。
- 若分配涉及人类权益，应同时评估 EF1 外的 ex-ante/ex-post 公平、Pareto efficiency、MMS/proportionality、群体影响、可解释性与申诉；EF1 不保障每人绝对满意或没有结构性不利。
- 实现时应保留 agent order、每次 GRR pick、envy-cycle elimination、leftover group 来源、Pass_Rule_List 变换和 six-item pair 构造审计日志；可独立验证所有 \(i,j\) 的 EF1 inequality 与所有 \(i,C\) 的 capacity inequality。
- 复现应固定 laminar normalization/dummy categories、\(\theta\) 与完整性条件、valuation/tie-break、leaf-to-root traversal、topological ordering、最小值 leftover 选择、special `[2,2,2]` partition、dummy items，并在小实例穷举检查 EF1/feasibility。扩展到四人以上必须新证 leftover 处理，而不是直接复用该 six-item routine。

## 与 AAMAS 的关系与核验说明

这是 constrained fair division 的算法博弈论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MMPM6195.pdf) 核对模型、EF1/laminar feasibility、三 agent 主定理、Round-Robin with Leftovers、`[2,2,2]` six-item 子程序、归纳证明边界与多 agent 未解挑战；没有把三人加性 laminar 情形的理论 EF1 误写为通用/经验性公平或效率保证。
