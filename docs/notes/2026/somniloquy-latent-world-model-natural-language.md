---
title: "Translating Latent State World Model Representations into Natural Language"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "argumentation_reasoning", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/GUWU9511"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GUWU9511.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["world_model_miscalibration", "language_translation_faithfulness_limit", "rule_based_narrator_supervision", "simulation_only", "goal_text_ambiguity", "no_deployment_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Translating Latent State World Model Representations into Natural Language

## 一句话总结

Somniloquy 在 Dreamer 的 RSSM 潜状态计划上训练 encoder–decoder translator，把模型想象中的一段计划译为语言；再以“译文是否蕴含目标”的首次达成时刻作为模型内 reward 来训练 policy。Crafter、AI2THOR、MiniGrid 与固定 BabyAI gridworld 的结果支持这一受控模拟接口，但语言描述首先是对 world model 的陈述：模型失准时，它可以流畅而忠实地描述一个错误的“梦”，不构成真实环境理解、开放式指令对齐或部署安全保证。

## 方法与证据

- Dreamer 的 latent state 由确定性 RNN 分量与随机分量组成；Somniloquy 将固定长度 latent plan 逐步线性嵌入，输入 transformer encoder，再由 decoder 自回归产生语言 token（§3–4）。训练用 teacher forcing 和 token cross-entropy；translation loss 可回传至 world model，作者默认采用这一版本，并另比较 detach latent state 的版本。
- 监督文本不是人工自由标注或开放世界视觉语言描述：为方便概念验证，作者为每个环境构造 rule-based narrator，读取模拟器提供的环境 state 序列并生成交互说明（§4）。state 仅用于训练监督、模型输入仍是 observation；但这也把可译内容、词表、粒度和对象语义限定在研究者设计的 narrator 中。
- 对语言目标 \(\ell_g\)，实验把“译文蕴含目标”简化成 substring match；当当前前缀首次匹配时给 reward 1，之后为 0（§5.1）。这缓解了把 reward 放在完整 planning horizon 末端的 credit-assignment 问题，却不是对否定、歧义、组合泛化、语用意图或安全约束的通用自然语言理解。
- 确定性翻译评测在 Crafter（固定 procedural-generation seed 的生存/采集/制作环境）和 AI2THOR kitchen（首次拿起不同物品的自定义任务）进行：每次以 16-step plan、15 evaluation episodes 测译文与实际执行 narrator 的 BLEU-4，5 seeds 报均值和标准差（§6.1–6.3）。作者报告 Crafter 中持续较高的翻译分数，AI2THOR 也表现良好但波动更大；这衡量的是自设 narrator 的 n-gram 相似，不等于人是否正确理解、语言是否因果解释或现实机器人是否可靠。
- 随机性测试使用自建 MiniGrid teleporter：从同一开始状态生成多条 latent rollout，按翻译估计 transition distribution，与已知真实分布比较 TVD；每个起点 30 samples、15 evaluation episodes、5 seeds（§6.1–6.3）。结果只称“somewhat accurately”近似随机动态，且作者明确无法区分是 translator 错还是 world model 错。
- 语言→reward 评测在固定的 BabyAI `GoToLocal`：世界模型以 uniformly random exploration 收集的 50K environment steps 训练并冻结，随后仅在模型中、每个目标 500 次 policy updates；目标是四个固定颜色/物体组合（red key、blue/green ball、purple box），与 naive-language-rewarding 和使用真实目标标注训练 reward head 的 extrinsic-rewarding 对照（§6.2–6.3）。论文报告所有方法/目标到 100 updates 后环境成功率为 100%，Somniloquy 与后者表现持平、naive 版本的 credit assignment 较差；这是一项小型、封闭词表和固定布局设定下的可行性证据，不能证明 unseen goals 泛化——作者也明确把泛化排除在范围外。
- 允许 translation gradient 塑造 representation 时，Crafter 的 return 与 detach 版本无显著差异，AI2THOR 中作者观察到较高且更稳定的 task performance；随机 MiniGrid 也呈现较低波动（§6.3）。这些是实验曲线趋势而非跨任务显著性、安全性或计算成本结论。

## 适用边界与复现

- 适用于已能在训练模拟器中取得近似 state、可定义结构化 narrator、且希望检查/约束 world-model imagined plans 的研究工作。面向真实机器人时，须独立验证感知、状态估计、world-model calibration、语言 fidelity 和执行后果；不得把计划文字直接当作事实报告或安全认证。
- 不能仅凭 substring reward 让用户用自然语言授权高风险行为。实际系统需采用能处理否定、量词、时序、约束与歧义的目标判定，加入权限与硬安全约束、独立 runtime monitor、动作前确认、审计日志、真实环境失败检测与人工接管；语言解释不能替代这些控制。
- 复现应固定 Dreamer/RSSM、translator 架构与 tokenization、plan length 16、\(\beta_{trans}=10\)、是否让梯度回传、narrator 规则、环境 seed、exploration 数据、50K world-model steps、policy update budget、所有四个 BabyAI goal 与三个 reward modelling 方案。报告每 seed 的 BLEU-4/其他指标、TVD、modelled/real success、return、失败样例和随机性采样数，而不只给平均曲线。
- 应扩展到模型失配和 OOD 观测、长短不同 horizon、学习式或人工 narrator 的偏差、人类可读性/忠实度研究、复杂组合与未见目标、部分可观测真实机器人、目标冲突和 adversarial prompt；还要分开测量“latent plan 被正确翻译”与“latent plan 对真实世界预测正确”。

## 与 AAMAS 的关系与核验说明

这是连接 model-based RL、可解释 agent planning 与 language-conditioned reward 的 AAMAS 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GUWU9511.pdf) 核对 Dreamer+transformer 结构、rule-based narrator、substring entailment、四个模拟环境、16-step/15-episode/30-sample/5-seed 协议、BabyAI 50K/500-update 设置以及作者对 world-model error 与固定 horizon 的限制；没有将 narrator-BLEU、模型内成功率或受控 gridworld 结果误写成真实环境准确性、开放语言理解、人的信任校准或部署级安全性。
