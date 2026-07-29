---
title: "Leveraging Context-Oriented Programming to Implement Normative Rules in Autonomous Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "agent_engineering", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/BLFA6735"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BLFA6735.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02z"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "normative_rule_interpretation", "ros_design_schema", "runtime_context_correctness", "no_deployment_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Leveraging Context-Oriented Programming to Implement Normative Rules in Autonomous Systems

## 一句话总结

本文提出 CO-SLEEC，把 SLEEC 规范规则的触发、默认义务与按优先顺序覆盖的 hedge clauses，映射为 context-oriented programming（COP）的事件调用、基础方法实现和动态 layer；并给出 ROS Manager、Context Listener 与 COP Layer Manager 的实现架构。它提供的是将已形式化规则接入机器人运行时的设计/实现模式，不证明规则提取无误、运行时 context 判断正确，或真实机器人已获得伦理、安全或法律合规保证。

## 方法与证据

- SLEEC 规则形如 `WHEN C0 THEN O0 UNLESS C1 IN WHICH CASE O1 ...`。例如在请求打开窗帘时，默认打开；用户未着衣时拒绝并说明；用户高度焦虑时再覆盖为警告后打开。论文用这一例子说明上下文和有序例外会改变义务（§1）。
- CO-SLEEC 的映射是：rule trigger 对应触发方法调用的 event，default obligation 对应 base implementation，hedge clause 对应 COP layer，条件对应 runtime-context predicate，例外义务对应该 layer 绑定的方法实现；rule evaluation 对应 layer activation（Table 1、§2.1）。
- 运行时持续对上下文评估规则。对于一个有序 hedge-clause 序列，只有最后一个条件成立的 clause 生效，故每条规则至多有一个 active hedge clause；触发事件到来时，layered method dispatch 选择对应实现，没有活跃 layer 时走默认实现（§2.1）。
- ROS 方案由 Manager 桥接规则推理与机器人执行：Context Listener 监测条件/领域变化，Manager 解析并评估 SLEEC 规则，COP Layer Manager 激活相应 layers；受规则约束的 task ROS node 须实现 default 行为及多个 layer-bound variants（Figure 1、§2.2）。
- 摘要描述 reusable implementation schema，却未报告真实机器人部署、规则解析/上下文检测错误率、延迟/吞吐、冲突规则处理、形式化端到端验证或用户研究。因此不能从该设计推断某一规则集在实际环境中必然被正确执行。

## 适用边界与复现

- 适合已有 SLEEC 规则、能把义务落实为可切换任务实现、且可观测运行时上下文的 ROS 原型。规则的自然语言释义、传感器状态、事件定义和默认/例外的业务含义都必须由领域专家审计。
- 有序“最后成立的例外优先”只解决单条规则的 layer 选择；原文没有给出多条规则竞争同一 task、相互矛盾义务、多个 layers 的优先级或安全关键 fail-safe 的完整策略。部署时应另设冲突分析、权限控制、硬安全约束和人工升级路径。
- 复现应公开 SLEEC parser/evaluator、ROS message/interface、Context Listener、layer manager、任务节点和每个 rule-to-method/layer mapping；对例外嵌套、上下文抖动/过期、触发竞态、传感器误报、规则更新和节点故障做可追溯测试。
- 需把规范符合性与系统安全分开验证：用独立 oracle 检查每个 context 下的义务选择，再测 ROS 调度/执行是否实际完成动作；高风险机器人不应仅以动态方法分派作为安全或合规证据。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 ethical-aware autonomous systems 扩展摘要，连接规范多智能体系统、COP 与 ROS。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BLFA6735.pdf) 人工核对 SLEEC--COP mapping、最后适用例外的语义及 ROS 架构；未将实现模式夸大为实际伦理、安全或合规认证。
