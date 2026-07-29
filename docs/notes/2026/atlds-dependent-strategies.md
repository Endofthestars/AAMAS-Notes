---
title: "Alternating-Time Temporal Logic with Dependent Strategies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "safety_verification", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/MYRV8798"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MYRV8798.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["sequential_action_order_assumption", "privileged_information_semantics", "positional_strategy_scope", "efficient_encoding_pspace", "finite_agent_set", "logic_property_not_system_implementation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Alternating-Time Temporal Logic with Dependent Strategies

## 一句话总结

ATLDS 扩展 ATL 的 coalition modality，为每个策略能力公式附上 agent permutation：在每一步按该顺序行动，后行动者可依赖此前行动者的动作，因此能表达 Stackelberg/特权信息下的能力。论文给出 ordered effectivity 的表示定理、ATLDS 的 sound/weakly complete 公理化，并证明与 Strategy Logic 的 \(SL-[SG]\) fragment 表达等价。该逻辑的语义把“顺序”视作每状态动作可观察性/依赖关系；它不是自动从现实通信或信息结构推断的安全/合规证明，且 efficient encoding 下模型检查为 PSPACE-complete。

## 方法与证据

- 在 CGM 中，普通 ATL 假设 concurrent action；ATLDS 的 \(\langle\langle C\rangle\rangle_P\) 用全体 agent 的 permutation \(P\) 指定同一步谁先行动。agent 的 strategy 可读取先于自身的 actions，因而 coalition 内/外均可有非对称依赖（§1、§3–4）。
- 例如 \(P=(\alpha,\beta,\gamma)\) 让 \(\gamma\) 知道 \(\alpha,\beta\) 的当步动作；作者可把它理解为 interleaved processes 或 privileged knowledge（§1）。实际系统若动作同时提交、观测延迟、消息可伪造或有部分可见性，则该排列语义不应直接使用。
- 仅需 positional strategies，但其 action 输出依赖 state 与先行动者动作；同一 coalition 对不同 permutations 的能力具单调性：让 coalition agent 更晚行动不会降低可强制性质（§3–4）。这不是任意历史依赖/记忆策略的通用逻辑扩展。
- 论文以 ordered/\(\pi\)-effectivity functions 表示 coalition 在各种顺序下可强制的 outcome sets，给 representation theorem，把满足公理的集合重建为 strategic game（§5）。随后在 SOEM/CGM 上给 ATLDS sound 且 weakly complete 公理化（Theorems 25/Corollary 28，§6）。
- ATLDS 与 \(SL-[SG]\) fragment 表达等价（§1、§4）；这带来比 ATL 更强的依赖表达，但不可把 full Strategy Logic 的不判定/高复杂度结果简单套到此 fragment。
- 对 efficient/implicit CGM encoding，Proposition 29 给 ATLDS model checking PSPACE-complete；固定 agent 数的情形有更低的多项式层级界，unbounded agent 数随 alternation number 上升（§7）。显式表/agent 数/动作空间的编码方式会实质改变可运行性。

## 适用边界与复现

- 适用于明确规定先后手或动作可见依赖的协议、leader–follower 机制、交替式决策与安全性质模型检查；使用前应先把实际信息流映射为合法 permutation。
- 不应把公式满足解释为现实 agent 一定能观察、理解并及时响应前序行动。需单独验证通信认证、时序、隐私/可见性、失败模式和 implementation refinement。
- 复现需固定 CGM/隐式 encoding、agent/actions、permutation、state labeling、公式 fragment、strategy semantics、effectivity construction与 model-checker；报告 model size、action profile size、agent count、formula alternation和实际耗时/内存。
- 后续应研究不完全/带噪观测、异步或动态 action orders、记忆/概率策略、与 runtime monitors/协议实现的 refinement，以及可用的 symbolic/parameterized checking。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多智能体逻辑、策略依赖与验证工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MYRV8798.pdf) 核验 permutation semantics、representation/axiomatization、\(SL-[SG]\) 等价和 §7 模型检查复杂度；没有将形式逻辑的 sequential-observability 假设误说成部署系统自动具备的知识、通信或安全保证。
