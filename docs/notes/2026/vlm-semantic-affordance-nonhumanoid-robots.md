---
title: "Assessing VLM-Driven Semantic-Affordance Inference for Non-Humanoid Robot Morphologies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "human_agent_interaction", "safety_verification"]
dblp_key: ""
doi: "10.65109/WTKR8312"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WTKR8312.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["vlm_hallucination_risk", "semantic_metric_dependency", "human_annotation_dependency", "synthetic_data_dependency", "limited_morphology_coverage", "no_closed_loop_robot_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Assessing VLM-Driven Semantic-Affordance Inference for Non-Humanoid Robot Morphologies

## 一句话总结

本文评估 VLM 能否根据非人形机器人的文字形态描述，推断画面中物体对该机器人的语义可供性；在混合真实/合成数据上，模型对与形态直接对应的 Push、Scoop 等更有效，但跨形态、空间与材料约束时不稳定，呈现低 false-positive 与高 false-negative 的保守偏差。它可作为生成候选语义的感知研究，不是可直接执行动作的安全 affordance detector。

## 方法与证据

- pipeline 将机器人尺寸/能力的自然语言 prompt 与相机帧交给 VLM，要求输出对象及 affordance；再以 GroundingDINO 做 2D localisation，并用空间邻近和语义相似度合并对象标签（§3）。机器人能力主要由文本描述约束，未闭环验证几何可达性、抓力、接触、碰撞、控制误差或任务成功。
- 数据为 100 个独特对象、774 个标注 object instances，含 86 个真实来源/246 实例与 528 个 synthetic 实例；总共有 4,745 affordance–object instances（Tables 1–2）。真实视频来自受控但杂乱的 DOTS arena，合成视频由 Google Veo3 生成；所有 ground truth 由人工标注。作者报告真实/合成 mean score 差约 ±0.05，但这不是对合成偏差、注释一致性或真实世界覆盖的完整检验。
- 评估 GPT (`gpt-5`)、Gemini (`gemini-2.5-pro`) 与 Claude (`claude-opus-4-1-20250805`) 的 provider 默认超参、五次独立 trials；比较 humanoid baseline 和 Scoop/Push/Pick/Lift/Cut/Collect 六种非人形能力（§4）。模型版本、服务行为、图像输入和默认参数会随时间变化，五次调用不等于跨版本或跨场景鲁棒性。
- ground-truth/VLM 的 affordance–object labels 先用 SBERT `all-MiniLM-L6-v2` cosine similarity 配对，阈值 \(\tau=0.45\) 由典型样本选择，再算 TP/FP/FN 与 F1（§4.1）。因此 F1 同时依赖人类标签、文本同义词嵌入、阈值、对象配对和“可供性”本体；不能直接解释成物理可执行率或安全概率。
- humanoid baseline 下 Claude/GPT mean F1 为 0.53/0.51、Gemini 为 0.36；non-humanoid 结果更分散，Gemini overall mean F1 为 0.5（§5）。模型常把标注能力替换为一般人类行动（如 Throw、Squeeze），导致正确但任务外的输出被记作 false negative；这支持该基准中的保守偏差，不证明模型知道何时行动。
- 清晰的非人形物理描述改善 Push、Scoop、Collect 等与形态直连的推断并减少 out-of-scope 人类动作；但 Lift 中 Claude/GPT 会把地上物体判为可抬，Cut 会把 golf ball、screwdriver、paint pot 等不合材料也判可切（§5–6）。这些是空间、上下文与材料理解失效，实际机器人若无独立约束不得执行。
- 作者也指出 Food/Sports Equipment 比 Construction Items 表现好，推断与人类中心训练数据有关；API 调用耗时 3–10 秒，不支持实时更新，并建议 task-conditioned prompts、人类验证和更大公开 benchmark（§6）。一个初步 real-data task prompt 探索提升 non-humanoid mean 约 0.03–0.1，尚非完整对照实验。

## 适用边界与复现

- 可用作高层语义候选生成或离线 benchmark baseline；应把 VLM 输出视为未经验证的 hypotheses，交给几何/动力学 affordance model、场景图、物体检测、可达性规划和任务约束共同筛选。
- 在真实机器人上，所有动作前须经可信状态估计、碰撞/工作区/速度/力/负载限制、物体材料与姿态感知、motion planning、runtime monitor、emergency stop 和 human override。低 FP/high FN 不是安全认证：漏掉可行动作会降低任务能力，空间或材料 false positive 仍可能造成损害。
- 复现需固定作者数据集/标注、真实与 Veo3 生成材料比例、抽帧率、六种 robot prompt、API model snapshot/temperature/图像格式、五个 trial seeds、GroundingDINO 与关联距离、SBERT 模型及 \(\tau=0.45\)、object matching、F1/confusion-matrix 汇总。应分别报告真实/合成、每种形态、每类物体及每条 affordance 的 precision/recall。
- 应在更多实体机器人、未见对象/材质、不同光照/遮挡、连续几何/动作测量、任务条件、对抗 prompt 与闭环执行中评估，并报告碰撞、失败、near-miss、延迟、人工干预和校准；仅在独立安全控制器内测试 VLM 建议。

## 与 AAMAS 的关系与核验说明

这是面向异构 embodied/multi-robot 场景的 VLM 语义可供性评测。AAMAS 官方 PDF 镜像在本次核验中连续连接超时；笔记改依据同题、同作者、同 AAMAS DOI 的 [作者公开 arXiv 全文](https://arxiv.org/abs/2604.19509) 逐项核对，并保留 [AAMAS 官方记录](https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm)。没有把文本形态 prompt、F1/语义匹配、低 false-positive 或受控视频结果误写成物理 affordance 识别、实时规划、闭环执行或机器人安全保证。
