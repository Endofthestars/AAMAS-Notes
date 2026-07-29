---
title: "Let Leaders Play Games: Improving Timing in Leader-based Consensus"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/KDLJ1170"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KDLJ1170.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "leader_based_blockchain_scope", "two_proposer_mechanism", "gamma_delay_simulation", "valid_blocks_assumed"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Let Leaders Play Games: Improving Timing in Leader-based Consensus

## 一句话总结

本文针对 leader-based blockchain 中已知下一 slot proposer 因较快网络而延迟 block announcement、以截取后续交易 fee/MEV 的 timing game，提出 2‑Prop：每 slot 选择两 proposer，各自只提一 block，attestors 在截止前为所有收到的有效 block 投票并记录相对到达顺序；若两个均达阈值，确认一个并按先到 votes 比例分 reward。Latency Game 显示同质网络中零延迟是 NE，异质 Gamma-delay 参数下快 proposer 通常也不延迟，除非另一方极慢；这是协议/网络分布/valid block 假设下的激励分析，不等于完整共识安全、抗 MEV 或主网性能证明。

## 方法与证据

- timing game 是 fast proposer 在 \(\delta\in(0,\tau_1]\) 延迟发布以纳入 \(t=0\) 到 \(\delta\) 到达的交易，获取本应落到下 block 的 fees/MEV（§1）。文章把 proposer identities/slot leader 预知、block有效、交易收益随 delay 单调增加作为模型基础，未建模 censorship、reorg、equivocation、bribery、builder/relay、private order flow、cross-slot collusion、validator centralization或攻击者控制多个 proposer。
- 2‑Prop 从 \(n+2\) validators 选 2 proposers，剩余为 attestors；每 proposer独立构造并宣布一个 block，attestors在 \(\tau_1\) 前对每个收到的 valid block attestation，并标记哪个先到（§2）。若两 blocks 都未达 \(K\) 则不确认，只有一个达阈值则确认它，两者均达阈值则随机确认 \(B_k\)，并按 \(R_i=Y_i/(Y_i+Y_{i+})\) 分享确认 block reward；论文没有讨论双 block bandwidth/验证开销、attestation duplicates、liveness under partitions、slashing/invalid blocks或与现有 protocol state transition的兼容性。
- 网络到达时间 density \(f_P\) 被假定 unimodal、support \([0,\infty)\)，对解析结果另要求在 \([0,\tau_1]\) 的 restricted \(L_2\) norm 足够集中；作者说 protocol 不依此假设但 guarantee 分析变难（§2）。收益 delay value 以 Ethereum blocks 21720000–21750648 timing观察后用 \(v(\delta)=cU\delta/\tau_1,c\le1\) 上界。真实 MEV/fee distribution、mempool visibility、transaction arrival/selection与latency相关性可能不满足线性/同分布假设。
- Latency Game 有两个 proposer，策略为 \([0,\tau_1]\) 发布 delay，utility由到达/先后投票概率和 reward构成。Theorem 1 在 homogeneous \(f_{P0}=f_{P1}\)、support \([0,\tau_1]\)、\(c\le1\) 时给 \((0,0)\) Nash equilibrium（§3）；并非所有网络/收益函数/阈值的一般结论。
- 异质情形无法解析求 PSNE，作者将策略以 \(\zeta\ll\tau_1\) 离散、假定 utility Lipschitz、packet delay 是 Gamma；在 Ethereum \(\tau=12s,\tau_1=4s,n=127,K=\lfloor2n/3\rfloor+1\) 下为两组 delay distributions 计算 75 games（§3）。Claim 1 为慢 proposer不延迟；Claim 2 为快 proposer只有在慢方极慢时才可能延迟。这是数值/分布特定的 equilibrium观察，未报告client implementation、network simulation、message loss、variance/robustness或economic welfare。

## 适用边界与复现

- 适合讨论已知 leader 的 BFT/区块链协议如何通过共同提议和 reward sharing 减少某类 timing incentive；不应直接部署到持有真实资产、结算或关键系统，除非先经过完整协议规范、形式验证、经济攻击审计、测试网和治理批准。
- 复现需给 validator/proposer selection、\(\tau,\tau_1,n,K\)、attestation/receipt-order/aggregation、tie/randomness、reward accounting、valid/invalid block行为、收益数据及 \(v\) fitting、all \(f_P\)/Gamma shape-scale/\(\mu\)/\(\gamma\)、\(\zeta\) grid、payoff integrals、Nash solver和75 games原始 matrices。验证 homogeneous theorem的支持/\(c\)条件，并报告离散化误差。
- 应测试 packet loss/jitter/partitions、adversarial routing/DoS、clock skew、heterogeneous validator stakes、correlated latency、builder/relay/MEV auctions、censorship/reorg/equivocation、malicious dual proposer、reward farming、transaction fairness、liveness/safety and finality。与单 proposer、PBS/MEV-Boost及其他 anti-timing proposals比较 latency, throughput, cost, centralization和用户交易结果。
- 生产设计要结合 cryptographic eligibility、slashable equivocation rules、fair/randomized proposer selection、network monitoring、rate/bandwidth safeguards、transparent reward accounting、emergency rollback和独立 security/economic review。隐藏或调整 timing incentive不能替代共识安全证明、抗审查保障和对用户 MEV harms 的治理。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的机制设计、博弈论与 leader-based consensus extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KDLJ1170.pdf) 核验 2‑Prop流程/reward、arrival assumptions、Latency Game、同质 Theorem 1、异质离散 Gamma model、Ethereum parameters/75 games及 claims；没有把它写成 Ethereum 主网验证、无 MEV、通用 NE 或完整区块链安全保证。
