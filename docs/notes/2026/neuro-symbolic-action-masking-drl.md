---
title: "Neuro-symbolic Action Masking for Deep Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/JWPH6906"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JWPH6906.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["learned_grounding_error", "constraint_or_precondition_misspecification", "early_training_violations", "hard_mask_feasibility_only", "benchmark_to_real_world_gap"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Neuro-symbolic Action Masking for Deep Reinforcement Learning

## 一句话总结

NSAM 用人工给定的命题约束与动作前置条件编译 PSDD，再由神经网络从原始 state 学习符合约束的符号模型，以 MAP model 生成 0/1 action mask 并与 PPO 联训。在 Sudoku、N-Queens、Graph Coloring 和 Visual Sudoku 的 16 个任务上，训练违规率和收敛回报优于其比较对象；但其“formal verification”只针对 learned symbolic model 上的前置条件，不能跨越感知错误、规则漏项/误写、未知约束或现实动力学而保证系统安全。

## 方法与证据

- 输入的领域知识仍须人工提供：atomic propositions \(P\)、每个 action 的 propositional precondition \(AP\)，以及 domain constraint \(\phi\)。作者先把 \(\phi\) 编译为 SDD/PSDD；任一违反 \(\phi\) 的 truth assignment 被赋零概率。PSDD 的 gating network \(g(s)\) 将高维状态映射为其参数，表示条件于 state 的有效符号模型分布（§2--3.2）。
- 最小监督不是安全 oracle：从 rollout transition \((s,a,s',y)\) 取 `y=1` 当 \(s\) 与 \(s'\) 均不违反 \(\phi\)，否则为 0，并以 action 可探索概率的 cross-entropy 训练 gating network（Eq. 1--3）。因此标签仍依赖能检测 constraint violation，且把一次 transition 的结果当作 action applicability 信息。
- 执行时取 PSDD 的 MAP symbolic model \(\hat m\)，对满足 \(\hat m\models\varphi_a\) 的动作保留 policy probability，对其他动作置零后重新归一化（Eq. 4--5），以 masked PPO 优化（Eq. 6）。论文称二元 mask/renormalization 保持有效 policy gradient；这不等于 learned mask 对真实状态或未来后果正确。
- 实验覆盖 Sudoku (2×2--5×5)、N-Queens (4--10)、4 个 Graph Coloring task 与 Visual Sudoku (2×2--5×5)，共 16 个合成逻辑任务。Visual Sudoku 以 MNIST 生成图像输入；5×5 state 为 140×140、action 125，PSDD 有 125 propositions 和 782 clauses（§7.1--7.4）。每个 learning curve 的 error band 来自 5 个随机 seed。
- Table 1 的最终 episode violation rate 显著低于列出的 baseline：例如 Sudoku 5×5 为 NSAM 4.3%（PLPG 18.3%、KCAC 94.9%、PPO/Rainbow/RC-PPO 100%），Visual Sudoku 5×5 为 2.5%（PLPG 53.7%、KCAC 88.5%、PPO 100%）；这仍不是零违规。作者也报告训练早期因未训练 PSDD 可能误判前置条件、违规率略高，随后快速下降至 near zero（§7.5、Table 1）。
- 比较对象为 Rainbow、PPO、PPO-Lagrangian、KCAC、RC-PPO、PLPG；消融以普通三层神经网络替代 PSDD，且有 single-transition 的结构泛化示例。结果支持给定逻辑结构的样本效率，不能单独证明对任意视觉/机器人任务的泛化（§7.3--7.7）。

## 安全边界与复现

- PSDD 的严格逻辑一致性仅适用于编译进来的 \(\phi\)，mask 的形式化检查仅适用于从 \(g(s)\) 推断的 \(\hat m\)。若传感器/视觉表征误识别、proposition schema 不全、precondition 写错、约束遗漏或环境动力学变动，系统可“形式上满足”错误模型同时实施危险动作。
- 该方法把 infeasible/unsafe/undesirable 合并为 action precondition；它不编码累计风险、概率不确定性、长期后果、恢复能力、控制屏障、人员安全、法规例外或多目标伦理权衡。硬 mask 还可能意外移除必要的紧急逃逸动作，因此实际 deployment 需要独立 fail-safe/controller、mask coverage 监测和人工 override。
- 训练会主动采集 `y=0` transition，论文承认 grounding 未训练时会有违规。不能用于不允许试错的实体系统，除非先在高保真隔离仿真/离线数据上验证，并在真实系统外层设置运行时 shield、动作权限最小化、限速/急停、uncertainty abstention 与可回滚审计。
- 论文的四类 benchmark 都是显式逻辑约束的离散组合问题，且 5 seeds；没有真实机器人/驾驶/金融测试、分布外约束变化、标签检测失效、攻击性观测、constraint conflict、延迟或人类因素评测。作者将 temporal logic、unknown/incorrect constraints 与 real-world domains 明确列为未来方向（§8）。
- 复现应固定 SDD/PSDD 编译器与 vtree、\(P,AP,\phi\)、action encoding、violation detector、gating/policy 网络、PPO 和 update schedule、seed、mask 为空时的 fallback；并独立报告 false-safe/false-unsafe mask、训练全过程而非最终违规、任务成功、延迟/算力及失效轨迹。

## 与 AAMAS 的关系与核验说明

这是 neuro-symbolic RL 与 action masking 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JWPH6906.pdf) 核对 PSDD/最小 supervision/MAP mask/PPO 流程、16 个任务、5-seed 比较、Table 1 的违规率、早期训练违规现象及 §8 限制；没有把约束内的 learned-symbolic check 误称为端到端或现实世界安全认证。
