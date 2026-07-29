---
title: "Decisions.jl: Representing and Transforming Decision Problem Classes in Julia"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "marl_coordination"]
dblp_key: ""
doi: "10.65109/XRMX3337"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XRMX3337.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "low"
risk_tags: ["model_aware_scope", "not_solver_library", "ddn_representability_requirement", "transformation_semantics_require_validation", "julia_ecosystem_dependency", "case_studies_not_benchmarks", "opponent_model_assumption"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Decisions.jl: Representing and Transforming Decision Problem Classes in Julia

## 一句话总结

Decisions.jl 是一个 Julia 的 model-aware sequential decision modelling ecosystem：显式表示底层 dynamic decision network（DDN），以节点、时间链接、tensor plate 及采样依赖描述从 MDP/POMDP 到多 agent/连续/约束等问题类；再用可组合 transformation 在问题类间增加、删除或重解释结构。论文用 Gridworld 的 MDP→POMG→belief-MDP 和 Markov game 的 fictitious play 展示表达/原型能力，但不是 solver 库，也没有给出统一算法速度或求解质量 benchmark。

## 方法与证据

- 一个 decision network 包含带条件分布的 chance、decision 与 outcome 节点；DDN 以 temporal mapping 把当前与下个时步节点连接。problem instance 再附加目标与目标参数；problem class 固定网络结构/时间映射/目标，而允许分布与参数变化（§2.1--§2.2）。
- 除图本身外，框架保留随机变量标签、带 joint/independent 标记的任意维 plate、以及 plate 边的 parallel/dense 关系；因此能将动作、记忆、观测、奖励按 agent 轴展开或保持耦合（§2.1）。这是多 agent 表示的核心，不等同于已提供所有多 agent solver。
- 标准 Markov family 显式命名 state/successor、memory/successor memory、action、reward、observation、sojourn-time 等节点，覆盖 MDP、POMDP、Markov game 等；也可表示没有惯用名称的组合类及 normal-form game（§2.3）。能否使用仍要求问题可表为 DDN。
- transformation 是 \(T:Q_{in}\to Q_{out}\)，保证同一输入问题类的实例仍映射到同一输出类。Insert、InsertDynamic、Implement、Recondition、AddAxis、WithIndep、IndexExplode、MergeForward、Rename 等操作可改变假设；输出可更简单、更复杂或等价，且两类之间可有多条路径（§3.1）。因此转换后模型语义、近似和 solver 前提需要用户审计。
- Gridworld case study 用一串 transformation：在 MDP 中插入 observation/memory 与时间链接、设 observation distribution、按 agent 轴复制并设局部条件独立，得到 POMG；再把 opponent policy/belief update 实现为分布、合并进状态并构造 belief update，把 POMG 转为 belief MDP 供 MDP solver 使用（§3.2）。后一步明确假设 opponent 行为，不能把它理解为无假设的 POMG 精确求解。
- 另一个 case study 把 two-player Markov game 的 action/reward 分裂，循环中令对手 action 等于历史 policy 的 empirical average，merge 成 ego MDP，调用 MDP solver，表达 fictitious play（§3.3）。论文借此说明算法可写为变换序列，而不是声称 fictitious play 新颖或保证收敛。
- 作者说明该系统主要面向 model-aware setting，既不是环境集合也不是 solver library，只带少量 prototyping domain/algorithm；Julia JIT 的目标是提供高性能 interface（§1）。会议稿展示 architecture 与案例，未报告跨框架 runtime、内存、scaling 或 solution-quality benchmark。

## 适用边界与复现

- 适用于研究者要快速比较/原型化多个明确的 sequential decision formulation，特别是需要从单 agent 模型系统地加入部分可观测、多 agent、连续或自定义依赖时。
- 不适用于没有显式生成模型的纯 model-free RL 工作流，或把 transformation 当作自动保持最优性/信息结构的黑箱。任何 MergeForward、belief update、agent-axis independence 和 opponent-policy Implement 都是建模决定。
- 复现应固定 Julia、Decisions.jl 与 solver 的版本，先重建论文 Gridworld DDN，再逐条执行表 1/表 2 transformation；在每个中间类验证 node/edge、条件变量、plate 采样语义、rollout distribution 与 reward。fictitious-play 示例还应比对 policy 平均、best response 和不同初始策略。
- 采用前应为目标领域写 schema/unit tests、转换前后不变量、随机 rollout equivalence 或可接受的近似误差，并单独测量编译开销、稳态 throughput、内存和 solver 表现；框架表达性不能替代安全/性能验证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 agent engineering 与决策理论软件基础设施工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XRMX3337.pdf) 核验 §1--§3 的 DDN/问题类/transformations、两项 Gridworld 与 fictitious-play case study、以及结论中的定位；没有将框架设计主张误报为实证 solver 基准或通用算法保证。
