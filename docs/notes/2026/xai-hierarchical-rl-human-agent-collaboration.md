---
title: "Evaluating XAI Support From A Hierarchical Reinforcement Learning Policy in Human-Agent Collaboration"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["human_agent_interaction", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/HDMG2174"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HDMG2174.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "human_subjects_study", "underpowered_exploratory_results", "gaming_experienced_sample", "explanation_action_mismatch"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Evaluating XAI Support From A Hierarchical Reinforcement Learning Policy in Human-Agent Collaboration

## 一句话总结

本文以 Overcooked-AI Counter-Circuit 的 HA2 hierarchical policy 为解释来源：Manager 每步选择 12 个可读 subtask，trigger system 仅在协调相关时刻以文字或语音说明当前 subtask。between-subjects study（最终 \(n=38\)）没有发现 explanations 对峰值表现、NASA-TLX 或协作量表的显著效益；音频有较快但不显著的适应趋势。它说明这种实时 explanation delivery 可被实验评估，并不证明 XAI 改善人机协作、信任或决策质量。

## 方法与证据

- HA2 使用原 Worker policies 和经 PPO self-play 训练的 Manager；Manager 每 timestep 从 12 个 domain-specific subtasks 中选一项，Worker 执行 primitive actions（§2）。解释取自 policy 的 high-level selection，因此比 post-hoc 更接近实际内部决策，但并不保证该 subtask 对每一低层动作、未来行为或人类可理解的“意图”忠实；作者也观察到 Manager mid-execution subtask switch 可使陈述与动作失配。
- pilot 显示连续解释会压倒用户，故 trigger 只在 Blocking、Critical Path、Distance Threshold 或 Subtask Change 时触发，6 秒 cooldown；文字显示 4 秒，音频用 browser-native speech synthesis（§2）。这种 filtering 改变了信息量和时机，不能分离“模态”与 salience/频率/注意力的效应，也没有验证人是否理解每条解释。
- between-subjects 有 Control/Text/Audio；每人四个 80-second sessions，后测 NASA-TLX、Godspeed、Human-Agent Fluency。IRB 批准后从 academic convenience sample 招 41，剔除后 \(n=38\)：Control 14、Text 14、Audio 10；92% gaming familiarity ≥6/10，post-hoc sensitivity 显示对 observed medium effects underpowered（§2）。样本小、不均衡且高度熟练，不能推广到新手、不同语言/无障碍群体或现实协作场景。
- 对 gaming-experienced participants，Control score \(125.00\pm18.19\) vs explanations \(114.17\pm22.59\)，\(p=.136,d=-.51\)；Text vs Audio \(p=.745,d=.14\)。所有 workload/subjective measures在 Bonferroni 后不显著。Audio/Text/Control learning slopes 11.20/8.00/5.39 points/session，\(F(2,34)=1.51,p=.236\)，作者称探索性 medium pattern（§3）。这些数值不支持 performance/信任/负荷改善的结论。

## 适用边界与复现

- 适合研究 hierarchical policy 的实时解释呈现及其人因评估；不应把 subtask status text/audio 用作高风险系统的意图、原因、保证或安全说明。解释若与动作不一致，反而可能误导协调和过度信任。
- 复现需给 HA2/Manager/Workers weights 与 training、Counter-Circuit layout、12 subtask schema、trigger priorities/cooldown/templates、speech synthesis/browser、UI、随机分配和排除、instruction checks、sessions/questionnaires、预注册统计/多重检验和匿名化数据。应报告每条件完整 trials、individual trajectories、缺失数据和每项效应/CI。
- 后续应使用充足样本、预注册、不同经验/语言/可访问性人群、多 layout/更长协作及实际团队任务；测量 explanation fidelity、理解/mental model、attention、calibration、recovery from policy changes和长期信任。比较同内容不同频率/视觉显著性，避免将“听到更多”误归因于音频本身。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 human-agent teaming、XAI 与 HRL 扩展摘要。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HDMG2174.pdf) 核验 HA2、trigger system、\(n=38\)、条件/量表及 §3 统计；没有把不显著的探索性趋势写成 XAI 的人因或协作收益。
