---
title: "Yanapay: A Simulation Toolkit for Autonomous Agents Reasoning about Human Behaviour in Emergency Evacuations"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["human_agent_interaction", "robotics_embodied", "safety_verification", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/YQLN3900"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YQLN3900.pdf"
code_url: "https://github.com/kangkelidis/robot-assisted-evacuation"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05l"
spark_draft_verdict: "source_grounded_with_figure_strategy_count_and_scope_errors"
spark_qa_verdict: "needs_revision_corrected_for_model_validation_strategy_labels_statistics_and_safety_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["emergency_evacuation_simulation", "impact_plus_validation_not_yanapay_deployment_validation", "human_behaviour_model_simplification", "sensitive_demographic_attributes", "social_identity_and_compliance_inference", "privacy_safeguards_not_specified", "fairness_and_discrimination_not_evaluated", "figure_without_numeric_table", "runs_seeds_and_uncertainty_missing", "nearest_candidate_logic", "physical_sar_safety_not_validated", "simulation_to_deployment_boundary"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_human_behaviour_model_sensitive_attribute_fairness_statistics_physical_sar_and_deployment_boundary_check"
escalation_verdict: "pass_after_source_model_validation_strategy_label_statistics_privacy_fairness_and_sar_safety_corrections"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted human-behaviour and SAR-safety check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Yanapay: A Simulation Toolkit for Autonomous Agents Reasoning about Human Behaviour in Emergency Evacuations

## 一句话总结

Yanapay 把 social-psychology crowd model、NetLogo simulation、Python SAR strategy controllers、scenario orchestration 与结果可视化封装成 transportation-hub evacuation toolkit；它可比较机器人招募 first-/zero-responder 的策略，但三页 demo 没有数值结果表、runs、seeds 或 uncertainty，且引用模型的 drill-data validation 不等于 Yanapay、机器人策略或现实疏散已经验证。

## Toolkit 的研究边界

Yanapay 面向 emergency evacuation 中的 socially-aware Search and Rescue（SAR）agent evaluation。示例任务是 SAR robot 找到 fallen civilian 后，判断应请求 civilian zero-responder 还是 scarce first-responder 提供帮助（pp. 4062–4063）。

工具的贡献是：

- 自动生成、执行和分析 user-defined simulation scenarios；
- 让研究者在 Python 中插入不同 SAR decision/prediction strategies；
- 在相同 crowd model 中比较这些 strategies；
- 以统计比较和 visualisation 展示 evacuation outcomes。

它不是 physical SAR robot stack，也没有验证 sensing、navigation、communication、actuation 或现场 command protocol。

## IMPACT+ 来源模型与验证边界

Yanapay 建立在 IMPACT+ 上；论文把 IMPACT+ 描述为 IMPACT 的 extension，由 social-psychology domain experts 工程化，并引用 [8] 称其依据 real-world evacuation-drill data 做过 human-behaviour validation（p. 4063）。

这一证据属于来源模型/引用工作。它不能自动证明：

- Yanapay 的 software integration 正确；
- 新增 SAR strategy 与 zero-responder recruitment 合理；
- simulation 在其他 transportation hubs、cultures 或 emergencies 外部有效；
- modelled evacuation time 与真实现场一致；
- robot deployment 安全。

三页稿没有展示对 Yanapay 本身的 drill replay、calibration transfer 或 field validation。

## 人群与社会行为模型

simulation agents 带有 internal cognitive/social states（p. 4063）：

- belief state 表示 perceived danger；
- environmental/social cues 触发 desire to evacuate；
- 未决定撤离时在空间中随机移动；
- age、gender、cultural group、familiarity、compliance 等 demographic/behavioural attributes；
- group leaders 作出撤离决定后，其 members 跟随，并可能在出口前寻找彼此形成 bottleneck；
- high concentration 提高 accidents/falls 的概率；
- fallen state 持续一段时间，获得 group leader、first-responder 或 zero-responder 帮助可缩短持续时间；
- zero-responder 是基于 shared social identity 帮助他人的 civilian。

这些是模型规则，不是对所有真实人群的普遍行为定律。

## SAR robot 决策

SAR robot 独立于 civilian group leaders，需要为 fallen agent 选择求助对象：

- 请求 zero-responder，可利用 civilian assistance；
- 请求 first-responder，使用专业但稀缺的资源；
- 若请求一个拒绝帮助的 civilian，会浪费一次 attempt 并延迟通知 first-responder；
- 若过度依赖 first-responders，也可能因资源稀缺增加 evacuation time。

当前 implementation **只考虑 nearest candidate**（p. 4063）。论文说研究者可替换 prediction/decision model，但没有证明某个 model 已最优，也没有给 prediction accuracy、calibration 或 group-wise error。

## 软件架构

Yanapay 的 workflow 包括：

1. NetLogo 实现 Simulation Model；
2. Python 实现 SAR behaviours/strategy controllers；
3. PyNetLogo 与 Flask 桥接 NetLogo 和 Python；
4. Simulation Manager 根据 crowd/robot density 等 user-defined settings 生成并 parallel execute scenarios；
5. Results Analyser 在 termination 后生成 strategy statistical comparisons 与 visualisations。

论文提供 [source code](https://github.com/kangkelidis/robot-assisted-evacuation) 和 [demo video](https://youtu.be/erLsxmFtHzs)。三页稿没有固定 commit、release、dependency versions、environment lock、input-data version、default seeds 或 end-to-end reproduction command。

## Demonstration 证据

Figure 3 展示 predefined scenarios 的 evacuation-time distributions，并按 median 给出五个 labels（p. 4063）：

1. no SAR robot；
2. always asking for help；
3. random decision；
4. always calling for help；
5. predicts the chance of a passenger accepting to help。

论文没有给 Figure 3 对应的数值 table、axis values、scenario parameters、number of runs、random seeds、variance、confidence intervals 或 significance tests。不能从图注排序声称第五种策略具有统计显著优势、现实最优性或安全保证。

## 敏感属性、隐私与公平性

age、gender、cultural group、compliance、familiarity 和 shared social identity 都可能成为高影响代理变量。论文只说，现实部署中用 shared-identity markers 应受 privacy safeguards 约束；没有说明：

- 是否必须采集这些属性；
- consent、data minimisation、retention 或 access control；
- identity inference error；
- 不同群体的 help-request、拒绝、delay 或 rescue outcome；
- fairness objective、bias audit、appeal 或 human override。

simulation 使用这些属性不等于现实系统获得了合法、可靠或公平的识别能力。错误 proxy 可能造成 stereotyping、差别化求助和资源分配伤害。

## Safety 与适用边界

Yanapay 可以在仿真中低成本探索 scenario，不等于已经证明：

- human behaviour prediction 真实；
- robot 能正确识别人、伤情或身份；
- request 不会造成 panic、coercion 或 delay；
- navigation/collision/communication/system failure 安全；
- evacuation time 是唯一或充分的 safety outcome；
- 模型可直接指导现场 first-responder allocation。

现实使用仍需 domain/ethics review、physical safety case、human command authority、uncertainty-aware abstention、fairness/privacy safeguards、validated sensing、failure recovery 和 field/drill evaluation。

## Future Work

作者明确提出（p. 4063）：

- 用 prioritised ranking system 替代 current nearest-candidate logic；
- 更细致地建模 fallen agents 作为 obstacles 的 crowd dynamics；它们可能减少 exit congestion 并改变 total evacuation time。

这两项尚未实现，也说明当前 crowd/robot decision model 仍有重要简化。

## 页码与核验说明

PDF 逐页核对：p. 4062 为 identity、abstract、Introduction、tool motivation、Figure 1 和 code footnote；p. 4063 为 Related Work、IMPACT+/agent model、tool architecture、demonstration、Figure 3、Conclusion/Future Work；p. 4064 为 Acknowledgments 和 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YQLN3900.pdf) 核对来源模型、五类 strategy labels、软件架构与证据边界；`reviewed` 不表示真实人群行为、SAR robot safety 或现场 deployment 已经验证。
