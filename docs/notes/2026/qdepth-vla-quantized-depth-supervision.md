---
title: "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/LJRK3716"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LJRK3716.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["monocular_depth_pseudolabels", "vqvae_representation_loss", "benchmark_and_task_scope", "limited_real_robot_trials", "additional_model_compute", "perception_control_coupling", "no_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models

## 一句话总结

QDepth-VLA 以离线估计的深度图经 VQ-VAE 量化后的 token 为辅助预测目标，由独立 Depth Expert 学习几何表征，而 Action Expert 仍生成动作；推理只需 RGB。论文报告在 LIBERO、Simpler 和 Piper 实臂操控上优于 Open \(\pi_0\) 等基线，但深度是单目伪标签、真实评估样本很小，不能构成复杂环境或安全操控保证。

## 方法与证据

- 训练深度由 Video-Depth-Anything（ViDA）对 VLA 数据做单目估计，VQ-VAE 把 depth maps 编为离散 latent tokens。Depth Expert 预测 token，action branch 预测 action，hybrid attention 将几何线索选择性路由；总损失为 \(L_{action}+\lambda_tL_{depth}\)（§3）。
- 采用 PaliGemma-3B VLM backbone，Action/Depth experts 均为 18 layers、8 heads、hidden dim 1024 的 Transformer；前者输入 proprio+action、后者输入 RGB image tokens。附加 branch 将参数从 Open \(\pi_0\) 的 2.606B 增至 2.924B（+12.2%）（Table 1、§4.3.5）。
- LIBERO：在 Spatial/Object/Goal/Long 四套件训练/评估，单视图 QDepth-VLA 的平均 success 为 85.4%，论文称比 Open \(\pi_0\) 高 6.1%（最大 Spatial 增益 8.8%）。这里与多视图模型的输入条件不同，应按同视图基线解释（§4.1、Table 2）。
- Simpler：Bridge 训练的 WidowX250 与 Google Robot 任务均在 visual matching 配置、不同 initial positions 下各 10 次评估；QDepth-VLA 在 Google Robot 表中平均 75.1%，WidowX250 表中 68.5%，并在长 horizon/空间任务报告改善（§4.1、Tables 3--4）。
- 真实 Piper 6-DoF 臂配 RealSense D455，四个 pick/place/stack tasks 每个收集 50 trajectories、评估 10 trials。QDepth-VLA 对论文所列 ACT/Open \(\pi_0\) 基线有提高，文中以 task 3/4 的 10% gain 等说明；十次试验的成功率不确定性大，且环境/对象/相机配置固定（§4.2、Table 5）。
- 消融：去 Depth Loss 平均 68.5→65.6；去 Depth Expert 到 60.0；以 pixel depth regression 替换 latent prediction 在部分 task 降幅明显；去 hybrid attention 平均降约 5.5%。这些支持量化深度和独立 branch 在该配方的作用，但不分离 ViDA 深度误差与 VQ-VAE codebook 的贡献（§4.3、Table 6）。
- 深度标注预处理 Bridge/Fractal 约 4 小时；作者称实臂 control latency 与 Open \(\pi_0\) 接近。结论列出未来探索更有效 VAE depth 表示，未报告碰撞、力控制、分布外物体或故障恢复（§4.3.5、§5）。

## 适用边界与复现

- 适用于已有 RGB VLA 训练数据、希望以训练期辅助任务提升几何关系表征而不在推理加入深度传感器的研究型机器人操控。
- 单目伪深度可能在透明/反光/遮挡、尺度变化、快速运动与相机外参漂移下错误；离散 token 会丢失细节，辅助几何 loss 也可能与动作目标冲突，均需在目标场景验证。
- 复现应固定 ViDA 版本/预处理、VQ-VAE/codebook、PaliGemma/Open \(\pi_0\) checkpoint、hybrid attention、\(\lambda_t\) schedule、Fractal/LIBERO/Bridge 数据与 augment、Simpler visual matching/initial states、Piper tasks、50 demonstrations和10 trials；报告 per-task success、seeds、延迟、参数/显存和深度质量。
- 部署前应加入显式深度/碰撞/力传感交叉检查、工作空间与速度限制、低置信度停机、人工接管、遮挡/反光/对象位置变化压力测试；VLA success rate 不能替代安全认证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 VLA、空间感知和具身机器人论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/LJRK3716.pdf) 核验 quantized-depth 架构、LIBERO/Simpler、Piper 设置、消融和计算成本；没有将有限真机 trial 或仿真 success 误称为通用 3D 理解或安全操控能力。
