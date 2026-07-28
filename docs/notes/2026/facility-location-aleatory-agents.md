---
title: "The Facility Location Problem with Aleatory Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "planning_scheduling"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HKJY8780.pdf"
preprint_url: "https://arxiv.org/abs/2409.18817"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["worst_case_distribution_scope", "quantile_information_scope", "strategyproofness_scope"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# The Facility Location Problem with Aleatory Agents

## 一句话总结

FLPAA 将未报告位置、但会以未知分布到来的外部用户纳入一维设施选址；论文以能查询到的分布 quantile 数量为信息预算，刻画 truthful 机制的最坏分布强近似比（SAR）。

## 方法与证据

- 设施容量为 $n$，其中 $n_r$ 个 strategic reporting agents 报告位置，余下 $n_u=n-n_r$ 个 aleatory agents 独立同分布于未知 $\mu$；目标是报告者绝对距离和加上 $n_u\mathbb E_{X\sim\mu}|X-y|$ 的 ex-ante social cost（§1）。
- 机制只须对 $n_r$ 位报告者 truthful。SAR 对所有报告 profile 和所有 $\mu\in\mathcal P(\mathbb R)$ 取比值上确界，因而比固定 $\mu$ 下的 approximation ratio 更强（§2）。
- Phantom Quantile Mechanism（PQM）取报告位置与若干查询 quantile 的中位数；任意 PQM 都 truthful 且 anonymous（Theorem 3）。在零信息时，报告者中位数机制达到所有 truthful 机制中最优的 SAR；该值随 $\lambda=n_r/n$ 和 $n_r$ 奇偶性而变（Theorems 4–5）。
- 若可查询至少 $n_u$ 个等间距的特定 quantile $q_j=(2j-1)/(2n_u)$，PQM truthful 且达到最优 ex-ante cost，SAR 为 1（Theorem 6）。仅知 $\mu$ 的 median 时，重复该 median 的 PQM 有界于 3 以下，但并非通常最优，且论文给出任何 truthful 机制的下界（Theorems 7–8）。
- 对 $1<k<n_u$，论文用 lift 把 $k$ 个 quantile 复制成 $n_u$ 个 phantom positions；给出其 SAR 的精确偏差公式，并在特定整除/等距量化条件下给出最优查询向量与下界（Theorems 9–11）。还讨论双设施版本，但部分证明与结果在附录。

## 局限与复现

- 主体是线性上的单设施、绝对距离、外部 agent i.i.d. 同一分布、以所有 $\mu$ 为对手的 worst-case 模型；不是已知分布的 Bayesian welfare 最优机制。
- 查询的 quantile level 必须在看到报告前预先选定；不能将结论扩展到根据 report 自适应查询、样本估计 quantile 或外部用户可策略报告的设置。
- SAR=1 依赖可获得至少 $n_u$ 个指定 quantile；只知 median 或较少 quantile 时仅有常数界/特定下界，不能称为全信息最优。
- 复现应枚举 $n_r,n_u$ 与奇偶性，构造集中分布验证 worst-case SAR，并单独检查 quantile 误差、样本有限性及双设施容量假设；不要仅在单个 uniform $\mu$ 上估计平均成本。

## 与 AAMAS 的关系与核验说明

该文结合部分分布信息与无金钱的 truthful facility location。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2409.18817) 核对了模型、Theorems 3–11 及其信息获取前提。
