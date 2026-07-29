---
title: "A Unified Framework for Zero-Shot Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "generative_agents"]
dblp_key: ""
doi: "10.65109/TFVS6666"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/TFVS6666.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "taxonomy_framework", "unknown_downstream_rewards", "zero_shot_boundary_ambiguous", "no_new_benchmark_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Unified Framework for Zero-Shot Reinforcement Learning

## 一句话总结

本文为 zero-shot RL 提供统一记号与 taxonomy：训练 representation \(\mu\)，使未见 reward 下可经 \(F_\mu(\mu,r)\) 得到 \(Q_r^*\)，再抽取 policy。方法按 direct（直接 reward-to-value）/compositional（分解 value）及 pseudo-reward-free（训练可采样 rewards）/reward-free（representation 独立于 reward）划分。它澄清不同声称“zero-shot”的方法假设，但明确承认 test-time 可允许多少计算没有统一阈值，因此不是对泛化、样本效率或“无需推理”的可验证性能保证。

## 方法与证据

- zero-shot setting 是固定 dynamics、reward family \(\mathcal R\) 的 MDP family；训练时未知 downstream distribution \(D_{test}\)，推理时希望对未见 reward 得到 policy，且无 parameter update、显式 transition planning 或大量计算（§1）。
- direct representations 学 \(Q^*(s,a,r)\) 的端到端 mapping，并由 argmax action 抽取 policy；它不显式分解 dynamics/reward/value structure（§2.1）。
- compositional representations 学 \(\mu(s,a)\)，再通过 decomposition operator \(F_\mu\) 重构 \(Q_r^*\)。successor-feature style inner product 是其可用实例；框架本身不要求一种唯一 \(\mu\) 或算法（§2.1）。
- pseudo reward-free 训练时采样 rewards，通常要求 \(\mathrm{supp}(D_{test})\subseteq\mathrm{supp}(D_{train})\)；direct methods 必属于此类。reward-free methods 学与 reward 无关的 \(\mu^\pi\)，推理时再搜索/recover policy（§2.2）。
- 作者强调 zero-shot 边界是连续的：禁止更新 \(\mu\) 与显式 planning，但 \(F_\mu\) 的计算预算无标准定义。单次 forward pass 是严格例子，reward-free recovery search 是否仍算 zero-shot 取决于使用者延迟约束（§2.3）。

## 适用边界与复现

- 适合比较 zero-shot RL 论文的训练 reward access、representation target、test-time policy extraction与计算预算。taxonomy 不可替代在明确 OOD reward、dynamics shift 与 latency budget 上的实测。
- 复现/评审应明确 \(\mathcal R,D_{train},D_{test}\) 的 support relation，是否更新参数、是否访问 transition model、\(F_\mu\) 的搜索步骤/时间，以及 reward family外推失败率；不要把“无 task-specific fine-tuning”简化成“无任何推理成本”。
- 摘要引用 full paper 中 successor-feature extended bound，但不在三页中充分给出推导/实验；使用该 bound 时应回查完整版本的前提和符号，不能只凭此摘要推广为所有 compositional methods 的性能界。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 zero-shot RL 统一框架扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/TFVS6666.pdf) 人工核对两组分类、统一方程和 zero-shot boundary 讨论；未将 taxonomy 写成新算法或实证优越性。
