---
title: "Multi-Objective Coverage via Constraint Active Search"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "resource_allocation", "agent_engineering"]
dblp_key: ""
doi: "10.65109/XTVI9400"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XTVI9400.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["gp_model_assumption", "threshold_specification", "coverage_radius_sensitivity", "surrogate_objective_scope", "independent_objective_gp_assumption", "computational_optimization_cost", "no_wet_lab_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Objective Coverage via Constraint Active Search

## 一句话总结

论文提出 Multi-Objective Coverage（MOC）：在每个 objective 有 threshold 的可行区域内，用有限评估挑一小组 outcome 彼此分散的代表样本，而非覆盖输入样本空间或逼近 Pareto front。MOC-CAS 为各 objective 拟合独立 GP，用 UCB feasibility 与新增 objective-space coverage 选择候选，并把硬约束/球并集平滑化以可微优化；在 SARS-CoV-2 和 cancer protein-target 数据上优于所比基线的 positives、AUP 和 fill distance。结论依赖预测目标、阈值、GP 校准和覆盖尺度 \(r\)，不等价于真实药物活性或临床效用。

## 方法与证据

- 输入集合 \(X\) 的黑箱输出是 \(m\) 维 \(f(x)\)，每维 threshold 定义 feasible objective region。给定 resolution \(r\)，若两个 outcome 距离小于 \(r\) 就视为冗余；目标是用观察到的 feasible outcomes 的 \(r\)-balls 覆盖更多输出空间（§1、§3）。因此它服务于“多种可接受方案”的 down-selection，而非最大 hypervolume/Pareto frontier。
- MOC-CAS 为每个 objective 建独立 Gaussian process。每轮以 UCB 估计候选是否能越过 per-objective thresholds；只有 optimistic feasible candidate 才获得新增 coverage 价值。coverage tie 以离已选 feasible outcomes 最远的 objective-space distance 打破，鼓励分散（§3--§4）。
- 为使 acquisition 可优化，论文用 unit-mass Gaussian kernel 平滑 \(r\)-ball、用 probit gate 平滑可行 orthant、用 soft kernel sum 平滑已覆盖球并集，得到可微的 local average/novelty term，采用 multi-start L-BFGS 或类似法（§4）。这些是对原硬覆盖的近似，选择效果取决于 smoothing、GP posterior 与数值优化。
- 与 CAS 的不同是：过去 ECI/CAS 在 sample space 做 fill-distance coverage；MOC-CAS 在 outcome/objective space 覆盖。与多目标 BO 的不同是：不追 Pareto front/hypervolume，而奖励阈值内的代表 outcome（§1--§2）。
- 数据为大规模 protein-target 分子集合：SARS-CoV-2 与 cancer 任务，每个用从 SMILES 特征得到的五个 objectives；论文还列出 WRN 结果于 Appendix。评估包含 positive feasible samples、AUP 和 fill distance；四个 trial 的均值±调整标准误（§6.1）。这些是数据库/预测指标而非湿实验 outcome。
- 比较包括 One-Step active search、sample-space CAS/ECI、level-set straddle、MOO+Cluster 等。论文报告在 SARS-CoV-2 中 MOC-CAS 三指标最好；straddle 在 positives/AUP 上最弱，MOO+Cluster 在 posterior uncertainty 高时较弱（§6.2）。Cancer 三蛋白（6T2W、RTCB 等）同样报告整体优势，但受 feasible region 稀疏/碎片程度影响（§6.3）。
- ablation 显示 \(r\) 改变 coverage granularity：较大 \(r\) 倾向更低 fill distance/更高 positives，SARS-CoV-2 3CLpro 的中间 \(r=0.05\) 有较高 AUP；UCB exploration 参数 \(\beta_t\) 也影响阈值附近探索。作者明确没有一个固定设置对 cancer/viral targets 一律最优（§6.4）。
- 论文开源 appendix/code，讨论目标是加速科学迭代而非全面枚举 feasible set（§1、§7）。它没有对 correlated objectives、多保真湿实验、测量噪声偏移、合成可行性或候选 safety 作完整验证。

## 适用边界与复现

- 适用于预算有限、决策实际发生在多个测量 outcome 上、且需要一组多样 threshold-compliant 候选的科研筛选/材料/配置探索。
- 不应在药物、材料或安全参数选择中只依赖 surrogate feasibility：阈值、尺度、objective normalization、GP calibration 和 input domain 变化都可导致虚假 coverage 或忽略关键风险。
- 复现应固定 candidate pool、五 objective 的方向/normalization/threshold、initial design、independent GP kernel/noise/UCB、\(r\)、soft-relaxation、optimizer restarts、budget、random trials与所有基线；报告 positives/AUP/fill distance 的完整学习曲线及候选重复率。
- 真实应用需将 MOC-CAS 输出作为实验优先级队列，加入湿实验/高保真验证、uncertainty calibration、batch/diversity/合成约束、failure labels 与安全审查；可为相关 objectives 使用 multi-output GP 或对独立性假设作消融。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的约束主动搜索、多目标决策与科学发现工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/XTVI9400.pdf) 核验 MOC 定义、MOC-CAS 的 UCB/平滑优化、§6 的数据/基线/ablation 与 §7；没有将目标空间覆盖的离线性能误表述为经过实验验证的药物或材料发现成功。
