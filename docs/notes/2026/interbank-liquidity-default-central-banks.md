---
title: "Capital Provision to Reduce Liquidity Defaults and the Role of Central Banks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "applications"]
dblp_key: ""
doi: "10.65109/RENG3297"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RENG3297.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02s"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "financial_model_assumptions", "six_bank_calibration", "equilibrium_solver_dependence", "not_policy_or_regulatory_advice"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Capital Provision to Reduce Liquidity Defaults and the Role of Central Banks

## 一句话总结

论文以多期 agent-based interbank model 和经验博弈分析（EGTA）研究流动性紧缺：有正价值的供给银行在“不贷、只贷给偿付能力银行、贷给全部需求银行”间策略选择，中央银行可向仍具偿付能力的需求银行提供资金以改变其还款预期。以 EBA 数据校准的六家系统重要银行模拟中，当所有需求银行均 solvent 时，央行贷款或集中协调能减少流动性违约；混有偿付能力违约时，非合作均衡仍倾向囤积流动性。结果是强简化金融网络模型的情景分析，不能导出真实央行的救助、监管或放贷决定。

## 方法与证据

- 每期以现金、负债矩阵和 Greatest Clearing Vector Algorithm 求支付/银行价值；\(v_i(t)<0\) 为 distress。需求银行的借款需求为 \(-v_i(t)\)，供给银行按策略提供现金，借款被写入下一期附息负债（§2）。
- 供给银行策略集合为 `{none, solvent, all}`：囤积、不向任何需求方放贷；只向偿付能力需求银行放贷；或向所有需求银行放贷。其收益是下一期银行价值；每期由供给银行的策略 profile 形成博弈，论文以 EGTA 的不同 equilibrium solvers 求均衡（§2.1--2.2）。
- 央行只向 solvent demand banks 提供贷款，金额按文中两期净资产不足额定义，目的在于让供给方预期偿还并提高 interbank lending incentive，而非直接覆盖所有损失（§2.2）。
- 采用 EBA 2024 transparency data，取总资产最大的六家银行为 SIB lenders，设现金比例参数 \(\beta\)、利率范围 \(r_{min}=0.02,r_{max}=0.08\)。当所有银行被额外给现金以保证 solvency 时，有央行贷款的非合作均衡中多数 SIB 放贷且无后续违约；无央行贷款时几乎都囤积。集中协调即使不放央行贷款也可改善（§3）。
- 在同时有 liquidity/solvency defaults 的模拟中，即使有央行支持，非合作 SIB 往往囤积；集中协调下低 \(\beta\) 时部分 SIB 仅贷给 solvent banks，随 \(\beta\) 增加更多银行选择 all（§3--4）。

## 适用边界与复现

- 适用于研究银行网络中短期流动性、放贷激励和协调机制的机制设计/压力测试原型；模型不等同于资本充足率、信用风险、抵押、监管规则、破产程序、市场价格或跨境结算的完整金融系统。
- 六家 SIB、策略离散化、随机借款匹配、\(\beta\)、利率界、中心银行仅支持 solvent borrower 以及 equilibrium solver 都会改变结论。EGTA 近似支付表与多均衡选择也可能使“均衡行为”不唯一。
- “所有需求银行 solvent”是正面结果的重要条件；不能把它外推到现实危机中混合违约的政策效果。集中协调的可执行性、信息需求、激励相容性、分配公平和道德风险未被实证验证。
- 复现应版本化 EBA 输入和映射、clearing-vector、现金/负债演化、策略/利率/\(\beta\)、央行规则、EGTA sampling 与 solver；报告每个均衡、违约数、贷款量、银行价值、敏感性和置信度，并由金融监管/风险专家审核任何现实解释。

## 与 AAMAS 的关系与核验说明

该文将资源配置、金融网络与经验博弈分析结合。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RENG3297.pdf) 人工核对清算模型、三种放贷策略、央行规则、六 SIB 设置与两类情景结果；不将模拟发现表述为金融建议。
