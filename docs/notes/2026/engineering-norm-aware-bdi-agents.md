---
title: "Engineering Norm-aware BDI Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/SEJS3352"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SEJS3352.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "norm_aware_bdi", "goal_plan_tree_transformation", "jason_implementation", "running_example_evaluation", "not_legal_compliance_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Engineering Norm-aware BDI Agents

## 一句话总结

本文提出不修改既有 BDI platform 的 norm-aware engineering 方法：把每条 ADICO-like norm 转为 Goal-Plan Tree（GPT），在原 GPT 的潜在 compliance point 加 link，并赋予 comply/violate consequences 的 valuings，供 meta-reasoning 选择。Jason 实现的公共交通购票示例展示 agent 可添加步骤以合规、明知违反或因后果改变 plan selection。它是一个设计/实现 pattern，并非对法律合规、规范完整性、偏好正确性、冲突规范解析或实际系统运行时成本的保证。

## 方法与证据

- example 中 agent 的 Go To Work 可 walk/rideshare/drive/use public transport；PT 有“passenger must have valid ticket，否则 fine”的 norm。作者关注三种能力：为合规而加 buy-ticket step、权衡后明知违反、在 original plan choice 中计入合规成本/违反后果（§1）。能表示 fine/reputation 等 valuing 不代表这些后果在现实中合法、准确或可比较。
- 流程为：（1）每个 \(N_i\) 按 Figure 2 pattern 翻为 GPT \(G_{N_i}\)；（2）将 original GPT \(G\) 与可能需补充 steps 的点连接；（3）为 \(G\) 与 \(G_{N_i}\) 添加 valuings。must/must-not 各有 Violate、Conform、N/A branches，context condition 确定 applicability（§2）。norm formalization、link placement、valuing与 preference ordering仍需工程师正确提供。
- agent 再以 meta-reasoning、valuings 和 preference 选择 plans。摘要没有定义统一 optimization、冲突/优先级/时限、跨 norm interaction、uncertainty、动态法律变化或 adversarial belief updates 的完整解决方案；“can violate”是 deliberation option，不是获准违反的规范/法律判断。
- 运行例已在 Jason fully implemented，使用 meta-events 实现 \(G\to G_{N_i}\) link，将 valuings 译为 beliefs，加入 agent preferences/meta-reasoning；作者称对 Jason-specific features 有 generic alternative（§3）。评估仅展示三个 cases、适应 norm applicability、添加 norms、多种满足方式、plan failure；没有规模 benchmark、unit/property tests、agent population、runtime/memory测量或用户/组织 validation。
- Table 1 将相关 approaches 按 add steps、violate norm、select plan、off-the-shelf BDI 比较，本文列四项全支持。该表是作者的特征定位，并不替代对实现覆盖、平台兼容性、工程代价或 safety/security 的独立评测；future work 明列自动 code/link generation、dynamic norms和 runtime-overhead assessment。

## 适用边界与复现

- 适合在可审查的 BDI/GPT system 中显式编码组织/模拟规范；不要把它用作法律或监管 compliance engine。实际公共服务、金融、医疗或机器人系统须由合格人员确认规范来源、适用范围、冲突优先级、权限与责任，并保留人工 override/appeal/audit。
- 复现应提供 ADICO norm schemas、GPT source、link annotations、context beliefs、valuing scale、preferences/meta-reasoning rules、Jason version/meta-event implementation和 generic alternative；对 conform/violate/N/A、applicability changes、new/contradictory norms、plan failures与 belief errors 写可执行 tests，并记录 selected plan、reasons、payments/penalties和 trace。
- 应评估多 norm/conflict/priority、temporal obligations、dynamic add/remove、large GPTs/many agents、uncertain sensing、malicious norms/beliefs、concurrent plan changes和 runtime overhead。部署还需 policy change management、provenance、access control、impact review和 independent verification；可解释的 plan choice不等同于合规或无害。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 norm-aware BDI engineering 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SEJS3352.pdf) 核验 GPT transformation、three cases、Jason implementation、Table 1 与 future-work gaps；没有将示例的规范推理改写为现实法律合规或通用平台支持结论。
