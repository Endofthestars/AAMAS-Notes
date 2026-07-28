---
title: "Human-Inspired Context-Selective Multimodal Memory for Social Robots"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "human_agent_interaction", "agent_engineering"]
dblp_key: ""
doi: "10.65109/JQIR9876"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JQIR9876.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["biometric_emotion_inference", "long_term_personal_data", "synthetic_pilot_dataset", "identity_misrecognition_risk", "threshold_tuning_dependency", "no_longitudinal_robot_deployment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check; author preprint fallback)"
reviewed_at: "2026-07-29"
---

# Human-Inspired Context-Selective Multimodal Memory for Social Robots

## 一句话总结

SUMMER 是一个免训练的社交机器人图文 episodic-memory 架构：以人脸情绪显著性或场景新颖性选择存储，再融合文本、图像和场景描述检索个体化经历。它在 81 张合成社会场景的 memorability 标注、通用图文检索基准及运行时测试中有正面结果；但它会处理人脸、情绪、身份与长期私人记忆，且没有真实长期人机部署或隐私/同意验证，不能直接视为安全的社交记忆系统。

## 方法与证据

- SUMMER 分为 perception、interaction 与 control layers：perception 从场景和面部表情估计 memorability，满足选择条件的图像及自动生成 scene description 按 user ID 存储；interaction 以 text/multimodal/scene embedding 融合检索并由 Mistral-small3.2 生成回复（§3–4）。它是组件编排，不训练新的端到端社交记忆模型。
- 存储规则是“emotion salience 超过按类别设置的阈值”或“当前场景与既存 memory 的 embedding 距离超过 novelty threshold”（§3.2）。阈值、emotion model、face detection、embedding drift 和初始记忆库都会决定哪些事件被永久保存/遗漏；“难忘”不等于用户希望机器人保留、可再次提及或向他人披露。
- 身份模块以 face verification 关联 user-specific memories；无匹配时创建新 ID，置信区间会触发澄清（§3.4）。作者称 memory operations 在获得 consent 后才激活，但论文没有提供同意 UI、撤回/删除、加密、访问控制、保留期、未成年人/旁观者处理、跨设备同步或 biometric false-match 的实证评估。
- 选择性存储评测使用作者生成的 81 张合成 social-scenario 图片；25 名参与者都以 1–9 Likert 评分，每图观看 1 秒。通过 nested cross-validation（5 outer/3 inner folds，20 repeats）调 per-emotion 与 novelty thresholds（§4.2）。最佳 emotion+novelty 配置 \((0.5,0.5,0.0)\) mean Spearman \(\rho=0.506\)，human consistency 是 0.4152；作者明确较高的“与聚合人类评分相关”不表示超过人类记忆能力。
- social pilot 中 ResMem/ViTMem 表现差，作者归因于 domain mismatch；在各自训练领域的 LaMem 测试上则为 0.8145/0.7583（§4.2）。因此 SUMMER 的优势可能部分来自针对该小型合成数据和阈值的设计/调参，不能据此外推到真实持续交往、不同文化、弱表情或异常情绪。
- retrieval 在 Flickr8k、Flickr30k、MS COCO 上比较 image-only、text-only 与 fusion，作者报告 fusion 的 Recall@1 最多高出单模态 13%，常见最佳融合权重约 \(\alpha=0.7\)（§4.3）。这些通用 caption/image 数据不包含 robot-user 的长期关系、同意状态、身份混淆或社交后果。
- runtime 在 2×RTX 4090 上测量，per memorable scene perception pipeline 约 0.37±0.03 秒，情境事件非连续发生；这不能证明端到端实时社交机器人可行，尤其不含摄像、网络、身份错误处理、对话排队、数据库增长和人类纠正延迟（§4.4）。
- qualitative 比较展示图文 memory 回复比 text-only baseline 更丰富、更能回答视觉上下文（§4.5），但没有盲评、人类满意度、信任校准、情绪伤害、记忆错误率或长期依恋/过度拟人化指标。作者未来仍要加入 social relevance、关系和个体意义等选择因素（§5）。

## 适用边界与复现

- 可作为获得明确许可后的本地、可检索多模态记忆研究原型；每次存储/检索应向用户可见，提供查看、编辑、按事件/人删除、导出与永久退出机制，并把情绪/身份推断标作不确定信号而非事实。
- 真实社交/辅助机器人应实行 data minimization、默认短保留、加密与密钥隔离、角色访问控制、旁观者遮蔽、明确/持续同意、身份不确定时不关联历史、敏感话题检索禁区、审计日志和人工申诉。绝不可根据情绪模型或旧记忆独立作医疗、照护、纪律、招聘或安全关键决定。
- 复现需固定 81 图数据和生成过程、25-rater protocol、观看时长、Likert 聚合、OpenFace emotion pipeline、face/ID 阈值、embedding encoders、novelty memory order、nested-CV splits、Flickr/MS COCO 切分、fusion \(\alpha\)、Mistral prompt、硬件/版本和完整 runtime 定义。应报告 individual-rater 分布、失败/删除案例和数据泄露测试。
- 后续须用有伦理审批的长期真实交互研究评估 consent comprehension、false recall、identity mix-up、记忆纠错、隐私伤害、偏见、文化差异和退出后的删除有效性；在不同算力及 memory growth 下量化延迟、成本和检索准确性。

## 与 AAMAS 的关系与核验说明

这是连接 embodied HAI、选择性长期记忆与多模态检索的社交机器人架构工作。AAMAS 官方 PDF 镜像本次连续超时，笔记依据同题、同作者、同 AAMAS DOI 的 [作者 arXiv 全文](https://arxiv.org/abs/2604.12081) 核对；并保留 [AAMAS 官方记录](https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm)。没有把合成 pilot correlation、公共检索 Recall@1、组件运行时间或定性回答误写成长期个性化有效性、情绪理解准确性、用户同意、隐私保护或真实机器人部署保证。
