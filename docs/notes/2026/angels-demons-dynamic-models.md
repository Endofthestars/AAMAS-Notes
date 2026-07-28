---
title: "On Angels and Demons: Strategic (De)Construction of Dynamic Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "safety_verification", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/XEZZ1033"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XEZZ1033.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["permanent_graph_modification", "complexity_upper_bound_only", "memoryless_strategy_scope", "formal_model_not_deployment_assurance"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# On Angels and Demons: Strategic (De)Construction of Dynamic Models

## 一句话总结

本文在带成本有向图上提出三种永久修改模型结构的战略时序逻辑：恶魔删边的 SDL、天使加边的 SCL、两者并发的 SUL；它们均严格强于 CTL，SUL 严格涵盖前两者，模型检查对 SDL/SCL 为 PSPACE-complete，而完整 SUL 只证明属于 EXPSPACE。

## 方法与证据

- 模型是带 serial transition relation 与边成本的图；恶魔在预算内永久删除边，天使在预算内添加原先不存在的边，traveller 随后沿修改后的图移动。SUL 将二者的选择并发组合，可表达合作或对抗（§1--2）。
- 三种语义都量化修改者的策略，使目标对 traveller 的任意后续移动成立。与 Obstruction Logic (OL) 的关键差异是：OL 的禁用边在 traveller 一步后恢复，SDL/SCL/SUL 的更新会保留（§1、§3--4）。
- Theorem 1 给出 CTL ≺ SDL、CTL ≺ SCL、CTL ≺ SUL；Theorem 2 给出 SDL 与 SCL 表达力不可比，且各自都严格弱于 SUL。论文还展示 SCL 严格强于 OL、SDL 严格弱于 OL；部分与 OL/SUL 的关系仍是开放问题（§3）。
- 通过 QBF reduction 和交替算法，SDL model checking 为 PSPACE-complete（Theorem 5）；SCL 同样 PSPACE-complete（Theorem 6）。SUL 的 next-time fragment 是 PSPACE-complete，但完整 SUL 在 EXPSPACE（Theorem 7）。
- 完整 SUL 的上界来自可产生指数多个 graph updates 的计算树；论文没有声称 EXPSPACE-completeness。作者也指出现有定义为 memoryless strategy，并把 perfect-recall、satisfiability 及其他动态逻辑扩展列为未来工作（§4、§6）。

## 适用边界与复现

- 这是一种形式图模型语义；“删除/添加边”可以抽象 access control、路由或防御动作，但不等于网络、交通或安全关键系统已得到真实部署保证。
- 删除/添加的永久性是复杂度与表达力差异的核心前提；若实现要在一步后恢复边，应使用不同语义（如论文对比的 OL），不能把 SDL 结果直接移植。
- 结论针对有限、带成本且 transition serial 的模型与 memoryless 修改策略；不覆盖部分可观测、执行失败、动态成本、资源耗尽或 perfect recall。
- 复现应固定图、边成本、budget、目标公式、更新持久性与 strategy class；分别检查 QBF encoding、SDL/SCL PSPACE case、SUL next-time case，并报告完整 SUL 仅为已证 EXPSPACE 上界。

## 与 AAMAS 的关系与核验说明

这是多智能体战略推理与动态模型验证工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XEZZ1033.pdf) 核对操作语义、Theorems 1--2、5--7 和 §6 的开放问题；没有把抽象图上的安全/访问控制例子表述成现实系统认证。
