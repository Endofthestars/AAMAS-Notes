---
title: "The Monetization Agent: A Deployed POMDP for Maximizing Lifetime In-App Advertising Revenue"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "planning_scheduling", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/WOQF1299"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WOQF1299.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "commercial_deployment", "revenue_optimization_objective", "latent_user_profiling", "two_games_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# The Monetization Agent: A Deployed POMDP for Maximizing Lifetime In-App Advertising Revenue

## 一句话总结

本文将 rewarded in-app advertising 下的 dynamic difficulty adjustment 建模为 POMDP：用 latent player type 表示 skill 与 ad tolerance，以广告 impression 为即时/累计 reward，在玩家 win/loss、看广告、churn 观测下离线规划难度 seed。两款生产游戏的随机对照实验显示，长期广告 impressions 增加 23.6% 与 7.0%，level 300 survival 相对提升最高 204.9% 与 297.3%；但模型的显式目标仍是 lifetime 广告收入，而非用户福祉、知情选择、公平或最小化操纵。

## 方法与证据

- POMDP hidden state 是 latent player type（skill、ad tolerance），observable state 是当前 level 与 trial count；每 trial action 是有限 action set 中的 difficulty random seed，观测 win/loss、rewarded-ad decision 和 terminal churn，reward 为 ad-impression indicator（§2）。因此价值函数优化的是 expected lifetime ad views，不含满意度、消费负担、儿童保护、广告质量/欺诈、accessibility、玩家自主性或长期负面影响。
- 行为结构模型为每 latent type 以 logistic functions 参数化 win、ad watching、churn 概率；先以 segmented win models 和 EM 从 win/loss 恢复 seed-level difficulty，再在估计 difficulty 条件下以 weighted convex logistic regressions 拟合 ad/churn（§2）。direct joint MLE 被称 non-convex，hyperparameters 用 grid search joint likelihood、information criteria 和部分 business constraints 选定。结构化假设可能把相关性当 action effect，且 extended abstract 未给 type count、features、identifiability、propensity/干预、privacy data handling 或 calibration。
- 由于 online POMDP 在大状态和严格延迟下不可行，作者用 learned model 以 POMCP 离线在离散 belief points 求 action，再存为几 MB lookup table；runtime 仅 belief update/table lookup，可 on-device（§2）。这减小 serving compute，不保证模型在分布漂移、广告库存变化、作弊/机器人、policy feedback 或隐私受限 telemetry 下保持最优/安全。
- 两个 industrial-partner games 的 new users 被随机分 control（原 difficulty）或 treatment（agent 管 early gameplay seeds，之后回到同 control mechanism）（§3）。Table 1 以 \((Treatment/Control-1)\) 报：Game A total ads at level 1000 +23.6%、B +7.0%；level 300 survival A +204.9%、B +297.3%，但 level 1 total ads 分别 −11.4%、−77.0%。这是 production RCT evidence，但文章未给样本量、experiment duration、attrition definition、p-values/CI、multiple testing、pre-registration、absolute retention、收入金额、广告频率/时长、玩家年龄/地区或负面体验指标。
- 作者解释 policy 为两阶段：初期不确定且 early churn 高时给较易难度，以留住用户并收集信号；belief 集中后，对 ad-receptive users 提高困难度来诱导广告，同时保护 ad-averse/frustration-sensitive users免于 spike（§3）。后者是模型解释，不是由本文报告的用户研究/因果 fairness audit 验证；“保护”不应与营收增长或 level-survival 指标混同。

## 适用边界与复现

- 适合在有明确用户同意、可退出、广告政策与独立产品治理的环境中研究 POMDP-based DDA；不应直接用于未成年人产品、赌博/高压消费设计、健康/教育干预或以隐藏画像推动曝光的系统。
- 复现需取得 treatment/control assignment、eligibility、sample size/duration、seed action set、level/trial definitions、ad inventory/placement、reward/churn/retention definitions、raw event timing、latent-type model/features/priors、EM/logistic/POMCP configs、belief grid、lookup table、business constraints、all hyperparameter search 与 analysis plan。应报告 ITT、absolute/relative effects、CI/显著性、异质性、missingness、广告量/时长分布、付费/投诉/opt-out和长期复访。
- 应外部验证更多 genres/regions/platforms、冷启动/returning players、广告频率上限、广告质量差异、模型 drift、counterfactual hard/easy policies、latent-type misclassification、targeting对不同年龄/skill/花费群体的差异、玩家主观体验和 adverse outcomes。将收入目标与 retention、满意度、自主性、疲劳、accessibility、privacy、儿童保护和监管约束做多目标/硬约束比较。
- 上线应有显性告知/可控 difficulty 与广告偏好、频率/金额/时间 caps、禁止以脆弱性画像推动曝光、data-minimization/retention limits、独立 A/B 审核、实时 harm metrics、投诉与撤回、版本化 policy logs 和人工 escalation。高 retention 或更多 ad views 本身并不证明玩家获益或设计无操纵性。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的部署型 POMDP、用户交互与数字广告 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WOQF1299.pdf) 核验 hidden type/observation/reward、structural estimation、POMCP lookup policy、两款游戏 RCT、表 1 数值和两阶段解释；没有把 relative ad/retention uplift 写成用户福祉、公平画像、因果机制完整识别或合规性保证。
