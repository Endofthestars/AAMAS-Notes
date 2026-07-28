---
title: "LLM-augmented Empirical Game Theoretic Simulation for Social-Ecological Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "game_theory_mechanism", "applications"]
dblp_key: ""
doi: "10.65109/SEWU4006"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SEWU4006.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["llm_behavioral_validity_unproven", "expert_payoff_model_dependence", "prompt_and_model_sensitivity", "policy_simulation_not_causal_evidence", "distributional_equity_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# LLM-augmented Empirical Game Theoretic Simulation for Social-Ecological Systems

## 一句话总结

论文比较 procedural ABM、generative ABM、naive LLM-EGTA 和 expert-guided LLM-EGTA，模拟 Amu Darya 流域灌溉/渔业在集中与分散治理下的 100 年动态。LLM-only 的策略/博弈构造会产生退化或病态策略；由专家定义连续 payoff、以 Gambit 解 Nash equilibrium 并加入 Pigouvian tax 的 EGTA 是唯一维持混合农业—渔业经济的分散模型。该结论是特定生态 ABM、行为/税率与模型规范下的机制探索，不能作为真实农户偏好、税收因果效果或水资源政策部署的预测认证。

## 方法与证据

- 四种 pipeline 共用 procedural ecological ABM：农户按年选择灌溉 fields，河流出流影响下游灌溉与湖泊鱼类；模型包括 13 个鱼龄类、月度 river flow、crop yield 与收支，仿真 horizon 为 100 年。行为/制度不同，生态方程及完整 ODD+D 在补充材料（§2--5）。
- generative ABM 给 LLM farmer role、行为 profile 和环境 context 后直接询问动作。naive LLM-EGTA 让 LLM 从 ODD+D 抽取 Action Situations、选 canonical game、选策略，随后用 ecological ABM 更新状态；论文报告 DeepSeek-V3 (671B) 在重复运行中抽取出 farming 与 fishery games（§3.1、§5.1）。
- expert-guided LLM-EGTA 不把 LLM 产出的 high/low game 当成最终模型：专家可改为 \([0,10]\) 连续 fields/extraction action、随预算变化的 closed-form payoff，并用 Gambit 等算法解 equilibrium。相邻农户 farming game 的 payoff 包含外部性税 \(\tau\)，\(\tau>0\) 为 Pigouvian tax（§3.1.2、§5.1.4）。
- 比较含 centralized baseline、procedural ABM、generative ABM、naive LLM-EGTA、expert LLM-EGTA 的 \(\tau=0\) 和 \(\tau=0.25\)。exogenous parameters 与 Schlüter model 校准相同，每个 simulation 使用季初（7 月）校准的真实 water inflow（§6）；这不是用历史农户 actions/outcomes做外部预测验证。
- Figure 4--5：无税 expert model 中除 3 位 upstream household 外，多数在约第 10 年负债；naive LLM-EGTA 更差，因为 LLM 经常在 shrinking budget 下持续灌溉，且 low strategy 也不能选 0。\(\tau=0.25\) expert model 将策略约束在河/湖 carrying capacity 内，是唯一维持 mixed agriculture/fishing 的 decentralized model，且总体 wealth 最好。
- 鲁棒性实验换用 DeepSeek-R1、QwQ-32B、GPT-OSS-20B，并用 altruistic/balanced/rational system prompts。prompt/model 会显著改变年 100 wealth/activity，QwQ-32B 在 naive LLM-EGTA 的 balanced 与 rational 甚至给出相同策略；相反 expert payoff 内的 \(\tau=0.25\) 或 1 带来 min/max budget 约 4,000--4,620 且 100% mixed activity，\(\tau=0\) 则 minimum -246.01、mixed 6.3%（Table 1、§6）。

## 安全边界与复现

- LLM 生成的 "plausible" dialogue/strategy 不构成对真实 Amu Darya 农户、机构或生态因果机制的验证。本文并未报告人类行为拟合、历史 outcome backtest、holdout geography/time、调查校准、模型不确定性后验或实地政策试验；真实 inflow calibration 不能替代这些证据。
- 结果高度取决于由专家选择的 action-space granularity、payoff function、Nash solution concept、税率 \(\tau\)、fish/water dynamics 与 carry-capacity 参数。专家模型加税后更可持续，首先说明该**模型设定**中的激励内化效果；不能据此自动推导真实税率、征收可行性、合规、政治合法性或分配公平。
- naive LLM-EGTA 的 two-action/anti-coordination abstraction 甚至不能在 low 策略下选 0 fields，产生反复付成本的病态行为。LLM 输出必须接受 schema、range、budget feasibility、non-negativity、mass-balance、策略支配与 solver consistency 验证；LLM 不应独自抽取制度游戏或求 equilibrium。
- 资源政策会改变 upstream/downstream 的利益与贫困风险。部署前需让地方利益相关者参与 ODD+D/假设审计，提供可解释的税收收入使用和申诉机制，比较多种 equity/welfare/food-security 目标，并让独立生态/水文专家验证模型；禁止依赖单一 LLM simulation 直接分配水权、征税或限制生计。
- 复现须锁定 ODD+D、生态 ABM equations/parameters、inflow series、随机数、100-year horizon、所有 prompts/system profiles、模型 ID/version/temperature、canonical game library、专家 payoff/\(\tau\)、Gambit settings及 centralized baseline。应报告多次 stochastic run、敏感性、OOD气候/市场/人口情景、极端干旱和多种 solution concepts，而不只比较单一轨迹图。

## 与 AAMAS 的关系与核验说明

这是 generative agents、ABM 与 empirical game-theoretic analysis 的社会—生态系统仿真工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/SEWU4006.pdf) 核对四条 pipeline、Amu Darya case、100 年生态模拟、专家 payoff/\(\tau\)、Figure 4--5、Table 1 与 LLM sensitivity；没有把建模内的可持续模式或 prompt 行为诱导表述为现实人群预测或政策因果保证。
