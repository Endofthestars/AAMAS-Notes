---
title: "From Actions to Words: Towards Abstractive-Textual Policy Summarization in RL"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "human_agent_interaction"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EGVR4787.pdf"
preprint_url: "https://arxiv.org/abs/2503.10509"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["llm_hallucination_scope", "captioner_domain_dependence", "human_study_external_validity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# From Actions to Words: Towards Abstractive-Textual Policy Summarization in RL

## 一句话总结

SySLLM 将 RL 的多条状态—动作轨迹转写为带时间顺序的文本经验缓冲区，再以分层 LLM 摘要和候选共识选择，生成描述策略全局行为模式的自然语言说明。

## 方法与证据

- 论文把策略摘要定义为从经验缓冲区 $B_\pi$ 到抽象文本解释 $T$ 的映射；coverage、parsimony 与 fidelity 是指导设计和评估的概念性目标，而非被直接求解的优化保证（§3）。
- 每一步 observation 与 action 经领域 captioner 转为文本，并连同 reward、episode id 组成 Textual Experience Buffer；MiniGrid 用规则 captioner，Crafter 还编码库存、邻近资源/威胁、健康与成就（§4.1–4.2、§5）。
- 当缓冲区超出上下文预算时，SySLLM 将其分块、递归摘要后再次摘要；在可容纳的输入上采样 $K$ 个候选，以 embedding 到中心距离的中位代表候选作为最终文本（§4.3、Algorithms 1–2）。这是一种稳定化启发式，而不是对真实性的证明。
- 实验使用 GPT-4-Turbo（temperature 0.5）与 `text-embedding-3-small`，在五个 MiniGrid 环境的七个 agent 及 Crafter 的两个 agent 上评估；MiniGrid 每 agent 收集 50 个评估 episode，Crafter 每 agent 收集 5 个（§5）。
- 六名有 RL 训练/评估经验的研究生依据视频形成专家摘要，作者用原子行为点的人工匹配计算 recall/precision；九个 agent 的平均 recall 为 0.840、precision 为 0.839，平均 raw agreement 为 70%、Gwet's AC1 为 0.72（§7、Table 3）。
- 与 HIGHLIGHTS-DIV 的用户研究初始招募 200 人、剔除后为 192 人；75.5% 直接偏好 SySLLM。策略识别任务中两种呈现形式都高于随机猜测，三道题的正确率差异不显著；仅其中一个条件的 SySLLM confidence 更高（§8、Figures 5–6）。

## 局限与复现

- 文本说明的忠实性受 captioner 限制：作者明确指出当前依赖领域特定 captioning，向高维或部分可观测真实场景迁移仍需可靠的视觉/感知 grounding（§9）。
- 专家一致性与平均匹配分数支持的是本文九个受控策略上的评估，不等于 LLM 对任意轨迹、长尾失败模式或反事实问题都不会产生幻觉。
- 用户研究比较的是 MiniGrid 中的三种策略和指定的 HIGHLIGHTS 配置；“75.5% 偏好”是该受试样本的主观偏好，不能直接推出对真实操作员的调试效率或安全性提升。
- 复现应固定 caption 模板、每个策略的轨迹数和切块方式、LLM/embedding 版本与采样随机种子；同时保存候选摘要、原子点标注和排除规则，才能检查共识选择是否掩盖少见但关键的行为。

## 与 AAMAS 的关系与核验说明

该文将 LLM 用于解释已训练 RL agent 的全局策略行为，连接 agent engineering 与人—agent 理解。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2503.10509) 核对了文本经验缓冲、分层摘要、候选选择、专家评估和用户研究的适用范围。
