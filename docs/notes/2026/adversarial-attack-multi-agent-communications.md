---
title: "Finding the Weakest Link: Adversarial Attack against Multi-Agent Communications"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "marl_coordination", "agent_engineering"]
dblp_key: ""
doi: "10.65109/GION7107"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GION7107.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02t"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["white_box_attack_assumption", "q_learning_scope", "simulated_benchmark_only", "attack_not_defense", "extended_abstract_only"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Finding the Weakest Link: Adversarial Attack against Multi-Agent Communications

## 一句话总结

论文为 communicative MARL 的鲁棒性评测提出 single-victim message perturbation 攻击：以 Jacobian proxy 选择敏感受害者、消息和时刻，并用最大/加权损失替代单纯“改动作”的 untargeted loss，以平衡攻击影响与成功概率。在导航、PredatorPrey 与 TrafficJunction 的 30 个设定中，方法在一半场景最强、在其获胜场景相对基线平均提升 42%；它假定白盒访问和训练良好的 Q-learning agent，应作为防御测试的强攻击威胁模型，而非真实系统失效概率或可部署的攻击指南。

## 方法与证据

- SVCP-APOSG 在 DEC-POMDP-Comms 环境元素外增加消息置换、攻击节奏、\(L_2\) 幅度、受害者选择、消息选择和被扰消息数等六项攻击变量；目标是提高损害同时降低幅度、次数和可察觉性（§1--2）。
- 假设白盒且 agent 的 Q-function 已训练良好。Jacobian proxy 取损失对接收消息各元素梯度绝对值之和，按 top-\(k\) 选择消息；选择 top-\(k\) 总 proxy 最大的 agent 为 victim，并以阈值决定攻击时刻（§2）。
- maximum loss 诱导原本 Q 值差距最大的劣动作以获得更大影响但可能更难成功；weighted loss 按 action 的 Q-difference 加权，以折衷成功率/影响。二者与 untargeted loss 比较（§2）。
- 在简单 grid navigation、两种 PredatorPrey、两种 TrafficJunction，以及 full-observation sharing 与 RIAL 两类通信下，对比多种 tempo、随机消息选择和 untargeted loss。Jacobian-proxy 在 30 个场景的一半最优，获胜时较基线均值提升 42%；复杂环境、高 attack rate、OBS 下通常更有效，但并非各系统通胜，orthogonal PredatorPrey 例外，部分被攻击系统甚至胜过未攻击系统（§2）。

## 适用边界与复现

- 适合在授权的模拟/红队环境中评测消息通道的最坏情形脆弱性；白盒梯度、可拦截/修改消息、训练充分和 Q-learning 假设未必在生产或物理系统成立。
- episode cumulative reward 是单一损害指标，不能覆盖安全约束、隐蔽性检测率、通信开销、恢复行为或长期社会影响。攻击成功也不证明特定真实协议或系统必然可被攻破。
- 作者自身观察到“训练良好”假设可能不成立；结果受网络、seed、攻击 budget/tempo 阈值、通信编码、baseline 实现和环境动力学影响，30 个 benchmark 不能建立通用排序。
- 防御复现应在隔离环境中版本化模型/通信/攻击 budget，报告每 seed 的收益损失、扰动范数、攻击率、检测率和置信区间；同时测试认证、鲁棒训练、消息过滤/冗余、随机化与黑盒/部分信息威胁模型。任何真实系统测试须经授权并采用安全控制。

## 与 AAMAS 的关系与核验说明

该文面向多智能体通信的对抗鲁棒性评估。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/GION7107.pdf) 人工核对 SVCP-APOSG、Jacobian 选择、两种损失、五类环境/两种通信和 30 场景结论；没有提供可用于未授权目标的操作细节，也未将攻击实验写成现实系统风险量化。
