---
title: "PADME: Procedure Aware DynaMic Execution"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "safety_verification"]
dblp_key: ""
doi: "10.65109/HIOH2748"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HIOH2748.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02m"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["llm_procedure_execution", "graph_extraction_errors", "benchmark_action_match_scope", "tool_authorization_not_addressed"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# PADME: Procedure Aware DynaMic Execution

## 一句话总结

PADME 自动将自然语言 procedure 转为含依赖、决策点和节点元数据的 DAG；在 Teach 阶段生成可执行 decision graph，在 Execute 阶段按拓扑顺序运行并由环境反馈解决分支，以减轻长时程 LLM agent 的执行漂移。

## 方法与证据

- Procedure 表为 DAG `G=(V,E)`，nodes 分为 Human Input、Information Processing、Information Extraction、Knowledge、Decision 五类；非 decision nodes 绑定工具/函数，边表示数据或时间依赖（§2.1）。
- Teach 阶段 LLM 切分文本、构造局部子图并合并全局图；Execute 阶段对标准 nodes 确定性执行，在 Decision nodes 以当前上下文选择 `p(branch|context)`，再继续 traversal（§2.2--2.3）。
- 论文称图把未结构化动作搜索从 `Θ(|A|^T)` 约束为 `O(V+E)` traversal；这是结构表示下的搜索空间比较，不保证 LLM 抽取正确、工具调用成功或现实环境安全。
- GPT-4 在 Business Process、Recipe、ScienceWorld、ALFWorld 四类任务比较 Act-Only/ReAct/CoT/SPRING，以 action sequence 的 PML、PA、SM、FM 衡量；Figure 2 为五次 trial 的平均 FM，PADME 在图示四类数据上较高/最强。摘要未提供完整动作级错误、成本或统计显著性细节。

## 适用边界与复现

- Decision graph 可能遗漏前置条件、例外、权限、数据保留和人类判断；“可读/可验证 blueprint”不等于经过领域专家审核或合规批准。
- 预测 action sequence 与 ground truth 对齐不是业务成功、事实正确、风险受控或授权工具操作的充分指标。LLM graph extraction、tool bindings 和 runtime branch resolution 都可引入新错误。
- Business、食谱和模拟环境不代表金融、医疗、法律、生产系统中的长时程工作流。真实 automation 必须有最小权限、审批门、审计日志、回滚、异常处理与 human-in-the-loop。
- 复现需公开 procedure corpus、结构化 prompts/model version、DAG schema/validation、tool bindings、执行环境、baselines prompts、metrics definition、seeds、token/latency/cost和失败案例；高风险用例还需独立 domain review。

## 与 AAMAS 的关系与核验说明

该工作是图结构化的 LLM procedure execution。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HIOH2748.pdf) 核对 §2--4、Figure 1--2，未把基准序列匹配解释为生产部署可靠性。
