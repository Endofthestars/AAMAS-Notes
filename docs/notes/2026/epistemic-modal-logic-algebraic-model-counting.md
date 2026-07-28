---
title: "Epistemic Modal Logic Meets Algebraic Model Counting"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MSKZ1140.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["propositional_only_knowing_scope", "constant_query_complexity", "knowledge_compilation_dependency", "single_agent_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Epistemic Modal Logic Meets Algebraic Model Counting

## 一句话总结

论文将 propositional only-knowing（OL）的特定认识蕴涵、概率 only-believing（OBL）及有限动态扩展归约为 algebraic model counting（AMC）；可复用 semiring 和知识编译工具，但计数并未让一般认识推理变成多项式时间。

## 方法与证据

- AMC 以 propositional theory、literal-to-semiring labeling 和 models 的加/乘聚合统一 SAT、#SAT、weighted/probabilistic counting。论文定义 $\lVert\phi\rVert^A_\Sigma$ operator，将 $O\Sigma\models\phi$ 的 only-knowing 查询转为一系列 AMC tasks（§2–3）。
- 对 constant-size queries，Corollary 3.6 给 OL epistemic reasoning 的时间界 $P^{NP[O(1)]}$；这是查询大小固定时的复杂度表达，非一般输入大小下 tractability，也不取消 OL 的既有 $\Sigma^P_2$-complete 推理难度（§3）。
- 对 propositional OBL 的概率知识库，literal weights 形成 AMC/WMC；Corollary 4.7 对 constant-size queries 给 $P^{\#P[O(1)]}$。概率计数本身通常 #P-hard，收益来自可用编译 circuit 的重复评估，而编译可有指数离线代价（§4）。
- 论文还定义 AMC-based regression 处理特定 stochastic actions 的动态概率认识投影；其动态复杂度结论同样要求 action sequence 与 query 为常量大小。作者明确将扩展到 multi-agent setting 留作未来工作（§5–6）。

## 局限与复现

- 结果限定于 propositional only-knowing / 指定 OBL 语法与语义；不直接覆盖一般 K、S5、多 agent mutual/common knowledge、任意一阶量词推理或任意 belief update。
- AMC 归约正确不表示计数廉价：须给出 semiring、literal weights、编译语言与 circuit，并将 compilation cost、query size、action sequence 长度单独报告。
- 概率部分依赖规范化、可数可加分布及知识库权重约束；错误或相关 weights 不能直接套 literal-weighted counting。
- 复现应实现 operator、SAT/#SAT/WMC semiring 实例和 regression，验证静态/动态示例，并分别测量编译与重复查询成本。

## 与 AAMAS 的关系与核验说明

该文为知识型 agent 的符号认识推理接入模型计数和知识编译。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MSKZ1140.pdf) 核对 OL/OBL/dynamic 范围及 Corollaries 3.6、4.7；不将其限定片段外推为通用多 agent 认识逻辑高效求解。
