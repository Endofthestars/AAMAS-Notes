---
title: "Generating Fair Consensus Statements with Social Choice on Token-Level MDPs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "human_agent_interaction", "norms_trust_governance", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/NZPR5925"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NZPR5925.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["fairness_proxy_from_llm_likelihood", "truncated_candidate_space", "lottery_vs_single_statement_gap", "sensitive_topic_data", "small_human_validation", "nonbinding_decision_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Generating Fair Consensus Statements with Social Choice on Token-Level MDPs

## 一句话总结

论文把共识文本生成视为 token-level multi-objective MDP：每位参与者由一个条件语言模型 policy 表示，其 token likelihood 诱导奖励/效用。对**随机的完整陈述 lottery**，在有限候选树上最大化 Nash welfare 可得到 ex-ante core outcome；对**单个陈述**，以最小 agent 的累积 log utility 做 egalitarian search。后者在三个基准情景的模型 perplexity 上更好，但其“公平”本质是由 prompt-conditioned LLM likelihood 代理，单陈述没有 core guarantee，输出不应被当作绑定的集体决定。

## 方法与证据

- state 是已生成 text prefix，action 是下一个 token/eos，transition 为 append token。每个 agent policy \(\pi_i(a|s)\) 可由其意见条件化的 LLM 或个性化模型给出；实际只保留 reference model 提议的 \(B\) 个 token，并设最大长度 \(L_{max}\)，所以可行完整 paths \(C\) 有限（§3）。
- 两种效用不能混用：单 statement 用 additive \(U_i^{log}(X)=\sum_t\beta\log\pi_i(a_t|s_{t-1})\)，以 \(\max_X\min_i U_i^{log}(X)\) 作 egalitarian welfare；lottery 用非负的 multiplicative probability utility \(U_i^{prob}(X)=\prod_t\pi_i(a_t|s_{t-1})\) 及其期望（§3.1）。
- stochastic policy 先对所有 complete paths 求 \(p^*\in\arg\max_{p\in\Delta(C)}\sum_i\log(U_i^{prob}(p))\)，再按子树条件概率转为逐 token policy。借助 Nash-welfare/core 的既有结果，所诱导 lottery 位于相对于该有限 \(C\) 的 ex-ante core（§4、Algorithm 1、Corollary 1）。这不意味着某一条采样出的句子本身公平，也不覆盖被 pruning 掉的陈述。
- core algorithm 需要形成所有 agent--leaf utilities，成本随 leaves \(m\) 增长且 tree 本身为 \(B^{L_{max}}\) 级。论文用 chunking/有限候选是管理搜索空间的启发式；未给不看完整 tree 的 unchunked core 近似（§4、§7）。
- deterministic case 用 finite lookahead（depth 4, branching 2）或 beam search（width 4）近似 EW；论文承认没有 single-statement 的 theoretical guarantee（§5、§7）。
- preference-proxy 检验采用 Fish 等人的 abortion dataset：42 位人类写意见、各自对 5 个候选 statement 做 1--5 Likert rating。用条件 LLM likelihood 与 rating 的 Spearman correlation；随提供的意见文本增多，相关性升高，但全文也仍“somewhat low”（§6.1）。
- credit-assignment 示例用 Llama 3.1 8B Instruct，在 vegetarian/cold climate/morning/gun-control 等控制 prompt 下替换 token；变化 token 的 Z-score 较大。这是少数构造例子，说明 localized likelihood shift，并非对真实政治偏好建模的全面验证（§6.2、Table 1）。
- consensus 实验从 Habermas Machine dataset 聚类选 3 个 scenario，每个 4 agents；agent/base policies 都以 Llama 3.1 8B Instruct prompting 实例化，报告每方法/情景 3 seeds。Beam Search 平均 EPPL 2.87、finite lookahead 4.18，优于 Best-of-N 6.35、prompted HM 9.67；原 HM 15.69 还使用不同的 Chinchilla-70B，故非同模型的纯算法比较（§6.3、Figure 4）。

## 安全边界与复现

- LLM likelihood 是“该 prompt 下模型会如何续写”的 proxy，而非参与者的真实效用、同意、理解、少数群体权利或程序正义。prompt、模型、语言、长度归一化和 tokenization 都会改变 utility；低 EPPL 不能认证政治/伦理公平。
- ex-ante core 是针对 lottery 和有限 candidate set 的 coalition stability 定义，不保证各人接受一次随机抽出的 statement，更不保证确定性输出、事实正确性、非歧视、法律合规或结果合法性。使用时必须区分随机方案与单个文本。
- 输入意见可能涉及敏感个人/政治信息。收集、个性化提示、日志和输出应有知情同意、最小化保留、访问控制、删除机制、代表性与语种审计；不得将系统输出用于自动作出政策、雇佣、福利或其他权利决定。
- 论文自身建议将输出当作 collective sense-making 的讨论材料、而非 binding decision。现实审议还需要独立事实核验、反驳/修订回合、参与者复核、反操纵保护、少数意见呈现、人工主持与申诉渠道。
- 复现应固定 dataset/split、issue/opinion prompts、agent/reference LLM checkpoint、top-\(B\)/\(L_{max}\)/chunking、reward scale \(\beta\)、Nash solver/tolerance、beam/lookahead 参数、EPPL prompt/length normalization、baseline/model differences、seeds；同时报告 candidate coverage、每 agent utility、coalition checks、生成成本、human acceptability 与事实/伤害审计。

## 与 AAMAS 的关系与核验说明

这是 generative social choice 与人机集体决策工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/NZPR5925.pdf) 核对 token MDP、两类效用、finite-set ex-ante core 推导、单陈述 search、42 人相关性检验、Table 1/Figure 4 与作者的非绑定使用警告；没有将 LLM likelihood proxy、有限 tree lottery 或 EPPL 优势误写为真实人类共识、确定性公平或可自动执行的治理决策。
