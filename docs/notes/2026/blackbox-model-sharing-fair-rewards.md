---
title: "Incentivizing Black-Box Model Sharing with Fair Rewards and Payoffs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/DPVB1014"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DPVB1014.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "trusted_host_required", "public_query_dataset_required", "ensemble_weight_attribution", "blackbox_predictions_can_leak"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Incentivizing Black-Box Model Sharing with Fair Rewards and Payoffs

## 一句话总结

本文为多方 black-box model sharing 设计两阶段 incentive mechanism：trusted host 在 public dataset 上查询私有 models、以 ensemble soft labels 作为数据 reward；Weighted‑Ensemble Game 将每方 Shapley contribution 化为其平均 ensemble weight，Fair‑Replication Game 将 prediction reward 与 monetary payoff 合并并导出闭式分配。机制在定义内满足 contribution-proportional fairness、weak efficiency 与 \(\epsilon\)-individual rationality，但它依赖可信 host、公开查询分布、ensemble weight/支付可验证及 models 真诚参与；只交 predictions 不等于无 model/data leakage，也不处理真实市场串谋、身份分裂或法律/合同风险。

## 方法与证据

- 有 \(n\) parties，各自保有 local model \(h_i\) 和 private data \(D_i\)；trusted host 在 public dataset \(U\) 的每个 \(x\) 查询 predictions，并按 selected ensemble 的 input-dependent \(\beta_{i,x}\) 聚合成 \(h_N(x)\)（§2）。host、U、ensemble method和weights被假定可信/可用；文章不提供 secure query、TEE/MPC、authentication、audit、query-rate limits、model extraction/inversion防护或对预测输出泄露的实证。
- Stage 1 Weighted‑Ensemble Game 定义 coalition value 为其在 \(U\) 上总 weight mass。由于 additive，Shapley value 化简为 \(\phi_i=V(\{i\})=|U|^{-1}\sum_{x\in U}\beta_{i,x}\)（§2.1）。Prop. 2.1 以 weighted individual errors及 \(\Sigma_N\) 项界定 ensemble generalization error，支持高平均 weight的 attribution；但 attribution高度依赖 ensemble procedure、U 的代表性、loss/labeling function、adversarial/sybil models，且平均权重不必等同于实际成本、data uniqueness、fairness或社会价值。
- Stage 2 parties收 baseline reward \(r_i\)（ensemble predictions subset），可支付 \(p_i\) 获得 additional reward \(r_i^+\) 并从其他 payment pool 收补偿 \(p_i^+\)。目标定义 fairness（rewards/net payoff与 \(\phi_i\) 成比例）、\(\epsilon\)-IR（mixed retrained model不比原模型差超过 \(\epsilon\)，且 \(r_i^+\ge p_i\)）和 weak efficiency（至少一个 party获 full ensemble reward）（§2.2）。这些是 mechanism axioms，不保证每方现金流为正、短期预算可行、长期业务价值、抗操纵或所有方的严格 performance improvement。
- Fair‑Replication Game 以 total payments和 contribution scarcity 定义 coalition value，与 WEG 合并后 Theorem 2.2 给 \(u_i=r_i+r_i^++p_i^+-p_i\) 的 closed-form allocation，并声称 payoff balance、dummy payment、semi-symmetry、strict monotonicity（§2.2）。公式需要 \(V_N-\phi_i\) 等项和实际付款准确；边界 cases、负/无限/预算 constraints、payment default、tax/contract、collusion/false payment或splitting contribution未在摘要文稿展开。
- Prop. 2.3 的 \(\epsilon\)-IR bound 依 hypothesis VC dimension、private/public domain divergence、local data size \(m_i\)、reward size \(T_i\)、mix \(\alpha_i\) 和 ensemble error；作者指出 strict IR只有无限 optimal ensemble predictions或infinite optimal source data等理想极限才直接成立，实际论文称 empirical strict IR一致实现（§2.3），但未给 datasets、model families、sample sizes、experiments/table、seeds/CI或各 party performance/economic simulation。故核心证据是理论机制，非市场部署验证。

## 适用边界与复现

- 适用于经授权的组织/研究联盟在可审计 public queries 上交换蒸馏 predictions、且需要同时分配模型改进和货币补偿的机制设计研究；不应将其视为自动合并商业模型、绕过数据许可/隐私、替代合同或保证参与者经济公平的产品方案。
- 复现需公开/可审计 U、query protocol、model/ensemble definition和 \(\beta_{i,x}\)、loss/ground truth、Shapley/weight computation、payments \(p_i\)、all allocation equations/rounding、reward sampling \(S_i\)、mix/retraining \(\alpha_i\)、VC/divergence estimator、\(\epsilon\) bound和edge cases。验证 contribution/payoff balance、weak efficiency、IR gap及预算守恒，并测试多种 U/ensemble/party distributions。
- 应压力测试 nonrepresentative/poisoned public queries、correlated/low-quality/Sybil models、collusion/strategic prediction、query/response privacy attacks、untrusted host、missing/default payments、unequal data rights和out-of-domain clients。比较 Shapley alternatives、data/compute/communication cost、actual performance/fairness、privacy leakage、robustness和mechanism incentives under repeated participation。
- 生产实施需 secure/attested query execution、rate limits/DP或output controls、data/model licensing与consent、identity/anti-Sybil、escrow/settlement/audit、transparent attribution/payment records、independent dispute resolution和withdrawal/deletion process。black-box predictions仍可能支持 extraction/inference；公平 reward公式不能替代隐私、安全、竞争法或合同治理。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 black-box collaborative learning 与 incentive mechanism extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/DPVB1014.pdf) 核验 trusted host/public U、WEG平均weight Shapley value、FRG/combined closed form、公平/弱效率/\(\epsilon\)-IR及 Prop. 2.3 条件；没有将理论 allocation 写成隐私保证、真实市场公平、抗操纵支付或可直接部署的商业机制。
