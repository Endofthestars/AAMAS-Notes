---
title: "LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/VLUA1303"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VLUA1303.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "offline_memory_curation", "workflow_action_risk", "memory_poisoning_unexamined", "officebench_only", "three_seed_scope", "retrieval_details_omitted"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation

## 一句话总结

LEGOMem 把成功的多智能体工作流轨迹离线蒸馏为 full-task plan/reasoning memory 与对各工具 agent 的 subtask/tool-interaction memory，再分别分配给 orchestrator 与执行 agent；在 OfficeBench 上的三种检索变体比无记忆团队报告约 12--13 个百分点的成功率提升，但论文为 Extended Abstract，只有单一 benchmark、三 seed 汇总与有限实现细节，尚未验证记忆正确性、污染防护、生命周期或真实办公系统的安全执行。

## 方法与证据

- 目标架构是带 central orchestrator 与 specialized tool-using task agents 的 workflow automation 系统（§1）。离线 curation 从“无记忆”运行中抽取成功 trajectories：full-task memories 包含 task-level plan/reasoning trace，subtask memories 包含特定 agent 的行为和 tool interactions；它们存入 procedural memory bank，作为现有 multi-agent 系统上的 RAG layer（§1、Figure 1）。
- inference 时 orchestrator 得到相关 full-task memory 以帮助分解/选 agent，task agents 得到与委派子任务对齐的 memory。比较三种策略：vanilla（task-level retrieve 后分配相关 subtask memory）、dynamic（为 agent 按语义选相似 subtask memory）、query rewriting（改写 subtask query 后检索，§1）。文本没有提供 memory schema、trajectory success 判定、embedding/index、query rewrite prompt、容量/淘汰、版本、检索质量或污染过滤细节。
- OfficeBench 是唯一报告 benchmark；表格比较 LLM-only、hybrid、SLM-only multi-agent teams（§2、Table 1）。相对 memory-less teams，vanilla/dynamic/query-rewrite 分别提高总体 success 12.61、12.72、13.38 个绝对百分点；作者举例 hybrid + QueryRewrite 为 50.22%，高于 memory-less LLM team 45.83%。每个 data point 为三个 random seeds 平均，不能据此得出跨应用、跨模型或高置信生产增益。
- Table 2 认为 memory placement 比 retrieval variant 更关键：orchestrator + task agents 的 joint allocation 最好；在仅 task-agent memory、且 hybrid team 的小 task agents 场景，dynamic/query-rewrite 比 vanilla 高约 4--5%（§2）。这支持“plan memory 给 orchestration、操作 memory 给执行”的设计假说，但并没有将 memory 信息量、role prompts、agent model/工具能力、工作流长度或 token/cost 独立消融。
- 原文明确标为 Extended Abstract（首页），结论也仅称在 workflow automation tasks 上“consistent improvement”（§3）。没有完整实验 protocol、OfficeBench 子任务/权限/环境配置、基础模型/API snapshot、工具调用次数、运行成本/延迟、置信区间/显著性、失败案例、persistent update、memory leakage、恶意 trajectory、过期流程或真实用户评测。

## 适用边界与复现

- 适合研究可组合 workflow 中把已验证的执行轨迹拆分成 planner/executor 级 hints，尤其是有可回放 sandbox 与明确成功判据的办公自动化基准；不应把它直接用于发邮件、改云文件、财务/HR/医疗/法律系统或任何不可逆的生产工具动作。
- 复现需要公开 OfficeBench 版本与任务 split、全部 agent/orchestrator prompts/models/tools、成功轨迹选择规则、memory objects/source citations、index/embedding/retriever/query rewriting、三变体和 placement ablations、three seeds 原始 success/失败轨迹、token/latency/API/tool cost。应做跨 benchmark、跨团队/模型、不同 memory size 与任务相似度的独立评测。
- 必须测错误或过时 procedure、部分成功 trajectory、tool response drift、prompt injection/数据外泄、memory poisoning、agent role mismatch、retrieval OOD、重复运行与 memory growth；报告 false retrieval、错误动作率、实际权限范围、回滚成功率和人审覆盖。仅“成功记忆”离线蒸馏并不排除将隐含的不安全操作模式复用到新任务。
- 生产系统应把记忆当作建议而非可执行授权：每条 procedure 要有来源/版本/owner/有效期/权限标签，工具调用经 policy engine、dry-run、least privilege、transactional rollback 和独立 verifier；涉及外部账户、发送/删除/支付必须人工审批。更高 OfficeBench success 不构成数据安全、合规或现实工作流正确性保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多智能体 workflow automation、程序记忆与任务规划论文，且为 Extended Abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/VLUA1303.pdf) 核验 full-task/subtask memory、三种 retrieval、orchestrator/task-agent placement、OfficeBench 三-seed 成功率结果及 Extended Abstract 范围；没有把其单一基准上的离线轨迹复用夸写为通用 long-term memory、安全工具自动化或成熟生产系统。
