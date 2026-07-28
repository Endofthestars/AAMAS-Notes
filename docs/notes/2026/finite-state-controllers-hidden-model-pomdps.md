---
title: "Finite-State Controllers for (Hidden-Model) POMDPs using Deep Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/TBFQ5922"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TBFQ5922.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["finite_hidden_model_set_scope", "extraction_fidelity_dependence", "one_hour_timeout", "verified_model_not_real_environment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Finite-State Controllers for (Hidden-Model) POMDPs using Deep Reinforcement Learning

## 一句话总结

Lexpop 先以 PPO/RNN 从模拟交互学习 POMDP policy，再抽取为可模型检验的 stochastic finite-state controller（FSC）；对有限个模型组成的 HM-POMDP，反复把验证得出的 worst-case model 加入训练，优化 FSC 的最坏模型 value。可验证保证属于抽取后的 FSC 与给定模型集，不属于 RNN 或真实环境。

## 方法与证据

- pipeline 是 DRL RNN policy → SIG/Alergia 等 extraction → model-based FSC evaluation；FSC 可精确计算期望/robust value，RNN 不能直接提供此保证（§1、§4--5）。
- RobustLexpop 对 HM-POMDP 的有限 POMDP 集用 deductive verification 找 worst-case POMDP，收集其轨迹迭代 robust PPO，再抽取/验证 FSC（Algorithm 1，§4）。
- 比较 Saynt、rfPG 和 Lexpop；single 与 HM benchmark 包含大状态、sparse reward；实验运行 10 fixed seeds，robust settings 为 1-hour timeout（§6）。
- extraction 有时因 FSC memory limitation 损失 robust value；Alergia 的较大 controller 最坏可令 verification time 增约 6 倍，worst-case-directed training 比随机选模型稳定（§6）。

## 局限与复现

- robust value 是有限 HM-POMDP 枚举中最差模型的 value，不覆盖连续/无限不确定性、sim-to-real、感知误差、执行故障或模型集外扰动。
- 验证的是已经抽取的有限 controller 与模型，不验证黑箱 RNN；提取保真度、controller size、PPO tuning 和 worst-case search 决定最终性能。
- 一小时、10 seed 与特定 Ryzen/JAX 环境的 benchmark 结果不是实时或安全关键部署证明。复现应公开模型、reward、PPO/SIG参数、FSC size、verification backend、seed 与每轮 worst-case trajectory。
- 作者计划以 programmatic controllers 改进 robust loop；安全应用还需验证模型假设及运行期监测（§7）。

## 与 AAMAS 的关系与核验说明

该文连接 POMDP learning、controller extraction 与形式化验证。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/TBFQ5922.pdf) 核对流程、HM-POMDP 定义、实验设置和提取损失；未将模型内 FSC verification 外推为现实世界安全保证。
