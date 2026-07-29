---
title: "Centralized and Distributed Approaches for Restoring the Weak Controllability of Multi-Agent Interdependent STNUs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/FQWT7513"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FQWT7513.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03a"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "weak_controllability_only", "contract_bounds_discretization", "benchmark_time_limit", "privacy_claim_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Centralized and Distributed Approaches for Restoring the Weak Controllability of Multi-Agent Interdependent STNUs

## 一句话总结

论文针对 MISTNU 的 Weak Repair：把每个导致 weak uncontrollability 的 STNU negative cycle 写成只含 contracts bounds 的线性约束，并最小化收缩后的 contract widths；既可集中式线性规划求解，也可把同一问题转为 DCOP 分布式求解。作者在既有 benchmark、每实例一小时限制下称集中方法解出 250 个实例、此前 SMT 方法为 100；这是对可协商时长区间的弱可控性修复，不能直接推出动态可控性、在线执行鲁棒性或完整隐私保护。

## 方法与证据

- MISTNU 由各 agent 的 cSTNU、同步 reference timepoint 与 reification function 组成；contract 由 owner 控制、对其他 readers 是 contingent。论文假设不存在来自 Nature 的 non-negotiable contracts，且通过缩小 negotiable contract bounds 协商修复（§2）。
- Weak controllability 要求每个由 bounds reify 的 STNU 都 WC。检查算法返回的 negative/inconsistent cycles 是不可控根因；修复将 cycle 写成关于 lower/upper bounds 的线性表达，要求新 bounds 恢复至少负环长度，并加 \(l_p\le u_p\) 等约束及最小收缩目标（§3）。
- 例如摘要把一个长度 \(-5\) 的 cycle 编为 \((l_p-5)+(l_q-10)+(l_r-10)\ge5\)，可取三个 lower bounds 均为 10。该示例说明约束构造，不证明所有网络都有小幅或可行修复（§3）。
- 分布式方案中各 agent 本地检查 WC，分享涉及他人 contracts 的 cycles；把 contract bounds 作为 variables、bounds 离散化为 domain、cycle constraints 设为满足时 0/否则 \(+\infty\)，并以 bounds width 为代价构成 DCOP。原文的 privacy 理由是共享的 cycle 只包含公开 contract bounds（§4）。
- 实验称集中方法在一小时限制内解决 250 对 100 个实例；SyncBB/AFB 表现较好，DPOP/ADOPT failed，前两者相较集中 SMT 仅略好；若接受非最优解，所有实例可在数秒内解出。扩展到 Dynamic Controllability 仍是未来方向（§5）。

## 适用边界与复现

- 适合能公开可协商 contract intervals、且目标是修复 weak controllability 的多主体时间规划。收缩区间会改变任务弹性/可行集合，需要外部协商规则、业务代价与公平约束；最小总宽度不自动代表最公平或最有价值的修复。
- “privacy preserved”局限于 cycle 表达只用公开 contract bounds；cycles 的出现、结构、求解消息、时序或可推断信息仍可能泄露计划信息，必须在具体通信/威胁模型下审计。
- 复现应公开 MISTNU benchmark、WC checker/negative-cycle enumeration、线性约束生成、bounds discretization、LP/SMT/DCOP solver versions、time/memory limits、最优性定义和所有 instance outcomes；分开报告 no-solution、timeout 与失败。
- 动态执行、持续不确定性、Nature contracts、连续域近似和多目标谈判未被本文完整覆盖。生产调度应额外验证 DC、实时通信失败和执行策略，不能以 WC repair 单独保证可执行。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多智能体时间规划与 DCOP 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FQWT7513.pdf) 人工核对 negative-cycle 线性化、DCOP 转换、实验计数及 DC future work；未把弱可控性修复或有限信息共享夸大为动态执行/隐私保证。
