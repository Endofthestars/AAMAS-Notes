---
title: "Token-level Advantage Policy Optimization from Negative Feedback in Multi-Turn Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "marl_coordination", "applications"]
dblp_key: ""
doi: "10.65109/RDEZ2224"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RDEZ2224.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["sparse_terminal_reward_scope", "entropy_threshold_tuning", "benchmark_only_evidence", "policy_optimization_safety_not_established"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Token-level Advantage Policy Optimization from Negative Feedback in Multi-Turn Agents

## 一句话总结

TAPO 是面向稀疏终局 reward 多轮 agent 的后训练方法：从同一起点的一组成功/失败 rollout 算 group-relative advantage，将其广播到 token，并仅在高 entropy、由 agent 生成的 action tokens 上优化；论文在 WebShop、ScienceWorld、ALFWorld 的特定训练设置下报告 Qwen3-4B 平均 89.4。

## 方法与证据

- 方法旨在避免 RFT 丢弃失败轨迹与 DPO/ETO 依赖固定 win-loss pair：对同任务起点的 G 条 reference-policy trajectories，将各自 terminal reward 在 group 内标准化为 advantage，因此可利用未配对成功/失败样本（§1、§3.3）。
- 每条 trajectory 的 group advantage 被赋给其 tokens；entropy selector 以阈值 η 选取高 entropy token，并用 mask 排除 prompt 与 environment feedback，仅让 agent-generated action tokens 接收 policy gradient（Eq. 1--2、§3）。
- 论文还加入 auxiliary cross-entropy 以稳定训练、缓解偏离 SFT language knowledge；这不是逐步 ground-truth reward 标注，也不声明可准确定位真实因果错误 token（§3、§4.3）。
- 在 WebShop、ScienceWorld、ALFWorld 上，Qwen3-4B TAPO 的 table-average 为 89.4，SFT 为 74.2；对应 DPO/RFT/NSR/PMPO-AR 为 80.2/84.4/85.6/84.4（Table 2）。评估将不同环境 reward 线性缩放到 0--100，报告 8 个独立 trial。
- 消融中移除 TAPO loss、CE 或 entropy filter 分别令文中比较平均从 87.0 降至 81.7、85.3、83.6；η=0.01 在 ScienceWorld/ALFWorld 的报告设置最优，约滤掉半数低 entropy tokens（§4.3）。实现基于修改版 openrlhf，使用单台 8×NVIDIA A800 server（§4.1）。

## 适用边界与复现

- 终局 reward 的相对 advantage 仍会广播给轨迹内的被选 token；high entropy 是启发式“决策关键”代理，并不证明 token 的因果责任或防止 reward hacking。
- 结果来自三种文本/交互 benchmark、给定 SFT base、rollout 与 reward scaling；不能推断到任意工具、长程真实任务、对抗环境或安全关键 agent。
- 最优 η、learning rate 和 rollout group composition 均依环境/模型而变；文中 Qwen3-4B 超过 8B 的现象也被作者归因于 hyperparameter sensitivity 与 task/model capacity 交互，不能把规模趋势当定律。
- 复现应发布 prompt、task split（seen/unseen）、environment version、reward normalization、G、η、KL/CE 权重、token masking、sampling seeds、epochs、GPU/precision 和所有 failure rollouts；另行评测安全、成本、工具副作用与分布外鲁棒性。

## 与 AAMAS 的关系与核验说明

这是多轮 agent RL/后训练工作，重点是从负反馈和稀疏 reward 做 token-level credit assignment。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RDEZ2224.pdf) 核对算法、Table 2、§4.1--4.4 与实验硬件；没有把 benchmark 成绩表述为通用 agent 能力或安全保证。
