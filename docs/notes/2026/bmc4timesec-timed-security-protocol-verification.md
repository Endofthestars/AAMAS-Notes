---
title: "BMC4TimeSec: Verification Of Timed Security Protocols"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["safety_verification", "argumentation_reasoning", "agent_engineering", "norms_trust_governance", "applications"]
dblp_key: ""
doi: "10.65109/URZB3421"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/URZB3421.pdf"
code_url: "https://github.com/agazbrzezny/BMC4TimeSec"
demo_url: "https://youtu.be/aNybKz6HwdA"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-06d"
spark_draft_verdict: "bounded_counterexample_tool_with_high_false_assurance_and_governance_risk"
spark_qa_verdict: "needs_revision_preserve_bounded_witness_scenario_library_and_unreported_quantitative_evidence_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["bounded_counterexample_search_not_unbounded_security_proof", "dolev_yao_and_term_algebra_assumptions", "session_k_and_trace_bound_dependence", "json_interpretation_and_parser_semantics", "included_attack_scenarios_not_per_protocol_verdicts", "no_quantitative_results_or_known_vulnerability_detection_evaluation", "no_runtime_memory_scaling_timeout_or_variance", "first_comprehensive_to_best_knowledge_author_claim", "anyone_can_verify_without_user_study", "real_crypto_implementation_side_channel_and_time_sync_gap", "web_flask_input_resource_tenant_auth_and_storage_controls_unreported", "solver_code_version_provenance_and_reproduction_package_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_bounded_security_false_assurance_dolev_yao_protocol_library_evaluation_web_input_resource_tenant_storage_and_real_implementation_boundary_check"
escalation_verdict: "pass_after_bounded_counterexample_and_protocol_library_boundary_reconciliation"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted bounded-security and false-assurance check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# BMC4TimeSec: Verification Of Timed Security Protocols

## 一句话总结

BMC4TimeSec 把 Alice–Bob protocol、JSON attack/fair interpretation 和 session bound \(k\) 转为 TIS/TIIS timed multi-agent model，再用 SMT-based bounded model checking 搜索知识可达性的 SAT counterexample；三页稿列出较广的 protocol/scenario library，但没有任何 quantitative 或逐协议 verdict 结果，因此“未找到 witness”不能被解释为真实协议的无界安全证明。

## 资源

PDF annotation 提供 [代码](https://github.com/agazbrzezny/BMC4TimeSec) 和 [演示视频](https://youtu.be/aNybKz6HwdA)。正文只说资源公开，没有给 commit、release、container 或与论文实验对应的版本。

## TIS/TIIS timed protocol model

BMC4TimeSec 使用 Timed Interpreted Systems（TIS）与 Timed Interleaved Interpreted Systems（TIIS）：

- environment execution automata 生成 protocol sessions/runs；
- 控制 step order、multiple-session interleaving、minimum transfer/execution delays、ticket/timestamp clocks 与 lifetimes；
- participant 和 intruder 的 knowledge automata \(K(a,t)\) 表示 agent 何时知道 term/message；
- intruder gating 只在满足 knowledge requirements 时允许构造/发送 action，对应 Dolev–Yao symbolic adversary assumption。

这能表达 time window、replay、session interleaving 与 artifact lifetime，但不自动覆盖 concrete cryptography、randomness、message serialization、implementation bug、side channel 或所有 compromise model。

## 从 specification 到 counterexample

输入为：

1. Alice–Bob notation 的 protocol description；
2. JSON interpretations/scenarios，支持 step override、spoofing、sender/recipient replacement、deadline substitution 与 intruder message injection；
3. session number \(k\)。

Pipeline：

1. 生成 multiple sessions 和 fair/attack interpretations；
2. 建立含 delays/lifetimes 的 TIS/TIIS model；
3. 生成 reachability formula，例如 \(EF(\psi)\)，其中 \(\psi\) 结合 session termination 与 \(K(I,secret)\) 等 knowledge conditions；
4. 输出 SMT-LIB2 并用 Z3 求解；
5. SAT 时提取 witness/counterexample；
6. GUI 逐 step 显示 execution 与 knowledge changes。

软件栈包括 Python Alice–Bob parser、Python TIIS generator、C++ SMT-BMC formula generator、Z3 launcher，以及 Python/Flask GUI。

## Attack scenarios 与 protocol library

论文列出的 attack categories 包括：

- step-level impersonation / man-in-the-middle；
- message 或 component replay between sessions；
- mix-up / mismatch；
- non-injective authentication violation，例如 freshness element 跨 session 重用；
- long-term key compromise scenario。

Specification library 覆盖 time-based NSPK/Lowe、WMF/Lowe、Denning–Sacco、Kao–Chow、Carlsen SKIP、NSSK、Yahalom 及 Lowe/Paulson/BAN variants、Woo–Lam Pi 1/2/3、Andrew/Lowe、MobInfoSec、SNEP 等。

“每个 protocol 含 fair variant 与 attack scenarios”表示项目提供输入规格/解释，不等于这篇论文报告了每个 protocol 的安全 verdict、发现新攻击、复现已知攻击或证明无漏洞。

## 完全缺失的 quantitative evaluation

三页正文没有 experiments/results table，也没有报告：

- protocol-by-protocol SAT/UNSAT/witness outcome；
- known-vulnerability detection 或 witness replay validation；
- false positive、false negative、soundness/completeness empirical check；
- runtime、memory、formula/state size 或 scaling；
- tested \(k\) values、trace/time bounds、timeout 或 failure rate；
- baseline/VerSecTis empirical comparison；
- repeats、variance、hardware、solver options；
- code version、test suite、benchmark command 和 reproduction package。

“more attacks”“verify more than previous works”是 scenario/capability 范围的作者描述，不是量化 superiority 结果。“anyone can verify their protocol”是 usability slogan，没有 user study、error rate 或 learnability evidence。

## Bounded verification 的核心边界

SAT witness 说明：在当前 Alice–Bob/JSON interpretation、TIS/TIIS/Dolev–Yao model、session \(k\)、trace/time bounds 与 SMT encoding 下，存在达到 violation/knowledge condition 的 counterexample。

UNSAT 或没有 witness 只说明当前 bound/interpretation 内未找到反例。它不证明：

- 更大 \(k\) 或更长 trace/time horizon 也无攻击；
- attack scenario library 完备；
- parser、generator 和 SMT encoding 正确；
- deployed implementation 与 formal model 一致；
- real cryptography、key generation、time synchronization、network stack、side channel 和 operational compromise 安全。

因而工具更适合生成可检查的 bounded counterexample，而不是直接签发 protocol security certificate。

## False assurance 与服务治理

正式使用还需记录 protocol/spec version、JSON interpretation、bounds、solver/config、witness trace 和 model-to-implementation mapping，并做 known-attack regression、independent model/encoding review 与 counterexample replay。

Flask/Web pipeline 接收用户 protocol/JSON 并运行 solver，正文没有报告：

- parser/input validation、upload size 与 malicious specification handling；
- CPU/memory/time quota、solver isolation、job cancellation 与 denial-of-service control；
- tenant isolation、authentication/authorization 与 secret management；
- protocol/result/witness access、encryption、retention、deletion 与 audit；
- code/dependency/solver pinning、artifact provenance 与 rollback。

这些是未报告控制，不是已发生攻击或数据泄露的证据。高风险来自 security-verification 输出被误读为充分安全保证。

## Novelty 与页码核验

“first comprehensive and extended implementation”由作者以 “to the best of our knowledge” 限定，笔记不把它写成外部穷尽验证后的绝对首创。

- p. 4173：题名、摘要、引言、TIS/TIIS、execution/knowledge automata 与 pipeline；
- p. 4174：architecture、software stack、JSON example、system innovations、attack categories 与 protocol library；
- p. 4175：致谢与参考文献，没有新增实验。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/URZB3421.pdf) 核验；`reviewed` 不表示 unbounded protocol security、scenario completeness、implementation security 或 Web service governance 已得到验证。
