---
title: "Resolving Task Objective Conflicts in Unified Model via Task-Aware Mixture-of-Experts"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "generative_agents", "safety_verification"]
dblp_key: ""
doi: "10.65109/DLJD3800"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DLJD3800.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "two_task_scope", "supervised_task_routing", "expert_capacity_growth", "limited_benchmark_scope", "no_open_task_evaluation", "no_safety_alignment_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Resolving Task Objective Conflicts in Unified Model via Task-Aware Mixture-of-Experts

## 一句话总结

UniDecouple 针对统一自回归多模态模型中 MMU（理解）与 T2I（生成）的梯度/信息流冲突，用 task-specific expert groups、shared expert 和两级 router 构成 TA-MoE，并先分任务训练 experts、再 LoRA 联合微调；在 POPE、MMMU、GenEval 上优于 JanusPro，但“冲突”实证只覆盖这两类有已知任务标签的目标，且为 3 页 Extended Abstract，尚不能证明对开放多任务、未知路由、真实多模态安全或所有负迁移普遍有效。

## 方法与证据

- 作者把 Task Objective Conflict（TOC）定义为 AR sequential dependency/causal attention 下 MMU 主要更新早 token representation、T2I gradient 从后 token 流动，二者 gradient overlap 可能产生负内积、negative transfer/catastrophic forgetting（§1--§2）。这是针对统一 AR 模型的机制性假设；文中没有给跨架构、跨数据、跨 seed 的完整梯度统计或因果干预证明。
- TA-MoE 把 experts 划为 MMU-specific、T2I-specific 和一个 shared expert。hierarchical routing 先由 task-aware router 指派 token 到 expert group，再由 dynamic router 在组内 top-\(k\)；specific 与 shared 输出以 learnable \(\alpha\) 加权相加（§2）。loss 由两个 task-specific cross-entropy loss 加 router group supervision 组成，因此正确 task/group label 是训练时显式输入；未知、混合、模糊或跨域请求的 routing/abstention 没有评测。
- 训练两阶段：Stage 1 冻结 self-attention、单独训练 task-specific FFNs；Stage 2 用 TA-MoE 替换 FFNs，对两任务 end-to-end LoRA fine-tune，rank \(r=16\)（§2）。这减少直接干扰但新增 task/expert/router 状态与训练步骤；没有报告总参数、activated compute、load balance、router collapse、专家迁移、训练成本或随着任务数增长的容量/延迟。
- TOC 验证用 POPE（understanding）与 GenEval（generation）的单任务对照：MMU-only 86.9 POPE、T2I-only 0.74 GenEval、joint 86.2/0.73，降 0.7/0.01（Table 1，§3）。同时提到 antagonistic loss dynamics。这个小幅、两任务损失不等于所有 unified multimodal AR models 都存在严重 conflict，亦未排除数据/任务权重/容量/训练日程造成的差异。
- 表 2 对 JanusPro：UniDecouple 为 POPE 87.2、MMMU 41.7、GenEval 0.76，JanusPro 为 86.2、36.3、0.73（§3）。作者还称 task router/shared expert 和 two-stage training 均有帮助，2:1 的 group-specific:shared expert ratio 最佳；但 Extended Abstract 未给完整 ablation 数字、seed/CI、模型规模、数据/训练 token、prompt/sampling、视觉 tokenizer或显著性检验。
- qualitative samples 讨论 VQA、description、OCR、spatial/natural/character scenes（Figure 1、§3），但没有评测 hallucination、版权/偏见/隐私、图像安全、prompt injection、task misclassification、实际用户价值或涵盖 video/audio/agent tools。结论限制为 MMU/T2I unified model 的一种效率/性能方向（§4）。

## 适用边界与复现

- 适合研究两类已标注、多模态自回归训练目标之间如何进行 parameter/pathway partition，并比较专门化与共享信息；不应被当作通用多任务 optimizer、复杂 agent 的 objective alignment 方案，或生成内容/理解结果安全可靠的证明。
- 复现需公开 base AR model、image/tokenizer、MMU/T2I datasets/splits、task-mixing schedule、stage-1/2 optimizer/steps/LoRA/\(r=16\)、expert count/ratio/top-k/\(\alpha\)、router group labels/\(L_{group}\)、loss weights、JanusPro baseline、seed/CI/compute。应报告单任务、联合、各个消融、router assignments/load、loss/gradient conflict measurements 和错误样本。
- 必须评估三种以上互冲突任务、continuous/multi-label/unknown task、OOD inputs/intent shifts、task label noise、不同 capacity/data balance、expert scaling/collapse、cross-modal adversarial examples、long-context/vision-language/video，以及质量--延迟--成本 trade-off。应使用独立 safety/factuality/calibration/fairness metrics，不能仅以 POPE/MMMU/GenEval 代替。
- 在高风险生成或决策中，task router 输出需要置信度与 safe fallback；专家隔离不应绕过内容过滤、权限/隐私控制、来源核验、人类复核与可撤销处置。性能分数更高不代表目标冲突、用户意图冲突或社会伤害已被解决。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的统一多模态模型、Mixture-of-Experts 路由与负迁移缓解论文，且为 Extended Abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DLJD3800.pdf) 核验 TOC 定义、TA-MoE/两级路由/两阶段 LoRA、Table 1 的冲突对照、Table 2 的 JanusPro 比较和 2:1 expert ratio 叙述；没有把有限的 MMU--T2I 有监督实验夸写成开放多任务冲突解决、模型对齐或多模态系统安全保证。
