---
title: "CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "argumentation_reasoning", "marl_coordination"]
dblp_key: ""
doi: "10.65109/DVBN4652"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DVBN4652.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["synthetic_benchmark_scope", "training_contamination_risk", "single_model_pair", "no_key_ablations", "high_inference_cost", "no_real_world_causal_discovery"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate

## 一句话总结

CRAwDAD 让 Qwen3-32B 与 DeepSeek-R1-Distill-Qwen-32B 对已给定的因果图/概率描述执行 CLadder 的 yes/no 因果问答：第二个 agent 先审查第一个答案，只有初始答案不一致才继续至最多四轮。全量 10,112 条 synthetic benchmark 上，Qwen3 从 84.16% 升至 89.41%，DeepSeek 从 78.03% 升至 87.45%，counterfactual（Rung 3）增益更大；但这不是从真实观测数据发现因果结构，也未证明能处理现实中有歧义、缺数据、未知 DAG 或高风险决策的问题。

## 方法与证据

- CLadder 的每题绑定形式化 causal model，oracle 生成 ground truth；共 10,112 题：Rung 1/2 各 3,160，Rung 3 counterfactual 为 3,792，并包含 common-sense、nonsensical 和 anti-common-sense 表述（§3.1）。因此它测的是**已提供结构与概率条件下**的符号式因果推理，而不是从数据可靠地 learn/discover causal graph。
- 每题随机决定 first speaker。首个 RLM 获得 CausalCoT 风格形式化步骤、背景关系/概率、yes/no 与 confidence 要求；只将其 concise rationale 与 final answer 交给对手，内部 reasoning trace 留作人工分析（§3.2）。
- 第二个 RLM 负责审查而非完整重解；若它同意，答案即结束。若不同意，批评回传 first speaker（round 3）；若 first speaker 坚持，second speaker 在 round 4 给最终答案，即使仍无共识。预实验称更多轮次收益很小，甚至可能使正确率停滞/下降（§3.2）。
- 论文没有 judge，以避免语言模型 judge 的位置/末位偏好并减少开销；同时采用不同 base lineage 的 Qwen3-32B 与 DeepSeek-R1-Distill-Qwen-32B。后者由 Qwen2.5 base 蒸馏而来，并非完全独立家族，所谓 diversity 仍是有限的（§2、§3.4）。
- RLM 不稳定遵循 structured-output 指令时，pipeline 额外用 Granite3.3-2B 抽取 final yes/no 与 confidence；作者只人工检查 50 个随机输出并称抽取均正确。这是有限审计，不是对所有 10,112 条抽取正确性的形式验证（§3.3）。
- Table 1：Qwen3 initial/final overall accuracy 为 84.16%/89.41%，DeepSeek 为 78.03%/87.45%；Rung 3 从 71.53% 至 80.35%、67.94% 至 80.04%。这支持该固定模型对与 prompt 的相对提升，但 final 分别仍有约 10.6%/12.6% 错误（§4、Table 1）。
- 论文还以 500 条 commonsense 子集换用 Yu et al. prompt 做 small secondary check；总体趋势相近，但 Qwen 的 4.6% 降幅显著（\(p=0.007\)）。prompt choice 本身会改变结论，不能把表内提升归为纯 debate effect（§4）。
- Rung 1 有 93% 初始直接同意；约四分之一 Rung 3 会争议。10,112 题中 148 题在四轮后仍无共识，即使都能正确 tie-break 总准确率也只会再增 0.55%（§4.3、Fig. 6）。
- DeepSeek 的 debate response 中 22.60%（1412/6247）不足 100 characters，而 Qwen 为 0.40%（11/5986）；其 debate median 249 vs Qwen 的 739 characters。作者从少量 trace 检查推测这削弱了 DeepSeek 的说服能力，属于解释性观察而非受控因果消融（§4.4、Fig. 7）。
- confidence 不可靠作 early gate：两模型 confidence 从不低于 60%，只依赖 first speaker 的 initial confidence 会使准确率降低 5.7%。因此该系统仍要求每题至少调用两个大模型，并非只在低置信题上廉价辩论（§4.2--4.4）。

## 适用边界与复现

- 不应将 benchmark answer accuracy 标为真实世界的因果效应估计能力。现实问题通常含 noisy/ambiguous language、missing/confounded variables、未知/错误 DAG、selection bias 和 measurement error；系统也没有做 intervention、反事实或政策建议的真实性验证。
- 论文承认 CLadder 生成于 2023 年，2025 发布的模型可能已经训练见过数据；synthetic、整洁、文本格式均一的题目也与实践不同。应生成严格去重/holdout 的新实例、检验 contamination、评估未知图/错误图/缺失概率/干预数据，并用外部因果求解器对可审计计算做交叉验证（§5.2）。
- 全集运行耗时 380 hours。因成本/时间未做 standard LLM substitution、三名以上 RLM、judge、去除 confidence、去除“更自信”指令的消融；仅试一个模型组合且受硬件限制于 32B。故不能判断增益来自模型规模、模型配对、prompt、round cap、confidence 指令或 judge 缺席中的哪一项（§5.2）。
- counterfactual Rung 3 即便辩论后仅约 80%，作者明确说 RLM 目前不能在无外部精确计算工具时被信任来回答此类问题。医疗、司法、科学与公共政策等高风险场景必须由已验证 structural causal model/solver、数据审计、专家审阅、uncertainty reporting 和 human accountability 覆盖，不能用 agent consensus 代替（§4.4）。
- 复现需固定 CLadder revision/全量题目与 Rung/alignment strata、模型权重和量化/VRAM、Ollama/runtime、CausalCoT 与 debate prompts、speaker randomization、temperature/sampling、round-2/3/4 stopping、Granite extractor 与 parse failures、answer/consensus definitions、wall-clock/token/energy、all seeds和 per-stratum accuracy；另预注册 contamination audit 与完整 ablations。

## 与 AAMAS 的关系与核验说明

这是 generative-agent debate 与形式化因果问答工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DVBN4652.pdf) 核对 CLadder 范围、两 agent/最多四轮流程、extractor、模型选择、Table 1、round/response/confidence 分析以及 contamination、synthetic scope、成本与缺失消融等作者限制；没有把对已知合成 causal model 的高分误写成现实因果发现、干预效果预测或可信自动决策。
