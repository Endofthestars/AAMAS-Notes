---
title: "Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MCSD1905.pdf"
preprint_url: "https://arxiv.org/abs/2505.17801"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["simulator_fidelity_dependency", "llm_as_judge", "autonomous_driving_scope", "multi_turn_llm_brittleness"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour

## 一句话总结

AXIS（Agentic eXplanations via Interrogative Simulation）让 LLM 以多轮 `add`、`remove`、`what`、`whatif` 查询驱动多智能体模拟器，观察反事实轨迹后生成动作解释；在作者构建的 10 个自动驾驶场景中，相对仅给上下文的 LLM 基线提升了 LLM 评审的解释正确性，但证据并非真人用户研究或真实道路安全验证。

## 方法与证据

- 问题被定义为：给定 POSG 中用户对某个 agent 动作序列的查询与状态轨迹，产生自然语言 action explanation。方法建立在 counterfactual effect size model：在相近背景条件下，干预后事件是否仍发生，用来筛选更可能的原因（§2–3）。
- AXIS 要求一个近似环境转移与联合策略的模拟器 $\hat T$。LLM 将观察、option 和可选静态环境转成文本，提出干预；模拟器向前执行后返回状态、动作和 reward，LLM 再综合。每轮可用 `add`（增 agent）、`remove`（移除 agent）、`whatif`（在指定时间强制 option）或 `what`（查询状态/动作）；最多 10 轮，也可输出 `DONE` 早停（Table 1、Algorithm 1）。
- 实验使用 IGP2 驾驶模拟器：静态语义道路、车辆通过 A* 或 MCTS 规划。10 个场景最多 5 辆车，包含 5 个理性、2 个非理性和 3 个遮挡场景；每场景最多 3 个自然语言问题。生成模型为 GPT-4.1、o1、DeepSeek-V3、DeepSeek-R1、Llama 3.3-70B（§4）。
- 对照是 ModelOnly（给同样初始上下文、直接要求 LLM 解释）与 NoExp（只用于下游预测的无解释基线）。作者以 Claude 3.5 作为未参与生成的 LLM-as-a-judge，评估偏好、感知正确性以及从解释预测目标/下一动作；并用案例分析、模型/条件扰动与 Shapley context-feature 分析辅助检验（§4）。这不是由人类被试完成的主观偏好或信任测量。
- 聚合结果按各轮中“偏好与感知正确性几何均值最高”的 explanation 选 best round。相对 ModelOnly，5 个生成模型的感知正确性均上升，幅度至少 7.67%、最高 17.83%；4 个模型的 goal prediction 从基线的约 23.73% 相对增至约 46%（最高相对 +23 个百分点），action prediction 改善或相近，但并非每一模型均改善（Table 3、§5.2）。
- 质性结果显示 `remove` 与 `whatif` 常被用于获得因果信息；理性驾驶场景能找到较相关原因。对非理性车辆和遮挡因素，模型往往假定其他车理性或误判遮挡，因而解释不完整（§5.1）。

## 局限与复现

- AXIS 的反事实是否可信，首先取决于 $\hat T$ 是否近似真实环境转移与其他 agent 策略；模拟器不能代表的行为、隐藏状态或干预，不能由语言综合补回。它提供的是模型内反事实解释，不是实际道路因果证明。
- “perceived correctness”、偏好与 actionability 的主体是 Claude 3.5 评审器，不是人类被试；论文也明确指出 LLM 评审和主观偏好存在偏差。只能报告为该评审协议下的结果，不能声称用户信任、理解或安全性已提升。
- 数字依赖于 10 个、最多 5 agent 的驾驶模拟场景、问题模板、best-round 选择、模型版本和 prompt；没有与成熟专用 XAI/MARL 基线的直接比较。跨任务、更多 agent、离散领域或真实车队的可扩展性尚未证明。
- 多轮 prompt history 会暴露 verbosity、过早结束、错误假设与 recency bias；论文观察到某些推理模型虽提高感知正确性，却降低目标/动作预测表现。单次自然语言解释不应作为自动控制、事故归因或合规判定依据。
- 复现应固定 IGP2 场景、option 词表、观测文本化、最大轮数、每个模型的采样配置与 judge prompt；分别报告各场景、各模型、轮数与 `DONE` 行为，保留 simulator 的干预轨迹以检查解释所述反事实是否实际发生。

## 与 AAMAS 的关系与核验说明

该文将可执行模拟和 LLM 语言接口连接到多智能体动作解释，适合研究人机协作中的可审查说明。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2505.17801) 核对 AXIS 的模拟器前提、查询操作、10 场景/5 模型设置、LLM 评审协议与 Table 3 结果；不把评审器得分外推为真人信任、真实世界因果或自动驾驶安全保证。
