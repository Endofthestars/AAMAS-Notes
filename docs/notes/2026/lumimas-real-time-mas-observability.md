---
title: "LumiMAS: A Comprehensive Framework for Real-Time Monitoring and Enhanced Observability in Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["agent_engineering", "safety_verification", "generative_agents"]
dblp_key: ""
doi: "10.65109/PNWL9707"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PNWL9707.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04f"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["mas-observability", "anomaly-detection", "root-cause-analysis", "llm-security", "synthetic-attacks"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# LumiMAS: A Comprehensive Framework for Real-Time Monitoring and Enhanced Observability in Multi-Agent Systems

## 一句话总结

LumiMAS 是面向 LLM 多智能体系统的三层可观测性框架：统一记录 agent/workflow 事件与通信特征，实时检测异常，再以分类和 root-cause analysis 解释失败来源，目标覆盖跨 agent 的系统级失效而非单 agent 监测。

## 方法与证据

- logging 层记录 Application/Agent start-finish、LLM calls、tool usage、operational/resource/communication 特征；异常层组合事件模式与文本语义特征，解释层输出 failure classification 和 RCA（§4）。
- 威胁模型覆盖 DPI、IPI、memory poisoning、hallucination 与 bias，并映射到 MAST 的 specification/misalignment failure modes；明确对 verification-oriented modes 覆盖有限（§3）。
- 七个 CrewAI/LangGraph 应用中每个模拟逾 2,000 benign scenarios，validation/test 各 200 logs、半数异常；在五 seed CrewAI+GPT-4o-mini 结果中 combined 检测器平均 F1 0.754、FPR 0.267、decision 0.057s，文中最快 LLM judge 为 8.448s（§5）。

## 适用边界与复现

- 数据和攻击由作者模拟，阈值/日志 schema、应用和失败类别强烈影响检测性能；0.754 F1 不能证明可识别任意 prompt injection 或提供安全保证，RCA 的正确性还需独立核验。
- 复现需公开七应用、日志事件 schema、attack scripts、train/val/test generation、features/embeddings、detector/RCA prompts、thresholds、LLM 版本和 token/runtime accounting。部署还须做隐私最小化、日志访问控制和攻击者规避检测的红队评测。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PNWL9707.pdf) 人工核对三层架构、设置与 §5.2 数值；未将合成失败检测结果外推为生产系统完整安全认证。
