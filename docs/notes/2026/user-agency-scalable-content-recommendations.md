---
title: "Enabling User Agency in Scalable Content Recommendations with Large Language Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "human_agent_interaction", "applications"]
dblp_key: ""
doi: "10.65109/CBUQ6936"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CBUQ6936.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["offline_recommendation_evaluation", "synthetic_interest_data", "privacy_claim_scope", "user_agency_not_user_study", "profile_edit_side_effects", "cross_provider_interoperability_unvalidated"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Enabling User Agency in Scalable Content Recommendations with Large Language Models

## 一句话总结

本文提出 personal agent 在本地把交互历史转换为带权、可读写的自然语言兴趣 profile；provider 在共享 embedding space 中以 ANN 检索内容，避免直接取得 raw profile/history。MIND 与 Goodreads 的离线 ranking 实验显示该方法优于所选 baselines，并在 100 名 news users 的 profile 编辑模拟中，插入 topic 后相关推荐占比约 87–88%。这证明在所设离线协议下的排序与编辑响应，不证明真实用户获得更多自主权、隐私保护、跨 provider 可携带性或长期福祉。

## 方法与证据

- 架构分为 centrally maintained shared content–interest embedding space、local personal agent、provider retrieval API（§2）。LLM 从 content sample 生成 synthetic content–interest pairs，再以 contrastive objective fine-tune embedding；个人 agent 在 history 上优化自然语言兴趣及其 weights，provider 用 weighted profile embedding 做 ANN（§2.1–2.2）。中央 embedding model、API 与 content embedding 仍是信任/治理边界，“本地 profile”本身不消除服务端日志、query linkage、embedding inversion 或模型供应链风险。
- interest weights 由历史 content embedding 与 binary engagement label 的 least-squares 解并归一化得到（§2.2）。engagement 是偏好代理，可能受曝光、位置、操纵、短期吸引和缺失反馈影响；作者没有给出偏好因果识别、negative preference、操纵/投毒或群体公平保证。
- 实验使用 Microsoft MIND 与 Goodreads；不同于 centralized baseline 的大规模 pooled training，personal agent 在每 user 的 local history/profile 上学习（§3）。离线 split、candidate construction 和 implicit labels不能测量新 provider cold start、用户迁移、真实设备成本或长期 feedback loop。
- Table 3 报告 MIND 上 best AUROC 72.13%（强 baseline GLIMPSE 71.66%），Goodreads 69.56%（GLIMPSE 68.91%），且 nDCG/MRR 等指标也提升（§3.1）。这些排名数值是特定 datasets、baselines 和 protocol 的效果，未包含线上 A/B、满意度、diversity、harmful content、provider competition或统计不确定性结论。
- profile optimisation 以 profile pool 的 sampling/refinement 迭代，依 held-out validation reward（§2.2, §3）。论文称 1–8 iterations 即超越 baselines；这可能带来 per-user LLM compute、latency、energy、validation leakage 与 profile drift 成本，主文没有在真实用户端评估。
- Editability test 对 100 个 news users 插入或删除 Politics/Music/Local News，并量化相关 topic 推荐占比；插入约 87–88%，删除后仍约 15–18%（Table 4, §3.3）。作者明确删除被当作 profile sanitization、并非负偏好；因此编辑不是强排除/安全过滤语义，敏感或不想看内容仍需专门 blocking/consent policy。
- 作者以“profile ownership/portability”作为设计目标并称新 provider 只需嵌入 catalog（§1–2）。实际跨 provider portability 还需共同 schema/version、认证、权限、撤回、数据格式、商业/法律协议、malicious catalog 防护及用户理解测试；论文没有 end-to-end multi-provider deployment 证据。

## 适用边界与复现

- 适用于研究可解释 profile 与 scalable retrieval 的分离设计。实践时应让用户查看 profile、单项 weights、数据来源和编辑后果，并提供明确的删除、拒绝、export/import与撤回接口。
- 不能以自然语言 profile 或“local agent”直接宣称 privacy/agency 合规。需要 threat model、local/remote telemetry 审计、embedding/query 泄露测试、access control、加密与 retention policy、内容安全/公平性评估、未成年人/敏感兴趣保护以及独立可用性研究。
- 复现应固定 content-only synthetic-pair generation prompt/model、embedding fine-tuning、per-user history split、profile generation/refinement prompt、weight fit、ANN index和 ranking metrics；也应运行 edit insertion/deletion，记录不相关结果及删除残留。
- 后续应做真实用户及跨 provider study、online counterfactual evaluation、longitudinal preference/feedback analysis、negative preference与hard safety constraints、profile poisoning/prompt injection测试、privacy attack与heterogeneous catalog robustness。

## 与 AAMAS 的关系与核验说明

这是 AAMAS user-agent recommendation 研究。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CBUQ6936.pdf) 核验了三组件架构、synthetic pair embedding training、least-squares weights、MIND/Goodreads offline 结果和 Table 4 编辑试验；没有把离线排序/编辑响应写成经验证的用户自主、隐私、跨 provider 互操作或长期推荐福祉。
