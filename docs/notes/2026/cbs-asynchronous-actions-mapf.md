---
title: "Conflict-Based Search for Multi Agent Path Finding with Asynchronous Actions"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: "10.65109/FSCJ9273"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FSCJ9273.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["mapf_aa_model_scope", "duration_conflict_definition", "time_limited_simulation", "no_physical_robot_validation"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Conflict-Based Search for Multi Agent Path Finding with Asynchronous Actions

## 一句话总结

CBS-AA 面向具有异步、异质动作时长的图 MAPF：以持续时间冲突为约束对象，避免 CCBS 因连续 wait duration 的不可数状态空间而不完整的问题；论文证明在其 MAPF-AA 模型中 optimal 且 solution-complete，并以更强约束传播减少高层分支，但不等同于连续几何机器人碰撞安全证明。

## 方法与证据

- MAPF-AA 允许 agent/edge 有不同 action duration；本文的 duration conflict 规定 traverse edge 的全过程同时占用两端 vertex，不能与其他 agent 同时占同 vertex（§1--2）。
- CBS-AA 仍是 CBS 两层搜索，但产生针对 action/time interval 的 mutually disjunctive constraints；低层处理连续 wait，并以约束传播尽量延长/扩大禁止动作区间（§3--5）。
- Theorem 1 声称 CBS-AA optimal 与 solution complete：文中论证约束互斥、有限终止，若 feasible solution 存在则能返回最小 sum-of-costs 解（§6）。
- 实验比较 CCBS、LS-M* 与 CBS-AA/CMA/CMAS：每实例 30s，另有 120s；作者报告高层 branching 最多减少 90%，并在可解实例得到与 LS-M* 相同的 optimal costs（§7）。

## 局限与复现

- 完备/最优性仅对论文的 graph action、duration conflict、cost 与约束构造成立；不直接涵盖圆形/多边形机器人几何扫掠、加速度、动力学、定位误差、通信时延或不确定速度。
- 30/120-second cutoff 下 success rate 受机器、实现、instance distribution 与低层 solver 影响；branches 少不必然代表实际 wall-clock 或安全裕度更好。
- 复现应公开所有 maps、duration distribution、硬件、timeout、CMA/CMAS/SIPP 参数与逐实例结果，并用外部 continuous-time simulator 验证 edge/vertex 占用抽象没有漏碰撞。
- 作者将 speed 与 uncertainty 纳入模型列作 future work；这些因素是落地场景的核心而非已解决部分（§8）。

## 与 AAMAS 的关系与核验说明

这是异步多机器人路径规划的形式化 search 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FSCJ9273.pdf) 核对 MAPF-AA 定义、Theorem 1、实验 timeout 和 future scope；未将其理论 graph guarantee 表述为真实机器人安全认证。
