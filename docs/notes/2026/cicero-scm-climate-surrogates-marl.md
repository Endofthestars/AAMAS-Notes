---
title: "Climate Surrogates for Scalable Multi-Agent Reinforcement Learning: A Case Study with CICERO-SCM"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "applications", "safety_verification"]
dblp_key: ""
doi: "10.65109/RJBJ9974"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RJBJ9974.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "climate_surrogate", "cicero_scm", "marl_climate_policy", "trajectory_replay_validation", "not_climate_policy_or_scientific_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Climate Surrogates for Scalable Multi-Agent Reinforcement Learning: A Case Study with CICERO-SCM

## 一句话总结

作者以 20,000 条扰动 SSP2-4.5（2015–2075）multi-gas emissions pathways 训练 RNN surrogate 近似 CICERO-SCM 的 annual 40-gas→global mean temperature update。Table 1 中 LSTM/GRU test RMSE 约 \(4\times10^{-4}\) K、GPU per-step约 0.0004 s（CICERO约 0.4 s），MARL env step 约加速 137×；4-agent scenario 与原 simulator 对训显示接近 policy ordering，10-agent heterogeneous setting仅能以 original simulator replay surrogate-trained trajectories。它可减少指定 SCM 在该 distribution 的训练成本，不能代表 Earth-system fidelity、区域气候影响、真实政策最优性或替代气候科学/治理评估。

## 方法与证据

- CICERO-SCM mapping 40 greenhouse gas annual emissions 到 global mean \(\Delta T\)，摘要称约0.4s/call。RNN 输入 recent-emission window并输出 next-year temperature；training ensemble围绕 SSP2-4.5，用 CO2 fossil/land-use、CH4、N2O、SO2 的 year-over-year growth ±7.5% perturbations（§2）。其它 scenarios、extreme tipping/feedback、regional distributions、emission accounting error与 long extrapolation不由此训练集覆盖。
- MARL climate-economic Markov game：regional agents选择 discrete decarbonization/methane/land-use/adaptation actions，centralized observations，reward合并 mitigation/adaptation costs与 climate damages。action/reward/economic/negotiation/justice formulation是该 toy environment，未等同真实国家政策、political economy、international law、uncertainty或 social impacts。
- scenario (i)为 4 homogeneous agents + one mitigation lever，可用surrogate和CICERO direct train；scenario (ii)为10 heterogeneous agents+multiple levers，原 simulator training deemed intractable，故只用 surrogate train（§2）。因此“same policies as simulator”有直接支持仅限(i)；(ii)不能直接比较 learned policy。
- empirical policy consistency：replay surrogate-induced trajectories in CICERO，比较 temperature RMSE与 returns’ Kendall \(\tau\)。Table 1 LSTM/GRU policy-induced RMSE约 \(2.0\!\sim\!5.9\times10^{-4}\)K、rank-\(\tau\) 0.990–0.997；在(i)政策order与direct comparison一致。replay只验证已访问 trajectories，依赖 surrogate/simulator trajectory sets error趋零的假设（Eq.3），无法排除 optimizer exploiting off-distribution surrogate errors。
- 速度：LSTM inference CPU/GPU 442×/1161×，GRU 202×/1161×；完整 scenario(i) env step均137×，非“每任务均>100×”；TCN policy-induced errors较大、环境49×。摘要没有 energy/carbon footprint、surrogate training cost、random seeds/CI、economic sensitivity或 independent climate validation。

## 适用边界与复现

- 适合用于快速筛选指定 climate-economy MARL environment 中的候选策略，再用权威 simulator/多模型 ensemble 做离线复核；不得以 surrogate policy 直接发布减排目标、适应投资、碳价或区域资源分配建议。
- 复现需公开 CICERO version/config、20k scenario generator/seed、all gas preprocessing/window、RNN architecture/training splits、simulator vs surrogate timings/hardware、MARL state/actions/rewards/algorithms、scenario(i)/(ii)params、trajectory replay policy set、RMSE/rank-\(\tau\)/return metrics和 CI。还应计入 training/validation cost。
- 应测试 withheld SSPs、extreme/nonlinear emissions、long horizons、multiple SCMs/ESMs、regional/sectoral metrics、damage-function uncertainty、distribution shift和 policy optimization adversarial to surrogate。报告 false ranking、worst-case temperature error、equity outcomes和 sensitivity，保持气候专家/利益相关者治理。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 surrogate-enabled climate MARL 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/RJBJ9974.pdf) 核验 20k pathways、two scenarios、Table 1 speeds/errors与 replay consistency criterion；没有把 approximation/replay证据写成真实气候政策或科学预测保证。
