---
title: "QD-MAPPER: A Quality Diversity Framework to Automatically Evaluate Multi-Agent Path Finding Algorithms in Diverse Maps"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/UZVN6052"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UZVN6052.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["generator_objective_induced_bias", "grid_map_and_instance_sampling_scope", "implementation_timeout_and_hardware_dependence", "algorithm_comparison_not_global_ranking"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# QD-MAPPER: A Quality Diversity Framework to Automatically Evaluate Multi-Agent Path Finding Algorithms in Diverse Maps

## 一句话总结

QD-MAPPER 用 CMA-MAE 搜索 NCA 生成器并以 MILP 修复连通 grid map，按 MAPF 运行结果把难度与地图特征填入 QD archive；它能为六个 MAPF 算法找到固定 benchmark 未覆盖的反例地图，但生成分布由目标、descriptor、超时、起终点采样和实现版本共同定义，不能产生全局算法排名或真实机器人可靠性结论。

## 方法与证据

- NCA 从固定 seed 生成图，MILP 以最小 Hamming 修改保证空格连通和障碍数范围；CMA-MAE 按 QD-score 更新 archive。实例以 bucket method 均匀采样 starts/goals，每图运行 `N_e` 个实例（§3、图 1）。
- one-algorithm 模式对 CBS/EECBS/PBS/LaCAM3 最大化平均 CPU runtime（超时截为 `T`），对 PIBT/LTF 最小化 regularized success rate；two-algorithm 模式最大化 EECBS--PBS runtime 差或 PIBT--LTF RSR 差（§3.2）。
- 论文在所有算法上生成 10,000 maps，选择障碍数和相对 maze tile-pattern KL 作为 diversity measures；以 CBS/EECBS/PBS 50 agents、LaCAM3 100、PIBT/LTF 150，且每 map 5 instances 的设置报告新失败模式（§3--5）。
- 例如 200-instance 验证中，PIBT 在某类高障碍/one-entry 地图的平均 success rate 比 LTF 高 14%，另两类 LTF 地图高 20%；这些是被 QD 搜到的特定地图类型，不是跨所有地图的胜负结论（§5、表 1）。

## 局限与复现

- “多样”仅覆盖 chosen obstacle count/KL descriptor；NCA 架构、seed、MILP repair 和 maze pattern prior 会排除或偏好某些布局。QD 最大化的失败/差距也会诱导对目标算法不利的 test distribution。
- 地图是四邻域静态 grid，bucket starts/goals、固定 agents、`N_e=5`、makespan/timeout 和算法源码决定结果；动态障碍、连续运动、传感误差、异构机器人、任务分配及真实仓库不在范围。
- runtime 不能在硬件、语言、优化和 timeout 不同的实现间直接比较；RSR 与 SoC 的 lexicographic regularization 也把特定效率/成功偏好写入评价。应报告原始 seeds、完整 archive、失败类型与资源使用。
- 复现应锁定 NCA/CMA-MAE/MILP 参数、障碍区间、descriptor bins、MAPF commit/hyperparameters、CPU/GPU、time/makespan、所有 10,000 map 与 starts/goals；用 held-out generators、多个采样器和 200+ instance 复核观察。

## 与 AAMAS 的关系与核验说明

该文研究多智能体路径规划算法的程序化、质量多样性评测。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/UZVN6052.pdf) 核对 NCA+MILP、目标函数、descriptor、10,000-map 协议和表 1；未将生成地图上的算法差异外推为普遍 MAPF 排名或实体机器人性能。
