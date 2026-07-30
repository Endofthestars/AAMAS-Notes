---
title: "MininetGym: A Live Demonstration of RL-Based Cybersecurity Training"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["marl_coordination", "safety_verification", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/VVUY3381"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VVUY3381.pdf"
code_url: "https://github.com/dipi-unimore/mininet-gym"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05p"
spark_draft_verdict: "source_grounded_with_scenario_action_comparison_and_platform_claim_boundaries"
spark_qa_verdict: "needs_revision_corrected_for_link_detachment_action_platform_claim_quantitative_evidence_and_security_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["simulated_attacks_not_live_adversaries", "contextual_bandit_not_sequential_rl", "quantitative_results_missing", "algorithm_baseline_seed_variance_and_hyperparameters_missing", "traffic_and_attack_isolation_unreported", "production_authorization_unreported", "false_positive_operational_harm_unassessed", "link_detachment_availability_harm", "recovery_and_rollback_unreported", "least_privilege_unreported", "threat_model_missing", "real_incident_validation_missing", "platform_claims_not_empirically_validated"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_scenario_semantics_contextual_bandit_quantitative_evidence_network_isolation_authorization_false_positive_link_detachment_recovery_and_deployment_boundary_check"
escalation_verdict: "pass_after_corrections_for_scenario_action_platform_claim_evidence_and_network_security_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted network-safety and evidence-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# MininetGym: A Live Demonstration of RL-Based Cybersecurity Training

## 一句话总结

MininetGym 把 Mininet 的 Linux-kernel network emulation、OpenDaylight/Open vSwitch 的 SDN 数据与 Gymnasium 接口接成可交互的单/多智能体网络安全训练平台；三页 demo 说明了三个场景和操作流程，但没有报告定量结果，不能据此认定算法有效、生产网络安全或真实攻击防御已经验证。

## 系统定位

MininetGym 是一个 RL cybersecurity training/evaluation framework 与 live demonstration，不是新 RL algorithm，也不是在 production network 上进行的红蓝对抗实验（pp. 4086–4087）。

其技术栈包括：

- **Mininet**：使用真实 Linux kernel network code 模拟网络；
- **OpenDaylight + Open vSwitch**：提供 SDN control/switching 与 flow-level statistics；
- **Gymnasium**：把网络拓扑封装为标准 RL environment；
- **Stable-Baselines3 与 custom tabular agents**：作为可使用的学习器。

真实 Linux 网络栈提高了 emulator 的系统现实性，但仍不等于真实组织网络、真实攻击者或生产部署验证。

## 五个主要模块

架构分为五部分（pp. 4086–4087）：

1. web-based configuration editor，以及 real-time monitoring/control dashboard；
2. 围绕 Mininet/SDN topology 的 Gymnasium-compatible wrapper；
3. 负责 agent instantiation、training 与 evaluation 的 agent manager；
4. 生成正常与攻击流量的 traffic generator；
5. 负责 data persistence、metrics 与 plots 的 results manager。

平台支持 YAML 配置及实时校验、训练暂停与观察、多个 agent/algorithm 比较、协调过程展示，以及 raw data 和 trained model 导出。它可以生成 confusion matrices、training progression curves 与 comparison histograms；三页稿本身没有展示这些图的数值结果。

## 单智能体与多智能体机制

single-agent mode 由 manager 实例化一个学习器，使其接收 observation、选择 action 并根据 reward 更新策略。

multi-agent mode 支持：

- heterogeneous roles；
- 每个 host 对本地 network interface 的 partial observability；
- independent learning；
- explicit message-passing communication bus；
- 鼓励 collective performance 的 team rewards；
- learning algorithm hot swapping。

作者说这些机制可用于比较 centralized/decentralized learning、independent/coordinated policies 以及 communication-based/implicit coordination；论文没有实际报告这些比较的结果。

traffic module 列出的协议是 TCP、UDP、ICMP；攻击类型是 UDP flood、TCP SYN flood、Slowloris、ICMP flood、DDoS 与 HTTP。

## 三个演示场景

### Scenario 1：Traffic Classification

单个 agent 把流量分为 None、Ping、UDP、TCP 四类（p. 4087）：

- observation 是 4-dimensional state，正文只用 packets、bytes 概括其内容；
- action 是四类 traffic label；
- reward 被描述为 symmetric，但没有给出数值。

论文明确说明 samples 在 time steps 间 i.i.d.，没有 sequential dependence，所以这里的 RL formulation 实际退化为 contextual bandit。它不能作为一般 sequential RL defense capability 的证据。

### Scenario 2：Binary DoS Attack Detection

单个 agent 做 normal/attack 二分类（p. 4087）：

- observation 为 4D，并包含 over-time percentage changes，用于识别 traffic spikes；
- actions 为 report normal 或 report attack；
- reward 为正确检测攻击 `+2`、正确判断正常 `+1`、false positive `-0.1`、missed attack `-2`。

若攻击未被检测，模拟器会提高后续 attack probability。该机制模拟会增强攻击强度的 adaptive adversary，不是真实攻击者的行为测量或现场对抗。

### Scenario 3：Multi-Agent DoS Detection

每个 network node 配一个 host agent（p. 4087）：

- host observation 为 9D，包含 TX/RX packets、TX/RX bytes、variations 与 coordinator messages，仅覆盖本地 interface；
- host 的三个分类 actions 是 report normal、incoming attack、outgoing attack；
- coordinator observation 为 5D，包含 global packets、bytes、variations 与 agent messages；
- coordinator 可 broadcast alert 或 remain silent。

host 还可以在检测到 outgoing attack 时 autonomously detach its network link。detach link 是另行描述的 mitigation capability，不是上述三分类 actions 中的第四项。论文也没有给出该场景的逐项 reward 数值。

## 证据边界

三页稿没有 quantitative experiment table，也没有报告：

- accuracy 或 training-curve 数值；
- algorithms 与 hyperparameters；
- baselines 或 controlled comparisons；
- seeds、run count、variance 或 confidence interval；
- compute/hardware；
- real traffic、live attack 或 incident-level validation。

论文所用的 “realistic”“fair algorithm comparisons”“reproducible environment”“publication-ready plots” 与 “safety-critical domains” 是作者对平台能力或应用方向的表述，不是由本文定量实验建立的结论。

## 网络安全与部署缺口

把平台用于更接近真实系统的实验前，还需要处理短稿未说明的边界：

- generated attack traffic 是否被可靠限制在授权的 isolated environment；
- operator、agent、SDN controller 的 authentication、authorization 与 least privilege；
- false positive 导致误封禁、断链或业务中断的影响；
- link detachment 的审批、范围限制、恢复与 rollback；
- controller、traffic generator 与 model compromise 的 threat model；
- 数据、模型、配置和操作日志的完整性；
- production network 的 fail-safe、incident response 与 change control。

尤其是 detach link 会直接影响 availability。模拟 reward 中的 false-positive penalty 不能替代真实业务影响评估和恢复机制。

## 资源与页码核验

论文提供 [GitHub repository](https://github.com/dipi-unimore/mininet-gym) 与 [demo video](https://youtu.be/pSdEV-MSdA8)。

PDF 逐页核对：p. 4086 为 identity、Abstract、Introduction 与 System Architecture 起始；p. 4087 为 architecture continuation、workflow、three scenarios 与 Value Added；p. 4088 只有 References。三页稿没有 Conclusion 或 Future Work section。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VVUY3381.pdf) 核验；`reviewed` 表示文内事实与边界已核对，不表示算法效果、生产网络安全或真实攻击防御已经验证。
