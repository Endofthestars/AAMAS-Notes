---
title: "Offline Safe Policy Optimization From Heterogeneous Feedback"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/XGRR7655"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XGRR7655.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03k"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "offline-distribution-shift", "human-label-quality", "lagrangian-tuning", "continuous-control-benchmark"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Offline Safe Policy Optimization From Heterogeneous Feedback

## 一句话总结

PreSa 面向离线、安全关键的连续控制：只用轨迹段的奖励偏好对和安全/不安全二元标注，直接优化策略而不先拟合 reward/cost model，再用单一拉格朗日目标在偏好与安全可行性之间权衡。摘要报告它在合成及真实驾驶人类反馈上优于相应基线；这仍是 3 页扩展摘要中的实验主张。

## 方法与证据

- 数据集包含偏好对 $\sigma^+ \succ \sigma^-$ 与各轨迹段安全标签 $y\in\{-1,+1\}$；问题以未知 reward/cost 的 CMDP 描述（§2）。
- 偏好部分采用基于策略相对参考策略的累计 log-likelihood ratio 的 contrastive loss，直接提高观察到的偏好概率；安全部分把同一 utility score 作为二分类式监督，鼓励安全段高分、非安全段低分（§3.1–3.2）。
- 作者把安全分类正确率阈值写为策略可行域约束，并以 $\min_\pi\max_{\nu\ge0}$ 的拉格朗日形式联合优化，避免单独 reward/cost model 与后续 constrained-RL 阶段（§3.3）。
- 评估覆盖由 SafetyGym、BulletGym、MetaDrive 派生的连续控制任务：合成反馈由累计 reward 和 ground-truth cost threshold 生成；另在驾驶情景使用真实人类反馈。比较对象包括可访问 ground-truth reward/cost 的 offline safe RL，以及安全段行为克隆和适配后的 Safe RLHF（§4）。作者报告安全约束和奖励均有优势，但未在此扩展摘要给出全部数值表与标注协议。

## 适用边界与复现

- 该方法依赖离线数据覆盖、偏好一致性和安全标签可靠性；未覆盖状态的安全性不能由段级分类约束直接推出。拉格朗日乘子与阈值 $\delta$ 的设定也会改变奖励—安全折中。
- 复现应取得论文链接的完整版本，并记录任务/离线数据生成方式、轨迹段长度、参考策略、偏好与安全标注流程、$\delta$ 与乘子更新、每个 SafetyGym/BulletGym/MetaDrive 环境的 cost 定义及随机种子。实际部署仍需独立安全验证与在线监测。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XGRR7655.pdf) 人工核对问题定义、PreSa 目标及实验范围；未将 benchmark 的安全比例外推为真实系统安全保证。
