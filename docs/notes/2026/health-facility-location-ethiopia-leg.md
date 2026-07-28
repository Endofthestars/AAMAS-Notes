---
title: "Health Facility Location in Ethiopia: Leveraging LLMs to Integrate Expert Knowledge into Algorithmic Planning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "planning_scheduling", "human_agent_interaction"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AIFQ1928.pdf"
preprint_url: "https://arxiv.org/abs/2601.11479"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["health_planning_scope", "synthetic_expert_advice", "llm_alignment_proxy", "coverage_not_health_outcomes"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Health Facility Location in Ethiopia: Leveraging LLMs to Integrate Expert Knowledge into Algorithmic Planning

## 一句话总结

LEG（LLM and Extended Greedy）先用有保证的覆盖优化选 health-post upgrade，再让 LLM 在受限交换内按自然语言建议迭代调整 district allocation；其目标是在保留 population-coverage 下界时提升对定性建议的对齐。

## 方法与证据

- 基础目标是以有限 budget 选候选 health posts/网格，使一小时步行覆盖范围内的人口覆盖 $f(S)$ 最大；$f$ 是单调 submodular coverage。专家建议的对齐函数 $g(S)$ 没有被解析成固定数学目标，而由 LLM 反馈代理（§3–4）。覆盖不等于医疗服务质量、人员/药品能力、利用率、疾病负担或健康结局。
- 初始 greedy 为 max-coverage 提供标准 $1-1/e$ 近似。GuidedGreedy 强制至少 $\lceil\alpha b\rceil$ 个选择具不小于当前最大边际收益 $\beta$ 倍的收益，随后 LLM 提议受限调整；Theorem 4.1/4.2 给出相对 budget-$b$ 最优覆盖的 $(1-e^{-\alpha\beta})$ 下界（多阶段定理对每一阶段保持相同类型保证）（§4、Appendix B）。当 $\alpha=0$ 时该下界退化，不能将“LLM refinement”本身解释为 coverage approximation。
- LEG 的迭代包含 baseline allocation、LLM 依据 advice/coverage 给 verbal 或 quantitative feedback、将建议限制为一次移动一或两个 district allocation units、再调用 constrained greedy 在 grid cell 层选择。LLM 可影响 alignment 与局部重分配，但 budget/覆盖约束由算法结构约束（§4、Algorithms 2–3、Appendix A）。
- 实验使用 Ethiopia projected population 和候选设施/一小时步行覆盖，覆盖 Afar、Somali、Benishangul-Gumuz 三个地区；文中比较不同 $\alpha$ 和 verbal/quantitative feedback 的 10 次迭代，展示 coverage–alignment trade-off 及地图示例（§5、Figures 3、8–9）。这不是上线后的设施建设、患者流量或健康影响评估。
- “multi-stakeholder advice”在实验中是 Gemini-2.5-Pro 生成的 20 条建议，分为四组、每组五条并故意引入矛盾；allocation–advice alignment 亦由 Gemini-2.5-Pro 打分 0–1，迭代调用 Gemini-2.5-Flash（§5、Appendix A）。因此实验证据是 LLM-to-LLM 对齐代理，不是与独立 Ethiopian planners 的盲评或偏好学习。
- 作者报告 coverage 随 $\alpha$ 增大通常更高而 advice alignment 更低；Afar 的 $\alpha=0.25$ 例外显示仅靠保证参数并不完全预测经验表现。文中还指出 advice 可偏好现有健康状况/公平性，从而主动牺牲总 coverage（§5.2–5.3）。

## 局限与复现

- 健康设施选址是高风险决策。模型未验证临床质量、可达性的季节性/安全性、道路和交通、设施容量与人员、预算成本、行政可行性、政治公平、数据缺失或受影响社区同意；产出只能作为规划讨论输入，不能直接决定升级名单。
- 近似保证只覆盖定义的人口 coverage 函数及 $\alpha,\beta$ 的算法条件；它不证明 LLM 理解建议、alignment score 有效、分配公平、或实际卫生结局改善。低 coverage 的“人类偏好”调整需要由具授权的专家审查。
- 用 Gemini 同时产生 advice 和评分会带来共模偏差、prompt sensitivity 与模型版本漂移；没有替代 LLM、人类专家一致性、反事实/历史政策、或真实部署比较，不能把高 alignment 视为 stakeholder acceptance。
- 复现应固定人口栅格、候选站点、步行时间/coverage 半径、地区边界、budget、$\alpha/\beta$、所有 prompts 与 Gemini model/version、每轮 allocation/coverage/advice-score；并加入独立专家盲评、弱势群体分层覆盖、成本/容量约束与对历史选址的外部验证。

## 与 AAMAS 的关系与核验说明

该文将 submodular planning 与 LLM 解释自然语言建议结合，应用于公共卫生设施升级。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2601.11479) 核对 LEG、Theorems 4.1–4.2、三地区数据、参数 trade-off 与实验 advice/score 的生成方式；不将模拟 LLM 对齐结论夸大为真实卫生政策效力。
