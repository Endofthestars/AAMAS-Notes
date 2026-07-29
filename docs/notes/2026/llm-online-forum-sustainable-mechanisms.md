---
title: "From Competition to Collaboration: Designing Sustainable Mechanisms Between LLMs and Online Forums"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "generative_agents", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/STKG8016"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/STKG8016.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "platform_mechanism_design", "utility_proxy_assumptions", "offline_simulation", "privacy_and_moderation_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# From Competition to Collaboration: Designing Sustainable Mechanisms Between LLMs and Online Forums

## 一句话总结

本文将 GenAI provider 与 Q&A forum 建为无货币、非对称信息的重复两阶段博弈：LLM 提交有限候选问题，forum 按私有规则发表一部分；发表的问题既可带来 views，也可作为 LLM 高不确定性监督信号。基于五个 Stack Exchange communities 与开源 LLM 的离线模拟，G-Utility strategy 的 estimated utility recovery rates 约 0.463–0.664；这不是上线合作、社区健康、知识质量、训练许可或用户福利的实证结果。

## 方法与证据

- 每轮 GenAI 从 pool \(Q_t\) 提交 \(A_t\)（\(|A_t|\le M\)），forum 用选择规则 \(R\) 发出 \(S_t=R(A_t)\)（\(|S_t|\le K\)）；双方各自私有的 additive utilities 在发表集合上累计（§2）。这把 forum 和 provider 简化为单一策略方，未建模专家回答质量、moderator 工作、用户反馈、声誉、版权、数据许可、垃圾内容、对抗操纵或多平台竞争。
- full-information cooperative benchmark 用 Nash product 选集合，求解 NP-hard；EURR 用若干启发式中各方可达的最大估计 utility \(\tilde U_G,\tilde U_F\) 归一化实际 utility（Eq. 1，§2.1）。因此 EURR 不是对真实最优/福利的比例，且分母本身是 heuristic estimate，不能解释为“实现了多少真正可持续收益”。
- 396,408 个问题来自五个 communities，按 2024-07-23 至 2025-07-23 的 weekly rounds 模拟。forum utility proxy 是 normalized view count，capacity \(K=50\)；GenAI proxy 是 Pythia 6.9B/LLaMA 3.1 8B/8B-Instruct 在 title+question 前 64 tokens 的 perplexity，\(M=100\)（§3）。高 perplexity 可能是噪声/低质问题，作者假定活跃 moderation 使其相对罕见；views 也不等同于价值、答案质量、成员留存或公平。
- G-Utility 最大化 \(U_G(q)\pi_b(q)\)，其中 \(\pi_b\) 从 accept/reject feedback 估计；forum 以离线 learned classifier 加阈值选择 top-K（§3）。策略及 classifier 的校准、反馈偏差/延迟、cold start、隐私泄露、分布漂移和 strategic manipulation 未由摘要实测。
- Figure 1 的 perplexity 与 normalized views 关联弱负（示例 Spearman −0.11）；Table 1 中 G-Utility 的 EURR_F 为 0.664/0.555/0.600，EURR_G 为 0.521/0.463/0.500（Pythia/LLaMA/LLaMA-Instruct），Random 的 EURR_G 约 0.11。它支持该离线 proxy game 中相对基线的表现，不是对 ChatGPT/Stack Overflow 因果影响或实际双方同意机制的结论。

## 适用边界与复现

- 适合研究平台与生成式模型间的非货币 selection mechanism；不可据此自动转发用户问题、收集论坛数据、优化 engagement 或训练模型。任何真实合作须处理同意、robots/API 条款、版权/许可、隐私/PII、内容质量、作者署名、moderation 负担、恶意操纵及收益分配。
- 复现需固定五个 communities/questions/timestamps、过滤/normalization、models/tokenizers/perplexity、64-token截断、\(M,K\)、classifier/features/threshold、\(\pi_b\) estimator、heuristics/\(\tilde U\)、随机性与策略更新。分别审计 candidate pool 是否与模型训练数据重叠、views 的时间泄漏和 forum selection classifier 的公平/校准。
- 应进行预注册 sandbox 或经 forum 同意的逐步 field trial，测量发表/回答/质量/留存、expert/moderator workload、用户体验、错误/有害问题、隐私与长期 feedback loop。测试新社区、冷启动、不同容量、恶意/低质问题、反操纵和多方机制；让人类治理而非 perplexity/views 独自决定发布。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 strategic interaction、LLM agent 与 platform mechanism design 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/STKG8016.pdf) 核验两阶段模型、EURR、Stack Exchange/LLM 设定、Figure 1 与 Table 1；没有把代理指标的离线模拟写成真实合作成功、许可或可持续性证明。
