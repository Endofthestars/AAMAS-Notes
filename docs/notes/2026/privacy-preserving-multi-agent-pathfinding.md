---
title: "Privacy Preserving Multi Agent Path Finding"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "safety_verification", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/JWHZ7620"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JWHZ7620.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "multi_agent_pathfinding", "k_privacy", "mock_agents", "field_of_view_privacy", "not_cryptographic_or_full_privacy_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Privacy Preserving Multi Agent Path Finding

## 一句话总结

本文把 MAPF privacy 分为 planning-level 与 execution-level：planning 中对任一 real agent/time，messages 诱导的 possible-location belief set 至少有 \(k\) 个；kPP 令每 real agent 加 \(k-1\) 个 mock agents，联合规划 real+mock 的无冲突路径，真实 agent仅执行自己的路径。runtime privacy再把不同 agent-groups 的 FoV visibility 视为冲突，并可在 safe zones局部重规划降低 real agent cost。该是给定消息/观测模型下的 anonymity-style location ambiguity，不保证抵抗全局 observer、traffic/timing side channels、compromised dispatcher、网络攻击或法律意义的隐私。

## 方法与证据

- classical MAPF有 known graph、start/goal、discrete wait/move、vertex/swap conflicts和 SOC；本文假设每 agent知道 \(G\)，但不知others start/target，可直接即时 message（§1–2）。真实系统中的 identity、vehicle telemetry、communication metadata、maps/sensors、operator logs与 adversary knowledge不在该基础模型。
- planning belief \(b_i(\mu,t)\) 是根据 planning messages，others认为 \(i\) 在 \(t\) 可能占的 vertices；\(k\)-privacy定义为每 \(|b_i(\mu,t)|\ge k\)（Definition 3.1）。它只下界位置候选数，不保证候选分布均匀、不可链接、不可推断 start/goal/route purpose，亦不涵盖 message contents beyond该belief abstraction。
- kPP为每real agent生成 \(k-1\) mock start/target pairs，解扩大的 MAPF后丢弃mock plans。mock assignment可随机（may collide）、privacy-preserving DisCSP，或 external dispatcher；作者明确指出 dispatcher only if collaborates with an agent 才造成某种 privacy loss。assignment itself、known dummy distribution和 solver information leaks需要独立评估。
- execution-level FoV conflict：任一时刻一方位置落入另一方 FoV即 conflict；Runtime \(k\)-Privacy要求 planning \(k\)-Privacy且无 FoV conflicts。将 FoV conflicts加到 PIBT/LaCAM planners中，只强制不同 agent groups；同 group real/mock互见不泄露（§4）。传感噪声、camera range/occlusion、noncooperative observers、communication emissions和 physical collision safety未被证明。
- safe zone是其他groups保证不可见的 planned vertices，real agent可不协调地只在这些vertices重规划；摘要称 standard MAPF benchmarks上随 \(k\)/sensing range增加，runtime与 solution quality在多数case drastically increase。没有具体 counts/CI、end-to-end privacy attacks、optimality proof或 field deployment。

## 适用边界与复现

- 适合共享已知地图中组织间 route disclosure 的 MAPF research；不能作为隐私合规/匿名化或安全认证。实际 trucks/drones/robots还需加密通信、access control、data minimization、secure logging、threat modeling、collision/safety certification和法律审查。
- 复现需公开 maps/scenarios, \(k\), mock-generation/assignment method、message protocol/belief computation、PIBT/LaCAM* modification、FoV functions/ranges、safe-zone postprocessing与 SOC/runtime metrics。对每 time step audit belief cardinalities、vertex/swap/FoV conflicts和 replan violations。
- 应测 global/passive/compromised observers、timing/traffic side channels、unequal priors、dummy identification、random seed leakage、sensor noise/occlusion、dynamic obstacles/map changes和 failures。报告 privacy–SOC–runtime–feasibility Pareto frontier，不能只给 average planning statistics。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 privacy-aware MAPF 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JWHZ7620.pdf) 核验 belief-based \(k\)-privacy、kPP mock construction、FoV conflicts/safe zones和 PIBT/LaCAM adaptation；没有把模型内候选集保证写成密码学或完整隐私保证。
