---
title: "Beyond Vibe Decision Theory: Asymmetric Manipulation Vulnerabilities in LLM Multi-Agent Coordination"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["generative_agents", "safety_verification", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/CSLO7280"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CSLO7280.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["prompt_framing_manipulation", "synthetic_game_scope", "short_horizon_evaluation", "model_version_drift", "non_independent_api_trials", "no_real_world_validation", "alignment_inference_limit", "multi_agent_coordination_risk"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Beyond Vibe Decision Theory: Asymmetric Manipulation Vulnerabilities in LLM Multi-Agent Coordination

## 一句话总结

论文用互相冲突的叙事 framing 与显式策略建议，测试 LLM 双智能体在囚徒困境、性别之战和连续公共物品博弈中的协调稳定性。8 个模型家族在每一 game–frame–advice 条件下进行 30 个独立 trial、每个 trial 10 轮、temperature 0；公共物品博弈最突出：在合作叙事中加入竞争建议会令多模型贡献下降 61–96 个百分点，而在竞争叙事中加入合作建议只提高约 33–52 点。结果揭示提示冲突可造成不对称操控风险，但不证明模型“偏好”或真实系统会以同样方式失效：测试是短期、对称同模型、规范化博弈的文本提示，未覆盖真实资源约束、长期学习、身份差异、工具调用或人类监管。

## 方法与证据

- 采用 \(2\times2\) factorial：contextual framing 为 cooperative/competitive，strategic advice 为 baseline/与 framing 冲突的建议（§3.1）。叙事是多段文本而非简单标签；因此测量的是该具体 prompt 族中的反应，不是对任意“合作/竞争”语言的因果总效应。
- 评测囚徒困境（互相合作 \((3,3)\)，背叛严格占优）、性别之战（两个非对称 pure Nash、需协调）和两人连续公共物品博弈；后者令 \(c_i\in[0,10]\)，贡献成本 1、回报系数 \(\alpha=0.5\)，零贡献是 Nash 而完全贡献最大化 welfare（§3.2）。公共物品的连续决策和重复轮次使 framing 影响可通过预期累积，不等同于离散、一次性选择。
- 覆盖 GPT-4、GPT-4o、GPT-5、Llama-3.3-70B、Llama-3.1-70B、Gemma-27B、Gemini Flash、Gemini Pro；temperature 0、max tokens 512。同一模型的两个实例接收相同 prompt，仅实验因素不同；每条件 30 trial、每 trial 10 轮（§3.3）。这隔离了异构模型不对称，却未验证供应商版本漂移、API 确定性/独立性或现实多模型网络的传播效应。
- primary metric 是 10 轮中互利协调结果的 coordination rate：PD 为 \((C,C)\)，BoS 为任一协调 equilibrium，公共物品则双方贡献高于 socially optimal threshold；另报告相对 baseline 的方向性操控量和其标准差归一化的 asymmetry ratio（§3.4）。这些是行为代理指标，不能直接解释为内在信念、忠诚度或安全保证。
- 公共物品中，合作 framing 被竞争建议打断时，多数模型贡献下降 43–96 点，其中四个模型下降超过 60%；反向在竞争 framing 中给合作建议通常提升 7–52 点，6/8 在 33–52 点之间（§4.1）。这显示方向性不对称：既有合作默认比竞争默认更容易崩塌，而非说明合作建议总是无效。
- PD 的模式按架构分化：作者报告 GPT-5 的合作 baseline 约 95–100%，操控下变化约 \(\pm4\) 点；Llama 在竞争到合作方向可增 79–93 点、其原始合作基线仅 6–18%，Gemini 的高合作 baseline 在冲突建议下又会显著下降（§4.2）。模型/游戏的相互作用意味着不能仅按“GPT、开源或对齐方法”类别预测鲁棒性。
- BoS 的变化通常更小、更均匀（文中概述为低于 45 点）；论文将其归因于可观察的 matching action 降低了 belief-channel 的作用（§5.1）。这是对该游戏实现的机制解释，而不是已被中介分析或反事实测量证明的因果机制。
- 限制明确包括仅 10 轮、只为短期协调快照；更长时域可能出现适应或级联，现实交易/资源分配/车辆协调及人在环验证仍缺失，并需要更多架构、语言/文化 context 与 adversarial fine-tuning 测试（§5.5）。

## 适用边界与复现

- 适用于将其作为 LLM 多智能体 prompt-conflict red-team 基准：在部署前检测“既定叙事/角色与显式行动建议冲突”时，协调结果是否剧变，尤其应加入连续贡献、重复互动与集体福利目标。
- 不应据此选择某一模型处理真实交易、公共资金、基础设施或谈判，也不应把游戏中的 cooperation rate 当作该模型的整体 alignment 分数。高风险环境需单独审计 prompt provenance、角色/建议分离、权限、工具调用、对手策略、长期效应与人工升级。
- 复现需版本锁定所有 API/model、保存完整 narrative/advice prompts、game payoff/阈值和轮数、temperature/max tokens、数值输出 parser、trial seeds/时间戳及失败重试；报告每条件 30 个完整轨迹、raw coordination/contribution、方差、effect size、预注册显著性检验和多重比较处理。
- 缓解上应对 frame–advice conflict 做输入/策略层检测和分流；让 agent 显式抽取 payoff、检查建议与目标是否冲突、在高影响 action 前请求澄清/人工复核。要测试 prompt injection、串联 agent、异质模型、人类参与、长时程和任务特定安全约束，不能只依赖内容过滤。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 LLM multi-agent coordination、game theory 与对齐鲁棒性工作。笔记基于扫描版 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CSLO7280.pdf) 逐页核验了实验因子、三类博弈、八模型、30×10 试验协议、公共物品的不对称幅度及作者的短时域/现实验证限制；没有将提示行为结果表述为真实部署攻击成功率、模型心理状态或通用安全结论。
