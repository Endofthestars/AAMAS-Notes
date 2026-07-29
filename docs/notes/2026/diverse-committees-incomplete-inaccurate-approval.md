---
title: "Diverse Committees with Incomplete or Inaccurate Approval Ballots"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["game_theory_mechanism", "resource_allocation", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/UDNL2582"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UDNL2582.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04c"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["committee-voting", "maximum-coverage", "incomplete-ballots", "query-complexity", "polis-data"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Diverse Committees with Incomplete or Inaccurate Approval Ballots

## 一句话总结

本文将 approval committee 的多样性建模为 Chamberlin--Courant/Maximum Coverage，在只查询少量、且可能出错的选票项时研究达到 $1-1/e$ 近似所需的 query complexity，并给出 greedy 与 matroid local-search 算法。

## 方法与证据

- committee 的 CC score 是至少有一位被选候选人获其批准的 voters 数，等价 unit-weight Maximum Coverage；精确问题 NP-complete，$1-1/e$ 是一般多项式算法的紧界（§1–2）。
- 不完整信息下，接近最优近似的 non-adaptive query lower bound 为 $\Omega(m^2)$，adaptive 降至 $\Omega(m)$；greedy 匹配至对数因子。对 matroid-valid committees，采用 non-oblivious local search，支持配额等结构限制且仍为 $\widetilde\Theta(m)$（§3–5）。
- 独立响应以小概率出错时，获得 $1-1/e$ 近似需 $\widetilde\Theta(nm)$ queries。作者用 18 个 Polis datasets 与 $n=1000,m=400$ 的 100 个合成 elections 测试；少量查询的实践分数通常仍接近完整信息版本（§5–7）。

## 适用边界与复现

- 理论 inaccurate model 是特定独立错误设定，尚未给出与 incomplete+inaccurate 的联合理论；CC diversity 也不自动满足比例代表、公平或抗策略操纵。
- 复现需公开 query oracle、$\delta,\gamma,\beta$、matroid/quotas、Polis 预处理与 18 数据集、合成 $(q,\phi)$ 模型、随机 trials/seed，以及查询数和分数原始结果。真实民主平台还应处理拒答、时变偏好与知情同意。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UDNL2582.pdf) 人工核对 Max Coverage 对应、query bounds、matroid 扩展和 Polis 实验；未将有限数据实验视为平台级民主质量证明。
