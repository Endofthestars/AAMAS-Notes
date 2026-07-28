---
title: "Learning from Delay Distributions: A New Representation for Delay-Aware Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "agent_engineering", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XDQU6782.pdf"
preprint_url: ""
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["independent_delay_assumption", "finite_action_convergence_scope", "simulated_delay_wrapper", "baseline_prior_information"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Learning from Delay Distributions: A New Representation for Delay-Aware Reinforcement Learning

## 一句话总结

D2 AC 以 action/observation delay 的概率分布加权 distributional return，并嵌入 SAC critic，以避免显式拼接长历史；在模拟的 MuJoCo 随机延迟中表现较强，但其理论和实现依赖离散独立延迟、已知/估计 delay distribution 与特定反馈规则，不等同于真实异步控制保证。

## 方法与证据

- 设定区分 environment 真正的 state/action/reward 与 agent 收到的 delayed feedback。reward 和 observation 假定共享同一 observation delay；同一时刻收到多个反馈时取最新，未收到时复用上次反馈（§3.2）。
- stochastic delay representation 将未来 return 按 action-delay $p_i^a$ 和 observation-delay $p_j^o$ 的乘积加权；有效 delay range 以分布概率阈值截断。Proposition 1 只在两类离散 delays 统计独立时，将它们化为总 delay 的 joint distribution（§3.2–3.3）。
- Theorem 1 声明该 representation with distributional returns 可收敛到最大化 expected Q 的 policy，前提包括 $|A|<\infty$、bounded reward 与 distributional soft Bellman operator contraction。它不是对连续动作 SAC、未知或相关 delay、非平稳网络的直接收敛证明；policy objective仍以 expected value 而非完整 Z distribution 为准（§3.3）。
- D2 AC 用 distributional SAC 的 Gaussian return 假设，replay 中按 delay distribution 采样未来轨迹并以 KL divergence 训练。论文承认定理使用 Wasserstein metric 而实现用 KL 是实践选择；因此实验实现不等于定理算子逐项实现（§4）。
- MuJoCo/Gymnasium wrapper 实验包含 gamma、double Gaussian、uniform 随机 delay，1M steps、8 seeds；比较 VDPO、AD-SAC、State Aug-MLP、BPQL、DCAC 和 DFBT。constant-delay baselines获知随机分布均值，State Aug-MLP获知最大 delay，DFBT/DCAC获知每步 exact delay；DFBT 单独在旧的 MuJoCo v2 比较，其余在 v4（§5.1）。
- 表格显示 D2 AC 在多项随机-delay任务中较高或接近最好，但并非全项独占；constant delay 5 时作者明确该机制退化、不能稳定胜过所有 constant-delay专用方法。action+observation gamma delay 仅在附录实验，ablation 说明 SDR 与 distributional return 均有贡献（§5.2–5.3）。

## 局限与复现

- 方法需要 delay distribution 及其有效范围；未说明如何在分布漂移、相关 action/observation delay、packet loss、乱序重组、计算负载反馈或恶意网络条件下持续可靠估计。
- 应将“observation/action equivalence”限定在 Proposition 1 的独立、离散、总延迟表示下；它不保证两种延迟对安全、控制稳定性、执行器饱和或信息可用性具有相同物理后果。
- 收敛 theorem 的有限 action 条件与常用连续动作 SAC 实验之间存在适用鸿沟，且没有真实 UAV/网络控制闭环部署。MuJoCo delay wrapper 的 reward 不能验证实时系统的时钟、通信与安全行为。
- 基线有不同先验信息和 v2/v4 版本分离，结果应按组阅读，不能作统一绝对排名；8-seed SEM 与平滑曲线也不足以说明所有 delay distribution 的统计优势。
- 复现应公开 delay sampling/threshold、反馈选择与复用规则、Gaussian critic/KL 设置、每 seed 原始回报及分布估计；分别测试未知、相关、漂移 delay，并报告估计 distribution 错配时的性能和控制失败率。

## 与 AAMAS 的关系与核验说明

该文面向多 agent/控制系统中的随机反馈延迟，以 distributional RL 表示替代大历史状态增广。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XDQU6782.pdf) 核对 representation、Proposition 1、Theorem 1、D2 AC 实现与 8-seed 实验协议；不将模拟随机延迟中的奖励提升外推为真实异步系统的收敛或安全保证。
