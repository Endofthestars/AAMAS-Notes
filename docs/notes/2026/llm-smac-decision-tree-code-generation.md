---
title: "LLM-SMAC: Solving Multi-Agent Decision-Making Tasks via LLM Decision Tree Code Generation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "generative_agents", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/RVAB7186"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RVAB7186.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "llm_code_generation", "smac_benchmark", "decision_tree_scripts", "ten_episode_evaluation", "official_pdf_doi_mismatch", "not_real_world_control_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# LLM-SMAC: Solving Multi-Agent Decision-Making Tasks via LLM Decision Tree Code Generation

## 一句话总结

LLM-SMAC 用同一 DeepSeek-Coder-V2.5-236B 驱动 Planner–Coder–Critic：根据 SMAC map/unit prompt 产 decision-tree strategy skeleton，译成 python-sc2 script，执行后把 win rate、score、damage 与 stack trace 交给 critic 决定改 plan 还是改 code。Table 1 在 23 张 maps 中 19 张报 90–100% win rate、4 张为 0%（在 iteration limits 内未找到 winning script），每 script 只评估 10 episodes。它展示对固定 SMAC/version、可执行脚本环境的闭环生成潜力，不等于无需探索的普遍 MARL、可迁移策略或真实自主系统安全。

## 方法与证据

- Planner 读取 task/unit/map info、previous skills/historical strategies，输出含 skill definitions/usage conditions 的 decision tree；Coder 生成 python-sc2 executable code；Critic 用 runtime stack traces、win rates、scores、damage statistics给 strategy/code revision建议，并决定下一轮改高层 plan或实现（Figure 1, §2）。代码执行与 critic feedback本身可能引入 prompt injection、unsafe side effects、sandbox escape、overfit and debugging loops；摘要未有隔离或 code verification 描述。
- 该框架是 scripts 的 open-loop game control planning，与 standard SMAC pysc2 policy training不同。LLM pretrained knowledge可能解释 low interaction，但也有 benchmark/code prior、prompt choice、iteration budget和 selected map的依赖；没有与可比 token/compute budget 的 MARL/rule/script baselines表格。
- Table 1 maps 3m…so_many_baneling 等 19 rows 为 90/100%（8m_vs_9m、27m_vs_30m为90），5m_vs_6m、3s5z_vs_3s6z、MMM2、6h_vs_8z均为0。相对标题的“strong transferability across homogeneous environments”，摘要没有具体 held-out transfer protocol/metrics，且四个失败显示 capability不均匀。
- 实验用 DeepSeek-Coder-V2.5-236B，each script 10 episodes with different seeds，report win rate/plan rounds/code rounds。未给 seed values、episode confidence intervals、model/prompt/temperature、max iteration/cost/time、SMAC/python-sc2 versions、script sandbox、enemy policy或 implementation source；10 episodes不足以支持稳定性或置信主张。
- 官方 metadata/PDF URL 使用 RVAB7186，而 PDF 的 ACM reference/footer 显示 DOI `10.65109/V1X2Y3Z4`。本笔记和 metadata 以官方 proceedings identifier `10.65109/RVAB7186` 保持可追踪，并标记该不一致，未擅自断言哪一个 DOI 是出版勘误后的最终值。

## 适用边界与复现

- 适合 SMAC-style simulator 的可审阅 code-generation research；不得直接让 LLM 生成并执行真实机器人、军事、交易或基础设施控制代码。必须使用 least-privilege sandbox、allowlisted API/actions、static/dynamic validation、simulation gate、human review、logging/rollback与 emergency stop。
- 复现需固定 SMAC/StarCraft/python-sc2 versions和 maps/enemy configs、all prompts/history, Planner/Coder/Critic/model settings、iteration limits、execution harness/sandbox、failure handling、10+ seeds/raw episodes、plan/code rounds、tokens/latency/cost。报告 23 map 的完整 win CIs、invalid-script/compile/runtime-error rates和 trajectory diagnostics。
- 应在 held-out/modified maps、randomized unit stats/spawns、partial observability、longer horizons、adversarial prompts/code outputs、tool failures和 nonhomogeneous tasks测泛化；与 MARL/rule baselines在同等 interaction/compute下比，并审计 rationale/tree是否与实际 code behavior一致。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM-assisted MARL decision-tree code-generation 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RVAB7186.pdf) 核验 Figure 1 workflow、DeepSeek backbone、Table 1 map outcomes和 ten-episode protocol；保留官方 ID 与 PDF DOI 的不一致，而未将 SMAC 成绩写成真实控制验证。
