---
title: "Better Goals, Better Policies: LLM-Driven Relabeling for Offline Goal-Conditioned Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "generative_agents", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/ENPN5664"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ENPN5664.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "offline_benchmark_only", "llm_rule_compilation_dependency", "td_error_proxy_assumption", "state_semantics_required"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Better Goals, Better Policies: LLM-Driven Relabeling for Offline Goal-Conditioned Reinforcement Learning

## 一句话总结

本文为 reward-free fixed dataset 的 offline goal-conditioned RL 提出 LLM‑Driven Relabeling：由 LLM 按 task description 给出语义 key-state rules，将规则编译为 deterministic discriminators，再优先将未来关键状态作为 hindsight goal；没有关键状态时回退标准 HER。作者在其假设下把更大的 expected TD error 关联到更小 GOAL‑BE dimension/样本复杂度，并在 OGBench 的 AntMaze-large 与 Cube-single-play 中、尤其 50% 数据时报告改进；这是依赖状态语义、规则正确性与 TD-error premise 的离线学习方法，不保证生成的 goal 可达、安全或适用于真实机器人。

## 方法与证据

- 标准 HER 均匀从未来 states 抽 goal；论文认为这常得到“easy/low-signal” goals，影响 value estimation（§1）。这种描述依赖任务、dataset coverage和representation；高 TD error 也可能来自 out-of-distribution、不可达或错误标注 goal，而不必然代表有用学习信号。
- 四步 framework（§2.1）：(1) task description prompt LLM 生成少量语义 rules（PointMaze 示例含 Turning Event、Terminal Stabilization、Stop-at-Checkpoint）；(2) 编译成对部分 state dimensions 的 deterministic discriminator；(3) future states若在 temporal window 内满足任一 rule则优先采样，否则 HER fallback；(4) 以原 offline GCRL routine 训练 policy/value。这样 LLM 调用被编译摊销，但 rule compilation、state-coordinate semantics、threshold/temporal window及task description都成为可信输入；文稿未报告 LLM model/prompt、rules、compile failure rate或跨任务的人工审查。
- reliability mechanism 包括 compile-time 检查 discriminator executability，和 relabel-time 以 agent TD error 为 proxy 监测 relabel quality并调整 selection（§2.1）。它并非形式化 verification：可执行 rule 不等于任务正确，TD error不等于safe/reachable/optimal goal；没有给自检算法、阈值、避免 reward hacking/feedback loop、LLM hallucinated constraints或安全约束。
- Theorem 2.1 在引自 [21] 的 \(\epsilon\)-independence 条件下，若 \(\mathbb E[\delta_\theta^{LLM}]\ge\mathbb E[\delta_\theta^{HER}]\)，则 \(dim_{GOAL-BE}^{LLM}\le dim_{GOAL-BE}^{HER}\)；Corollary 2.2 由有限样本 guarantees推到约 \(O(dim_{GOAL-BE}/\epsilon^2)\) relabeled samples（§2.2）。该为条件推导，非无条件“更大 TD error 一定更高 return”；论文 Fig.2 只在其 sparse-reward data 比较TD-error distributions支持 premise。
- 评估 OGBench 的 AntMaze-large navigation、Cube-single-play manipulation，比较 GCIVL、GCIQL、QRL、CRL、HIQL；reduced-data 只留 50% dataset、training steps固定 500,000（§3）。图 3 显示所述方法缓解 drop，但摘要/正文未给环境 score 数值/CI/seeds、full-data table、规则数/LLM费用、compute、ablation/self-check failure、OOD/safety或真实机器人实验，不能声称普适 sample-efficiency。

## 适用边界与复现

- 适用于已具有可解释连续 state dimensions、离线轨迹覆盖任务关键事件且可人工审查规则的研究型 offline GCRL；不应用于无人机、机械臂、车辆或生产流程直接生成/执行 goals，尤其当状态语义不完整、dataset含危险行为或goal必须满足硬约束。
- 复现需公开 OGBench revision/data splits、task descriptions、LLM/model version/prompt/temperature、所有 rules及人工修订、rule-to-code compiler/discriminators/state dimensions/thresholds/windows、compile/relabel checks、goal sampling/fallback probabilities、base algorithms/hyperparameters、50% selection/500k steps、seeds和evaluation scripts。逐 rule 审计选中 goals 的频率、可达性、coverage/TD error及失败案例。
- 应测试更多 OGBench tasks/dataset qualities、random/ambiguous/wrong task descriptions、LLM/seed/prompt changes、state representation shifts、sparse/dense rewards、OOD/restricted datasets、long horizons、多目标/constraints与真实/sim-to-real robotics。比较 non-LLM heuristic/learned key-state samplers，报告return/success、goal feasibility、value overestimation、compute/cost、rule compile errors和 safety violations。
- 高影响系统中，key-state rules必须来自经验证的任务/安全 specification并在 deterministic shield/constraint checker下过滤；保留 provenance、人工审批、fallback/abort和运行监控。LLM生成的语义prior不能取代可达性证明、collision/limit checks或对数据中历史行为的安全性判断。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 offline goal-conditioned RL 与 LLM-assisted relabeling extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ENPN5664.pdf) 核验四个组件/两类自检、Theorem 2.1/Corollary 2.2 的条件、OGBench 两任务、五个baseline、TD-error图与50%/500k setting；没有将条件性 TD-error 理论或基准图写成任意任务/机器人安全可执行、通用LLM可信或真实世界样本效率保证。
