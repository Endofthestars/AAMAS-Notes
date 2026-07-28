---
title: "Peach: Program Each Agent and Communicate Howsoever"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/SAXY3841"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SAXY3841.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["operational_semantics_not_end_to_end_evaluation", "langshaw_protocol_assumptions", "adapter_implementation_maturity", "distributed_failure_and_security_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Peach: Program Each Agent and Communicate Howsoever

## 一句话总结

Peach 将 agent 的 communicative-action reasoning 与通信基础设施分离：程序面以 Langshaw protocol 表达社会动作，adapter 以配置映射到共享状态或去中心化消息；论文给出三种 adapter 的操作语义，但只声称已有 prototypes，未提供端到端性能、故障注入或安全评测。

## 方法与证据

- 每个 Peach agent 由 reasoner 和按 Langshaw protocol/基础设施配置的 adapter 构成；reasoner 面向动作意义编程，不直接依赖数据库、artifact 或点对点消息（§1、§4）。
- 同步部分定义 batched 与 instantaneous/shared-memory adapter；后者依赖底层 store 的原子事务或队列/共识来序列化 attempts。异步 adapter 把 Langshaw 编译为 BSPL，维护每 agent 的 local state，而非一个统一 social state（§5--6、图 7）。
- 文中通过 inference rules 描述 attempt、feasibility、sayso approval、forward/failure 等转换，并以 Purchase 协议示例解释；结论称已实现三种 adapter 的 prototypes，Python 工程与 Jason adapter 均为后续/实现方向（§3--7）。

## 局限与复现

- 不含 benchmark、吞吐/延迟、规模、互操作或真实部署实验；“切换基础设施不改 reasoning”是该语义/编程模型的设计目标，具体 adapter 仍须正确实现并适配对应系统。
- 同步实现把并发与故障语义交给数据库事务、队列或共识；异步实现依赖 BSPL 编译、local observation 与消息送达。网络分区、拜占庭/恶意 agent、认证、保密、持久化和重放攻击没有在本文建立安全保证。
- Langshaw protocol、roles、keys、sayso/冲突规则是前提；协议建模错误、不同 adapter 的时序差异或混合同步异步通信会改变可观察行为。应对每个协议和目标 adapter 单独验证 safety/liveness。
- 复现应获取原型及其版本，公开 Purchase 之外协议、配置、消息 trace、共享存储一致性、deadline/batching、BSPL 编译产物和故障测试；比较同一 reasoner 在三种 adapter 下的 trace equivalence、性能与恢复行为。

## 与 AAMAS 的关系与核验说明

该文面向协议驱动的多智能体软件工程与通信抽象。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SAXY3841.pdf) 核对 Peach/Langshaw、三类 adapter、BSPL 编译与 prototype 声明；未把操作语义或示例解释为分布式系统的实证可靠性或安全证明。
