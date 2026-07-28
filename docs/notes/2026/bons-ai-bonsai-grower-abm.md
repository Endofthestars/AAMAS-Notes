---
title: "Bons-AI: An Agent-Based Model to Evaluate the Behavior of Bonsai Grower According to Different Levels of Communication and Experience"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "marl_coordination", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/UHQU6299"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UHQU6299.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["parameterized_abm_only", "simplified_biological_model", "ten_repeat_simulation", "no_real_horticulture_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Bons-AI: An Agent-Based Model to Evaluate the Behavior of Bonsai Grower According to Different Levels of Communication and Experience

## 一句话总结

Bons-AI 以 bonsai biological-state agent 与带不同经验的 grower agent 构成 ABM，grower 以 Q-learning、规则化气候/操作和 master–apprentice Q-table 分享进行护理；在该模拟中沟通降低死亡、改善健康，但这是模型参数下的 social-learning 现象，不是对真实盆景栽培的实证建议。

## 方法与证据

- 模型含 30 棵 bonsai 与单 grower，动作包括 pruning、wiring/unwiring、watering、fertilizer 与 repotting；health/style 由季节、气候和规则化生物状态更新（§3--4）。
- 比较无知识、autonomous Q-learning 与 master–apprentice；沟通触发条件是 bonsai health ≤50，信息经 Q-table 传递，经验类别含 0--30 年（§4--5）。
- 每 scenario 运行 10 次、10 年，死亡后不替换；记录 mortality、health 与 style。论文称 5-year experience 的 communication scenario mortality 降 18.04%、health/lifespan 增 9.5%，经验也改善 style 保留（§5）。
- 15 与 30 年经验的 health 差异较小，且较多 rounds/learning period 才出现更有效策略，表明结论对 training duration 和规则敏感（§5--6）。

## 局限与复现

- “树健康”、季节、肥料、水分、pruning 效应和经验都是模型设定；30 株、单 grower、10 次重复无法验证真实物种、生长介质、病虫害、人工操作差异或跨文化师徒传承。
- Q-table communication 只是窄的信息共享机制，不能代表语言教学、误解、社会关系、成本或隐性知识。百分比结果不可外推为真实死亡率。
- 复现应公开源码、所有状态转移/奖励/阈值、气候序列、随机 seed、每次 run 数据和 sensitivity analysis；应与真实园艺专家/长期观测作外部验证。
- 作者计划增加风格、物种、生物特征与更复杂的沟通/学习机制（§6）。

## 与 AAMAS 的关系与核验说明

该文把非传统栽培情境作为 heterogeneous expertise 与社会学习的 ABM 测试床。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UHQU6299.pdf) 核对 agent、实验规模、结果和未来范围；未将模拟结果当作园艺、生态或健康建议。
