---
title: "Identifying the Source of Information Spread in Networks via Markov Chains"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "safety_verification"]
dblp_key: ""
doi: "10.65109/LLZL6722"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LLZL6722.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["single_source_assumption", "complete_network_and_weight_assumption", "model_misspecification", "low_identification_accuracy", "privacy_and_misattribution_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Identifying the Source of Information Spread in Networks via Markov Chains

## 一句话总结

论文针对已知完整有向加权网络、单一均匀先验 source 与 Independent Cascade (IC) 扩散的观测 active set，利用 Markov-chain tree theorem 的 stationary distribution 高效计算一个基于 spanning out-tree 权重的 MLE 近似排序。no-loops 转换在受控模拟中优于多个启发式，但即使满足筛选条件，平均 top-1 命中仅为随机图 11.7% 和真实网络拓扑上的模拟扩散 34.7%；它不能识别现实中消息作者、转发首发者或法律意义上的责任主体。

## 方法与证据

- IC 模型中每条有向边有已知 activation probability，扩散从单个 source 开始，每个 newly active node 仅尝试一次激活未活跃邻居；激活节点与激活边形成以 source 为根的 out-tree（§3.2）。目标是给定扩散结束的 active set \(A\)，选择最大 \(P(R_i\mid A)\) 的节点，且论文显式假定所有节点作为 source 的 prior 相等（§4）。
- 精确 ML-Source 在任意图上困难。方法把候选缩至对全部 active nodes 可达的强连通集合 \(A'\)，并将 \(G[A']\) 反向成为 Markov chain；spanning out-tree 与其 in-tree 对应。由 Markov-chain tree theorem，stationary distribution 与加权 spanning in-tree 总和的归一化值相等（Theorem 5.1）。
- 论文承认其 likelihood 是估计：tree weight 为所选边的 activation probability 乘积，忽略不在 spanning tree 内的边；不同 tree events 也不独立，完整修正需 inclusion-exclusion（§5）。self-loops 与 no-loops 两种转换经对应校正能恢复相同的归一化 ranking；直接解 stationary distribution 时相同，random-walk 估计时 no-loops 所需步数更少（Theorem 6.1--6.2、§7）。
- 评测使用 14 类随机有向图（每类保留 1000 个）及 Konect Social 类的 9 个真实网络拓扑。每次均从随机 source **模拟**一次 IC diffusion；若 active nodes 少于 20 或 \(|A'|=1\)，则丢弃并重采样。YouTube friends 的所有扩散都被筛掉，因而从后续分析移除（§7、Table 2--3）。这不是用真实历史传播日志验证归因。
- 在符合上述筛选的随机图 14,000 cases，no-loops direct calculation 平均正确 116.92/1000（11.69%），最强比较基线 maximum-weight arborescence 为 101.07/1000；在 8 个保留的网络各 1000 case，no-loops 平均 347.25/1000（34.73%），arborescence 为 267.875/1000、IM-based 为 217.75/1000（Table 4--5）。方法优于这些 baseline，不代表高置信度的个案定位。

## 安全边界与复现

- 模型要求单一 source、完整节点/边/edge weights、IC 机制、扩散末态 active set 与等先验。隐藏账号、删帖、平台推荐、多平台跳转、bot amplification、外部曝光、多个独立首发、时间变化的影响概率和 non-IC 人类行为都会破坏 ranking 解释。作者也把 missing nodes/edges/weights 与其他 diffusion models 列作未来工作（§8）。
- \(A'\) 的候选裁剪依赖完整图；论文明确说明若边或节点缺失，就必须把所有 active nodes 作为可能 source。将该筛选直接用于不完整社交图会产生结构性 false exclusion，而不是更可靠的调查结论。
- 仅报告 top-1 命中次数，且只在规模足够、非 singleton 的成功模拟上测量；没有 calibration、top-k coverage、置信区间、时间戳噪声、edge-probability uncertainty、对抗传播、多源 diffusion 或真实 ground truth。部署前应按完整未筛选数据与这些失配条件报告不确定性和拒答率。
- source ranking 是敏感的身份/归因推断，可能被用于错误指控、审查、骚扰或执法决定。不得基于此自动封号、公开点名或处罚；应实施数据最小化、访问控制、审计、独立证据交叉核验、申诉/人工复核和对结论的概率性表述。
- 复现须固定网络 snapshot、edge-weight 估计、IC simulation、source prior、\(A'\) 计算、筛除规则、random-walk burn-in/步数或线性解法、tie breaking 与所有 baseline 预算。应区分“真实 topology 上的模拟”与真实传播数据，避免将 Table 5 宣称为现场检测准确率。

## 与 AAMAS 的关系与核验说明

这是网络扩散 source detection 与 Markov-chain 方法论文。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/LLZL6722.pdf) 核验 IC/单源设定、MLE approximation、stationary-distribution 构造、self/no-loops 比较、筛样机制、Table 4--5 结果及 §8 的缺失网络限制；未将模拟中的 source ranking 误写为现实身份归因或责任判定。
