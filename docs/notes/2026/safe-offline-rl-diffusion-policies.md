---
title: "Safe Offline Reinforcement Learning using Diffusion Policies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/QVZU7986"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/QVZU7986.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03v"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "offline-coverage-assumption", "cost-critic-conservatism", "soft-constraint", "dsrl-benchmark"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Safe Offline Reinforcement Learning using Diffusion Policies

## 一句话总结

Safe-DQL 在 Diffusion-QL 的数据流形正则基础上增加双 cost critics 与超过成本阈值的 hinge penalty，试图同时处理 OOD 和软安全约束。作者在 DSRL 的 SafetyGymnasium/BulletSafetyGym 上报告 normalized cost 接近零且 reward 有竞争力；理论安全界有明确的 critic、coverage、参考策略等前提。

## 方法与证据

- policy 是条件 denoising diffusion reverse process；reward critic 取双 critic 的最小值，cost critic 取最大值以保守估计。目标为 diffusion BC loss 减 reward Q 项，加上 $\mathrm{ReLU}(\tilde Q_c^{max}-\kappa)$ penalty（Eq. 1）。
- 采用 soft CMDP constraint。Theorem 9 称全局最小化者的真实 discounted cost 至多为 $\kappa$ 加上 conservative critic error、随 $1/\lambda$ 缩小的 penalty 项和 occupancy mismatch 项；前提包括 bounded critics、concentrability、近似误差、至少一个保守 cost critic、BC-KL 控制及可行 reference policy（§3）。
- DSRL Table 1：20 evaluation episodes、3 seeds、cost threshold 1；Safe-DQL 每个列出任务 cost 都小于 1，如 PointCircle1/CarCircle/BallRun 为 0.00/0.00/0.00，reward 分别 0.46/0.72/0.25。它并非每任务 reward 最高，例如 CarRun 0.73 低于 CDT 0.99（§2, Table 1）。

## 适用边界与复现

- 扩散行为克隆无法覆盖数据外情形；cost critic 低估、cost 定义漏项、reference policy 不可行或 occupancy mismatch 大都会削弱安全界。该方法是 expected discounted soft constraint，不是逐步零违规保证。
- 复现应固定 DSRL tasks/datasets、cost threshold、diffusion schedule、critic architecture/target updates、$\eta/\lambda$、clipping/保守性检查、reference policy和评估 episodes/seeds。安全关键部署须有独立 runtime monitor 和真实系统验证。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/QVZU7986.pdf) 人工核对目标、定理假设和 Table 1；未将 benchmark 的低成本外推为无条件安全。
