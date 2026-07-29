---
title: "Detecting Approximate Clones under Approval Voting"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "game_theory_mechanism", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/MBRB4492"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MBRB4492.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02p"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "approval_asymmetry", "complexity_result_scope", "real_election_interpretation", "no_causal_inference"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Detecting Approximate Clones under Approval Voting

## 一句话总结

论文把 approval ballot 中“支持者集合完全相同”的 perfect clone 放宽为近似克隆，并以候选人支持者集合的对称差定义集合内最大距离 \(\mu^H_{max}\) 或两两距离和 \(\mu^H_{\Sigma}\)。寻找给定规模/质量的 clone set，或把候选人划分为近似 clone sets，在一般情形均难解；文章给出按候选/投票人数等参数的 FPT/XP 边界并在真实 approval election 上探索。该工具可揭示重复候选或偏好群体结构，不能单凭统计相似性认定候选串通、选民阵营或资源分配不公。

## 方法与证据

- 两候选的距离是支持者集合的 symmetric difference。对候选集合 \(C\)，\(\mu^H_{max}\) 取任意候选对的最大距离，\(\mu^H_{\Sigma}\) 累加全部候选对距离；值越小越接近 perfect clone（§1--2）。这两个指标把“不支持”与“支持”同等对待。
- 研究两个判定问题：是否存在至少 \(k\) 个候选、质量不超过阈值 \(q\) 的 approximate clone set；以及能否按最多 \(t\) 个集合、每集合最大大小 \(b\)、质量 \(q\) 将所有候选分区（§2）。
- 表 1 显示 clone-set 问题按候选数 \(m\) 或选民数 \(n\) 为 FPT；按 \(q\)、\(k\)、最大支持者数等会出现 XP/W[1]-hard 或未知边界；最大 ballot size \(A_v\) 下为 NP-hard。表 2 显示 partition 问题在完美克隆 \(q=0\)、\(b\le2\) 或 \(t=1\) 等特例可多项式求解，而容许非零误差、较大分区或较多集合通常 NP-complete（§2、表 1--2）。
- 文章还在美国最高法院 yes/no 选举与 Pabulib participatory budgeting 数据上寻找近似克隆；扩展摘要未给出所选阈值、样本量、具体发现或稳健性统计（§2）。

## 适用边界与复现

- 在 PB 中，大量未获支持的候选会显得彼此接近，即使没有选民同时支持它们；作者建议先按支持数范围筛候选。是否把未批准视为明确反对，是决定性建模选择。
- 克隆结构可用于审计候选冗余、项目主题或转置选举中的偏好相似群，但不能推断因果、组织关系、恶意操纵或代表性；需结合题目文本、地域、人口统计和制度规则。
- 复现应版本化 approval matrix、预处理与缺失规则，枚举 \(q,k,b,t\) 和支持数筛选阈值；分别实现 max/sum 距离与 exact/parameterized solver，报告解、运行时、参数、稳定性和对随机置换/抽样的敏感性。

## 与 AAMAS 的关系与核验说明

该文连接计算社会选择、选举审计和参数化算法。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MBRB4492.pdf) 人工核对两种度量、两个任务、表 1--2 的复杂度概览及两个真实数据来源；没有将近似克隆检测解释为行为或公平性的定论。
