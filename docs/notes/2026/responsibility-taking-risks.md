---
title: "Reasoning About Responsibility for Taking Risks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "norms_trust_governance", "safety_verification"]
dblp_key: ""
doi: "10.65109/OAJK8159"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OAJK8159.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["normative_definition_choice", "finite_probability_grid", "model_completeness_assumption", "epistemic_assumption", "not_legal_attribution", "single_predecessor_history", "fixed_temporal_depth"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Reasoning About Responsibility for Taking Risks

## 一句话总结

本文提出一个把 probability、行动能力、knowledge 和过去时间结合的多 agent modal logic，用于在伤害尚未发生时推理“未选最安全选项”“超过风险阈值”或“增加风险”的群体责任。对其有限、tree-like model class，作者给出 sound/complete axiomatization、可判定 satisfiability 和 \(O(|M|\cdot|\varphi|)\) model checking。它使特定风险责任定义可形式化和审计，但不决定真实因果、证据充分性、道德责备或法律责任。

## 方法与证据

- model 是有限 Epistemic Concurrent Game Structure：有限 agents/actions/states、每 agent 的 S5-like epistemic equivalence、nondeterministic transition、final deadlocks 和 state-associated probability measure（Def. 1, §3）。每个 state 至多一个 predecessor，故历史是 linear past、未来分支；作者称可视为 stochastic game 的有限深度 unfolding，不能直接覆盖一般循环/多前驱过程。
- probability 与行动的关联是 backward-looking：在 action 后 state \(s\)，\(P(s)\) 给同一前一 action profile 的可能结果之间的概率；这不同于 stochastic game 常见的 forward transition probability（§3）。将日志、预测风险或因果模型映射到该语义需要额外的建模与校准，不由逻辑自动完成。
- language 有 \(Pr(\varphi)\ge\alpha\)、\([\delta_G]\varphi\)、Yesterday \(Y\varphi\)、knowledge \(K_i\varphi\) 和 Boolean connectives（Def. 2–3）。\([\delta_G]\) 是 group action profile 在所有外部补全下的结果，\(E_G\) 表示每名成员知道；因此责任结论取决于可用 actions、观察等价类、outcome labels 和 coalition minimality 的完整且可信编码。
- 传统 counterfactual responsibility 需 harmful outcome 已发生、group 曾能并知道如何防止、且 group minimal。作者指出这会遗漏“发生概率很高但未发生”的风险情形，并在医疗 treatment/self-driving toy examples 中说明不同责任准则可给不同判断（§1–2, §4）。这些例子说明概念选择，不是对医疗或自动驾驶的经验/法律验证。
- 文中可表达 threshold responsibility \(Resp_G(\varphi,\alpha)\)：当前风险高于 \(\alpha\)，前一步 group 有知情 uniform strategy 让风险不高于阈值且自身最小；也给出 \(Resp_G^{min}\)（未将风险降至最小）和 \(Resp_G^{\uparrow}\)（使风险高于前一步）的定义（§4）。阈值、最小化和“任何增风险均不可接受”是规范性选择，需由领域治理决定，不能从概率事实本身推出。
- 为表达跨 state 的 probability comparison，模型将可取概率限制为有限有理集合 \(F\subseteq[0,1]\)（含 0/1）；量词由有限析取替代（§3, §6）。这有利于可判定性，却可能粗化连续风险、置信区间和概率估计误差；论文说明该限制源于表达/axiomatization 的挑战。
- Theorem 1 证明此 class 上 \(\models\varphi\) iff \(\vdash\varphi\)；Prop. 4 给 decidable satisfiability。作者还说明 \(Pr\)、action、past、knowledge 子式检查均为 \(O(|M|)\)，整体 model checking 为 \(O(|M|\cdot|\varphi|)\)（§5–6）。这些是已给 model 的逻辑计算界，非从现实证据自动推断责任的准确率或可扩展生产系统性能。
- 当前语言可用嵌套 \(Y\) 表达 fixed-depth 多步情形，但不能表达不固定深度的“eventually in past”；更强 PATL-style temporal/strategic extension 被留作未来工作（§4, §6）。

## 适用边界与复现

- 适用于为已明确的安全/治理协议编写可审计风险责任规范：先定义 adverse event、可行动作、信息可见性、概率来源、时间深度、可接受阈值与最小 group，再执行 model checking。
- 不应用于自动裁定个人过错、惩罚、保险、信用、招聘或事故法律责任。此类结论还需要适用法、正当程序、证据链、数据质量/不确定性评估、反事实因果分析、人的解释和申诉；形式满足某一公式不等于道德或法律上应归责。
- 复现应实现 Def. 1 的 P1–P5/C1–C2 与单 predecessor 约束，解释 \(Pr\)、\([\delta_G]\)、\(Y\)、\(K_i\)，在文中两个 toy model 检验三种 \(Resp\) 公式，再对 axioms/closure/canonical construction 验证 completeness 思路和 model-checker 复杂度。
- 实践扩展应支持概率区间与 calibration、连续风险、循环和长期轨迹、部分日志、因果/干预模型、多层组织责任、容错阈值与 human review；任何归因输出都应连同定义版本、输入证据和不确定性保存。

## 与 AAMAS 的关系与核验说明

这是 AAMAS formal reasoning、responsibility 与安全治理研究。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OAJK8159.pdf) 核验了 ECGS-style model、风险责任公式、有限 \(F\)、complete axiomatization、decidable satisfiability、\(O(|M||\varphi|)\) checking 和语义限制；没有把该形式框架写成法律归责、临床判责或现实因果证明。
