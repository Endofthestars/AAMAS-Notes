---
title: "Stochastically Dominant Preference Optimization: Policy Improvement for All"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "norms_trust_governance", "agent_engineering"]
dblp_key: ""
doi: "10.65109/KBIV4686"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KBIV4686.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03m"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "ranking-consistency-assumption", "limited-evaluation", "preference-heterogeneity", "policy-support-dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Stochastically Dominant Preference Optimization: Policy Improvement for All

## 一句话总结

SDPO 处理彼此异质的用户排序反馈：它不拟合一个折中的平均 reward，而要求新策略相对初始策略对每位排序者都满足随机占优，因而对任一与该排序一致的非递减社会福利/奖励函数都不变差。作者在双排序者 Point Bot 上报告其保留两种高质量行为，而 reward-model 与 self-play preference optimization 会牺牲其中一方。

## 方法与证据

- 对初始策略 $\pi_0$、输出及每名用户的排序 $\sigma_j$，定义 $\pi\succeq_{\sigma_j}\pi_0$ 为：对所有与该排序一致的 reward，$\pi$ 的期望 reward 不低于 $\pi_0$（Definition 1）。这比优化平均效用更强，目标是同时覆盖所有 $j$。
- Proposition 2 给出可行的概率质量转移：仅从在所有排序中较好的输出 $y$ 转给较差的 $y'$ 会维持占优（原文符号以逆排序写出）；算法随机排列排序者，反复把概率重分配给其最佳、且相对所有排序均满足条件的输出。
- 以生成的目标分布加权初始策略样本的 log probability，并用 REINFORCE-style policy gradient 训练；无需显式 reward estimation（Approach）。
- Point Bot 中两位 ranker 都偏好短路径，但一位无视灰区、另一位避开灰区。Table 1 报告 SDPO 对两个排序者的 stochastic dominance 为 100.0%/98.8%，且 utilitarian improvement 为 1.090；RM 与 SPO 会让至少一个排序者的指标变差。该结论来自单一示例环境和作者定义的采样配对测量。

## 适用边界与复现

- 保证只针对已给出的 ranking-consistent reward class 与从 $\pi_0$ 支持中重分配概率的设定；它不自动解决新输出探索、排序冲突的语义质量、稀疏或对抗反馈。
- 完整复现应公开 Point Bot 动力学、演示与灰区偏好、ranker 排序、初始 BC policy、目标分布构造次数、REINFORCE/基线/SPO 的超参、随机种子和严格的 dominance 检验。还需要在更多用户、更多任务和真实偏好噪声上验证。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KBIV4686.pdf) 人工核对随机占优定义、算法概要与 Table 1；未把 Point Bot 的保证泛化为任意真实 RLHF 系统中的公平性保证。
