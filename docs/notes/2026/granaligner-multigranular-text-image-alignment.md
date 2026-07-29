---
title: "Multigranular Alignment via Linguistic Decomposition and Reward Optimization for Text to Image Diffusion"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/UEMK8185"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UEMK8185.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["reward_model_bias", "llm_assisted_object_scoring", "benchmark_alignment_scope", "detector_metric_limit", "stable_diffusion_v15_scope", "limited_training_data", "persistent_human_anatomy_failures"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multigranular Alignment via Linguistic Decomposition and Reward Optimization for Text to Image Diffusion

## 一句话总结

GranAligner 先将复杂 prompt 分解为 noun-phrase concepts 并控制 Stable Diffusion 的 cross-attention，再用 BLIP-2 的全局相似度和 RAM+LLM 的局部对象评分筛选高分图文对，以 LoRA/ReFL 微调模型。它改善 MS-COCO、ABC-6K 和 CC-500 指标，但“对齐”受 CLIP/GLIP/RAM/LLM 代理信号限制，复杂细节、对象数量和人体解剖仍会失败。

## 方法与证据

- Structural Decomposition 用语言解析把 prompt 分为 noun phrases，各自提供 cross-attention key/value 与 attention maps，以减少属性—对象混淆；Stage 1 生成初始图（§3.2）。这依赖 parser 对 prompt 结构的正确分析，抽象概念、否定、歧义和跨短语关系未被单独验证。
- Semantic Realignment 的 global reward 是 BLIP-2 caption/image embedding 与 prompt embedding 的 cosine similarity；local reward 用 RAM 给图像打标签，再由 LLM 依据 prompt/标签给对象 likelihood scores。二者选 top-\(K\) 图文对，随后以 \(L_{total}=\lambda_1L_{global}+\lambda_2L_{local}+L_{diff}\) 做 LoRA/ReFL 微调（§3.3）。评分器会继承其标签、语言和偏好偏差，reward 高不等于实体、关系或事实真实。
- 基准为 MS-COCO、ABC-6K 与双实体 compositional CC-500；全部 fine-tuned 方法使用同样随机选择的 3,000 个 MS-COCO samples，重复三次报告均值。骨干为 Stable Diffusion v1.5、512×512、A100 80GB（§4.1）。论文称兼容 DiT，但没有新 backbone 的实测结果。
- Table 1：GranAligner 在 MS-COCO FID/CLIP 为 13.1937/0.3394（Realign Diffusion 13.8941/0.3341），ABC-6K 为 13.1768/0.3412（13.9385/0.3352）。FID 衡量生成—真实图像分布距离，CLIP 是嵌入相似度；二者不单独验证关系、计数、偏见或安全。
- Table 2 的 CC-500 GLIP 检测：GranAligner “Two” 成功为 35.4%，仅比 Realign Diffusion 34.9% 高 0.5 percentage points；Zero/One omission 64.6%。因此虽然为表中最佳，绝大多数双实体 prompt 仍未被 GLIP 判为两个正确对象。
- 消融（Table 3）显示 Stage 1 单独为 FID 13.9103、CLIP 0.3346；Stage 2 单独为 14.4641/0.3214；完整模型 13.1937/0.3394。作者的 error analysis 仍报告复杂隐藏属性、纹理、时钟和人体手部失败（§4.4--4.6）。

## 适用边界与复现

- 适用于研究中改善英文式复杂 prompt 的属性绑定/对象存在，不应当作图像内容真实性、事实正确性、计数保证、身份一致性或视觉安全过滤系统。
- 局部 reward 取决于 RAM 识别和 LLM 打分；若对象漏检、标签粒度不匹配、属性/关系难以语言化或 LLM 有偏，训练会把错误监督固化。应人工审计筛选对、记录使用的 LLM/提示与版本，并检验不同评分器的一致性。
- 论文没有人类偏好研究、对抗 prompt、版权/训练数据治理、未成年人/生物特征/有害内容、偏见、地理文化泛化或真实设计工作流测试；复杂人体图和细粒度实体仍显示明显失败。
- 复现需固定 Stable Diffusion v1.5 checkpoint、parser/NP extraction、attention control、MS-COCO 3,000 样本与 seed、BLIP-2/RAM/LLM versions/prompts、top-\(K\)、LoRA/ReFL/\(\lambda\) 配置、图像 seeds/分辨率、MS-COCO/ABC-6K/CC-500 protocol、FID/CLIP/GLIP versions；报告完整生成预算、失败率和人工核验。
- 在任何面向用户、教育、广告或决策场景部署前，应增加内容与版权安全策略、人工复核、来源声明和敏感主体保护；benchmark 对齐改善不构成图像可信或无害保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的生成式代理、文本图像语义对齐和 reward-guided diffusion 论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UEMK8185.pdf) 核验两阶段流程、评分器、Tables 1--3、样本规模和失败分析；没有把 CLIP/FID/GLIP 的有限基准改进误写为普适的语义正确性、事实可靠性或安全生成保证。
