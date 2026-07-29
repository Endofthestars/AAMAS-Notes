---
title: "AFRC: Adaptive Responsible Compression for Federated Learning under Data Heterogeneity"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/OIBA2819"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OIBA2819.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04a"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "federated-learning", "differential-privacy", "fairness-controller", "non-iid-data"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# AFRC: Adaptive Responsible Compression for Federated Learning under Data Heterogeneity

## 一句话总结

AFRC 将异构联邦学习中的公平、隐私与压缩视为在线协调问题：PI 控制器按客户端准确率离散度调节 fairness regularization，RDP 预算控制器按剩余 $(\epsilon,\delta)$ 选择每轮 DP 噪声，并结合结构化剪枝。

## 方法与证据

- 每轮按数据量聚合 clipping 加高斯噪声的本地更新；PI 控制器以滚动 accuracy variance 与目标差作为误差，使用 projection 和 anti-windup 限制全局公平权重（§2）。
- DP scheduler 在 Poisson subsampling 的 RDP accounting 下，以剩余 privacy budget 和轮数求最小可行 noise multiplier；早期噪声较大、末期较小。服务器执行平滑的 magnitude-based structured pruning，默认最高 90%（§2）。
- 在 100 agents、200 rounds、$q=0.1$、Dirichlet $\alpha=0.1$、$\epsilon=5,\delta=10^{-5}$ 的五随机种子实验中，表 1 报告 AFRC 在 CIFAR-10 的平均准确率 78.0%、variance 0.052，Shakespeare 为 59.3%、0.035；摘要还给出简化变体的收敛邻域界（§3–4）。

## 适用边界与复现

- 公平仅以参与客户端验证准确率离散度/10th percentile 表征，不能替代群体公平、激励兼容或 client-level 伤害审计；理论保证也排除了 pruning 和时变控制器的完整动态。
- 复现需公开 non-IID partition、client sampling、模型/剪枝 schedule、PI gains 和 target variance、clipping/RDP orders/accountant、privacy budget 分配、每 client 指标及 baseline 的同等通信预算。真实部署还需验证安全聚合、失效客户端与隐私会计假设。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OIBA2819.pdf) 人工核对双控制器、定理假设与表 1；未将模拟/基准的平均改善表述为所有联邦部署中的公平或隐私保证。
