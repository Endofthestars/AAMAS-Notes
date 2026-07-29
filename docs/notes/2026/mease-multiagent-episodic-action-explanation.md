---
title: "MEASE: Multi-agent Episodic Action Sequence Explanation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "human_agent_interaction"]
dblp_key: ""
doi: "10.65109/OUUG8445"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OUUG8445.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["post_hoc_explanation_scope", "trajectory_distribution_dependence", "action_only_abstraction", "scripted_replay_fidelity", "small_user_study", "no_causal_fidelity_test", "environment_scope"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# MEASE: Multi-agent Episodic Action Sequence Explanation

## 一句话总结

MEASE 从已训练 MARL policy 的完整联合轨迹中用 EM-ART 2 学习事件/episode 记忆，再以区间检索和 MASA 把多个代理重复的动作序列压缩为符号化协作策略。其在 MOSMAC 4t1sp 的脚本复演接近原 QMIX，但解释是对既有行为数据的后验抽象，未证明状态因果、反事实可靠性或跨环境通用解释能力。

## 方法与证据

- EM-ART 2 将多代理联合行为编码为可检索的 episodic memory；interval retrieval 以 abstraction factor \(\phi\) 分段，MASA 保留每段中至少 \(M\) 个代理共同执行的动作，并合并连续重复事件。论文称这种两阶段压缩通常减少单条 episode 的 90--95% 内容（§5）。
- 数据来自收敛后冻结的 QMIX policies（EPyMARL）：VMAS Joint Passage/Balance 与 MOSMAC 4t1sp/4t8sp，每个场景 1,000 条完整轨迹；MOSMAC 训练门槛为 >90% success，VMAS 为稳定高回报（§6.1）。解释质量因此紧密依赖同一策略、默认环境配置和轨迹覆盖。
- Table 3：Balance 的 99,964 raw events 形成 3,883 个 \(F2\) event patterns 和 59 个 \(F3\) episode strategies；4t1sp 为 37,647/8,012/48，4t8sp 为 44,500/17,608/58。较少的 \(F3\) code 是模式压缩，不本身证明人类可理解或完整涵盖策略状态。
- “explanation-as-strategy”仅在 MOSMAC 4t1sp 中将抽象动作脚本直接执行，十次、每次 1,000 episodes：MEASE AE win rate \(93.2\pm1.1\%\)、reward \(19.59\pm0.07\)，QMIX 为 \(93.7\pm3.4\%\)、\(19.53\pm0.31\)；删除关键片段后 AE-4/AE-8/AE-0 分别降至 88.1%/69.9%/19.8%（Table 7）。这是固定环境的行为保真度证据，不是逐状态或反事实因果忠实度。
- 31 名参与者各观看 10 个 MOSMAC episode（4t1sp/4t8sp 各 5），先无解释后看同一序列加解释，采用 5 点 Likert。4t1sp clarity/usefulness/satisfaction 中位数为 3.9/3.8/3.8；4t8sp 为 4.0/3.9/3.8（§8.4）。样本小、无随机对照顺序或外部任务表现指标，主观接受度不等于准确理解或信任校准。

## 适用边界与复现

- 适用于离线审阅离散动作、协作结构明显的 MARL 轨迹，帮助研究者概括共同移动、分散、攻击等重复协作模式；适合做事后诊断而非在线安全监控的唯一依据。
- MASA 主要解释行动序列并按代理共同行为筛选，未纳入完整状态属性、观察误差、价值函数或未发生动作的反事实；同一动作可因不同状态而有不同意义，抽象解释可能遗漏个体关键动作。
- 论文的性能复演只报告 4t1sp，不能推出对 VMAS、4t8sp、其他算法、连续控制、异质代理或真实系统同样保真；script replay 也绕开了原 policy 的实时状态反馈与恢复行为。
- 复现应固定 QMIX/EPyMARL/MOSMAC/VMAS 版本、训练 seeds 与收敛准则、1,000-trajectory 数据收集、EM-ART vigilance \(\rho_s=0.25,\rho_e=1.0\)、\(\phi=10\)、\(M=2\)、检索/压缩实现和脚本执行器；报告多场景 replay success、状态扰动/反事实删除、解释覆盖/稳定性和完整人类研究协议。
- 高风险系统中，解释应与独立日志、状态约束、仿真回放和人工审查交叉验证。清晰的文字/符号摘要不能替代对策略安全性、偏差或责任链的审计。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的可解释多智能体强化学习与协作行为抽象论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OUUG8445.pdf) 核验 EM-ART/MASA、数据收集、Table 3/7 与用户研究；没有把后验轨迹摘要或主观评分误称为对策略内部因果机制的完整解释。
