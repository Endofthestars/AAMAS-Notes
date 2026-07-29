---
title: "Real-time Cohorting of Nursing Care into Bubbles"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "resource_allocation", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/GLZA7190"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GLZA7190.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["healthcare_simulation_only", "single_micu_data_source", "covid_model_assumption", "online_irrevocable_assignment", "patient_care_quality_unmodeled", "staff_fairness_and_preference_unmodeled", "demand_estimation_error", "clinical_governance_required"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Real-time Cohorting of Nursing Care into Bubbles

## 一句话总结

论文提出 Online Bubble Clustering（OBC）：病人入院时不可撤销地选房间与照护 bubble，使可替代 HCP 分配到 bubble、专科 HCP 的跨 bubble 接触需求最小，同时约束 bubble 房间直径与 HCP excess load。由于未来入/出院与需求未知，任意 deterministic 或 randomized online 算法在最坏情形相对离线 OPT 都可有无限 competitive ratio；作者因此评估 Random、Greedy、\(\tau\)-Greedy 启发式。把单个 MICU 30 天传感器移动日志叠加 COVID-19 agent-based disease model 的模拟显示，bubble 可在部分场景把感染从约 74.7 降到 44.8–48.2（K=5、90% occupancy），但这是模型内传染与运营 proxy，绝不构成临床感染控制、患者照护质量或人员配置安全的部署证据。

## 方法与证据

- OBC 以入院/出院 event 流为输入。每次 admission 需立即把 patient visit 放入可用房间和一个 bubble；每位病人的 day/night 可替代护理和各 non-substitutable specialist 需求只在到达时揭示（§2）。该 online 假设刻画缺少预见性，但真实医院可能知道候床、预约或历史需求。
- 目标是 cross-bubble demand：对分属不同 bubble 且住院时间重叠的病人，累积共同 non-substitutable HCP 所需服务时间的乘积；它用作病原跨 bubble 接触机会 proxy（§2）。它没有直接测量手卫生、PPE、空气/表面传播、人员感染状态或护理质量。
- 约束包括每 bubble 的 room-distance diameter 与 substitutable HCP total excess load；本文均匀分配可替代 HCP（§2）。患者 acuity、连续照护、护士经验/偏好、休息、技能 mix、伦理公平及真实 unit 流程没有被完整优化。
- Theorems 1–3 构造对抗式 event 序列：任一 online deterministic 或 randomized 方法均可有 \(\Omega(Td^2)\) cross-bubble demand，而 offline OPT 为零，即 competitive ratio 无限；即使 online 方法可用任意多 bubbles/大直径仍有下界（§2）。这是最坏情况信息论结论，不表示实际 hospital 数据必然无法获得有用在线策略。
- 启发式包括 Random、局部最小 cross-bubble demand 的 Greedy，及在接近局部最优需求的可行 pair 中权衡直径/载荷的 \(\tau\)-Greedy；ILP 仅作中小实例可解的离线 oracle（§3）。没有一般的启发式近似比或临床可行性证明。
- 数据是大型三级医院 MICU 的 30 天匿名 patient/operations 与 sensor/badge mobility：25 nurses、12 specialists、20 个动态占用房间。每个 outbreak replicate 从一个随机 infected substitutable HCP 开始，使用 COVID-19 disease model；每设置 2,500 replicates（§4）。单单位、单时间窗、假定接触/感染参数限制了外推。
- 在 K=5、90% occupancy 的表 1，Baseline infection 为 \(74.7\pm45.4\)，Greedy \(45.8\pm38.6\)，\(\tau\)-Greedy \(44.8\pm39.7\)，Random \(48.2\pm37.4\)；总 HCP load 也从 \(1444.7\pm48.5\) 降至约 1178–1193（§4、表 1）。随机与贪心相近表明“进行 cohorting”比细节选择更关键，也意味着该设置下算法优越性很弱。
- 作者明确限制：只模拟 COVID-19；fomite/其他 HAI（如 C. difficile、VRE、MRSA）可能得出不同结果；仅单 MICU、假设仅知道下一到达病人，且没有纳入 unmet demand 或 patient-care quality 成本（§4）。这些都是任何临床试点前必须补齐的证据。

## 适用边界与复现

- 适用于医院运营研究中的预防性 cohorting decision-support 原型或仿真对照，前提是由感染控制、护理管理、床位调度和隐私团队共同定义约束与可接受的 workflow。
- 不应自动决定病人房间/护士指派、削减 staff flexibility，或宣称降低真实 HAI。临床使用需监管审查、前瞻性/分阶段验证、人工 override、病人安全和公平监测，且须不取代标准感染控制措施。
- 复现应固定 event log 清洗、房间 metric、HCP 分类与负荷/病人需求估计、bubble 数/直径/载荷上界、Random/Greedy/\(\tau\) 参数、ILP 限制、疾病自然史与接触传播参数、occupancy/transmissibility grid、2,500+ seeds，并报告置信区间和原始 contact 改变。
- 后续要在多 unit/多病种/季节验证，显式纳入技能/连续照护、患者与人员公平、延迟和紧急 override、提前到院信息、成本效用与 staff feedback；对真实感染、护理遗漏和人员伤害做独立监测。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 online allocation、agent-based epidemiology 与医疗运营工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GLZA7190.pdf) 核验 OBC 目标/约束、online hardness、三种启发式、MICU 数据、2,500 replicate COVID 模拟、表 1 和作者列出的临床局限；没有把感染 proxy 或仿真差异误写成临床有效性或可自动部署的照护分配方案。
