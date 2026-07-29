---
title: "Towards Probabilistic Strategic Timed CTL"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "argumentation_reasoning", "marl_coordination"]
dblp_key: ""
doi: "10.65109/OEXM4130"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OEXM4130.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02t"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "initial_model_checking_prototype", "irP_strategy_scope", "small_benchmark_scalability", "complexity_unestablished"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Towards Probabilistic Strategic Timed CTL

## 一句话总结

PSTCTL 将 Strategic Timed CTL 扩展为可表达连续时间、异步 stochastic multi-agent systems 和 coalition 达到概率时限性质的分支时序逻辑；本文聚焦具有不完美信息、无记忆、概率选动作的 irP strategies，并把每个局部状态的动作概率编码为 PRISM 参数。Train–Gate–Controller 实验表明小模型可验证一个 irP 可满足而 irp 不可满足的性质，但 5 列车/较大时限已耗时数百秒或内存耗尽，表达能力与模型检查复杂度仍待正式建立。

## 方法与证据

- 模型是由概率 timed automata 组成的 PCAMAS：私有动作异步交错，共享动作同步，状态具有连续时间；策略按信息（I/i）、记忆（R/r）和动作选择（P/p）分类。irP 将本地状态映射为可用动作上的概率分布，irp 是其点分布特例（§1--2）。
- 语法在战略模态 \(\langle\langle A\rangle\rangle\) 下加入 PCTL 风格概率 path operator 与有界连续时间 until/release。语义要求联盟存在策略，使策略兼容执行所诱导的概率分布满足阈值关系（§2）。
- 为在 PRISM 中表示 irP，对 coalition agent 每个 local state 的每个可用动作设置概率参数；数字时钟引擎导出的中间模型在适当限制下可看作保留 probabilistic reachability 值的离散时间 MDP，再返回 PRISM 验证（§3）。
- TGC benchmark 验证 \(\langle\langle C\rangle\rangle P\ge0.8 F_{[0,T]}(passed1\wedge passed2)\)。两车约 0.1s，三车在 \(T=100\) 为 28.6s，四车为 493s，五车 \(T=30\) 为 849s、\(T=100\) memout（32 GB）；irP 可通过随机化选车而 irp 不可满足该例（§3、表 1）。

## 适用边界与复现

- 适用于提出/验证具时限、概率和战略能力的异步多智能体规格；它不直接给出控制器部署、安全证明或大规模 system synthesis。
- 本文只演示 irP、memoryless、imperfect-information 策略；与 irp、perfect recall、不同同步语义或不同 probabilistic model 的可判定性/复杂度不应混同。
- 参数化 PRISM 编码会快速爆炸，表 1 已显示规模限制。导出数字时钟 MDP 所需限制、PRISM 版本、参数处理、内存阈值和硬件会影响结果。
- 复现应公布 PCAMAS/TGC 模型、时钟离散化限制、策略参数域、PRISM 命令与版本、CPU/RAM、所有 \(n,T\) 表项；与 abstraction、partial-order reduction、近似方法比较，并将任何安全相关结论在原连续系统上再验证。

## 与 AAMAS 的关系与核验说明

该文属于多智能体形式化验证与时序逻辑。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/OEXM4130.pdf) 人工核对 PSTCTL/irP 定义、PRISM 参数编码、TGC 性质与表 1；没有把初步可行性实验表述为可扩展验证器或已证明的复杂度结果。
