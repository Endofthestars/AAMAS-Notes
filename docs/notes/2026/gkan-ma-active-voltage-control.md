---
title: "KAN-Enhanced Graph Learning for Active Voltage Control in Dynamic Power Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "robotics_embodied", "safety_verification"]
dblp_key: ""
doi: "10.65109/WDUC5953"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WDUC5953.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["critical_infrastructure_scope", "ieee_simulation_only", "reward_safety_penalty", "no_hardware_in_loop_or_protection_validation", "not_for_grid_deployment"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# KAN-Enhanced Graph Learning for Active Voltage Control in Dynamic Power Systems

## 一句话总结

GKAN-MA 将动态拓扑 GATv2、Kolmogorov-Arnold Network（KAN）与多 agent actor-critic 结合，用 PV inverter reactive-power actions 调节配电网电压；论文在动态 IEEE 33/141-bus 仿真中提高 controllable ratio，但 reward 中的 voltage penalty 与 benchmark band 不构成真实电网安全或可直接部署证据。

## 方法与证据

- AVC 被表述为 MARL：每个 PV inverter 是 agent，action 为受 inverter capacity 限制的 reactive power；状态含 load、PV active power、reactive injection 与 complex nodal voltage，transition 由 AC power-flow equations 隐式给定（§2）。
- reward 同时惩罚 voltage deviation、network power loss 与超出 operating range 的 safety penalty；论文使用 [0.95, 1.05] p.u. 为 controllable ratio（CR）的 voltage boundary（Eq. 1、§4.1）。
- GATv2 用 current edge matrix 建模不断变化的 grid topology；KAN 以可学习 B-spline functions 表达 voltage-power 的强非线性 mapping，二者送入 centralized value estimation/actor-critic framework（§3）。
- 评估修改后的 IEEE 33-bus（6 PV/3 regions）和 141-bus（22 PV/9 regions）静态与动态 variants；dynamic 33-bus 每 50 steps、141-bus 每 30 steps 变 topology。负荷来自 Portugal 300 customers、PV 来自十 region records，均转为 3-minute resolution（§4.1）。
- 与 GAMARL、MAGRL、MADDPG、MAPPO、IPPO 等比，文中动态 33-bus 最终 CR 为 0.9869；141-bus 也报告 CR 排名优势。ablation 移除 GATv2 或 KAN 后 CR/PL 变差，表明两模块在这些仿真配置下有贡献（§4.2--4.3）。

## 安全边界与复现

- “safe voltage”仅在仿真 reward/CR metric 中用 [0.95,1.05] p.u. 表示；未覆盖 protection relays、faults、N-1 contingencies、communication delay/loss、bad telemetry、cyberattack、inverter hardware limits/thermal dynamics、operator override 或 cascading outage。
- IEEE topology 修改与历史 PV/load time series 不能证明可迁移到真实 feeder、不同 market/dispatch constraints 或极端天气；高 CR/低 loss 也不是 grid-code compliance、stability margin 或 safety case。
- 动态 graph attention 与 KAN 只在特定 control/training distribution 评估；在线 policy exploration 对关键基础设施须放在安全屏障、OPF fallback、certified constraints 与 human operational governance 后面。
- 复现应发布 feeder modifications、topology-change schedule、AC solver、PV/load preprocessing、action/ramp limits、reward weights、training/eval seeds、all voltage trajectories 与 violation severity；另做 real-time/hardware-in-loop、contingency、adversarial telemetry 和 protection coordination 验证。

## 与 AAMAS 的关系与核验说明

这是面向配电网控制的 MARL/graph representation 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/WDUC5953.pdf) 核对模型、reward、IEEE/PV-load 设置、CR/PL 与 ablation；未将仿真中的 voltage regulation 结果表述为生产电网部署或安全认证。
