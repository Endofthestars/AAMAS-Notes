---
title: "Information Contagion in Climate-Stressed SME Networks: An Agent-Based Simulation Study"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "norms_trust_governance", "marl_coordination"]
dblp_key: ""
doi: "10.65109/OCAP7538"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OCAP7538.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["agent_based_simulation_only", "heuristic_investment_policy", "calibration_assumption_dependence", "synthetic_networks", "signal_precision_boundary_condition", "no_empirical_causal_validation", "policy_inference_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Information Contagion in Climate-Stressed SME Networks: An Agent-Based Simulation Study

## 一句话总结

论文构造 200 家欧洲 SME 的双层（supply-chain/credit）网络 ABM：是否采用 GABA 环境会计决定气候信号精度，未采用者从邻居资本变化推断风险并据此用启发式投入 adaptation。仿真中，部分采用（约 \(\lambda=0.25\)–0.5）出现比零采用与完全采用更高的 systemic capital loss，作者称为“valley of vulnerability”；高采用时振荡衰减。该结论是指定 damage、网络、信息与投资规则下的情景机制发现；低精度信号时 valley 消失，尚无真实 SME 气候事件数据的因果验证，不能直接推导 GABA 推广政策的实际风险。

## 方法与证据

- 模型为 \(N=200\) firms 的有向多层网络，资本、气候 stress、adaptation capital 和二元 GABA adoption 随时间演化；supply/credit weights 设为 0.6/0.4，网络采用 sectoral clustering 与 power-law degree 等配置（§3–4.1）。所谓“欧洲校准”是参数/结构对齐，不是对具体企业关系或行为的逐户观测建模。
- 采用者得到含噪的本地气候信号（baseline precision \(\tau_{GABA}=4\)）；未采用者从邻居资本变化的 logistic transform 汇总风险，无法区分气候与其他损失来源（§3.2）。该 attribution error 是信息 contagion 的假设机制，非由企业调查或因果实验识别。
- 资本/气候/adaptation 用指定的 Cobb–Douglas、damage 和非线性动态方程；原本应解 HJB 的 adaptation decision 被“calibrated heuristic”替代，作者称将计算降约 50×（§3.1–3.3）。结果因此依赖 heuristic 权重、流动性、损害和信号函数，不能解释为经济主体最优行为的证明。
- 基线为 adoption \(\lambda\in\{0,0.125,\ldots,1\}\) × climate intensity 两水平、每格 20 replications，共 360 个 120-month simulations；另做 network size、heuristic、参数和 signal precision robustness，总 720 simulations（§4）。随机种子/合成网络的重复性支持内部情景稳定性，不等于外部有效性。
- 报告的 systemic capital loss 在 \(\lambda=0.375\) 达 0.758，零采用 0.691、完全采用 0.523；FFT 主频 0.2 cycles/month（5-month period）幅度随采用提高从 13.8 降至 8.2（§5.1–5.2）。这些数字是模型 metric，不是观测到的企业违约、就业或排放影响。
- signal precision 压力测试给出关键边界：\(\tau=2\) 时损失随采用单调下降、无 valley；\(\tau=4\) 出现 valley；\(\tau=6\) 更深（§5.3、§6.2）。说明现象需要信息足以造成 informed/uninformed 行为分化，不能声称 partial adoption 普遍有害。

## 适用边界与复现

- 适用于探索“异质信息质量 + 网络依赖 + 气候适应”可能产生的非线性机制，帮助生成应收集哪些数据、该做哪些协调部署实验的假设。
- 不应用来给具体 SME、国家或监管阈值下结论，亦不应据此推断部分披露/环境会计会导致真实系统性损失。政策应先做真实 disclosure、供应链/信贷暴露、气候冲击、适应投资和 failure outcome 的纵向验证/准实验。
- 复现需公开网络生成/sector 配置、全部方程与参数、GABA adopter assignment、seeds、initial capital、arrival shocks、integration step、heuristic/targeting规则和 loss/entropy/FFT metric；报告绝对值、置信区间与所有 robustness cells。
- 后续应校准到实证 SME microdata，比较替代行为模型（强化学习/优化/调查规则），加入内生 adoption、政策成本、信息可验证性、真实供应中断与异质网络不确定性，并预注册可被数据反驳的 valley 预测。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的社会经济 agent-based simulation、网络 contagion 和气候适应工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OCAP7538.pdf) 核验 200-agent 模型、信息/投资机制、720-run 实验设计、valley/FFT 结果与 precision 边界；没有把校准 ABM 的机制输出表述为现实企业的因果结论或直接政策建议。
