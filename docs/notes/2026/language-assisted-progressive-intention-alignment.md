---
title: "Efficient Teammate Adaptation with Language-assisted Progressive Intention Alignment"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "generative_agents", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/HOBH9968"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HOBH9968.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "language_prior_assumption", "simulated_teammates", "benchmark_evaluation", "passive_inference_latency"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Efficient Teammate Adaptation with Language-assisted Progressive Intention Alignment

## 一句话总结

TALP 把未知 teammate intention 当离散假设 \(T\)，以 LLM 将自然语言描述映射成 prior \(P(T)\)，再用观察到的 teammate actions 通过 distilled policy likelihood 更新 posterior；当 entropy 低于阈值时从 intention-agnostic policy 切换到对应 cooperation policy。GridNav/Overcooked 中它优于 FCP、Fastap、VariBAD，precise language 的 Overcooked 分数 49.2 vs 最强 baseline 38.4；这是预定义 intentions/语言和模拟行为分布下的单 episode 适配结果，不是对真实人类意图、语言忠实性或安全协作的保证。

## 方法与证据

- posterior 按 \(P(T|\tau_t)\propto P(\tau_t|T)P(T)\) 更新（Eq. 1）。LLM 将 teammate language 与每个 intention 的高回报 trajectory description 比 semantic similarity，归一化为 prior；若语言错误、含糊、文化不同、恶意或不在离散 intention set，prior 可能系统性误导，而贝叶斯形式本身不保证 calibration。
- true likelihood 须在各 intention 的巨大 teammate-policy space 上积分（Eq. 2），作者为每种 intention 生成 diverse policy population 并以 total-variation distillation 得单个 \(\pi^{G}_{dis}\)，以其动作概率近似 trajectory likelihood（§2）。population coverage、distillation fidelity、policy/action observability 和 teammate 是否遵循训练意图决定 inference 质量；摘要没有给 calibration、posterior error 或 OOD teammates 的量化。
- 推断阶段使用 intention-agnostic ego policy 采证，posterior entropy 小于 \(E\) 后，选择 \(\hat T\) 并切至 intention-aware ego policy（§2）。阈值/commit 是不可逆或难恢复的切换风险；若 teammate 改意图、存在多意图/连续目标、交互短或高动态，错误早承诺会损害协作。作者明确承认被动观察可带来 latency，建议 future inverse dynamics。
- Table 1：GridNav TALP no/vague/precise language 0.535/0.552/0.573；Overcooked 43.9/45.4/49.2，FCP 在 precise language 为 38.4、Fastap 37.7、VariBAD 38.2。文字称精确语言下相对 strongest baseline 28% boost。对 vague language 的例子来自训练/描述格式（如 “bottom” vs “bottom-left”），不能说明任意自然语言或跨语言鲁棒性。

## 适用边界与复现

- 适合研究预定义 teammate hypotheses 下的 zero-shot coordination/intent inference；不应以此推断真实人的目标、偏好、可信度或授权，更不应在医疗、车辆、安保或其他高风险人机协作中基于单一 LLM prior 自动改变行为。
- 复现需给 GridNav/Overcooked environments、intention set/rewards、teammate population generation、distillation loss/TV estimate、ego policies、LLM/model/prompt/description retrieval/semantic similarity、entropy threshold、action histories、baselines、seeds及 intent-classification calibration/CI。测量 language-only、behavior-only和每个模块的消融。
- 应测试 unseen/mixture/changing/adversarial intentions、missing/noisy actions、ambiguous/contradictory/multilingual language、long delays、incorrect posterior recovery和 human teammates；报告 early commitment、adaptation time、worst-case return、trust/overreliance和 uncertainty calibration。部署应让人可更正 agent 的假设，保留保守 fallback和审计记录。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 open MARL、teammate modeling 与 language-assisted coordination 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HOBH9968.pdf) 核验 Bayesian prior/likelihood、distillation、entropy switch和 Table 1；没有把模拟 teammate/基准回报写成真实人类意图识别或协作安全结论。
