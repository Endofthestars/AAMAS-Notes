---
title: "Surrogate-Augmented Deception in Reinforcement Learning (SAD-RL)"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/KOTB1262"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KOTB1262.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["static_adversary_assumption", "shallow_surrogate_scope", "simulation_only", "strategic_opacity_tradeoff", "interpretability_reduction", "dual_use_adversarial_behavior", "no_real_world_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Surrogate-Augmented Deception in Reinforcement Learning (SAD-RL)

## 一句话总结

SAD-RL 在标准 RL 回报中加入 surrogate 对策略动作预测得越准、惩罚越大的项，使策略在完成任务的同时更难被指定的可解释模型模仿。论文在离散 Adversarial Grid World 与连续 Sharks-and-Minnows 中发现中等权重可平衡胜率与低 surrogate fidelity；这是针对静态浅层 surrogate 的仿真抗建模训练，不等价于已能欺骗真实、适应性对手。

## 方法与证据

- 每个 episode 后训练 surrogate 拟合收集的 state-action pairs，并以 \(R_{final}=R_{task}-\lambda A_\epsilon\) 修改训练信号；\(A_\epsilon\) 是 surrogate 在 \(\epsilon\)-容忍动作误差内的预测准确率。\(\lambda\) 控制任务绩效与 opacity 的权衡（§3.1--§3.3）。
- threat model 特意设为 static observer：对手用近期 episode 训练 surrogate 但不在训练期间共同适应。该设置隔离 surrogate pressure，却不覆盖在线学习、模型集成、神经预测器、直接观测 policy 参数或主动试探的强对手（§3.2、§5）。
- AGW 中 surrogate 是深度最多 3 的 entropy decision tree；SaM 中为深度最多 7 的 regression tree，连续动作容忍度 \(\epsilon=0.5\)。这将“deception”定义为对这些特定树模型的低 fidelity，而非任何形式的意图误导或安全鲁棒性（§3.3--§3.5）。
- 结果图显示随 \(\lambda\) 增大 surrogate accuracy 下降而任务性能存在 trade-off；AGW 的 \(\lambda=0.50\) 和 SaM 的中等 \(\lambda\) 常位于“高成功/高 deception”区域，高权重会出现 deceptive 但性能差的 over-deception（§4）。
- 作者控制 action entropy 后报告 partial Spearman \(\rho=0.017,p>0.8\)，并以注入 Gaussian noise 的 baseline 比较，认为低 fidelity 不只是随机噪声；但这只是在所用环境与度量中支持 goal-directed opacity，不证明对手实际被误导（§4.3--§4.4）。
- 限制明确包括静态 adversaries、刻意浅的 surrogates、缺少 adaptive opponent/多智能体共同演化和多样 surrogate 比较；代码与训练模型已列出（§5--§6）。

## 适用边界与复现

- 可用于竞争式仿真中研究 policy extractability、模型盗用抵抗或策略可预测性的可控 trade-off；使用前需明确“难解释”是否真是系统目标。
- 不应在需要审计、可解释、合规或人机协作的安全关键系统中默认启用：故意压低可解释 surrogate fidelity 会削弱监控、调试、责任追踪与使用者信任，且可产生不可预期策略。
- 复现应固定 AGW/SaM 环境、RL 算法/网络/seed、surrogate 类型和最大深度、\(\epsilon\)、episode 训练时序、\(\lambda\) 网格、curriculum、成功率/accuracy/entropy 统计和噪声基线；再用未参与训练的强预测器测试跨模型 transfer。
- 对防御性应用，应将其限制于沙箱红队评估，增加对自适应黑盒/白盒攻击的测试、任务安全约束、可验证日志和独立可解释性审计；不得将“抗 surrogate”误作为对人类或现实安全攻击的认证。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的对抗性 RL、对手建模与可解释性反向利用论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/KOTB1262.pdf) 核验 SAD-RL reward、树 surrogate、AGW/SaM、\(\lambda\) trade-off、entropy/noise 分析与作者限制；没有把 surrogate 低 fidelity 误称为对真实对手的通用欺骗成功。
