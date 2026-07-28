---
title: "Constrained Multi-Agent Reinforcement Learning with MAF-Net for Safe Trajectory Planning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/MQDV9851"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQDV9851.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["custom_simulation_scope", "rule_based_action_mask", "two_dimensional_fixed_flight_level", "shared_state_assumption", "chance_constraint_proxy", "no_operational_certification"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Constrained Multi-Agent Reinforcement Learning with MAF-Net for Safe Trajectory Planning

## 一句话总结

IDDPG-MAF 将 independent DDPG + constrained policy optimization 与预训练、可微的 Multi-head Action Filter Network 结合：按 rule-based time-dependent mask 将连续航向动作标成 unsafe/desired/undesired，投影危险动作、保留期望动作并惩罚其他安全但低效动作。自定义多飞机雷暴仿真中它降低 LOS、提高到达率；但滤器安全性受二维运动、共享状态、30 NM probes 和规则 mask 的正确性限制，不是飞行运行许可或碰撞安全认证。

## 方法与证据

- 任务是 fixed flight level 的二维 rerouting；每秒 aircraft 共享 position/heading/speed/route，action 为每步 \([-30°,30°]\) heading change（§3）。作者明确假定高度变更很少使用、雷暴高度超民航性能；未建模三维机动、爬降、飞行性能包线、ATC 指令、通信/定位延迟、不同机型、人员因素或失效处置。
- 约束是 aircraft-aircraft minimum separation 与 aircraft-storm ellipse distance 的 chance constraints，容忍概率 \(\epsilon\)；position noise 为每步 displacement 的乘性高斯噪声 \(u\sim N(0,\sigma^2)\)（§3.1）。环境中的 binary violation reward/penalty 与平均 LOS 是代理指标，不是经验证的碰撞概率、wake turbulence、airspace compliance 或 ACAS/法规安全边界。
- CTDE 下 centralized critic 见所有 aircraft state/action，decentralized actors 仅用本地 state；论文假定 transition 因子化，inter-agent coupling 交由 joint reward/weather/safety costs 经验处理（§4.1–4.2）。实机若共享 state 的频率、延迟、丢包、身份/意图质量不同，协调结果不保证保留。
- MAF mask 对 candidate absolute heading（非仅 delta）以 12 个 30° bins、30 NM sensor probes 分类：unsafe=0（会 LOS）、desired=1（向 exit 的 30° buffer）、undesired=0.5（安全但偏离）（§4.3.1）。因此关键“安全动作集”不是从数据或形式验证自动得出，而是实时规则与观测计算的；传感盲区、预测误差、错误 storms/traffic track 会传入 filter。
- MAF-Net 预训练时对随机 action 使用该 mask 标签：Head-1 将 unsafe 投影到最近 safe alternative，Head-2 identity-preserve desired，Head-3 对 undesired 加距离 penalty；网络训练中固定但将 filtered action 放入 replay，仍在过滤后加 Gaussian exploration noise（§4.3.2–4.4, Alg.1）。可微并不证明投影后的动作持续安全，尤其 filter 后再加噪声；CPO 训练约束也被作者明说不保证 execution action safety。
- 评测为 custom 200×200 NM² simulator：400 knots、5 NM separation、50–90 knots storms、10–25 NM radius、storms 每五步更新、12 秒 timestep/最多 150 steps（30 min）；比较 FMT、DDPG、作者 IDDPG 与 IDDPG-MAF，主要表为 100 runs（§5）。这不是经过认证的 flight simulator、真实雷达/航迹/天气数据或 hardware-in-the-loop 验证。
- Table 2：4/6/8 架时 IDDPG-MAF 的 aircraft/storm LOS 为 0%/0%、0%/1%、0%/1%，goal reach 为 100%/99%/99%；FMT 在 8 架为 17%/1%、82%，DDPG 为 1%/15%、84%，IDDPG 为 0%/5%、95%。这些是该 scenario generator、mask/threshold与100次测试的经验结果，不可推出“所有密集空域均 >99% safe separation”。
- Scalability table 在 100 test runs 报 200×200 到 600×600 NM²、5 到45架的 99–100% goal reach（Table 3），但未同时列 45 架的 aircraft/storm LOS、计算延迟/吞吐、通信负荷或 worst-case conflicts；goal reach 不能单独代表安全扩容。
- 不确定性扫 \(\sigma\) 时，\(\sigma=0.5\) 为 aircraft LOS 1.5%、storm LOS 3.0%、goal 95.5%；\(\sigma=1\) 则为 7.5%/17.5%/75%（Table 4）。这直接表明在较高噪声下非零风险和目标失败；任何 operational claim 必须匹配测得的 uncertainty calibration。
- 作者明确限制为更复杂环境下 shared-network training 可能难稳定、storm tracks 被无不确定性观测、MAF 依赖 rule-based mask；建议 future work 是 probabilistic forecasts/adaptive masks/更广泛机器人测试（§5.4–6）。

## 适用边界与复现

- 可作为连续动作 MARL 中 differentiable safety-filter 的仿真研究基线。不得直接将其作为 aircraft separation assurance、ATC automation 或 autonomous release；生产飞行需要独立已认证的 separation assurance/ACAS、rule compliance、controller authority、failure-safe fallback 与监管批准。
- 部署前需把 raw surveillance/weather forecast 误差、延迟/丢包、storm nowcast uncertainty、wake/vertical separation、aircraft dynamics/turn-rate、restricted airspace、mixed equipage和 human-controller coordination 纳入高保真仿真及 shadow/HIL 评估，报告每 flight/每 encounter 的最大/累计风险、near miss、worst-case loss、P95 inference latency与通信负荷。
- rule mask 应单独版本化、测试和监控：记录每次 raw/filtered/noisy action、mask bin/原因、projection距离、约束 slack、filter coverage/false safe/false unsafe；对 filter 失效使用独立 runtime monitor 和保守 emergency maneuver，而不能以 learning reward 代替 hard guard。
- 复现应固定 simulator seeds/entry timing/exit routes/storm trajectories、2D dynamics/noise、5 NM/30 NM/12-bin mask和标签、CPO \(\epsilon\)/reward weights、MAF architectures/loss/\(\zeta=1\)、training 20k episodes/150 steps/100k replay/512 batch、baseline tuning以及各 density/\(\sigma\) 的 100-run protocol。应补报 45 aircraft 的 LOS/latency及独立 OOD weather/traffic results。

## 与 AAMAS 的关系与核验说明

这是 constrained MARL multi-aircraft trajectory planning 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQDV9851.pdf) 核对二维/共享状态假设、chance constraints、CTDE+CPO、rule-based MAF heads/训练执行、custom simulator、baseline/LOS/goal结果、不确定性扫与作者限制；没有把 simulation filter 或平均 LOS 误写为真实航空认证、零碰撞保证或可直接部署的 autonomous ATC。
