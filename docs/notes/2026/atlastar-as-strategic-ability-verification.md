---
title: "ATL*AS: An Automata-Theoretic Approach and Tool for the Verification of Strategic Abilities in Multi-Agent Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "argumentation_reasoning", "agent_engineering"]
dblp_key: ""
doi: "10.65109/LHUR4872"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LHUR4872.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["perfect_recall_perfect_information_scope", "synthetic_and_modelled_cybersecurity_evaluation", "toolchain_and_automata_dependency", "partial_observability_heuristic_encoding"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# ATL*AS: An Automata-Theoretic Approach and Tool for the Verification of Strategic Abilities in Multi-Agent Systems

## 一句话总结

ATL*AS 为 CGS 上、完美回忆策略的 ATL* 与有限轨迹 ATL*f 提供 symbolic 模型检查：finite trace 用 DFA/BDD fixpoint，infinite trace 归约为 BDD 编码 parity game。它在合成基准和一个建模的攻防场景中显示可扩展性，但不证明真实网络安全或不完美信息系统的战略安全。

## 方法与证据

- 工具输入是扩展了 final states 的 ISPL 子集，含 explicit/symbolic ATL*f 后端及 symbolic parity-game ATL* 后端；有限 trace 将终止路径纳入语义，无限 trace 用 DPA 与 parity game（§2--5）。
- 评测使用多智能体 counter synthetic benchmark、fair scheduler 和 CyMARL 启发的五服务器、两 defender/一 attacker 攻防 CGS。公平调度表中 process 6 时 ATL*AS 为 21.40s、MCMAS-SL[1G] 为 60851.20s；两工具逻辑、automata 和 solver 实现不同，非纯粹同算法对照（§6.3、表 2）。
- 网络安全模型的 defender 可用动作由 suspicion buckets/heuristics 限制；有限 horizon 的验证在逾百万状态下报告一小时内完成，并计算四种 heuristic 下保证防御的最小预算（aggressive 12，其他列出的 conservative/diversity 14）（§6.4、表 3）。

## 局限与复现

- 语义为有限 CGS、perfect recall 策略及模型给定的完美信息；真实部分可观测性仅以动态动作限制启发式编码，非 ATL* 不完美信息语义。结论不能直接覆盖隐藏状态、消息延迟、攻击者操纵观测或真实 SOC 运行。
- 2EXPTIME 逻辑复杂度未消失；性能取决于 BDD variable ordering、DFA/DPA translation、外部 automata tooling、内存、模型/公式结构和 timeout。所报告的优势须在原始 inputs/版本/硬件上复核。
- cybersecurity case 是受控 CGS 而非 CyMARL 或实网 replay；资产、攻击路径、flags、budget、risk thresholds 与 defender heuristics 均是建模选择，验证的是该模型中战略能力而非防御有效性/合规认证。
- 复现应取得 supplementary/arXiv 代码，锁定 compiler、automata/parity solver、ISPL models、公式、BDD 设置、CPU/RAM、timeout；报告成功/失败、峰值内存和所有规模点，并与 MCMAS-SL[1G] 使用等价语义与相同模型复核。

## 与 AAMAS 的关系与核验说明

该文面向多智能体战略时序性质的形式验证。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LHUR4872.pdf) 核对语义、工具后端、表 2 与网络安全建模；未将模型检查结果外推为真实网络系统安全保证。
