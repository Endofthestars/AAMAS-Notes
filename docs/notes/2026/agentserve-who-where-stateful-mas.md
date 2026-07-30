---
title: "AgentServe: Online Who–Where Adaptation for Open-World, Geo-Distributed Stateful Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["agent_engineering", "marl_coordination", "planning_scheduling", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/NWCW1919"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NWCW1919.pdf"
demo_url: "https://youtu.be/d56kDFyv8qA"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05p"
spark_draft_verdict: "needs_revision_for_decentralization_page_map_risk_and_distributed_guarantee_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_passive_discovery_page_map_risk_migration_consistency_failure_security_and_v2x_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["quantitative_evaluation_missing", "scalability_claim_not_benchmarked", "migration_downtime_unreported", "lost_duplicate_and_ordered_message_semantics_unreported", "directory_atomicity_and_consistency_unreported", "in_flight_message_handling_unreported", "split_brain_risk", "source_destination_and_replica_failure_unreported", "migration_rollback_unreported", "authentication_and_authorization_unreported", "state_privacy_unreported", "control_plane_overhead_unreported", "state_continuity_not_strong_consistency_guarantee", "v2x_not_field_validated"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_who_where_migration_directory_consistency_message_delivery_failure_rollback_security_scalability_and_v2x_boundary_check"
escalation_verdict: "needs_revision_corrected_for_decentralization_migration_consistency_failure_security_quantitative_evidence_and_v2x_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted migration-consistency and distributed-systems risk check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# AgentServe: Online Who–Where Adaptation for Open-World, Geo-Distributed Stateful Multi-Agent Systems

## 一句话总结

AgentServe 在 Ray 上把动态通信对象发现（Who）与跨异构 tier 的 placement/live migration（Where）做成可插拔控制层，并在三台服务器上展示 stateful agents 的 spawn、despawn 与迁移；短稿没有量化 scalability、迁移停顿或消息一致性，因此不能把连续行为演示解释为零停机、exactly-once 或 fault-tolerance 保证。

## 问题定位

论文针对 open-world、non-stationary、geo-distributed MAS：agents/workloads 会出现或消失，local context 与 objectives 会变化，执行跨 edge locations 与 regional clouds（pp. 4089–4090）。

它把在线适配拆成两个耦合问题：

- **Who**：locality 改变时，哪些 agents 应互相通信；
- **Where**：latency、bandwidth 与 server load 改变时，stateful agents 应运行在哪个 site/tier。

AgentServe 是 framework/demo，不是完整的 distributed-systems correctness proof，也没有提供 scalability、fault tolerance、strong consistency 或 physical V2X validation 的定量研究。

## System boundaries 与 agent runtime

AgentServe 作为 control layer 运行在 Ray execution substrate 上，并可选 Kubernetes 来抽象异构资源（p. 4090）。外部 clients/systems 通过 lifecycle API 根据事件或 workload changes spawn/despawn agents。

每个 long-running stateful agent 内置 runtime services：

- 在 directory 中 self-register，用于 name resolution；
- 向 discovery registry 发布 position、attributes 等 dynamic state；
- 使用 logical identifier 做 name-based communication；
- 支持 live migration 与 state transfer。

用户把普通 Python class 标记为 `@agent`；decorator 注入 communication、migration、self-registration 与 directory/discovery access。discovery 和 scheduling policy 通过 declarative YAML 选择，也可以替换为 custom policy。

## Who：Discovery 与动态图

Discovery 维护 published agent state registry，并对 on-demand queries 返回 neighbor set 或 edge map（p. 4090）。pluggable policy 依据最新 registered state 计算互动关系；论文以 spatial indexing 为例，把空间分成 grid/tiles 后返回 nearby candidates。

Discovery 被设计为 intentionally passive：

1. agents 主动 push state updates；
2. Discovery 在收到查询时响应。

作者据此声称它会随 agent population 扩展而不需要 central coordinator。三页稿没有 benchmark 该 claim；directory、registry 和 scheduler 仍是明确的平台组件，所以不能进一步写成 AgentServe 已实现完全去中心化或消除了所有 central control。

## Where：Placement 与 live migration

scheduler 读取 registry 与 derived edges，使用 pluggable policy 跨 heterogeneous tiers 做 placement，并在 load、fragmentation 或 coordination objective 变化时触发 migration（p. 4090）。

三类 operational goals 是：

- **consolidation**：减少 active tiers；
- **balance**：减少 hotspots；
- **locality**：co-locate frequently interacting agents，减少 cross-tier edges。

正文描述的 migration 顺序是：

1. scheduler 作出迁移决策；
2. 在 destination spawn replica；
3. agent 把 state transfer 到该 replica；
4. directory entry 更新，使 subsequent communication 指向 migrated instance。

因此迁移执行被作者称为 largely agent-driven，而 decision 仍来自 scheduler。name-based communication 降低了 application 手工维护 endpoints 的负担，但这段流程没有定义 directory update 的原子性、迁移窗口消息语义或故障恢复保证。

## Demonstration

demo 在三台远程服务器 A、B、C 上运行真实 stateful agents，并把三台机器表示为 heterogeneous tiers（p. 4090）：

- agents 使用 random walk；
- discovery 固定为 spatial-indexing policy，并随 proximity 更新 communication edges；
- `binpack` 对应 consolidation；
- `spread` 对应 load balancing；
- `friends` 利用 interaction locality 减少 cross-tier edges；
- agent population 通过 spawn/despawn 变化；
- migrations 使用 live state transfer。

论文说 demo 中 behavior remains continuous，并在结论中说 migration preserves state continuity。这是设计和演示层面的观察，没有配套 downtime 或 message-delivery measurement。

## 没有报告的定量证据

短稿没有给出：

- agent count 或 tested scale；
- latency、bandwidth、load 的范围或分布；
- migrated state size；
- migration downtime；
- lost、duplicate 或 reordered messages；
- throughput 与 control-plane overhead；
- directory/discovery query cost；
- 三种 policy 的 performance metrics；
- baseline、seed、run count、variance 或 confidence interval。

因此 “scales”“transparent communication”“state continuity” 与 “continuous behavior” 不能被外推为 zero downtime、exactly-once delivery、linearizability、optimal scheduling 或 fault tolerance。

## 一致性、故障与安全边界

三页稿没有说明：

- directory entry 与 replica state 是否原子切换，以及 consistency model；
- in-flight messages 如何 buffer、retry、deduplicate、order 或 route；
- source/destination/replica 在迁移中失败时如何处理；
- network partition 或 concurrent migration 下的 split brain；
- partial state transfer 的 rollback 与 recovery；
- directory、registry、scheduler 和 lifecycle API 的 authentication/authorization；
- published attributes 与 migrated state 的 confidentiality、integrity 与 tenant isolation。

这些缺口不表示系统一定错误，但意味着当前稿件不足以支撑高可用、强一致或安全生产部署的保证。

## V2X 与未来工作

V2X-style cooperative perception 在 Introduction 中是 representative example，不是已经完成的 physical deployment（p. 4089）。Conclusion and Future Work 明确把 V2X-like cooperative perception、其他 wide-area cyber-physical workloads，以及 decentralized discovery/scheduling 的 scalability/adaptivity improvement 放在未来。

## 资源与页码核验

论文提供 [demonstration video](https://youtu.be/d56kDFyv8qA)，但三页稿没有给出 code repository。

PDF 逐页核对：p. 4089 为 identity、Abstract、Introduction 与 Architecture 起始；p. 4090 为 Architecture continuation、Implementation、Demonstration、Conclusion and Future Work；p. 4091 为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NWCW1919.pdf) 核验；`reviewed` 表示系统机制、demo 范围和未报告边界已核对，不表示 scalability、strong consistency、fault tolerance 或 V2X deployment 已经验证。
