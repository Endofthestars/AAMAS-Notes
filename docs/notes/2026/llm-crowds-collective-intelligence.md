---
title: "Wisdom of the Machines: Exploring Collective Intelligence in LLM Crowds"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "agent_engineering", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/MTWR9974"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MTWR9974.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["small_evaluation_sample", "vision_numeric_estimation_scope", "three_model_ensemble", "no_human_baseline", "independence_assumption", "api_version_and_cost_drift", "scalar_aggregation_only", "domain_specific_oversight_required"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Wisdom of the Machines: Exploring Collective Intelligence in LLM Crowds

## 一句话总结

论文将无通信的视觉语言模型调用视为独立“群体成员”，比较异构模型造成的 model diversity 与同一模型多温度采样造成的 response diversity，再盲态汇总数值估计。在人像体重、物体质量和 Amazon 商品价格各 100 个样本上，三模型（GPT-4o-mini、Qwen2-VL-72B、Llama-3.2-11B-Vision）的温度 0 输出取中位数是最稳健方案，平均优于 68% 的同条件个体预测；增加温度采样没有显著改善且增加成本。结果只覆盖小样本、视觉标量估计与三种当时 API 版本，不能证明 LLM 调用真的独立、能替代人类群体，或适用于需要交互、事实核验、结构化输出和高风险决策的多智能体系统。

## 方法与证据

- 三个数据集各以固定 seed 42 随机抽 100 个：人像的体重（可提供身高）、Image2Mass 小物体质量（可提供尺寸）、Amazon Canada 商品价格（可提供商品标题）（§3.1.1）。任务是从图像预测一个标量，不是开放式问答、协商或真正的社会模拟。
- 使用 GPT-4o-mini、Qwen2-VL-72B-Instruct、Llama-3.2-11B-Vision-Instruct-Turbo；前两类重量任务对每模型测试温度 0.2–1.0、每配置每图 15 次，共 225 次调用/图。Amazon 价格依据前述发现仅温度 0、每模型每图一次（§3.1.2–3.1.4）。模型版本、供应商、价格与推理行为都可能随时间变化。
- 汇总比较 arithmetic mean 与 median，并曾试 token log-probability 加权但未见显著收益；主分析采用不看真值的中位数。性能用 aggregate 的绝对误差在同一条件下所有 individual errors 中的 rank percentile，并用单侧 paired t-test 检验（§3.2–3.3）。这种排名衡量相对群体位置，不直接给出绝对校准、安全阈值或跨任务效用。
- 论文将三模型的差异解释为可抵消的系统偏差，形式化上假设误差零中位数且弱相关；coordinate-wise median 是最小化绝对距离和的 Fréchet mean（§3.4）。共享网络语料、相似视觉表征或提示诱发的共同偏差可违反独立/弱相关假设，论文没有直接测量这些相关性。
- 各数据集与 context 条件下，All Models + temperature 0 的 median 对比平均 individual rank 的 one-sample t-test 均 \(p<0.0001\)；表 2 的平均 rank percentile 为 0.342（身高体重）、0.314（Image2Mass）、0.311（Amazon 价格），平均 0.322，即约优于 68% 个体预测（§4、表 2）。这不表示在每个样本上都胜过最佳模型，作者也明确没有单个模型在所有任务持续最佳。
- median 在所有可检验条件下优于 mean（\(p<0.001\)），符合其对离群预测的鲁棒性；成本–MRE 图显示主收益来自 model diversity，单模型加温度多样性只带来边际改进且成本更高（§4、图 3–5）。这是对所选三模型及请求实现的经验 Pareto 比较，并未完整核算 FLOPs、延迟、内存或生产系统开销。
- context 的效果依任务而定：商品标题将 Amazon 价格 aggregate 的 MRE 从 88% 降至 45%（\(p=0.025\)）；身高体重（\(p=0.13\)）和 Image2Mass（\(p=0.15\)）未显著（§4）。应把辅助信息是否消除主要不确定性作为设计假设，而非一律附加上下文。

## 适用边界与复现

- 适用于预算允许、可将输出化为同一量纲标量、且可选取来源较异构的多个视觉/语言模型的低至中风险数值估计；中位数可作为抗单个极端值的简单 baseline。
- 不应把无通信 API 调用称为具有人类意义的集体智能或社会互动，也不应将其用于医疗、定价、信贷、招聘等高风险自动决策。需要真实标签校准、偏差/公平评估、拒答与人工复核；“多数/中位数”不能纠正共同幻觉或共同训练数据偏差。
- 复现应固定三个数据来源、每类 100 个样本与 seed、单位换算、图像预处理、精确 prompt/context、模型快照、temperature/top-p/max tokens、调用重复次数、数值解析失败处理、API 成本口径；同时报告每任务绝对误差/MRE、rank percentile、置信区间、配对统计与逐样本结果。
- 后续应加入更大且预注册的多模态/非视觉任务、直接 human baseline、更多独立模型/开源权重、误差相关与校准测量、不同聚合器和 token distribution、结构化预测/排序的适当度量，以及带 communication 的动态多 agent 设计。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM agent、ensemble 与 collective intelligence 探索工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/MTWR9974.pdf) 核验三数据集/各 100 样本、三模型与温度设计、中位数聚合、68% 排名结果、context 统计和作者列出的局限；没有把该视觉标量评测表述为对真实群体智慧、模型独立性或一般多智能体协作的验证。
