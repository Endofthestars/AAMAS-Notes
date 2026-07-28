---
title: "Beyond Neighbor Influence: A Behavior-Driven Agent-Based Model of Silence"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/UPPI5986"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UPPI5986.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["synthetic_simulation_only", "no_empirical_calibration", "neighbor_influence_not_compared", "structural_pattern_by_construction"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Beyond Neighbor Influence: A Behavior-Driven Agent-Based Model of Silence

## 一句话总结

论文以“个性—环境”随机配置、主观一致性分数和表达概率函数构建沉默/表达/swing 的 ABM，在大量合成抽样中得到双端高沉默的形状；它提出一种可解释的机制假设，但并未用真实行为数据或直接含邻居影响的对照模型证明“邻居影响不重要”。

## 方法与证据

- agent 的固定意见经“Dual Perception → Consistency Judgment → Expression Decision”链路转为行为。人格由精神/物质取向 `a,b`（`a+b=1`）和环境奖励/惩罚 `c,d,e,f` 构成；一致性 `J` 将相对个人参考点的两类净奖励加权，系统 tolerance `S=c+d-e-f` 控制表达函数形状（§2）。
- 当 `J` 极负或极正，模型设定 agent 都更可能沉默，介于两者时更可能表达；再将表达与沉默概率对称拆分出固定 1/2 的 swing 概率。极端取向/奖励条件触发 collapse 或 silent point（§2.3–2.4）。
- base case 的 10 个独立随机运行各采样 `10^8` agents，按 75 个 `J` 区间汇总；论文报告窄置信区间的非对称 U 形沉默曲线、约 2% silent point 和 0.2% collapse point（§3.1、表 1）。五个受控配置中，固定取向的曲线与基线 Spearman ρ 为 0.955–1.000；按 `S≤0`/`S≥0` 的受限情况为 0.760/0.802（§3.2）。

## 局限与复现

- 输入参数均由 `[0,1]` 均匀随机抽样，未以调查、平台发言、实验或纵向社会数据校准；报告的“稳定性”是此数学函数和抽样分布下的重复性，不是预测有效性或外部效度。
- 邻居影响被汇入抽象系统 outcome/奖励惩罚机制并被设为非主导，文中没有实现、校准或比较显式网络传播/spiral-of-silence ABM。因此结果不能识别现实中行为链与邻居影响的相对因果贡献。
- 双端沉默和 `J` 分布的偏斜部分由表达函数、`J∈[-2,0.5]` 的不对称范围以及固定 swing 拆分决定；与“stylized pattern”相似并不独立验证这些构造选择。
- 复现应开放完整代码、随机数发生器/种子、`10^8` 的实际执行与聚合实现、所有区间和 special-point 规则；进一步验证应预注册真实数据映射、与网络 ABM 的消融比较、参数拟合和样本外预测。

## 与 AAMAS 的关系与核验说明

这是一种面向意见动态的 agent-based 社会行为建模方案。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UPPI5986.pdf) 核对参数化、概率生成、抽样规模和受控结果，并将作者提出的“可能是主要驱动”保持为待实证检验的机制假设。
