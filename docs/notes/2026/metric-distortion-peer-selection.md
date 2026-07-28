---
title: "Metric Distortion in Peer Selection"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "norms_trust_governance", "resource_allocation"]
dblp_key: ""
doi: "10.65109/BEYC4030"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BEYC4030.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["ordinal_information_only", "line_metric_assumption", "worst_case_not_empirical_quality", "strategyproofness_not_modeled", "unbounded_distortion_regimes"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Metric Distortion in Peer Selection

## 一句话总结

论文首次研究 voter 与 candidate 是同一批人的 peer selection 中，依据序数偏好选择大小为 \(k\) 的委员会时的 metric distortion。在线度量下，排名足以恢复 agents 的左右顺序；作者给出四种 social-cost 组合的界：utilitarian-additive 可由选 \(k\) 个中间 agents 得到介于 1 与 2 的 distortion，egalitarian-additive 的两端选择接近最优 2；但若 \(q\)-cost 的 \(q\) 过小，则仍不存在任何常数 distortion。它刻画的是在隐藏距离下的最坏情况社会成本近似，不是对真实同行评审“质量”、诚实性或公平程序的实证保证。

## 方法与证据

- 模型中 \(n\) 位 agents 同时是 voters 和 candidates；每人按共同 metric space 中到其他人的距离给出严格排序，规则仅见 rankings，输出 \(k\) 人 committee。distortion 是该委员会 social cost 与知道真实距离的最优委员会之比，取所有与排序一致的 metrics 的 worst case（§1、§2）。
- individual cost 有两种 aggregation：additive 是到全部 \(k\) 位委员距离之和；\(q\)-cost 是到第 \(q\) 近委员的距离。overall social cost 再取所有 agents 的 sum（utilitarian）或 maximum（egalitarian）（§1、§2）。因此结果随这两个建模选择变化，不能把某个界当作通用“代表性”结论。
- 研究限定于 line metric。由于每人把自己排第一，排序 profile 足以计算 agents 在直线上的相对顺序；这比一般 metric 或普通选民/候选人分离的情形强得多（§1.1）。
- 对 utilitarian additive，Median Alternation 选择 \(k\) 个中间 agents。其上界随 \(k,n\) 给出：当 \(n-k\) 为偶数为 \(\sqrt{k^2(n-2)/(n(n-k))}\)，接近 \(k\ll n\) 时的 1、并在 \(k\) 接近 \(n\) 时趋近 2；任何规则对 \(k\ge3\) 仍有至少 1.0914 的下界（Theorem 3.1--3.2、Table 1）。
- 对 utilitarian \(q\)-cost，当 \(q\le k/2\) 没有常数 distortion；当 \(q>k/2\) 可达 3。特别 \(q=k=2\) 时，中位附近的规则达到最优 2（偶数 \(n\)），奇数 \(n\) 的 Favorite Couple 达到最优 \(4/3\)（§3.2、Theorem 3.3）。
- 对 egalitarian additive，\(k\)-Extremes 从两端各选约半数；\(k=2\) distortion 正好为 1，较大 \(k\) 的界接近 1.5，而全局上界为 2（§4.1、Theorem 4.3）。对 egalitarian \(q\)-cost，\(q>k/3\) 时 \(k\)-Extremes 达到紧的 2；\(q\le k/3\) 时任何规则都不可能有常数界（§4.2、Theorem 4.4--4.5）。
- 所有结论为证明性最坏情况 bounds，并非用户研究、模拟实验或真实 peer-review 数据评测。论文的例子包括组织选委员会、学术聘任/晋升和学生代表，但这些是动机，不是验证数据（§1、§5）。

## 适用边界与复现

- 需要共同的一维 latent metric、严格且完全的 rankings、每人自身为最优项、所有人同时可当候选人，以及固定 committee size。真实同行选择常有多维专长、缺失/并列排名、利益冲突、候选资格约束、群体配额和非距离型偏好，不能直接套用这些常数。
- distortion 只比较隐藏距离定义的 social cost，不保证程序性公平、代表性、资格、研究质量、diversity、抗操纵或参与者接受度。尤其 peer selection 中 agents 同时报他人偏好，策略性谎报与互惠操纵不在本文模型或证明内。
- “无常数 distortion”是存在同一 ordinal profile 对应的不同一致 metrics，使任何规则在某个 metric 上比最优坏任意多；不是说现实中必然失败，也不是算法运行时间下界。使用时应说明 \(q,k\) 及采用 utilitarian/egalitarian 的目标。
- 复现理论结果应固定 \(n,k,q\)、strict ranking convention、line embedding 与 metric-consistency 定义、tie/偶奇数处理；枚举或构造论文的 adversarial metrics，分别计算 rule 和 oracle optimum 的 cost，再验证比值和极限。对应用方案还须另测真实质量、操纵、群体公平、隐私与多维/缺失偏好的稳健性。

## 与 AAMAS 的关系与核验说明

这是 multi-winner voting、metric social choice 与 peer selection 的理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BEYC4030.pdf) 核对模型、四类 objective、line-order 可恢复性、Table 1 及 Theorems 3.1--3.3、4.3--4.5；没有把 worst-case metric approximation 误写为真实同行评审的质量、策略防护或公平认证。
