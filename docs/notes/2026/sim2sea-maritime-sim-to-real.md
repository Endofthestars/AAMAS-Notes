---
title: "Sim2Sea: Sim-to-Real Policy Transfer for Maritime Vessel Navigation in Congested Waters"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/CMRP6518"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CMRP6518.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["safety_critical_maritime_deployment", "simulation_reality_gap", "velocity_obstacle_model_limit", "limited_real_world_trials", "fixed_speed_control_scope", "no_regulatory_certification"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Sim2Sea: Sim-to-Real Policy Transfer for Maritime Vessel Navigation in Congested Waters

## 一句话总结

Sim2Sea 将 GPU 并行船舶模拟器、含 temporal Transformer 与 BEV 的双流 PPO policy、velocity-obstacle（VO）action masking 和 targeted domain randomization 结合，用于拥挤水域的闭环航行。作者在两个 2 km × 2 km 模拟场景中相对 VO/COLREG reward-shaping baselines 报告更快训练、更高成功和更少 unsafe actions，并展示纯模拟训练 policy 在 17 吨无人船上的零样本试航。该结果是受控真实场景的积极证据，不是 COLREG 合规证明、航海认证、全气象可靠性或无人值守商业航行许可。

## 方法与证据

- Sim2Sea simulator 支持 MMG/Nomoto 等船舶模型、海况/传感器建模、GPU 并行与 continuous-time collision detection（§2, §4）。模拟真实性仍是模型假设：水流、风浪、船体/推进器误差、地图、动态目标行为和 sensor delay/noise 的未建模部分会直接影响 sim-to-real transfer。
- policy 以时序状态流和 Bird’s-Eye-View spatial input 双路编码；Transformer 用于处理惯性与历史，BEV 表示环境几何/邻船信息（§1, §4）。该输入依赖 GNSS、AIS、radar/camera/chart 等 sensing 在时间/坐标上可靠对齐；AIS 只覆盖 cooperative targets，视觉/雷达漏检、欺骗或遮挡并未由网络自动解决。
- action masking 用 VO 排除预测碰撞动作，训练仍使用 PPO；目标还包括到达、进展、碰撞/越界等 reward（§4）。VO 是基于相对速度和几何预测的安全先验，不能代表复杂 COLREG 判断、优先权、通信、人的不确定意图、浅水/系泊/漂浮物、极端操纵能力或多船非合作互动。
- targeted domain randomization 改动动力学、传感与环境变量以缩小 sim-to-real gap（§4）。randomization 增加指定扰动下的鲁棒性，并不覆盖真实分布外天气、设备故障、网络延迟、GNSS denial、海图错误或对手策略性行为。
- 仿真比较在 Mini Coastline 和 Mini Port 两个拥挤地图进行，均为 2000 m × 2000 m；episode 在到达、CCD 碰撞或步数上限终止，步数上限分别 600/750（§5）。baselines 为 VO-RL、COLREG-RL 和 classical VO controller；所有方法共享 simulator/observation/action setting，十次 rollout 报 success rate、episode length、unsafe actions（Table 1–2）。这支持同一实验栈内的相对比较，不等于对其他船型、港口、能见度或 traffic mix 的普遍优势。
- 论文称 full parallelization 在 A100 上相对最慢实施有明显加速（Table 1），并在两场景中获得较高成功率和较低 unsafe-action rate；ablation 移除 action mask、BEV 或 temporal sequence 后更差（§5, Figs. 3–4）。unsafe actions 是作者定义的代理指标，不能替代 collision probability、closest-point-of-approach 分布、法规判定或人员/环境损害评估。
- 真实部署为 17-ton unmanned vessel，使用 GNSS、AIS、marine radar 与相机，控制 loop 1 Hz、固定 speed 10 knots，且有 manual/autonomous mode switching、状态/图表界面与 live camera safety display（§5）。作者展示 Mini Coastline/Mini Port 对齐后的 zero-shot trials，以及无 randomization/无 temporal input 的失败可视化（Fig. 6）。论文没有报告试验数量、系统化 weather/traffic 覆盖、独立安全审查、近失事件统计或监管授权。
- 结论只称 collision-free、smooth、goal-oriented navigation，并将进一步 real-world deployment scenarios 列为未来工作（§6）。因此实船演示不应被表述为可在开放海域无监督连续运行的证明。

## 适用边界与复现

- 适用于研究型 maritime autonomy 的仿真训练、受监督试航和 sim-to-real ablation。任何实船航行应先在封闭/受控水域做 hazard analysis、系统识别、软件/硬件-in-the-loop 与渐进式 ODD 扩展，并保留合格船员/远程操作者的随时接管权。
- 不应以 learned VO mask 作为 sole safety layer。需要独立 runtime safety monitor、经验证的操纵/制动 envelope、geofence、通信失效与定位失效 fallback、冗余 sensing、目标追踪置信度、COLREG/当地海事规则审查、记录回放、碰撞与近失阈值，以及暂停/返航策略。
- 复现需固定船体动力学、action discretization、reward、VO/CCD 实现、BEV/temporal window、PPO 超参数、domain-randomization ranges、两张地图和 traffic initialization；报告多 seed 的 success、collision/near-miss、unsafe actions、route/energy、训练吞吐和完整 ablation。实船复现还需公开 ODD、硬件延迟/校准、操作监督和原始 trial logs，论文并未提供这些即充分证明。
- 应扩展至恶劣天气/昼夜/低能见度、非 AIS/非合作目标、传感器/推进器/通信故障、密集多船协调、不同船型速度、实际 COLREG adjudication、cybersecurity、long-horizon maintenance 与独立第三方安全评估。

## 与 AAMAS 的关系与核验说明

这是 AAMAS embodied maritime navigation 的 sim-to-real 应用工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CMRP6518.pdf) 核对 simulator、dual-stream policy、VO mask、domain randomization、两场景/终止协议/baselines、A100 吞吐、17-ton hardware 与 1 Hz/10-knot real trials及作者未来工作；没有把受控 zero-shot 试航、VO proxy 或 reward 结果误写成广泛 COLREG 合规、碰撞零风险或监管批准。
