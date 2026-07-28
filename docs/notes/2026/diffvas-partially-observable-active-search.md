---
title: "DiffVAS: Diffusion-Guided Visual Active Search in Partially Observable Environments"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "robotics_embodied", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/PUUC3893.pdf"
preprint_url: "https://arxiv.org/abs/2605.15519"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["synthetic_partial_observability", "diffusion_reconstruction_error", "satellite_dataset_generalization", "uav_deployment_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# DiffVAS: Diffusion-Guided Visual Active Search in Partially Observable Environments

## 一句话总结

DiffVAS 面向有限查询预算下的目标条件视觉搜索：先用 diffusion conditional generative module（CGM）从已见卫星图像块重建搜索区域，再以 target-conditioned PPO planner（TCPM）选择下一格，从而兼顾探索与目标发现。

## 方法与证据

- 作者定义 TC-POVAS：一张航拍图被划为网格，agent 仅在访问单元后看到该图像块及其真值标签；给定目标类别集合 $Z$ 和预算 $B$，目标是最大化被查询到的目标单元/实例覆盖（§2）。论文主实验把移动成本设为均匀，故 $B$ 实际为查询次数。
- CGM 以随机遮蔽的历史观测为条件训练 diffusion noise-prediction loss；训练 TCPM 时冻结 CGM，用重建图的 latent 与已观测图像 latent 的拼接作为视觉 state，并加入 CLIP 文本目标 embedding、历史 target observation 与剩余预算（§3.1）。
- TCPM 使用 actor-critic PPO，reward 同时包含 active-search target reward、global reconstruction quality 和 local uncertainty 成分；多目标推理对每一个目标类别产生 cell distribution，再将这些分布相乘后采样下一格（§3.1–3.2、Algorithm 1）。
- 评测指标为 Average Number of Targets（ANT）。主实验在 DOTA 的 $5\times5$ 网格、$B\in\{5,7,10\}$，与 Random Search、全局可见的 E2EVAS、单目标 MPS-VAS 对比；单目标场景相对最强 MPS-VAS 提升 8.9%–28.8%，多目标场景提升 8.3%–48.8%（§4、Tables 1–2）。
- 消融显示移除 CGM reconstruction latent 后 ANT 降低（报告相对差 8.1%–37.7%）；以预测 target cell 的 greedy planner 替换 PPO planner 也更差，完整 reward 在所列设置表现最佳（§4、Tables 3–5）。
- 零样本实验只在 DOTA 上训练、在类别集不重合的 xView target set 上测试；表中相对基线提升 36.3%–281.5%，但该数字仍处于两套预标注卫星数据及指定预算/网格的离线模拟内（§4、Table 7）。

## 局限与复现

- “部分可观测”是预先分割卫星图后逐格揭示的模拟，主结果采用均匀移动成本；它不等同于真实 UAV 的连续动力学、相机姿态、飞行风险、带宽、目标检测错漏或非均匀航程成本。
- CGM 的重建是生成模型预测而非环境真相。早期 history 较少时的幻觉、地域/季节转移或稀有类别偏差都可能把 planner 引向错误区域；论文将已观察 latent 一并输入是缓解措施，不是误差上界。
- xView/DOTA 的 train/validation/test 分割为 50%/17%/33%，主结果使用 DOTA；跨数据集检验只覆盖一个 DOTA→xView 方向与少数不重叠类别，不能推出任意地理区域、实时图流或救援任务的泛化。
- 复现应固定 image tiling、类别/实例标签到网格标签的映射、初始观测、预算和成本矩阵、CGM checkpoint/随机遮蔽、PPO/CLIP 参数、reward 权重及 seed；还应报告按稀有类、不同飞行成本和带检测器噪声的结果。

## 与 AAMAS 的关系与核验说明

该文将部分可观测规划、生成式场景重建和 UAV 风格视觉搜索结合，属于 planning、embodied agent 与应用型多 agent/自治系统研究。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2605.15519) 核对了 TC-POVAS 任务、训练流程、ANT 对比和零样本范围。
