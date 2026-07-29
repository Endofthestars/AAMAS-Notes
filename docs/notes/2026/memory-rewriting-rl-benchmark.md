---
title: "Memory Retention Is Not Enough to Master Memory Tasks in Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/SOSN3643"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SOSN3643.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "pomdp_memory_benchmark", "memory_rewriting", "selected_architecture_baselines", "not_general_architecture_ranking"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Memory Retention Is Not Enough to Master Memory Tasks in Reinforcement Learning

## 一句话总结

本文提出把 partial-observability 下的“memory rewriting”单独压测：Endless T-Maze 的每段新 cue 使旧方向失效，Color-Cubes 中 cube teleport 迫使 agent 更新内部 map。所测 PPO-LSTM、FFM、GTrXL、SHM、MLP 的 rewriting hierarchy 是 PPO-LSTM > FFM > GTrXL > SHM > MLP，作者归因于 explicit/adaptive forgetting；这说明这些任务和训练设置下，稳定保存不足以处理持续失效的信息，并不证明 LSTM 普遍优于 transformer/structured memory，也不验证真实机器人记忆安全。

## 方法与证据

- Endless T-Maze 由连续 corridors组成，每段开头 binary cue指示将来 junction left/right；turn后 cue变化并使之前信息失效。它把“保留旧 cue”构成错误，测试更新频率随 corridor count增加的能力（§2）。该环境是合成 navigation，不含真实感知、长期任务多义性或 noisy instruction semantics。
- Color-Cubes 是 \(G\times G\) grid，phase初见 colored cubes positions+target，随后观测隐藏；target cube到达后 teleport，non-target cubes也可能随机 teleport。Trivial \(N=K=1\)、Medium有multiple cubes/full updates、Extreme为positions-only/color hidden的incomplete updates。性能既取决于 exploration/navigation/reward design也取决于 memory rewriting，不能单独归因于遗忘门。
- comparisons覆盖 recurrent PPO-LSTM、Fast and Forgetful Memory (FFM)、GTrXL、Stable Hadamard Memory (SHM)、MLP。Figure 3在 Endless T-Maze validation interpolation/extrapolation、same corridor lengths/fixed sampling但 varying corridors报告 success mean±sem；摘要没有完整 curves/numerics、seeds/compute/model sizes、hyperparameter tuning、learning curves、Color-Cubes table或 statistical tests。
- authors’ architecture analysis：PPO-LSTM有 learnable forget gate；FFM有 rule-based replacement；GTrXL gating在部分情景generalizes；SHM缺 explicit forgetting。PPO-RNN ablation及与PPO-GRU gates comparison被称支持 adaptive forgetting，然而 architecture parameterization/optimization/scale differences仍是混杂因素。
- 论文建议 future memory mechanisms要平衡 retention与controlled transformation。它不提出已验证的 universally optimal forgetting rule，也没有 clinical/cognitive claim、human memory comparison或 real-world continual-learning deployment.

## 适用边界与复现

- 适合诊断 POMDP agent 是否能在旧信息失效时更新 belief；不可依据 single benchmark ranking选择安全关键机器人、医疗、金融或 autonomous system memory architecture。部署需观测可靠性、uncertainty/state-estimation、fallback与安全监控。
- 复现需发布 environment source/versions、T-Maze corridors/cues、Color-Cubes \(G,N,K\)/teleport distributions/observability、reward/horizon、all model implementations and parameter counts、PPO hyperparameters/training budgets、interpolation/extrapolation splits、seeds/raw success and CIs。应分别测 retention and rewrite tasks以确认 tradeoff。
- 应测 different update rates、stochastic/contradictory cues、longer horizons、OOD layouts、partial/noisy observations、catastrophic forgetting、external memory and modern transformers at equal compute。报告 probe-able state belief、stale-memory error、adaptation time、worst-case failure而非仅成功率。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 RL memory benchmark 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SOSN3643.pdf) 核验两类任务、Trivial/Medium/Extreme条件、baseline ranking、Figure 3 和 forgetting-gate解释；没有将相对baseline表现外推为所有记忆架构结论。
