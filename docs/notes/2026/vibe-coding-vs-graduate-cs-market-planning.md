---
title: "Can Vibe Coding Beat Graduate CS Students? An LLM vs. Human Coding Tournament on Market-driven Strategic Planning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "game_theory_mechanism"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SEOT8410.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_apdp_benchmark_scope", "prompt_model_version_sensitivity", "human_cohort_scope", "tournament_not_general_coding"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Can Vibe Coding Beat Graduate CS Students? An LLM vs. Human Coding Tournament on Market-driven Strategic Planning

## 一句话总结

在 Auction Pickup and Delivery Problem（APDP）物流竞赛中，作者将 40 个 LLM 生成的 agent 与 17 个预 LLM 时代的人类编码 agent 比较；12 个双循环赛约 4 万场中前五均为人类 agent，但这是特定长程规划、竞价和车辆调度基准，非普适编程能力排名。

## 方法与证据

- APDP 要求 agent 在不确定任务到达下竞价、规划多车 pickup/delivery，并与对手进行动态市场竞争；评测核心是策略/优化代码在对战中的 profit/wins，而不是单元测试或单函数正确率（§3）。
- 比较 57 个 agents：40 个由 4 种 LLM、多个 prompting 策略（含 vibe coding、迭代改进、critic 等）生成，17 个为 ChatGPT 前开发的 12 个 EPFL 研究生课程 agent 和 5 个实验室 baselines。作者调试后仅保留可运行 LLM agents（§4）。
- 12 个 double all-play-all tournaments 覆盖 4 个 network topologies，每赛所有 agent 双方各执一次，合计每 tournament 3192 matches、总约 4 万场。结果称 top 5 均为学生 agent，33/40 LLM agents 被简单 baseline 击败；给最佳人类代码让 LLM 改进也导致性能下降（§5–6）。

## 局限与复现

- 结论限定 APDP、选定 LLM/模型版本、prompt、两次生成与调试流程、17-agent 人类 cohort 和固定 tournament topology；不证明人类普遍优于 LLM、也不证明任意 LLM coding workflow 无效。
- agent 的可运行性筛选、提示策略、时间限制、代码模板和是否给错误信息修复会显著影响成绩；应报告全部生成尝试、失败原因、token/成本与源码，而非只报告 tournament winners。
- 竞赛 wins/profit 混合算法设计、市场策略、运行效率和对手分布；不能外推到安全关键软件、普通应用开发、开发者生产率或经过人工审查/工具调用的协作编程。
- 复现应固定 APDP simulator、任务分布、topologies、时限、prompt/model version 与随机种子，开放所有 57 agents 和逐场日志，并加入不同 human experience、LLM-assisted human 及独立基准。

## 与 AAMAS 的关系与核验说明

该文以竞争型多 agent 物流市场测试 LLM 代码生成的长程策略能力。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SEOT8410.pdf) 核对 benchmark、agent 构成、12 场赛制与作者列出的评估限制；不将其外推为通用编程能力结论。
