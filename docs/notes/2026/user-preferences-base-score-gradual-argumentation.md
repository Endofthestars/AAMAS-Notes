---
title: "From User Preferences to Base Score Extraction Functions in Gradual Argumentation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "human_agent_interaction", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/LIEI2830"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LIEI2830.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["preference_elicitation_dependency", "argument_modeling_dependency", "synthetic_evaluation", "semantics_sensitivity", "no_user_study", "no_robot_deployment_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# From User Preferences to Base Score Extraction Functions in Gradual Argumentation

## 一句话总结

本文提出 Base Score Extraction Functions（BSEFs），把用户对论点的偏好序（含“远强于”关系）映射为 Bipolar Argumentation Framework 中的 \([0,1]\) base scores，再交由 gradual semantics 求最终论点强度和决策。它在辅助喂食的合成论证场景中展示偏好与参数/semantics 的交互；但结果的对齐依赖偏好 elicitation、论证图和语义选择，实验并非用户研究、真实机器人或安全验证。

## 方法与证据

- 输入为带 attack/support 关系的 BAF 与反身、传递的 argument preference ordering；BSEF 输出 \(\tau:X\to[0,1]\)，将其转成 QBAF，决策论点的 base score 固定为 0.5（§2–3）。论文主要假定树状、无环的 QBAF，把 cyclic QBAF 留作未来工作。
- 两个具体 BSEF 依据排序中的普通偏好间距 \(\delta\) 与“much greater”间距 \(\Delta\) 计算距离并归一化；Algorithm 1 允许调整范围/centralisation 等设计选择（§3.3）。这些参数是设计者规定的心理强度代理，不能从排序本身唯一识别真实用户的效用差、风险容忍或偏好不确定性。
- 理论部分表明在 \(\Delta,\delta\) 等条件下两个函数满足所定义的 preference-order、range、regularity 和 stability 性质；若 gradual semantics 具有 monotonicity 与 balance，则在相同攻击/支持下更偏好的论点会有更高最终强度（§3.4, §5.1）。这些是模型内结构性质，不验证用户是否接受排序、论证是否完备或最终行动是否正确。
- 案例是 robot-assisted feeding：六个关于慢/快喂食的论点与两个决策论点；如安全/吞咽风险、压力、无聊、与亲属相处等被人工编码（§2–3）。该图的遗漏、关系方向和“快/慢”动作集合已强烈决定输出，不能把论证透明性等同于临床安全或知情同意。
- 实验产生 30,000 个随机 preference orderings 与设计选择，用 QE、Euler-Based（EB）和 DF-QuAD 三种 semantics 比较同一合成图的选项（§5.2）。centralisation 下 QE–EB agreement 0.98、QE–DF 0.85、EB–DF 0.84，Cohen’s \(\kappa\) 分别 0.96、0.65、0.62；这些衡量方法间模拟输出一致性，不是对人类偏好/疗效/风险的外部效度。
- DF-QuAD 在高 base-score supporter/attacker 下更能主导被影响论点，极端范围时更敏感；QE 较平滑，EB 对接近 0/1 的论点更保守（§5.2–5.3）。作者将强反应性描述为可能适合安全关键优先级，但没有运行传感误差、冲突偏好、意外事件、恢复动作或真人安全评测，不能据此部署为安全控制规则。
- 作者明确未来工作包括用反馈/情境调参、partial orders、多用户偏好聚合和 structured argumentation（§7）。因此当前方法未解决不可比较偏好、多人冲突、动态偏好、偏好操纵或论证知识获取。

## 适用边界与复现

- 可用于把明确 elicited 的单用户论点排序转成可追踪的 gradual-argumentation decision-support 初始分数。应向用户展示排序、强度间距、图结构、语义和反事实结果，并允许更正、拒绝自动决策及记录版本。
- 医疗、护理、机器人或其他高风险决策不得只靠 BSEF 输出。必须加入临床/领域规则、禁忌与硬约束、可靠状态估计、风险/不确定性评估、实时监控、紧急停止和具备权限的人类复核；“安全论点更受偏好”不构成医学、物理或监管安全证明。
- 复现需公开完整 BAF/QBAF、六个论点及关系、随机排序/参数的生成分布与 seed、\(\Delta,\delta\)、范围和 centralisation 规则、QE/EB/DF-QuAD 精确实现、tie-breaking、30,000 样本、agreement/\(\kappa\) 计算。还应测量实际调用成本与对排序/边/参数扰动的敏感性。
- 后续应以真实但低风险的参与式研究验证理解、校准、负担和纠错，纳入不完整/矛盾/多用户偏好、错误论证关系、感知噪声与长期更新；对真实机器人仅可在独立安全壳和伦理审批下测试，报告违例和近失事件。

## 与 AAMAS 的关系与核验说明

这是将人类偏好纳入 gradual bipolar argumentation 的可解释决策支持工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LIEI2830.pdf) 核对 BSEF 输入/输出、两种函数与性质、辅助喂食图、三种 semantics、30,000 随机样本及 agreement/\(\kappa\)、作者列出的未来缺口；没有把合成论证的一致性、模型内 monotonicity 或机器人叙事案例误写成用户验证、真实偏好学习、医疗建议或部署级安全保证。
