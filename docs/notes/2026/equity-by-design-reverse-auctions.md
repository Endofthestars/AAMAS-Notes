---
title: "Equity by Design in Task Allocation: Reverse Auctions with Group and Individual Fairness"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/CCDY4126"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CCDY4126.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "fair_task_allocation", "truthful_in_expectation", "observable_verified_groups", "asymptotic_group_fairness", "not_deployment_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Equity by Design in Task Allocation: Reverse Auctions with Group and Individual Fairness

## 一句话总结

本文为 budgeted task allocation 的 reverse auction 提出 GIFTA：先以独立 learning/allocation split 学习每任务的 group-selection probabilities，再在被选 group 内使用随 bid 递减的随机分配与 truthful payment。作者证明其 truthful in expectation、IR、budget feasible、within-group Lipschitz fairness，且随市场规模 \(n\to\infty\) 渐近满足 \(\epsilon\)-group fairness；实验显示相对 R-SPA 降低 group/individual disparity，但代价是 social cost 与效率的权衡。它不是对群体标签、劳动成本、社会公平或现实平台合法合规的通用保证。

## 方法与证据

- 模型有单一 requester、\(\kappa\) 个公开 value \(v_k\) 的 tasks 和 \(n\) 位 workers；每位 worker 对每个 task 的真实 private cost 在 \([\underline c_k,v_k]\)，可策略性申报 bid；一个 task 至多给一人、worker 可获多个 tasks（§2）。budget feasibility 的形式是每 task payments 总和不超过 \(v_k\)，不包含总体预算、质量/交付、容量、动态需求、劳动法规或 bid collusion。
- group fairness 比较任意两个可观测、互不相交 group 的 expected aggregate utilities，差不超过 \(\epsilon\)（Definition 2）；individual criterion 仅在同组内，对 task \(k\) 的 expected allocation-probability difference 由 normalized bid distance 限制（Definition 3）。论文假定群组是 platform 验证的外生属性，且 structural cost heterogeneity 由 group 分布表达；这不是对未观察身份、交叉群体、历史歧视、equal opportunity 或 outcome quality 的保证。
- Stage 1 随机分 workers 为 learning set \(L\) 与 allocation set \(A\)，在 \(L\) 上模拟 intra-group rule 来估计 cost/aggregate utility，解带 absolute group-gap constraints 的 optimization 为每 task 学 \(\gamma_{t,k}\)；摘要称通过 Lagrangian dual、分 task subproblems、Adam 更新 multipliers 求解。Stage 2 按 \(\gamma\) 抽 group，eligible \(A\) bidders 的 winning probability 与 \(1/b_{i,k}\) 成比例，并使用积分形式 payment（§3）。训练样本、optimizer convergence、估计噪声与 split 代表性会影响公平目标的实际达成。
- Theorem 1 证明 GIFTA IC、IR、BF，满足 within-group Lipschitz fairness，并在 \(n\to\infty\) 时渐近 \(\epsilon\)-group fair。IC 是 randomized mechanism 下的期望效用性质；渐近结果不是有限市场、有限 learning sample 或每一次随机抽签的 exact fairness/error bound。
- Figure 1 比较 R-SPA 与 GIFTA：放宽 \(\epsilon\) 降低 social cost、提高 approximation ratio，同时放松 equity；GIFTA 在 allocation set 的 realized fairness 接近从 \(L\) 学到的 target，within-group disparity 近零，R-SPA individual gap 为 1.0。摘要没有完整数据生成、市场 sizes/group costs、seeds/CI、absolute costs、solver tolerance或对实际 workers 的实地评估。

## 适用边界与复现

- 适合受控的 procurement/crowdsourcing allocation mechanism research；不应据此自动雇佣、定价、拒绝或分配高风险服务。实际系统须先进行合法性/歧视影响审查，取得处理敏感群组属性的适当授权，并允许申诉、审计、人类复核和纠错。
- 复现应公开 task values/cost domains、groups 和 cost distributions、\(L/A\) split、eligibility、\(\epsilon\)、simulation estimator、optimization dual/Adam hyperparameters/tolerance、intra-group allocation/payment implementation、R-SPA baseline、market sizes、seeds 和 confidence intervals；逐项测真实申报/偏离时 expected utility、payments、budget、group aggregate utility、within-group probability gaps与 social cost。
- 应检验 finite/small or unbalanced groups、intersectional/misclassified groups、missing/strategic group information、collusion/Sybil bids、multi-task capacity/quality constraints、dynamic arrivals、non-stationary costs、estimation shift和 payment delays。还须报告 per-run fairness distribution而非仅期望或平均值，并独立评估用户/worker harm、隐私和政策约束。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 mechanism design/fair resource allocation 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CCDY4126.pdf) 核验两类 fairness definitions、GIFTA 的 split/optimization/auction stages、Theorem 1 和 Figure 1；没有把期望、有限样本估计或渐近性质误写为现实社会公平认证。
