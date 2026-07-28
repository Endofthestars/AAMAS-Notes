---
title: "Modelling Customer Trajectories with Reinforcement Learning for Practical Retail Insights"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/AJIK9102"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AJIK9102.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["single_store_dataset", "offline_trajectory_proxy", "simulation_based_profit", "uniform_margin_assumption", "reward_filtered_rollouts", "no_live_ab_test"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Modelling Customer Trajectories with Reinforcement Learning for Practical Retail Insights

## 一句话总结

论文把便利店顾客走行建模为 conditional maximum-entropy RL：PPO agent 在 gridworld 中按购物篮、checkout 和可选步数预算生成路径，以终点的取货/checkout/时长奖励和完成后状态覆盖 bonus 学习多样路线。对一间店的匿名轨迹，RL 比 TSP/PNN 更接近观测路径与货架访问密度，并在一个单簇、两种 impulse 商品的重新摆放**模拟**中选出与 human-trajectory reference 相同的方案；这证明的是该店离线数据与建模假设下的 proxy fidelity，不是实际门店收入、因果 uplift 或跨店泛化。

## 方法与证据

- 数据来自一间安装 overhead camera 的 local convenience store，收集期为 2023-09--2024-02；3D joints 以 5 Hz 记录，并关联 checkout baskets。清洗、二维化、网格映射、推断 pickup 后剩 3,054 条轨迹（§3.1、§3.3）。没有报告多门店/季节/促销条件或独立上线实验。
- 店铺被离散为 16×36、每格 50×50cm 的 MiniGrid gridworld；只保留 top-61 畅销品（约 51% sales），按 11 个 category 建模，每 shelf 只放一个 category（§3.1）。剩余商品与品类/库存/价格变化、拥堵和人际互动未进入环境。
- PPO+CNN 的 conditional MaxEnt agent 观察 layout/object、step、可选 budget、未访问 mask、categories、basket、位置/朝向；action 是前进、左右转、pickup/checkout。checkout reward 按正确取货、正确 checkout、接近目标时长给分，\(\gamma=1\)，完成主目标后按 unique states 给 exploration bonus（§3.2--3.4）。这并非从人类轨迹 inverse-RL 得到的真实偏好/reward model。
- train baskets 为 0--5 products，课程式由简单到复杂、并行环境与 channel normalization；用于生成的 RL rollout 还只保留超过 minimum reward threshold 的轨迹（§3.4--3.5）。这种筛选会提高“可完成 basket”的样本质量，比较时需考虑 selection effect。
- 以 real dataset 已出现的 basket/checkout 组合为条件，每法 sample 10k trajectories；可用条数不足的 human/TSP 以 replacement upsample。按 basket 聚合为 2D distribution，再报 JSD/WD（§4.1）。这比较的是同店、同已见购物篮的空间 occupancy，不是 prospective customer choice 或未见 basket prediction。
- Table 1：RL average JSD/WD 为 0.476/0.00920，低于 PNN 0.676/0.0142、TSP 0.777/0.0176；average heatmap JSD/WD 为 0.415/0.00800，低于 0.580/0.0120 和 0.657/0.0140。结果支持空间路径 proxy 更接近人类，不能单由 divergence 得出利润或满意度结论。
- Shelf traffic density 将到 shelf adjacent cell 记作 visit。比例采样时 RL JSD/WD 0.430/0.217，对比 PNN 0.549/0.278、TSP 0.632/0.313；uniform-basket 时 RL 0.347/0.00676，仍低于 TSP/PNN 约 0.505/0.0106（§4.2、Table 2）。指标受 basket sampling、网格/adjacency 定义影响。
- impulse-rate 推算为 \(P_{purchase}=P_{visit\ shelf}P_{impulse}\)，因每 shelf 单品类设 visibility=1。以 elbow 方法将 61 baskets 划三 clusters，将 cluster 内 purchase probability <20% 的 category 定为 impulse；这是一套 operational definition，不分离广告、价格、库存、促销、顾客异质性和实际曝光（§4.3）。
- Cluster 2 中 TSP/PNN 不经过两种 impulse 商品货架，分母为零；RL 给 Fruits/Yogurt 0.0577、Soft Drinks 7.20，human reference 0.115、3.20，虽然绝对值偏差很大但 ordering 相同（§4.3、Table 4）。因此“识别排序正确”不等于 impulse-rate 校准。
- 重摆只研究 Cluster 2、一个 impulse product、两个空 shelf。商品以 \(i_p\times price_p\times margin_p\) 选取；缺少真实 margin 时统一假设 5%，TSP/PNN 无 visit 的商品还以 purchase frequency proxy impulse rate（§4.4）。
- 新 layout 的评估不是现场改店：把原 layout 中购买 essentials 的实际人类轨迹 rollout 到 modified gridworld，并施加原布局推得的 ground-truth impulse rates。Table 6 的 human-evaluated average impulse profit/customer 为 TSP 0.0900、PNN 0.0501、RL 0.162、human recommendation 0.162；它是同一轨迹和假设下的仿真估计，不能解释为已实现的 dollar uplift（§4.4、Table 6）。

## 适用边界与复现

- 适用于有明确平面图、商品/checkout mapping、历史 basket 与可合法使用的轨迹数据的离线 layout screening；实际部署前需按门店、时段、客群、basket size、拥堵和促销做 out-of-time/out-of-store validation。
- 轨迹更像不等于顾客看到商品、愿意购买、复购、满意或长期收入更高。重摆会反过来改变路线、可见度、替代/缺货、收银排队、员工补货和客户体验；须用随机化 A/B 或逐店 phased rollout，预注册主指标、guardrails 和停止规则。
- 不应把 $0.162 simulated average profit/customer 或 5% margin 假设用于财务承诺。部署需以 SKU-level costs/margins、库存/废损、促销、价格弹性、替代需求、合规/安全/无障碍和客诉等真实数据重估，并报告不确定区间。
- MaxEnt/PPO reward 是 designer-defined task completion+exploration，不保证 recovered human utility；其 policy 为每个新 layout 重训，作者明确称训练昂贵、目前无法跨 layout 直接泛化。应测试 reward、minimum-return filter、grid resolution、budget/basket distribution、checkout mix、random seed 与 layout perturbation 的敏感性（§5）。
- 复现应固定原始数据访问/匿名化流程、time window与剔除规则、camera-to-grid mapping、61 product/category/shelf mapping、basket clusters、PPO network/hyperparameters/reward/filter、TSP/PNN implementation、10k sampling/replacement、JSD/WD/visit definition、prices/margin/impulse formula与 modified-layout evaluator；特别报告 train/eval overlap 和全部 failure cases。

## 与 AAMAS 的关系与核验说明

这是 retail applications 中的 agent-based trajectory modelling 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/AJIK9102.pdf) 核对门店数据范围、grid/PPO/reward与 trajectory filter、Table 1--2 divergence、impulse-rate construction、Table 4--6 和作者明确的单客群/单商品、需重训及未来真实部署限制；没有把同店离线 trajectory proxy 或仿真利润误写成已验证的经营因果增益。
