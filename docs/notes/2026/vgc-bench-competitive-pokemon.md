---
title: "VGC-Bench: Towards Mastering Diverse Team Strategies in Competitive Pokémon"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "game_theory_mechanism", "agent_engineering"]
dblp_key: ""
doi: "10.65109/BOUG5148"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/BOUG5148.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["game_simulator_scope", "team_usage_only", "restricted_human_comparison", "opponent_distribution_dependence", "partial_observability_and_rng", "benchmark_not_general_agent_proof"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# VGC-Bench: Towards Mastering Diverse Team Strategies in Competitive Pokémon

## 一句话总结

VGC-Bench 为 Pokémon Video Game Championships double-battle 的 team-usage（非 team-building）研究提供 PettingZoo/poke-env 基础设施、70 万以上 open-team-sheet human battle logs、heuristic/LLM/behavior cloning/MARL baselines，以及 performance/generalization/exploitability/human-play protocol。论文显示：在单一 team configuration 的 mirror-match 限制下，所述方法能战胜一名职业 VGC competitor；扩大 team 集合后，单-team 最强算法退化且更可 exploit，但泛化到未见 team 有所改善。它是复杂 POSG 的 benchmark，不是通用多智能体能力或对所有 VGC meta 的超人结论。

## 方法与证据

- VGC 是 2-player zero-sum partially observable stochastic game：双方带 6 只 Pokémon，preview 同时选 4，只能两只 active，行动同步而 outcomes 含命中/伤害/次要效果 RNG；OTS 仍不公开精确 stats（§2）。这些规则与 Poke-env/Showdown 实现、generation/format、可见性和 action legality 共同定义 benchmark，不能直接等价现实团队决策。
- 作者估算 team configuration 约 \(10^{139}\)，并指出单回合 branching、hidden stats、simultaneous multi-Pokémon action 与 preview selection 造成困难（§2）。这是配置空间估算/游戏形式化，不等于训练分布真的覆盖相同规模或证明任何算法能处理完整空间。
- benchmark 提供超过 700,000 human-play OTS logs、PettingZoo parallel multi-agent integration、VGC/doubles support，并比较 heuristic、LLM、behavior cloning、self-play、fictitious play、double oracle/empirical-game-theoretic approaches（§1, §4）。日志的玩家层级、历史 meta、selection bias、许可/隐私、parser准确性以及与未来规则版本的偏移仍决定可复用性。
- 论文明确只研究 team usage，把 team building 留为 open challenge（§1）。因此方法不选择 6-Pokémon roster、items/moves/stats/Tera composition，不能宣称解决 competitive Pokémon 的完整策略问题。
- 正式目标以随机 team configuration draw 下 policies 的 expected terminal win/loss return 表示（§2.2）。uniform team draw、对手 pool、训练/评估 matchups和 exploitability定义都是协议选择；真实 tournament 有 meta、玩家 preparation、pairing和规则变化，分布不同。
- 单 team mirror-match 训练/评估时，论文报告可赢一名 professional VGC competitor；随后扩大 team set，单-team setting 的最佳算法 performance 下降、exploitability 增加，但 unseen-team generalization 变好（abstract, §1）。专业人类比较的样本、固定 team、对局数量和协议限制使其不能被概括为“AI 已超人类 VGC”。
- benchmark 还涉及 team preview、switch/target/Tera 等 action；实现错误、server mechanics、illegal action masking和 policy observation都会显著改变结果。开放代码/数据促进复现，但不替代 independent implementation、cross-version或 human-subject validation。

## 适用边界与复现

- 适用于研究竞争 POSG 中“策略随可观测 team matchup 而变”的 generalization、population training 与 exploitability。报告时应分开 in-distribution team、unseen team、mirror match、不同 opponent population与 human games。
- 不能用 VGC win rate 为现实机器人协作、安全、人机信任或一般 game intelligence 的代理。部署到线上对战还要遵守平台规则、反作弊、用户同意、服务器负载与作弊/对抗输入治理。
- 复现应锁定 Pokémon generation/ruleset、Poke-env/Showdown version、team sets/OTS、RNG seeds、legal-action masks、human-log preprocessing、training budget、opponent sampling和 exploitability estimator；并报告 confidence intervals、match count和多 seed。
- 后续应联合 team building 与 usage、跨 meta/patch generalization、hidden-stat belief modelling、robust/exploitability-aware policies、human partnership/contest protocol，以及对 human data、online evaluation与规则变更的长期维护。

## 与 AAMAS 的关系与核验说明

这是 AAMAS competitive multi-agent learning benchmark 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BOUG5148.pdf) 核验 POSG formulation、OTS double-battle mechanics、70 万日志、baseline/infrastructure、team-usage scope与 single-team human comparison；没有将受限镜像对局结果写成完整 VGC、泛化 multi-agent 或现实能力的超人证明。
