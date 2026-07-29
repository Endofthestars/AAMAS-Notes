---
title: "Kidney Exchange: Faster Parameterized Algorithms and Tighter Lower Bounds"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/VKIC3106"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VKIC3106.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["theoretical_result_scope", "asymptotic_runtime_only", "complexity_assumption", "compatibility_graph_quality", "no_clinical_evaluation", "no_fairness_or_policy_analysis"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Kidney Exchange: Faster Parameterized Algorithms and Tighter Lower Bounds

## 一句话总结

论文给出受帮助患者数 \(t\) 参数化的 Kidney Exchange 最快已知确定性 FPT 算法，运行时间 \(O^*((4e)^t)\approx O^*(10.88^t)\)，并刻画若干结构参数下的不可解性：对 pathwidth 仍 W[1]-hard、对 \(t+\ell_p+\ell_c+|B|\) 无多项式 kernel（除非 \(NP\subseteq coNP/poly\)）。它改进的是兼容图上的组合优化理论，不是临床试验或全国登记系统的匹配策略评估。

## 方法与证据

- 输入为有向 compatibility graph：普通顶点是 patient-donor pair，\(B\) 是 altruistic donors；可选顶点不交的交换 cycle 或由 altruistic donor 起始的 chain，受最大 path/cycle 长度 \(\ell_p,\ell_c\) 限制，目标至少让 \(t\) 位患者获得肾脏（§1、§2）。
- Theorem 1 将 color coding（用 \(t\)-perfect hash family 去随机化）和 subset DP 结合。对着色图先检测指定颜色集合的 colorful cycles/altruistic paths，再以颜色子集 DP 拼接顶点不交组件；有色图决策时间为 \(O^*(4^t)\)，hash-family 开销导出确定性 \(O^*((4e)^t)\)（§3）。\(O^*\) 隐去输入规模的多项式项，指数改善不代表对任意大 \(t\) 实例高效。
- 作者对比既有 randomized \(O^*(4^t)\) 与 deterministic \(O^*(14^t)\)；新界约为 \(10.88^t\)。这是确定性算法的渐近上界，论文未报告真实 compatibility graph 的 runtime、memory、匹配数量或 benchmark（§1.1、§3）。
- Theorem 2 从 Directed \(k\)-Path 作参数保持归约，表明若 \(NP\nsubseteq coNP/poly\)，对 \(t+\ell_p+\ell_c+|B|\) 不存在 polynomial kernel 或 compression。该结论是条件性复杂度下界，不能排除在临床数据分布上有效的预处理启发式（§4）。
- Theorems 3--4 从 unary Bin Packing 的 W[1]-hardness 给出：按无向 pathwidth 参数即使图是 DAG（\(\ell_c=0\)）仍 W[1]-hard；即使没有 altruistic donor（\(\ell_p=0\)）亦然。与已有 treewidth+\(\ell_p+\ell_c\) FPT 结果合起来，区分单独/部分参数和三者合用的可解边界（§5）。
- Theorem 5 进一步给出在 DAG、固定常数最大 path length 下仍 NP-hard，故对 \(DFVS+\ell_p+\ell_c\) para-NP-hard（Corollary 1）。证明经 Fixed-Size-3-Partition 构造；它强调某些看似限制结构不足以使问题固定参数可解（§6）。

## 适用边界与复现

- 适用于研究或清算引擎的算法选择、参数化分析和预处理设计，尤其当目标解中受助患者数较小且需要确定性最优性保证时。
- 不应将算法复杂度直接转化为病人福利、等待时间、移植成功率或公平性结论。真实登记还取决于血型/HLA 兼容性、交叉配型失败、链中断、地域/手术容量、权重、隐私和分配政策，均非本文模型变量。
- 复现应实现 compatibility graph、\(B,t,\ell_p,\ell_c\)、perfect-hash derandomization、colorful path/cycle detector、subset DP 和各归约；用小图穷举校验正确性，分别记录 \(t\) 的指数增长、hash-family 大小、内存与输入图规模的多项式项。
- 若进入医疗清算流程，须与经过验证的 IP/branch-and-price 模型和历史登记数据比对，并由临床、伦理和监管主体审核优先级/公平约束、撤回与失败风险；理论算法仅可作为候选组件。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的机制/资源分配中的参数化算法与复杂性论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VKIC3106.pdf) 核验 Theorems 1--5、Corollary 1、颜色编码 DP 和各参数含义；没有将条件性下界或运行时间上界误表述为已证实的临床匹配改进。
