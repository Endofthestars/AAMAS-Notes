---
title: "Team of Rivals: Hierarchical Deep Reinforcement Learning and Behavior Cloning for Multiplayer Poker"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/LRNX6318"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LRNX6318.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["poker_simulation_scope", "behavior_cloning_demonstration_bias", "identity_blind_opponent_modeling", "discrete_action_abstraction", "win_probability_oracle_feature", "limited_expert_dataset", "baseline_prompt_sensitivity", "no_multiplayer_equilibrium_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Team of Rivals: Hierarchical Deep Reinforcement Learning and Behavior Cloning for Multiplayer Poker

## 一句话总结

Havoc 是六人无限注德州扑克的两层策略：下层将每位人类专家分别做 behavior cloning（先全体预训练、再按玩家微调）得到风格专家，上层以 DQRN 根据牌局历史选择当前回合由哪名专家出牌。该组合在随机配桌仿真中以平均每局收益超过 BC-Pluribus、单个 BC 玩家和作者构建的 ChatGPT-4.0 基线，并频繁切换专家；但它不直接学习多人均衡、主策略不看对手身份，且下层动作、胜率输入和评价对模拟规则/对手池高度绑定，因此不能推出对真实对手、一般不完全信息博弈或策略性对抗升级的稳健性。

## 方法与证据

- 架构有一个 value-based master 与多个 player specialist。每次轮到 Havoc，master 从专家 bank 选择一个，下层 LSTM specialist 只执行一个离散动作；master 本身不与扑克环境直接互动（§3.1）。这使它可切换模仿风格，而不是将多个策略融合为一个可解释的均衡策略。
- 专家来自 13 名人类六人 no-limit Texas Hold’em 玩家数据，筛后保留 8 人，平均每人约 4,200 局、共 67,034 个 state。BC 先在全部局面训练 general LSTM，再冻结 LSTM 层、只微调 dense 层到个别玩家（§3.4、§4.1–4.2）。这个流程保留数据集的打法/选择偏差；BC 不证明专家最优，也不能从示范外情形恢复正确动作。
- 下层将 fold/call/raise 离散为 5 个动作，三类 raise 是相对大盲/最近加注的区间；all-in 没有独立动作（§3.3）。因此收益比较针对这一受限动作抽象，不能等同于完整 no-limit poker 的策略质量。
- 状态含活动人数、底池、call 成本、位置、按当前可见牌估的胜率，以及完整行动序列的非 Markov 特征；胜率由每手 1,000 次随机补全未知牌的模拟得到（§3.2）。该特征约需一秒/手，依赖规则正确的 rollout，且把牌面压缩为 scalar 可能抹去对 bluff/范围推断重要的信息。
- master 是 LSTM DQRN，以终局货币盈亏训练；用 9,240 个随机生成手牌训练，位置和五名其余玩家随机化。论文称总训练约 10 小时（GTX 1080 Ti）；BC specialist 的 overall action imitation 为约 80–87%，raise 单类为 64.7%（§4.1–4.3）。高 fold 准确率并不代表关键下注决策被准确模仿。
- 4,000 局的 Havoc–BC-Pluribus 评测中，Havoc 平均每局收益 0.013，BC-Pluribus 为 -0.007；其余玩家从固定池随机补足，作者报告与所有其他 agent 的 t-test \(p<0.01\)（表 5、§4.4.1）。BC-Pluribus 是对公开 Pluribus 对局的再克隆而非原始 Pluribus，故不能将该结果说成击败原系统。
- leave-one-out 中每次用七名专家训练 Havoc、与未见的第八名和四个随机玩家打 4,000 局；Havoc 在 8 名中显著胜过 7 名，却未胜 player 2（表 6）。这直接表明对未见对手的适应不是全面成功，而是受对手池互动结构影响。
- ChatGPT 基线用特定 prompt 与相同信息，3,000 局中 Havoc 0.012、ChatGPT 0.005，作者报告 Havoc 优势 \(p<0.001\)（表 7）。这不是对 LLM poker 的系统比较：模型版本、提示、数值动作映射、工具/思维链和对手建模均未广泛消融。
- 分析显示 master 在不同活跃人数/胜率下偏好不同专家，长局中仍多次切换（表 8、10）；但 player 4 从未选择，且作者承认当前模型 identity-blind，未来才会加入对手 personality embedding（§4.5、§5）。专家多样性有时被实际选择策略压缩，不能据此假定每个 specialist 都有持续价值。

## 适用边界与复现

- 适用于可获得多位可用专家的离线轨迹、动作可离散化、环境可反复仿真、且需要在有限风格库间做情境选择的低风险部分可观测对抗任务；可把它视为 hierarchical policy-selection baseline。
- 不应作为多人 poker Nash/near-Nash 解、反剥削保证、赌博建议或金融竞价策略。多人一般和/部分信息环境中，胜过一个固定随机对手池不能排除被针对、共谋或分布外策略剥削。
- 复现应固定扑克 engine、盲注/筹码与摊牌规则、行动区间、完整人类数据预处理和 split、每个 specialist 的 BC 训练/冻结细节、1,000-rollout 胜率估计与 seed、master DQRN/replay/epsilon 参数、随机配桌方案、局数、positions 和 AWG 计算。
- 应报告 per-seed/per-opponent confidence intervals、强度匹配的原始 Pluribus/其他 CFR 或 self-play baseline、不同专家数/质量、移除胜率 oracle、动作粒度、对手身份条件化、在线对手分布变化与 exploitability/最佳响应评估。对任何现实多 agent 迁移需另做安全、延迟和策略滥用测试。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的不完全信息博弈、hierarchical RL 与 imitation-learning 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LRNX6318.pdf) 核验 Havoc 两层选择、8 名人类 BC 数据、胜率模拟特征、训练/评测局数、表 5–7、专家选择分析及 identity-blind 限制；没有把仿真桌局收益写成多人均衡、真实 Pluribus 对胜或通用 LLM 对抗能力。
