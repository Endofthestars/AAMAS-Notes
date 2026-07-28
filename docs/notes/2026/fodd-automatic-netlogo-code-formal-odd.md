---
title: "Transparent and Accessible ABMs with FODD: Automatic Code from Formal ODD"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "human_agent_interaction"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XDBV4230.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["proof_of_concept_scope", "netlogo_target_only", "static_checks_not_semantic_validation", "user_friendly_claim_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Transparent and Accessible ABMs with FODD: Automatic Code from Formal ODD

## 一句话总结

FODD 将 ODD agent-based-model 文档的部分内容变为带类型与结构约束的领域规格，并由 JetBrains MPS 中的 ODD2NetLogo 生成器确定性地产生 NetLogo 代码；这降低文档—代码漂移，但当前只是六个模型上的 proof of concept，不是对 ABM 行为、有效性或生成代码语义正确性的通用形式验证。

## 方法与证据

- FODD 保留 ODD 的文档结构，将 entities/state variables、process/scheduling、initialization、submodels 和 experiments 等选择性地形式化；purpose、rationales、emergence 等仍可为 informal，interaction/stochasticity 等部分由规格推导并保留文本。因而其“formal ODD”不是把所有叙述都形式化（Table 1、§2、§4）。
- 工具 ODD2NetLogo 建在 JetBrains MPS，包含 structure（抽象语法）、editor（投影编辑器）、constraints（静态语义）和 generator（动态语义）。用户在 ODD 式编辑器内写规格，完成后点击生成，导入 NetLogo 运行实验；同一规格确定性产生同一输出（§2.1、§3）。
- 约束通过类型、作用域和结构完整性检查拦截例如把 sheep 用于 wolf action、非数值 attribute 的 increment、未定义引用和必填字段为空；生成规则是可审查的参数化 templates。它们保证的是规则允许的规格与生成路径的一致性，不自动验证建模假设、现实对应关系或研究问题是否被正确表达（§3.3–3.4）。
- 文档中的 derived section 从形式规格抽取已用实体、属性、随机性与实验信息，减少重复输入；interface/experiment 部分仍有 NetLogo 专有约定，因此“backend-independent”主要指概念层，支持其他平台需要另行编写 generator/runtime mapping（§2、§4）。
- 可行性报告覆盖 MARG、DomWorld 以及 NetLogo Library 的 Voting、Fire、Wolf Sheep Predation、Cooperation 六个模型；对这些案例，论文称 NetLogo implementation 全部由 FODD 规格生成，无需手写 NetLogo。评估维度是 executability、expressivity、user-friendliness，但为初步可行性评估，未报告受控生产率/错误率对照试验（§5）。
- 当前 generator 只产出 NetLogo，行为构件刻意受限以维持高抽象；用户需要学习 FODD，行为规格尚不直观于社会科学家，不支持从既有 NetLogo 代码反向生成规格，且输出不保证与手写代码一样多样或已优化（§5–6）。

## 局限与复现

- FODD 的静态检查不能发现所有“意图不完整但仍类型合法”的规格；论文明确说这类输入可能无错误生成。因而 runnable NetLogo 既不证明 ABM 的因果机制正确，也不替代校准、验证、敏感性分析或同行审查。
- 所谓 verified alignment 应理解为规格—生成器—输出的可追溯/确定性链接；generator 模板本身编码了实现与代码风格选择。它不是针对生成 NetLogo 的定理证明、模型检查或对自然语言 ODD 的完全语义等价证明。
- 六个案例只说明受限行为语言在这些模型上可表达；不支持将可用性、表达性、跨领域部署或减少建模时间概括到任意社会模拟、复杂学习 agent、连续空间/网络 ABM 或已有代码库。
- 目标仅 NetLogo，且无 reverse engineering；采用 Java、Python、Mesa、Repast 或目标平台专有 UI/experiment 功能的项目，需要新的映射并重新验证其约束与生成语义。
- 复现应固定 MPS/ODD2NetLogo 版本、六个 FODD 规格、generator templates 和 NetLogo 版本；分别记录 constraint diagnostics、生成差异、运行日志及 ODD-derived fields。若评价“accessible”，应采用预注册的 domain-expert 用户研究，与 narrative ODD 和手写模型工作流比较任务正确率、时间和理解，而非仅检查代码可运行。

## 与 AAMAS 的关系与核验说明

该文针对 agent-based simulation 的可审查性与跨学科协作，提供从高层 ODD 规格到可执行 ABM 的工程链路。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XDBV4230.pdf) 核对形式化边界、MPS 结构/约束/生成器、六案例证据和作者列出的限制；不将 proof of concept 或静态可检查性误写为 ABM 的完整形式验证。
