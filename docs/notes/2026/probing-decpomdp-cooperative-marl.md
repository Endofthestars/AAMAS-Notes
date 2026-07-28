---
title: "Probing Dec-POMDP Reasoning in Cooperative MARL"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/ECCJ1033"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ECCJ1033.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["baseline_scope", "diagnostic_not_causal_proof", "mutual_information_estimation", "benchmark_distribution_dependence", "training_seed_variance", "return_not_safety"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Probing Dec-POMDP Reasoning in Cooperative MARL

## 一句话总结

本文提供一套审计 cooperative MARL benchmark 的 diagnostics，而非新训练算法：用 RNN 与 feed-forward performance gap 和 conditional mutual information 检验 learned policy 是否真正从 history、队友私有信息和时间依赖中获益。对 IPPO/MAPPO 在 MPE、SMAX、Overcooked、Hanabi、MaBrax 的 37 个场景、10 seeds，作者发现所有策略都有 history dependence，但仅 16/37（43.2%）有显著 memory performance advantage；许多高回报策略可能依赖 reactive shortcut 或脆弱的同步约定。结论限定于这些 baseline、训练与轨迹分布，不能泛化为任何算法均不需 Dec-POMDP reasoning。

## 方法与证据

- Dec-POMDP 含 private local observations、joint action/reward 和部分可见 global state；作者区分 structural partial observability 与对解决任务真正相关的 partial observability（§2, §4）。理论 worst-case NEXP-completeness 不自动说明某一个 benchmark 或已训策略在实践中需要 history-based coordination。
- Memory–Reactive Gap 为 matched RNN/FF policies 的 \(\Delta_{Mem}=J(\pi_{RNN})-J(\pi_{FF})\)，用 paired one-sided Wilcoxon signed-rank \(p<0.05\) 判断 memory advantage（Diagnostic 1）。它评估这两类训练产物的 return 差，不识别最优策略、因果机制或其他 memory architecture 的能力。
- History–Action Relevance (HAR) 是 \(I(H_t^i;A_t^i\mid O_t^i)\)，Observation–Action Relevance (OAR) 衡量当前 observation 对 action 的信息；Private Information Flow (PIF)、Action–Action coupling (AA)、Directed Action Information (DAI) 分别探查跨 agent 私有轨迹、即时 action coupling 和定向时间影响（§4, Fig. 1）。MI/CMI 是在收敛 joint-policy trajectory distribution 下的统计依赖，作者也指出它们不是因果关系证明。
- 试验覆盖 MPE、SMAX V1/V2、Overcooked V1/V2、Hanabi、MaBrax，共 37 scenarios；使用 IPPO 与 MAPPO，FF/RNN architectures，10 seeds，评估 return 为 32 episodes 平均（§6）。这是广但仍有限的 benchmark/baseline protocol，不覆盖 value-based、model-based、communication、transformer memory、不同 reward shaping 或更强训练预算。
- 所有 37 个 scenarios 的 learned policies 都有 HAR 超过 permutation null，但仅 16/37 有显著 \(\Delta_{Mem}>0\)；Hanabi 在这些 baselines 下没有显著 memory–reactive gap（§6.2）。因此“network encodes history”不等于该 history 对当前 return 有功能性价值。
- PIF 在 26/37（70.3%）场景超出 null，DAI 在 30/37（81.1%）超出 null；AA 与 DAI 可分离，表明同步 coupling 不等于持续的 temporal influence（§6.2）。高 AA 也可能反映效率高但与陌生伙伴不稳健的 convention，而非可解释或安全的协作。
- 作者认为 MPE 是唯一每个 tested scenario 均满足其四项诊断标准的 suite；Overcooked V1→V2 在 private-information 需求上的差异支持 V2 redesign 的动机（§6, §9）。这是一组 policy-level diagnostics 对环境设计的证据，不是 benchmark 的绝对质量排名或对其它训练方法的保证。

## 适用边界与复现

- 适用于在以 return 为主的 benchmark 报告外，审计 partial observability 和 coordination 是否被实际利用。应同时报告 RNN/FF paired seeds、return statistics、HAR/OAR/PIF/AA/DAI、permutation null、训练曲线与失败 cases。
- 不应由高 MARL return、正 MI 或一个显著 p-value 推断 robust communication、generalisation、因果理解或真实系统安全。部署还要测 partner swap、distribution shift、observation/action delay/noise、communication failure、adversarial behavior、rare events、resource constraints 和人机协作。
- 复现须固定 environments/maps/versions、observation encoding、agent ordering、IPPO/MAPPO hyperparameters、FF/RNN capacity、10 seed pairing和 evaluation episode count；从 policy trajectories估计各信息量，并保持同一 permutation/test protocol。有限样本、连续变量离散化/估计器选择和非平稳训练都会影响 MI。
- 后续可加入 interventions/causal probes、cross-play 和 unseen partners、更多 algorithm families、scaling to longer horizons，以及把诊断用于创建“无 history/无私有协调即明显失败”的环境；论文已发布诊断代码供此类审计。

## 与 AAMAS 的关系与核验说明

这是 AAMAS cooperative MARL benchmark/evaluation 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ECCJ1033.pdf) 核验了五类诊断、37 scenarios、IPPO/MAPPO/10-seed protocol、16/37 memory gap、PIF/DAI 比例及 MPE 观察；没有把 MI diagnostics 或这些 baseline 结果写成普遍的算法能力、因果推理或系统安全证明。
