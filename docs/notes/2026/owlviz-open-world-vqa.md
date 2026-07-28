---
title: "OWLViz: An Open-World Benchmark for Visual Question Answering"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "safety_verification"]
dblp_key: ""
doi: "10.65109/EPVO9609"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EPVO9609.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["private_benchmark", "small_author_annotated_dataset", "exact_match_format_effect", "open_world_tool_safety_not_evaluated"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# OWLViz: An Open-World Benchmark for Visual Question Answering

## 一句话总结

OWLViz 是 248 题人工设计的视觉问答 benchmark，要求模型在 degraded images、计数/测量、多步推理、外部知识与工具使用之间协调；即使 Gemini-2.5-Pro/2.0-Flash 的最佳 EM 也仅 21.51%，但数据集保持私有、答案格式受限，分数不能作为通用“开放世界”能力的可复现结论。

## 方法与证据

- 数据集包含 248 个图像-问题-明确 ground-truth 答案。技能 taxonomy 包括识别、spatial relation、measurement、算术/计数、OCR/QR、GUI、knowledge search、API/metadata retrieval（§3、Table 1）。
- 问题由作者设计：一名作者初建，五名作者独立 review，随后内部工具随机分配给至少两位 reviewer；不能在无原作者额外信息下可靠作答的问题被移除（§3.3）。
- 为便于 Exact Match，答案被约束为多选/yes-no/单数值/短文本；作者明确指出这种格式可能收窄输出空间、从而高估模型表现，而 free-form answers 失败更多（§3.4）。
- 难度以独特 skills 数定义：Level 1 至多 2 skills/1 tool，Level 2 为 3--5 skills/通常两 tools，Level 3 可需任意长 action sequence、任意 tools 与 whole Internet access（§3.5）。
- VLM 表现中最佳 EM 为 Gemini-2.0-Flash/Gemini-2.5-Pro 的 21.51%，human 为 69.21%；tool agents 的最佳 EM 为 HF Agent 18.32%，DynaSaur 16.23%，GUI baselines EM 均 0。强制 DynaSaur 至少调用一个外部工具在作者测试中仅提升 EM 2 points（§4、Tables 2--5）。

## 适用边界与复现

- 248 个 author-annotated questions 规模小且 benchmark 私有；他人无法独立检查样本、泄漏、工具可用性、数据版本或复现实验，不能据此稳健比较模型排行。
- “open-world”在此是 image-driven query 可能需 Web/tools，不代表连续、对抗、隐私敏感或物理世界开放环境；外部搜索/API 的正确性、来源、权限、费用与副作用未被安全评估。
- Exact-match 与 constrained response 的低/高分都混入格式遵循因素；LM metric 也依赖 LLM-based judging。实际 agent 应另测事实核验、引用/provenance、拒答、不确定性、tool errors 和 harmful actions。
- 复现需要发布题目/图像及版权/许可、tool environment snapshots、internet access policy、prompt/model versions、EM/LM judge、human evaluation protocol 与 error taxonomy；在受控 sandbox/allowlist 中评估 tool-call agents。

## 与 AAMAS 的关系与核验说明

这是视觉语言 agent 与工具使用的 benchmark 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EPVO9609.pdf) 核对数据构建、skill levels、Tables 2--5 与格式限制；没有把私有小基准的分数或外部工具要求表述为通用开放世界能力/安全结论。
