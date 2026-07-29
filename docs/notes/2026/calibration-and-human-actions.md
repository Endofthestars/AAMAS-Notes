---
title: "Does Calibration Affect Human Actions?"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "safety_verification", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/YHRI7310"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YHRI7310.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "human_study_scope_unclear", "correlation_not_decision_quality", "prospect_theory_parameter_dependency", "loan_decision_context"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Does Calibration Affect Human Actions?

## 一句话总结

本文研究 non-expert 面对 classifier confidence 时，普通 calibration 是否改变信任和行动。它在 rain forecasting 与 loan approval HCI 场景中比较原始、isotonic-calibrated、以及以 prospect-theory probability weighting inverse 修正后的分数；只有“calibrated + prospect correction”显著提高 participant action 与 model prediction 的相关性，而自报信任在非随机条件间无显著差异。该结果说明显示概率需考虑感知偏差的可能性，不证明更高 reliance 必然更正确、更公平或适合高风险信贷/医疗决策。

## 方法与证据

- calibration 问题是 predicted probability \(p\) 是否约有 \(p\) 比例发生；论文使用 neural network 原始概率和 isotonic regression calibration（§1）。这种统计 calibration 是总体/数据分布性质，不能单独说明给某一用户的 recommendation 是否解释充分、可行动、因果有效或无偏。
- prospect layer 使用 Kahneman–Tversky weighting \(w(p)=p^\gamma/(p^\gamma+(1-p)^\gamma)^{1/\gamma}\)，对 calibrated probability 用 \(w^{-1}\) 的近似作显示转换，分别提及 gain/loss 可有不同 \(\gamma\)（§2）。文中在 \(p=0,0.01,\ldots,1\) 上报告 \(w^{-1}(w(p))\) 的 MAE 0.00963；该是数学近似误差，不是对具体参与者或人群 probability perception 的校准验证。
- between-subject design 的五条件是：Uncalibrated、isotonic Calibrated、PT-calibrated、PT-uncalibrated，以及显示与 PT-calibrated 相同 probabilities 但 outcomes randomized 的 Random control（§3）。Random 用于测试是否是 predictive accuracy 而非显示概率分布造成效果；它并未控制所有 demand effects、interface、domain familiarity、financial stakes、feedback learning 或对概率语言的理解。
- 两个 domain 是 rain forecasting 与 loan approval；metrics 为 mean self-reported trust 和每 participant 的 action rating 与 system prediction correlation，之后 average；用 one-way ANOVA、\(\alpha=0.05\) 比较（§3）。摘要/正文没有参与者数量、招募/人口统计、任务奖励/真实后果、question wording、model accuracy/calibration values、\(\gamma\) fit source、effect sizes/CI、ANOVA assumptions/multiple comparisons 或预注册，限制可复现性和外推。
- 结果称 PT-calibrated 在两 domain 都比其它方法有更高且显著的 decision-prediction correlation；isotonic-only 与 uncalibrated 非常相似，rain 略升/loan 略降；Random correlation 明显低。除 Random 外 trust ratings 无显著差异（§3–4）。Correlation 增加可表示更随从 model，也可能是 inappropriate automation reliance；本文没有测 decision accuracy、expected utility、calibration of participant beliefs、公平/差异影响、拒贷伤害或长期信任。

## 适用边界与复现

- 可作为人机概率沟通和 perceived-probability calibration 的探索性实验设计，适用于低风险、可撤回的 decision-support research；不应直接将 PT-transformed score 用于授信、保险、医疗、刑事风险、招聘或其他会影响权利/资源的自动决策。
- 复现应公开 rain/loan scenarios、model training/test data与原始/校准 reliability curves、isotonic implementation、\(\gamma\) by gain/loss、inverse approximation、完整界面/行动与信任题目、assignment/randomization、sample/exclusions/demographics、incentives、outcome generation、participant-level actions、ANOVA/post-hoc/CI/effect sizes与所有 seeds。分别报告 score distribution、participant subjective-probability elicitation和真正 decision utility。
- 应在不同文化/数理素养/风险偏好/无障碍群体、真实与有后果的决策、不同 base rates/uncertainty/解释样式、longitudinal feedback、adversarial/miscalibrated models、group fairness与 abstention/second-opinion conditions 下测试。比较 direct probability education、natural frequencies、uncertainty intervals、confidence disclaimers 和可调整 threshold，而不仅是改变数值。
- 高风险部署应将 calibrated score 作为不确定性沟通的一部分，配合透明 data/model limitations、independent bias/calibration audit、human authority/申诉、理由与证据审查、禁止 sole reliance、monitoring 和可逆措施。不得利用行为加权刻意提高用户对系统的服从；“alignment with prediction”必须与用户利益、错误成本、公平和知情同意一起评估。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 calibration、行为经济学与 human–AI interaction extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YHRI7310.pdf) 核验五个条件、prospect weighting/inverse approximation、0.00963 MAE、rain/loan domains、ANOVA metrics和“PT correction提高相关性但非随机条件信任不变”的结论；没有把它写成信贷/医疗等高风险场景的 decision-quality、信任、合规或公平提升保证。
