---
title: "General Flexible f-divergence for Challenging Offline RL Datasets with Low Stochasticity and Diverse Behavior Policies"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "marl_coordination", "robotics_embodied"]
dblp_key: ""
doi: "10.65109/CKXI1923"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CKXI1923.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["offline_dataset_support_gap", "heuristic_hyperparameter_adaptation", "function_choice_environment_dependent", "negative_density_ratio_interpretation", "simulator_benchmark_scope", "five_seed_reporting", "value_overestimation", "no_online_safety_guarantee"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# General Flexible f-divergence for Challenging Offline RL Datasets with Low Stochasticity and Diverse Behavior Policies

## 一句话总结

论文针对由近确定性、不同水平行为策略混合而成的离线 RL 数据，提出 Flexible \(f\)-divergence：在线性规划（LP）的 Bellman residual 视角下，对数据支持约束的正/负侧使用可调的凸惩罚，并以启发式估计的 \(\alpha_\pm,\beta\) 在训练中调节约束强度。它将此替换进 IQL 类 Bellman 最小化（Flex-\(f\)-Q）和 OptiDICE（Flex-\(f\)-DICE），在新建 MuJoCo/Fetch 混合行为策略数据及 D4RL AdroitHand 上报告部分改进，尤其 Flex-\(f\)-DICE 多数优于 OptiDICE。方法并未自动识别正确约束或消除离线分布外风险：函数组合和超参数依环境/算法而变，有组合会数值爆炸，且放松 \(\zeta\ge0\) 后 density ratio 不再具有通常的重要性采样概率解释。

## 方法与证据

- 离线设定只给静态 transition 数据集 \(D\)，目标是在提升回报时不偏离其 state–action support。作者关注低随机性采集和多行为策略/不同 expertise 的混合，因为统一的悲观约束可能过松或过保守（§1–2）。没有数据覆盖的动作仍不能从该框架获得可靠 value 估计。
- 理论从 MDP 的 value LP 与 occupancy-measure dual 出发，将 Bellman residual \(e_\nu\) 的损失和 density ratio \(\zeta=d/d_D\) 的 \(f\)-divergence 用 convex conjugate 联系；Theorem 1 给出满足指定凸性与导数条件时，\(g(e_\nu)-e_\nu\) 在零 residual 处最小（§3）。这是目标形式的等价/解释，不是有限样本、函数逼近或策略性能界。
- 统一 LP 形式允许在 value/Bellman residual 或 density ratio 上加入 penalty，并把原始不等式约束改为等式；为扩展函数域，作者移除 \(\zeta\ge0\)（§3.2–3.3）。论文明确说明 \(\zeta<0\) 使传统 importance-sampling 解释失效，因此不应把输出当作合法 occupancy ratio 或概率证书。
- Flexible \(f\)-divergence 把基函数的正负区间以 \(\alpha_\pm\) 与阈值 \(\beta\) 调整，意在使正/负 Bellman error 获得不同强度的惩罚（§4）。这些量是额外超参数；训练中 \(\beta\) 的估计为数值稳定被裁在 \([-0.2,0.15]\)，适应过程是启发式而非端到端最优。
- 实作 Flex-\(f\)-Q 直接半梯度最小化 Bellman 形式，概念上接近 IQL；Flex-\(f\)-DICE 是把 OptiDICE 的 divergence 替换为 flexible 形式（§6）。比较保持各对的其他超参数相同，但方法仍依赖所选 \(g_+^*,g_-^*\)、网络/优化和数据构造。
- MuJoCo Hopper/Walker2d/Ant/HalfCheetah 与 Fetch Push/PickAndPlace 的新数据由 SAC/HER 行为策略收集，固定 policy variance 为 0.0，并混合 2、4、10 个不同水平策略；另用 D4RL AdroitHand Pen/Hammer cloned/human 数据。每设置五个 seeds，报告平均 normalized return（§6）。这模拟了挑战性采样，却不是对现实机器人日志、非平稳数据或安全限制的覆盖。
- 表 2 中 Flex-\(f\)-DICE 在许多、但非全部设置改善 OptiDICE：例如 Hopper 4-p 为 99.0 对 77.9、Walker 4-p 为 94.2 对 75.7；但 Hopper 2-p 反而为 40.8 对 45.2，Fetch/Adroit 多个格也下降。Flex-\(f\)-Q 通常接近 IQL，偶有提高（§6、表 2）。因此结果支持“可改善特定困难数据”，不支持稳定支配基线。
- 消融显示没有全环境通用的 divergence 组合：Hopper/Walker 的最佳 \(g_+^*,g_-^*\) 不同；Flex-\(f\)-Q 在 KL/KL 组合发生 explosion（表 3）。作者结论也承认新增超参数，未来才计划将 \(\alpha_\pm,\beta\) 纳入完全可优化的算法（§6–7）。

## 适用边界与复现

- 可作为离线连续控制研究中的一个约束函数族，适合已知数据由不同质量、低探索行为策略混合，且能用保留的离线验证/仿真评估来选择函数与约束强度的场景。
- 不应用于无独立评测的真实机器人、医疗或其他安全关键决策；它不产生 online safety、OOD action 可行性、concentrability 或 policy improvement 保证。若数据缺少危险状态/动作覆盖，调弱惩罚可能放大 Q-value overestimation。
- 复现需公开 transition 数据生成代码、各行为策略 checkpoint/专家水平、2/4/10-p 混合比例、SAC/HER 参数与固定方差、D4RL version，及网络、batch、学习率、训练步数、五个以上 seeds、评估 episodes 与 normalized-return 公式。
- 应网格或贝叶斯搜索 \(g_+^*,g_-^*,\alpha_\pm,\beta\) 并记录裁剪、NaN/explosion、Q/residual/ratio 分布；与 IQL、OptiDICE、CQL、TD3BC 在同一数据切分比较。额外报告 support coverage、最差 seed、置信区间和对更少覆盖/分布移位/真实日志的鲁棒性。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 offline RL、优化与机器人控制工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CKXI1923.pdf) 核验 LP/convex-conjugate 论证、移除非负 ratio 约束的含义、Flex-\(f\)-Q/DICE 实作、数据集构造、表 2–3 的非一致结果和作者所述超参数限制；没有将其表述为普适的离线 RL 改进或部署安全保证。
