---
title: "When is Offline Policy Selection Sample Efficient for Reinforcement Learning?"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/VDEF3989"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VDEF3989.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["offline_policy_coverage_requirement", "candidate_near_optimal_value_assumption", "worst_case_exponential_hardness", "atari_ops_failure_evidence"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# When is Offline Policy Selection Sample Efficient for Reinforcement Learning?

## 一句话总结

本文研究只凭离线数据从候选 RL policy 中选取一项的 OPS：证明 OPE 可归约到 OPS，因而最坏情形 OPS 同样会指数级困难；提出以可识别 Bellman error 做选择的 IBES，在更强 coverage/近优 value-function 假设下可能比 OPE 更省样本，但 Atari 离线基准中没有方法能稳定胜过随机选择。

## 方法与证据

- Theorem 1 以对每候选 policy 运行 sound OPE 给出 OPS 上界（差一个对候选数的对数项）；Theorem 2 将 OPE 降至 OPS，Corollary 1 由已有 OPE hard instance 得 OPS 最坏情形指数 sample complexity（§3）。
- IBES 对候选 `Q` 的 Bellman error 作辅助回归、用 holdout 选择函数类并选最小估计 error。其理论条件比 FQE/importance sampling 更强：需要对 `Π ∪ {π*}` 的覆盖，且候选中有近优 `q`；BVFT 要求更强 coverage（§4、表 1）。
- 在 Cartpole/Acrobot 与 sticky-action 版本，CQL 候选由含 40% random actions 的数据生成；10 runs 的 top-1 regret 显示 IBES 比 SBV/IBES-TQ 更省样本，model selection 比固定 32/256 hidden units 更好，但条件不足时会失效（§5.1--5.2、图 4--6）。
- Atari 使用 Breakout/Seaquest DQN replay 的 100 万 transitions，一半训练 CQL candidates、一半 OPS；early/late candidates 下 FQE、IBES、FQE+IBES 都不能稳定超过 random baseline（§5.3、图 7）。

## 局限与复现

- 下界是 worst-case finite-horizon MDP 结论，并不说所有 OPS 都指数难；IBES 的正面结论恰取决于离线场景中通常不可验证的近优候选与 coverage。不能把受控 sample-efficiency 结果当作安全部署选择准则。
- Bellman error 小不必意味着 value/policy 好；函数类、auxiliary regression、数据划分、candidate construction 和 model selection 都会改变排序。Atari 的随机基线失败也显示真实 coverage 下这些诊断未足够可靠。
- 实验候选主要来自 CQL 及特定 hyperparameter sweep，control data 与 Atari replay 不能代表不同算法、非平稳环境、连续安全约束或真实策略分布。
- 复现应固定 MDP/sticky actions、behavior policy、CQL grids、candidate seeds、train/validation split、IBES function classes/hidden units、FQE/SBV/BVFT implementations、top-k regret 和所有 Atari sampling seeds；独立报告 failure cases 及比 random 的置信区间。

## 与 AAMAS 的关系与核验说明

该文研究离线 RL 的算法/超参数 policy selection。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VDEF3989.pdf) 核对 Theorem 1--2、IBES 假设、表 1 与图 4--7；未将 IBES 的条件性样本效率外推为一般离线 RL 的可靠模型选择。
