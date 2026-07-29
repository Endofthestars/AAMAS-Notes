---
title: "Multi-Agent Decision S4: Leveraging State Space Models for Offline Multi-Agent Reinforcement Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/YJTX3478"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YJTX3478.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["offline_dataset_dependence", "sequential_agent_order_assumption", "latent_communication_semantics", "benchmark_scope", "on_policy_finetuning_instability", "return_conditioning_heuristic", "no_real_world_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Multi-Agent Decision S4: Leveraging State Space Models for Offline Multi-Agent Reinforcement Learning

## 一句话总结

MADS4 将 Structured State Space（S4）序列模型用于 offline cooperative MARL：在 Sequentially Expanded MDP（SE-MDP）里，同一环境时刻的 agents 依序决策，每个 agent 只接收前一 agent 的 S4 latent state，借可微 shared memory 将此前信息/梯度沿链传递。它用卷积视角做离线长轨迹训练、recurrent 视角做 on-policy 微调；RWARE 全部六个配置领先表中基线，SMAC 多数 medium/poor 与两个难图具有竞争力或领先，但并非每个 map/data-quality 条件都最佳。

## 方法与证据

- offline MARL 的难点是 joint state-action 的指数增长和 distribution shift。MADS4 将一时步 joint action 拆为 \(n\) 个 mini-step：第 \(i\) agent 的输入包括自己的 observation/global state、past action/return-to-go 与前一 agent 的 hidden S4 projection；训练时 gradients 也沿该 memory 回传（§3--§4）。
- S4 在全 trajectory 可用的离线训练采用并行 convolutional mode，在 rollout/fine-tuning 采用 recurrent mode；作者主张其序列长度上比 transformer 固定 context 更灵活、推理相对 sequence length 为常数时间。模型默认 \(H=N=96\)、约 200k parameters，对比文中 MADTKD 的 1.8M（§3.4、§4.1、§5.4）。这是架构/参数量比较，并非完整的 wall-clock benchmark。
- 共享仅需“前一 agent→当前 agent”的单条 latent link，宣称 constant communication-memory overhead；其合作语义依赖 agent order 与训练时可访问的 latent representation，并非无通信 CTDE 的等价替代（§3.4）。作者也测试 random vs fixed order，报告相近表现，但所测场景有限（§5.4）。
- 离线数据：RWARE 来自 MAT 训练的 expert trajectories（tiny/small，2/4/6 agents）；SMAC 来自 MAPPO good/medium/poor data，在 5m-vs-6m、2c-vs-64zg、6h-vs-8z、corridor 四图测试。离线评估为 30 episodes、5 seeds，desired return-to-go 设为数据中最高 return 的 110%（§5.1--§5.2）。
- RWARE Table 1 中 MADS4 是全部六列最高：tiny 2/4/6 agents 11.79/15.52/17.29，small 2/4/6 为 6.58/9.47/10.87；例如最佳非本方法 AlberDICE 在 small-6 是 9.65。结果支持仓库型长轨迹协作的优势。
- SMAC Table 2 是混合结果：MADS4 在 2c-vs-64zg 的 good/medium/poor 为 19.40/17.27/14.67，并在 6h-vs-8z 的 good/medium/poor 为 12.75/12.57/11.89；但 5m-vs-6m good 时 OMIGA 8.25 高于 MADS4 8.00，corridor good 时 MADT 17.81 高于 MADS4 16.02，corridor poor 时 MADT 8.76 高于 8.57。因此应称“多数配置竞争力强”，而非全局 SOTA。
- online fine-tuning 基于 MAPPO actor--critic。作者发现 offline pretraining 后继续交互通常提升，但长时间 recurrent S4 training 可能因 error accumulation 降级；通过冻结 state-transition kernel \(A\)、仅微调 input-dependent \(B,C\) 缓解（§4.2、§5.3）。这说明微调仍须 early stopping/回归监测。
- ablation 显示与独立 IDS4 相比，顺序 latent sharing 在复杂多 agent maps 提高 return；full-length trajectory pretraining 优于截断；parallel decentralized variant 用前一时刻 hidden states 作为 proxy，论文报告未见性能下降（§5.4）。后者仍假设同步时序和可用历史 memory。

## 适用边界与复现

- 适用于有静态离线 trajectory、shared cooperative reward、可定义稳定 agent ordering 或上一时刻 memory 的多机器人/仿真控制任务，特别是长 context 很重要而 transformer memory 成本受限时。
- 不适用于把 latent state 当作可解释、可信或安全通信的场景；对 adversarial/corrupted agent、异步通信、异构 agent、partial data coverage 和 non-cooperative games，论文没有充分验证。
- 复现应固定 RWARE/SMAC dataset 版本、split/quality、return-to-go 目标、state/observation access、agent ordering、action masks、S4 HiPPO/N/H、context padding、5 seed/30-episode protocol；逐列复现 Tables 1--3，且报告 parameters、throughput、GPU/CPU memory 与完整置信区间。
- 若做 on-policy 微调，记录 pretraining-only 对照、S4 \(A\) freeze、\(B,C\) learning rate、rollout budget、性能随训练时间曲线和最差 seed；部署前加入 OOD detection、行为约束和安全 shield，offline return 提升不等于真实系统安全。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 offline MARL、序列建模与协作表示工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YJTX3478.pdf) 核验 §3--§5 的 SE-MDP/S4/微调设计、Tables 1--3、agent-order/decentralized/context ablation 与 §6；没有把选择性基准优势或参数量主张泛化成所有 offline MARL 的性能和安全保证。
