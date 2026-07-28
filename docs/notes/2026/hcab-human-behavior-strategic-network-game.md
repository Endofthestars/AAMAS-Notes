---
title: "Modeling Human Behavior in a Strategic Network Game With Complex Group Dynamics"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "marl_coordination", "applications"]
dblp_key: ""
doi: "10.65109/NQKD4743"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NQKD4743.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_strategic_game_scope", "small_human_dataset_and_groups", "user_study_power_and_experienced_sample", "population_match_not_individual_or_causal_validity"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Modeling Human Behavior in a Strategic Network Game With Complex Group Dynamics

## 一句话总结

本文在 Junior High Game (JHG) 中比较行为匹配/社区感知模型与均值/分布参数学习；hCAB-EPDM 最接近训练外小群体的人类 population metrics，并在极小用户研究中难被识别为 bot，但这只说明特定游戏内的表面行为拟合，不能解释或预测一般人类社会网络。

## 方法与证据

- JHG 是 token give/keep/take 产生动态有向加权符号网络与 popularity 的策略游戏。作者比较 hTFT/hCAB 参数化与 PSO/EPDM 两种学习，EPDM 表示人类参数分布而非单一均值（§2--4）。
- population test 使用 335 个 human player games，平均 24.96 rounds、6--11 人（平均 7.93），超过 30 rounds 截断；按测试 games 的人数/回合做每模型 60 次模拟，以 popularity/Gini、行动比例、reciprocity/density/entropy/polarization 和 Mahalanobis distance 比较（§4）。
- hCAB-EPDM 的 Mahalanobis distance 为 3.393，论文的 Chi-square 对比得 `p=0.486`；其它模型 `p<0.001`。但文中也报告其 evolution coefficient 与人类不相似，故不是所有动态均得到拟合（§4、表 2）。
- 用户研究仅 8 名已有 JHG 经验者，四期组成含 4 人/4 hCAB 的 8 人游戏，共 8 games，分析前 15 rounds；对 associates 的人/bot 正确识别率 56.7%，而知晓构成下随机为 57.1%（§5、表 4）。

## 局限与复现

- 训练和验证都是 JHG 的具体激励、动作与 popularity 更新规则；拟合不等于真实社会的因果决策、文化差异、伦理、财富/健康/欺凌结果或干预效果。
- 样本仅小组、有限 games 和有经验用户；8 人 user study 没有支持广泛“human-like”或欺骗能力结论，且接近随机的识别率不等同于统计证明不可区分。
- population aggregate match 可掩盖个体策略、跨回合变化与少数群体失配；作者明确发现 evolution coefficient 不匹配。模型的 hand-coded CAB mechanism、参数搜索、截断和 metric choice 均会影响结果。
- 复现应锁定 JHG version、335-game split、所有参数/PSO/EPDM seed、60 simulation protocol、Mahalanobis covariance/检验、user-study 招募/告知/分析窗口，并在新文化、未经验玩家、更大群体、预注册实验下独立评估。

## 与 AAMAS 的关系与核验说明

该文研究战略网络游戏中的人类行为生成模型。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NQKD4743.pdf) 核对数据规模、表 1--4、hCAB-EPDM 结果和用户研究；未把 JHG 中的拟合外推为通用人类网络行为模型。
