---
title: "Building Large-Scale Drone Defenses from Small-Team Strategies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "safety_verification", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/GYJS4496"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GYJS4496.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["drone_defense_dual_use", "simulation_only", "full_observability_assumption", "independence_approximation", "llm_generated_heuristics", "no_operational_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Building Large-Scale Drone Defenses from Small-Team Strategies

## 一句话总结

论文以分阶段 GA--DP pipeline 将小规模防御队的整套 heuristic chromosome 组合成大规模 drone-defense 配置：先在 1--5 attackers、1--8 defenders 上演化，再以动态规划分配子队、在大规模仿真采样并根据真实组合表现迭代重加权。相较直接大规模 GA，模拟胜率提高；但评测是开放二维、全可观测、确定动力学的 pursuit--evasion playground，DP 对子战斗成功概率的可组合性只是近似，不能视为针对真实无人机群的安全、识别、通信或交战部署验证。

## 方法与证据

- 环境为固定关键资产的开放二维场地。Red attackers 从随机初始半径/角度出发，沿随机 sinusoidal paths 接近目标；Blue defenders 以 turn/acceleration 控制，具有对所有友军和对手的完全可见状态。目标仅为阻止 Red 到达目标的 win rate（§3.1）。
- 每个 Blue agent 的 gene 编码 heuristic、spawn location 和该 heuristic 参数；整个 team chromosome 才是 GA 的有效 building block。低层 heuristic 做拦截/编队/威胁优先等动作，高层以分配这些 heuristic 协调；没有 RL 的 policy/value learning（§3.2--3.4）。
- Stage 1 在 1--5 Red、1--8 Blue 小队中以平均 128 episodes win rate 评估：随机初始 population 1024，20% elitism、tournament selection、70% single-point crossover 与 mutation。候选包含手写和 LLM 一次生成后转为 JAX 的 heuristics（§3.4--3.5）。
- Stage 2 以小队经验成功率 \(P(r,b)\) 把 \(R\) attackers partition 为子群、把 \(B\) defenders 分配给各子群，最大化 \(\prod_i P(r_i,b_i)\)。固定预计算最大子群大小 \(k\) 时，作者给出 DP worst-case \(O(R^3B^3)\)；这避免暴力枚举的组合爆炸，但前提是子群结果可近似分解（§3.6、Proposition 1）。
- Stage 3 依据 DP allocation 抽样整套高表现小 chromosome，在完整大规模 simulation 中直接评估；Stage 4 将 Stage-1 prior 和组合中观察到的表现按 \(K=200\) 平滑加权，避免小队强策略在大队失效仍被保留（§3.7--3.8）。
- 图 4 的内部 baseline 是随机 chromosome 与直接对大规模问题跑同一 GA，不是外部 drone-defense/MARL benchmark。20 Red、Blue/Red=1.5 时，Stage 3 的最佳 chromosome win rate 0.69，而 direct-GA baseline 为 0.13；Stage 4 在 20 Red、ratio 1.3 的 top-10% 从 0.22 升至 0.45（§4.1--4.2）。
- 在最具挑战的 30 Red scenarios，Stage 4 最佳 chromosome win rate 为 0.52；小 swarm 的某些 ratio 才超过 0.80。论文声称测试至 30 attackers、45 defenders，但结果并非“稳定拦截所有对手”（§1、§4.2、Figure 4）。
- gene-level 独立重组明显变差，支持“synergistic full chromosome”而非单个 heuristic 是搜索单位的结论；最终高频组合包括 Predictive Interception 和 Threat-Level Assessment（§4.3、Figure 5）。

## 安全边界与复现

- 这是防御性、双用途的 swarm coordination 研究，笔记仅记录抽象优化结果；不提供拦截轨迹、目标识别、武器/载荷配置或实际行动指导。现实系统应经过合规授权、人工监督、地理围栏、可靠的 fail-safe/abort、审计与独立安全评估。
- 模型假定 full observability、确定性 dynamics、无通信限制、开放无障碍场和固定资产；未建模传感器误报/遮挡、定位延迟、风、动力/电池、碰撞、链路攻击、非合作飞行器、禁飞区、法律约束和人群风险。论文也将 partial observability、动态 adversary、障碍、异构能力与在线 adaptive learning 列为未来工作（§4.3、§5）。
- DP 的乘积目标不是多队相互影响下的真实成功概率；Stage 3/4 的完整仿真与再权重只是对该近似的经验修正，不给全局最优性、鲁棒性或安全证明。迁移时需要对协同干扰、通信故障和 adversarial distribution shift 作压力测试。
- “LLM 产生 heuristic 的偏差会被 simulation selection 中和”仅对给定 simulator/metric 成立；不能保证边界条件、长尾事件或现实对手上的正确性。候选代码仍应进行 sandbox、静态/动态安全审查和 independent red-team evaluation。
- 复现应固定场景随机化、动力学/碰撞规则、终止条件、win-rate 定义、seed、JAX/硬件、每 chromosome episodes、GA population/selection/mutation、heuristic 库及 LLM-generation provenance、\(P(r,b)\) 表、\(k\)、DP allocation、Stage-3 sampling 和 \(K=200\) 更新；同时报告置信区间、失败模式、计算成本和未见 adversary/partial-observation robustness。

## 与 AAMAS 的关系与核验说明

这是 adversarial multi-agent coordination 的层次化进化/动态规划工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GYJS4496.pdf) 核对场景与可观测性、四阶段流程、Proposition 1、GA 参数、Figure 4 的数值、chromosome 消融及作者列出的限制；没有把 simulation win rate 或 factorized allocation 误写为现实无人机防御的交战能力或安全认证。
