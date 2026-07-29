---
title: "Fast and Robust Information Spreading in the Noisy PULL Model"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "norms_trust_governance", "argumentation_reasoning"]
dblp_key: ""
doi: "10.65109/FFHM1865"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FFHM1865.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "theoretical_distributed_protocol", "biased_noise_assumption", "quasi_self_stabilization", "not_network_deployment_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Fast and Robust Information Spreading in the Noisy PULL Model

## 一句话总结

本文研究 noisy PULL(\(h\)) 模型中的 majority rumor spreading：每轮每 agent 从 \(h\) 个随机 peer 被动读取、消息经带偏置的随机噪声信道。2-bit/4-symbol 的 quasi self-stabilizing SSF protocol 从任意初始内部状态出发，以高概率在 \(O((n/h)\log n)\) 轮达成 source-majority opinion；当 \(h=n\) 为 \(O(\log n)\)。这是满足其同步轮次、随机采样、偏置噪声和可用元信息假设的理论结果，而不是现实网络、恶意攻击或生物群体的实测性能。

## 方法与证据

- 有 \(n\) 个 binary-opinion agents，sources 的多数定义 correct opinion；每个同步 round 每 agent pull \(h\) 个随机 peers 的 alphabet \(\Sigma\) 消息。信道噪声要求“biased”：原符号保留概率略大于 \(1/|\Sigma|\)（§1）。若噪声无偏/相关/对抗、topology 非随机、消息丢失/延迟或 peers 可被控制，结论不自动适用。
- 先前 lower bound 是任意 protocol 需要 \(\Omega(n/h)\) rounds（constant success probability）。SSF 用 4-symbol alphabet，从任意初始 state 以 high probability 在 \(O((n/h)\log n)\) 收敛；相比 lower bound 差一个 log，作者解释为 high-probability 与 constant-probability 保证之间可能的差别（§1）。因此“optimal”应理解为该模型/概率标准下 up to logarithmic factor。
- quasi self-stabilization 不是传统完全 adversarial self-stabilization：允许可靠访问某些信息，例如 population size、noise distribution 或 agent 是否 source（§1）。这减弱了初始化/知识假设，不能把 SSF 当作不依赖身份、规模、信道参数的自稳定协议。
- SSF 建基于同步启动时 1-bit SF：Phase 1 从 first-hand source observations 得到略偏于正确的 weak opinion；Phase 2 对 weak opinions majority amplify。为处理不同启动/时钟，SSF 把协调嵌入 2-bit message（第一位 source marker、第二位 weak opinion），但接收时二者都可能翻转（§1.1）。完整 proofs 在作者给出的 arXiv full version，三页摘要本身未给概率常数、完整 state machine 或证明。

## 适用边界与复现

- 适合分布式算法、群体信息传播和噪声通信的理论研究；不应据此直接设计安全、医疗、金融、选举、传感器网络或社交平台的共识机制。现实系统还需身份认证、拜占庭容错、消息延迟/丢包、拓扑、隐私、操纵与公平性分析。
- 复现需精确定义 source fraction/majority gap、\(n,h\)、sampling replacement、alphabet/channel transition matrix及 bias、同步 round/start model、quasi self-stabilization 中可靠信息、SSF state machine/phase logic和 success/stabilization event。用不同 n/h/noise/gaps 多次模拟，报告收敛分布、失败概率与常数，而非只拟合渐近阶。
- 应测试 correlated/adversarial noise、heterogeneous degree/graph constraints、unknown n/noise、source churn、clock drift、message loss及 network partitions；与 1-bit SF、传统 self-stabilizing 和具身份验证 protocols 比较。若用于可信信息传播，需独立来源验证、攻击监测、审计和安全回退，不能将“majority sources”视为事实真相机制。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 distributed multi-agent coordination/rumor spreading 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/FFHM1865.pdf) 核验 noisy PULL 定义、SSF/SF、2-bit、\(O((n/h)\log n)\) 与假设范围；没有把理论 high-probability 收敛写成真实通信或真伪判断保证。
