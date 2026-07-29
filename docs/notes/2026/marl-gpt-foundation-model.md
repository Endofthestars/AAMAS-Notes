---
title: "MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["marl_coordination", "agent_engineering", "generative_agents"]
dblp_key: ""
doi: "10.65109/BWFP6427"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BWFP6427.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04k"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["offline-marl", "transformer-policy", "imitation-learning", "cross-domain-generalization", "benchmark-evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning

## 一句话总结

MARL-GPT 以统一 transformer encoder 从大规模 expert trajectories 离线学习，尝试用单一模型跨 SMACv2、Google Research Football 与 POGEMA 执行多 agent 决策，并在论文所测任务中与专用 baselines 竞争。

## 方法与证据

- 输入将每个 agent 的局部结构化 observation（自身、队友、对手）tokenize，并加入 feature type、agent/team identity 与 temporal embeddings，以适应 agent 数和 observation 长度变化（§1、§4）。
- 基于 expert observation–action–reward trajectories 训练 action prediction 与离散 Q-value critic，结合 behavior cloning 与 offline RL；主数据规模为 SMACv2 400M、GRF 100M、POGEMA 1B trajectories（摘要、§4、§5）。
- 在三个环境对 BC、CQL、Decision Transformer、BC-LSTM、RATE 等作比较，报告多数已测 setting 的 competitive performance；另考察未见 race/agent count 的 zero-shot 与小数据 fine-tuning（§5）。

## 适用边界与复现

- 跨域结论限于三套离散 benchmark、作者的 expert coverage、7M model 和指定训练/评估 protocol；并非对任意 MARL 环境、连续控制或真实世界迁移的 foundation-model 认证。
- 复现应固定环境版本、expert policy/trajectory splits、tokenization 与 agent ordering、history length、BC/critic losses、Q bins、offline/online fine-tuning 配置、seeds 与每项 zero-shot/fine-tuned 评估。论文给出代码链接，但笔记不假定其资产持续可用。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BWFP6427.pdf) 人工核对数据规模、模型编码、训练目标和实验域；未将 benchmark 中的 competitive result 夸大为通用多 agent 基础模型能力。
