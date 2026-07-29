---
title: "AI Alignment Via Power-Mean Elicitation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["norms_trust_governance", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: "10.65109/UAUY5393"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UAUY5393.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "power_mean_family_assumption", "fixed_group_weights", "anchoring_sensitivity", "prompt_sycophancy", "synthetic_social_dilemmas", "not_alignment_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# AI Alignment Via Power-Mean Elicitation

## 一句话总结

该文把一个决策者对群体 disutility 的“malfare”假设为已知群体权重下的 power mean，并以比较式社会困境通过近似二分搜索估计未知 (p^*)；理论给出该受限函数族中的对数查询复杂度，但 LLM 实验发现估计强烈受初始搜索端点影响，同一场景可表现为近似 utilitarian 或更 egalitarian，因此它更像检测/量化语境敏感社会偏好的工具，而不是已经让模型与稳定人类价值对齐的方法。

## 方法与证据

- 假设 outcome 对每个群体产生非负 disutility \(s_g\)，真实聚合函数属于 weighted power-mean family \(W^*(o)=M_{p^*}(s;w)\)，其中 group weights \(w\) 已知、\(p^*\ge1\) 未知（§2）。(p) 的含义从更 utilitarian 到更 egalitarian 的特定 malfare 聚合轴；它不能表达权利、程序正义、个体不可比性、因果责任、约束/禁忌、动态不确定性或人类价值的全部结构。
- Approximate Search with Binary Queries（ASBQ）让 actor 反复在两个 outcome 间选偏好，以获得 \(\epsilon\)-近似 power mean。论文以 outcome-space 的 supremum distance 和其 additive upper bound，而非直接 \(p\) 参数距离，导出 minimax query complexity 的上下界，并在 uniform groups、大 group limit 下给出 \(\Theta(\log(\log(p/q)/\epsilon))\) 级别结论（Theorem 2.3，§2）。该定理前提是回答可被一个固定真实 power mean、一致比较和已知 (w\) 描述；不会保证对不稳定或策略性回答者收敛到“真实价值”。
- 实验模型是 GPT‑4.1（`GPT-4.1-2025-04-14`）、Gemma‑3‑27b-it、Llama‑3.3‑70B-Instruct、Llama‑4‑Scout‑17B‑16E-Instruct，temperature 0；以 \(\epsilon=10^{-4}\) 进行 100 次、从 \(p=1\) 初始化的实验（§3）。每轮固定 group weights、按回复生成 outcome pairs，并通过变动 weights 观察同一 scenario 的 contextualized preference。
- 作者称平均不超过 10 个 query、总数不超过 25 个即可找近似值（§3）。这衡量搜索在模型给出回答后的数值收敛，不等价于对人类偏好、模型内在规范或真实部署行为的 sample-efficient/faithful inference；文本未给所有 prompts、scenario generator、response parser、API/seed、失败/拒答率、置信区间或独立人工校验。
- 关键负面结果是初始化依赖：disaster-relief 场景从 \(p=1\) 开始时各模型趋近 utilitarian power means，而以 \(p=\infty\) 开始时趋于更 egalitarian（Figure 1、§3）。作者认为早期生成的情境使模型“stick”于初值，可能与 sycophancy 有关，并建议加入随机 social dilemmas 的噪声来缓解 anchoring；这直接反驳 H1 所期待的稳定一致 elicitation。
- H2（不同 LLM 有相近 malfare concepts）也被拒绝：灾害场景中 Llama 3/Gemma 3 更 utilitarian，Llama 4 更 egalitarian（§3）。这些是对特定 prompt/template 下选择行为的描述，不是对模型固有道德观、实际政策、对齐程度或哪种价值观更正确的验证。该文为 Extended Abstract，缺少完整理论证明/实验附录和跨文化/人类对照。

## 适用边界与复现

- 可用于受控机制设计/社会选择研究中探测一个明确、固定 power-mean 假设是否能解释二元 comparison choices，或作为模型 prompt/context 稳定性的 red-team signal；不可把单一 \(p\) 当成人类/社会偏好、组织治理原则、模型 alignment score 或可直接用于资源/生命/权利分配的决策规则。
- 复现要公开 outcome/disutility generator、所有 social-dilemma wording、group definitions/weights、initial intervals/initial endpoints、ASBQ stop rule/\(\epsilon\)、模型 snapshots/decoding/seed、100-run 原始 choices和估计轨迹、解析方法、每种 scenario/context 的完整分布。应独立验证 Theorem 2.3 的条件、查询复杂度和数值精度，而非只复画累计 histogram。
- 必须加入 counterbalanced/no-anchor/randomized order、prompt paraphrase/多语言、不同 group identities/人数/weights、inconsistent/abstaining answers、persona/system instructions、long dialogue、tool-mediated action、human participants与伦理审查。对模型使用的“噪声”不能掩盖不稳定性；应区分测量误差、上下文敏感偏好和被诱导回答。
- 高风险 alignment/evaluation 中，要以多主体、可申诉的规范程序与独立安全限制为主，比较查询只能提供诊断证据；不得将估计值直接编译成行动 policy。任何报告都应披露 power-mean 价值假设、prompt 初值敏感性与受影响群体，避免把数学收敛误表述成价值合法性或安全保证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的偏好 elicitation、社会福利/公平聚合与 alignment 诊断论文，且为 Extended Abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UAUY5393.pdf) 核验 power-mean 假设、ASBQ/距离与 Theorem 2.3、四个 LLM、\(\epsilon=10^{-4}\)/100-run 设置、初始化 anchoring、H2 被拒绝及作者提出的随机 dilemma 缓解；没有将理论上的受限族查询界或提示下的选择结果夸写为 AI alignment、社会价值真实性或可执行治理机制。
