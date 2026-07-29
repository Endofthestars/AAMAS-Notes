---
title: "Efficient Device-Cloud Collaborative Offline-to-Online Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/STCC8399"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/STCC8399.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02f"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["simulated_federated_rl", "data_sharing_privacy_scope", "policy_collapse_scope", "no_real_device_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Efficient Device-Cloud Collaborative Offline-to-Online Reinforcement Learning

## 一句话总结

论文提出 DCC-O2ORL：云端先在历史离线数据上训练 TD3 初始化策略，按 advantage/PER 选取高价值经验下发给客户端，再与本地在线经验混合做联邦微调，旨在缓解 offline-to-online 转换初期的 policy collapse。

## 方法与证据

- 云端离线预训练后计算 offline samples 的 advantage，选出 `D_off`；服务器将初始 global model 与该子集广播给 clients。每个 client 将 `D_off` 与本地在线经验放进 replay buffer，周期性上传加密模型更新供服务器聚合（§3）。
- 论文把选样、下发和联邦 online fine-tuning 组成两阶段 DCC-O2ORL；早期训练可重做选样。其核心实证比较是 prioritized experience replay（PER）选样与无离线数据、随机、全量、balanced replay 等策略（§3--4.3）。
- 在 D4RL/MuJoCo 的 HalfCheetah、Hopper、Walker2d 及不同数据质量上，与 TD3-all 和 TD3+BC 比较。Table 1 中 DCC-O2ORL 在多数条目为最高或接近最高，例如 HalfCheetah random 为 `5902.79±63.73`，对 TD3-all 的 `4474.91±95.00`；但 Walker2d random 为 `42.11±36.85`，远低于两基线，故“所有场景稳定提升”不成立。
- Figure 2--3 显示其在部分任务的转换初期较少出现性能下降；该“policy collapse mitigation”仅在所列模拟任务、实现和评价回报下得到支持。

## 适用边界与复现

- 实验是单机 MuJoCo/D4RL 仿真，并未实测真实设备、无线通信、异构硬件、掉线、非 IID clients、能耗、延迟或对抗性参与者；不能据此推断 device--cloud 部署效率。
- 客户端获得 cloud offline experiences，可能产生数据泄漏/重识别、许可、数据主权和训练数据投毒风险。摘要只称更新加密、引用隐私工作，未定义安全协议、威胁模型或 privacy evaluation；因此不能把“privacy-preserving”视为已验证属性。
- advantage 选样依赖云端 critic/数据分布；跨域分布偏移、差质量数据与 local objective 差异仍可能造成负迁移，Walker2d random 的结果已显示性能并非一致改善。
- 复现需发布 clients 数/聚合规则/轮数、offline-to-online 切分、TD3/PER 与 advantage 细节、选样比例、通信/加密实现、全部 seeds 和曲线；部署前还需做真实网络基准、隐私攻击/防御审计与安全约束评估。

## 与 AAMAS 的关系与核验说明

这是联邦式多智能体强化学习与 offline-to-online 转换的工程方法。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/STCC8399.pdf) 核对 §3--5、Table 1 和 Figures 2--3，并保留失败/边界情形而未将其写成现实隐私或设备性能保证。
