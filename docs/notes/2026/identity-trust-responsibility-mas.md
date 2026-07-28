---
title: "The Triad of Identity, Trust and Responsibility in Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "game_theory_mechanism", "safety_verification"]
dblp_key: ""
doi: "10.65109/VTZX9616"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VTZX9616.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["iterated_prisoners_dilemma_scope", "trust_transitivity_assumption", "normative_responsibility_definition", "scenario_not_deployment_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# The Triad of Identity, Trust and Responsibility in Multi-Agent Systems

## 一句话总结

本文扩展 Computational Transcendence 式的 elastic identity agent：agent 按自身 elasticity 与对其他 agent 的 semantic distance 把他人效用纳入决策，并沿网络传播间接 trust；在 25-agent Iterated Prisoner’s Dilemma 仿真中提高合作与总福利，但“责任/信任”是该模型的规范化定义，不是现实系统的 accountability 认证。

## 方法与证据

- 每个 agent 有 elasticity γ（多大程度在乎直接邻居福利）与 directed semantic distance d_a(b)；utility 是自身 payoff 与 identity-set 邻居 payoffs 的加权组合，低 d/高 γ 代表更强认同（Eq. 1、§4）。
- 交互后 agent 比较来自邻居的相对 reward/cost，更新 semantic distance；对 connected non-neighbours，用 shortest-hop path 上 edge distances 的几何式聚合推得间接 distance/trust，disconnected agent 取无穷距离（Eq. 2--5、§4）。
- 实验让 Erdős–Rényi、Watts–Strogatz、Barabási–Albert networks 上的 25 agents 进行 IPD：先 100 rounds、更新 distances、再 100 rounds；每个 setting 10 seeds，基线为 Random 与带 10% 随机性的 TFT(0.9)（§5）。
- 在此模拟，CT+ 接近 60% 的 games 为 mutual cooperation；varying elasticity 的 CC 比例按 low/medium/high 为 22%/64%/83%，报告每 agent average reward 为 18031/26125/27803（§5.1--5.3）。不同 topology 的 utility 分布也不同，Erdős–Rényi 报最高 normalized-utility Nash Product（§5.2）。
- 供应链间接 trust、攻击者/defender、气候合作均为可解释该 abstraction 的 scenarios；论文结论自己指出只聚焦一种“responsible behaviour”理解，并提出探查其他伦理原则（§6--7）。

## 适用边界与复现

- 模型把 cooperation in a chosen IPD payoff matrix 视作 responsible；现实责任还涉及权限、因果归责、可审计证据、法律义务、伤害/补偿和人类治理，不能由 higher cooperation 或 Nash Product 直接推出。
- 信任沿 shortest path 的 transitivity、semantic distance 的 reward/cost update、cost 可忽略等均为建模假设；恶意中介、sybil、collusion、观测噪声、冷启动、身份伪造与非平稳偏好可能破坏该传播。
- 网络安全、供应链与气候示例未做 domain data、attack simulation、对手策略、stakeholder study 或 deployment evaluation；不得据此把 CT+ 用作防御/治理系统的安全承诺。
- 复现应发布 graph generator/parameters、IPD payoff、γ distribution、initial distances、update cadence/λ/ε、strategy tie-breaking、seeds、reward/cost definition 与 all topology results；并报告不同责任定义和 adversarial trust failure 下的敏感性。

## 与 AAMAS 的关系与核验说明

这是将身份、信任传播与重复博弈合作结合的多智能体社会推理工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VTZX9616.pdf) 核对 Eq. 1--5、IPD 设置、§5 数值与 §6 情景性质；没有把模拟中的合作提升表述为现实可信/负责 AI 的证明。
