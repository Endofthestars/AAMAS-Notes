---
title: "Rejecting Arguments Based on Doubt in Structured Bipolar Argumentation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "norms_trust_governance", "agent_engineering"]
dblp_key: ""
doi: "10.65109/WZOU6484"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WZOU6484.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["formal_semantics_not_truth_verification", "doubt_representation_subjectivity", "framework_encoding_dependence", "no_empirical_human_validation", "support_attack_specification", "computational_complexity_not_established"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Rejecting Arguments Based on Doubt in Structured Bipolar Argumentation

## 一句话总结

本文提出 structured bipolar argumentation framework（SBAF）及 coherent/adequate semantics：agent 可因某 premise 或推理缺乏支持而保留怀疑、拒绝一个即使在 Dung complete semantics 下被防御的论证，同时还能以可接受的 sentence set 而非只以 argument set 表示立场。它刻画的是给定 encoding 下的规范性语义选择，既不判定论证的真实与否，也没有证明人类会如此推理或该机制能防止错误信息。

## 方法与证据

- SBAF 使用 language \(\langle L,\;\text{incompatibility},\;naming\rangle\)：argument 是 premises 与 conclusion 的 tuple；incompatibility 表示句子冲突，naming 使“从这些 premises 推出 conclusion”的推理声明本身可被句子谈论和 undercut（§3.1）。attack 由 conclusion 与另一论证的句子不相容而来，support 则表达接受某些 conclusion/premises 会承诺接受另一论证（Def. 3–5）。
- 该建模不假定一般逻辑 consequence relation；语言、冲突、argument 名称、attack 和 support 都由框架提供（§3.1）。所以结果高度依赖谁把何种怀疑、反驳、证据关系编码进框架；遗漏来源可靠性、证据强度或语义歧义不会由 semantics 自动补回。
- 在 argument level，strongly/weakly coherent extensions 从 admissible 出发但施加不同的 support/doubt 条件（Def. 7）；strong coherence 蕴含 weak coherence（Obs. 1）。相对于 complete semantics，它们不强迫接纳所有 defended arguments；相对于纯 admissibility，又保留了 support 的作用（§3.2）。这是对“可理性地怀疑”的形式化许可，不是对怀疑是否合理的外部证据检验。
- weak coherence 满足 directionality，而 strong coherence 不满足（Prop. 2）；因而两者面对不相关新增论证的行为不同。选择其中任一语义是建模价值取舍，不能把某一结果宣称为唯一正确的 debate outcome。
- 在 sentence level，作者定义 strong/weak argument set、characteristic function、initial set 和 strongly/weakly adequate language extensions（Def. 8–11）。这些让输出可写成接纳哪些单独 claims；但 sentence compatibility、argument closure 和可推断内容仍全部取决于原始 SBAF。
- 对 saturated SBAF，strong/weak adequate language extensions 与相应 coherent argument extensions 双向对应（Props. 6–7）；加入 confident（极大）版本后，作者讨论与 Dung preferred semantics 的关联（§4.1）。文中还指出在 strongly saturated 情况下，confident weak coherence 可与 preferred extensions 对应，从而 support 可能变得冗余；这不是任意 SBAF 的完全等价。
- 对 deductive support semantics，满足指定条件时 strong coherence 与 d-admissibility 互相推出（Prop. 12），据此将该既有语义作为其框架特殊情形/推广（§4.2）。定理是结构关系，不给出 argument acceptance 的复杂度界、可扩展实现或真实对话实验。
- 论文以小提琴来源/所有权的示例说明：可接受“Clara 作出某声称”而暂不接受该所有权结论，也可因 Alex 来源可疑拒绝一个被防御的 argument（§1, Ex. 1–2）。例子展示表达力，不是用户研究、标注基准或事实准确率评估。

## 适用边界与复现

- 适用于需要显式区分 claim、inference claim、support 与 attack，并允许保留判断的解释型多 agent reasoning/argumentation 原型。部署到医疗、法律、金融、内容治理或安全决策时，必须将它作为辅助表达层，不能把 extension 当作事实裁定或自动拒绝依据。
- 高影响使用应记录论证来源、证据等级、编码规则、怀疑的提出者与理由、语义版本和每一步 extension；提供人工复核、异议/申诉、来源核验、偏差审计与不确定性提示。允许 doubt 也可能放大不信任或选择性拒证，需防止被用来任意排除不利论证。
- 复现需实现 language、incompatibility/naming、minimal arguments、attack/support、saturation，分别枚举 admissible、complete、strong/weak coherent 和 strong/weak adequate extensions；验证 Props. 1–12 的包含/对应关系，以及文中的 violin 示例和 d-admissibility 特例。应公开实例 encoding，因为没有它无法复核语义结论。
- 后续应研究 acceptance/verification complexity、增量计算、概率/证据强度、来源可信度、群体分歧、噪声与恶意输入，以及与人类论证判断的实证校准；这些均非本文所证明的保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS computational argumentation 的语义建模工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WZOU6484.pdf) 核对 SBAF 构成、coherent/adequate 语义、directionality、saturated 对应、preferred 与 deductive-support 的条件性关系，以及作者的示例和未覆盖范围；没有将形式可接受性写成真相判断、人类行为验证、证据可靠性或安全内容治理保证。
