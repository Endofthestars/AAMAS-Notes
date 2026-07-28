---
title: "Adaptive Agents in Spatial Double-Auction Markets: Modeling the Emergence of Industrial Symbiosis"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "applications", "marl_coordination"]
dblp_key: ""
doi: "10.65109/EXII2056"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EXII2056.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["single_byproduct_model", "stylized_virtual_geography", "fixed_external_market_price", "simulation_not_industrial_deployment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Adaptive Agents in Spatial Double-Auction Markets: Modeling the Emergence of Industrial Symbiosis

## 一句话总结

本文构造一个空间嵌入的多边双边拍卖仿真：卖方以 RL/EMA 方式调整副产品价格，买方将报价、运输成本和外部市场价格一起比较；在虚拟地理和单一副产品条件下，价格、交易量与 symbiosis index 会随 scarcity、空间聚集、disposal cost 和密度共同涌现，但这不是实地工业共生干预的因果验证。

## 方法与证据

- 市场包含空间位置不同的 buyers/sellers。buyer 只接受不高于其外部 market-price 阈值的 offer，并选净效用最大的卖方；seller 需承担运输成本及未售库存 landfill/disposal penalty（§3.1--3.2）。
- 在每轮多边 double auction 后，seller 从离散 markup actions 中选价；其 action value 以 exponential moving average reward 更新，softmax temperature 控制探索并衰减，目标是累计利润（§3.2--3.3）。
- 作者定义 symbiosis index，并以 price convergence、交易、local circularity、counterfactual regret 等分析 emergent outcomes（§3.4、§5）。
- 实验为 decentralized spatial simulation：四个企业空间 clusters、默认 10 buyers/10 sellers/1 byproduct，external market price 固定为 100，1000 steps；报告 10-run means。另运行 20,000 independent simulations 做 Sobol sensitivity analysis（§4--5）。
- 结果显示 transaction price 会在不同 scarcity 下接近某个 equilibrium；scarcity、disposal penalty、spatial spread/density 的高阶交互影响交易/循环性。文中强调 adaptive sellers 的 aggregate regret 随时间下降，而非给出一般均衡或真实市场因果结论（§5--6）。

## 适用边界与复现

- 模型只含单一 byproduct、固定外部价格、stylized virtual geographies；抽去了 product quality/compatibility、多个耦合市场、合同/法规、生产周期、storage、capacity、信用风险、谈判权力和真实物流网络。
- RL/EMA 收敛于模拟的 payoff/auction rules；不保证 strategy-proofness、价格公平、社会最优、企业参与意愿或不同产业/地域下的可迁移性。
- “工业共生/减排”是该市场中副产品重用的代理结果，论文没有 LCA、material traceability、污染风险、实际企业数据校准或 field deployment；不能用于直接制定补贴、废物监管或基础设施投资。
- 复现应公开 agents、markups、price threshold、transport/disposal costs、geography generator、scarcity/density distributions、auction clearing 与 random seeds；并做 empirical EIP case calibration、out-of-sample validation、multi-product temporal dynamics 和 distributional-impact analysis。

## 与 AAMAS 的关系与核验说明

这是空间市场机制、学习 agent 与循环经济的 agent-based modelling 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EXII2056.pdf) 核对 auction/RL 机制、simulation scale、Sobol analysis 和 §6 limitations；没有将模拟中出现的 circularity 或稳定价格表述为真实工业园政策效果。
