---
title: "Influencing LLM Multi-Agent Dialogue via Policy-Parameterized Prompts"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "human_agent_interaction", "safety_verification"]
dblp_key: ""
doi: "10.65109/VAVC8140"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VAVC8140.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["dialogue_behavior_steering", "public_policy_topic_simulation", "synthetic_personas_and_knowledge_bases", "llm_judge_and_embedding_metrics", "not_human_opinion_or_policy_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Influencing LLM Multi-Agent Dialogue via Policy-Parameterized Prompts

## 一句话总结

本文把多 LLM 对话中的 prompt 视为 policy action，以 persona/task (T)、dialogue memory (M)、retrieved knowledge (D)、rule template (R) 与权重 (W) 动态组装 prompt，在两类公共议题讨论中改变回应、反驳、引用、重复和立场相似度指标；这表明 prompt 能操控模拟 agent 的文本动态，不表示它模拟了真实公众、产生更真实/正确的观点，或适合在实际公共协商中暗中引导参与者。

## 方法与证据

- 每个 agent 为 (\{Q,T_i,D_i,LLM_i\})，state 由 task/persona、global dialogue memory 与 role-specific knowledge 构成；policy (\pi_i) 根据 state 产生 prompt (a_i(k))，输出写回 memory。权重控制 (T,M,D) 的提示强度，rule template 决定格式/信息使用方式（§3.1--3.2）。
- 三个 rule templates 分别为 None（无结构约束）、Light（先回答、给 1--2 条 (D) 证据、必要时回应 (M)、长度限制）与 Struct（按 supporting/opposing/conflict/cooperation 四类提取后生成）；每个 (T/M/D) 权重在 0--2 映射为 low/mid/high 微指令（§3.2.1--3.2.2）。
- adaptive schedule 令 memory weight 随轮数增加、knowledge weight 递减；若上一轮未用 (D) 或未回应 (M)，则按 (\alpha) 增加相应权重。该方式是 hand-designed update rule，不是经 reward/gradient 学得的 RL policy（§3.2.3）。
- 评测五项输出指标：judge 判定的 responsiveness/rebuttal、字符串/embedding 重复度、retrieved snippets 的 phrase match evidence usage、输出与 persona embedding 的 stance similarity。三个指标依赖 embedding，另外两项依赖 LLM judge（§3.3）。
- 实验有 Land Resource Use 与 Educational Resource Allocation 两场景，各 3 个角色（分别配 Qwen3-8B、Llama3-8B、Mistral-7B）、每题 10 轮、每 query 5 次运行。role-specific knowledge 来自公开政策文件/博客/网站，先由 ChatGPT-5 汇总补充并生成 stakeholder roles/task descriptions（§4.1、Table 2）。
- 结果显示规则/权重改变指标，但没有单调“最好”配置：Struct 常提高 non-repetition；高 (W_T) 提高 rebuttal/role loyalty；(D+T) ablation 较平衡；全组件仅温和改善。Rovers 等并非此文内容；该文也发现 homogeneous Qwen3 对话活跃度低于 heterogeneous backbones，且 adaptive weights 改变 round-wise 曲线而不显著改均值（§4.2--4.4、Table 1/4/6）。

## 安全边界与复现

- policy-parameterized prompt 是可解释的文本控制界面，也可被用于放大既定角色、冲突、证据外观或立场稳定性；在涉及公众、选民、学生、员工、患者或消费者的实际对话中，不应把这种 steering 隐藏为中立协商。需要清楚披露 agent 身份、角色/目标、prompt 干预、知识来源与自动化程度，并允许退出、纠错和人工复核。
- 两个公共议题是三 agent 的合成 persona 讨论；ChatGPT-5 对素材的汇总和角色生成会引入筛选/框架偏差。文本 stance similarity 不等于态度、代表性、同意、说服或事实准确性；evidence metric 仅检验 retrieved phrase 出现，也不验证证据的真实性、相关性或推理有效性。
- 5 runs、10 rounds、两个领域、固定小模型组合不足以证明跨议题、跨语言、长时群体互动或人类参与的稳定效果。作者的 cross-judge 检查可降低一部分 judge-choice 风险，但不替代 human annotation、统计功效、事实核查、偏见审计或社会影响评估。
- 复现应固定公开材料/检索索引、ChatGPT-5 summarisation 与 role-generation prompts、RAG chunking/top-3、完整 (T/M/D/R/W) 提示、模型版本/temperature、轮数、judge prompts/embedding model、(\alpha)、seeds 与逐轮 transcripts。部署前还应做 adversarial prompt injection、citation provenance、manipulation/undue-influence 测试、human consent 与 domain governance 审查。

## 与 AAMAS 的关系与核验说明

这是 LLM multi-agent dialogue、可控 social simulation 与 prompt policy 参数化工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VAVC8140.pdf) 核对 (T/M/D/R/W) 设计、三种规则、五指标、两场景十轮五次运行、backbone/judge/ablation 实验；没有把被影响的 agent dialogue 表述为真实社会意见、事实性协商或公共政策建议。
