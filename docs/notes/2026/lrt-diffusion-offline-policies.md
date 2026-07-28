---
title: "Calibrated LRT Guidance for Offline Diffusion Policies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/VBFF4869"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VBFF4869.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["model_relative_type_i_risk", "k_nn_ood_proxy", "offline_critic_label_error", "equal_variance_assumption", "d4rl_scope", "no_constraint_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Calibrated LRT Guidance for Offline Diffusion Policies

## 一句话总结

LRT-Diffusion 在固定 offline dataset 上训练一个 background diffusion head 和一个由 IQL advantage top-20% actions 训练的 good head；采样时累积二者 reverse-kernel 的 log-likelihood ratio，以校准阈值/soft logistic gate 决定向 good mean 拉近多少。\(\alpha\) 因而是“在 learned background-head \(H_0\) 下错误激活 conditional pull”的 Type-I budget，而不是物理安全概率。D4RL MuJoCo 上它通常以较低 k-NN state-conditional OOD 换取较低 return，加入小 Q-step 会提高 return 也常提高 OOD；表现并非每个任务均占优。

## 方法与证据

- 先训练 IQL critic \(\hat Q,\hat V\)，以 standardized state/action 上的 advantage \(A=\hat Q-\hat V\) 全局 top-\(p\) 切分 good data（论文设 \(p=0.2\)）。global quantile 在状态覆盖稀疏时更稳定，但会把不同 state 的价值估计误差、数据密度和 reward scale 混入同一标签（§3.1、§4.1）。
- 两 head 共用 DDPM backbone/相同 reverse-time variance：unconditional head 学全部数据，conditional head 学 good subset，配合 class balancing 和可选 positive advantage soft weights。所谓“vanilla training”是没有 critic-guided diffusion loss，并非不依赖 critic：critic 决定 labels/weights（§3.2、§4.2）。
- 在 shared covariance Gaussian reverse kernels 下，每步 LLR 是到 background/good mean 距离平方差，trajectory LLR 为各 denoising steps 之和。hard threshold test 在该 simple-vs-simple/equal-covariance model 下是 level-\(\alpha\) UMP；实践用 soft logistic gate \(\mu_u+\beta(\mu_c-\mu_u)\) 改善数值稳定性（§3.3--4.3、Prop. 5.1）。
- 阈值 \(\hat\tau\) 需针对**每个 task、模型、gate/sampler 和 Q-gradient anchor**以 held-out \(H_0\) draws 校准；若部署 sampler、variance、normalization、clipping 或 Q-step 改变，原阈值的 Type-I 语义不再自动成立（§4.4--4.6、Prop. 5.3、Theorem 5.4）。
- 理论的 finite-sample level 与 return/OOD comparison 依赖 training heads、equal/匹配 covariance、calibration sampling及 offline-error split；把 \(\alpha\) 变成 OOD upper bound 还需单调性假设。它不证明真实 MDP reward、约束违例、动作可行性或长期 closed-loop safety（§5）。
- 实验为 D4RL continuous-control MuJoCo，报告 raw return、realized Type-I、以及 k-NN state-conditional OOD（若 action 距 dataset 中 k 个相近 states 的 actions 超过 q-th percentile 即 flag OOD）。后者是数据几何 proxy，不是 support density、causal OOD 或安全风险的 ground truth（§6）。
- Table 1 的典型 frontier：halfcheetah-medium-replay LRT return 558/OOD 1.14×10⁻²，Q 598/13.13，LRT+Q 615/13.93；hopper-medium-replay LRT 329/1.84，Q 363/6.32，LRT+Q 366/6.67。它支持保守性--return trade-off，非绝对性能优势。
- walker2d-medium 是反例：LRT return 568、OOD 10.79，高于 Q 的 2282/5.28 与 LRT+Q 的 2448/4.94；作者也说明部分任务/selected hyperparameters 下 LRT 可同时更低 return 和更高 OOD。故“often lower OOD”不是普适结论（§6、Table 1）。
- deliberate variance mismatch stress test 会破坏 Type-I/OOD 并降低 return，印证 calibration 不可脱离 sampler/model assumptions（§6）。

## 适用边界与复现

- \(\alpha\) 仅是模型内 Neyman--Pearson false activation rate，不能标为安全级别、事故概率、可部署风险预算或 regulatory assurance。安全关键控制还须有真实 dynamics/constraint model、shield/barrier、action bounds、uncertainty monitor和 independent validation。
- good-head quality直接继承 IQL critic/advantage label 的偏差；dataset reward corruption、sparse/biased coverage、suboptimal expert trajectories或OOD states都会使“高 advantage”与真实高回报脱节。应检验 label stability、critic calibration、per-state coverage与不同 top-\(p\)/weighting 的敏感性。
- 只在 D4RL MuJoCo offline benchmark 验证，未覆盖高维视觉、部分可观测、nonstationary dynamics、真实 robot/action latency、offline data shift、hard safety constraints或多 agent。不能从 simulator k-NN OOD 推断 sim-to-real robustness。
- 复现应固定 D4RL version/splits、state/action standardization及部署时反标准化/clip、IQL network/expectile、top-\(p\)、two-head/DDPM schedule、variance、\(\alpha,\beta_{max},\delta\)、calibration states/draws/confidence、Q-step anchor/schedule、seeds/rollouts和 OOD k/q definition；每个实际 sampler 重新校准并报告 Type-I bands、return、OOD和失败 cases。

## 与 AAMAS 的关系与核验说明

这是 offline RL diffusion sampling 的风险校准工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VBFF4869.pdf) 核对 two-head/IQL labeling、LLR/gate、校准范围、理论前提、D4RL metrics、Table 1与 variance-mismatch stress test；没有把模型相对 Type-I 或 k-NN OOD 代理误写为环境安全、真实 support guarantee或所有任务的回报提升。
