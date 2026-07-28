---
title: "My Body, My Perceptions: A Shift from Computationalism to Embodied Cognition in BDI-agent-based Embedded Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "agent_engineering", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/QIVX3835"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QIVX3835.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_synthetic_scenario", "framework_version_compatibility_scope", "namespace_solution_interpretation", "no_multi_agent_hardware_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# My Body, My Perceptions: A Shift from Computationalism to Embodied Cognition in BDI-agent-based Embedded Systems

## 一句话总结

论文提出 MAOP+b/JACAMO+b：把嵌入式 BDI agent 的硬件 body 从共享环境 artifact 中分离，并把感知标为 interoception、exteroception、proprioception；单一模拟吸尘机器人场景显示这能避免同名温度 belief 覆盖，但其证据主要是建模/命名空间表达性，不是对 embodied cognition 或复杂真实 MAS 的广泛性能验证。

## 方法与证据

- MAOP 原有 agent、environment、organization 三维；作者新增 mechatropsychosocial/body construct，并在 JACAMO+b 项目语法中将 apparatus 绑定到 agent。body percept 直接写入 belief base，带 `source(interoception|exteroception|proprioception, apparatus)` 和 `myBody::` namespace（§4、Listing 1）。
- 相关工作 mapping 从 MAOP 种子论文出发，2025 年 8 月在 Scopus/WoS forward snowballing 得 536 条记录，筛后 full-read 33 篇；对四个 MAOP-compliant/physical-resource 方案 ARGO、Jason-ROS、JasonArchEmb、Javino 做比较（§3）。
- Descriptive Evaluation 为校园真空机器人：实验室空调与机器人内部都报告 `powerStatus`/`temperature`。在 JaCaMo+Javino、Jason-ROS 与 JACAMO+b 中运行同一 BDI plans/goals；前两者将同谓词、同 `source(percept)` 的最新信念覆盖，模拟中未区分内部过热，JACAMO+b 以来源/namespace 区分并在阈值前关闭清扫（§5、表 2、图 3）。
- ARGO 与 JasonArchEmb 因当前 JaCaMo 版本兼容性/CArtAgO workspace 问题未进入完整场景比较；表 2 将 JACAMO+b 标为 full MAOP/body/body-percepts 均具备，Javino 为显式 MAOP 与感知但无 body，Jason-ROS 为隐式 body（§5）。

## 局限与复现

- 成功主要验证了 schema/namespace 能避免同名温度 percept 覆盖；既有框架若加入来源标签、artifact ID、belief namespace 或冲突消解，也可能解决这个特定故障。因此不能从该案例推出新认知理论必然带来更好自主性、鲁棒性或安全性。
- 场景使用两个 software simulators/digital-twin 风格设备，单 agent、单 body、单故障模式；没有真实硬件时延、传感器噪声、执行器失效、资源竞争、多个 bodies/agents 或长期维护测试。作者也将 multi-agent/multi-body 留为未来工作。
- mapping 是一次 snowballing 和限定关键词的文献选择，不是系统综述的穷尽性/质量评估；框架可运行性取决于 2025 年的 JaCaMo/扩展版本，未能运行的架构不能仅据此判断概念能力。
- 复现应使用论文给出的源码/视频页，锁定 JaCaMo、Java、Javino/ROS/CArtAgO 依赖版本，公开 simulator 规则和 threshold、完整 agent plans、belief trace，并加入用传统来源标记的等价基线、真实或 hardware-in-the-loop、多 agent 的冲突/故障测试。

## 与 AAMAS 的关系与核验说明

该工作面向具传感器和执行器的 BDI agent 程序设计及 embodied MAS 建模。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/QIVX3835.pdf) 核对 MAOP+b construct、JACAMO+b 语法、mapping 和描述性场景，未将单例 API 表达性提升为通用的身体认知实证结论。
