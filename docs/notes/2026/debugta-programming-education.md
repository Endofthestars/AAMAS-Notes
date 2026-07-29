---
title: "DebugTA: An LLM-Based Agent for Simplifying Debugging and Teaching in Programming Education"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "generative_agents", "safety_verification"]
dblp_key: ""
doi: "10.65109/GYMB4283"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GYMB4283.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "student_simulator_evaluation", "reference_solution_access_required", "variable_alignment_error_risk", "academic_integrity_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DebugTA: An LLM-Based Agent for Simplifying Debugging and Teaching in Programming Education

## 一句话总结

DebugTA 是编程教育的 debugging-and-teaching agent：从 code repository 以 BM25 检索标准解，用 LLM 把标准解变量名对齐为学生代码命名，配合 compiler 和 dictionary memory 分步生成修改建议。它在 CodeApex、ACMOJ、Code4Bench 与 GPT‑4o‑mini/Qwen‑7B/DeepSeek‑16B 上，以 Student Simulator 采纳建议后的 AC@1 显示优于 direct/self-debug baselines；这说明该 pipeline 可提高模拟代码修复率，并不证明学生学会调试、避免答案泄露或课堂学习成效提升。

## 方法与证据

- DT 输入包含 erroneous code、error message、reference/standard solution 与 problem description（§1）。作者指出直接给标准解可能造成 answer leakage 或因 variable names 不一致而混淆；系统是否真正避免泄露还取决于检索范围、提示/输出 policy、作业规则、学生可见内容和复制检测，本文未做 academic-integrity study。
- Standard Code Retrieval 以 BM25 基于 structural/textual similarity 从 repository 取最相关 correct solution（§2.1）。BM25/文本相似性可能选错题目、旧版本、边界条件不同或有版权/许可限制的 code；论文未报告 retrieval Recall@k、repository coverage/contamination、licensing、跨语言或对抗性代码/注释的鲁棒性。
- Variable Substitution 以 LLM aligner 将 reference variables 映射为 student variables而不改 logic，作为 backbone 的“perfect hint”（§2.2）。此描述是设计目标：若 scope、alias、shadowing、types、data structures、control flow 或多函数语义不对齐，替换可能掩盖真正 bug/给出错误建议；未给 alignment correctness、syntax validity、failure rate或人工教师审查。
- agent 的 dictionary memory 存 retrieval results、compiler feedback和intermediate reasoning，选择性检索避免 context overflow（§2.3）。外部 compiler 给实时分析，但文稿未说明 sandbox、resource/time limits、untrusted code isolation、language/version、test generation、privacy/retention、memory contamination或prompt injection防护。
- 评估 CodeApex、ACMOJ、Code4Bench，backbones GPT‑4o‑mini、Qwen2.5‑Coder‑Instruct 7B、DeepSeek‑Coder‑V2‑Lite‑Instruct 16B；baselines含 direct debug/teach、standard-code direct、self-debug explanation/trace（§3.1）。Student Simulator（StuBot）收到 suggestion后尝试修复，metric 是 repaired code AC@1。Table 1 例如 GPT‑4o‑mini DebugTA AC@1 为 CodeApex 94.44、ACMOJ 42.00、Code4Bench 26.44；Qwen 86.11/25.00/18.39；DeepSeek 90.74/24.00/20.69。图 2 在 ACMOJ 报 Origin 27.02、DebugTA 50.70，去掉 retrieve/aligner降低。
- AC@1 由 LLM simulator而非学生完成，且本文未给任务数/splits、StuBot prompt/model/temperature、human ratings、learning pre/post test、完成时间、suggestion factuality、compilation/pass rate、seeds/CI/显著性、作弊/依赖或不同基础学生效果。因而“teaching effectiveness”“preventing plagiarism”“reduced costs”应限于 simulation/系统设计主张。

## 适用边界与复现

- 适合在许可的练习环境为学生提供带解释的调试提示，尤其教师已维护可信 reference solutions且能控制输出粒度时；不应直接用于高风险考试、自动评分/纪律处分、要求保密的商业代码或将完整修改直接交付为学生作业答案。
- 复现需公开或合法获得 datasets/problems/reference repos/licenses、BM25 indexing/query/top-k、variable aligner prompt/model/validation、memory schema、agent workflow/stop criteria、compiler/runtime/container/test suite、StuBot prompt/model/decoding、all backbones/baselines、AC@1 evaluator、seeds/CI与每题输出。单独评测 retrieval/alignment/compile/teaching explanation正确性，而不只看最终AC。
- 应做人类学生随机对照研究：理解/迁移/保留、debugging strategy、时间、认知负荷、不同经验/语言/无障碍群体、公平与overreliance，并审查 hallucinated/unsafe suggestions、answer leakage、版权、code plagiarism、隐私和teacher workload。测试多语言/大型项目/test failures/ambiguous specs、adversarial inputs及长多轮对话。
- 生产教学需最小权限的 compiler sandbox、代码和学生数据保护、reference solution access control、可见性分级（hint而非完整patch）、citation/provenance、plagiarism/assessment policy、教师复核和学生申诉。LLM/agent 应明确显示不确定性并鼓励学生运行测试、解释修改，而不能以 simulator AC 替代教学质量或学术诚信判断。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM agent、工具使用和编程教育 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GYMB4283.pdf) 核验 BM25/variable substitution/compiler/memory、三数据集/三backbones、StuBot AC@1、表 1 和图 2；没有把 simulation repair success写成学生学习、无抄袭、教学安全或通用代码正确性保证。
