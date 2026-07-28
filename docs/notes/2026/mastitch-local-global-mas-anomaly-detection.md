---
title: "MAStitch: Unifying Local and Global Perspectives for Anomaly Detection in Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/BMJZ4532"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BMJZ4532.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["post_hoc_log_detection", "llm_judge_hallucination_risk", "threshold_calibration_scope", "external_search_attack_surface", "token_latency_overhead", "not_preventive_control"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# MAStitch: Unifying Local and Global Perspectives for Anomaly Detection in Multi-Agent Systems

## 一句话总结

MAStitch 是一个无需额外训练的 LLM-based MAS 日志异常检测器：Local Analyzer Agents（LAA）按 agent execution chunk 对照配置基线评分，Global Analyzer Agent（GAA）聚合跨 agent 证据并在阈值触发时告警。它在特定 CrewAI/LangGraph 日志集上有较高平均 F1，但属于依赖日志完整性、LLM 判断、阈值校准和可选联网检索的检测/取证层，而不是攻击阻断、访问控制或安全保证。

## 方法与证据

- 输入是监控层产生的 execution log 加被监控 MAS 的实现；预处理按一次 agent invocation-to-termination 切为 chunks，并从 CrewAI/LangGraph 类属性抽取 role、goal、tools、task/expected output，作为 expected baseline（§3.1）。配置缺失、实现与运行时策略漂移、未记录工具调用或日志被攻击者篡改都会削弱这一基线。
- 每个 LAA 对一个 chunk 输出 validity score \(VS_i\in[0,100]\)、解释、issues 与摘要；原文说明低于 45 为稳定、45–75 为轻微偏离、至少 75 为 critical anomaly，并可并行处理 chunks（§3.2）。这是 prompt 驱动的评分，不是经校准的概率、形式化验证或独立安全裁决。
- GAA 累积所有 LAA records 形成动态记忆 \(H_i\)，估计 compromise confidence \(CL_i\)，并在任一 \(VS_i\ge V\) 或 \(CL_i\ge C\) 时告警；可在触发后 early-stop（§3.3）。early stopping 降低开销但可能漏掉随后传播/延迟出现的异常；设 \(V,C=100\) 可关闭该行为。
- 方法可让 LAA/GAA 用 internet search 验证可疑事实，也可接 code scanner、integrity validator 等工具（§3.4）。工具增强不是信任根：外部网页、检索结果、prompt injection、网络不可用和工具权限本身都是额外攻击/数据泄露面，部署需 allowlist、sandbox、审计和最小权限。
- 评测使用 LumiMAS 的日志/monitoring layer：CrewAI 的 Trip Planner、Instagram Post、Game Builder、Real Estate Team，及 LangGraph 的 GenFic/改造 Trip Planner；威胁为三类 DPI（misinformation/exhaustion/backdoor）、IPI、memory poisoning、Bandit 判为 medium/high 的 insecure code（§4.1）。hallucination、bias 等被作者明确排除在范围外，不能把“platform-/threat-agnostic”读成覆盖任意 agent 失效或政策风险。
- 每个 validation/test set 各 200 条、anomalous/benign 平衡且日志不跨集；MAS 端使用 GPT-4o mini 与 o3-mini，LAA/GAA 和 LLM baselines 使用 GPT-4.1 mini，最多 5 iterations/30 秒（§4.1）。\(V=70,C=75\) 由 CrewAI Trip Planner 的 benign+DPI validation F1 选择，故阈值跨应用、攻击强度、类先验或模型版本的泛化仍须重校准。
- CrewAI + GPT-4o mini 的 Table 1 中，MAStitch 各威胁 F1 为 0.826/0.947/0.920/0.966/0.798/0.941；作者报告平均 accuracy/F1/recall/precision/FPR 为 0.902/0.900/0.882/0.930/0.078（§4.2）。IPI 上 LumiMAS F1 0.970 略高于 MAStitch 0.966；insecure code 的 MAStitch FPR 为 0.310，说明平均数不能替代各威胁的误报/漏报和业务成本。
- Table 3 中完整方法的平均 F1 0.900、FPR 0.078，相对 w/o Config + Tool 的 0.849/0.130、w/o Config 的 0.827/0.100、w/o Tool 的 0.833/0.117 有改善。其平均 latency 12.653、token count 60,215.3；论文也承认多 LLM agents 带来较高 token/延迟开销，并可能降低告警时效（§4.3, §5）。

## 适用边界与复现

- 可作为有完整 trace 和显式配置的 MAS 的二线监测/事后取证组件；高风险操作应在工具执行前另有 deterministic policy guard、权限/审批、sandbox、egress control、secret redaction、rate limit 与可撤销的 kill switch。不要让“检测到告警”替代预防性控制。
- 论文明确承认 LLM analyzer 可能 hallucinate 或受外部攻击影响，且超 context-window 的 trace 必须截断、会丢失异常细节（§5.1）。应将检测器与被测 MAS 隔离，固定模型/提示/工具版本，保存输入哈希和原始不可变日志，并对配置/日志完整性建立签名或可信审计链。
- 生产评估需按目标业务的真实类不平衡、长 trace、并发 agents、tool failure、变化的角色/配置、未知攻击、对检测器的 prompt/data poisoning 与检索操纵测量 precision/recall、P95 latency、tokens/cost、漏报后的 blast radius 和告警可操作性。阈值应以独立校准集和明确的 false-positive budget 确定。
- 复现应取得补充材料中的 LAA/GAA/baseline prompts、应用/日志生成与 label 流程、monitoring schema、所有 split/seeds、GPT-4.1-mini calls/temperature、search provider 和缓存、threshold sweep、early-stop 配置、Bandit rule/version、LangGraph/o3-mini/10-agent 结果；正文未给出的补充内容不能从主文推断。

## 与 AAMAS 的关系与核验说明

这是面向 LLM multi-agent system 的安全监测与异常检测工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BMJZ4532.pdf) 核对 configuration-aware LAA/GAA 架构、阈值与 early-stop、辅助联网工具、六个应用/威胁/数据切分、模型与实现设置、逐威胁指标、ablation，以及作者对开销、LLM 失效和 context 截断的限制；没有把离线日志检测/解释误写为在线攻击预防、完整威胁覆盖或 MAS 安全认证。
