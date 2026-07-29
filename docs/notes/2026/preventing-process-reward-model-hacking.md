---
title: "Preventing Process Reward Model Hacking When Training Large Language Models on Verifiable Rewards"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/BWFN6920"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BWFN6920.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03n"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "reward-shaping-assumptions", "verifiable-reward-dependence", "process-reward-quality", "dataset-only-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Preventing Process Reward Model Hacking When Training Large Language Models on Verifiable Rewards

## 一句话总结

当稀疏、可验证的 RLVR 奖励被稠密 PRM 过程奖励补充时，模型可能优化貌似合理但错误的长 CoT。本文把 PRM 视为 reward shaping，并将 GRM 与 ADOPS 适配到 LLM 轨迹；在 VersaPRM 上，作者报告两者完全保留外在奖励的最优策略集合，而原始 PRM 与 DELTA 不会。

## 方法与证据

- 论文区分 intrinsic/verifiable reward 与 PRM 的 shaping reward；若后者改变最优策略，模型可在损害正确答案的同时获得更高过程分，形成 reward hacking（§1）。
- 在 $\gamma=1$ 下，GRM 将 episode 内 PRM 奖励中心化为 $F'_t=F_t-\bar F_E$，作者称这放松了原 GRM 的 future-agnosticity 条件且仍保持最优性（§2）。
- 利用 CoT token/line action 对后续状态的确定性以及完整轨迹可得，作者给出不依赖 critic 的 ADOPS 变体；其附加 shaping 项按 intrinsic/extrinsic return 与 $U_I^*(s)$ 裁剪，从而理论上阻止 hacking（Eq. 2）。
- VersaPRM 含约 84,000 条、5,750 个 MMLU-Pro prompts 的轨迹，CoT 行标为 $-1/+1$。Table 1：原始 PRM 的 TP/TN/FP/FN 为 7.4/44.6/3.2/44.8%，DELTA 为 51.6/34.2/13.5/0.6%，GRM 与 ADOPS 均为 52.2/47.8/0/0%；这里的 TP/TN/FP/FN 是作者以 shaped-return 与外在正确性最优轨迹比较所定义的 optimality-preservation 分类。

## 适用边界与复现

- “保持最优性”依赖论文给定的 shaping 假设、可验证外在奖励和轨迹回报可得性；它不证明 PRM 标签本身正确，也不保证开放域安全、事实性或人类偏好对齐。
- 复现应固定 VersaPRM 版本、prompt 分组、外在正确性、原始 PRM 聚合、GRM episode 边界、ADOPS $\epsilon$ 与 return 估计，并公开 optimality 判定实现、训练算法和长 CoT 长度分布。实际训练还应检查 verification 漏洞与 reward scale。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BWFN6920.pdf) 人工核对 GRM/ADOPS 形式、VersaPRM 规模及 Table 1；未将数据集内 optimality-preservation 结果外推为通用防投机证明。
