---
title: "Faithful Language-Based Explanations for Decision-Making Agents"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["human_agent_interaction", "safety_verification", "agent_engineering", "generative_agents"]
dblp_key: ""
doi: "10.65109/YSGJ1412"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YSGJ1412.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-04y"
spark_draft_verdict: "source_grounded_draft_pass"
spark_qa_verdict: "pass_after_usability_faithfulness_and_future_rationale_revision"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "policy_level_rl_summary", "llm_generated_explanations", "feature_attribution_alignment", "counterfactual_proxy_boundary", "self_consistency_vs_faithfulness", "preference_optimization", "future_inference_time_control", "limited_quantitative_reporting"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_faithfulness_proxy_internal_reasoning_and_future_work_boundary_check"
escalation_verdict: "pass_after_attribution_alignment_and_inspectable_rationale_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted faithfulness-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-29"
---

# Faithful Language-Based Explanations for Decision-Making Agents

## 一句话总结

本文把博士研究组织为两条互补路线：用 LLM 把 RL agent 的多条轨迹抽象成全局策略文本，再以“决策与解释的特征归因分布对齐”操作化解释忠实性；专家一致、用户偏好、任务准确率和 attribution alignment 是不同证据，后者也只是代理指标，不能视为直接读取模型内部推理。

## 问题：语言可读不等于忠实

序列决策行为从长时交互中形成，单步 saliency、少量 trajectories、rules 或 decision-tree surrogates 往往只给局部片段，用户仍需自行拼接 agent 的全局策略、目标和失败模式。自然语言可以提供高层抽象，但 fluent、persuasive explanation 可能与真正影响决策的因素不同，反而制造虚假的理解感（§1，p. 3984）。

论文因此区分两个目标：

- **Human-usable**：解释是否连贯、可读、容易形成策略级理解；
- **Faithful**：解释强调的因素是否与模型决策依赖的因素一致。

前者不能作为后者的替代证据。

## 路线一：[2] RL policy-level textual summary

作者把 policy interpretation 改写成跨多条 trajectories 的语言生成问题，目标是总结 recurring strategies、goals 和 characteristic failure modes，而不是逐状态解释（§2，pp. 3984–3985）。

概述给出的流程是：

1. 从 agent 的 experience buffer 收集行为经验；
2. 将经验转成 structured natural-language representations；
3. 用 LLM 做 hierarchical summarization，以处理 long-horizon 输入；
4. 生成多个 candidate summaries，再聚合为 consensus description，降低语言生成波动。

概述称，经验评估中这些摘要与 expert-written analyses 高度一致，并且用户相对于 demonstration-based explanation baselines 表现出强偏好（§2，p. 3985）。这里没有给环境、agents、模型、专家和用户数量、评分协议、偏好比例、方差或显著性。

这些结果支持摘要在所测设置中的可理解性、专家内容一致和主观偏好；它们不证明摘要忠实捕获了 policy 的实际决策依据，也不保证少见但关键的 failure behavior 不会在抽象过程中丢失。

仓库内已有 [From Actions to Words: Towards Abstractive-Textual Policy Summarization in RL](./actions-to-words-sysllm.md) 的完整论文独立笔记；本节只记录博士概述明确转述的流程与定性结果。

## 路线二：[1] 决策—解释归因对齐

### 操作定义

作者把 faithfulness 定义为：

> 驱动模型决策的特征，与解释文本所强调特征之间的 alignment。

具体做法是分别为模型 output 和对应 explanation 计算 feature-attribution distributions，再比较二者。它把忠实性从“听起来合理”转为可测的 decision–explanation alignment（§3，p. 3985）。

该框架使用 counterfactual interventions 估计 feature influence，但这类 attribution 计算昂贵。更重要的是，counterfactual attribution 仍是依赖干预设计、特征表示和 attribution method 的操作代理；它不提供模型内部真实 reasoning process 的 ground truth。论文也指出，许多所谓 faithfulness metrics 实际捕获的是 self-consistency，而 self-consistency 与 faithfulness 并不等价。

### Benchmark 与报告结果

作者称构建了连接 model decisions、diverse explanations 和 attribution vectors 的 large-scale benchmark，覆盖多个 datasets、attribution methods 和 model families。三页稿没有列出它们的名称、版本、样本量或配置。

概述报告三项实验结果（§3，p. 3985）：

- decision–explanation alignment 与 task accuracy 大体正交；
- ranking-based metrics 比 magnitude-based measures 提供更可靠的 alignment signal；
- 在所测设置中，preference-based optimization 改善了这一操作化 faithfulness 指标，且未观察到 task-performance degradation。

这些是概述转述的测量结果，但没有数值、效应量、置信区间、显著性或消融。它们不能推广成所有模型中 alignment 与 accuracy 都无关，也不能证明 preference optimization 一般不会损害性能。

## 六种证据不能互换

| 维度 | 实际回答的问题 |
|---|---|
| Fluency | 解释是否自然、连贯 |
| User preference | 用户在给定比较中更喜欢哪种呈现 |
| Expert agreement | 摘要内容与专家分析是否接近 |
| Task accuracy | 模型任务答案或行为是否正确 |
| Self-consistency | 输出、解释或不同评估过程是否彼此一致 |
| Attribution alignment | 决策与解释的特征归因分布是否对齐 |

Fluency、偏好和专家一致支持 usability/plausibility；task accuracy 衡量任务表现；self-consistency 与 attribution alignment 是另外的关系指标。没有一个维度单独证明解释揭示了真实内部推理。

## 未来方向

### ReThink：固定 policy 上的推理时改进

计划让已有 policy 生成 candidate actions 或 trajectories，再由 LLM 根据任务推理和约束进行评价、排序或改进，从而在不额外训练原 policy 的情况下研究 inference-time performance improvement（§4，p. 3985）。

语言化 deliberation 可以产生可检查、可诊断的 intermediate rationales，但“可见”不等于“忠实 by construction”。ReThink 在本稿中没有算法、实验或性能结果，也没有证明 LLM 选择与固定 policy 的真实因果依据一致。

### Preference optimization 的 stability 与 locality

另一计划是显式约束模型偏离 reference model 的程度，研究小规模 preference-data 或 optimization changes 引起的大幅行为漂移，并尝试使更新更 stable、interpretable 和 behaviorally consistent（§4，p. 3985）。

这些是研究目标，不是已建立的稳定性、局部性或行为一致性保证。

## 证据与复现边界

- [2] 是 policy-level summary，[1] 是 attribution-alignment benchmark 与优化；本三页稿把两者整合为博士路线，但不重新给完整实验。
- 没有具体模型、数据集、attribution variants、样本和用户数量、评价说明、分数、统计检验、代码/数据链接、counterfactual 查询成本或 preference-optimization 目标。
- Attribution alignment 依赖 proxy validity；需要对特征定义、干预、归因稳定性、反事实合理性和跨方法一致性做敏感性分析。
- 用户更喜欢某种解释、解释更流畅或 intermediate rationale 可被检查，都不能替代忠实性核验。

## 与 AAMAS 的关系与核验说明

本文连接 explainable RL、LLM explanations、人—agent 协作、agent supervision 与安全核验。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YSGJ1412.pdf) 核对 §2 的摘要管线和定性评估、§3 的操作定义与三个结果、§4 的两项未来工作；未把 attribution proxy、self-consistency 或 inspectable rationales 写成内部推理真值。
