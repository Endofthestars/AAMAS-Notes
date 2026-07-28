---
title: "Eliminating Inconsistencies among CP-Theory Qualitative Preferences"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "planning_scheduling", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/WOCS8295"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WOCS8295.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["preference_discard_governance", "qualitative_preference_model_scope", "synthetic_evaluation", "optimization_tradeoff", "no_participant_consent_model", "computational_complexity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Eliminating Inconsistencies among CP-Theory Qualitative Preferences

## 一句话总结

本文处理聚合 CP-theory qualitative preferences 所诱导的 dominance graph 存在 cycle（即某 outcome 可优于自身）的情况：从原始 preference statements 中删一部分，使 set-labeled induced preference graph（SL-IPG）无环。MP 最小化删 statement 数，MD 最小化因删 statement 而失去的 dominance edges；两者 NP-complete。迭代 ILP 在合成 CP-net/CP-theory 上可行，但“删除得少”与“保留更多关系”通常冲突；算法修复的是形式一致性，不能决定应由谁让步、被删偏好是否错误、利益冲突是否获得正当处理。

## 方法与证据

- CP-theory statement 可写为条件下某 variable value 胜过另一 value，并指定无关变量；一组 statement 诱导 outcomes 间 dominance relation/IPG（§2）。若 IPG 有 directed cycle，某 outcome 经偏好链支配自身，形式上不一致。该语义依赖变量、条件、ceteris-paribus/relative-importance encoding，不涵盖偏好强度、概率、不确定性、权利或谈判权力。
- 直接做 minimum feedback arc set 不够：一个 statement 可诱导多条 edges，一条 edge 又可由多个 statements 共同诱导；任意删 IPG edge 后未必对应原 statement 的合法子集（§1, §3）。作者定义 SL-IPG \(G=(V,E,A,L)\)，label map 将每条 dominance edge 映到诱导它的 preference set（Def. 1）。
- MP\(_G\) 寻找令 resulting SL-IPG acyclic 的最小 discarded preference set；MD\(_G\) 则寻找移除后损失 dominance edges 最少的 statement set（§3–4）。例中 MP 可有 \(\{p_3,p_5\}\) 与 \(\{p_4,p_5\}\) 两个解，而因 \(p_4\) 诱导更多 edges，MD 选择前者（Ex. 2）。两目标分别编码“让多少声明让步”和“语义图改动多大”，都不是个人负担、伤害或公平补偿的度量。
- 作者证明 MP 和 MD decision versions NP-complete（§4），并给精确 ILP：对发现的每个 cycle 加至少破坏一条边/其诱导 statements 的约束；MD 另以 edge removal variable 建目标（§5.1–5.2）。复杂性表示大实例可能难解，且 IPG outcomes/循环数量可指数增长。
- E-Algo 采用 lazy iterative ILP：DFS 找当前 cycles、用当前 cycle constraints 解 ILP、在删后的图继续找新 cycles，直到 acyclic（Alg. 1, §5.3）；Theorem 1 证明对 MP 或 MD encoding 输出精确解。它避免一次枚举所有 cycles，但未承诺固定 runtime/内存上界，也依赖 IPG/edge-label 构造和 ILP solver 正确性。
- 实验从既有方法合成 CP-net/CP-theory：binary variables、变量数 3–9、随机相关变量与 preferences，使用 Gurobi/ILP 实现（§6.1）。因此验证的是该生成分布与小/中表达规模，并非来自真实群体的冲突偏好、自然语言规范或真实政策协商。
- 结果显示 MP-only 解往往牺牲 MD，MD solution 平均比 MP 多删约 1.61 倍 preferences（CP-nets）；作者比较先 MP 后 MD 或反序的 lexicographic strategies，并称“先最小删 preference”在两目标间经验上平衡较好（§6.2–6.3）。这是 aggregate synthetic statistics，不能建立普遍的伦理优先顺序或保证每个 instance 的低失真。
- 论文也比较 MFAS ILP，指出其可能在不对应合法 preference subset 的意义上失效且运行代价高；文末提到进一步扩展/启发式工作（§6–7）。未讨论 agents 对删改的 consent、拒绝、策略性表达、隐私、compensation 或二次验证。

## 适用边界与复现

- 适用于已由专家/参与方审计过的 CP-theory preference base 中，诊断并提出候选最小形式 repair。每个候选删集应回交 statement author 或合法决策者解释/确认，不能由 solver 自动视为“错误偏好”。
- 在医疗、规划、产品、环境和公共政策等高影响场景，删除某群体条件偏好可造成系统性排除。须设置不可删除的权利/安全约束、provenance、理由与影响披露、群体/个体损害审查、申诉与复核、隐私保护和版本化审计；一致的 IPG 不等于正当聚合。
- 复现需固定 CP-theory grammar/semantics、outcome enumeration、SL-IPG labels、MP/MD cost、DFS cycle finder、ILP variables/constraints、solver version/time limit和 synthetic generator seeds/3–9 variable settings。报告 optimality gap、cycles/iterations、删 statements/edges、每 statement 的诱导范围及两种 lexicographic ordering。
- 应评估真实偏好数据、weighted/agent-specific deletion costs、statement confidence/uncertainty、incremental updates、larger sparse domains、approximation/parameterized algorithms、strategyproof elicitation以及人类对 repair explanation/acceptance；这些不是现有实验覆盖的保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS qualitative preference reasoning 的 inconsistency-repair 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WOCS8295.pdf) 核对 CP-theory/IPG/SL-IPG、MP/MD 目标、NP-completeness、iterative ILP/E-Algo、合成 CP-net/CP-theory 实验、MP–MD trade-off和 lexicographic 策略；没有把图无环、最少删除或实验可行性误写为偏好真伪判定、群体同意、伦理公平或现实冲突解决保证。
