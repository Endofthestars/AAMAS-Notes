---
title: "Explaining Agent Intentions"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["human_agent_interaction", "safety_verification", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/XMCQ3388"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XMCQ3388.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05e"
spark_draft_verdict: "source_grounded_draft_needs_revision"
spark_qa_verdict: "needs_revision_novelty_attribution_corrected"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_program", "explainable_agency", "frequentist_intention_attribution", "hypothesised_desire_not_ground_truth", "prior_work_application_only", "illustrative_explanations_not_system_output", "reliability_metric_not_defined", "potential_intention_in_progress", "inter_intention_graph_future_work", "no_user_or_causal_validation", "llm_explainability_open_question"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_intention_attribution_causality_reliability_prior_work_and_future_work_boundary_check"
escalation_verdict: "pass_after_ground_truth_reliability_illustration_and_novelty_boundary_revision"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Explaining Agent Intentions

## 一句话总结

这篇 Doctoral Consortium 文稿以 causality、conversationality、teleology 和 ladder of intentions 组织 Explainable Agency，并回顾基于观测构造的 Intention-aware Policy Graphs；当前研究计划试图解释多意图选择和优先级，但 potential intention 仍在进行中，意图关系图与策略干预仍是未来工作，本稿没有新的实验、可靠性指标、ground-truth intention 或用户验证。

## Explainable Agency 的框架

作者将 causality 与 conversationality 列为解释系统的两项基本属性，并依据引用工作把 teleology 定位为 XAg 的第三支柱。ladder of intentions [6] 以 BDI concepts 将 agent architecture 从 designer intention 到 executed action 分层，不同层回答 action、policy、desire 和 intention-prioritisation 问题（§1，pp. 4023–4024）。

这些是本文采用和引用的解释框架，不是本稿通过实验验证的新性质。作者进一步以 “to the best of our knowledge” 限定地声称，XAg literature 尚无方法处理 multi-intention reasoning 的 explainability queries；本笔记将它保留为作者的文献判断，不写成已证实的全领域首创结论。

## Intention-aware Policy Graph

IPG 是先前工作 [5] 引入的 post-hoc 方法。它从 agent 与环境交互的 observations 以 frequentist 方式构造概率图：

- node 对应 discretised state \(s\)；
- edge 表示执行 \(a\) 后从 \(s\) 到 \(s'\) 的联合概率

\[
P(s',a\mid s)=P(a\mid s)P(s'\mid s,a).
\]

一个假设会引导 agent 行为的 desire \(d\)，被形式化为在 desirable state region
\(S_d\) 中执行 desirable action \(a_d\)。从 \(s\) 出发的 intention
\(I_d(s)\) 是所有最终到达 \(s'\in S_d\) 并执行 \(a_d\) 的 state-action paths 的概率和。

因此，IPG 能安全地表述为：相对于预先定义或 hypothesised desire，基于观察给出概率化的 intention attribution 与 purpose-oriented explanation。这个量不是 agent 真实心智状态的 ground truth，也没有在本稿中被验证为 causal effect 或 faithful causal explanation（p. 4024）。

## 既有自动驾驶应用

作者称先前工作 [22,23] 已将 IPGs 应用于使用 real driving scenes 数据的城市自动驾驶，以做 intention attribution、全局/局部目的导向解释和 anomalous or undesirable conduct 识别。

当前三页稿没有复述这些工作的 dataset size、split、protocol、metrics、baselines、统计结果或实现细节。因此可以记录作者对 prior work 的归纳，不能把被引用论文的实验结果算作本稿的新验证。

## Figure 1 与 reliability 的证据边界

Figure 1 描绘 AV 变道过程中另一辆车进入其轨迹的情境。文中的两类自然语言解释分别由 “the explanation might indicate” 和 “the AV response would be” 引导，是 conditional illustrations，不是可确认的系统生成输出，也没有用户研究证明读者理解或接受这些解释。

作者称方法可以“with a quantifiable degree of reliability”识别行为背后的 motivation，但本稿没有给出：

- reliability 的公式或指标定义；
- 数值结果、阈值或不确定性；
- ground-truth intention；
- 用户研究；
- faithfulness 或 causal validation；
- baselines、统计检验或复现协议。

因此这里只能报告作者称该可靠性“可量化”，不能说它已经被测量、验证，或等同于忠实、因果正确、可理解和可信。

## 当前进行中的第三层解释

作者将现实问题定位为：agent 可能在一段 action sequence 中同时追求多个 intentions，或依据 global/contextual priorities 和 desires 之间的关系进行取舍。in-progress work 试图达到 ladder 的第三层，解释 agent 为什么形成和选择某个 intention，以及 desire priorities 为什么影响选择。

当前 \(I_d\) 同时受 agent action choice \(P(a\mid s)\) 和 environment dynamics
\(P(s'\mid s,a)\) 影响，因而把 motivation/desirability 与 feasibility 混在一起。ongoing work 提出 potential intention：

\[
PI_d=\text{agent 若能在 desire 达成前选择所有 actions 时可达到的最大 }I_d.
\]

这是来源中的进行中定义与研究目标；三页稿没有算法、估计方法或结果证明它已经完成 desirability–feasibility disentanglement。

## 未来工作

作者计划从 active intentions 提取 general/contextual priorities，并构造 inter-intention graph，表示：

- independence：追求 \(I_i\) 不影响 \(I_j\)；
- conflict：追求 \(I_i\) 阻碍 \(I_j\)；
- facilitation：追求 \(I_i\) 帮助实现 \(I_j\)。

作者还计划用 potential intention 识别相对 desires 的 suboptimal actions，并干预 graphical model 以改善行为。这些均为 future work，本稿没有实现、policy intervention 或行为改进实验（p. 4024）。

## LLM explainability 开放问题

文稿讨论 LLM component 的 next-token-prediction training objective 可能限制 input–output causal threads 的可靠性，并提出两个待探索问题：LLM components 如何影响 explanation reliability，以及人工 agent 的可靠解释是否总能提供。本文没有 LLM model、prompt、dataset、实验或经验结论。

## 复现与评测缺口

本稿没有新的数据表、代码、模型参数、路径概率估计细节、离散化方法、误差界、消融、human-subject protocol 或 ground-truth intention 标注。它是一份将既有 IPG 工作、当前 thesis 任务与未来方向连接起来的研究计划，而不是闭环评测论文。

页码依据原始 PDF 换页和页脚核对：extended abstract 开端与 Figure 1 在 p. 4023；ladder 后续、IPG、既有应用、in-progress/ongoing/future work 与 LLM 开放问题在 p. 4024；References 在 p. 4025。

## 与 AAMAS 的关系与核验说明

该工作把 Explainable Agency、BDI intention reasoning、多目标优先级和自动驾驶解释连接起来。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XMCQ3388.pdf) 核对 IPG 定义、prior-work 归属、Figure 1 的示例性质、potential intention 与未来方向；`reviewed` 仅表示这些来源主张及其缺口已核验，不代表模型可靠性或解释质量已经验证。
