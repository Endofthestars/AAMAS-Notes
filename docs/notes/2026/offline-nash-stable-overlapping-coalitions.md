---
title: "Offline Learning of Nash Stable Coalition Structures with Possibly Overlapping Coalitions"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["marl_coordination", "game_theory_mechanism", "agent_engineering"]
dblp_key: ""
doi: "10.65109/ZZZS1209"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZZZS1209.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04d"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["coalition-formation", "nash-stability", "offline-learning", "semi-bandit-feedback", "coverage-assumptions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Offline Learning of Nash Stable Coalition Structures with Possibly Overlapping Coalitions

## 一句话总结

本文从固定历史数据学习可能重叠联盟的近似 Nash stable 策略：在对称、可加分离偏好下，利用 utility estimates 加 UCB 式 exploration bonus 优化 duality gap，并证明不同 feedback 粒度所需的 coverage 条件。

## 方法与证据

- agent 可同时加入多个 candidate coalitions，mixed/pure strategy 决定加入选择；目标是不存在单边改变策略可提升 expected utility 的近似 NS。数据只含过去 joint actions 与 semi-bandit（agent-level）或 bandit（coalition-level）反馈（§1–3）。
- semi-bandit 下 Assumption 1 的 coalition-size coverage 足以让 Algorithm 1 直接估计 pairwise utilities；Theorem 3 给出随 dataset size $M$ 约 $1/\sqrt M$ 缩小的 approximate duality-gap bound，且可修改为学习 pure strategy（§4）。
- bandit 下 Theorem 4 说明 Assumption 1 不足：存在任意数据量仍至少 $1/20$ gap 的不可区分情形；增加 Action Coverage（Assumption 2）后，ridge regression 与 bonus 的算法得到 sample-efficient 近似 NS（§5）。合成实验中随机 exploration 满足 coverage 时 gap 随 $M$ 下降，刻意不足覆盖时失败（§6）。

## 适用边界与复现

- 结果依赖独立离线 samples、对称可加偏好及覆盖假设；历史数据的“充分覆盖”通常不可由有限日志无条件保证，联盟/偏好非平稳、相关样本和战略性反馈仍开放。
- 复现需公开 action/coalition space、utility distributions、exploration policies、coverage coefficients、confidence/bonus、coordinate-descent stop rule、Monte Carlo budget和每种 $n,k,M$、seed 的 gap。应报告 coverage 诊断，而非仅在随机日志上宣称稳定。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/ZZZS1209.pdf) 人工核对两种 feedback、Theorem 3–5、coverage 假设与合成实验；未将近似 duality gap 视为真实组织中的长期稳定证明。
