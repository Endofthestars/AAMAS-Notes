---
title: "On the Semantics of Primary Cause in Hybrid Dynamic Domains"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "safety_verification", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/UETG8421"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UETG8421.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "formal_model_scope", "primitive_temporal_fluents_only", "linear_executable_scenarios", "causal_explanation_not_blame"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# On the Semantics of Primary Cause in Hybrid Dynamic Domains

## 一句话总结

本文为同时有离散 action 与连续时间演化的 Hybrid Temporal Situation Calculus（HTSC）定义 primary cause：找出使 temporal fluent 的相关 context 最后被启用、从而达成并持续 effect 的直接贡献 action；再通过移除该 cause 及其被抢占的潜在贡献者的“defused”反事实场景，给出修正的 but-for 验证。结论是受严格逻辑模型前提约束的因果解释，不是从观测数据学习原因或自动归责。

## 方法与证据

- 因果 setting 为 \(\langle D,\varphi,s\rangle\)：basic action theory、观察 effect 与可执行的线性 action history；文中处理 effect 原先为 false、执行后为 true 的情形（§2）。HTSC 在 situation calculus 的 successor-state axioms 外加入 action/situation time 与 state evolution axioms，使 temporal fluents 连续变化；并假设 contexts mutually exclusive。
- 查询只针对 primitive temporal fluents 的条件（如 temperature\((P)>1000\)），且为简化而相对 situation start time 提问（§2）。复合 effect、离散+时间 fluents 的任意组合、并发/分支历史、部分观测、随机噪声、因果发现及真实连续控制均不在本 extended abstract 的范围。
- temporal effect 可在相关 action 后延迟实现。作者先找 achievement situation \(s_\varphi\) 及其中最后启用的 active context；由于 contexts 互斥，直接启用它的最后 action 是唯一的 direct cause。新的 primary cause 被定义为：在 achievement situation 中、其 contribution 后 effect 达成并持续至 scenario 末尾的 direct actual contributor（§2–3）。论文声称此定义与先前定义等价，但完整形式化在外部版本 [22]。
- 普通 but-for 在 preemption 下失败：移除 actual cause 后，随后原本被抢占的 action 仍可使 effect 发生。方法在删除 cause 的 counterfactual scenario 中归纳识别 preempted contributors，并在 defused situation 中以 noOp 替换 cause 与这些 contributors（§3）；它声称若存在 primary cause 则 defused scenario 唯一，且若所有 contexts 初始 inactive、defused history 可执行，则 effect 消失。
- 这些是条件性理论性质。文中也指出 hybrid domains 可能无 primary cause，例如 achievement context 初始已启用；modified but-for 也可能因 counterfactual 不可执行而不能给出“effect 消失”。没有实验、case study、benchmark、model-checking implementation、complexity 或对人类因果判断的定量验证。

## 适用边界与复现

- 适合为已显式编码 dynamics 的混合规划/控制模型生成形式化因果追溯，特别是需要处理连续 fluent 延迟与 preemption 时；不宜把它直接作为事故调查、医疗/法律责任、自治系统问责或根因分析的唯一依据。
- 复现须给出 HTSC BAT、action timestamps、initial contexts、successor/state-evolution axioms、完整 executable scenario、目标 primitive fluent 与 query time。计算 achievement situation、active context、direct possible/actual contributors，再递归构造移除 cause 的 counterfactual、识别 preempted contributors 并 noOp 化，检验 defused executability/effect；须以 arXiv:2602.14994 补齐本文省略的 definitions/proofs。
- 应测试初始 context 已激活、多个接近阈值的连续 evolution、action timing perturbation、context 非互斥、compound/discrete effects、并发与不完全 history、model mis-specification、噪声传感器和极长 trace。报告 no-cause、non-executable defused scenario 与多种 plausible model 的比例，避免只列成功解释。
- 若将解释展示给操作员或用于纠正/处罚，应提供 action/context assumptions、反事实修改、被移除的 preempted events 和无结论情形；区分“模型内反事实贡献”与意图、控制权、预见性、政策责任。应支持人类复核、证据保留与对模型遗漏/偏差的申诉。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的因果推理与混合动态系统 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UETG8421.pdf) 核验 HTSC/primitive-temporal 限定、achievement context、contribution-based primary cause、defused counterfactual 及其 four 条性质；没有把模型内的 modified but-for 性质写成一般因果发现、实际根因确定或道德法律归责。
