---
title: "MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/PAPW1165"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PAPW1165.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["cbf_assumption_scope", "qp_feasibility", "linearization_and_step_size", "maze2d_only_evaluation", "soft_proximity_violations", "decentralized_communication_error", "no_real_robot_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models

## 一句话总结

MA-SafeDiffuser 在扩散规划的每个 reverse step 后，使用 QP/Dykstra 投影使单体、两两和可选任务级 control-barrier-function (CBF) 约束成立，并给出集中式及有界通信误差下分散式的不变性论证。在自建 Maze2D 中它较无约束 diffusion 少 40--60% 违规，但安全结论依赖 QP 可行、平滑/步长等假设，实验仍记录近障违规，未验证真实机器人或复杂动态场景。

## 方法与证据

- 将联合安全集定义为每个代理自身约束、代理对分离约束和可选 task/global barrier 集的交集。无约束 denoiser 提议更新后，centralized projector 一并修正全部变量；decentralized variant 依靠邻居状态预测和鲁棒 margin 做本地投影，并有 receding-horizon execution-time CBF filter（§2--4）。
- RoS 强制 hard constraints，ReS 允许松弛，TVS 以随扩散时间收紧的 barrier 改善局部陷阱/死锁。三者是不同模式；含 slack 的 ReS 不能被称为无条件硬安全（§3）。
- Theorem 7 的 finite-time diffusion invariance 在 Assumption 3 下成立：active barriers \(C^{1,1}\)、梯度局部 Lipschitz、class-K \(\alpha\)、每个 reverse step 的 QP/projection 可行或适当 relaxations、drift Lipschitz、控制有界且步长足够小。定理的“概率 1”还以每次 QP 可行为条件（§5）。
- Theorem 8 的分散式结论另需邻居预测误差有界 \(\epsilon\)，并取足够的 robust margin（由 barrier/gradient/\(\alpha\) Lipschitz constants 和最大控制量决定）。这并不涵盖通信丢失、时延、未建模动态或错误 state estimation（§5）。
- 实验仅为连续平面 6×6 Maze2D、\(M\in\{2,4,8\}\)、700 steps、三 seeds；安全计数包括 wall proximity、穿墙和出界，且两方法同样 clamp \(\|u\|\le0.085\)（§6.1）。Table 1 集中式 Safe/Unsafe 违规为 9/23.66（2 agents）、11.33/42.66（4）、40/87.33（8），reward 近似相同；分散式则为 16/22.66、45/73.66、70.66/88.66。
- 学习 MLP denoiser 用 1,500 samples、1,000 epochs；四代理表中 Safe 仍为 62 violations、Unsafe 为 125（Table 2）。作者称该 learned-score 结果 preliminary 且可能需要微调；这些“违规”包括保守定义的近墙事件，并非所有都是硬碰撞。
- 对 4-agent Maze2D，Table 3 报 MAPPO-Lagrangian 0% success、532.3 violations，而 centralized/decentralized MA-SafeDiffuser 都 100% success、11.33/45 violations。该比较使用相同 door-waypoint guidance，却不证明对其它 SafeRL 实现、随机地图或真实动力学的普适优势。

## 适用边界与复现

- 适用于可把安全要求写成已知、可微/局部线性化 CBF 的低维或可控多机器人规划研究；应把 diffusion proposal 视为候选计划，并保留独立、实时的安全 filter。
- CBF 安全集与模型/感知准确性绑定。若障碍、动力学、尺寸、延迟、抓地/接触、通信或执行器饱和不被 barrier 正确表示，论文定理不覆盖；实际系统必须先验证每个 barrier、离散化和 QP 可行域。
- 作者明确列出 dense crowds 的 QP feasibility、分散式需要 bounded communication error、以及长 horizon reward shaping sensitivity 为限制（§8）。无解时 ReS/TVS 可能放宽约束，不能将其用于零容忍碰撞任务而没有冗余安全层。
- 复现需固定 Maze2D 几何/门、初始—目标采样、agent/wall/pair clearance、\(H,N,T\)、\(\Delta\tau\)、barriers/\(\alpha\)/margin、centralized/decentralized QP/Dykstra 和通信半径、identical clamp、违规计数/冷却、reward shaping 和所有 seeds；报告硬碰撞与软 proximity 分开、QP infeasibility、延迟、运行时和最坏情况间隔。
- 部署前需要高保真动力学、传感/通信故障注入、动态人/机器人、密集拥堵和急停测试；由仿真中的约束投影得到的减少违规不构成真实机器人、人身或监管安全认证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的多智能体扩散规划与 CBF 安全验证论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PAPW1165.pdf) 核验 Assumption 3、Theorems 7--8、Tables 1--3 和限制段；没有将条件性不变性证明或 Maze2D 的违规减少误称为无条件、零违规的现实部署安全保证。
