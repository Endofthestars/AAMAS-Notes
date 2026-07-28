---
title: "Developing Guidelines for Human-LLM Agent Teams: A Multi-Stakeholder Lens"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "norms_trust_governance", "agent_engineering"]
dblp_key: ""
doi: "10.65109/JOWO4591"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JOWO4591.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["expert_sample_bias", "workplace_context_bias", "guideline_not_control", "no_field_deployment", "llm_capability_assumption", "regulatory_context_dependency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Developing Guidelines for Human-LLM Agent Teams: A Multi-Stakeholder Lens

## 一句话总结

本文以工作场所中的持续性 human–LLM teaming 为对象，提出面向 LLM agent、互动人类、团队设计者和嵌入组织的 24 条设计指南，并按团队发展的五个阶段组织。指南由专家工作坊、对 93 篇经验研究的综述和小规模专家评估迭代得到；它们是可进一步本地化、测试与治理的设计起点，而不是能自动控制 LLM、保证输出正确或已被真实组织绩效验证的操作标准。

## 方法与证据

- 论文将指南安排在 early stages、active collaboration、completion、continuous learning 与 affect management 五类团队过程，并分配给四类行为主体：LLM agent、与其互动的人、team designer、embedding organization（§3, Fig. 1）。这一结构刻意把人、设计与组织责任纳入范围，不把安全/协作责任都归给 prompt 或模型。
- 阶段 1 是便利抽样的 15 位 human-AI teaming 专家工作坊，分三组观看 OpenAI Operator 示例、把既有 HAI/human-agent guideline 转成系统需求，并以 reflexive thematic analysis 提炼透明度、主动性、协调/控制、保障与适应性等主题（§4）。其中 8 人自报 AI 相关专长、7 人偏 HCI/HAI/社会技术系统；这提供探索性专家输入，不是代表性用户需求或因果效果证据。
- 阶段 2 从 ACM Digital Library 于 2025-07-17 检索到 241 篇，按七项排除准则保留 93 篇包含人与 LLM/agent 自然语言交互的经验研究，人工提取其情境、结果与设计建议（§5.1）。作者将其与工作坊材料做反思式主题分析，得到 27 条规则式指南，再经全体作者 5 轮迭代与团队过程映射整合（§5.2）。来源被限于学术文献和一个数字图书馆，行业发布、实践材料及检索/筛选主观性仍会影响覆盖面。
- 阶段 3 以 personal health、coding、travel、legal assistant 情境做 survey 与 60 分钟 think-aloud，再把 27 条收敛为 24 条（§6）。参与者总数为 10 位、经作者网络目的性招募；分析时因明显疲劳剔除一名 survey 受访者，因此 Fig. 2 的 guideline-group 评分为 survey \(n=4\)、think-aloud \(n=5\)。这些是清晰度、相关性和可设想行动的专家主观反馈，并未测量任务成功、事故、信任校准、生产成本或长期福祉。
- 评估显示 coding 与 legal 等工作场景下普遍被认为相关，而 travel/health 等消费者情境出现较多“不相关”或角色不清的问题；作者据此指出其 teaming lens 更贴合迭代、持续的 workplace collaboration（§6.2）。因此不能直接把每条规则套用于一次性客服、个人健康建议或无明确组织/团队边界的产品。
- 评审促成具体收敛：把逐步解释改为“提供供输出核验的信息”以避免过度依赖；把一条对使用者要求过高的指南移交 team designer；把“提升感知能力”改为让感知能力与实际能力匹配；并合并部分重叠的 continuous-learning 指南（§6.2）。这支持作者对可读性/适配性的修订，不验证 LLM 实际遵守、用户实际核验或风险已降低。
- 论文明确假定 LLM agent 具备执行面向 agent 的指南的技术能力；foundation model 的开发不在范围内，组织可通过 fine-tuning、基础设施或 system prompt 实现部分规则（§3）。提示词或训练并不能替代工具权限控制、身份认证、审计、数据治理、模型评测和运行时执行约束。

## 适用边界与复现

- 可作为设计工作场所 human–LLM agent team 的讨论框架：先明确谁是团队成员、角色/责任/交接、允许的自主性、信息与工具边界、核验与反馈闭环，再选择与情境有关的指南。每一项都应有可观察的 owner、触发条件、失败模式和验收指标。
- 高风险或受监管领域不能只凭指南上线。应另行实施权限最小化、显式确认与双人复核、工具 sandbox、数据分类/访问控制、日志与独立审计、模型/工具失效降级、申诉与人工接管，并依据适用法规和组织责任结构进行法律、安全与隐私审查。
- 复现应保留 241→93 的检索式、日期、七项 exclusion criteria、每篇提取字段、工作坊材料/分组/转录与 coding trace、27 条初版及五轮改动记录、四种 scenario 文案、问卷量表与 fatigue exclusion、think-aloud 脚本/编码规则；作者提供的详细指南材料链接也应按版本归档。
- 后续验证宜在行业团队中做预注册、跨组织和跨文化研究，比较采用/未采用指南的协作质量、错误发现率、过度依赖、延迟、责任归因、心理负担与长期适应；同时覆盖消费者、公共服务与高风险情境，并以真实 agent 权限和工具调用进行红队测试。

## 与 AAMAS 的关系与核验说明

这是将 human-AI teaming、组织化多智能体角色/规范与 LLM agent 工程连接起来的设计研究。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JOWO4591.pdf) 核对 24 条指南、四类主体与五阶段框架、15 人工作坊、241→93 文献筛选、10 人评估与最终有效评分、场景差异、具体修订和作者限制；没有把专家对相关性/清晰度的反馈误写成实地部署、标准合规、模型可控性、输出真实性或安全性保证。
