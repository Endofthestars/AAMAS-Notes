---
title: "Self-Evolving Software Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/HKPK4104"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HKPK4104.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02x"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "llm_code_synthesis_risk", "preliminary_prototype", "behavioral_inheritance_instability", "no_security_or_sandbox_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Self-Evolving Software Agents

## 一句话总结

论文提出 BDI--LLM self-evolving agent：在常规 belief--desire--intention loop 旁设置 Automated Evolution Module，在现有知识/目标/动作无法解释或利用经验时，自动生成新需求、修订推理结构和合成可执行行为，并以 variation--selection--inheritance 保留有效结果。Deliveroo.js 风格动态多智能体原型显示从极少先验可发现操作目标，但行为继承、稳定性和复杂环境扩展性仍是作者承认的未解限制；它不是能安全自修改生产系统的工程方案。

## 方法与证据

- 标准 BDI loop 负责运行时感知、belief 更新、desire deliberation、intention/plan 执行；独立 evolution module 监视经验，在发现当前结构不能解决的新需求时触发，不把长期演化混入每一步决策（§2）。
- 演化作用于三层：知识/推理（感知和推断机制）、goal/decision（新目标和 intention selection）以及 execution（合成/调整 actions 与 plans）。设计意图是以隔离保持行为连贯，同时利用 LLM 做需求、设计和代码更新（§2）。
- 原型基于 BDI control loop 加 LLM evolution module，在 Deliveroo.js 启发的动态多智能体环境中仅给文本环境说明和最少 API；不可解释/不可利用的感知触发演化，新行为经环境交互验证，成功者保留、无效者丢弃（§3）。
- 摘要只给初步定性结果：能从 minimal prior knowledge 发现 operational goals、生成 executable behaviours；同时指出 inheritance、robustness、稳定性和更复杂环境的 scalability 问题，没有任务数量、成功率、成本、测试集或代码安全实验（§3--4）。

## 适用边界与复现

- 可作为研究“运行时适应”与“受控软件演化”边界的架构概念；LLM 生成 goals、reasoning 或代码会扩大权限、依赖、注入、数据泄露和不可逆副作用风险，必须置于 sandbox、审批和回滚机制中。
- 环境交互验证不等于行为正确、非回归或安全；成功/失败的选择标准、memory consolidation、版本化和长期一致性尚未被量化。作者也把 reinforcement、继承和稳定机制列为未来工作。
- 单一 Deliveroo.js 式原型与最小 API 不足以证明跨语言、跨工具、跨组织或长期自治；文本说明/LLM version/prompt/model nondeterminism 可显著改变演化结果。
- 复现应发布 BDI semantics、触发条件、prompts/model/version、API permissions、生成代码审查/测试/沙箱、选择与回滚策略及完整事件轨迹；在隔离基准报告成功、失败、回归、成本、持续行为保留、攻击/注入抵抗和人工审批负担。

## 与 AAMAS 的关系与核验说明

该文把软件演化原则加入 BDI agent architecture。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HKPK4104.pdf) 人工核对三层演化、原型触发/验证流程和作者自述限制；没有将可执行行为生成解释为安全、可靠或无监督生产部署。
